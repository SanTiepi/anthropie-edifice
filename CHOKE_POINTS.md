# L'Anthropie — Carte des points d'étouffement

> *Chaque dépendance qui peut arrêter l'édifice en une seule perte (personne, compte, format, outil, savoir), avec un substitut opérable même s'il est inférieur. Pour traiter la continuité réelle avant l'optimisation.*

CC0 1.0 Universal. Document de résilience. Pull Request bienvenue pour amender — qui voit un point d'étouffement non listé contribue.

**Pourquoi ce document ?** Un édifice CC0 anonyme ne peut pas se permettre les illusions habituelles d'organisation établie. Si un seul élément critique tombe (un mainteneur, un compte GitHub, un domaine, un format), et qu'il n'a pas de substitut documenté, l'édifice s'arrête. Mieux vaut nommer publiquement ces points avant qu'ils ne défaillent.

---

## Échelle de criticité

| Niveau | Signification | Délai de récupération avec substitut |
|---|---|---|
| 🔴 **CRITIQUE** | Perte = arrêt immédiat de la transmission | < 7 jours |
| 🟠 **MAJEUR** | Perte = dégradation visible, ralentissement portage | < 30 jours |
| 🟡 **MODÉRÉ** | Perte = inconvénient géré sans choc | < 90 jours |
| 🟢 **FAIBLE** | Perte tolérable, redondance déjà présente | tolérable durablement |

---

## 1. Points d'étouffement — personnes

| Point d'étouffement | Niveau | Substitut opérable |
|---|---|---|
| Le commissariat originel (mainteneur unique pour l'instant) | 🔴 | Tout fork dans [FORKING.md](forker/) après son retrait. La doctrine CC0 garantit que personne n'est nécessaire pour la **survie** du contenu — seulement pour le **portage actif**. |
| Aucun arbitre sécurité formé | 🟠 | En cas de signalement [`05-safety-garde-fou`](https://github.com/SanTiepi/anthropie-edifice/issues), redirection immédiate vers autorités civiles compétentes (CIC CH, Miviludes FR, [findahelpline.com](https://findahelpline.com)) sans attendre traitement interne. |
| Aucun médiateur juridique pour relire 31bis-duodecies avant dépôt BIE Genève | 🟠 | Reporter le dépôt formel jusqu'à recrutement d'un juriste ou abandon du dépôt comme objectif officiel (cf. [REFUTATION.md §1](refutation/) auto-effacement). |
| Aucun co-design autochtone effectif sur Couches 7, 10, 11 | 🟠 | Marquer publiquement ces couches comme "référence sans co-design" en attendant. Cf. [OBJECTIONS.md §3](objections/). |
| Aucun coordinateur traduction | 🟡 | Rester en français uniquement jusqu'à ce qu'un porteur volontaire émerge. Pas de pseudo-traduction par défaut. |

---

## 2. Points d'étouffement — comptes et infrastructures

| Point d'étouffement | Niveau | Substitut opérable |
|---|---|---|
| Compte GitHub `SanTiepi/anthropie-edifice` (org GitHub Microsoft) | 🟠 | Mirroir [Software Heritage](https://www.softwareheritage.org/) (indexation automatique) + [Internet Archive](https://web.archive.org/) (indexation manuelle si besoin). Repli : Codeberg ou GitLab.com via clone direct. |
| Domaine `anthropie.org` (Infomaniak Suisse) | 🔴 | URL fallback `https://santiepi.github.io/anthropie-edifice/` toujours actif (GitHub Pages sous-domaine, n'expire pas tant que le repo existe). Domaine secondaire pourrait être enregistré chez registrar tiers (Gandi, Cloudflare Registrar) si Infomaniak défaille. |
| Email `contact@anthropie.org` (alias Infomaniak — non encore actif) | 🟢 | Discussions GitHub publiques sont le canal officiel. L'email n'a jamais été mis en exergue. |
| Hébergement GitHub Pages | 🟠 | Repli vers Cloudflare Pages, Netlify (anonyme), ou auto-hébergé. Le site est statique pur (aucun runtime), donc redéployable partout en 1h. |
| SSL Let's Encrypt (auto-renouvelé par GitHub) | 🟢 | En cas de panne LE, GitHub Pages bascule automatiquement vers son propre cert. Pas de point d'étouffement réel. |
| DNS Infomaniak | 🟠 | Cloudflare DNS gratuit prend le relais en < 1h sur changement nameservers. |

---

## 3. Points d'étouffement — formats et outils

| Point d'étouffement | Niveau | Substitut opérable |
|---|---|---|
| Astro 6.x (framework de build du site) | 🟡 | Le contenu est en Markdown pur. En cas de disparition d'Astro, migration vers Hugo, Eleventy, ou Pandoc → HTML. Estimation : 1-2 jours de mainteneur compétent. |
| Node.js 22+ (requis par Astro) | 🟡 | Pour les .md, *aucune* dépendance Node — lecture directe possible avec n'importe quel viewer Markdown. Le build statique précompilé reste lisible sans JS. |
| `prepare-content.mjs` (script Node ESM custom) | 🟡 | 130 lignes. Réécriture en Bash ou Python en 2-3h si Node disparaît. Le script lui-même est sans dépendance externe (`fs`, `path`, `url` standards). |
| Format Markdown CommonMark | 🟢 | Standard universel. Aucune dépendance vendor-locked. Lisible en texte brut. |
| Format SVG (schéma 12 couches, OG image, favicons) | 🟢 | Standard W3C. Lisible texte brut, convertible en PNG/JPEG via ImageMagick, Inkscape, librsvg. |
| Format CFF (CITATION.cff) | 🟢 | YAML standard, lisible texte brut, convertible BibTeX/RIS via outils citation. |

---

## 4. Points d'étouffement — savoirs tacites

C'est le plus insidieux : ce qui est **dans la tête** d'un mainteneur sans être documenté.

| Point d'étouffement | Niveau | Substitut opérable |
|---|---|---|
| Comment configurer les nameservers Infomaniak pour pointer vers GitHub Pages | 🟠 | Documenter dans `site/README.md` (à compléter à l'occasion d'iter ultérieures du loop). |
| Comment debugger un build Astro qui échoue avec `prepare-content.mjs` | 🟡 | Le script log clairement (`[prepare-content] N/N files prepared`). Erreurs Astro affichent stack trace. |
| Quels juristes accepteraient de relire 31bis-duodecies CC0 sans attribution | 🟠 | À documenter dès qu'un contact aboutit, dans une Issue épinglée tag `legal`. |
| Quelles communautés autochtones ont mandat reconnu pour co-design Couche 11 | 🟠 | À documenter dans une Issue épinglée tag `co-design-souverain`. Pour l'instant : aucun contact établi. |
| Le raisonnement derrière chaque choix doctrinal | 🟢 | Couvert par [DECISIONS.md](decisions/) (10 ADR explicites). |
| Le critère pour suspendre une couche | 🟢 | Couvert par [REFUTATION.md §2](refutation/). |

---

## 5. Points d'étouffement — dépendances externes non-substituables

| Dépendance | Niveau | Pourquoi non-substituable | Atténuation |
|---|---|---|---|
| Convention relative aux droits de l'enfant (CRC ratifiée par 196 États) | 🟢 | Cadre juridique stable depuis 1989. Aucun précédent d'abrogation massive. | Aucune ; risque acceptable. |
| Standard W3C Verifiable Credentials (Couche 3 Open Badges 3.0) | 🟡 | Si W3C abandonne VC, l'infrastructure Pont des Certifications doit être repensée. | Documenter alternative (clé publique git + checksum simple) en cas de bascule. |
| Software Heritage Foundation (archive code source pérenne) | 🟢 | Aucune dépendance vitale ; complément, pas un point unique. | — |
| Internet Archive (Wayback Machine) | 🟢 | Idem, complément. | — |

---

## 6. Ce que cette carte n'inclut PAS (volontairement)

- **Plateformes de réseaux sociaux** : aucune dépendance. Pas de compte Twitter/X, Mastodon, LinkedIn, Bluesky portant le nom Anthropie. C'est doctrinal.
- **Services de newsletter ou CRM** : aucun. Cf. [LEGAL_BOUNDARIES.md §5](cadre/).
- **Services d'analytics** : aucun. Cf. doctrine anti-marketing.
- **Services AI commerciaux** : aucun en runtime. Le site est statique pur.
- **Comptes de fondation, organisme tiers** : aucun. L'édifice n'a pas de personne morale.

L'absence de ces dépendances est un choix doctrinal qui réduit considérablement la surface d'étouffement. C'est la meilleure défense.

---

## 7. Procédure si un point d'étouffement défaille

**Si une personne disparaît / se retire** :

1. Si elle est titulaire d'un mandat (cf. [MANDATES.md](mandats/)), ouvrir Issue épinglée tag `governance` annonçant le retrait.
2. Si elle est mainteneur GitHub avec admin rights, le second mainteneur (ADR-0008 multi-référents) prend le relais.
3. Si aucun second mainteneur, basculer vers fork (cf. [FORKING.md](forker/)) hébergé par un autre porteur volontaire.

**Si un compte / domaine défaille** :

1. Vérifier le mirroir Software Heritage pour récupérer l'état antérieur.
2. Republier sur infrastructure de substitution (URL fallback `santiepi.github.io/anthropie-edifice/` toujours actif).
3. Annoncer publiquement la nouvelle URL (via les forks existants, références académiques, Software Heritage ID).

**Si un format / outil défaille** :

1. Le contenu Markdown reste lisible avec n'importe quel viewer.
2. Migration de stack documentée dans [DECISIONS.md ADR-0005](decisions/) (Astro est un choix réversible).

---

## 8. Auto-audit recommandé tous les 12 mois

Vérifier :

- [ ] Aucun mandat critique vacant > 90 jours sans annonce publique.
- [ ] Le mirroir Software Heritage indexe la dernière version.
- [ ] Le domaine `anthropie.org` est encore enregistré et pointe vers GitHub Pages.
- [ ] Le repo est encore accessible et clonable depuis n'importe où.
- [ ] La build pipeline GitHub Actions fonctionne (CI verte sur main).
- [ ] L'URL fallback `santiepi.github.io/anthropie-edifice/` répond 200.
- [ ] Au moins un fork connu existe (santé du portage distribué).

Inscrire le résultat dans une Issue épinglée tag `audit-annuel`.

---

*« On ne supprime pas les points d'étouffement — on les rend nommables, donc négociables. »*
