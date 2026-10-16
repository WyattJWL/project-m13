import test from 'node:test';
import assert from 'node:assert/strict';
import * as L from '../js/logic.js';
import { DIALOGUE } from '../js/dialogue.js';
import { Game, INTERACT_RANGE } from '../js/game.js';
import { CONFIG as C } from '../js/config.js';

function seeded(seed = 1) {
  let s = seed;
  return () => ((s = (s * 1664525 + 1013904223) % 4294967296) / 4294967296);
}
const hero = (power = 'retenir', name = 'Test') => ({ name, power, colorIndex: 0 });

test('dialogue : graphe cohérent', () => {
  assert.deepEqual(L.validateDialogue(DIALOGUE), []);
});

test('dialogue : détecte un noeud cassé', () => {
  const bad = { nodes: { a: { text: 'x', next: 'zz' } }, entries: ['a'] };
  assert.ok(L.validateDialogue(bad).length > 0);
});

test('codes de groupe', () => {
  const code = L.generatePartyCode(4, seeded(3));
  assert.equal(code.length, 4);
  assert.ok(L.isValidPartyCode(code));
  assert.equal(L.normalizePartyCode(' ab c d '), 'ABCD');
  assert.ok(!L.isValidPartyCode('ABC0'));
  assert.ok(!L.isValidPartyCode('ABC'));
});

test('personnages : noms réservés et validation', () => {
  assert.ok(!L.sanitizeCustom({ name: 'Darius', power: 'rendre' }).ok);
  assert.ok(!L.sanitizeCustom({ name: 'A', power: 'rendre' }).ok);
  assert.ok(!L.sanitizeCustom({ name: '<b>x</b>', power: 'rendre' }).ok);
  assert.ok(!L.sanitizeCustom({ name: 'Zoé', power: 'vol' }).ok);
  const r = L.sanitizeCustom({ name: ' Zoé ', power: 'rendre', colorIndex: 99 });
  assert.ok(r.ok);
  assert.equal(r.character.name, 'Zoé');
  assert.equal(r.character.colorIndex, 0);
});

test('Retenir : absorbe puis stocke', () => {
  const r = L.absorb(40, 0, 25);
  assert.deepEqual(r, { left: 0, shieldRemaining: 15, stored: 25 });
  const r2 = L.absorb(15, 25, 20);
  assert.deepEqual(r2, { left: 5, shieldRemaining: 0, stored: 40 });
  assert.equal(L.releaseDamage(40), 60);
  assert.equal(L.releaseDamage(500), 120);
});

test('Rendre : se rapproche de la moyenne sans tuer', () => {
  const out = L.share([
    { id: 'a', health: 100, maxHealth: 100 },
    { id: 'b', health: 10, maxHealth: 100 },
  ]);
  assert.ok(out.a < 100 && out.b > 10);
  assert.ok(out.b >= 1);
});

test('Repousser : choisit l\'allié le plus en forme à portée', () => {
  const t = L.pickDeflectTarget(
    [
      { id: 'a', health: 30, maxHealth: 100, distance: 5 },
      { id: 'b', health: 90, maxHealth: 100, distance: 5 },
      { id: 'c', health: 100, maxHealth: 100, distance: 99 },
    ],
    10,
    60,
  );
  assert.equal(t, 'b');
  assert.equal(L.pickDeflectTarget([{ id: 'a', health: 5, maxHealth: 100, distance: 2 }], 10, 60), null);
});

test('jeu : solo Darius, machine -> couloir', () => {
  const g = new Game({ rng: seeded(5) });
  g.addPlayer('me', L.dariusCharacter());
  const p = g.players.get('me');
  p.x = 0;
  p.z = -9;
  assert.ok(g.interact('me'));
  assert.ok(g.effect('me', 'scene:nonlieu'));
  g.update(1);
  assert.equal(g.scene, 'nonlieu');
  assert.equal(g.doors.filter((d) => d.real).length, 1);
  assert.equal(g.doors.find((d) => d.real).label, 41);
});

test('jeu : seul l\'hôte insère l\'année', () => {
  const g = new Game({ rng: seeded(5), solo: false });
  g.addPlayer('host', hero());
  g.addPlayer('guest', hero('rendre', 'Zoé'));
  for (const p of g.players.values()) {
    p.x = 0;
    p.z = -9;
  }
  assert.ok(!g.effect('guest', 'scene:nonlieu'));
  assert.ok(g.effect('host', 'scene:nonlieu'));
});

test('jeu : mauvaise porte -> instabilité et ennemis, porte 41 -> Kayden', () => {
  const g = new Game({ rng: seeded(9) });
  g.addPlayer('me', hero());
  g.startScene('nonlieu');
  const p = g.players.get('me');
  const wrong = g.doors.find((d) => !d.real);
  p.x = wrong.x;
  p.z = wrong.z;
  g.interact('me');
  assert.ok(g.instability >= 15);
  assert.ok(g.enemies.length >= 2);
  const right = g.doors.find((d) => d.real);
  p.x = right.x;
  p.z = right.z;
  g.interact('me');
  g.update(2.5);
  assert.equal(g.scene, 'kayden');
  assert.equal(g.enemies.filter((e) => e.kind === 'boss').length, 1);
});

test('jeu : Retenir absorbe puis libère', () => {
  const g = new Game({ rng: seeded(2) });
  g.addPlayer('me', hero('retenir'));
  g.startScene('nonlieu');
  const p = g.players.get('me');
  assert.ok(g.usePower('me'));
  g.damagePlayer(p, 30);
  assert.equal(p.health, 100);
  assert.equal(p.stored, 30);
  g.enemies.push({ id: 99, kind: 'sil', x: p.x + 3, z: p.z, hp: 200, maxHp: 200, cd: 9 });
  assert.ok(g.usePower('me'));
  assert.equal(p.stored, 0);
  assert.equal(g.enemies.find((e) => e.id === 99).hp, 200 - 45);
});

test('jeu : Rendre seul ne fait rien, à deux équilibre', () => {
  const g = new Game({ rng: seeded(2), solo: false });
  g.addPlayer('a', hero('rendre'));
  g.addPlayer('b', hero('retenir', 'Bob'));
  g.startScene('nonlieu');
  const a = g.players.get('a');
  const b = g.players.get('b');
  b.health = 20;
  assert.ok(g.usePower('a'));
  assert.ok(b.health > 20);
  assert.ok(a.health < 100);
  g.removePlayer('b');
  a.powerCd = 0;
  assert.ok(!g.usePower('a'));
});

test('jeu : Repousser dévie le coup sur un allié, sinon le monde glitche', () => {
  const g = new Game({ rng: seeded(2), solo: false });
  g.addPlayer('a', hero('repousser'));
  g.addPlayer('b', hero('retenir', 'Bob'));
  g.startScene('nonlieu');
  const a = g.players.get('a');
  const b = g.players.get('b');
  g.usePower('a');
  const inst = g.instability;
  g.damagePlayer(a, 10);
  assert.equal(a.health, 100);
  assert.equal(b.health, 90);
  g.removePlayer('b');
  g.damagePlayer(a, 10);
  assert.equal(a.health, 100);
  assert.ok(g.instability > inst);
});

test('jeu : instabilité 100 -> trous puis retour à 40', () => {
  const g = new Game({ rng: seeded(4) });
  g.addPlayer('me', hero());
  g.startScene('nonlieu');
  g.instability = 100;
  g.update(0.1);
  assert.ok(g.holes.length > 0);
  assert.ok(g.instability <= C.instability.resetAfterMajor);
});

test('jeu : le boss peut être vaincu, la partie se termine', () => {
  const g = new Game({ rng: seeded(4) });
  g.addPlayer('me', hero());
  g.startScene('kayden');
  const boss = g.enemies.find((e) => e.kind === 'boss');
  assert.equal(boss.maxHp, C.boss.baseHealth);
  g.damageEnemy(boss, boss.maxHp / 2 + 1, 'me');
  assert.ok(g.bossMid);
  g.damageEnemy(boss, 9999, 'me');
  assert.ok(g.finished);
  assert.equal(g.enemies.length, 0);
});

test('jeu : la vie du boss grandit avec le groupe', () => {
  const g = new Game({ rng: seeded(4), solo: false });
  for (let i = 0; i < 3; i++) g.addPlayer('p' + i, hero('retenir', 'P' + i));
  g.startScene('kayden');
  assert.equal(g.enemies[0].maxHp, C.boss.baseHealth + 2 * C.boss.perExtraPlayer);
});

test('jeu : limite de 4 joueurs', () => {
  const g = new Game({ rng: seeded(1), solo: false });
  for (let i = 0; i < 4; i++) assert.ok(g.addPlayer('p' + i, hero('retenir', 'P' + i)));
  assert.ok(!g.addPlayer('p5', hero()));
});

test('jeu : simulation longue sans erreur ni valeur invalide', () => {
  const g = new Game({ rng: seeded(11), solo: false });
  g.addPlayer('a', hero('repousser'));
  g.addPlayer('b', hero('retenir', 'Bob'));
  g.addPlayer('c', hero('rendre', 'Cléo'));
  g.startScene('nonlieu');
  for (let i = 0; i < 30 * 120; i++) {
    for (const id of ['a', 'b', 'c']) {
      g.setInput(id, Math.sin(i / 30 + id.charCodeAt(0)), Math.cos(i / 40));
      if (i % 20 === 0) g.attack(id);
      if (i % 90 === 0) g.usePower(id);
    }
    g.update(1 / 30);
    g.drainEvents();
  }
  for (const p of g.players.values()) {
    assert.ok(Number.isFinite(p.x) && Number.isFinite(p.z) && Number.isFinite(p.health));
  }
  JSON.stringify(g.snapshot());
});

test('portée d\'interaction', () => {
  const g = new Game({ rng: seeded(1) });
  g.addPlayer('me', hero());
  const p = g.players.get('me');
  p.x = 0;
  p.z = 12;
  assert.ok(!g.interact('me'));
  assert.ok(INTERACT_RANGE > 0);
});
