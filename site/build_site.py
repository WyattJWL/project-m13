import json

data = json.load(open("/Users/WyattLapaillerieEngone/Desktop/M13/site/chapters.json", encoding="utf-8"))
data_json = json.dumps(data, ensure_ascii=False)

# Full-book narration (synthesized, French system voice "Thomas" via macOS `say`),
# one m4a per chapter, served as relative files rather than embedded base64
# (the full book is ~270MB of audio, far too large to inline in one HTML page).
AUDIO_MAP = {c["num"]: f"audio/voices/chapitre-{c['num']:02d}.m4a" for c in data["chapters"]}
audio_map_json = json.dumps(AUDIO_MAP)

html_template = """<meta charset="utf-8">
<title>PROJECT-M13</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;1,7..72,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">

<style>
:root {
  --bg: #f2ede1;
  --surface: #e9e0cd;
  --surface-2: #ddd2b8;
  --ink: #221f1a;
  --ink-dim: #6b6152;
  --ink-faint: #948a78;
  --accent: #2f6fa8;
  --accent-ink: #ffffff;
  --accent-soft: #d9e8f4;
  --rule: #d3c6a9;
  --machine-bg: #e2d7bd;
  --machine-ink: #4a4331;
  --shadow: 0 10px 30px -12px rgba(40, 32, 16, 0.25);
  --font-display: 'Fraunces', Georgia, 'Times New Roman', serif;
  --font-body: 'Literata', Georgia, 'Times New Roman', serif;
  --font-mono: 'IBM Plex Mono', 'SF Mono', Menlo, monospace;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #14120e;
    --surface: #1c1913;
    --surface-2: #262117;
    --ink: #ece4d4;
    --ink-dim: #a89b83;
    --ink-faint: #766c5a;
    --accent: #7cb6f0;
    --accent-ink: #0c1620;
    --accent-soft: #23374a;
    --rule: #332c1f;
    --machine-bg: #201c14;
    --machine-ink: #b9ac8e;
    --shadow: 0 10px 30px -12px rgba(0, 0, 0, 0.6);
  }
}

:root[data-theme="dark"] {
  --bg: #14120e;
  --surface: #1c1913;
  --surface-2: #262117;
  --ink: #ece4d4;
  --ink-dim: #a89b83;
  --ink-faint: #766c5a;
  --accent: #7cb6f0;
  --accent-ink: #0c1620;
  --accent-soft: #23374a;
  --rule: #332c1f;
  --machine-bg: #201c14;
  --machine-ink: #b9ac8e;
  --shadow: 0 10px 30px -12px rgba(0, 0, 0, 0.6);
}

* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  min-height: 100vh;
  transition: background 0.25s ease, color 0.25s ease;
}

a { color: inherit; }

button {
  font-family: inherit;
  cursor: pointer;
  border: none;
  background: none;
  color: inherit;
}
button:focus-visible, [tabindex]:focus-visible, a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.app { max-width: 780px; margin: 0 auto; padding: 0 20px 40px; }

/* ---------- Header / brand ---------- */
.topbar {
  position: sticky; top: 0; z-index: 20;
  display: flex; align-items: center; justify-content: space-between;
  gap: 12px;
  padding: 14px 20px;
  background: color-mix(in srgb, var(--bg) 88%, transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--rule);
}
.brand {
  display: flex; align-items: baseline; gap: 8px;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.05rem;
  letter-spacing: 0.01em;
  text-decoration: none;
}
.brand .dot { color: var(--accent); }
.topbar-actions { display: flex; gap: 6px; align-items: center; }
.icon-btn {
  width: 38px; height: 38px; border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  color: var(--ink-dim);
}
.icon-btn:hover { background: var(--surface); color: var(--ink); }
.icon-btn svg { width: 19px; height: 19px; }

/* ---------- Cover ---------- */
.cover {
  padding: 56px 20px 8px;
  text-align: center;
}
.cover-eyebrow {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 18px;
}
.cover h1 {
  font-family: var(--font-display);
  font-size: clamp(2.6rem, 11vw, 4rem);
  font-weight: 700;
  line-height: 0.98;
  margin: 0;
  text-wrap: balance;
}
.cover .sub {
  font-family: var(--font-display);
  font-style: italic;
  font-optical-sizing: auto;
  font-weight: 400;
  font-size: clamp(1.15rem, 4.5vw, 1.5rem);
  color: var(--ink-dim);
  margin: 6px 0 0;
}
.cover .byline {
  margin: 22px 0 0;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--ink-faint);
  letter-spacing: 0.02em;
}
.cover .progress-ring-wrap {
  display: flex; justify-content: center; margin: 34px 0 6px;
}
.resume-btn {
  margin: 28px auto 0;
  display: inline-flex; align-items: center; gap: 10px;
  background: var(--accent); color: var(--accent-ink);
  padding: 13px 26px;
  border-radius: 999px;
  font-family: var(--font-body);
  font-weight: 600;
  font-size: 0.98rem;
  box-shadow: var(--shadow);
}
.resume-btn:hover { filter: brightness(1.06); }
.resume-sub { display:block; margin-top: 10px; font-size: 0.8rem; color: var(--ink-faint); font-family: var(--font-mono); }

/* ---------- Chapter list ---------- */
.toc { margin-top: 44px; }
.toc-heading {
  font-family: var(--font-mono);
  font-size: 0.7rem; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--ink-faint);
  border-bottom: 1px solid var(--rule);
  padding-bottom: 10px; margin-bottom: 4px;
  display: flex; justify-content: space-between;
}
.chapter-row {
  display: flex; align-items: center; gap: 16px;
  width: 100%; text-align: left;
  padding: 16px 4px;
  border-bottom: 1px solid var(--rule);
}
.chapter-row:hover .chap-title { color: var(--accent); }
.chap-num {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: 0.85rem;
  color: var(--ink-faint);
  width: 28px; flex-shrink: 0;
}
.chap-meta { flex: 1; min-width: 0; }
.chap-title {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 1.05rem;
  transition: color 0.15s ease;
}
.chap-tag { font-size: 0.78rem; color: var(--ink-faint); font-style: italic; margin-top: 2px; }
.chap-status { flex-shrink: 0; }
.chap-check { color: var(--accent); width: 18px; height: 18px; }
.chap-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--rule); }
.chap-dot.current { background: var(--accent); box-shadow: 0 0 0 4px var(--accent-soft); }

/* ---------- Reading view ---------- */
.reader { display: none; }
.reader.active { display: block; }
.cover-view.hidden, .toc.hidden { display: none; }

.chapter-head {
  padding: 26px 0 6px;
  text-align: center;
}
.chapter-head .eyebrow {
  font-family: var(--font-mono);
  font-size: 0.72rem; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 10px;
}
.chapter-head h2 {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: clamp(1.6rem, 6vw, 2.1rem);
  margin: 0;
  text-wrap: balance;
}
.chapter-head .tag { font-family: var(--font-display); font-style: italic; color: var(--ink-dim); margin-top: 6px; font-size: 0.95rem; }

.prose {
  margin-top: 30px;
  font-size: var(--reading-size, 1.14rem);
  line-height: 1.75;
  max-width: 66ch;
  margin-left: auto; margin-right: auto;
}
.prose p { margin: 0 0 1.25em; }
.prose p:first-of-type::first-letter {
  font-family: var(--font-display);
  font-size: 3.1em;
  font-weight: 700;
  float: left;
  line-height: 0.82;
  padding: 0.05em 0.08em 0 0;
  color: var(--accent);
}
.prose p.speaker {
  font-family: var(--font-mono);
  font-size: 0.75em;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ink-faint);
  margin: 1.6em 0 -0.6em;
}
.prose p.dialogue { margin-left: 0; }
.prose .machine-block {
  font-family: var(--font-mono);
  font-size: 0.86em;
  color: var(--machine-ink);
  background: var(--machine-bg);
  border-left: 3px solid var(--accent);
  padding: 14px 18px;
  margin: 1.6em 0;
  white-space: pre-line;
  letter-spacing: 0.02em;
}
.prose p.active-tts { background: var(--accent-soft); border-radius: 6px; box-shadow: 0 0 0 6px var(--accent-soft); }

.chapter-end {
  text-align: center;
  margin: 3em 0 1em;
  color: var(--ink-faint);
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
}
.chapter-end::before, .chapter-end::after {
  content: ""; display: inline-block; width: 28px; height: 1px;
  background: var(--rule); vertical-align: middle; margin: 0 10px;
}

.reader-nav {
  display: flex; justify-content: space-between; gap: 12px;
  margin-top: 22px; padding-top: 18px; border-top: 1px solid var(--rule);
}
.nav-btn {
  flex: 1;
  display: flex; flex-direction: column; gap: 2px;
  padding: 12px 14px;
  border-radius: 12px;
  border: 1px solid var(--rule);
  min-width: 0;
}
.nav-btn:hover { border-color: var(--accent); }
.nav-btn.next { text-align: right; align-items: flex-end; }
.nav-btn .label { font-family: var(--font-mono); font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-faint); }
.nav-btn .title { font-family: var(--font-display); font-weight: 600; font-size: 0.92rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 100%; }
.nav-btn:disabled { opacity: 0.35; pointer-events: none; }

/* ---------- Bottom toolbar (reading view) ---------- */
.toolbar {
  position: sticky; bottom: 0; z-index: 20;
  margin-top: 26px;
  display: flex; align-items: center; justify-content: center; gap: 6px;
  padding: 10px;
  background: color-mix(in srgb, var(--bg) 90%, transparent);
  backdrop-filter: blur(10px);
  border-top: 1px solid var(--rule);
}
.toolbar .icon-btn.playing { color: var(--accent); }
.progress-track {
  position: fixed; top: 0; left: 0; height: 2px; width: 0%;
  background: var(--accent); z-index: 30; transition: width 0.15s ease;
}

/* ---------- Panels (settings / TOC drawer) ---------- */
.sheet-backdrop {
  position: fixed; inset: 0; background: rgba(10, 8, 4, 0.45);
  opacity: 0; pointer-events: none; transition: opacity 0.2s ease; z-index: 40;
}
.sheet-backdrop.open { opacity: 1; pointer-events: auto; }
.sheet {
  position: fixed; left: 0; right: 0; bottom: 0; z-index: 41;
  background: var(--surface);
  border-radius: 20px 20px 0 0;
  padding: 18px 22px 28px;
  max-width: 780px; margin: 0 auto;
  transform: translateY(100%);
  transition: transform 0.25s ease;
  box-shadow: var(--shadow);
  max-height: 78vh; overflow-y: auto;
}
.sheet.open { transform: translateY(0); }
.sheet-handle { width: 36px; height: 4px; border-radius: 2px; background: var(--rule); margin: 0 auto 16px; }
.sheet h3 { font-family: var(--font-display); font-size: 1.05rem; margin: 0 0 14px; }
.row { display: flex; align-items: center; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid var(--rule); }
.row:last-child { border-bottom: none; }
.row .row-label { font-size: 0.92rem; }
.stepper { display: flex; align-items: center; gap: 14px; }
.stepper button {
  width: 34px; height: 34px; border-radius: 50%; border: 1px solid var(--rule);
  display: flex; align-items: center; justify-content: center; font-size: 1.1rem;
}
.theme-switch { display: flex; gap: 6px; }
.theme-switch button {
  padding: 7px 13px; border-radius: 999px; border: 1px solid var(--rule);
  font-size: 0.82rem;
}
.theme-switch button.active { background: var(--accent); color: var(--accent-ink); border-color: var(--accent); }
.voice-select {
  font-family: var(--font-body); font-size: 0.88rem;
  background: var(--bg); color: var(--ink);
  border: 1px solid var(--rule); border-radius: 8px; padding: 7px 10px;
  max-width: 60%;
}

.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; }

@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; }
}
</style>

<div class="progress-track" id="scrollProgress"></div>

<div class="topbar">
  <a class="brand" href="#" id="brandHome">PROJECT<span class="dot">-</span>M13</a>
  <div class="topbar-actions">
    <button class="icon-btn" id="tocBtn" aria-label="Sommaire" title="Sommaire">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h10"/></svg>
    </button>
    <button class="icon-btn" id="settingsBtn" aria-label="Réglages de lecture" title="Réglages">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .34 1.87l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.7 1.7 0 0 0-1.87-.34 1.7 1.7 0 0 0-1.04 1.56V21a2 2 0 0 1-4 0v-.09A1.7 1.7 0 0 0 9 19.4a1.7 1.7 0 0 0-1.87.34l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.7 1.7 0 0 0 4.6 15a1.7 1.7 0 0 0-1.56-1.04H3a2 2 0 0 1 0-4h.09A1.7 1.7 0 0 0 4.6 9a1.7 1.7 0 0 0-.34-1.87l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.7 1.7 0 0 0 9 4.6a1.7 1.7 0 0 0 1.04-1.56V3a2 2 0 0 1 4 0v.09A1.7 1.7 0 0 0 15 4.6a1.7 1.7 0 0 0 1.87-.34l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.7 1.7 0 0 0 19.4 9a1.7 1.7 0 0 0 1.56 1.04H21a2 2 0 0 1 0 4h-.09a1.7 1.7 0 0 0-1.56 1z"/></svg>
    </button>
  </div>
</div>

<div class="app">

  <div class="cover-view" id="coverView">
    <div class="cover">
      <p class="cover-eyebrow">Une histoire de Wyatt Lapaillerie-Engone</p>
      <h1>PROJECT-M13</h1>
      <p class="sub">La page 404</p>
      <p class="byline">LAPAILLERIE ENGONE Wyatt &middot; <span id="chapCountLabel"></span> chapitres</p>
      <button class="resume-btn" id="resumeBtn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
        <span id="resumeLabel">Commencer la lecture</span>
      </button>
      <span class="resume-sub" id="resumeSub"></span>
    </div>

    <div class="toc" id="tocList">
      <div class="toc-heading"><span>Chapitres</span><span id="tocCount"></span></div>
    </div>
  </div>

  <div class="reader" id="readerView">
    <div class="chapter-head">
      <p class="eyebrow" id="chEyebrow"></p>
      <h2 id="chTitle"></h2>
      <p class="tag" id="chAudioBadge" style="display:none; color: var(--accent); font-style: normal; font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.06em; text-transform: uppercase;">&#127911; narration audio disponible</p>
      <p class="tag" id="chTag"></p>
    </div>
    <div class="prose" id="chProse"></div>
    <p class="chapter-end" id="chEnd"></p>
    <div class="reader-nav">
      <button class="nav-btn prev" id="prevBtn">
        <span class="label">&larr; Précédent</span>
        <span class="title" id="prevTitle"></span>
      </button>
      <button class="nav-btn next" id="nextBtn">
        <span class="label">Suivant &rarr;</span>
        <span class="title" id="nextTitle"></span>
      </button>
    </div>
    <div class="toolbar">
      <button class="icon-btn" id="playBtn" aria-label="Lire à voix haute" title="Lire à voix haute">
        <svg viewBox="0 0 24 24" fill="currentColor" id="playIcon"><path d="M8 5v14l11-7z"/></svg>
      </button>
      <button class="icon-btn" id="fontMinusBtn" aria-label="Texte plus petit" title="Texte plus petit">A&minus;</button>
      <button class="icon-btn" id="fontPlusBtn" aria-label="Texte plus grand" title="Texte plus grand">A+</button>
      <button class="icon-btn" id="tocBtn2" aria-label="Sommaire" title="Sommaire">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h10"/></svg>
      </button>
    </div>
  </div>

</div>

<div class="sheet-backdrop" id="backdrop"></div>

<div class="sheet" id="tocSheet" role="dialog" aria-label="Sommaire">
  <div class="sheet-handle"></div>
  <h3>Sommaire</h3>
  <div id="tocSheetList"></div>
</div>

<div class="sheet" id="settingsSheet" role="dialog" aria-label="Réglages de lecture">
  <div class="sheet-handle"></div>
  <h3>Réglages de lecture</h3>
  <div class="row">
    <span class="row-label">Thème</span>
    <div class="theme-switch" id="themeSwitch">
      <button data-theme="light">Clair</button>
      <button data-theme="dark">Sombre</button>
      <button data-theme="system">Auto</button>
    </div>
  </div>
  <div class="row">
    <span class="row-label">Taille du texte</span>
    <div class="stepper">
      <button id="fontMinus2">A&minus;</button>
      <span id="fontSizeLabel" style="font-family: var(--font-mono); font-size: 0.85rem;">100%</span>
      <button id="fontPlus2">A+</button>
    </div>
  </div>
  <div class="row" style="flex-direction: column; align-items: flex-start; gap: 8px;">
    <div class="row" style="width: 100%; padding: 0; border: none;">
      <span class="row-label">Voix (lecture audio)</span>
      <select class="voice-select" id="voiceSelect"></select>
    </div>
    <p style="font-size: 0.78rem; color: var(--ink-faint); margin: 0; line-height: 1.5;">
      Les 12 chapitres ont désormais une narration audio complète, du début
      à la fin — bouton &#9654; en bas de la page, ça continue même écran
      verrouillé. C'est une voix de synthèse française (pas une voix
      enregistrée naturelle), mais elle couvre le livre entier.
    </p>
    <p style="font-size: 0.78rem; color: var(--ink-faint); margin: 0; line-height: 1.5;">
      <strong style="color: var(--ink-dim);">Pour une autre voix (celle de ton téléphone)&nbsp;:</strong>
      Réglages iPhone &rarr; Accessibilité &rarr; Contenu énoncé &rarr; active
      &laquo;&nbsp;Énoncer l'écran&nbsp;&raquo;. Ensuite, sur cette page, glisse deux doigts
      vers le bas depuis le haut de l'écran &mdash; iPhone lit tout avec la voix
      Siri, en arrière-plan.
    </p>
  </div>
  <div class="row">
    <span class="row-label">Vitesse de lecture</span>
    <div class="stepper">
      <button id="rateMinus">&minus;</button>
      <span id="rateLabel" style="font-family: var(--font-mono); font-size: 0.85rem;">1.0x</span>
      <button id="ratePlus">+</button>
    </div>
  </div>
</div>

<script id="storyData" type="application/json">__DATA__</script>
<script id="audioMap" type="application/json">__AUDIOMAP__</script>
<audio id="chapterAudio" preload="none" playsinline></audio>

<script>
(function () {
  const DATA = JSON.parse(document.getElementById('storyData').textContent);
  const chapters = DATA.chapters;
  const AUDIO_MAP = JSON.parse(document.getElementById('audioMap').textContent);
  const audioEl = document.getElementById('chapterAudio');
  const LS_KEY = 'm13-reader-state-v1';

  let memoryState = {};
  function loadState() {
    try { return JSON.parse(localStorage.getItem(LS_KEY)) || {}; }
    catch (e) { return memoryState; }
  }
  function saveState(patch) {
    const s = Object.assign(loadState(), patch);
    memoryState = s;
    try { localStorage.setItem(LS_KEY, JSON.stringify(s)); } catch (e) { /* storage unavailable, keep in memory */ }
    return s;
  }
  let state = loadState();

  // ---------- Theme ----------
  function applyTheme(t) {
    const root = document.documentElement;
    if (t === 'light') root.setAttribute('data-theme', 'light');
    else if (t === 'dark') root.setAttribute('data-theme', 'dark');
    else root.removeAttribute('data-theme');
    document.querySelectorAll('#themeSwitch button').forEach(b => {
      b.classList.toggle('active', b.dataset.theme === (t || 'system'));
    });
  }
  applyTheme(state.theme || 'system');
  document.getElementById('themeSwitch').addEventListener('click', (e) => {
    const btn = e.target.closest('button[data-theme]');
    if (!btn) return;
    state = saveState({ theme: btn.dataset.theme });
    applyTheme(state.theme);
  });

  // ---------- Font size ----------
  function applyFontSize(pct) {
    document.documentElement.style.setProperty('--reading-size', (1.14 * pct / 100) + 'rem');
    document.getElementById('fontSizeLabel').textContent = pct + '%';
  }
  let fontPct = state.fontPct || 100;
  applyFontSize(fontPct);
  function stepFont(delta) {
    fontPct = Math.max(75, Math.min(160, fontPct + delta));
    state = saveState({ fontPct });
    applyFontSize(fontPct);
  }
  document.getElementById('fontMinusBtn').addEventListener('click', () => stepFont(-10));
  document.getElementById('fontPlusBtn').addEventListener('click', () => stepFont(10));
  document.getElementById('fontMinus2').addEventListener('click', () => stepFont(-10));
  document.getElementById('fontPlus2').addEventListener('click', () => stepFont(10));

  // ---------- Sheets ----------
  const backdrop = document.getElementById('backdrop');
  const tocSheet = document.getElementById('tocSheet');
  const settingsSheet = document.getElementById('settingsSheet');
  function closeSheets() {
    backdrop.classList.remove('open');
    tocSheet.classList.remove('open');
    settingsSheet.classList.remove('open');
  }
  function openSheet(sheet) {
    closeSheets();
    backdrop.classList.add('open');
    sheet.classList.add('open');
  }
  backdrop.addEventListener('click', closeSheets);
  document.getElementById('tocBtn').addEventListener('click', () => openSheet(tocSheet));
  document.getElementById('tocBtn2').addEventListener('click', () => openSheet(tocSheet));
  document.getElementById('settingsBtn').addEventListener('click', () => openSheet(settingsSheet));

  // ---------- Build TOC ----------
  function progressForChapter(num) {
    return (state.read || []).includes(num);
  }
  function buildTocRow(ch, forSheet) {
    const row = document.createElement('button');
    row.className = 'chapter-row';
    row.style.cursor = 'pointer';
    const done = progressForChapter(ch.num);
    const isCurrent = state.currentChapter === ch.num;
    row.innerHTML =
      '<span class="chap-num">' + String(ch.num).padStart(2, '0') + '</span>' +
      '<span class="chap-meta"><span class="chap-title">' + escapeHtml(ch.title) + '</span>' +
      (ch.tag ? '<div class="chap-tag">' + escapeHtml(ch.tag) + '</div>' : '') + '</span>' +
      '<span class="chap-status">' + (done
        ? '<svg class="chap-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
        : '<span class="chap-dot' + (isCurrent ? ' current' : '') + '"></span>') + '</span>';
    row.addEventListener('click', () => { closeSheets(); openChapter(ch.num); });
    return row;
  }
  function renderToc() {
    const list = document.getElementById('tocList');
    list.querySelectorAll('.chapter-row').forEach(n => n.remove());
    document.getElementById('tocCount').textContent = chapters.length + ' chapitres';
    const sheetList = document.getElementById('tocSheetList');
    sheetList.innerHTML = '';
    chapters.forEach(ch => {
      list.appendChild(buildTocRow(ch));
      sheetList.appendChild(buildTocRow(ch));
    });
  }
  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  }

  // ---------- Resume button ----------
  function updateResume() {
    const readList = state.read || [];
    let label = 'Commencer la lecture';
    let sub = '';
    if (state.currentChapter) {
      const ch = chapters.find(c => c.num === state.currentChapter);
      if (ch) { label = 'Reprendre — Chapitre ' + ch.num; sub = ch.title; }
    } else if (readList.length) {
      label = 'Continuer la lecture';
    }
    document.getElementById('resumeLabel').textContent = label;
    document.getElementById('resumeSub').textContent = sub;
  }
  document.getElementById('resumeBtn').addEventListener('click', () => {
    openChapter(state.currentChapter || 1);
  });
  document.getElementById('brandHome').addEventListener('click', (e) => {
    e.preventDefault(); showCover();
  });

  // ---------- Reader ----------
  const coverView = document.getElementById('coverView');
  const readerView = document.getElementById('readerView');

  function showCover() {
    stopTTS();
    coverView.classList.remove('hidden');
    readerView.classList.remove('active');
    renderToc();
    updateResume();
    document.title = 'PROJECT-M13';
    window.scrollTo(0, 0);
  }

  function markRead(num) {
    const read = new Set(state.read || []);
    read.add(num);
    state = saveState({ read: Array.from(read) });
  }

  function openChapter(num) {
    stopTTS();
    const ch = chapters.find(c => c.num === num);
    if (!ch) return;
    state = saveState({ currentChapter: num });
    coverView.classList.add('hidden');
    readerView.classList.add('active');

    document.getElementById('chEyebrow').textContent = 'Chapitre ' + String(ch.num).padStart(2, '0') + ' / ' + chapters.length;
    document.getElementById('chTitle').textContent = ch.title;
    document.title = ch.num + ' - ' + ch.title + ' - Project M13';
    document.getElementById('chTag').textContent = ch.tag || '';
    document.getElementById('chTag').style.display = ch.tag ? 'block' : 'none';
    document.getElementById('chAudioBadge').style.display = AUDIO_MAP[String(ch.num)] ? 'block' : 'none';

    const prose = document.getElementById('chProse');
    prose.innerHTML = '';
    ch.blocks.forEach(b => {
      if (b.type === 'name') {
        const p = document.createElement('p');
        p.className = 'speaker';
        p.textContent = b.text;
        prose.appendChild(p);
      } else if (b.type === 'machine') {
        const p = document.createElement('p');
        p.className = 'machine-block';
        p.textContent = b.text;
        prose.appendChild(p);
      } else {
        const p = document.createElement('p');
        p.className = 'dialogue';
        p.textContent = b.text;
        prose.appendChild(p);
      }
    });

    document.getElementById('chEnd').textContent = 'fin du chapitre ' + ch.num;

    const idx = chapters.findIndex(c => c.num === num);
    const prev = chapters[idx - 1], next = chapters[idx + 1];
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    prevBtn.disabled = !prev;
    nextBtn.disabled = !next;
    document.getElementById('prevTitle').textContent = prev ? prev.title : '';
    document.getElementById('nextTitle').textContent = next ? next.title : '';
    prevBtn.onclick = () => prev && openChapter(prev.num);
    nextBtn.onclick = () => next && openChapter(next.num);

    markRead(num);
    window.scrollTo(0, 0);
    populateVoices();
  }

  // ---------- Scroll progress ----------
  window.addEventListener('scroll', () => {
    const h = document.documentElement;
    const scrolled = h.scrollTop;
    const max = h.scrollHeight - h.clientHeight;
    document.getElementById('scrollProgress').style.width = max > 0 ? (scrolled / max * 100) + '%' : '0%';
  });

  // ---------- Text to speech ----------
  let ttsUtterances = [];
  let ttsIndex = 0;
  let ttsPlaying = false;

  function voiceQualityScore(v) {
    const n = v.name.toLowerCase();
    if (n.includes('enhanced') || n.includes('premium') || n.includes('neural')) return 3;
    if (n.includes('siri') || n.includes('natural') || n.includes('wavenet')) return 3;
    if (v.localService === false) return 1; // network voices are often better than default robotic ones
    return 0;
  }
  function populateVoices() {
    const sel = document.getElementById('voiceSelect');
    const voices = window.speechSynthesis ? window.speechSynthesis.getVoices() : [];
    const frVoices = voices.filter(v => v.lang && v.lang.toLowerCase().startsWith('fr'));
    const list = (frVoices.length ? frVoices : voices)
      .slice()
      .sort((a, b) => voiceQualityScore(b) - voiceQualityScore(a));
    if (!list.length) { sel.innerHTML = '<option>Voix indisponible</option>'; return; }
    sel.innerHTML = list.map((v, i) => '<option value="' + i + '">' + v.name + ' (' + v.lang + ')' + (voiceQualityScore(v) >= 3 ? ' — recommandée' : '') + '</option>').join('');
    const savedName = state.voiceName;
    const savedIdx = list.findIndex(v => v.name === savedName);
    sel.value = savedIdx >= 0 ? savedIdx : 0;
    sel._voices = list;
  }
  if (window.speechSynthesis) {
    window.speechSynthesis.onvoiceschanged = populateVoices;
  }
  document.getElementById('voiceSelect').addEventListener('change', (e) => {
    const list = e.target._voices || [];
    const v = list[e.target.value];
    if (v) state = saveState({ voiceName: v.name });
  });

  let rate = state.rate || 1.0;
  function updateRateLabel() { document.getElementById('rateLabel').textContent = rate.toFixed(1) + 'x'; }
  updateRateLabel();
  document.getElementById('rateMinus').addEventListener('click', () => {
    rate = Math.max(0.6, +(rate - 0.1).toFixed(1));
    state = saveState({ rate }); updateRateLabel();
  });
  document.getElementById('ratePlus').addEventListener('click', () => {
    rate = Math.min(1.6, +(rate + 0.1).toFixed(1));
    state = saveState({ rate }); updateRateLabel();
  });

  function stopTTS() {
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    audioEl.pause();
    ttsPlaying = false;
    document.querySelectorAll('.prose p.active-tts').forEach(p => p.classList.remove('active-tts'));
    updatePlayIcon();
    if ('mediaSession' in navigator) navigator.mediaSession.playbackState = 'paused';
  }

  function playRealAudio(num, ch) {
    audioEl.src = AUDIO_MAP[String(num)];
    audioEl.currentTime = 0;
    audioEl.play();
    ttsPlaying = true;
    updatePlayIcon();
    setupMediaSession(ch);
    if ('mediaSession' in navigator) navigator.mediaSession.playbackState = 'playing';
  }
  audioEl.addEventListener('ended', () => { ttsPlaying = false; updatePlayIcon(); if ('mediaSession' in navigator) navigator.mediaSession.playbackState = 'paused'; });
  function updatePlayIcon() {
    const icon = document.getElementById('playIcon');
    const btn = document.getElementById('playBtn');
    btn.classList.toggle('playing', ttsPlaying);
    icon.innerHTML = ttsPlaying
      ? '<path d="M6 5h4v14H6zM14 5h4v14h-4z"/>'
      : '<path d="M8 5v14l11-7z"/>';
  }

  function setupMediaSession(ch) {
    if (!('mediaSession' in navigator)) return;
    navigator.mediaSession.metadata = new MediaMetadata({
      title: ch.title,
      artist: 'LAPAILLERIE ENGONE Wyatt',
      album: 'PROJECT-M13 — chapitre ' + ch.num
    });
    navigator.mediaSession.setActionHandler('play', () => {
      if (!ttsPlaying) { ttsPlaying = true; updatePlayIcon(); speakFrom(ttsIndex); }
    });
    navigator.mediaSession.setActionHandler('pause', () => stopTTS());
    navigator.mediaSession.setActionHandler('stop', () => stopTTS());
  }

  function speakFrom(index) {
    if (!window.speechSynthesis) { alert('La lecture audio n\\'est pas disponible sur ce navigateur.'); return; }
    const paras = Array.from(document.querySelectorAll('#chProse p')).filter(p => p.textContent.trim());
    if (index >= paras.length) { stopTTS(); return; }
    window.speechSynthesis.cancel();
    const p = paras[index];
    document.querySelectorAll('.prose p.active-tts').forEach(el => el.classList.remove('active-tts'));
    p.classList.add('active-tts');
    p.scrollIntoView({ behavior: 'smooth', block: 'center' });
    const utter = new SpeechSynthesisUtterance(p.textContent);
    utter.lang = 'fr-FR';
    utter.rate = rate;
    const sel = document.getElementById('voiceSelect');
    const list = sel._voices || [];
    const v = list[sel.value];
    if (v) utter.voice = v;
    utter.onend = () => { if (ttsPlaying) speakFrom(index + 1); };
    ttsIndex = index;
    window.speechSynthesis.speak(utter);
    if ('mediaSession' in navigator) navigator.mediaSession.playbackState = 'playing';
  }

  document.getElementById('playBtn').addEventListener('click', () => {
    if (ttsPlaying) { stopTTS(); return; }
    const ch = chapters.find(c => c.num === state.currentChapter);
    if (ch && AUDIO_MAP[String(ch.num)]) {
      playRealAudio(ch.num, ch);
      return;
    }
    ttsPlaying = true;
    updatePlayIcon();
    if (ch) setupMediaSession(ch);
    speakFrom(0);
  });

  // Some mobile browsers suspend speechSynthesis after ~15s if the tab loses
  // focus; nudging resume() periodically keeps playback alive where possible.
  setInterval(() => {
    if (ttsPlaying && window.speechSynthesis && window.speechSynthesis.paused) {
      window.speechSynthesis.resume();
    }
  }, 4000);

  // init
  document.getElementById('chapCountLabel').textContent = chapters.length;
  renderToc();
  updateResume();
  if (location.hash.startsWith('#ch')) {
    const n = parseInt(location.hash.slice(3), 10);
    if (n) openChapter(n);
  }
})();
</script>
"""

out = html_template.replace("__DATA__", data_json).replace("__AUDIOMAP__", audio_map_json)
with open("/Users/WyattLapaillerieEngone/Desktop/M13/site/m13-reader.html", "w", encoding="utf-8") as f:
    f.write(out)

print("Written", len(out), "bytes")
