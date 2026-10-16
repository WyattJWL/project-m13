// Logique pure (sans navigateur) : pouvoirs, codes de groupe, personnages, dialogues.
// Même règles que la version Roblox (roblox/src/shared/*.luau).

import { CONFIG } from './config.js';

// ---------------------------------------------------------------- Pouvoirs
export const POWER_ORDER = ['retenir', 'rendre', 'repousser'];

export const POWERS = {
  retenir: {
    id: 'retenir',
    name: 'Retenir',
    cooldown: 6,
    color: [80, 140, 255],
    summary: 'Encaisse les coups et les garde en toi. Réutilise le pouvoir pour tout relâcher.',
  },
  rendre: {
    id: 'rendre',
    name: 'Rendre',
    cooldown: 8,
    color: [255, 200, 90],
    summary: 'Répartit la douleur entre les alliés proches. Ça te coûte un peu.',
  },
  repousser: {
    id: 'repousser',
    name: 'Repousser',
    cooldown: 7,
    color: [230, 90, 90],
    summary: 'Repousse les ennemis et dévie les coups... qui retombent sur un allié. Et le monde glitche.',
  },
};

export function isValidPower(id) {
  return typeof id === 'string' && Object.prototype.hasOwnProperty.call(POWERS, id);
}

// Retenir : le bouclier absorbe jusqu'à `shieldRemaining` points et les stocke.
// Renvoie { left, shieldRemaining, stored }.
export function absorb(shieldRemaining, stored, damage) {
  const absorbed = Math.min(damage, shieldRemaining);
  return { left: damage - absorbed, shieldRemaining: shieldRemaining - absorbed, stored: stored + absorbed };
}

// Retenir : relâcher le poids stocké (borné).
export function releaseDamage(stored) {
  return Math.min(Math.max(stored * 1.5, 0), 120);
}

// Rendre : chaque membre se rapproche du ratio de santé moyen. Personne ne meurt de ça.
// members : [{ id, health, maxHealth }]. Renvoie { id: nouvelleSanté }.
export function share(members, pull = 0.6) {
  const result = {};
  if (members.length === 0) return result;
  const average = members.reduce((sum, m) => sum + m.health / m.maxHealth, 0) / members.length;
  for (const m of members) {
    const ratio = m.health / m.maxHealth;
    const next = (ratio + (average - ratio) * pull) * m.maxHealth;
    result[m.id] = Math.min(Math.max(next, 1), m.maxHealth);
  }
  return result;
}

// Repousser : le coup retombe sur l'allié en meilleure santé (en ratio) qui peut l'encaisser.
// candidates : [{ id, health, maxHealth, distance }]. Renvoie un id, ou null (le monde paie).
export function pickDeflectTarget(candidates, damage, maxDistance) {
  let best = null;
  for (const c of candidates) {
    if (c.distance <= maxDistance && c.health > damage) {
      if (best === null || c.health / c.maxHealth > best.health / best.maxHealth) best = c;
    }
  }
  return best ? best.id : null;
}

// ---------------------------------------------------------------- Codes de groupe
export const PARTY_ALPHABET = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789';

export function generatePartyCode(length = CONFIG.partyCodeLength, random = Math.random) {
  let code = '';
  for (let i = 0; i < length; i++) code += PARTY_ALPHABET[Math.floor(random() * PARTY_ALPHABET.length)];
  return code;
}

export function normalizePartyCode(input) {
  if (typeof input !== 'string') return null;
  return input.replace(/\s+/g, '').toUpperCase();
}

export function isValidPartyCode(code, length = CONFIG.partyCodeLength) {
  if (typeof code !== 'string' || code.length !== length) return false;
  for (const ch of code) if (!PARTY_ALPHABET.includes(ch)) return false;
  return true;
}

// ---------------------------------------------------------------- Personnages
export const PALETTE = [
  [235, 235, 240],
  [90, 140, 255],
  [255, 190, 80],
  [230, 90, 90],
  [120, 200, 140],
  [190, 130, 230],
];

export const CANON = {
  darius: { name: 'Darius', power: 'retenir', colorIndex: 0 },
  clara: { name: 'Clara', colorIndex: 2 },
  alex: { name: 'Alex', colorIndex: 1 },
};

const RESERVED = [
  'darius', 'clara', 'alex', 'aubin', 'kayden', 'templier', 'franck', 'miel', 'vasseur', 'odile',
  'evie', 'évie', 'emilie', 'émilie', 'leopold', 'léopold', 'lecteur',
];

export function isReservedName(name) {
  return RESERVED.includes(String(name).trim().toLowerCase());
}

// Valide un personnage créé par un joueur (groupe). Renvoie { ok, character?, error? }.
export function sanitizeCustom(raw) {
  if (!raw || typeof raw !== 'object') return { ok: false, error: 'Personnage invalide.' };
  if (typeof raw.name !== 'string') return { ok: false, error: 'Choisis un nom.' };
  const name = raw.name.trim();
  const length = [...name].length;
  if (length < 2 || length > 16) return { ok: false, error: 'Le nom doit faire entre 2 et 16 caractères.' };
  if (/[\u0000-\u001f\u007f<>]/.test(name)) return { ok: false, error: 'Le nom contient des caractères interdits.' };
  if (isReservedName(name)) return { ok: false, error: "Ce nom appartient à l'histoire. Choisis-en un autre." };
  if (!isValidPower(raw.power)) return { ok: false, error: 'Choisis un pouvoir.' };
  let colorIndex = raw.colorIndex;
  if (typeof colorIndex !== 'number' || !(colorIndex >= 0 && colorIndex < PALETTE.length)) colorIndex = 0;
  return { ok: true, character: { name, power: raw.power, colorIndex: Math.floor(colorIndex), canon: null } };
}

// Personnage solo : Darius.
export function dariusCharacter() {
  return { ...CANON.darius, canon: 'darius' };
}

// ---------------------------------------------------------------- Dialogues
// Vérifie qu'un graphe de dialogue est cohérent. Renvoie la liste des erreurs.
export function validateDialogue(graph) {
  const errors = [];
  const nodes = graph.nodes;
  if (!nodes || typeof nodes !== 'object') return ['graph.nodes manquant'];
  const reachable = new Set();
  const visit = (id) => {
    if (reachable.has(id)) return;
    reachable.add(id);
    const node = nodes[id];
    if (!node) return;
    if (node.next) visit(node.next);
    if (node.choices) for (const choice of node.choices) if (choice.next) visit(choice.next);
  };
  for (const entry of graph.entries || []) {
    if (!nodes[entry]) errors.push(`entrée inconnue : ${entry}`);
    else visit(entry);
  }
  for (const [id, node] of Object.entries(nodes)) {
    if (typeof node.text !== 'string' || node.text.length === 0) errors.push(`${id} : texte vide`);
    if (node.next && !nodes[node.next]) errors.push(`${id} : next inconnu (${node.next})`);
    if (node.next && node.choices) errors.push(`${id} : a à la fois next et choices`);
    if (node.choices) {
      if (node.choices.length === 0) errors.push(`${id} : choices vide`);
      node.choices.forEach((choice, i) => {
        if (typeof choice.text !== 'string' || !choice.text) errors.push(`${id} : choix ${i + 1} sans texte`);
        if (choice.next && !nodes[choice.next]) errors.push(`${id} : choix ${i + 1} vers un noeud inconnu`);
      });
    }
    if (!reachable.has(id)) errors.push(`${id} : noeud inatteignable`);
  }
  return errors;
}
