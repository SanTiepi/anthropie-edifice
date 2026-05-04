# L'Anthropie — Journal des arbitrages doctrinaux (mini-ADR)

> *Décisions doctrinales et techniques structurantes, avec alternatives rejetées, raisonnement, et critères de retour arrière. Format mini-ADR (Architecture Decision Record) adapté à un édifice civilisationnel CC0.*

CC0 1.0 Universal. Chaque ADR est immutable une fois mergé — corrections via nouvelle ADR « Supersede ADR-NNNN ». Discussion publique 7 jours minimum avant ajout.

**Pourquoi ce fichier ?** Sans journal des arbitrages, un repreneur futur (humain ou AI dans 5-10 ans) reconstruira mal le raisonnement. Les décisions irréversibles (CC0, anonymat, structure 12 couches, charpente 31bis-duodecies) doivent être documentées avec leurs alternatives explicitement rejetées.

---

## ADR-0001 — Licence CC0 1.0 Universal stricte

- **Date** : 2026-04 (commit initial du repo).
- **Statut** : *Accepted, irréversible.*
- **Contexte** : un édifice civilisationnel proposant une extension juridique CRC peut prétendre à une protection (marque, copyright, IP). Plusieurs alternatives ont été considérées.
- **Décision** : publier intégralement sous CC0 1.0 Universal — domaine public, aucune attribution requise.
- **Alternatives rejetées** :
  - *Creative Commons BY-SA 4.0* (attribution + share-alike) — rejeté car attribution = signature, viole anonymat doctrinal.
  - *MIT/Apache 2.0* — non adapté à un corpus textuel civilisationnel.
  - *Marque déposée « Anthropie® »* — rejeté car incompatible avec « personne ne le possède ».
  - *Modèle freemium / contenu premium* — rejeté car incompatible avec anti-marketing.
- **Conséquences** : aucun pouvoir d'exclusion juridique. Tout porteur peut récupérer, modifier, renommer. Risque assumé d'usage abusif du nom (cf. `SAFETY.md` §9 et `PROTOTYPES.md` "En cas d'usage abusif").
- **Critère de retour arrière** : aucun. CC0 est par construction irréversible (les versions publiées restent CC0 même si une fork future change de licence).

---

## ADR-0002 — Anonymat strict du commissariat originel

- **Date** : 2026-04.
- **Statut** : *Accepted, partiellement appliqué.*
- **Contexte** : un édifice anonyme ne peut être attaqué *ad hominem*, ne dépend pas de la légitimité d'une personne, et permet l'auto-effacement (cf. ROADMAP Phase 4).
- **Décision** : aucune signature personnelle dans les fichiers publics du repo, footer = *Anthropie Network*, fichiers de méthodologie privés gitignored.
- **Alternatives rejetées** :
  - *Co-signature 2-3 noms académiques* — aurait facilité l'accueil institutionnel mais lié l'édifice à des biographies, fragilisé l'auto-effacement.
  - *Pseudonyme stable type « Bourbaki »* — moins anonyme qu'un anonymat strict, ouvre la spéculation identitaire.
- **Conséquences** : moins de levier institutionnel à court terme. Plus de robustesse à l'attaque personnelle, à la mode académique, à la chute d'une réputation.
- **Application partielle** : la config Git committe encore en `Robin Fragnière <robin.fragniere@gmail.com>`. À arbitrer (migration vers `Anthropie Network <contact@anthropie.org>` une fois l'alias mail créé). Voir `anthropy_improvements_backlog.md`.
- **Critère de retour arrière** : si un État menace pénalement le commissariat originel pour propos contenus dans l'édifice (extraordinairement improbable mais pas impossible dans certains régimes), une protection juridique nominative pourrait être préférable à l'anonymat. Le débat se poserait alors publiquement.

---

## ADR-0003 — Structure à 12 couches, pas 7 ni 24

- **Date** : 2026-04.
- **Statut** : *Accepted, structurel.*
- **Contexte** : combien de couches pour couvrir 0-∞ sans simplification ni inflation doctrinale ?
- **Décision** : douze couches. Couvrent : MATRICE (0-3), SANCTUAIRE (3-7), ATELIER (5-12), PAROLE (7-15), VILLE (10-18), REGARD (10-18), SEUILS (12-22), MYCOLOGIE (15-25), ARCHIVE VIVANTE (0-∞), CONSEIL DES MORTS (4-∞), PARENTÉ ÉLARGIE (3-25), SEUIL DE LA BRISURE (9-∞).
- **Alternatives rejetées** :
  - *7 couches* (correspondant aux 7 strates de Sanctuaire) — perdait MYCOLOGIE, CONSEIL DES MORTS, PARENTÉ ÉLARGIE, SEUIL DE LA BRISURE. Trop euro-centré, perdait les angles morts critiques.
  - *24 couches* fines — explosion combinatoire, illisible en 10 minutes. La transmissibilité prime.
  - *Structure non-numérotée, par thèmes* — perdait la lisibilité d'âge.
- **Conséquences** : redondances assumées (Couche 5 VILLE et Couche 6 REGARD se chevauchent à 10-18 ; Couche 9 ARCHIVE et Couche 10 CONSEIL DES MORTS se chevauchent sur la mort). Articulation explicite entre couches obligatoire dans chaque fichier.
- **Critère de révision** : si trois prototypes indépendants signalent qu'une couche est en pratique la même qu'une autre dans leur contexte, fusion à étudier.

---

## ADR-0004 — Charpente juridique 31bis-duodecies (extension CRC)

- **Date** : 2026-04.
- **Statut** : *Accepted, à tester.*
- **Contexte** : faut-il une charpente juridique ? Et laquelle ?
- **Décision** : onze articles d'extension (31bis à 31duodecies) du protocole optionnel à la *Convention relative aux droits de l'enfant* (CRC). Cinq États-pilotes identifiés (Norvège, Costa Rica, Nouvelle-Zélande, Bhoutan, Québec).
- **Alternatives rejetées** :
  - *Pas de charpente juridique* (pure pédagogie alternative) — rejeté car la transmissibilité civilisationnelle exige un point d'ancrage juridique.
  - *Déclaration ONU autonome type DUDH* — moins ratifiable, pas d'effet domino auprès d'États CRC.
  - *Convention nouvelle* — délai 50+ ans avant impact, perdait l'urgence (fenêtre 2026-2045).
  - *Lois nationales seules* — pas d'effet civilisationnel, fragmenté.
- **Conséquences** : obligation de qualité juridique des articles (chaque article relu par juriste avant dépôt formel BIE). Stratégie 5 États-pilotes assumée. Capture autoritaire = risque de réfutation §1.
- **Critère de révision** : si après 90 jours de Phase 1 ROADMAP aucun dépôt BIE Genève n'aboutit, repenser le canal (UNICEF Innocenti, Eurochild, Comité ONU CRC en parallèle).

---

## ADR-0005 — Site Astro statique, sobriété radicale, pas de framework JS

- **Date** : 2026-04 (premier déploiement GitHub Pages).
- **Statut** : *Accepted, technique.*
- **Contexte** : choix du stack pour le site `anthropie.org`.
- **Décision** : Astro 6 statique, dépendances minimales (`astro` + `@astrojs/sitemap`), aucun JavaScript runtime, aucune webfont, aucun tracking, hébergement GitHub Pages via Actions.
- **Alternatives rejetées** :
  - *Next.js / Nuxt / Remix* — over-engineered pour un site quasi-statique, signalent une orientation produit, demandent JS runtime.
  - *Hugo / Jekyll* — viables, choix Astro motivé par ergonomie composants + types TS partagés (`site/src/data/couches.ts`).
  - *Webflow / Notion publié* — incompatible avec doctrine "pas de tracking, pas de funnel".
  - *HTML pur sans builder* — perdait la cohérence métadonnées (JSON-LD CreativeWork, sitemap, OG).
- **Conséquences** : performance optimale (~16 KB index HTML), accessibilité native (skip-link, focus-visible, print stylesheet), faible coût cognitif pour repreneur.
- **Critère de révision** : si Astro 7+ change la doctrine (ex. exige JS runtime), évaluer migration vers Hugo. La portabilité Markdown reste la priorité.

---

## ADR-0006 — Garde-fous éthiques explicites (SAFETY.md)

- **Date** : 2026-05 (itération #1 de la session live).
- **Statut** : *Accepted, doctrinal.*
- **Contexte** : un édifice civilisationnel mobilisant mineurs, deuil, brisure, traditions vivantes, IA, doit poser explicitement ses limites avant tout prototype.
- **Décision** : `SAFETY.md` 10 sections non-négociables (protection mineurs, consentement/retrait, non-thérapie, anti-secte, données, deuil/trauma, co-design autochtone, IA non-substitution, signalement, ce que ce document n'est pas).
- **Alternatives rejetées** :
  - *Garde-fous implicites* dispersés dans chaque couche — illisibilité, pas de point unique d'entrée pour porteur prudent.
  - *Code de conduite générique GitHub* — couvre les interactions repo, pas les pratiques terrain.
- **Conséquences** : tout prototype mentionne SAFETY dans sa documentation. Issues template `safety` ajouté pour signalement structuré.
- **Critère de révision** : si un prototype rencontre un cas non couvert par SAFETY, ajouter par PR avec discussion publique.

---

## ADR-0007 — Refus de la résurrection AI (Couche 9 et 10)

- **Date** : 2026-04 (publication initiale).
- **Statut** : *Accepted, civilisationnel.*
- **Contexte** : la technologie AI permet de reconstruire des facsimilés de personnes décédées (voix, visage, écriture). Fait-on quelque chose de cette possibilité ?
- **Décision** : interdiction explicite de toute résurrection AI sans **opt-in vivant explicite, daté, révocable** avant le décès. Inscrit en Couche 9 Strate 7 (Maison d'Atomes) et Couche 10 Strate 7 (Conseil des Morts).
- **Alternatives rejetées** :
  - *Permission par défaut, opt-out tardif* — déséquilibre cognitif évident, le défunt ne peut pas s'opposer.
  - *Permission familiale post-mortem* — appropriation des proches, conflit d'intérêts évident (commercial, deuil pathologique).
  - *Pas de doctrine* — laisser le marché décider, qui est en train de produire des résultats massivement délétères 2024-2025.
- **Conséquences** : article 31novies CRC (Maison d'Atomes Personnelle) inclut explicitement cette protection. SAFETY.md §5 et §8 le martèlent.
- **Critère de retour arrière** : aucun à court terme. Si dans 50 ans un cadre éthique mature émerge avec consentement vivant rigoureux, possibilité d'amender — mais l'opt-in vivant restera nécessaire.

---

## ADR-0008 — Règle de décision multi-référents (gouvernance provisoire)

- **Date** : 2026-05.
- **Statut** : *Accepted, gouvernance.*
- **Contexte** : tant qu'aucune fédération formelle n'est constituée (cf. ROADMAP Phase 4), les décisions sur le repo (PR mergées, suspension d'une couche, modification de SAFETY ou REFUTATION) doivent éviter la recentralisation implicite sur un seul mainteneur.
- **Décision** : aucune décision dite *structurante* ne peut être mergée sans **convergence minimale de deux référents distincts** (mainteneurs ou contributeurs établis du repo) **et** une fenêtre de contestation publique d'au moins **7 jours** dans Issues ou Discussions GitHub. Les corrections triviales (typo, lien cassé) restent mono-mainteneur.
- **Décisions structurantes** (liste non-exhaustive) : modification de SAFETY.md, REFUTATION.md, FORKING.md, ADR existante ; suspension d'une couche ; fusion de couches ; changement de licence ; changement de domaine `anthropie.org` ; modification du tableau 12 couches ; ajout/retrait d'un article 31bis-duodecies.
- **Alternatives rejetées** :
  - *Mono-mainteneur libre* — risque de recentralisation, viole l'auto-effacement progressif.
  - *Vote majoritaire ouvert* — fragile aux brigading et au sock-puppeting tant que la communauté est petite.
  - *Comité de gouvernance signé* — recréerait une autorité personnelle, viole l'anonymat doctrinal.
- **Conséquences** : ralentissement de 7 jours minimum sur tout changement structurant. Visibilité publique de la délibération. Trace dans Issues. Dans une communauté petite (< 5 référents), risque que deux référents ne soient pas atteignables — alors la décision attend.
- **Critère de retour arrière** : si un cas d'urgence éthique (ex. Issue safety §1 SAFETY.md révèle violation grave) exige action en moins de 7 jours, mainteneur peut agir en urgence en signalant publiquement la dérogation et en justifiant *post hoc* dans une Issue dédiée. Déclenche automatiquement une revue par l'autre référent dans les 72h.

---

## ADR-0009 — Sas anti-contamination synthétique (provenance des contenus)

- **Date** : 2026-05.
- **Statut** : *Accepted, doctrinal.*
- **Contexte** : l'édifice est produit AI-assisté et publié à l'ère des LLM mainstream. Sans règle, un contenu produit dans une couche haute (ex. un audit IA d'une couche 8) ou directement par un modèle de langue peut redescendre comme « base » empirique d'une couche basse, créant une auto-référence circulaire qui prétend valeur sans en avoir.
- **Décision** : tout contenu **produit AI** ou **dérivé d'une couche haute non-validée empiriquement** ne peut pas être incorporé comme fondement d'une couche basse sans (a) **marque de provenance** explicite (ex. note *« hypothèse AI-générée non validée empiriquement »*), (b) **revue humaine** d'au moins un référent qualifié dans le domaine, et (c) **lien source explicite** quand la provenance est un autre fichier de l'édifice.
- **Cas type interdits** :
  - Insérer une « méta-analyse » générée par LLM dans la section *Fondement scientifique* d'une couche sans la marquer comme telle ni la valider contre les sources primaires citées.
  - Utiliser un audit matriciel produit par un modèle pour la Couche N comme référence dans la Couche N+1 sans relecture humaine.
  - Importer un développement de scénario fictionnel comme « précédent juridique » dans un article 31bis-duodecies.
- **Alternatives rejetées** :
  - *Aucune règle (laisser-faire)* — risque de contamination par retrait progressif de la rigueur empirique.
  - *Interdiction totale d'AI* — irréaliste et peu honnête, l'édifice originel est AI-assisté (cf. ADR-0006 §IA).
  - *Étiquetage seulement* — insuffisant : sans revue humaine, l'étiquette ne protège pas de l'amalgame.
- **Conséquences** : tout fichier modifié devra distinguer visiblement *fait sourcé* / *inférence* / *hypothèse* / *proposition normative* (cf. backlog : balisage statut épistémique). Travail d'audit rétroactif sur les 12 couches existantes à planifier pour repérer les contaminations potentielles passées.
- **Critère de retour arrière** : si un protocole d'AI-revue par modèles spécialisés (ex. audit cross-LLM avec consensus humain) émerge avec garanties méthodologiques équivalentes à la revue humaine, possibilité d'amender — mais le marquage de provenance reste obligatoire.

---

## ADR-0010 — Protocole de modification à contre-voix

- **Date** : 2026-05.
- **Statut** : *Accepted, gouvernance.*
- **Contexte** : un édifice civilisationnel CC0 anonyme est exposé au risque qu'un courant unique (idéologique, juridique, religieux, philanthropique, commercial) reprenne progressivement la doctrine en redéfinissant silencieusement le sens des termes, l'ordre de lecture, les priorités. Un linter de capture lexicale (cf. backlog codex iter#7 #1) seul ne suffit pas — il faut une discipline éditoriale.
- **Décision** : toute Pull Request modifiant le **noyau doctrinal** doit embarquer un bloc obligatoire en fin de description avec trois entrées :
  - **Risque de capture** : quel courant pourrait s'emparer de cette modification pour la détourner ? (Réponse possible : "aucun visible.")
  - **Lecture adverse** : quelle interprétation hostile ou opposée à l'esprit de l'édifice cette modification ouvre-t-elle ?
  - **Condition de refus** : quel critère, indicateur ou cas concret obligerait à retirer cette modification ?
- **Noyau doctrinal** (liste non-exhaustive, en synergie avec ADR-0008) : `README.md`, `ANTHROPIE_KERNEL.md`, `SAFETY.md`, `REFUTATION.md`, `FORKING.md`, `DECISIONS.md`, `WELCOME.md`, `LEGAL_BOUNDARIES.md`, le tableau 12 couches, la liste 11 articles 31bis-duodecies, la charte anti-appropriation Couche 7 Strate 5.
- **Alternatives rejetées** :
  - *Aucun protocole* — exposition silencieuse au glissement doctrinal.
  - *Comité éditorial signé* — viole l'anonymat et recrée une autorité personnelle.
  - *Vote majoritaire ouvert* — fragile aux brigading et insuffisant pour repérer la capture subtile (qui passe la majorité sans alerter).
- **Conséquences** : mainteneurs apprennent à pratiquer la *prédiction-avant-vocal* (Couche 4 Strate 5) sur leurs propres PR — quelle est la lecture la plus hostile possible ? Trace publique dans la PR. Coût : 5-15 minutes supplémentaires par PR doctrinale.
- **Critère de retour arrière** : si après 12 mois ce protocole n'a jamais signalé de risque réel et alourdit chaque PR sans valeur ajoutée, possibilité d'amender — par exemple en le restreignant aux modifications majeures uniquement.

---

## ADR-0011 — Pacte d'effacement progressif du commissariat originel

- **Date** : 2026-05.
- **Statut** : *Accepted, gouvernance long-terme.*
- **Contexte** : tant que le commissariat originel (mainteneur unique pour l'instant) tient les rôles `gardien doctrine`, `mainteneur dépôt`, `arbitre sécurité`, `archiviste`, etc., un *culte d'origine* peut s'installer même sans intention. Une disparition contrainte (santé, démission, hostilité externe) interromprait alors le portage. Cf. [`MANDATES.md`](https://github.com/SanTiepi/anthropie-edifice/blob/master/MANDATES.md), [`CHOKE_POINTS.md`](https://github.com/SanTiepi/anthropie-edifice/blob/master/CHOKE_POINTS.md), [`ROADMAP.md`](https://github.com/SanTiepi/anthropie-edifice/blob/master/ROADMAP.md) Phase 4 auto-effacement.
- **Décision** : pacte explicite du commissariat originel à céder progressivement, **avant** disparition contrainte, ses accès et arbitrages. Calendrier indicatif :
  - **0-12 mois** (phase Transmission embryonnaire) : commissariat originel mainteneur unique de fait, mais documente publiquement chaque arbitrage doctrinal.
  - **12-36 mois** : recruter ≥ 1 second mainteneur GitHub avec admin rights ; ≥ 2 contributeurs établis (pour ADR-0008 multi-référents). Le commissariat reste actif mais n'est plus seul.
  - **36-60 mois** : céder le rôle `gardien doctrine` à un·e successeur·euse passé·e par l'épreuve (cf. codex iter#10 #5 *Passation par Épreuve*). Le commissariat reste contributeur, plus mainteneur principal.
  - **60-120 mois** : céder progressivement les rôles techniques (mainteneur dépôt, archiviste). Reste possible : présence ponctuelle en tant que contributeur historique anonyme.
  - **120 mois et au-delà** : effacement complet du commissariat originel. Le repo continue, ou s'arrête avec annonce publique honnête (cf. [`REFUTATION.md` §1 et §6](refutation/)).
- **Alternatives rejetées** :
  - *Aucun calendrier* — l'effacement reste vœu pieux, pas planifié, ne survient pas.
  - *Calendrier rigide à dates fixes* — irréaliste face aux contingences (santé, vie familiale, opportunités).
  - *Disparition immédiate sans transition* — irresponsable, casse la transmission au moment où elle est la plus fragile.
- **Conséquences** : le commissariat originel s'engage publiquement à céder, ne pas s'accrocher, ne pas créer de dépendance affective ou logistique. Les successeurs s'engagent à ne pas créer de figure mythique du commissariat originel après son effacement.
- **Critère de retour arrière** : si à 36 mois aucun successeur n'a émergé malgré recrutement actif, possibilité de prolonger le calendrier de 24 mois supplémentaires en annonçant publiquement le retard et la raison (cf. ROADMAP "échec acceptable"). Au-delà, déclencher l'arrêt du portage actif (cf. REFUTATION §1).

---

## ADR-0012 — Tension CC0 / souveraineté autochtone : licence reste CC0 + complément doctrinal

- **Date** : 2026-05.
- **Statut** : *Accepted, doctrinal, fragile.*
- **Contexte** : un audit externe (deep research ChatGPT, mai 2026) a relevé une *« discordance potentielle entre éthique déclarée et force exécutoire de la licence »* : les Couches 7, 10, 11 mobilisent des références à des traditions vivantes autochtones, et la charte anti-appropriation (Couche 7 Strate 5) promet aux communautés concernées une *souveraineté avec retrait possible sous 90 jours*. Or **CC0 1.0 Universal** rend cette promesse difficilement opposable juridiquement : un repreneur de bonne foi peut continuer à publier la version pré-retrait sous CC0 sans violer aucune clause juridique. La doctrine éthique est donc plus forte que le droit positif applicable.
- **Décision** : **garder CC0 1.0 Universal sur l'intégralité de l'édifice** (pas de licence hybride CC-BY-SA pour les couches autochtones), **et** documenter explicitement cette tension dans [`SAFETY.md` §7](https://github.com/SanTiepi/anthropie-edifice/blob/master/SAFETY.md), [`FORKING.md` §3-5](https://github.com/SanTiepi/anthropie-edifice/blob/master/FORKING.md), et [`OPEN_GRIEVANCES.md` G-001](https://github.com/SanTiepi/anthropie-edifice/blob/master/OPEN_GRIEVANCES.md). La force opposable repose sur la **désolidarisation publique** + signalement aux autorités civiles compétentes (Miviludes, CIC, équivalents) en cas d'usage extractiviste — pas sur la licence.
- **Alternatives rejetées** :
  - *Dual-license CC0 (édifice général) + CC-BY-SA-NC (Couches 7, 10, 11)* — fragmenterait le corpus, créerait des conflits de réutilisation par les forks bien-intentionnés. Casserait la doctrine "personne ne le possède" sur 3 couches.
  - *CC-BY-SA-NC sur tout l'édifice* — rendrait l'édifice non-diffusible dans les contextes où la souveraineté communautaire **n'est pas en jeu** (90 % des couches), au prix d'une protection partielle (pas absolue) sur les 10 % concernés.
  - *Licence custom inspirée de la déclaration UNDRIP 2007* — non-reconnue juridiquement, fragile en pratique, et créerait une dépendance à un texte ONU non-justiciable.
  - *Ne rien dire* — laisserait l'audit deep-research ouvert sans réponse doctrinale, fragiliserait la crédibilité.
- **Conséquences** :
  1. La promesse de retrait 90 jours **dépend du portage actif de la communauté de porteurs**, pas du droit. Un fork publié en 2030 par un acteur extractiviste sera en règle juridiquement, **mais** la communauté de porteurs initiaux peut s'en désolidariser publiquement et appeler les communautés autochtones à s'appuyer sur leurs propres mécanismes juridiques nationaux (UNDRIP, lois locales sur les données ethnographiques, etc.) pour s'opposer.
  2. Toute couche co-designée avec une communauté autochtone (à venir, Phase 1 ROADMAP) **devra** explicitement documenter le ratio de protection effective offert (pas absolu) avant signature du co-design.
  3. Cette ADR formalise une **honnêteté doctrinale** : l'édifice ne peut pas promettre ce qu'il ne peut pas tenir juridiquement.
- **Critère de retour arrière** :
  1. Si dans les 24 mois suivant un co-design réel, une communauté autochtone signataire demande explicitement une migration vers CC-BY-SA-NC pour ses couches, possibilité d'examiner le compromis.
  2. Si une jurisprudence autochtone émerge (en Bolivie, Équateur, Nouvelle-Zélande, ou Canada-Québec) qui rend opposable la souveraineté communautaire face à CC0, possibilité de basculer.
  3. Sinon, la doctrine reste : **CC0 + désolidarisation publique** comme défense conjointe.

---

## ADR-0013 — Distinction Anthropie / Anthropic + clarification "pas un labo IA"

- **Date** : 2026-05.
- **Statut** : *Accepted, défensif.*
- **Contexte** : un audit externe (deep research ChatGPT, mai 2026) souligne le risque de confusion entre **Anthropie** (l'édifice civilisationnel CC0) et **Anthropic** (entreprise d'IA propriétaire). De plus, la mention de l'IA dans plusieurs couches (Couche 4 *Discipline de Prédiction-Avant-Vocal*, Couche 9 *Anti-Résurrection AI*) peut faire croire à un projet d'AI alignment technique. Sans clarification explicite, journalistes, institutions, et lecteurs grand public peuvent mal classer le projet.
- **Décision** : créer un fichier dédié [`NOT_AN_AI_LAB.md`](https://github.com/SanTiepi/anthropie-edifice/blob/master/NOT_AN_AI_LAB.md) qui clarifie en 7 sections ce que l'édifice **n'est pas** : (1) pas Anthropic, (2) pas un labo IA, (3) pas un produit, (4) pas une religion ni école nominée, (5) pas un mouvement politique, (6) pas une autorité, (7) pourquoi la précision est nécessaire (4 confusions prévisibles). Plus tableau "si vous étiez venu chercher autre chose" redirigeant vers les vrais labos IA, écoles alternatives, projets *rights of nature*, etc. Ce fichier est exposé sur le site sous `/lire/pas-un-labo-ia/`.
- **Alternatives rejetées** :
  - *Renommer Anthropie* — coût de migration énorme (domaine, documentation, citations académiques futures), perte de l'étymologie (anthropos + énergie/pratique).
  - *Sous-titre permanent "édifice civilisationnel CC0, pas un labo IA"* — devient verbeux, dilue l'identité.
  - *Ne rien clarifier* — laisse la confusion structurelle.
- **Conséquences** : Un seul fichier citable directement face à la confusion. Lien permanent depuis le pacte d'accueil et le brief. Force documentaire pour tout porteur ou journaliste qui doit poser la distinction.
- **Critère de retour arrière** : si à 24 mois aucun cas de confusion documenté n'a émergé (Issues GitHub, articles de presse, courriels au commissariat originel), possibilité de fusionner ce fichier dans WELCOME.md ou LEGAL_BOUNDARIES.md.

---

## ADR-0014 — Moratoire 90 jours sur tout nouveau dispositif

- **Date** : 2026-05-04 (itération #34 de la session live).
- **Statut** : *Accepted, doctrinal court terme.*
- **Contexte** : après 33 itérations de production continue, l'édifice atteint **70+ pages, 29 dispositifs, 13 ADR, 23 fichiers structurels**. Trois signaux doctrinaux se sont accumulés : codex iter#15 (*« consolidation > nouveau fond »*), codex iter#30 (*« maintenance > extension »*), codex iter#33 (*« moratoire 90 jours »*). En parallèle, [`AUTO_CRITIQUE.md`](https://github.com/SanTiepi/anthropie-edifice/blob/master/AUTO_CRITIQUE.md) a été créé à l'itération #32 et liste *« inflation doctrinale »* comme **erreur prévisible n°4**. Continuer à produire sans appliquer cette auto-critique serait incohérent.
- **Décision** : **moratoire de 90 jours** (à compter du 2026-05-04, donc jusqu'au 2026-08-02) sur la création de tout nouveau fichier `.md` qui constituerait un nouveau dispositif, toolkit ou couche doctrinale. Sont **autorisés** : modifications de fichiers existants, fusion de deux dispositifs, archivage selon [`MAINTENANCE.md` §3](https://github.com/SanTiepi/anthropie-edifice/blob/master/MAINTENANCE.md), corrections d'erreurs factuelles, ADR documentant des décisions à prendre, modifications de `REGISTRY.md` (pré-cycle d'élagage à blanc), modifications du site Astro pour amélioration de navigation. **Pas autorisés** : nouveau toolkit pour un contexte non-encore-couvert, nouveau dispositif de groupe, nouveau dispositif solo, nouveau format ou rituel.
- **Levée du moratoire** : la levée nécessite la satisfaction d'**au moins une** des conditions suivantes, **vérifiée publiquement** :
  1. **Un prototype documenté** d'au moins un dispositif existant a été engagé en pratique (Issue GitHub avec tag `prototype`, format minimal `PROTOTYPES.md`).
  2. **Une critique externe sérieuse** a été reçue (Issue GitHub avec tag `lecture-critique`, ou article académique/journalistique référençant l'édifice).
  3. **Une décision d'archivage ou de fusion** a été publiée pour au moins 1 dispositif existant (cf. `MAINTENANCE.md` §3 + `REGISTRY.md` mis à jour avec statut *archivé*).
- **Alternatives rejetées** :
  - *Pas de moratoire* — laisserait s'installer durablement la dynamique d'inflation, en contradiction avec AUTO_CRITIQUE et trois signaux codex.
  - *Moratoire permanent (sans condition de levée)* — figerait l'édifice et empêcherait toute évolution réelle ultérieure.
  - *Moratoire de 30 jours* — trop court pour qu'un prototype tienne ou qu'une critique externe arrive.
  - *Moratoire de 6 mois* — risque de paralyser l'édifice si une vraie urgence émerge.
- **Conséquences** :
  1. Pendant 90 jours, l'effort de la session live (et de tout porteur) se concentre sur **maintenance + élagage + dialogue avec porteurs réels** plutôt que sur extension.
  2. Le pré-cycle d'élagage à blanc inscrit dans `REGISTRY.md` à l'itération #34 sert de **première application concrète** du protocole `MAINTENANCE.md`.
  3. Toute Pull Request créant un nouveau dispositif est refusée (avec mention de cette ADR) jusqu'à levée du moratoire.
  4. Si **aucune** des trois conditions de levée n'est remplie au 2026-08-02, l'absence de levée **est** une donnée doctrinale — l'édifice n'a peut-être pas atteint son public, ou n'a pas su provoquer l'usage. Voir alors `REFUTATION.md` §1 et §6.
- **Critère de retour arrière** :
  1. Si une **urgence éthique grave** survient (ex. usage abusif documenté nécessitant une réponse doctrinale formalisée — cf. SAFETY §9), un nouveau dispositif peut être créé en urgence avec mention explicite de la dérogation et justification *post hoc* sous 72h.
  2. Sinon, le moratoire tient strictement.

---

## Modèle pour ajouter une nouvelle ADR

```markdown
## ADR-XXXX — Titre court de la décision

- **Date** : YYYY-MM.
- **Statut** : *Proposed | Accepted | Superseded by ADR-YYYY | Deprecated.*
- **Contexte** : pourquoi cette décision se pose, en 1-3 lignes.
- **Décision** : ce qui est décidé, en 1-3 lignes.
- **Alternatives rejetées** :
  - *Alternative A* — pourquoi rejetée.
  - *Alternative B* — pourquoi rejetée.
- **Conséquences** : ce que cette décision rend impossible, oblige, simplifie.
- **Critère de retour arrière** : sous quelles conditions cette décision serait révisée.
```

Pour ajouter une ADR : Pull Request avec tag `decision`, discussion publique 7 jours, merge.
