# PROJECT-M13 : version navigateur (Tome 1)

Jouable sur téléphone ou ordinateur, sans compte ni installation : ouvre `docs/jeu/index.html` via GitHub Pages (`/jeu/`).

- **Solo** : tu joues Darius (pouvoir Retenir).
- **Groupe** (2 à 4) : un joueur crée un groupe et reçoit un code de 4 caractères, les autres le tapent. Connexion directe entre navigateurs (WebRTC via PeerJS), l'hôte fait tourner la partie.
- Histoire : Luynes (machine) → Non-lieu (porte 41) → Kayden. Pouvoirs : Retenir, Rendre, Repousser. Jauge d'instabilité (glitch).
- Commandes : ZQSD/flèches, Espace = attaque, F = pouvoir, E = agir. Tactile : joystick + boutons.

Code : `js/logic.js` et `js/game.js` (règles, sans navigateur), `js/render.js` (Three.js), `js/net.js` (PeerJS). Librairies incluses dans `vendor/` (three 0.186.1, peerjs 1.5.5).

Tests : `node --test tests/logic.test.mjs` ; bout en bout : `M13_DEPS=<node_modules avec playwright-core et peer> node tests/e2e.mjs`.
