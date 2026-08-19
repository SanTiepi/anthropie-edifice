# Le mot du jour — Instagram, TikTok, Threads, Facebook

Chaîne de publication quotidienne pour [anthropie.org/mots](https://anthropie.org/mots/).
Chaque matin, un mot du dictionnaire est composé en carte typographique et en vidéo 9:16,
puis publié automatiquement. **Le mot posté est exactement celui qu'affiche le site ce jour-là.**

```
motdujour.py   le mot du jour (réplique exacte du tirage du site)
son.py         voix française hors ligne (Piper) + nappe générée ici — aucun droit tiers
render.py      carte 1080×1350 (feed) · couverture 1080×1920 · vidéo 9:16 calée sur la voix
legende.py     légendes Instagram, TikTok et Threads
assets.py      hébergement public des fichiers (branche social-assets + jsDelivr)
instagram.py   Graph API — publication du Reel
tiktok.py      Content Posting API v2 — publication ou dépôt en boîte de réception
threads.py     Threads API — conteneur puis publication
facebook.py    Graph API — photo sur une Page
coffre.py      réécriture des secrets GitHub (les jetons tournent)
publier.py     l'orchestrateur
```

## Le son

La vidéo n'est plus muette. `son.py` fait lire le mot puis sa définition par une voix
française synthétisée **hors ligne** (Piper, modèle `fr_FR-siwis-medium`, licence MIT), et la
pose sur une nappe **générée par le programme** — pas un morceau sous licence, donc rien à
craindre des scanners audio des plateformes. La durée de la vidéo suit celle de la voix, et
l'animation se cale dessus : le mot apparaît quand il est dit, la définition quand elle est lue.

Si Piper manque ou échoue, la nappe seule est montée ; si numpy manque, la vidéo reste muette.
Une chaîne quotidienne ne doit jamais casser pour un problème de son. `SANS_SON=1` la coupe.

## Essayer sans rien publier

```bash
pip install -r social/requirements.txt      # + ffmpeg
python3 social/publier.py --blanc           # visuels + légendes du jour dans social/out/
python3 social/publier.py --lot 30          # 30 jours d'avance, pour relire
```

## Le tirage du mot

Le site tire son mot du jour côté navigateur, avec un hash de la date. Ce hash n'est pas un
FNV-1a propre : `h * 16777619` dépasse 2⁵³ en JavaScript, donc le moteur arrondit, et `h ^= c`
repasse en entier **signé**. `motdujour.py` reproduit les deux imprécisions — sans elles, on
posterait un autre mot que celui affiché sur le site. Vérifié sur 400 jours consécutifs, zéro
divergence. Si un jour le site change son tirage, ce fichier doit changer avec lui.

---

## Montage — ce qui doit être fait à la main

### 1. Les deux comptes

- **Instagram** : créer le compte, puis le passer en **compte professionnel** (Paramètres →
  Type de compte). L'API ne publie que sur un compte Business ou Creator, et il doit être
  **relié à une Page Facebook** (Paramètres → Partage et intégrations). Sans Page, pas d'API.
- **TikTok** : créer le compte. Rien de particulier côté compte.

Poignée suggérée, identique des deux côtés : `lesmots.anthropie` (ou `anthropie.mots`).
Bio : `478 mots pour ce que la langue avait laissé muet · CC0 · anthropie.org/mots`.

### 2. L'application Meta (Instagram)

On passe par **Instagram API with Instagram Login** : hôte `graph.instagram.com`, jeton
utilisateur Instagram, **aucune Page Facebook requise**. (L'autre chemin, *Facebook Login*,
impose un compte relié à une Page et un jeton de Page ; il reste disponible avec
`IG_LOGIN_MODE=facebook`, mais il n'apporte rien ici.)

1. [developers.facebook.com](https://developers.facebook.com) → *Mes applications* → Créer,
   cas d'usage **Autre** → type **Business**.
2. Ajouter le produit **Instagram** → **API setup with Instagram login**.
3. Étape 1 : *Generate access tokens* → ajouter le compte Instagram professionnel.
   Étape 3 : *Set up Instagram business login* → noter l'**Instagram App ID** et
   l'**Instagram App Secret**, et déclarer une **OAuth redirect URI** (n'importe quelle URL
   https qu'on contrôle — `https://anthropie.org/` fait l'affaire : on ne lit que le
   paramètre `code` dans la barre d'adresse).
4. Permissions demandées : `instagram_business_basic` et `instagram_business_content_publish`.
5. Flux d'autorisation, à faire une seule fois dans le navigateur :
   ```
   https://www.instagram.com/oauth/authorize
     ?client_id=INSTAGRAM_APP_ID
     &redirect_uri=https://anthropie.org/
     &response_type=code
     &scope=instagram_business_basic,instagram_business_content_publish
   ```
   Après acceptation, l'URL de retour contient `?code=…` (jeter le `#_` final). Le code vaut
   1 heure et ne sert qu'une fois.
6. Code → jeton court :
   ```
   curl -X POST https://api.instagram.com/oauth/access_token \
     -F client_id=INSTAGRAM_APP_ID -F client_secret=INSTAGRAM_APP_SECRET \
     -F grant_type=authorization_code -F redirect_uri=https://anthropie.org/ -F code=LE_CODE
   ```
   La réponse donne aussi le `user_id` : c'est l'`IG_USER_ID`.
7. Jeton court → **jeton longue durée** (60 jours) :
   ```
   curl "https://graph.instagram.com/access_token?grant_type=ig_exchange_token\
   &client_secret=INSTAGRAM_APP_SECRET&access_token=JETON_COURT"
   ```

Le workflow `jeton-instagram.yml` prolonge ce jeton le 1er de chaque mois. Attention :
un jeton non rafraîchi pendant 60 jours meurt définitivement — il faut alors refaire
l'étape 5. Le rafraîchissement exige aussi que le jeton ait plus de 24 h.

**Accès** : *Standard Access* suffit pour un compte qu'on possède et qu'on a ajouté à l'app.
L'*Advanced Access* (revue Meta) n'est nécessaire que pour publier sur des comptes tiers.

### 3. L'application TikTok

1. [developers.tiktok.com](https://developers.tiktok.com) → créer une app.
2. Ajouter le produit **Content Posting API**, scopes `video.publish` et `video.upload`.
3. Ajouter le compte comme *target user* / testeur, autoriser l'app (flux OAuth) et garder le
   `refresh_token` (valable 365 jours, mais **il tourne à chaque rafraîchissement** — d'où
   `coffre.py`, qui le réécrit dans les secrets à chaque exécution).
4. **Audit** : tant que l'app n'est pas auditée, TikTok exige **deux conditions à la fois**
   pour la publication directe — le compte doit être en **privé** *et* la requête doit
   demander `privacy_level=SELF_ONLY`. L'une sans l'autre renvoie
   `unaudited_client_can_only_post_to_private_accounts`. Deux options en attendant :
   - `TIKTOK_MODE=inbox` (variable de dépôt) : la vidéo arrive dans la boîte de réception
     TikTok du compte, une notification, deux tapes pour publier. Fonctionne immédiatement.
     **L'endpoint inbox n'accepte aucun `post_info`** : la légende ne peut pas être
     transmise par l'API. Elle est déposée dans le résumé du run GitHub Actions, en bloc
     copiable, pour être collée au moment de valider le brouillon.
   - Demander l'audit, puis basculer sur `TIKTOK_MODE=direct` : publication réelle, zéro geste.

   C'est la seule étape où l'automatisation dépend d'un tiers. Le reste est autonome.

### 3 bis. Threads et la Page Facebook

**Threads** est le canal le mieux ajusté au projet : un fil de texte, où un mot et sa
définition tiennent sans mise en scène. L'API est officielle et **n'exige aucune revue pour
publier sur son propre compte**.

1. Créer le compte Threads depuis l'Instagram existant (Threads reprend la même poignée).
2. Le produit *Threads API* **n'apparaît pas** sur une app Meta de l'ancien modèle : il faut
   créer une **app dédiée** avec le cas d'usage *Access the Threads API*.
3. Redirect URI : `https://anthropie.org/mots/`. Scopes : `threads_basic`,
   `threads_content_publish`.
4. `python3 social/oauth_threads.py --client-id <APP_ID>` affiche l'URL d'autorisation, puis
   `--url "<URL de retour>"` échange le code et pose les secrets. Le secret de l'app est saisi
   à l'invite, sans écho.

Le jeton vit 60 jours ; `jeton-instagram.yml` le prolonge le 1er de chaque mois.

**La Page Facebook** est un dépôt d'archive : la portée organique d'une page neuve est
faible, mais le branchement est presque gratuit. Il faut un jeton de Page avec
`pages_manage_posts` et `pages_read_engagement` — en mode développement, l'administrateur de
l'app n'a pas besoin de revue pour sa propre Page.

### 4. Les secrets du dépôt

`Settings → Secrets and variables → Actions` :

| Secret | D'où il vient |
|---|---|
| `IG_USER_ID` | `user_id` renvoyé à l'échange du code (étape 2.6) |
| `IG_ACCESS_TOKEN` | jeton longue durée (étape 2.7) |
| `FB_APP_ID` / `FB_APP_SECRET` | uniquement en `IG_LOGIN_MODE=facebook` — inutiles autrement |
| `TIKTOK_CLIENT_KEY` / `TIKTOK_CLIENT_SECRET` | application TikTok |
| `TIKTOK_REFRESH_TOKEN` | jeton de rafraîchissement initial |
| `THREADS_TOKEN` / `THREADS_USER_ID` | `social/oauth_threads.py --client-id <id>` — canal sauté proprement s'ils manquent |
| `FB_PAGE_ID` / `FB_PAGE_TOKEN` | jeton de Page (permanent s'il dérive d'un jeton utilisateur longue durée) |
| `GH_PAT` | jeton personnel, permission *Secrets: read and write* sur ce dépôt — sert à réécrire les jetons qui tournent |

Variables (`Variables`, pas `Secrets`) : `TIKTOK_MODE` = `direct` ou `inbox` ; `IG_LOGIN_MODE` = `instagram` (défaut) ou `facebook`.

### 5. Vérifier

```
Actions → « Mot du jour » → Run workflow → blanc: true     # fabrique sans publier
Actions → « Mot du jour » → Run workflow                    # publie pour de vrai
```

Le cron tourne à 06:05 UTC — 08:05 à Zurich en été, 07:05 en hiver. En cas d'échec, les
visuels du jour sont conservés en artefact pendant 14 jours.

---

## Ce que la chaîne ne fait pas

- **Elle ne crée pas les comptes** : vérification par téléphone, obligatoirement humaine.
- **Elle ne relance pas un jeton mort** : un jeton Instagram non rafraîchi pendant 60 jours
  exige de refaire le flux OAuth à la main.
- **Elle ne contourne pas l'audit TikTok** : sans audit, la publication reste privée. C'est
  une règle de la plateforme, pas une limite du code.
- **Elle ne répond pas aux commentaires.** Un mot par jour ouvre une conversation ; personne
  ne la tient pour l'instant.
- **Elle ne mesure rien.** Aucune remontée d'audience n'est branchée.
