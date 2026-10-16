// Rendu 3D (Three.js) à partir des instantanés de la simulation.

import * as THREE from '../vendor/three.module.js';
import { PALETTE } from './logic.js';

const col = (c) => new THREE.Color(c[0] / 255, c[1] / 255, c[2] / 255);

function labelSprite(text, { size = 64, color = '#ffffff', bg = null } = {}) {
  const c = document.createElement('canvas');
  c.width = 256;
  c.height = 128;
  const g = c.getContext('2d');
  if (bg) {
    g.fillStyle = bg;
    g.fillRect(0, 0, 256, 128);
  }
  g.fillStyle = color;
  g.font = `bold ${size}px sans-serif`;
  g.textAlign = 'center';
  g.textBaseline = 'middle';
  g.fillText(text, 128, 64);
  const tex = new THREE.CanvasTexture(c);
  const m = new THREE.SpriteMaterial({ map: tex, transparent: true, depthTest: false });
  const s = new THREE.Sprite(m);
  s.scale.set(4, 2, 1);
  s.renderOrder = 10;
  return s;
}

function figure(color, scale = 1) {
  const grp = new THREE.Group();
  const body = new THREE.Mesh(
    new THREE.CapsuleGeometry(0.6 * scale, 1.2 * scale, 4, 10),
    new THREE.MeshStandardMaterial({ color, roughness: 0.6 }),
  );
  body.position.y = 1.2 * scale;
  grp.add(body);
  return grp;
}

export class Renderer {
  constructor(canvas) {
    this.canvas = canvas;
    this.renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(55, 1, 0.1, 400);
    this.camTarget = new THREE.Vector3();
    this.sceneKey = null;
    this.world = new THREE.Group();
    this.scene.add(this.world);
    this.actors = new Map(); // clé -> { obj, tx, tz }
    this.fx = [];
    this.scene.add(new THREE.AmbientLight(0xffffff, 0.9));
    const sun = new THREE.DirectionalLight(0xffffff, 1.1);
    sun.position.set(10, 30, 10);
    this.scene.add(sun);
    this.resize();
    window.addEventListener('resize', () => this.resize());
  }

  resize() {
    const w = this.canvas.clientWidth || window.innerWidth;
    const h = this.canvas.clientHeight || window.innerHeight;
    this.renderer.setSize(w, h, false);
    this.camera.aspect = w / h;
    this.camera.updateProjectionMatrix();
  }

  clearWorld() {
    this.world.clear();
    for (const a of this.actors.values()) this.scene.remove(a.obj);
    this.actors.clear();
    this.fx = [];
  }

  buildScene(key, snap) {
    this.clearWorld();
    this.sceneKey = key;
    const mat = (c) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.9 });
    if (key === 'miel') {
      this.scene.background = new THREE.Color(0x1b2430);
      this.scene.fog = new THREE.Fog(0x1b2430, 25, 70);
      const ground = new THREE.Mesh(new THREE.PlaneGeometry(60, 60), mat(0x3a3f4a));
      ground.rotation.x = -Math.PI / 2;
      this.world.add(ground);
      const lamp = (x, z) => {
        const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.15, 0.15, 7), mat(0x222222));
        pole.position.set(x, 3.5, z);
        const l = new THREE.PointLight(0xffd9a0, 40, 28);
        l.position.set(x, 7, z);
        this.world.add(pole, l);
      };
      lamp(-14, -14);
      lamp(14, -14);
      lamp(0, 14);
      const machine = new THREE.Mesh(new THREE.BoxGeometry(2.4, 4.2, 1.6), mat(0x6a1b1b));
      machine.position.set(0, 2.1, -10.8);
      const lbl = labelSprite('PAGE 41', { size: 52, color: '#ffd9a0' });
      lbl.position.set(0, 5.6, -10.8);
      this.world.add(machine, lbl);
      const npc = (x, z, name, c) => {
        const f = figure(c);
        f.position.set(x, 0, z);
        const t = labelSprite(name, { size: 60 });
        t.position.set(x, 4.2, z);
        this.world.add(f, t);
      };
      npc(-8, -2, 'Clara', 0xffbe50);
      npc(8, -2, 'Alex', 0x5a8cff);
    } else if (key === 'nonlieu') {
      this.scene.background = new THREE.Color(0xe9edf2);
      this.scene.fog = new THREE.Fog(0xe9edf2, 20, 90);
      const ground = new THREE.Mesh(new THREE.PlaneGeometry(14, 160), mat(0xf4f6f8));
      ground.rotation.x = -Math.PI / 2;
      ground.position.z = -72;
      this.world.add(ground);
      for (const sx of [-1, 1]) {
        const wall = new THREE.Mesh(new THREE.BoxGeometry(0.6, 8, 160), mat(0xc9d1d9));
        wall.position.set(sx * 7.6, 4, -72);
        this.world.add(wall);
      }
      for (const d of snap.doors) {
        const door = new THREE.Mesh(new THREE.BoxGeometry(0.4, 5, 3), mat(0x2b3440));
        door.position.set(d.x > 0 ? 7.1 : -7.1, 2.5, d.z);
        const t = labelSprite(String(d.label), { size: 90, color: '#ffffff' });
        t.position.set(d.x > 0 ? 6 : -6, 4.2, d.z);
        t.scale.set(2.6, 1.3, 1);
        this.world.add(door, t);
      }
      const l = new THREE.PointLight(0xffffff, 0.5, 0);
      l.position.set(0, 20, -40);
      this.world.add(l);
    } else {
      this.scene.background = new THREE.Color(0x120d1c);
      this.scene.fog = new THREE.Fog(0x120d1c, 25, 80);
      const ground = new THREE.Mesh(new THREE.CircleGeometry(30, 48), mat(0x2a2236));
      ground.rotation.x = -Math.PI / 2;
      this.world.add(ground);
      const ring = new THREE.Mesh(new THREE.TorusGeometry(30, 0.4, 8, 64), mat(0x6c4bb0));
      ring.rotation.x = Math.PI / 2;
      this.world.add(ring);
      for (let i = 0; i < 16; i++) {
        const a = (i / 16) * Math.PI * 2;
        const page = new THREE.Mesh(new THREE.BoxGeometry(2.2, 7, 0.3), mat(0xe9e4f2));
        page.position.set(Math.cos(a) * 32, 3.5, Math.sin(a) * 32);
        page.rotation.y = -a + Math.PI / 2;
        this.world.add(page);
      }
    }
  }

  getActor(key, make) {
    let a = this.actors.get(key);
    if (!a) {
      a = { obj: make(), tx: 0, tz: 0, seen: 0 };
      this.scene.add(a.obj);
      this.actors.set(key, a);
    }
    return a;
  }

  addRing(x, z, r, color, life = 0.5) {
    const m = new THREE.Mesh(
      new THREE.RingGeometry(r * 0.9, r, 48),
      new THREE.MeshBasicMaterial({ color, transparent: true, opacity: 0.7, side: THREE.DoubleSide }),
    );
    m.rotation.x = -Math.PI / 2;
    m.position.set(x, 0.1, z);
    this.scene.add(m);
    this.fx.push({ obj: m, life, max: life });
  }

  // Événements de la simulation -> effets visuels
  onEvent(e) {
    if (e.t === 'power') {
      const c = e.power === 'retenir' ? 0x508cff : e.power === 'rendre' ? 0xffc85a : 0xe65a5a;
      this.addRing(e.x, e.z, e.r, c, 0.6);
    } else if (e.t === 'slam') this.addRing(e.x, e.z, e.r, 0xff3355, 0.5);
    else if (e.t === 'hit') this.addRing(e.x, e.z, 1.2, 0xffffff, 0.25);
  }

  draw(snap, localId, dt) {
    if (snap.scene !== this.sceneKey) this.buildScene(snap.scene, snap);
    const seen = new Set();
    const k = Math.min(1, dt * 14);

    for (const p of snap.players) {
      const key = 'p' + p.id;
      seen.add(key);
      const a = this.getActor(key, () => {
        const f = figure(col(PALETTE[p.ci] || PALETTE[0]));
        const lbl = labelSprite(p.name, { size: 56 });
        lbl.position.y = 4.4;
        f.add(lbl);
        const shield = new THREE.Mesh(
          new THREE.SphereGeometry(1.9, 16, 12),
          new THREE.MeshBasicMaterial({ color: 0x508cff, transparent: true, opacity: 0.3 }),
        );
        shield.position.y = 1.8;
        shield.name = 'shield';
        f.add(shield);
        f.position.set(p.x, 0, p.z);
        return f;
      });
      a.obj.position.x += (p.x - a.obj.position.x) * k;
      a.obj.position.z += (p.z - a.obj.position.z) * k;
      a.obj.visible = p.alive;
      const sh = a.obj.getObjectByName('shield');
      if (sh) sh.visible = p.sh > 0 || p.df > 0;
      if (sh) sh.material.color.set(p.df > 0 ? 0xe65a5a : 0x508cff);
      if (p.id === localId) {
        this.camTarget.x += (p.x - this.camTarget.x) * k;
        this.camTarget.z += (p.z - this.camTarget.z) * k;
      }
    }

    for (const e of snap.enemies) {
      const key = 'e' + e.id;
      seen.add(key);
      const boss = e.k === 'boss';
      const a = this.getActor(key, () => {
        const f = figure(boss ? 0x8c1d3a : 0x15151c, boss ? 2.6 : 1.05);
        f.position.set(e.x, 0, e.z);
        return f;
      });
      a.obj.position.x += (e.x - a.obj.position.x) * k;
      a.obj.position.z += (e.z - a.obj.position.z) * k;
    }

    if (snap.slam) {
      seen.add('slam');
      const a = this.getActor('slam', () => {
        const m = new THREE.Mesh(
          new THREE.CircleGeometry(10, 48),
          new THREE.MeshBasicMaterial({ color: 0xff3355, transparent: true, opacity: 0.3 }),
        );
        m.rotation.x = -Math.PI / 2;
        m.position.y = 0.08;
        return m;
      });
      a.obj.position.x = snap.slam.x;
      a.obj.position.z = snap.slam.z;
    }

    snap.holes.forEach((h, i) => {
      const key = 'h' + i;
      seen.add(key);
      const a = this.getActor(key, () => {
        const m = new THREE.Mesh(new THREE.CircleGeometry(h.r, 24), new THREE.MeshBasicMaterial({ color: 0x000000 }));
        m.rotation.x = -Math.PI / 2;
        m.position.y = 0.12;
        return m;
      });
      a.obj.position.x = h.x;
      a.obj.position.z = h.z;
    });

    for (const [key, a] of [...this.actors]) {
      if (!seen.has(key)) {
        this.scene.remove(a.obj);
        this.actors.delete(key);
      }
    }

    for (const f of [...this.fx]) {
      f.life -= dt;
      f.obj.material.opacity = Math.max(0, f.life / f.max) * 0.7;
      f.obj.scale.setScalar(1 + (1 - f.life / f.max) * 0.3);
      if (f.life <= 0) {
        this.scene.remove(f.obj);
        this.fx.splice(this.fx.indexOf(f), 1);
      }
    }

    // Caméra : vue de dessus, légèrement inclinée
    const shake = snap.inst >= 50 ? (snap.inst - 40) / 600 : 0;
    this.camera.position.set(
      this.camTarget.x + (Math.random() - 0.5) * shake * 8,
      26,
      this.camTarget.z + 17 + (Math.random() - 0.5) * shake * 8,
    );
    this.camera.lookAt(this.camTarget.x, 0, this.camTarget.z);
    this.renderer.render(this.scene, this.camera);
  }
}
