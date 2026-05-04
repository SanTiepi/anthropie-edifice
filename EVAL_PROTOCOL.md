# L'Anthropie — Protocole d'évaluation empirique

> *Comment évaluer un prototype Anthropie à 90 jours et à 6/12/24 mois — sans glisser vers le management ni vers le marketing. Réponse au deep-research audit signalant l'absence de protocole empirique formalisé.*

CC0 1.0 Universal. Document opérationnel. Modifiable par PR avec discussion publique 7 jours minimum.

**Pourquoi ce document ?** L'édifice publie [`EVIDENCE_MAP.md`](preuves/) qui classe les claims par robustesse mais reconnaît qu'**aucune cohorte n'a traversé les inventions propres** (niveau D). Sans protocole d'évaluation publié, les premiers porteurs prototypent à l'aveugle, et l'édifice ne capitalise pas sur leurs apprentissages. Ce document **propose un cadre minimal** — pas un protocole académique RCT, mais un dispositif d'observation honnête à deux horizons.

---

## 1. Deux horizons d'évaluation

### Piste courte — 90 jours (faisabilité)

**Objectif** : valider qu'un prototype **peut tenir** opérationnellement.

**Questions que cette piste doit trancher** :
- Le ratio adulte/enfant prévu se maintient-il sur 12 semaines ?
- Le rythme proposé (hebdo, bi-mensuel, mensuel) tient-il sans épuiser les facilitateurs ?
- Les coûts logistiques réels (heures/sem/personne, espace, déplacements) sont-ils tenables ?
- Aucun incident majeur (cf. [`SAFETY.md`](garde-fous/)) n'a-t-il interrompu ?
- Les participants reviennent-ils volontairement (taux de présence > 60 % à 12 semaines) ?

**Métriques obligatoires** :
- Présence par session (chiffre brut, pas pourcentage agrégé).
- Heures totales investies par animateur·trice et par participant.
- Conflits documentés (1 ligne par incident).
- Demandes de retrait reçues (cf. [`SAFETY.md` §2 consentement et retrait](garde-fous/)).
- Signalements de détresse psychologique aiguë (cf. SAFETY §3).

**Critères d'arrêt** (à définir AVANT de démarrer) :
- Présence < 50 % moyenne sur 4 semaines consécutives.
- Multi-référents tombe à 1 seul animateur·trice pendant > 2 séances.
- Un incident SAFETY non-géré dans les 72h.
- Plainte parentale ou institutionnelle éthique grave non-résolue par médiation.

**Livrable** : rapport public anonymisé sous format [`PROTOTYPES.md`](prototyper/) §gabarit Issue. Publier dans Issues GitHub avec tag `prototype`.

### Piste longue — 6 / 12 / 24 mois (cohorte sentinelle)

**Objectif** : observer les effets **différés** d'une couche ou d'une combinaison de couches.

**Questions que cette piste doit trancher** :
- Les participants à 24 mois témoignent-ils d'effets différés (positifs ou négatifs) ?
- L'attrition naturelle se stabilise-t-elle ou continue-t-elle de baisser ?
- Quels effets inverses non anticipés apparaissent ?
- Le maintien de la pratique est-il viable sans subvention initiale ?

**Métriques** :
- Rétention longitudinale (présence à 6m / 12m / 24m).
- Échantillon de témoignages qualitatifs structurés (5-10 participants, entretiens semi-directifs anonymisés).
- Comparaison avec **groupe témoin informel** (autres adolescents/familles/communauté du même contexte qui n'ont pas participé) — pas un RCT, juste un repère.
- Indicateurs ANTI-WEIRD (cf. fichiers de couche, section O angles morts) — éviter QI, scolarité précoce, autonomie individuelle prématurée.

**Critères de réfutation à 24 mois** :
- Aucun effet différé positif observable malgré méthodologie correcte → niveau D maintenu, pas de promotion.
- Effet inverse documenté (mineurs lésés, communauté pathologisée, etc.) → suspension de la couche concernée (cf. [`REFUTATION.md` §2](refutation/)).
- Capture par dynamique sectaire (cf. [`SAFETY.md` §4](garde-fous/)) → arrêt immédiat + désolidarisation publique.

**Livrable** : étude qualitative ou pré-print académique. Si vous publiez en revue à comité, citer l'édifice via le BibTeX de [`README.md`](https://github.com/SanTiepi/anthropie-edifice/blob/master/README.md). Cf. [`NAMING.md` §3](nommage/) pour les métadonnées canoniques.

---

## 2. Cadre éthique commun aux deux pistes

Toute évaluation doit respecter :

- **Consentement éclairé** des participants et (pour mineurs) des parents/tuteurs. Renouvelable tous les 6 mois.
- **Anonymisation** des données dans tout livrable public.
- **Droit de retrait** sous 90 jours sans justification, sans pénalité (cf. SAFETY §2).
- **Pas de fausse promesse** : les participants savent qu'ils sont laboratoire, pas dans un dispositif validé (cf. [`OBJECTIONS.md` §2 Vous prétendez parler des enfants sans demander aux enfants](objections/)).
- **Comité de relecture éthique** pour les protocoles impliquant mineurs ou personnes vulnérables : minimum 3 référents extérieurs au prototype, idéalement avec un·e clinicien·ne ou éducateur·trice non-Anthropie.
- **Limites** : aucune évaluation Anthropie ne peut prétendre se substituer à un essai clinique de soin. Hospices des Brisures (Couche 12) **complète** les soins, ne les remplace pas (SAFETY §3).

---

## 3. Pour qui propose un pilote

Si vous porteriez un pilote, suivre cette séquence :

1. **Lire** [`SAFETY.md`](garde-fous/), [`PROTOTYPES.md`](prototyper/), [`EVIDENCE_MAP.md`](preuves/), [`REFUTATION.md`](refutation/).
2. **Choisir** une couche ou un mécanisme spécifique (idéalement un claim niveau D dans [`EVIDENCE_MAP.md` §6 dette empirique prioritaire](preuves/)).
3. **Définir** votre protocole : objectifs précis, métriques, critères d'arrêt, échéance d'évaluation.
4. **Documenter** publiquement votre protocole AVANT de démarrer (Issue GitHub, blog, ou fork avec FORK_NOTES.md).
5. **Constituer** votre comité de relecture éthique (3 référents extérieurs minimum).
6. **Démarrer** uniquement si tous les pré-requis sont remplis.
7. **Mesurer** selon votre protocole sans le modifier en cours de route (modification → suspendre + rééditer publiquement).
8. **Publier** votre rapport à 90 jours et/ou à 24 mois, **même si les résultats sont négatifs ou nuls**.

---

## 4. Pour qui veut financer un pilote

Si vous êtes fondation, État-pilote, université, ONG :

- L'édifice **n'a pas de structure réceptrice de financement** (cf. [`LEGAL_BOUNDARIES.md` §2](cadre/) et [`NAMING.md` §4](nommage/) demande de financement).
- Vous pouvez financer **un porteur** (chercheur, équipe, ONG) qui prototype selon ce protocole.
- Vous pouvez financer **votre propre pilote interne** sans demander permission à l'édifice (CC0).
- Vous pouvez financer **la traduction d'une couche** dans une langue prioritaire (cf. [`CONTRIBUTING.md` §5](contribuer/)).

Toute mention de financement doit respecter [`NAMING.md` §6 lettre type non-affiliation](nommage/).

---

## 5. Pour qui audite un pilote (extérieur)

Si vous êtes chercheur·euse, journaliste, comité d'éthique extérieur, et que vous voulez **auditer** un pilote en cours :

1. Utiliser le kit de [`HOSTILE_DRILL.md` Partie B audit adverse gelé](audit-adverse/) — 5 questions imposées, délai 4 semaines, règle de publication intégrale.
2. Demander accès aux **données brutes anonymisées** au porteur (Issue GitHub publique).
3. Si refus du porteur : signaler dans [`OPEN_GRIEVANCES.md`](griefs/) avec format gabarit.
4. Publier votre note même défavorable. L'édifice s'engage à la citer publiquement, à ne pas la censurer, et à répondre point-par-point sous 60 jours.

---

## 6. Liste des pilotes en cours / publiés

*(Mai 2026 — vide. Sera mise à jour à mesure que des prototypes émergent.)*

| ID pilote | Couche(s) | Porteur | Phase (90j / 6m / 12m / 24m) | Statut | Lien rapport |
|---|---|---|---|---|---|
| *(aucun pour l'instant)* | | | | | |

Pour ajouter un pilote : Pull Request sur ce fichier avec ligne nouvelle. Discussion publique 7 jours.

---

## 7. Limites de ce protocole

- **Pas un RCT.** Pas de groupe contrôle randomisé, pas de double aveugle. C'est volontaire — la nature qualitative et longitudinale des couches (5-10 ans Couche 8, 0-∞ Couche 9, etc.) rend le RCT inapproprié pour la majorité des claims.
- **Pas un substitut à l'éthique professionnelle.** Si votre prototype implique des mineurs ou vulnérables, votre déontologie professionnelle (médicale, psychologique, éducative, etc.) prime sur ce document.
- **Pas exhaustif.** Chaque couche a des spécificités (ex. évaluer la Couche 11 *3 Parents Non-Humains* nécessite des indicateurs écologiques + relationnels que ce document ne détaille pas).
- **Évolutif.** Ce protocole sera amendé au fil des premiers pilotes, selon ce qui aura tenu et ce qui aura cassé.

---

## 8. À implémenter dans une itération ultérieure

Backlog interne (cf. [`memory/anthropy_improvements_backlog.md`](https://github.com/SanTiepi/anthropie-edifice/blob/master/memory/anthropy_improvements_backlog.md) si exposé) :

- **`pilots.json`** machine-readable : registre des pilotes en cours/publiés au format JSON, lisible par RAG.
- **Schéma `pilot.schema.json`** : structure d'un rapport de pilote (cadre, métriques, résultats, critères d'arrêt activés ou non, apprentissages).
- **Tableau de bord public** sur le site `/pilotes/` listant les pilotes en cours avec leur phase et leur statut.

Ces éléments restent à construire quand le premier pilote sera réellement engagé.

---

*« Évaluer ne veut pas dire mesurer pour rassurer. C'est mesurer pour réfuter si nécessaire. »*
