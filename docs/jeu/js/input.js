// Entrées : clavier + manette tactile (joystick virtuel et boutons).

export class Input {
  constructor() {
    this.keys = new Set();
    this.stick = { x: 0, y: 0 };
    this.handlers = { attack: () => {}, power: () => {}, interact: () => {} };
    this.enabled = true;

    window.addEventListener('keydown', (e) => {
      if (!this.enabled || e.target instanceof HTMLInputElement) return;
      const k = e.key.toLowerCase();
      if (k === 'e') this.handlers.interact();
      else if (k === 'f' || k === 'shift') this.handlers.power();
      else if (k === ' ') {
        e.preventDefault();
        this.handlers.attack();
      }
      this.keys.add(k);
    });
    window.addEventListener('keyup', (e) => this.keys.delete(e.key.toLowerCase()));
    window.addEventListener('blur', () => this.keys.clear());
  }

  bindTouch(stickEl, knobEl, btnAttack, btnPower, btnInteract) {
    const R = 50;
    let active = null;
    const move = (t) => {
      const rect = stickEl.getBoundingClientRect();
      let dx = t.clientX - (rect.left + rect.width / 2);
      let dy = t.clientY - (rect.top + rect.height / 2);
      const len = Math.hypot(dx, dy);
      if (len > R) {
        dx = (dx / len) * R;
        dy = (dy / len) * R;
      }
      knobEl.style.transform = `translate(${dx}px, ${dy}px)`;
      this.stick = { x: dx / R, y: dy / R };
    };
    const end = () => {
      active = null;
      knobEl.style.transform = 'translate(0,0)';
      this.stick = { x: 0, y: 0 };
    };
    stickEl.addEventListener('touchstart', (e) => {
      e.preventDefault();
      active = e.changedTouches[0].identifier;
      move(e.changedTouches[0]);
    }, { passive: false });
    stickEl.addEventListener('touchmove', (e) => {
      e.preventDefault();
      for (const t of e.changedTouches) if (t.identifier === active) move(t);
    }, { passive: false });
    stickEl.addEventListener('touchend', end);
    stickEl.addEventListener('touchcancel', end);
    const tap = (el, fn) => {
      el.addEventListener('touchstart', (e) => {
        e.preventDefault();
        fn();
      }, { passive: false });
      el.addEventListener('click', fn);
    };
    tap(btnAttack, () => this.handlers.attack());
    tap(btnPower, () => this.handlers.power());
    tap(btnInteract, () => this.handlers.interact());
  }

  // Direction de déplacement (x = droite, z = bas à l'écran), normalisée.
  axes() {
    let x = this.stick.x;
    let z = this.stick.y;
    const k = this.keys;
    if (k.has('arrowleft') || k.has('a') || k.has('q')) x -= 1;
    if (k.has('arrowright') || k.has('d')) x += 1;
    if (k.has('arrowup') || k.has('w') || k.has('z')) z -= 1;
    if (k.has('arrowdown') || k.has('s')) z += 1;
    const len = Math.hypot(x, z);
    return len > 1 ? [x / len, z / len] : [x, z];
  }
}
