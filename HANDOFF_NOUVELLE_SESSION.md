# Prompt de reprise (à coller dans la nouvelle session, dépôt `game` sélectionné)

Tu reprends un projet commencé dans une autre session. Réponds en français, ton direct, structuré, avec quelques emojis. Je suis sur téléphone, sans ordinateur : explique les étapes simplement.

## Mon objectif
Dans le dépôt `game` (mon jeu Roblox existant), ajouter une **passerelle vers PROJECT-M13** :
- les **admins** voient un bouton **M13** ;
- il ouvre un choix **Solo** ou **Multi** ;
- en **Multi** : créer un groupe (un code de 4 caractères) ou rejoindre en tapant un code ;
- **Ne rien supprimer ni modifier de l'ancien jeu**, seulement ajouter (dossier séparé, par ex. `m13/`). Travaille sur une branche à part, pas de pull request sans que je le demande.

## Ce qui existe déjà (ajoute le dépôt avec add_repo : `WyattJWL/project-m13`, branche `claude/m13-second-book-jn0zra`)
- `roblox/` : code Luau du **Tome 1** déjà validé par CI (StyLua, 16 tests Lune, vérification d'API Roblox, test de fumée, builds Rojo 7.7.1). Contient `lobby.project.json` (lobby : solo / créer groupe / rejoindre), `tome1.project.json` (jeu), `src/shared` (Config, PlaceIds, Powers, PartyCode, Characters, DialogueGraph, Remotes, dialogues FR), `src/lobby`, `src/tome1` (Session, WorldBuilder, EnemyService, PowerService, GlitchService, StoryService, UI…).
- Règles : solo = on joue Darius ; groupe 2 à 4 joueurs avec **personnages créés par les joueurs** (pas ceux de l'histoire) et choix d'un pouvoir ; téléportation en **serveur privé** (`TeleportService`, `ReserveServer`) ; codes de groupe via **MemoryStore** ; 3 pouvoirs (Retenir, Rendre, Repousser), jauge d'**instabilité** (glitch), ennemis Silhouettes, boss Kayden.
- `.github/workflows/roblox-m13.yml` : checks + publication via Open Cloud (`POST https://apis.roblox.com/universes/v1/{universe}/places/{place}/versions?versionType=Published`), secret `ROBLOX_API_KEY`, variables `UNIVERSE_ID`, `LOBBY_PLACE_ID`, `TOME1_PLACE_ID`.
- `docs/jeu/` : version **navigateur** du Tome 1 (Three.js + PeerJS), testée (19 tests + e2e), non publiée (il faut fusionner dans `main` pour GitHub Pages).
- Histoire : `twist/01_bible_de_la_saga.md`, récap `twist/recap_t*.md`, 4 tomes écrits (`tome2/`, `tome3/`, `tome4/`, le Tome 1 n'existe qu'en PDF). Twist final : Darius porte une partie de l'âme de Léopold, « Nous sommes Léopold ».

## À faire dans cette session
1. **Lis mon jeu** : comment sont détectés les admins (liste d'ID, groupe, gamepass ?), s'il y a un lobby, combien de lieux (Places) il a, quelle structure (Rojo ou autre).
2. Propose un **plan court** de la passerelle avant de coder : bouton M13 (admin seulement, vérifié **côté serveur**), écran Solo/Multi, saisie du code, téléportation. Privilégie **un seul lieu supplémentaire** si possible (utiliser `game.PrivateServerId` pour distinguer lobby et partie) afin de limiter les Place ID.
3. Branche le code M13 (réutilise `roblox/src/shared` et `roblox/src/tome1`) sans toucher à l'existant. Ajoute des tests et fais passer la CI.
4. Dis-moi **où mettre la clé API** et quelles valeurs renseigner (voir sécurité).

## Sécurité (non négociable)
- Je ne colle **jamais** la clé Roblox dans le chat ni dans un fichier. Elle va dans GitHub : *Settings → Secrets and variables → Actions → Secret `ROBLOX_API_KEY`*. L'Universe ID et les Place ID vont en *Variables*.
- La clé n'a besoin que de **Place Publishing : Write**, limitée à mon expérience, avec une expiration courte.
- La publication **remplace la version** d'un lieu sur Roblox : montre-moi ce qui change avant toute publication, et ne publie que sur ma demande explicite.
- Ne crée pas de pull request sans que je le demande. Ne publie rien sans mon accord.
