// Simulation du jeu (pure, sans navigateur). L'hôte (ou le solo) fait tourner cette simulation.
// Plan 2D sur (x, z). Trois scènes : miel (Luynes), nonlieu (couloir), kayden (arène).

import { CONFIG as C } from './config.js';
import * as L from './logic.js';

export const INTERACT_RANGE = 4.5;
const DOOR_COUNT = 10;

export function sceneBounds(scene) {
  if (scene === 'miel') return { minX: -25, maxX: 25, minZ: -25, maxZ: 25 };
  if (scene === 'nonlieu') return { minX: -7, maxX: 7, minZ: -150, maxZ: 6 };
  return { radius: 30 };
}

export function clampPos(scene, x, z) {
  const b = sceneBounds(scene);
  if (b.radius) {
    const d = Math.hypot(x, z);
    if (d > b.radius) return [(x / d) * b.radius, (z / d) * b.radius];
    return [x, z];
  }
  return [Math.min(Math.max(x, b.minX), b.maxX), Math.min(Math.max(z, b.minZ), b.maxZ)];
}

export function spawnPoint(scene, index = 0) {
  const base = scene === 'miel' ? [0, 12] : scene === 'nonlieu' ? [0, 0] : [0, 22];
  return [base[0] + (index % 2 === 0 ? 1 : -1) * Math.ceil(index / 2) * 1.5, base[1]];
}

const r2 = (n) => Math.round(n * 100) / 100;
const dist = (a, b) => Math.hypot(a.x - b.x, a.z - b.z);

export class Game {
  constructor({ rng = Math.random, solo = true } = {}) {
    this.rng = rng;
    this.solo = solo;
    this.time = 0;
    this.scene = 'miel';
    this.players = new Map();
    this.enemies = [];
    this.holes = [];
    this.doors = [];
    this.instability = 0;
    this.finished = false;
    this.nextId = 1;
    this.events = [];
    this.pending = null;
    this.waveTimer = C.waves.interval;
    this.glitchTimer = 0;
    this.slam = null;
    this.bossMid = false;
    this.hostId = null;
    this.startScene('miel');
  }

  // ------------------------------------------------------------ Événements
  emit(e) {
    this.events.push(e);
  }
  drainEvents() {
    const out = this.events;
    this.events = [];
    return out;
  }
  say(node, to = null) {
    this.emit({ t: 'dialogue', node, to });
  }

  // ------------------------------------------------------------ Joueurs
  addPlayer(id, character) {
    if (this.players.size >= C.maxPartySize) return false;
    if (this.players.has(id)) return false;
    if (this.hostId === null) this.hostId = id;
    const [x, z] = spawnPoint(this.scene, this.players.size);
    this.players.set(id, {
      id,
      name: character.name,
      power: character.power,
      colorIndex: character.colorIndex,
      canon: character.canon || null,
      x, z,
      health: C.player.health,
      maxHealth: C.player.health,
      alive: true,
      respawn: 0,
      attackCd: 0,
      powerCd: 0,
      shield: 0,
      shieldT: 0,
      stored: 0,
      storedT: 0,
      deflect: 0,
      holeCd: 0,
      input: { mx: 0, mz: 0 },
    });
    return true;
  }

  removePlayer(id) {
    this.players.delete(id);
    if (this.hostId === id) this.hostId = this.players.keys().next().value ?? null;
  }

  setInput(id, mx, mz) {
    const p = this.players.get(id);
    if (!p) return;
    const len = Math.hypot(mx, mz);
    if (!(len > 0) || !isFinite(len)) {
      p.input = { mx: 0, mz: 0 };
      return;
    }
    const k = Math.min(len, 1) / len;
    p.input = { mx: mx * k, mz: mz * k };
  }

  alivePlayers() {
    return [...this.players.values()].filter((p) => p.alive);
  }

  // ------------------------------------------------------------ Scènes
  startScene(scene) {
    this.scene = scene;
    this.enemies = [];
    this.holes = [];
    this.slam = null;
    this.waveTimer = C.waves.interval;
    this.bossMid = false;
    if (scene === 'nonlieu') {
      this.buildDoors();
      this.instability = Math.min(this.instability, 20);
    }
    if (scene === 'kayden') {
      const n = Math.max(1, this.players.size);
      const hp = C.boss.baseHealth + C.boss.perExtraPlayer * (n - 1);
      this.enemies.push({ id: this.nextId++, kind: 'boss', x: 0, z: -8, hp, maxHp: hp, cd: 3, summonT: 8, phase: 1 });
    }
    let i = 0;
    for (const p of this.players.values()) {
      const [x, z] = spawnPoint(scene, i++);
      p.x = x;
      p.z = z;
      p.alive = true;
      p.health = p.maxHealth;
      p.shield = 0;
      p.stored = 0;
      p.deflect = 0;
    }
    this.emit({ t: 'scene', scene });
    if (scene === 'miel') {
      this.say('narr_pluie');
    } else if (scene === 'nonlieu') {
      this.say('nonlieu_intro');
    } else {
      this.say('kayden_intro');
    }
  }

  buildDoors() {
    const real = Math.floor(this.rng() * DOOR_COUNT);
    const used = new Set([41]);
    this.doors = [];
    for (let i = 0; i < DOOR_COUNT; i++) {
      let label = 41;
      if (i !== real) {
        do label = 1 + Math.floor(this.rng() * 99);
        while (used.has(label));
        used.add(label);
      }
      this.doors.push({ id: i, x: i % 2 === 0 ? -7 : 7, z: -14 * (i + 1), label, real: i === real, used: false });
    }
  }

  interactables() {
    if (this.scene === 'miel') {
      return [
        { id: 'clara', x: -8, z: -2, kind: 'npc', node: 'clara_1' },
        { id: 'alex', x: 8, z: -2, kind: 'npc', node: 'alex_1' },
        { id: 'machine', x: 0, z: -10, kind: 'npc', node: 'machine_label' },
      ];
    }
    if (this.scene === 'nonlieu') {
      return this.doors.map((d) => ({ id: 'door' + d.id, x: d.x, z: d.z, kind: 'door', door: d }));
    }
    return [];
  }

  nearestInteractable(p) {
    let best = null;
    let bestD = INTERACT_RANGE;
    for (const it of this.interactables()) {
      const d = Math.hypot(it.x - p.x, it.z - p.z);
      if (d <= bestD) {
        best = it;
        bestD = d;
      }
    }
    return best;
  }

  // ------------------------------------------------------------ Actions
  interact(id) {
    const p = this.players.get(id);
    if (!p || !p.alive || this.pending) return false;
    const it = this.nearestInteractable(p);
    if (!it) return false;
    if (it.kind === 'npc') {
      this.say(it.node, id);
      return true;
    }
    const door = it.door;
    if (door.real) {
      this.say('door_41');
      this.pending = { scene: 'kayden', in: 2 };
    } else {
      this.addInstability(15);
      this.say('door_wrong', id);
      this.spawnSilhouettes(2, p);
    }
    return true;
  }

  // Effet déclenché par un choix de dialogue (réservé à l'hôte).
  effect(id, name) {
    if (name === 'scene:nonlieu' && this.scene === 'miel' && id === this.hostId && !this.pending) {
      const p = this.players.get(id);
      if (p && Math.hypot(p.x, p.z + 10) <= INTERACT_RANGE + 2) {
        this.pending = { scene: 'nonlieu', in: 0.6 };
        return true;
      }
    }
    return false;
  }

  attack(id) {
    const p = this.players.get(id);
    if (!p || !p.alive || p.attackCd > 0) return false;
    p.attackCd = C.basicAttack.cooldown;
    let target = null;
    let best = C.basicAttack.range;
    for (const e of this.enemies) {
      const d = dist(e, p);
      if (d <= best) {
        best = d;
        target = e;
      }
    }
    this.emit({ t: 'swing', id });
    if (target) this.damageEnemy(target, C.basicAttack.damage, id);
    return true;
  }

  usePower(id) {
    const p = this.players.get(id);
    if (!p || !p.alive) return false;
    if (p.power === 'retenir') return this.powerRetenir(p);
    if (p.powerCd > 0) return false;
    if (p.power === 'rendre') return this.powerRendre(p);
    if (p.power === 'repousser') return this.powerRepousser(p);
    return false;
  }

  powerRetenir(p) {
    if (p.stored > 0) {
      const dmg = L.releaseDamage(p.stored);
      for (const e of [...this.enemies]) if (dist(e, p) <= C.retenir.releaseRadius) this.damageEnemy(e, dmg, p.id);
      this.emit({ t: 'power', id: p.id, power: 'retenir', release: true, x: p.x, z: p.z, r: C.retenir.releaseRadius });
      p.stored = 0;
      p.shield = 0;
      p.shieldT = 0;
      p.powerCd = L.POWERS.retenir.cooldown;
      return true;
    }
    if (p.powerCd > 0) return false;
    p.shield = C.retenir.shieldCapacity;
    p.shieldT = C.retenir.shieldSeconds;
    p.storedT = C.retenir.storedSeconds;
    this.emit({ t: 'power', id: p.id, power: 'retenir', release: false, x: p.x, z: p.z, r: 3 });
    return true;
  }

  powerRendre(p) {
    const group = this.alivePlayers().filter((q) => dist(q, p) <= C.rendre.radius);
    if (group.length < 2) {
      this.emit({ t: 'fizzle', id: p.id });
      return false;
    }
    const result = L.share(group.map((q) => ({ id: q.id, health: q.health, maxHealth: q.maxHealth })));
    for (const q of group) {
      let h = result[q.id];
      if (q.id === p.id) h = Math.max(1, h - C.rendre.selfCost);
      else h = Math.min(q.maxHealth, h + C.rendre.heal);
      q.health = h;
    }
    p.powerCd = L.POWERS.rendre.cooldown;
    this.emit({ t: 'power', id: p.id, power: 'rendre', x: p.x, z: p.z, r: C.rendre.radius });
    return true;
  }

  powerRepousser(p) {
    p.deflect = C.repousser.deflectSeconds;
    p.powerCd = L.POWERS.repousser.cooldown;
    for (const e of [...this.enemies]) {
      const d = dist(e, p);
      if (d <= C.repousser.radius) {
        const k = d > 0.01 ? 1 / d : 0;
        const dx = d > 0.01 ? (e.x - p.x) * k : 1;
        const dz = d > 0.01 ? (e.z - p.z) * k : 0;
        const push = e.kind === 'boss' ? C.repousser.push * 0.25 : C.repousser.push;
        [e.x, e.z] = clampPos(this.scene, e.x + dx * push, e.z + dz * push);
        this.damageEnemy(e, C.repousser.damage, p.id);
      }
    }
    this.addInstability(C.repousser.instabilityGain);
    this.emit({ t: 'power', id: p.id, power: 'repousser', x: p.x, z: p.z, r: C.repousser.radius });
    return true;
  }

  // ------------------------------------------------------------ Dégâts
  damageEnemy(e, amount, by) {
    if (!this.enemies.includes(e)) return;
    e.hp -= amount;
    this.emit({ t: 'hit', x: e.x, z: e.z, amount, boss: e.kind === 'boss' });
    if (e.kind === 'boss' && !this.bossMid && e.hp <= e.maxHp / 2 && e.hp > 0) {
      this.bossMid = true;
      e.phase = 2;
      this.say('kayden_mid');
    }
    if (e.hp <= 0) {
      this.enemies.splice(this.enemies.indexOf(e), 1);
      if (e.kind === 'boss') {
        this.enemies = [];
        this.finished = true;
        this.say('kayden_defeat');
        this.emit({ t: 'victory' });
      }
    }
  }

  damagePlayer(p, amount, fromDeflect = false) {
    if (!p.alive || amount <= 0) return;
    if (p.deflect > 0 && !fromDeflect) {
      const others = this.alivePlayers()
        .filter((q) => q.id !== p.id)
        .map((q) => ({ id: q.id, health: q.health, maxHealth: q.maxHealth, distance: dist(p, q) }));
      const target = L.pickDeflectTarget(others, amount, C.repousser.transferRange);
      if (target !== null) {
        this.emit({ t: 'deflect', from: p.id, to: target });
        this.damagePlayer(this.players.get(target), amount, true);
      } else {
        this.addInstability(amount * 0.8);
        this.emit({ t: 'deflect', from: p.id, to: null });
      }
      return;
    }
    let left = amount;
    if (p.shield > 0) {
      const r = L.absorb(p.shield, p.stored, amount);
      p.shield = r.shieldRemaining;
      p.stored = r.stored;
      left = r.left;
      p.storedT = C.retenir.storedSeconds;
    }
    if (left <= 0) return;
    p.health -= left;
    this.emit({ t: 'hurt', id: p.id, amount: left });
    if (p.health <= 0) {
      p.health = 0;
      p.alive = false;
      p.respawn = C.player.respawnSeconds;
      p.stored = 0;
      p.shield = 0;
      this.emit({ t: 'down', id: p.id });
    }
  }

  // ------------------------------------------------------------ Instabilité
  addInstability(n) {
    this.instability = Math.min(C.instability.max, Math.max(0, this.instability + n));
  }

  triggerMajorGlitch() {
    const alive = this.alivePlayers();
    this.holes = [];
    for (let i = 0; i < 5; i++) {
      const anchor = alive.length ? alive[Math.floor(this.rng() * alive.length)] : { x: 0, z: 0 };
      const [x, z] = clampPos(this.scene, anchor.x + (this.rng() - 0.5) * 16, anchor.z + (this.rng() - 0.5) * 16);
      this.holes.push({ x, z, r: 3, t: 5 });
    }
    this.instability = C.instability.resetAfterMajor;
    this.emit({ t: 'glitch', level: 2 });
  }

  // ------------------------------------------------------------ Ennemis
  spawnSilhouettes(n, around) {
    const alive = this.enemies.filter((e) => e.kind === 'sil').length;
    for (let i = 0; i < n && alive + i < C.waves.maxAlive + 2; i++) {
      const angle = this.rng() * Math.PI * 2;
      const d = 14 + this.rng() * 6;
      const [x, z] = clampPos(this.scene, around.x + Math.cos(angle) * d, around.z + Math.sin(angle) * d);
      this.enemies.push({ id: this.nextId++, kind: 'sil', x, z, hp: C.silhouette.health, maxHp: C.silhouette.health, cd: 1 });
    }
  }

  nearestAlive(e) {
    let best = null;
    let bestD = Infinity;
    for (const p of this.players.values()) {
      if (!p.alive) continue;
      const d = dist(e, p);
      if (d < bestD) {
        best = p;
        bestD = d;
      }
    }
    return best;
  }

  stepEnemy(e, dt) {
    const target = this.nearestAlive(e);
    if (!target) return;
    if (e.cd > 0) e.cd -= dt;
    const d = dist(e, target);
    if (e.kind === 'sil') {
      if (d > C.silhouette.attackRange) {
        const k = (C.silhouette.speed * dt) / d;
        [e.x, e.z] = clampPos(this.scene, e.x + (target.x - e.x) * k, e.z + (target.z - e.z) * k);
      } else if (e.cd <= 0) {
        e.cd = C.silhouette.attackCooldown;
        this.damagePlayer(target, C.silhouette.damage);
      }
      return;
    }
    // Boss
    const speed = C.boss.speed * (e.phase === 2 ? 1.25 : 1);
    if (!this.slam && d > 6) {
      const k = (speed * dt) / d;
      [e.x, e.z] = clampPos(this.scene, e.x + (target.x - e.x) * k, e.z + (target.z - e.z) * k);
    }
    if (this.slam) {
      this.slam.t -= dt;
      if (this.slam.t <= 0) {
        for (const p of this.alivePlayers()) {
          if (Math.hypot(p.x - this.slam.x, p.z - this.slam.z) <= C.boss.slamRadius) this.damagePlayer(p, C.boss.slamDamage);
        }
        this.emit({ t: 'slam', x: this.slam.x, z: this.slam.z, r: C.boss.slamRadius });
        this.slam = null;
        e.cd = e.phase === 2 ? 3 : 5;
      }
    } else if (e.cd <= 0) {
      this.slam = { x: target.x, z: target.z, t: 1.5 };
      this.emit({ t: 'telegraph', x: target.x, z: target.z, r: C.boss.slamRadius });
    }
    e.summonT -= dt;
    if (e.summonT <= 0) {
      e.summonT = e.phase === 2 ? 8 : 12;
      const sils = this.enemies.filter((x) => x.kind === 'sil').length;
      if (sils < 6) this.spawnSilhouettes(e.phase === 2 ? 3 : 2, e);
    }
  }

  // ------------------------------------------------------------ Boucle
  update(dt) {
    if (dt <= 0) return;
    this.time += dt;

    if (this.pending) {
      this.pending.in -= dt;
      if (this.pending.in <= 0) {
        const s = this.pending.scene;
        this.pending = null;
        this.startScene(s);
      }
    }

    for (const p of this.players.values()) {
      if (p.attackCd > 0) p.attackCd -= dt;
      if (p.powerCd > 0) p.powerCd -= dt;
      if (p.holeCd > 0) p.holeCd -= dt;
      if (p.deflect > 0) p.deflect = Math.max(0, p.deflect - dt);
      if (p.shieldT > 0) {
        p.shieldT -= dt;
        if (p.shieldT <= 0) p.shield = 0;
      } else if (p.stored > 0) {
        p.storedT -= dt;
        if (p.storedT <= 0) p.stored = 0;
      }
      if (!p.alive) {
        p.respawn -= dt;
        if (p.respawn <= 0 && this.alivePlayers().length > 0) {
          const [x, z] = spawnPoint(this.scene, 0);
          p.x = x;
          p.z = z;
          p.alive = true;
          p.health = p.maxHealth;
        }
        continue;
      }
      const slow = p.stored > 0 ? C.retenir.slowFactor : 1;
      const speed = C.player.speed * slow;
      [p.x, p.z] = clampPos(this.scene, p.x + p.input.mx * speed * dt, p.z + p.input.mz * speed * dt);
    }

    if (this.players.size > 0 && this.alivePlayers().length === 0) {
      let anyoneComing = false;
      for (const p of this.players.values()) if (p.respawn > 0) anyoneComing = true;
      if (anyoneComing) {
        this.emit({ t: 'wipe' });
        this.startScene(this.scene === 'kayden' ? 'kayden' : this.scene);
        for (const p of this.players.values()) p.respawn = 0;
      }
    }

    // Vagues (couloir)
    if (this.scene === 'nonlieu' && this.alivePlayers().length > 0) {
      this.waveTimer -= dt;
      if (this.waveTimer <= 0) {
        this.waveTimer = C.waves.interval;
        const alive = this.enemies.filter((e) => e.kind === 'sil').length;
        if (alive < C.waves.maxAlive) {
          const ps = this.alivePlayers();
          this.spawnSilhouettes(2, ps[Math.floor(this.rng() * ps.length)]);
        }
      }
    }

    for (const e of [...this.enemies]) this.stepEnemy(e, dt);

    // Instabilité et glitchs
    this.glitchTimer -= dt;
    if (this.instability >= C.instability.max) {
      this.triggerMajorGlitch();
    } else if (this.instability >= C.instability.minorThreshold && this.glitchTimer <= 0) {
      this.glitchTimer = 6;
      this.emit({ t: 'glitch', level: 1 });
    }
    if (this.instability > 0) this.instability = Math.max(0, this.instability - C.instability.decayPerSecond * dt);
    for (const h of this.holes) h.t -= dt;
    this.holes = this.holes.filter((h) => h.t > 0);
    for (const p of this.alivePlayers()) {
      if (p.holeCd > 0) continue;
      for (const h of this.holes) {
        if (Math.hypot(p.x - h.x, p.z - h.z) < h.r) {
          p.holeCd = 1.5;
          [p.x, p.z] = spawnPoint(this.scene, 0);
          this.damagePlayer(p, C.player.fallDamage);
          this.emit({ t: 'fall', id: p.id });
          break;
        }
      }
    }
  }

  // ------------------------------------------------------------ Instantané (réseau + rendu)
  snapshot() {
    return {
      time: r2(this.time),
      scene: this.scene,
      inst: r2(this.instability),
      finished: this.finished,
      host: this.hostId,
      players: [...this.players.values()].map((p) => ({
        id: p.id, name: p.name, power: p.power, ci: p.colorIndex,
        x: r2(p.x), z: r2(p.z), hp: r2(p.health), mhp: p.maxHealth, alive: p.alive,
        sh: r2(p.shield), st: r2(p.stored), df: r2(p.deflect), pcd: r2(Math.max(0, p.powerCd)),
      })),
      enemies: this.enemies.map((e) => ({ id: e.id, k: e.kind, x: r2(e.x), z: r2(e.z), hp: r2(e.hp), mhp: e.maxHp })),
      holes: this.holes.map((h) => ({ x: r2(h.x), z: r2(h.z), r: h.r })),
      doors: this.scene === 'nonlieu' ? this.doors.map((d) => ({ id: d.id, x: d.x, z: d.z, label: d.label })) : [],
      slam: this.slam ? { x: r2(this.slam.x), z: r2(this.slam.z) } : null,
    };
  }
}
