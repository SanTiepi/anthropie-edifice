# L'Anthropie — Bibliographie négative

> *Les sources que l'édifice **refuse explicitement** de citer comme fondement, même quand elles sont disponibles, populaires ou citées par d'autres frameworks similaires. Pour rendre la doctrine visible par ce qu'elle exclut, pas seulement par ce qu'elle invoque.*

CC0 1.0 Universal. Document évolutif — tout ajout argumenté via Pull Request avec discussion publique de 7 jours.

**Pourquoi ce document ?** Une bibliographie positive (cf. fichiers de couche, [`EVIDENCE_MAP.md`](preuves/)) montre **sur quoi** l'édifice s'appuie. Mais elle ne dit pas **ce qu'il a refusé** de mobiliser. Or l'absence d'une source attendue (par un lecteur académique d'un certain courant) est souvent plus signifiante que la présence d'une autre. Documenter explicitement les exclusions évite : (a) le soupçon d'oubli ; (b) la suspicion de capture par un courant ; (c) le glissement progressif vers ces sources lors de PR ultérieures.

Cette bibliographie négative complète l'[ADR-0009 Sas anti-contamination synthétique](decisions/) et l'[ADR-0010 Protocole de modification à contre-voix](decisions/).

---

## Quatre catégories d'exclusion

🚫 **Sources synthétiques** — produits par modèles de langue sans validation par source primaire humaine. Rejetées par ADR-0009.

⛔ **Sources propriétaires non-vérifiables** — tests psychométriques fermés, datasets sous licence restrictive, études internes d'entreprises éducatives sans publication peer-reviewed.

🔒 **Sources invérifiables** — anecdotes auto-rapportées sans triangulation, témoignages mobilisés sans contexte ni consentement explicite, "données" rapportées sans méthodologie publique.

🚧 **Sources hors-contexte** — sources qui existent mais dont la transposition à l'arc 0-∞ d'apprentissage humain serait abusive (sciences animales appliquées sans précautions cross-species, neuroimagerie de cas pathologique pris pour norme, etc.).

---

## Sources explicitement refusées

### Type 🚫 — Synthétiques

- **Toute "méta-analyse" générée par un LLM** sans validation contre les études primaires citées.
- **Tout "résumé" d'un courant pédagogique** produit par un LLM sans être confronté à au moins un texte primaire de ce courant.
- **Toute "citation"** dont la source primaire ne peut être ouverte et lue (lien mort, paywall sans abstract méthodologique, "private communication" non datée).

### Type ⛔ — Propriétaires non-vérifiables

- **Tests psychométriques propriétaires fermés** : QI WISC/WPPSI utilisés comme indicateurs de réussite éducative (anti-doctrine WEIRD). Cf. [`anthropie_couche_04_parole.md`](couche-04-parole/) section indicateurs ANTI-WEIRD.
- **Données internes Big Tech sur impact des écrans / réseaux sociaux** sur les jeunes : sans audit indépendant, ces données sont juge-et-partie. Préférer JAMA Pediatrics, *Lancet Planet Health*, *Frontiers Psychiatry* peer-reviewed.
- **"White papers" de fondations privées éducatives** sans publication peer-reviewed : utilisables comme indicateurs de pratique, pas comme preuve.
- **Études commanditées par éditeurs scolaires** sur leurs propres méthodes (ex. études Singapour Math financées par leur diffuseur).

### Type 🔒 — Invérifiables

- **Témoignages d'enfants mobilisés par des adultes** sans consentement parental explicite et sans relecture par l'enfant à âge ultérieur. Anti-doctrine [`SAFETY.md` §1](garde-fous/) (protection mineurs).
- **Récits "miraculeux"** d'éducation alternative sans données démographiques, sans cohorte témoin, sans suivi longitudinal.
- **Anecdotes Reggio / Sudbury / Big Picture** isolées rapportées sans contexte structurel ni statistique.
- **"Études de cas" d'AI-assistance pédagogique** sans documentation des prompts, des modèles utilisés, et des limites de l'expérience.

### Type 🚧 — Hors-contexte

- **Recherche éthologique animale** transposée hors précautions cross-species. Exemple : *« les éléphants enterrent leurs morts, donc les enfants doivent... »* est un saut catégoriel non rigoureux.
- **Neuroimagerie fonctionnelle (IRMf) sur cas pathologiques** (autisme, dépression majeure, addiction) prise pour norme du développement enfantin.
- **Travaux de psychologie évolutionniste pop** (cf. *Evolutionary Psychology* version Buss simplifiée) appliqués comme normes éducatives.
- **Recherches WEIRD universalisées** sans signalement de leur origine culturelle. Cf. Heidi Keller *The Myth of Universal Sensitive Responsiveness* (2018) — Keller est citée précisément **parce qu'elle critique** cette universalisation.

---

## Cas frontière (à arbitrer publiquement par PR si invoqués)

Certaines sources sont **utilisables sous conditions** mais souvent abusivement mobilisées :

- **Travaux de Daniel Goleman sur l'intelligence émotionnelle** : pop-psychology synthétisant des courants académiques. Citer le travail de John Mayer / Peter Salovey en source primaire, pas Goleman comme tel.
- **Maria Montessori (corpus historique)** : doctrine d'origine 1907-1952 ; ce qui est mobilisable est l'observation directe et certains principes pédagogiques, pas la cosmologie initiale ni les attributions miraculeuses ultérieures.
- **Travaux de Daniel Siegel sur "the developing mind"** : utiles comme synthèse mais à citer en source secondaire ; les sources primaires sont Schore, Stern, Tronick, Porges.
- **Études de cas IDG (Inner Development Goals)** : utilisables pour cadrer la question, pas comme preuve empirique tant que le cadre n'a pas accumulé de validation longitudinale.
- **Travaux de Marshall Rosenberg sur la CNV** : utiles dans certains contextes (Couche 4 *Cercles de Voix*), mais à utiliser **avec prudence** — la CNV mal pratiquée produit des effets pervers documentés (cf. débat 2018-2024).

---

## Sources que l'édifice ne cite PAS et qui pourraient sembler manquantes

Certains lecteurs pourraient s'étonner de ne pas trouver :

- **Daniel Kahneman *Thinking Fast and Slow*** — pop-psychology utile mais non central. Préférer les travaux primaires sur le dual-process (System 1/2) ou sur les heuristiques (Tversky, Stanovich, Mercier).
- **Steven Pinker *The Better Angels of Our Nature*** — synthèse contestée par historiens et anthropologues sur sa méthode statistique. Non mobilisée car insuffisamment robuste sur les longues périodes.
- **Yuval Harari *Sapiens / Homo Deus / 21 Lessons*** — vulgarisation utile pour grand public, mais imprécision empirique trop fréquente pour servir de fondement à une couche.
- **Jordan Peterson** — compendium psycho-religieux. Non mobilisé car les claims empiriques (psychometriques, neuroscientifiques) sont mélangés avec des prescriptions normatives sans démarcation claire.
- **Friedrich Hayek / École autrichienne d'économie** sur l'apprentissage spontané — non mobilisé car la transposition au domaine pédagogique enfantin a des effets idéologiques traçables (école de Chicago dérivée).
- **Jean Piaget** — utilisable historiquement, mais nombre de ses claims spécifiques (stades fixes, conservation, etc.) ont été remis en cause empiriquement (Brentano, Diamond, Carey). L'édifice cite le constructionnisme **post-Piaget** (Papert) plus que Piaget tel quel.
- **B.F. Skinner / behaviorisme classique** — utilisable historiquement, mais les principes de renforcement appliqués à l'enfance produisent des effets contraires aux objectifs de l'édifice (cf. Couche 2 *droit à la curiosité préservée*).
- **Cours en ligne (MOOCs, Khan Academy, Duolingo)** — non utilisés comme preuves d'efficacité éducative car les résultats publiés portent sur des populations auto-sélectionnées et la complétion réelle reste faible (~5-15 %).
- **Méthodes "neuro-pédagogiques" populaires** (méthodologie Brain Gym, Edu-K, etc.) — non scientifiques validées, parfois pseudo-scientifiques.

L'édifice peut **citer ces sources** dans les angles morts ou les passages contestables, mais ne les pose pas comme **fondements**. La distinction est doctrinale.

---

## Comment proposer un ajout / retrait

Pull Request avec :

1. **Source concernée** (nom, lien, contexte d'usage habituel).
2. **Catégorie d'exclusion** proposée (🚫 / ⛔ / 🔒 / 🚧 / cas frontière).
3. **Justification** : qu'est-ce qui rend la source non-mobilisable comme fondement ?
4. **Ce que perd l'édifice** en l'excluant — pour évaluer le coût.
5. **Alternative** : quelle source primaire utiliser à la place ?

Discussion publique 7 jours minimum. Convergence multi-référents (cf. [`DECISIONS.md` ADR-0008](decisions/)) pour validation.

---

## Pour les chercheurs hostiles

Si vous trouvez l'édifice manque d'une source canonique de votre courant, deux questions :

1. **Cette source est-elle dans ma bibliographie négative ?** Si oui, raison documentée.
2. **Cette source devrait-elle y être ?** Si oui, ajouter par PR avec justification.

Pour les sources que je n'ai pas explicitement exclues mais que vous trouvez manquantes : ce n'est probablement pas un refus doctrinal mais un oubli de synthèse. Ouvrir une [Issue GitHub](https://github.com/SanTiepi/anthropie-edifice/issues) avec tag `lecture-critique` proposant l'ajout, en précisant à quelle couche elle s'applique.

---

*« Une bibliographie sans bibliographie négative est une posture sans courage. »*
