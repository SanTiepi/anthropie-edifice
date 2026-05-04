# L'Anthropie — Reconstruction et mode dégradé

> *Comment rebuilder le site depuis zéro sur un hébergement banal, vérifier que la reconstruction est fidèle, et publier l'édifice sans réseau stable si l'infrastructure défaille.*

CC0 1.0 Universal. Document opérationnel destiné aux mainteneurs, repreneurs anonymes (cf. [`FORKING.md`](forker/)), et chercheurs souhaitant vérifier l'intégrité du site rendu.

---

## 1. Pré-requis pour reconstruction complète

Si vous voulez reconstruire `anthropie.org` **identique** à partir des sources :

| Outil | Version testée | Substitut acceptable |
|---|---|---|
| Git | ≥ 2.40 | n'importe quelle version raisonnable |
| Node.js | ≥ 22.12.0 | Node 20.x fonctionne probablement, non testé |
| npm | ≥ 10 (livré avec Node 22) | pnpm, yarn — non testés mais devraient marcher |
| Une connexion réseau | une fois (pour `npm install`) | mirroir de `node_modules/` archivé en local |

**Aucun outil propriétaire n'est requis.** Aucun compte sur un service tiers. Aucune clé API.

---

## 2. Reconstruction pas-à-pas (15 minutes sur machine standard)

```sh
# Cloner
git clone https://github.com/SanTiepi/anthropie-edifice.git anthropie
cd anthropie

# Installer les dépendances Astro (~80 MB de node_modules)
cd site
npm ci

# Bâtir le site (prepare-content puis astro build)
npm run build

# Servir localement pour vérification
npm run preview   # http://localhost:4321
```

Sortie attendue :

```
[prepare-content] N/N files prepared in src/content-md/
…
[build] M page(s) built in ~2 seconds
[build] Complete!
```

`M` = nombre de pages générées (varie selon les fichiers présents au moment de la reconstruction). Habituellement entre 25 et 35.

Le répertoire `site/dist/` contient le site complet, statique, déployable sur n'importe quel hébergement HTML/static.

---

## 3. Vérification d'intégrité

Pour vérifier qu'une reconstruction donne **exactement** le même site qu'une publication antérieure :

```sh
# Hash du site assemblé (Linux/macOS)
find site/dist -type f -exec sha256sum {} \; | sort | sha256sum

# Windows PowerShell équivalent
Get-ChildItem site\dist -Recurse -File | Get-FileHash -Algorithm SHA256 |
  Sort-Object Path | ForEach-Object { $_.Hash } | Out-String |
  Set-Content -NoNewline tmp.txt
Get-FileHash tmp.txt -Algorithm SHA256 ; Remove-Item tmp.txt
```

Comparer le hash obtenu à celui publié dans une release ou un manifest (cf. [backlog : `build-manifest.json` codex iter#4 #2](https://github.com/SanTiepi/anthropie-edifice/blob/master/PROTOTYPES.md), pas encore implémenté).

**Sources de variation possibles entre deux reconstructions** :
- Date d'exécution embarquée par Astro dans certains commentaires HTML.
- Version exacte des dépendances `node_modules/` (résolution `package-lock.json`).
- Plateforme (Linux vs Windows vs macOS) — encodage de fin de ligne.

Pour reproductibilité **byte-identical**, utiliser le même OS + même version Node + même `package-lock.json` pinné.

---

## 4. Reconstruction sans réseau (mode hors-ligne)

Si vous voulez pouvoir reconstruire l'édifice **sans accès Internet** :

```sh
# 1. Une fois, dans un environnement avec réseau :
cd site
npm ci
tar czf node_modules.tgz node_modules/

# 2. Sauvegarder localement :
#    - le repo (git bundle ou .tgz du dossier complet)
#    - node_modules.tgz
#    - une copie de Node.js binaire (https://nodejs.org/dist/)

# 3. Plus tard, sans réseau :
tar xzf repo.tgz && cd anthropie/site
tar xzf ../node_modules.tgz
npm run build  # fonctionne sans Internet
```

Taille totale offline minimale : repo (~1 MB sans `node_modules`) + `node_modules.tgz` (~30-50 MB compressé) + Node binaire (~30 MB) = **~100 MB sur clé USB**.

---

## 5. Mode dégradé canonique

Si l'infrastructure d'origine défaille (cf. [CHOKE_POINTS.md](etouffement/)) — domaine perdu, GitHub indisponible, mainteneur disparu — **le contenu Markdown reste intégralement consultable** sans Astro, sans Node, sans build :

### Niveau 1 — `cat` les fichiers

```sh
# Les 12 couches + KERNEL + SAFETY + REFUTATION + DECISIONS + autres
ls *.md
# Lecture directe : Markdown CommonMark, lisible texte brut
```

C'est doctrinal : aucune information n'est dans une base de données, aucune dans un service externe, aucune dans un compte personnel. Tout est dans des fichiers texte.

### Niveau 2 — Markdown viewer minimal

Tout viewer Markdown rend correctement les fichiers : `bat`, `glow`, `mdcat`, VS Code, GitHub UI, Pandoc, Marked.

### Niveau 3 — HTML statique sans Astro

Conversion en HTML via Pandoc :

```sh
for f in *.md; do
  pandoc -s -t html5 "$f" -o "${f%.md}.html"
done
```

Résultat : 25-30 fichiers HTML autonomes, lisibles dans n'importe quel navigateur, sans CSS/JS.

### Niveau 4 — Impression papier

Tous les fichiers sont conçus pour rester **lisibles à l'impression**. Pandoc → PDF :

```sh
pandoc ANTHROPIE_KERNEL.md -o noyau.pdf
```

Le print stylesheet du site (cf. `site/src/pages/index.astro` et `site/src/layouts/MarkdownLayout.astro`) garantit que les pages s'impriment proprement.

### Niveau 5 — Recopie manuelle

Pour chaque fichier essentiel, le contenu est **assez court pour être recopié à la main** dans un cahier d'environ 50-200 lignes. Le [pacte d'accueil](accueil/), le [test d'adéquation](adequation/), le [glossaire](glossaire/), la [carte des preuves](preuves/) sont particulièrement adaptés à la transmission orale ou manuscrite.

Codex iter#8 #4 (*capsule de recopie manuelle*) propose d'aller plus loin : générer pour chaque fichier une fiche ultra-courte (thèse, 2 citations, 2 ancres, 1 checksum) recopiable. Backlog futur.

---

## 6. Ordre de priorité en mode dégradé

Si seuls **quelques fichiers** peuvent être sauvés (espace USB limité, contrainte papier, etc.), priorité :

1. `LICENSE.md` — la doctrine CC0 elle-même (sans cela, rien n'est légalement clair).
2. `ANTHROPIE_KERNEL.md` — l'édifice en 10 minutes, suffit pour décider si on continue.
3. `SAFETY.md` — protection des humains avant tout prototype.
4. Les 12 fichiers de couche `anthropie_couche_NN_*.md`.
5. `REFUTATION.md` + `OBJECTIONS.md` + `EVIDENCE_MAP.md` — pour qu'un repreneur sache ce qui est solide vs spéculatif.
6. `DECISIONS.md` — les arbitrages doctrinaux (10+ ADR).
7. `FORKING.md` — comment reprendre.
8. Le reste (`GLOSSARY`, `WELCOME`, `LEGAL_BOUNDARIES`, `MANDATES`, `CHOKE_POINTS`, `ENTRY_SCENARIOS`, `PROTOTYPES`, `ADEQUATION`, `ROADMAP`, `CONTRIBUTING`).

Total minimal : ~20 fichiers Markdown ; environ **400-600 KB** non compressé. Tient sur une disquette historique de 1.44 MB. Tient évidemment sur n'importe quel support contemporain.

---

## 7. Drill de reconstruction à froid (recommandé tous les 12 mois)

Codex iter#6 #4 propose un drill : qu'une personne **inconnue** du commissariat originel rebuild + republie l'édifice depuis zéro sur un hébergement banal, sans mémoire tacite, sans contact privé.

Protocole minimal :

1. Recruter un volontaire externe (chercheur curieux, étudiant·e en informatique, autre porteur).
2. Lui demander de reconstruire en suivant **ce document uniquement** (pas de chat, pas d'aide tacite).
3. Mesurer : (a) durée totale, (b) blocages rencontrés, (c) clarification nécessaire dans la doc.
4. Mettre à jour `REPRODUCE.md` avec les améliorations identifiées.
5. Publier le rapport dans une Issue épinglée tag `audit-annuel`.

Si jamais réalisé : noter dans le backlog l'apprentissage (ex. *« la commande X manquait, le drill iter de juin 2027 a documenté le besoin »*).

---

## 8. Vérifications post-reconstruction

Après `npm run build`, vérifier :

- [ ] **Nombre de pages** : `find site/dist -name '*.html' | wc -l` retourne ~25-35 (selon nombre de `.md` au moment du build).
- [ ] **Sitemap** : `cat site/dist/sitemap-0.xml` liste toutes les URLs `/lire/<slug>/`.
- [ ] **Pages accessibles** : ouvrir `site/dist/index.html` dans un navigateur ; cliquer sur les liens internes ; vérifier que `/lire/noyau/`, `/lire/garde-fous/`, etc. répondent.
- [ ] **Liens internes réécrits** : ouvrir `site/dist/lire/noyau/index.html` ; vérifier que les liens `(SAFETY.md)` ont été convertis en `/lire/garde-fous/`.
- [ ] **Source GitHub** : la topnav de chaque page `/lire/` pointe vers le fichier source dans le repo.
- [ ] **CNAME** : `cat site/dist/CNAME` retourne `anthropie.org`.

---

## 9. Republier ailleurs (mirroir indépendant)

Si vous voulez héberger un mirroir de l'édifice sous un autre domaine :

```sh
# Sur votre serveur (n'importe lequel acceptant des fichiers statiques)
rsync -av site/dist/ user@example.com:/var/www/mon-mirroir/

# Ou GitHub Pages d'un autre compte
# 1. Forker le repo (cf. FORKING.md)
# 2. Modifier site/public/CNAME (votre domaine ou suppression)
# 3. Modifier site/astro.config.mjs (champ `site` : votre URL)
# 4. Activer GitHub Pages dans Settings > Pages
```

**Annoncer le mirroir publiquement** : ouvrir une Issue dans le repo d'origine avec tag `lecture-critique` ou `prototype-ou-traduction`, en précisant si votre mirroir est *fidèle* (identique au contenu d'origine), *adapté* (modifications mineures, ex. traduction), ou *divergent* (modifications doctrinales documentées). Cf. [`FORKING.md`](forker/) §6 et codex iter#5 #5 (*Protocole de fédération des miroirs*, backlog futur).

---

## 10. Sauvegardes pérennes

L'édifice est automatiquement archivé par :

- **Software Heritage** : indexation de tous les commits publics du repo. URL pérenne, pas dépendante de GitHub.
- **Internet Archive (Wayback Machine)** : snapshots manuels possibles via [web.archive.org](https://web.archive.org/save/anthropie.org). Recommandé après chaque modification doctrinale majeure.
- **Github lui-même** : tant que GitHub existe et que le repo n'est pas supprimé.
- **Forks** : chaque fork existant est une sauvegarde implicite.

**Pas de sauvegarde sur S3, Glacier, Backblaze ou autre service payant.** Doctrinal — pas de coût récurrent, pas de point d'étouffement supplémentaire.

---

*« Reconstructible sans effort tacite. Publiable sans réseau stable. Le minimum : un cahier, une bougie, un lecteur attentif. »*
