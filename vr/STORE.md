# Publier PROJECT-M13 VR sur Meta Quest

1. Dépôt GitHub > Actions > **Créer la clé de signature VR** > Run workflow.
2. Télécharger l'artefact `vr-keystore` (zip) : `keystore.b64` et `password.txt`.
3. Dépôt > Settings > Secrets and variables > Actions > New repository secret :
   - `VR_KEYSTORE_B64` = contenu de `keystore.b64`
   - `VR_KEYSTORE_PASSWORD` = contenu de `password.txt`
   Puis supprimer l'artefact. **Garde une copie de la clé** (gestionnaire de mots de passe) : sans elle, plus de mises à jour.
4. Actions > **Build VR APK (release)** > Run workflow : l'APK signé est dans l'artefact `project-m13-vr-release-apk`
   et sur la branche `vr-apk-release`.
5. Meta Developer Dashboard > ton app > Distribution > Builds : envoyer l'APK sur un canal de test (ALPHA / BETA).

L'identifiant de paquet est `com.siroxtag.projectm13` : il ne peut plus changer après le premier envoi.
Ne mets JAMAIS la clé secrète de l'application ni le token utilisateur Meta dans le dépôt : uniquement dans les secrets.
