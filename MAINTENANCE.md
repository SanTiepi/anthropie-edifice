# L'Anthropie — Maintenance de l'édifice (registre des claims, élagage, archive)

> *Trois mécanismes pour qu'un édifice CC0 anonyme puisse rester lisible, révisable et anti-bullshit dans le temps long. Sans maintenance explicite, un corpus de 68 pages et 25 dispositifs s'effondrera sous son propre poids.*

CC0 1.0 Universal. Cf. codex iter#30 #3+#4+#5 fusionnés. Cette page a été créée à l'**itération #31** de la session live, après que codex a doctrinalement pivoté de l'extension vers la maintenance. Cf. aussi [`REFUTATION.md`](refutation/), [`OPEN_GRIEVANCES.md`](griefs/), [`EVIDENCE_MAP.md`](preuves/) (sa logique des niveaux A/B/C/D s'applique aussi aux dispositifs).

**Pourquoi ce fichier existe** : à 68 pages et 25 dispositifs, l'édifice atteint le seuil où l'**accumulation** devient un risque doctrinal — un porteur potentiel ne sait plus par où entrer, un mainteneur perd le sens du tout, et la doctrine *« anti-marketing »* est compromise par la masse même du contenu. Maintenir explicitement ce qui existe est désormais plus important que créer du nouveau.

---

## Outil 1 — Registre des Claims (page par dispositif)

### Principe

Chaque dispositif (toolkit, ADR, document doctrinal, schéma) **doit** avoir une fiche de registre minimale et publiquement consultable. Sans cette fiche, le dispositif n'est pas considéré comme officiellement intégré à l'édifice.

### Format de la fiche

```markdown
## [NOM DU DISPOSITIF]

**Slug** : `xxxx-xxxx`
**Fichier source** : `XXXX.md`
**Date de création** : YYYY-MM-DD (itération #N)
**Auteur** : Anthropie Network (anonymisé)
**Date de dernière revue** : YYYY-MM-DD

### Promesse
1-3 phrases sur ce que ce dispositif **prétend** faire pour l'utilisateur.

### Contre-indications
1-5 lignes sur les contextes où ce dispositif est **inadapté ou
contre-productif**. Plus c'est précis, mieux c'est.

### Niveau de preuve
- 🟢 A : convergence empirique forte ou précédent juridique
- 🟡 B : framework éprouvé ailleurs, extrapolation à valider
- 🟠 C : hypothèse inférentielle, jamais testée à scale
- 🔴 D : invention propre Anthropie, jamais validée
  (la majorité des dispositifs)

### Conditions minimales
1-5 lignes sur ce qui est **requis** pour utiliser le dispositif :
formation, matériel, durée, accord institutionnel.

### Garde-fous obligatoires
Référence aux sections de SAFETY.md applicables :
- §1 (mineurs) si applicable
- §3 (non-thérapie) si applicable
- §4 (anti-secte) si applicable
- §7 (autochtone) si applicable

### Trajectoire dans le temps
- Date d'introduction : YYYY-MM-DD
- Statut courant : actif / en revue / rétrogradé / archivé
- Date prévue de prochaine revue : YYYY-MM-DD (max 12 mois)
```

### Procédure d'introduction d'une fiche

1. À la création d'un nouveau dispositif, **rédiger sa fiche en parallèle**.
2. Pendant la première année, marquer comme **expérimental** dans le statut.
3. À la première revue annuelle, basculer en **actif** ou **rétrograder**.

### Pourquoi ce format strict

- **Promesse explicite** = pas de fonction implicite ou rampante.
- **Contre-indications publiques** = anti-bullshit. Un porteur sait quand ne pas utiliser.
- **Niveau de preuve** = honnêteté épistémique (cf. EVIDENCE_MAP A/B/C/D).
- **Date de dernière revue** = on ne peut pas laisser un dispositif vieillir indéfiniment.
- **Garde-fous obligatoires** = articulation systématique avec SAFETY.md.

### Où héberger les fiches

Option A : un fichier unique `REGISTRY.md` à la racine, avec toutes les fiches concaténées.
Option B : un dossier `registry/` avec un fichier par dispositif.
Option C : intégrer chaque fiche **en tête** du fichier du dispositif lui-même (frontmatter étendu).

L'option C est la plus compatible avec le `prepare-content.mjs` actuel — c'est probablement ce qui sera implémenté dans une itération ultérieure.

---

## Outil 2 — Cycle Annuel d'Élagage

### Principe

Une fois par an, à date fixe (proposée : **anniversaire du commit initial du repo**, soit fin avril), un cycle de revue passe en revue **tous** les dispositifs et applique l'une des **4 décisions** :

1. **Garder** (statut *actif*) — le dispositif tient, sa fiche est mise à jour.
2. **Fusionner** — le dispositif est intégré dans un autre plus large ; la fiche est migrée.
3. **Rétrograder** — le dispositif passe en *expérimental* ou *en revue*, signalé comme tel sur le site.
4. **Archiver** — le dispositif sort de l'usage courant, va dans l'**Archive des Obsolètes** (Outil 3).

### Procédure du cycle annuel

```
SEMAINE -2 (préparation)
   - Le·a Gardien·ne de Doctrine (cf. MANDATES.md)
     prépare la liste de tous les dispositifs avec
     leur date de dernière revue.
   - Identifier les dispositifs qui n'ont pas été
     revus depuis 12+ mois — priorité à ceux-là.

SEMAINE 0 (revue collective)
   Une session publique (Issue GitHub épinglée + appel
   à contribution 14 jours) où chacun peut :
     - Signaler un dispositif obsolète.
     - Signaler un dispositif qu'il/elle veut conserver.
     - Proposer une fusion.
   
   Pas de vote majoritaire. Convergence multi-référents
   selon DECISIONS.md ADR-0008.

SEMAINE 4 (décisions)
   Chaque dispositif est documenté avec sa décision
   finale dans :
     - Sa fiche de registre (statut mis à jour).
     - Une Issue de cycle annuel récapitulative.
     - Si archivage : entrée dans l'Archive des Obsolètes.
```

### Critères d'archivage

Un dispositif est candidat à l'archivage si **au moins 2 de ces critères** sont remplis :

- Aucun usage documenté en 24 mois (aucun prototype rapporté, aucune mention en Issue, aucun retour).
- Remplacé par un dispositif plus récent et plus complet (fusion).
- Un défaut éthique ou doctrinal grave a été identifié et n'est pas corrigeable par amendement.
- Le contexte cible a disparu ou n'est plus pertinent (ex. dispositif spécifique COVID).
- Le·a Gardien·ne de Doctrine et au moins 1 autre référent·e jugent qu'il alourdit l'édifice sans valeur ajoutée.

### Pourquoi un cycle annuel et pas continu

- **Continu** = épuisant pour les mainteneurs, créerait une pression permanente.
- **Annuel** = rythme tenable, prévisible, conforme à la doctrine du temps long.
- **Avant 12 mois** = pas assez de recul pour juger.
- **Plus de 24 mois sans revue** = un dispositif peut survivre à sa pertinence.

---

## Outil 3 — Archive des Obsolètes

### Principe

Quand un dispositif est archivé, il **n'est pas supprimé** du repository. Il est **déplacé** dans une zone explicite *« obsolète »* avec un fichier `OBSOLETE_NOTES.md` qui documente :

- **Pourquoi** il a été archivé (motif).
- **Date** de l'archivage.
- **Limites constatées** dans son usage réel.
- **Successeur éventuel** (si remplacé par un autre dispositif).
- **Cas d'usage résiduels** : situations où le dispositif archivé peut encore servir, malgré son retrait du courant.

### Format de l'Archive (proposition)

Sous-dossier `obsolete/` à la racine du repo (gitignored du site mais commit dans le repo) :

```
obsolete/
├── OBSOLETE_INDEX.md       (liste avec dates et motifs)
├── 2027-04-15-DISPOSITIF-X.md
├── 2027-04-15-DISPOSITIF-Y.md
├── 2028-04-12-DISPOSITIF-Z.md
└── ...
```

Format de chaque fichier `YYYY-MM-DD-NOM.md` :

```markdown
# DISPOSITIF [Nom] — Archivé le YYYY-MM-DD

## Motif principal de l'archivage
[1 paragraphe]

## Limites constatées
- [bullet]
- [bullet]
- [bullet]

## Successeur éventuel
- [Nom du dispositif] (si applicable)
- ou : aucun successeur direct

## Cas d'usage résiduels
[Si oui : situations où ce dispositif peut encore servir,
 malgré son archivage. Si non : "aucun cas d'usage résiduel
 identifié."]

## Trace d'origine
- Créé : YYYY-MM-DD (itération #N)
- Dernière revue avant archivage : YYYY-MM-DD
- Décideur·euse·s archivage : [pseudonymes des référent·e·s]

---

[Le contenu complet du dispositif tel qu'il était au moment
 de l'archivage est conservé ci-dessous, en lecture seule.]

[... contenu du fichier original ...]
```

### Pourquoi un cimetière explicite plutôt qu'une suppression

- **Histoire préservée** : un porteur futur peut comprendre pourquoi un dispositif n'existe plus.
- **Apprentissage par les morts** : les dispositifs archivés enseignent ce qui ne marche pas.
- **Anti-révision idéologique** : on ne peut pas effacer rétroactivement ce que l'édifice a proposé. La trace est doctrinalement protégée.
- **Possibilité de réintégration** : si le contexte change, un dispositif archivé peut être ressuscité (avec notation explicite de ce parcours).

### Cas particuliers

- **Dispositif archivé pour défaut éthique grave** (rare) : conserver dans l'archive mais avec **avertissement** explicite en tête. Pas de réutilisation possible sans amendement structurel.
- **Dispositif fusionné** : archive courte qui pointe vers le dispositif fusionnant.
- **Dispositif jamais utilisé** mais retiré pour alléger l'édifice : note simple *« retiré pour cohérence du corpus »* sans jugement de valeur.

---

## Articulation entre les 3 outils

```
[Création d'un dispositif]
          ↓
[Fiche du Registre des Claims rédigée] (Outil 1)
          ↓
[Statut "expérimental" pendant 12 mois]
          ↓
[Cycle Annuel d'Élagage] (Outil 2)
          ↓
   [Décision parmi 4]
   ↓        ↓        ↓        ↓
Garder  Fusionner Rétrograder Archiver
   ↓        ↓        ↓        ↓
Statut    Migration  Statut   [Archive
"actif"   vers       "en      des
          fusion     revue"   Obsolètes] (Outil 3)
                              ↓
                     [Conservation explicite
                      avec motif et trace]
```

### Calendrier indicatif

- **Mai 2026 (itération #31, ce fichier)** : description du protocole.
- **Mai 2027** : premier cycle annuel d'élagage. Création des fiches de registre rétroactives pour les 25 dispositifs existants. Archive des Obsolètes initialisée si applicable.
- **Mai 2028, 2029, etc.** : cycles annuels successifs.

### Si le commissariat originel s'efface (cf. ADR-0011)

Le cycle annuel survit à l'effacement progressif du commissariat originel. C'est même son utilité : un porteur futur, isolé temporellement, sait **comment** maintenir l'édifice sans avoir à tout réinventer. Le protocole est **l'héritage opératoire** du commissariat, pas l'édifice lui-même.

---

## Limites de la maintenance

- **Pas une garantie d'éternité** : un édifice CC0 anonyme peut disparaître si tous les porteurs l'abandonnent. La maintenance ralentit l'effondrement, ne l'empêche pas.
- **Pas un substitut au jugement** : les décisions d'élagage restent humaines, pas algorithmiques.
- **Pas un dispositif d'auto-purification doctrinale** : si une critique externe sérieuse révèle un problème structurel (cf. OPEN_GRIEVANCES, REFUTATION), c'est cette critique qui prime, pas le cycle annuel.
- **Pas pour les forks** : chaque fork peut adopter ce protocole ou en proposer un autre. Cf. FORKING.md §3 (relicensiement compatible).

---

## Articulation avec l'édifice

- **Couche 9 (L'ARCHIVE VIVANTE)** : la Maintenance est l'expression méta de la Couche 9 — l'édifice lui-même fait sa propre Maison d'Atomes Personnelle et son propre Anti-Résurrection.
- **`DECISIONS.md` ADR-0008 multi-référents** : les décisions d'élagage suivent ce protocole.
- **`DECISIONS.md` ADR-0011 effacement progressif** : la maintenance opère **avec ou sans** le commissariat originel.
- **`OPEN_GRIEVANCES.md`** : un grief sérieux non clôturé peut déclencher un élagage anticipé hors cycle annuel.
- **`HOSTILE_DRILL.md`** : l'audit adverse gelé annuel peut **précéder** le cycle d'élagage — une critique externe sérieuse signale ce qu'il faut élaguer en priorité.

---

*« Un édifice qui s'étend sans s'élaguer s'effondre sous son poids. Maintenir, c'est aussi savoir mettre en terre. »*
