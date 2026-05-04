# L'Anthropie — Mandats fonctionnels (rôles sans personnes)

> *Sept rôles fonctionnels que l'édifice CC0 a besoin de couvrir pour tenir dans le temps. Décrits **anonymement et fonctionnellement** — durée, conditions d'entrée, conditions de sortie, rotation. Pas de noms, pas de titres ronflants. Une personne peut tenir plusieurs rôles ; un rôle peut tourner.*

CC0 1.0 Universal. Document de gouvernance provisoire. Modifiable par Pull Request avec discussion publique de 7 jours et bloc *contre-voix* (cf. [DECISIONS.md ADR-0010](decisions/)).

---

## Pourquoi des mandats sans personnes

Une fédération informelle CC0 anonyme a besoin de **fonctions** plus qu'elle n'a besoin de personnes nommées. Inscrire des rôles fonctionnels permet :

- de **reprendre** un rôle quand son détenteur s'efface (cf. [DECISIONS.md ADR-0002 anonymat](decisions/), [ROADMAP Phase 4 auto-effacement](roadmap/)) ;
- d'**éviter la recentralisation** sur un mainteneur charismatique (cf. [DECISIONS.md ADR-0008 multi-référents](decisions/)) ;
- de **rendre visible** le périmètre de chaque charge sans en faire une identité personnelle ;
- de **faciliter le fork** ([FORKING.md](forker/)) — un repreneur sait quels rôles couvrir avant de relancer.

Ces mandats ne sont pas exhaustifs. À mesure que l'édifice grandit (ou rétrécit), ils évoluent par PR.

---

## Les sept rôles fonctionnels

### 1. Gardien·ne de doctrine

- **Périmètre** : surveille la cohérence doctrinale de l'édifice. Vérifie que les PR sur le noyau (cf. [ADR-0010](decisions/)) embarquent leur bloc contre-voix. Signale dérives lexicales suspectes (cf. backlog : linter de capture lexicale).
- **Conditions d'entrée** : avoir lu intégralement les 12 couches + KERNEL + SAFETY + DECISIONS + REFUTATION. Avoir contribué publiquement (Issues, PR, discussions) sur ≥ 6 mois.
- **Conditions de sortie** : retrait volontaire à tout moment (annoncé publiquement dans une Issue). Retrait obligatoire si pratique professionnelle commerciale du nom Anthropie en parallèle.
- **Durée recommandée** : 18 mois, **renouvelable une fois** par convergence multi-référents (ADR-0008). Au-delà, rotation obligatoire.
- **Multiplicité** : au moins 2 personnes simultanément, idéalement 3.
- **Anti-pattern à éviter** : devenir l'arbitre unique de "ce qui est *vraiment* Anthropie".

### 2. Mainteneur·euse du dépôt

- **Périmètre** : merge les PR conformes après convergence ADR-0008 + 7 jours de discussion. Maintient la CI/CD GitHub Actions, le déploiement GitHub Pages, le DNS Infomaniak, le SSL. Sait reprendre le `prepare-content.mjs` et l'Astro build.
- **Conditions d'entrée** : compétence technique git + Astro + Node ≥ 22 + GitHub Actions. Avoir contribué techniquement ≥ 3 PR mergées.
- **Conditions de sortie** : retrait volontaire avec passation documentée (au moins 30 jours de chevauchement avec un successeur).
- **Durée recommandée** : 24 mois, renouvelable. Pas de limite stricte tant que la passation reste possible.
- **Multiplicité** : au moins 2 personnes ayant les droits d'admin GitHub (bus factor protégeable).
- **Anti-pattern à éviter** : centraliser les credentials, ne pas documenter, créer une dépendance personnelle au stack.

### 3. Arbitre sécurité

- **Périmètre** : reçoit les signalements via [ISSUE_TEMPLATE 05-safety](https://github.com/SanTiepi/anthropie-edifice/blob/master/.github/ISSUE_TEMPLATE/05-safety-garde-fou.md) (violations de [SAFETY.md](garde-fous/), usage abusif du nom, dérive sectaire, appropriation culturelle). Coordonne la désolidarisation publique si justifiée. Mobilise les autorités civiles compétentes pour les cas pénaux.
- **Conditions d'entrée** : formation ou expérience documentée en protection de l'enfance, prévention de l'emprise, droit pénal, ou éthique appliquée. Avoir lu intégralement SAFETY.md et REFUTATION.md.
- **Conditions de sortie** : retrait volontaire à tout moment. Retrait obligatoire si conflit d'intérêts (poste rémunéré dans une organisation exposée par un signalement actif).
- **Durée recommandée** : 12 mois, renouvelable. Rotation rapide pour éviter la fatigue émotionnelle.
- **Multiplicité** : 2 personnes minimum, par convention venant de juridictions différentes (France + Suisse, ou autre paire).
- **Anti-pattern à éviter** : se substituer aux autorités civiles compétentes, faire de la modération à la place du système judiciaire.

### 4. Archiviste

- **Périmètre** : maintient l'intégrité historique du repo. Vérifie les sauvegardes hors-ligne (Internet Archive, Software Heritage Foundation). Tient à jour le `CITATION.cff`. Documente les versions et les snapshots significatifs.
- **Conditions d'entrée** : familiarité avec git, Software Heritage / Internet Archive, métadonnées académiques (CFF, BibTeX, Dublin Core). Patience pour le travail de long terme.
- **Conditions de sortie** : retrait volontaire, passation documentée.
- **Durée recommandée** : 36 mois (rôle de stabilité), renouvelable.
- **Multiplicité** : 2 personnes idéalement, mais 1 minimum suffisant tant que les outils externes (SWH, Archive.org) sont configurés en automatique.
- **Anti-pattern à éviter** : transformer l'archive en gatekeeping (refuser des modifications sous prétexte d'intégrité).

### 5. Médiateur·trice juridique

- **Périmètre** : interface non-représentative avec institutions juridiques (BIE Genève, UNICEF Innocenti, Eurochild, comités CRC nationaux). Relit les articles 31bis-duodecies pour qualité juridique avant tout dépôt formel. Coordonne les éventuelles actions sur licence, marque, propriété intellectuelle.
- **Conditions d'entrée** : formation juridique (master de droit ou équivalent), idéalement spécialisation droits enfants ou droits humains. Compréhension explicite de CC0 et acceptation de l'anonymat.
- **Conditions de sortie** : retrait volontaire. Retrait obligatoire si activité de lobbying privé en parallèle pour des intérêts contradictoires.
- **Durée recommandée** : 24 mois, renouvelable.
- **Multiplicité** : 1 personne suffit en pratique mais idéalement 2 dans des juridictions différentes pour internationaliser le portage.
- **Anti-pattern à éviter** : devenir représentant officiel de l'édifice (*Anthropie Network* n'a pas de représentant — c'est doctrinal).

### 6. Coordinateur·trice de traduction

- **Périmètre** : suit les efforts de traduction (priorité [CONTRIBUTING.md §5](contribuer/) : EN, ES, AR, ZH, HI, SW, PT). Maintient le glossaire des termes-clé en cohérence inter-langues. Veille à l'adaptation culturelle sans dénaturer la doctrine.
- **Conditions d'entrée** : maîtrise fonctionnelle ≥ 2 langues incluant le français. Accord explicite avec la doctrine anonymat (ne pas signer la traduction nominalement).
- **Conditions de sortie** : retrait volontaire avec passation des traductions en cours.
- **Durée recommandée** : 18 mois, renouvelable.
- **Multiplicité** : 1 par paire de langues prioritaires. Peut être tenu par une même personne pour plusieurs paires.
- **Anti-pattern à éviter** : imposer une *vraie* version (FR), traiter les traductions comme dérivées subordonnées. Chaque traduction est une *fork de portage* à part entière.

### 7. Témoin de prototypes

- **Périmètre** : reçoit les retours de prototypes (cf. [PROTOTYPES.md](prototyper/) : 2h / 1 mois / 12 mois). Anonymise et indexe publiquement les apprentissages. Signale les patterns récurrents (succès, échecs, dérives) à la fédération.
- **Conditions d'entrée** : avoir documenté ≥ 1 prototype Anthropie soi-même. Compréhension explicite de la charte anti-appropriation et de SAFETY.md §1 (mineurs).
- **Conditions de sortie** : retrait volontaire. Retrait obligatoire si tension émerge avec un prototype dont la personne est partie prenante.
- **Durée recommandée** : 12 mois, renouvelable.
- **Multiplicité** : 2 personnes minimum, idéalement de cultures différentes (pour réduire le biais WEIRD dans le filtrage des retours).
- **Anti-pattern à éviter** : devenir l'évaluateur officiel des prototypes (*Anthropie* n'évalue pas, *Anthropie* documente — la communauté juge).

---

## Principes communs aux mandats

- **Aucun titre n'est porté en public**. Pas de "*Gardien de doctrine d'Anthropie*" sur LinkedIn. Le rôle est interne à la fédération.
- **Aucune rémunération directe par l'édifice**. CC0 → pas d'argent. Si un rôle est rémunéré (par fondation, État-pilote, employeur du tenant), c'est une affaire externe, déclarée publiquement comme conflit d'intérêts potentiel.
- **Rotation explicite**. Une personne ne devrait pas tenir le même rôle plus de la durée recommandée + 1 renouvellement. Au-delà, recentralisation = risque doctrinal.
- **Bus factor minimal**. Tout rôle critique a au moins 2 tenants. Si un rôle reste vacant > 90 jours, signaler dans une Issue épinglée.
- **Passation documentée**. Tout retrait inclut un document de passation public (Issue ou PR), même bref — pour éviter la perte tacite de mémoire.
- **Aucun mandat ne donne pouvoir d'exclusion juridique**. La doctrine CC0 / anonymat (cf. [DECISIONS.md ADR-0001-0002](decisions/)) prime sur tout mandat. Au mieux, désolidarisation publique.

---

## État actuel des mandats

*(Mai 2026 — phase Transmission embryonnaire.)*

| Rôle | Tenant·s actuel·s | Statut |
|---|---|---|
| Gardien·ne de doctrine | — | **vacant** (1 candidature implicite : commissariat originel ; 0 confirmé) |
| Mainteneur·euse du dépôt | — | **vacant** (commissariat originel, à formaliser ou déléguer) |
| Arbitre sécurité | — | **vacant** (priorité haute si premier prototype lancé) |
| Archiviste | — | **vacant** (Internet Archive et Software Heritage indexent automatiquement, mais pas de revue) |
| Médiateur·trice juridique | — | **vacant** (bloquant pour Phase 1 ROADMAP — dépôt BIE Genève) |
| Coordinateur·trice de traduction | — | **vacant** (toutes les traductions sont à *À démarrer*) |
| Témoin de prototypes | — | **vacant** (aucun prototype documenté à ce jour) |

Tous les rôles sont **vacants ou tenus par défaut** par le commissariat originel. C'est précisément l'état d'un édifice qui cherche porteurs.

---

## Postuler à un rôle

Pas de procédure formelle. Ouvrir une [Issue GitHub](https://github.com/SanTiepi/anthropie-edifice/issues) avec :

- Le rôle visé.
- Une présentation **fonctionnelle** (pas biographique) de votre adéquation : quelles compétences, quelle disponibilité, quelle juridiction de résidence.
- Un engagement de respecter la doctrine anonymat (votre identité civile peut être connue dans la discussion mais n'apparaîtra jamais en signature de l'édifice).
- Optionnellement, un signalement d'éventuels conflits d'intérêts.

Discussion publique 7 jours minimum. Convergence multi-référents pour confirmation. Pas de vote majoritaire — délibération assumée.

---

*« Un mandat sans personne n'est pas un poste vacant. C'est une fonction prête à être saisie quand quelqu'un veut servir l'édifice à ce niveau-là. »*
