// Réseau : l'hôte fait tourner la simulation, les invités envoient leurs commandes (WebRTC via PeerJS).
// Paramètres d'URL pour les tests : ?peerHost=localhost&peerPort=9000&peerPath=/&peerSecure=0

import { CONFIG } from './config.js';
import { generatePartyCode, isValidPartyCode, normalizePartyCode, sanitizeCustom } from './logic.js';

function peerOptions() {
  const q = new URLSearchParams(location.search);
  const opts = { debug: 0 };
  if (q.get('peerHost')) {
    opts.host = q.get('peerHost');
    opts.port = Number(q.get('peerPort') || 9000);
    opts.path = q.get('peerPath') || '/';
    opts.secure = q.get('peerSecure') === '1';
  }
  return opts;
}

function PeerCtor() {
  if (typeof window.Peer !== 'function') throw new Error('PeerJS indisponible');
  return window.Peer;
}

const ID_PREFIX = 'm13-';

// ------------------------------------------------------------------ Hôte
export class HostNet {
  constructor(game, hostCharacter, hooks) {
    this.game = game;
    this.hooks = hooks; // { onStatus(text), onRoster() }
    this.conns = new Map(); // playerId -> DataConnection
    this.hostCharacter = hostCharacter;
    this.code = null;
    this.snapAcc = 0;
  }

  open(tries = 5) {
    return new Promise((resolve, reject) => {
      const attempt = (left) => {
        const code = generatePartyCode();
        let peer;
        try {
          peer = new (PeerCtor())(ID_PREFIX + code, peerOptions());
        } catch (e) {
          reject(e);
          return;
        }
        peer.on('open', () => {
          this.peer = peer;
          this.code = code;
          peer.on('connection', (conn) => this.onConnection(conn));
          peer.on('error', (err) => this.hooks.onStatus?.('Réseau : ' + (err.type || err.message)));
          resolve(code);
        });
        peer.on('error', (err) => {
          if (!this.peer) {
            peer.destroy();
            if (err.type === 'unavailable-id' && left > 0) attempt(left - 1);
            else reject(err);
          }
        });
      };
      attempt(tries);
    });
  }

  onConnection(conn) {
    let playerId = null;
    conn.on('data', (msg) => {
      if (!msg || typeof msg !== 'object') return;
      if (msg.t === 'join') {
        if (playerId) return;
        const res = sanitizeCustom(msg.character);
        if (!res.ok) return conn.send({ t: 'reject', reason: res.error });
        if (this.game.players.size >= CONFIG.maxPartySize) return conn.send({ t: 'reject', reason: 'Le groupe est complet.' });
        const id = 'g' + Math.random().toString(36).slice(2, 8);
        this.game.addPlayer(id, res.character);
        playerId = id;
        this.conns.set(id, conn);
        conn.send({ t: 'welcome', id });
        this.hooks.onRoster?.();
        return;
      }
      if (!playerId) return;
      const g = this.game;
      if (msg.t === 'input') g.setInput(playerId, Number(msg.mx) || 0, Number(msg.mz) || 0);
      else if (msg.t === 'attack') g.attack(playerId);
      else if (msg.t === 'power') g.usePower(playerId);
      else if (msg.t === 'interact') g.interact(playerId);
      else if (msg.t === 'effect' && typeof msg.name === 'string') g.effect(playerId, msg.name);
    });
    const drop = () => {
      if (playerId) {
        this.game.removePlayer(playerId);
        this.conns.delete(playerId);
        this.hooks.onRoster?.();
        playerId = null;
      }
    };
    conn.on('close', drop);
    conn.on('error', drop);
  }

  // Appelé à chaque pas de simulation avec les événements produits.
  broadcast(dt, events) {
    if (events.length) {
      for (const [id, conn] of this.conns) {
        const mine = events.filter((e) => e.t !== 'dialogue' || e.to === null || e.to === id);
        if (mine.length && conn.open) conn.send({ t: 'ev', e: mine });
      }
    }
    this.snapAcc += dt;
    if (this.snapAcc >= 1 / CONFIG.snapshotRate) {
      this.snapAcc = 0;
      const s = this.game.snapshot();
      for (const conn of this.conns.values()) if (conn.open) conn.send({ t: 'snap', s });
    }
  }

  close() {
    try {
      this.peer?.destroy();
    } catch {}
  }
}

// ------------------------------------------------------------------ Invité
export class GuestNet {
  constructor(hooks) {
    this.hooks = hooks; // { onSnap(s), onEvents(list), onWelcome(id), onReject(reason), onClose() }
    this.id = null;
  }

  connect(rawCode, character) {
    const code = normalizePartyCode(rawCode);
    if (!isValidPartyCode(code)) return Promise.reject(new Error('Code invalide (4 caractères).'));
    return new Promise((resolve, reject) => {
      let peer;
      try {
        peer = new (PeerCtor())(undefined, peerOptions());
      } catch (e) {
        reject(e);
        return;
      }
      this.peer = peer;
      const timer = setTimeout(() => {
        reject(new Error('Groupe introuvable. Vérifie le code.'));
        peer.destroy();
      }, 12000);
      peer.on('error', (err) => {
        clearTimeout(timer);
        reject(new Error(err.type === 'peer-unavailable' ? 'Groupe introuvable. Vérifie le code.' : 'Réseau : ' + (err.type || err.message)));
      });
      peer.on('open', () => {
        const conn = peer.connect(ID_PREFIX + code, { reliable: true });
        this.conn = conn;
        conn.on('open', () => conn.send({ t: 'join', character }));
        conn.on('data', (msg) => {
          if (!msg) return;
          if (msg.t === 'welcome') {
            clearTimeout(timer);
            this.id = msg.id;
            this.hooks.onWelcome?.(msg.id);
            resolve(msg.id);
          } else if (msg.t === 'reject') {
            clearTimeout(timer);
            reject(new Error(msg.reason || 'Refusé.'));
          } else if (msg.t === 'snap') this.hooks.onSnap?.(msg.s);
          else if (msg.t === 'ev') this.hooks.onEvents?.(msg.e);
        });
        conn.on('close', () => this.hooks.onClose?.());
      });
    });
  }

  send(msg) {
    if (this.conn?.open) this.conn.send(msg);
  }

  close() {
    try {
      this.peer?.destroy();
    } catch {}
  }
}
