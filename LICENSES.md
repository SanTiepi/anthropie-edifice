# L'Anthropie — Matrice de licences par artefact

> *Quelle licence s'applique à quoi. Réponse explicite à la question : « pourquoi CC0 sur du code de site, alors que MIT ou Apache 2.0 serait plus standard ? »*

CC0 1.0 Universal. Document doctrinal complémentaire de [`LICENSE.md`](https://github.com/SanTiepi/anthropie-edifice/blob/master/LICENSE.md) (texte légal complet).

---

## 1. Réponse courte

**Tout l'édifice est CC0 1.0 Universal**, **par décision doctrinale assumée**, y compris le code source du site `site/`. Les utilisateurs qui requièrent une licence logicielle plus standard (MIT, Apache 2.0) peuvent **traiter le code comme s'il était sous MIT** — CC0 inclut toutes les permissions de MIT, sans clause d'attribution.

Pour les détails et alternatives examinées, voir ci-dessous.

---

## 2. Matrice par artefact

| Artefact | Licence | Justification |
|---|---|---|
| **12 fichiers de couche** (`anthropie_couche_*.md`) | **CC0 1.0** | Corpus textuel principal — domaine public assumé. Cf. [`DECISIONS.md` ADR-0001](decisions/). |
| **20+ documents structurants** (KERNEL, SAFETY, REFUTATION, DECISIONS, FORKING, etc.) | **CC0 1.0** | Documents normatifs en domaine public. |
| **Articles 31bis-duodecies** (proposition d'extension CRC) | **CC0 1.0** | Une proposition juridique en domaine public peut être amendée par tout État pilote sans demander permission. C'est doctrinal. |
| **Site web Astro `site/`** (HTML, CSS, TS) | **CC0 1.0** | Cohérence doctrinale et simplicité. Voir §3 ci-dessous pour la justification face à l'audit deep-research qui notait l'inhabituel de CC0 sur code. |
| **Schéma SVG des 12 couches** (`site/src/components/CouchesSchema.astro`) | **CC0 1.0** | Asset visuel de l'édifice. |
| **Favicon, OG image** (`site/public/*.svg`) | **CC0 1.0** | Pas de marque, pas de logotype protégé. |
| **`prepare-content.mjs`** (script Node ESM) | **CC0 1.0** | Outillage de build, ~200 lignes, sans dépendance externe. |
| **`couches.ts`** (données canoniques 12 couches + 11 articles) | **CC0 1.0** | Métadonnées en domaine public. |
| **CITATION.cff** (métadonnées académiques) | **CC0 1.0** | Métadonnées de citation. |
| **Issue templates GitHub** (`.github/ISSUE_TEMPLATE/*.md`) | **CC0 1.0** | Gabarits de gouvernance ouverte. |

---

## 3. Pourquoi CC0 sur le code du site (et pas MIT) ?

### Argument doctrinal

L'édifice prend la position que **CC0 est une licence valide pour du code**, pas seulement pour du contenu. CC0 inclut explicitement la renonciation aux droits d'auteur ET aux droits voisins (incluant les droits sur les œuvres logicielles dans la majorité des juridictions).

CC0 va **plus loin** que MIT en termes de permissivité : MIT exige le maintien de la mention de copyright ; CC0 ne l'exige pas (cohérent avec l'anonymat doctrinal).

### Pour les utilisateurs qui doivent garantir une licence logicielle classique

Si votre organisation, votre commanditaire ou votre revue exige formellement une licence reconnue comme licence logicielle (MIT, Apache 2.0, BSD, GPL), **vous pouvez traiter le code de l'édifice comme s'il était sous MIT** sans risque juridique :

- CC0 inclut toutes les permissions accordées par MIT (utiliser, modifier, distribuer, vendre, sous-licencier, intégrer dans logiciel propriétaire).
- CC0 n'impose **aucune** des contraintes de MIT (mention de copyright, mention de licence dans copies).
- Vous pouvez **rajouter** votre propre licence MIT/Apache 2.0 à votre fork du code, et ce fork sera valide. CC0 ne contraint pas votre relicence aval.

Concrètement : si vous forkez `site/` pour héberger votre propre Anthropie, vous pouvez le distribuer sous MIT, Apache 2.0, ou même propriétaire. CC0 ne s'oppose à aucune de ces évolutions.

### Pour les utilisateurs qui craignent des problèmes de brevet

CC0 ne contient **pas** de clause de licence de brevet explicite (contrairement à Apache 2.0 §3). C'est une faiblesse théorique mais pratiquement nulle pour ce projet :

- L'édifice ne contient **aucun algorithme brevetable** (pas de modèle d'IA, pas d'architecture novatrice, pas d'invention technique).
- Le code Astro statique est trivial sur le plan brevet.
- Si une zone de brevet apparaît dans une itération future (ex. mécanisme cryptographique original), elle sera traitée par ADR dédiée à ce moment-là.

### Pour les utilisateurs qui souhaitent une licence plus protectrice du share-alike

Si vous voulez **forcer** que vos modifications restent sous licence libre (effet copyleft), CC0 ne le permet pas. Vous devez :

1. Forker.
2. Relicencer votre fork sous CC-BY-SA 4.0, GPL-3.0 ou licence copyleft équivalente.
3. Documenter dans votre [`FORK_NOTES.md`](forker/) la raison de la divergence.

L'édifice originel reste CC0 ; votre fork peut être plus restrictif. C'est légalement compatible (CC0 n'oblige pas à rester CC0 en aval).

---

## 4. Alternatives examinées et rejetées

### Dual-license CC0 (contenu) + MIT (code site)

**Examiné, rejeté.** Raisons :

- Augmente la complexité légale de l'édifice (deux licences à comprendre, deux périmètres à délimiter).
- Crée des frontières difficiles à maintenir (où s'arrête le contenu, où commence le code ? Le frontmatter YAML est-il du code ?).
- Casse la doctrine "CC0 sur tout".
- Les utilisateurs qui requièrent MIT peuvent déjà traiter CC0 comme MIT (cf. §3).

### Apache 2.0 sur le code site

**Examiné, rejeté.** Raisons :

- Apache 2.0 exige préservation de notices et liste des modifications. Inadapté à un édifice anonyme.
- Apache 2.0 introduit clause de licence de brevet — pas d'utilité pratique pour ce projet (cf. §3).
- Augmente la complexité.

### Public Domain par déclaration unilatérale (sans CC0)

**Examiné, rejeté.** Raisons :

- Le domaine public n'est pas reconnu uniformément dans toutes les juridictions (notamment en France/Allemagne où les droits moraux sont inaliénables).
- CC0 fournit le mécanisme légal le plus solide pour atteindre l'effet "domaine public" cross-juridiction.

### Marque déposée *Anthropie®* + licence custom

**Rejeté doctrinalement.** Cf. [`DECISIONS.md` ADR-0001](decisions/) : violerait la doctrine "personne ne le possède".

---

## 5. Mention dans les fichiers individuels

Aucun fichier de l'édifice **n'inclut** de en-tête de copyright (cohérent avec CC0 et l'anonymat). Pour les contributeurs externes : ne pas ajouter d'en-tête de copyright dans vos PR. Si vous voulez documenter votre contribution, faites-le dans le commit message ou dans une [Issue GitHub](https://github.com/SanTiepi/anthropie-edifice/issues).

---

## 6. Cas du contenu co-designé avec communautés autochtones (Couches 7, 10, 11)

**Doctrine** : CC0 est le défaut. La promesse de retrait souverain 90 jours (charte anti-appropriation) **n'est pas opposable juridiquement** sous CC0 — elle dépend de la désolidarisation publique de la communauté de porteurs (cf. [`DECISIONS.md` ADR-0012](decisions/)).

**Si une communauté autochtone signataire demande explicitement une licence plus restrictive pour SES couches co-designées**, la fédération de porteurs examinera l'option d'une migration vers CC-BY-SA-NC ou licence communautaire équivalente sur ces seules couches. Décision par convergence multi-référents (ADR-0008) après discussion 7 jours.

Tant qu'aucune communauté autochtone n'est signataire effective, le débat est théorique. Cf. [`OPEN_GRIEVANCES.md` G-001](griefs/).

---

## 7. Pour ajouter un nouvel artefact

Tout nouveau fichier ajouté à l'édifice est **par défaut sous CC0**. Aucune mention de licence à ajouter dans le fichier lui-même.

Si vous voulez que votre contribution soit sous licence différente (CC-BY-SA, MIT explicite, etc.) :

1. Ouvrir une discussion par PR avec justification (raison doctrinale ou contractuelle).
2. Discussion publique 7 jours minimum.
3. Convergence multi-référents (cf. [`DECISIONS.md` ADR-0008](decisions/)).
4. Si accepté, le fichier porte un en-tête de licence explicite et est listé dans la matrice §2 ci-dessus.

L'édifice peut accommoder des fichiers sous licence différente, mais c'est l'exception, pas la règle.

---

## 8. Cas du fork

Tout fork ([`FORKING.md`](forker/)) peut relicencier ses **propres modifications** sous la licence de son choix (compatible CC0 → CC0, CC-BY, CC-BY-SA, MIT, Apache 2.0, GPL, propriétaire, etc.). Le contenu antérieur **reste CC0**.

Cf. [`FORKING.md` §3](forker/) pour le tableau des choix de licence pour fork.

---

## 9. Lecture machine — `licenses.json`

Pour les outils qui consomment l'édifice automatiquement (ex. RAG, indexeurs, audits de licence), un fichier `licenses.json` à la racine peut être ajouté dans une itération future avec ce contenu type :

```json
{
  "$schema": "https://anthropie.org/schemas/licenses.schema.json",
  "default_license": "CC0-1.0",
  "default_license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
  "policy": "All artefacts in this repository are CC0 1.0 Universal by default. Doctrinal decision documented in DECISIONS.md ADR-0001. See LICENSES.md for per-artefact matrix and rationale.",
  "exceptions": [],
  "non_affiliation": "Anthropie has no institutional, organizational, or financial link with Anthropic PBC, OpenAI, Google DeepMind, Mistral AI, or any commercial AI actor. The phonetic similarity with 'Anthropic' is coincidental.",
  "contact_for_licensing_questions": "https://github.com/SanTiepi/anthropie-edifice/issues"
}
```

À implémenter dans une itération ultérieure (codex iter#17 #3 — backlog).

---

## 10. Si vous avez encore un doute

Ouvrir une [Issue GitHub](https://github.com/SanTiepi/anthropie-edifice/issues) avec tag `legal`. Réponse argumentée publique sous 30 jours. Voir aussi [`LEGAL_BOUNDARIES.md`](cadre/) pour le cadre juridique global.

---

*« Une licence claire évite mille discussions. CC0 est claire — y compris quand elle paraît inhabituelle. »*
