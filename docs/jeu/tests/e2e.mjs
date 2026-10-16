// Test de bout en bout (Chromium headless). Usage :
//   M13_DEPS=/chemin/vers/node_modules node tests/e2e.mjs
// M13_DEPS doit contenir playwright-core et peer.
import { createRequire } from 'node:module';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';

const deps = process.env.M13_DEPS;
const req = createRequire(path.join(deps, 'x.js'));
const { chromium } = req('playwright-core');
const { PeerServer } = req('peer');

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const OUT = process.env.M13_OUT || '/tmp';
const types = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css' };

const server = http.createServer((q, r) => {
  const p = path.join(root, decodeURIComponent(new URL(q.url, 'http://x').pathname).replace(/\/$/, '/index.html'));
  if (!p.startsWith(root) || !fs.existsSync(p)) {
    r.writeHead(404).end();
    return;
  }
  r.writeHead(200, { 'content-type': types[path.extname(p)] || 'application/octet-stream' }).end(fs.readFileSync(p));
});
await new Promise((ok) => server.listen(8123, '127.0.0.1', ok));
const peerServer = PeerServer({ port: 9123, path: '/', host: '0.0.0.0' });

const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium',
  args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--no-sandbox'],
});
const errors = [];
const watch = (page, name) => {
  page.on('pageerror', (e) => errors.push(`${name}: ${e.message}`));
  page.on('console', (m) => m.type() === 'error' && errors.push(`${name} console: ${m.text()}`));
};
const BASE = 'http://127.0.0.1:8123/index.html';
const Q = '?peerHost=127.0.0.1&peerPort=9123&peerPath=/';

const T = (f, ms = 15000) => f.catch((e) => {
  throw e;
});

try {
  // ------------------------------------------------ Solo (mobile)
  const ctx = await browser.newContext({ viewport: { width: 390, height: 780 }, hasTouch: true, isMobile: true });
  const page = await ctx.newPage();
  watch(page, 'solo');
  await page.goto(BASE + Q);
  await page.screenshot({ path: `${OUT}/m13_menu.png` });
  await page.click('#btn-solo');
  await page.waitForFunction(() => window.__m13.snap && window.__m13.snap.players.length === 1);
  await page.waitForTimeout(500);
  await page.screenshot({ path: `${OUT}/m13_solo_miel.png` });

  // Aller à la machine et dialoguer
  const solo = (fn, arg) => page.evaluate(fn, arg);
  await solo(() => {
    const p = window.__m13.game.players.get('me');
    p.x = 0;
    p.z = -9;
  });
  await page.waitForTimeout(200);
  await page.evaluate(() => document.getElementById('t-interact').click());
  await page.waitForSelector('#dialogue:not(.hidden)');
  // fermer d'éventuels dialogues en file jusqu'au choix de la machine
  for (let i = 0; i < 6; i++) {
    const text = await page.textContent('#dlg-speaker');
    if (text === 'Distributeur') break;
    await page.evaluate(() => document.getElementById('dlg-next').click());
    await page.waitForTimeout(100);
  }
  await page.screenshot({ path: `${OUT}/m13_solo_dialogue.png` });
  await page.getByText('Insérer une année').click();
  await page.waitForFunction(() => window.__m13.snap.scene === 'nonlieu', null, { timeout: 8000 });
  await page.waitForTimeout(500);
  await page.screenshot({ path: `${OUT}/m13_solo_nonlieu.png` });

  // Mauvaise porte -> glitch + ennemis ; on teste pouvoir et attaque
  await solo(() => {
    const g = window.__m13.game;
    const d = g.doors.find((x) => !x.real);
    const p = g.players.get('me');
    p.x = d.x;
    p.z = d.z;
  });
  await page.evaluate(() => document.getElementById('t-interact').click());
  await page.waitForTimeout(300);
  const enemies = await solo(() => window.__m13.game.enemies.length);
  assert.ok(enemies >= 2, 'des Silhouettes doivent apparaître');
  await page.evaluate(() => document.getElementById('t-power').click());
  const shield = await solo(() => window.__m13.game.players.get('me').shield);
  assert.ok(shield > 0, 'Retenir doit activer le bouclier');

  // Porte 41 -> Kayden
  await solo(() => {
    const g = window.__m13.game;
    const d = g.doors.find((x) => x.real);
    const p = g.players.get('me');
    p.x = d.x;
    p.z = d.z;
  });
  await page.evaluate(() => document.getElementById('t-interact').click());
  await page.waitForFunction(() => window.__m13.snap.scene === 'kayden', null, { timeout: 8000 });
  await page.waitForTimeout(700);
  await page.screenshot({ path: `${OUT}/m13_solo_kayden.png` });

  // Victoire
  await solo(() => {
    const g = window.__m13.game;
    const boss = g.enemies.find((e) => e.kind === 'boss');
    g.damageEnemy(boss, 99999, 'me');
  });
  await page.waitForSelector('#end:not(.hidden)', { timeout: 10000 });
  await page.screenshot({ path: `${OUT}/m13_end.png` });
  await ctx.close();

  // ------------------------------------------------ Groupe : hôte + invité
  const c1 = await browser.newContext({ viewport: { width: 900, height: 600 } });
  const c2 = await browser.newContext({ viewport: { width: 390, height: 780 }, hasTouch: true, isMobile: true });
  const host = await c1.newPage();
  const guest = await c2.newPage();
  watch(host, 'host');
  watch(guest, 'guest');
  await host.goto(BASE + Q);
  await host.click('#btn-host');
  await host.fill('#char-name', 'Zoé');
  await host.click('.power-opt[data-power="rendre"]');
  await host.click('#btn-creator-ok');
  await host.waitForFunction(() => window.__m13.host && window.__m13.host.code, null, { timeout: 15000 });
  const code = await host.evaluate(() => window.__m13.host.code);
  assert.match(code, /^[A-Z2-9]{4}$/);

  await guest.goto(BASE + Q);
  await guest.fill('#join-code', code.toLowerCase());
  await guest.click('#btn-join');
  await guest.fill('#char-name', 'Max');
  await guest.click('.power-opt[data-power="repousser"]');
  await guest.click('#btn-creator-ok');
  await guest.waitForFunction(() => window.__m13.snap && window.__m13.snap.players.length === 2, null, { timeout: 20000 });
  const hostCount = await host.evaluate(() => window.__m13.game.players.size);
  assert.equal(hostCount, 2);

  // L'invité bouge (envoi d'entrée au réseau) : on force via l'axe virtuel
  await guest.evaluate(() => {
    window.__stick = true;
  });
  await guest.keyboard.down('d');
  await host.waitForTimeout(900);
  await guest.keyboard.up('d');
  const gx = await host.evaluate(() => {
    const g = window.__m13.game;
    return [...g.players.values()].find((p) => p.name === 'Max').x;
  });
  assert.ok(gx > 0, "l'invité doit avoir bougé côté hôte (x=" + gx + ')');

  // Seul l'hôte peut lancer le Non-lieu
  await host.evaluate(() => {
    for (const p of window.__m13.game.players.values()) {
      p.x = 0;
      p.z = -9;
    }
  });
  assert.equal(await host.evaluate(() => window.__m13.game.effect('g' === 'x' ? '' : [...window.__m13.game.players.keys()].find((k) => k !== 'host'), 'scene:nonlieu')), false);
  await host.evaluate(() => window.__m13.game.effect('host', 'scene:nonlieu'));
  await guest.waitForFunction(() => window.__m13.snap.scene === 'nonlieu', null, { timeout: 8000 });
  await guest.waitForTimeout(600);
  await guest.screenshot({ path: `${OUT}/m13_guest_nonlieu.png` });
  await host.screenshot({ path: `${OUT}/m13_host_nonlieu.png` });

  // Mauvais code
  const c3 = await browser.newContext();
  const bad = await c3.newPage();
  watch(bad, 'bad');
  await bad.goto(BASE + Q);
  await bad.fill('#join-code', 'ZZZZ');
  await bad.click('#btn-join');
  await bad.fill('#char-name', 'Nul');
  await bad.click('#btn-creator-ok');
  await bad.waitForFunction(() => document.getElementById('creator-error').textContent.includes('introuvable'), null, { timeout: 20000 });

  // Nom réservé refusé
  await bad.fill('#char-name', 'Darius');
  await bad.click('#btn-creator-ok');
  await bad.waitForFunction(() => document.getElementById('creator-error').textContent.includes('histoire'));

  const real = errors.filter((e) => !/favicon|Failed to load resource|WebGL|GPU stall/i.test(e));
  assert.deepEqual(real, [], 'aucune erreur JS attendue');
  console.log('E2E OK');
} finally {
  await browser.close();
  peerServer.close?.();
  server.close();
  setTimeout(() => process.exit(0), 200);
}
