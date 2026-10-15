# PROJECT-M13 : le jeu Roblox

Jeu Roblox tiré de la trilogie PROJECT-M13. **On avance tome par tome** : ce dossier contient le **Tome 1** (une première version jouable).

## Les deux modes

| Mode | Comment ça marche |
|---|---|
| **Solo** | Tu joues **Darius**, sur un serveur privé rien que pour toi. |
| **Groupe** (2 à 4) | Un joueur crée un groupe et reçoit un **code de 4 caractères**. Les autres tapent le code dans le lobby. Tout le monde joue sur le **même serveur privé**. Chacun crée un personnage **qui n'est pas dans l'histoire** et choisit son pouvoir. Clara, Alex et Kayden sont des personnages non jouables. |

## Les trois pouvoirs

| Pouvoir | Effet | Le prix |
|---|---|---|
| **Retenir** | Un bouclier encaisse les coups et les stocke. Réutilise le pouvoir pour tout relâcher en explosion. | Tu es ralenti tant que tu portes du poids. |
| **Rendre** | Répartit la santé entre les alliés proches. | Tu en gardes un peu pour toi. |
| **Repousser** | Repousse les ennemis et dévie les coups pendant 3 secondes. | **Le coup retombe sur un allié**, et le monde glitche. En solo, c'est le monde qui paie. |

## L'histoire jouable (Tome 1)

1. **Miel** : la place de Luynes sous la pluie. Parle à Clara et Alex, lis l'étiquette du distributeur, puis **insère une année** (réservé à l'hôte du groupe).
2. **Le Non-lieu** : un couloir blanc aux portes numérotées. Trouve la **porte 41**. Les autres portes mentent, font monter l'**instabilité** (le glitch) et attirent des Silhouettes.
3. **Kayden** : l'arène du boss. À la fin, la **page 41** est récupérée et la partie se termine.

Commandes : **Q** = pouvoir, **clic** = attaque, **E** = parler / ouvrir, **Espace** = continuer un dialogue. Au toucher, les boutons du HUD.

## Organisation du code

```
roblox/
  lobby.project.json        Lieu 1 : le lobby (point de départ)
  tome1.project.json        Lieu 2 : le jeu du Tome 1
  src/shared/               Code commun (réglages, pouvoirs, dialogues, personnages)
  src/lobby/                Menu : solo, créer un groupe, rejoindre un groupe
  src/tome1/server/         Histoire, ennemis, pouvoirs, glitch, décors générés par le code
  src/tome1/client/         Interface, dialogues, effets de glitch
  tests/run.luau            Tests de la logique (16 tests)
  tests/api_check.luau      Vérifie les noms de classes, propriétés et énumérations Roblox
  tests/smoke.luau          Génère vraiment les décors et les ennemis avec les types Roblox
```

Le code est compilé avec **Rojo**. Les décors sont **générés par le code** (blocs simples) pour que tout marche sans Studio. Tu pourras les remplacer plus tard par de vrais décors : garde les mêmes noms et les mêmes `ProximityPrompt`.

## Tester sur ton ordinateur

1. Installe **Roblox Studio** et **Rojo** (`cargo install rojo --locked`, ou via Rokit/Aftman).
2. Compile : `rojo build tome1.project.json -o build/M13-Tome1.rbxl`, puis ouvre le fichier dans Studio.
3. Lance une session de test (**Play**). Sans téléportation, tu joues **Darius en solo**.
4. Les groupes et la téléportation ne marchent **que sur le jeu publié** (pas dans Studio).

Tests : `lune run tests/run`, `lune run tests/api_check`, `lune run tests/smoke`. Format : `stylua src tests`.

## Publier sur Roblox (étapes)

### 1. Créer l'expérience (à faire une seule fois, dans Roblox)
1. Va sur **create.roblox.com** → *Creations* → crée une **expérience**. Elle contient un premier lieu : ce sera le **lobby** (lieu de départ).
2. Ajoute un **deuxième lieu** dans la même expérience (*Places* → *Create new place*) : ce sera le **Tome 1**.
3. Dans les réglages de chaque lieu : **Max players** = 50 pour le lobby, **4** pour le Tome 1.
4. Note ces trois numéros : l'**Universe ID**, le **Place ID du lobby**, le **Place ID du Tome 1**.
5. Garde l'expérience **privée** tant que tu testes.

### 2. Créer la clé API (Open Cloud)
1. *Creator Hub* → *Open Cloud* → **API Keys** → *Create API Key*.
2. Système d'API : **Place Publishing** (`universe-places`), permission **Write**. Limite-la à **ton expérience**.
3. Mets une **date d'expiration** courte.
4. **Ne colle jamais cette clé dans le chat ni dans un fichier du dépôt.**

### 3. Les mettre dans GitHub
*Settings → Secrets and variables → Actions* :

| Type | Nom | Valeur |
|---|---|---|
| **Secret** | `ROBLOX_API_KEY` | la clé |
| Variable | `UNIVERSE_ID` | l'Universe ID |
| Variable | `LOBBY_PLACE_ID` | le Place ID du lobby |
| Variable | `TOME1_PLACE_ID` | le Place ID du Tome 1 |

Utilise bien **Secrets** pour la clé (pas *Variables*, qui sont visibles).

### 4. Publier
Onglet **Actions** → **Roblox M13** → **Run workflow** → coche **publish**. Le workflow vérifie le code, compile les deux lieux et les envoie sur Roblox.

## Limites connues (première version)
- **Pas testé dans Roblox Studio par l'auteur du code** : il peut rester des petits bugs à corriger au premier essai.
- Pas de sauvegarde de progression, pas de sons, décors très simples.
- La création de l'expérience elle-même reste manuelle (l'API ne permet que de publier une nouvelle version d'un lieu existant).
