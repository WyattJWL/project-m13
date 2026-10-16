// Point d'entrée : menus, boucle de jeu, HUD, dialogues.

import { CONFIG } from './config.js';
import { DIALOGUE } from './dialogue.js';
import { Game } from './game.js';
import { HostNet, GuestNet } from './net.js';
import { Input } from './input.js';
import { Renderer } from './render.js';
import { POWERS, POWER_ORDER, PALETTE, dariusCharacter, normalizePartyCode, isValidPartyCode, sanitizeCustom } from './logic.js';

const $ = (id) => document.getElementById(id);
const SCENE_NAMES = { miel: 'Luynes, sous la pluie', nonlieu: 'Le Non-lieu', kayden: 'Kayden' };
const NPCS = [
  { x: -8, z: -2 },
  { x: 8, z: -2 },
  { x: 0, z: -10 },
];

if ('ontouchstart' in window || matchMedia('(pointer: coarse)').matches) document.body.classList.add('touch');

const state = {
  mode: null, // 'solo' | 'host' | 'guest'
  localId: null,
  game: null,
  host: null,
  guest: null,
  snap: null,
  renderer: null,
  dlgQueue: [],
  dlgActive: null,
  endTimer: null,
  character: null,
  pendingJoinCode: null,
  lastScene: null,
};
window.__m13 = state;

const input = new Input();
input.bindTouch($('stick'), $('knob'), $('t-attack'), $('t-power'), $('t-interact'));

// ------------------------------------------------------------------ Écrans
function show(id) {
  for (const s of ['menu', 'creator', 'end']) $(s).classList.toggle('hidden', s !== id);
}

function toast(text, ms = 2600) {
  const t = $('toast');
  t.textContent = text;
  t.classList.add('show');
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => t.classList.remove('show'), ms);
}

// ------------------------------------------------------------------ Créateur de personnage
let chosenPower = 'repousser';
let chosenColor = 1;
function buildCreator() {
  const box = $('powers');
  box.textContent = '';
  for (const id of POWER_ORDER) {
    const b = document.createElement('button');
    b.className = 'power-opt' + (id === chosenPower ? ' sel' : '');
    b.dataset.power = id;
    const name = document.createElement('b');
    name.textContent = POWERS[id].name;
    const sm = document.createElement('small');
    sm.textContent = POWERS[id].summary;
    b.append(name, sm);
    b.onclick = () => {
      chosenPower = id;
      buildCreator();
    };
    box.append(b);
  }
  const colors = $('colors');
  colors.textContent = '';
  PALETTE.forEach((c, i) => {
    const b = document.createElement('button');
    b.className = 'swatch' + (i === chosenColor ? ' sel' : '');
    b.style.background = `rgb(${c[0]},${c[1]},${c[2]})`;
    b.setAttribute('aria-label', 'Couleur ' + (i + 1));
    b.onclick = () => {
      chosenColor = i;
      buildCreator();
    };
    colors.append(b);
  });
}

// ------------------------------------------------------------------ Démarrage des modes
function ensureRenderer() {
  if (!state.renderer) state.renderer = new Renderer($('view'));
}

function enterGame() {
  ['menu', 'creator', 'end'].forEach((s) => $(s).classList.add('hidden'));
  $('hud').classList.remove('hidden');
  ensureRenderer();
  state.lastScene = null;
  state.dlgQueue = [];
  state.dlgActive = null;
  $('dialogue').classList.add('hidden');
}

function startSolo() {
  state.mode = 'solo';
  state.localId = 'me';
  state.game = new Game({ solo: true });
  state.game.addPlayer('me', dariusCharacter());
  enterGame();
}

async function startHost(character) {
  state.mode = 'host';
  state.localId = 'host';
  state.game = new Game({ solo: false });
  state.game.addPlayer('host', character);
  state.host = new HostNet(state.game, character, {
    onStatus: (t) => toast(t),
    onRoster: () => toast('Le groupe a changé : ' + state.game.players.size + ' joueur(s)'),
  });
  const code = await state.host.open();
  enterGame();
  toast('Code du groupe : ' + code + ' (partage-le !)', 8000);
  return code;
}

async function startGuest(code, character) {
  state.mode = 'guest';
  state.guest = new GuestNet({
    onSnap: (s) => (state.snap = s),
    onEvents: (list) => list.forEach(handleEvent),
    onClose: () => {
      toast('Connexion perdue. Retour au menu.', 4000);
      setTimeout(() => location.reload(), 2500);
    },
  });
  const id = await state.guest.connect(code, character);
  state.localId = id;
  enterGame();
}

// ------------------------------------------------------------------ Actions du joueur
function act(kind, extra) {
  if (!state.mode) return;
  if (state.mode === 'guest') {
    if (kind === 'effect') state.guest.send({ t: 'effect', name: extra });
    else state.guest.send({ t: kind });
    return;
  }
  const g = state.game;
  if (kind === 'attack') g.attack(state.localId);
  else if (kind === 'power') g.usePower(state.localId);
  else if (kind === 'interact') g.interact(state.localId);
  else if (kind === 'effect') g.effect(state.localId, extra);
}
input.handlers.attack = () => act('attack');
input.handlers.power = () => act('power');
input.handlers.interact = () => act('interact');

// ------------------------------------------------------------------ Dialogues
function pushDialogue(nodeId) {
  if (!DIALOGUE.nodes[nodeId]) return;
  if (state.dlgActive === nodeId || state.dlgQueue.includes(nodeId)) return;
  state.dlgQueue.push(nodeId);
  if (!state.dlgActive) nextDialogue();
}

function showNode(id) {
  const node = DIALOGUE.nodes[id];
  state.dlgActive = id;
  $('dialogue').classList.remove('hidden');
  $('dlg-speaker').textContent = node.speaker || '';
  $('dlg-text').textContent = node.text;
  const choices = $('dlg-choices');
  choices.textContent = '';
  const nextBtn = $('dlg-next');
  if (node.choices) {
    nextBtn.classList.add('hidden');
    for (const c of node.choices) {
      const b = document.createElement('button');
      b.textContent = c.text;
      b.onclick = () => {
        if (c.next) showNode(c.next);
        else closeDialogue();
      };
      choices.append(b);
    }
  } else {
    nextBtn.classList.remove('hidden');
    nextBtn.textContent = node.next ? 'Continuer ▸' : 'Fermer';
    nextBtn.onclick = () => (node.next ? showNode(node.next) : closeDialogue());
  }
  if (node.effect && node.effect.startsWith('scene:')) act('effect', node.effect);
}

function closeDialogue() {
  state.dlgActive = null;
  $('dialogue').classList.add('hidden');
  nextDialogue();
}

function nextDialogue() {
  const id = state.dlgQueue.shift();
  if (id) showNode(id);
}

window.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && state.dlgActive) {
    const btn = $('dlg-next');
    if (!btn.classList.contains('hidden')) btn.click();
  }
});

// ------------------------------------------------------------------ Événements de jeu
function handleEvent(e) {
  state.renderer?.onEvent(e);
  if (e.t === 'dialogue') {
    if (e.to === null || e.to === state.localId) pushDialogue(e.node);
  } else if (e.t === 'glitch') {
    const g = $('glitch');
    g.className = '';
    void g.offsetWidth;
    g.className = e.level === 2 ? 'l2' : 'l1';
    if (e.level === 2) toast('Le décor se fissure !');
  } else if (e.t === 'down' && e.id === state.localId) toast('Tu es à terre...');
  else if (e.t === 'wipe') toast('Tout le monde est tombé. On recommence la scène.', 3500);
  else if (e.t === 'fizzle' && e.id === state.localId) toast('Personne à portée.');
  else if (e.t === 'deflect' && e.from === state.localId) toast(e.to ? 'Le coup retombe sur un allié...' : 'Le monde encaisse...');
  else if (e.t === 'victory') {
    clearTimeout(state.endTimer);
    state.endTimer = setTimeout(() => {
      $('hud').classList.add('hidden');
      show('end');
    }, 5000);
  }
}

// ------------------------------------------------------------------ HUD
function nearInteractable(me, snap) {
  let list = [];
  if (snap.scene === 'miel') list = NPCS;
  else if (snap.scene === 'nonlieu') list = snap.doors;
  return list.some((it) => Math.hypot(it.x - me.x, it.z - me.z) <= 4.5);
}

function updateHud(snap) {
  const me = snap.players.find((p) => p.id === state.localId);
  if (!me) return;
  $('hp-fill').style.width = Math.max(0, (me.hp / me.mhp) * 100) + '%';
  $('hp-text').textContent = Math.ceil(me.hp) + ' / ' + me.mhp;
  $('inst-fill').style.width = snap.inst + '%';
  const boss = snap.enemies.find((e) => e.k === 'boss');
  $('boss-bar').classList.toggle('hidden', !boss);
  if (boss) $('boss-fill').style.width = Math.max(0, (boss.hp / boss.mhp) * 100) + '%';
  $('prompt').classList.toggle('hidden', !(me.alive && nearInteractable(me, snap)) || !!state.dlgActive);

  const pw = POWERS[me.power];
  let info = pw.name;
  if (me.power === 'retenir' && me.st > 0) info += ` · poids ${Math.round(me.st)} (relâcher)`;
  else if (me.pcd > 0) info += ` · ${me.pcd.toFixed(1)}s`;
  else info += ' · prêt';
  if (me.df > 0) info += ' · déviation';
  $('power-info').textContent = info;

  const lines = snap.players.map((p) => `${p.id === state.localId ? '▶ ' : ''}${p.name} ${Math.ceil(p.hp)}${p.alive ? '' : ' ✖'}`);
  const codeLine = state.host?.code ? [`Code : ${state.host.code}`] : [];
  $('party').textContent = '';
  if (snap.players.length > 1 || codeLine.length) {
    for (const l of [...codeLine, ...lines]) {
      const d = document.createElement('div');
      d.textContent = l;
      $('party').append(d);
    }
  }
  $('t-power').textContent = me.power === 'retenir' && me.st > 0 ? 'Relâcher' : pw.name;

  if (snap.scene !== state.lastScene) {
    state.lastScene = snap.scene;
    toast(SCENE_NAMES[snap.scene] || '');
  }
}

// ------------------------------------------------------------------ Boucle
let last = performance.now();
let acc = 0;
const STEP = 1 / CONFIG.tickRate;

function frame(now) {
  requestAnimationFrame(frame);
  const dt = Math.min(0.1, (now - last) / 1000);
  last = now;
  if (!state.mode || !state.renderer) return;

  const [mx, mz] = input.axes();
  if (state.mode === 'guest') {
    state.guestInputAcc = (state.guestInputAcc || 0) + dt;
    if (state.guestInputAcc > 1 / 20) {
      state.guestInputAcc = 0;
      state.guest.send({ t: 'input', mx, mz });
    }
  } else {
    const g = state.game;
    g.setInput(state.localId, mx, mz);
    acc += dt;
    while (acc >= STEP) {
      acc -= STEP;
      g.update(STEP);
      const events = g.drainEvents();
      events.forEach(handleEvent);
      state.host?.broadcast(STEP, events);
    }
    state.snap = g.snapshot();
  }

  if (state.snap) {
    state.renderer.draw(state.snap, state.localId, dt);
    updateHud(state.snap);
  }
}
requestAnimationFrame(frame);

// ------------------------------------------------------------------ Menus
$('btn-solo').onclick = startSolo;

function openCreator(next) {
  state.next = next;
  $('creator-error').textContent = '';
  buildCreator();
  show('creator');
}

$('btn-host').onclick = () => {
  $('menu-error').textContent = '';
  openCreator('host');
};
$('btn-join').onclick = () => {
  const code = normalizePartyCode($('join-code').value);
  if (!isValidPartyCode(code)) {
    $('menu-error').textContent = 'Le code fait 4 caractères (lettres et chiffres).';
    return;
  }
  state.pendingJoinCode = code;
  $('menu-error').textContent = '';
  openCreator('join');
};
$('btn-creator-back').onclick = () => show('menu');
$('btn-creator-ok').onclick = async () => {
  const res = sanitizeCustom({ name: $('char-name').value, power: chosenPower, colorIndex: chosenColor });
  if (!res.ok) {
    $('creator-error').textContent = res.error;
    return;
  }
  $('btn-creator-ok').disabled = true;
  $('creator-error').textContent = state.next === 'join' ? 'Connexion...' : 'Création du groupe...';
  try {
    if (state.next === 'host') await startHost(res.character);
    else await startGuest(state.pendingJoinCode, res.character);
  } catch (err) {
    $('creator-error').textContent = err.message || String(err);
    state.mode = null;
  } finally {
    $('btn-creator-ok').disabled = false;
  }
};
$('btn-again').onclick = () => location.reload();
