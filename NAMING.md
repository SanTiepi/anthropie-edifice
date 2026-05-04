# L'Anthropie — Nommage canonique et clauses de non-affiliation

> *Comment nommer l'édifice correctement, et comment poser explicitement l'absence de lien avec Anthropic, OpenAI, ou tout autre acteur commercial. Pour éviter à la fois la confusion et l'affiliation involontaire.*

CC0 1.0 Universal. Document doctrinal complémentaire de [`NOT_AN_AI_LAB.md`](pas-un-labo-ia/) et [`DECISIONS.md` ADR-0013](decisions/).

---

## 1. Forme canonique du nom

### Forme longue (à privilégier en première mention)

> **L'Anthropie — édifice civilisationnel d'apprentissage humain à 12 couches, CC0 1.0 Universal, sans lien avec Anthropic PBC.**

### Formes courtes acceptables

- *L'Anthropie* (avec article défini, en français)
- *l'édifice Anthropie*
- *Anthropie Network* (collectif éditorial anonyme — usage signature)
- *anthropie.org* (URL canonique)

### Formes à éviter

- ❌ *Anthropie AI*, *Anthropie Labs*, *Anthropie Inc.* — ces formulations suggèrent un acteur IA propriétaire qui n'existe pas.
- ❌ *Anthropic Project* — confusion directe avec l'entreprise Anthropic.
- ❌ *AnthroPy* (mauvaise capitalisation) — pas de lien avec Python.
- ❌ *Anthropie™* — l'édifice est CC0, pas une marque déposée.
- ❌ *L'Anthropy* — orthographe anglicisante non-canonique.

### Formes en langues étrangères (en attente de traduction)

| Langue | Forme proposée | Notes |
|---|---|---|
| EN | *The Anthropie — Human Learning Edifice* (ou *Civilisational Architecture of Human Learning*) | Garder le mot français *Anthropie*, pas *Anthropy* (homographie avec *anthropy* archaïque) |
| ES | *La Anthropie — edificio civilizacional* | Garder *Anthropie* |
| AR | الأنثروبية — الصرح الحضاري | Translittération à valider en co-design |
| ZH | 人類學構築 (proposition) | À valider en co-design |
| HI / SW / PT | en attente | Voir [`CONTRIBUTING.md` §5](contribuer/) |

Toute traduction se fait sous CC0, avec validation publique par discussion 7 jours minimum (cf. [`DECISIONS.md` ADR-0008](decisions/)).

---

## 2. Clauses de non-affiliation à utiliser

### Clause minimale (en bas de tout document public)

> *L'Anthropie est sans lien institutionnel, organisationnel ni financier avec Anthropic PBC, OpenAI, Google DeepMind, Mistral AI, Hugging Face, ou tout autre acteur commercial de l'IA. L'homonymie avec Anthropic est fortuite.*

### Clause étendue (en cas de question explicite)

> *L'Anthropie est un édifice civilisationnel d'apprentissage humain publié sous CC0 1.0 Universal et porté anonymement par le collectif éditorial Anthropie Network. Le projet n'a pas de personne morale, pas de financement, pas de revenus, pas de modèle d'IA produit ni hébergé. Il n'est affilié à aucune entreprise d'IA, à aucun parti politique, à aucune organisation religieuse ou philanthropique nommée. L'usage de l'IA dans la production initiale du corpus est documenté explicitement dans `SAFETY.md` §8 et `DECISIONS.md` ADR-0006.*

### Clause juridique (pour usage formel, par exemple lors d'un dépôt institutionnel)

> *« L'Anthropie est un corpus normatif et pédagogique en domaine public (CC0 1.0 Universal) sans personne morale identifiable. Toute responsabilité juridique liée à l'usage de l'édifice incombe à la personne ou organisation qui en fait usage. Cf. LEGAL_BOUNDARIES.md du repository officiel pour le cadre complet. »*

---

## 3. Métadonnées canoniques

### Pour les bibliographies académiques

```bibtex
@misc{anthropie_edifice_2026,
  title        = {{L'Anthropie} --- édifice civilisationnel d'apprentissage humain à 12 couches},
  author       = {{Anthropie Network}},
  year         = {2026},
  month        = {4},
  publisher    = {Anthropie Network (collectif anonyme CC0)},
  howpublished = {\url{https://anthropie.org}},
  url          = {https://github.com/SanTiepi/anthropie-edifice},
  note         = {CC0 1.0 Universal --- Public Domain Dedication. Aucune attribution requise. Sans affiliation à Anthropic PBC, OpenAI ou tout acteur commercial de l'IA.},
  version      = {0.1}
}
```

### Pour les balises HTML / JSON-LD

Les pages du site portent déjà :

- `<meta name="author" content="Anthropie Network" />`
- `<meta name="dcterms.rights" content="CC0 1.0 Universal — Public Domain Dedication" />`
- JSON-LD `"creator": { "@type": "Organization", "name": "Anthropie Network" }`

À ajouter dans une itération ultérieure pour renforcer la non-affiliation lisible-machine :

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "L'Anthropie",
  "alternateName": "Anthropie",
  "publisher": { "@type": "Organization", "name": "Anthropie Network" },
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/publicdomain/zero/1.0/",
  "additionalProperty": [
    {
      "@type": "PropertyValue",
      "name": "non-affiliation",
      "value": "Sans lien institutionnel avec Anthropic PBC, OpenAI, Google DeepMind, ou tout acteur commercial de l'IA."
    }
  ]
}
```

---

## 4. Conduite à tenir face aux confusions documentées

### Confusion *« est-ce un projet d'Anthropic ? »*

Réponse rapide : *non*. Renvoyer vers [`NOT_AN_AI_LAB.md` §1](pas-un-labo-ia/).

### Confusion *« vous publiez un modèle d'IA ? »*

Réponse rapide : *non, l'Anthropie publie un corpus textuel, pas de modèle*. Renvoyer vers [`NOT_AN_AI_LAB.md` §2](pas-un-labo-ia/).

### Demande *« nous voulons collaborer entre Anthropic et Anthropie »*

Réponse : c'est juridiquement possible (CC0), mais l'Anthropie n'a pas de personne morale pour signer une collaboration. L'entreprise peut **utiliser** le corpus librement (CC0). L'Anthropie reste **séparée** et ne s'inscrit dans aucun partenariat formel.

### Demande *« nous voulons financer l'Anthropie »*

Réponse : l'Anthropie n'a pas de structure réceptrice. Vous pouvez :
1. Financer un **porteur** (chercheur, ONG, fondation) qui prototype une couche ou en fait un dépôt institutionnel.
2. Financer un **fork** sous votre marque qui respecte la doctrine ([`FORKING.md`](forker/)).
3. Financer la **traduction** d'une couche dans une langue prioritaire ([`CONTRIBUTING.md` §5](contribuer/)).

L'argent doit toujours s'arrêter aux **personnes** et aux **prototypes**, jamais à l'édifice lui-même qui n'a pas de compte.

### Tentation *« déposons une marque pour protéger »*

Réponse doctrinale : non. La marque déposée violerait la doctrine CC0 + anonymat (cf. [`DECISIONS.md` ADR-0001-0002](decisions/)). La protection se fait par **présence active d'une communauté de porteurs** qui se désolidarise publiquement des usages abusifs (cf. [`PROTOTYPES.md` §usage abusif](prototyper/)).

---

## 5. Pour les médias et journalistes

### Présentation type 1 ligne

*« L'Anthropie est un édifice civilisationnel d'apprentissage humain en domaine public (CC0), publié anonymement, sans lien avec Anthropic. »*

### Présentation type 1 paragraphe

*« L'Anthropie est un corpus pédagogique et juridique de 12 couches couvrant l'arc 0 à infini de la vie humaine, avec une charpente de 11 articles d'extension proposée à la Convention relative aux droits de l'enfant. Publié sous CC0 1.0 Universal sans signature personnelle, hébergé sur anthropie.org sans tracking. Le projet est dans une phase Transmission embryonnaire (mai 2026) et cherche des porteurs : chercheurs, juristes droits enfants, communautés autochtones, fondations, États-pilotes (Norvège, Costa Rica, Nouvelle-Zélande, Bhoutan, Québec). Sans lien avec l'entreprise Anthropic. »*

### Pour interview ou citation

L'édifice **n'a pas de porte-parole**. Les réponses se font par référence aux fichiers publics. Toute citation directe d'un porteur engage **cette personne** à titre individuel, pas l'édifice.

### Photo / portrait

Aucune photo, aucun portrait, aucune voix individuelle ne peut représenter l'édifice. Les illustrations possibles : le schéma SVG des 12 couches stackées (cf. [`/`](/) ou `site/src/components/CouchesSchema.astro`), le logotype textuel *Anthropie Network*, les pages individuelles du site (captures d'écran).

---

## 6. Pour les institutions et fondations

### Lettre type non-affiliation à joindre à un dossier

> *« Nous sollicitons le soutien de [Institution] pour [projet précis] inspiré de l'édifice Anthropie (anthropie.org, CC0 1.0 Universal). Nous précisons que ce projet est porté par [notre organisation] et n'engage pas l'Anthropie elle-même, qui est un patrimoine documentaire en domaine public sans personne morale. L'Anthropie est sans lien avec Anthropic PBC, OpenAI ou tout autre acteur commercial de l'IA. Les responsabilités juridiques liées au prototype ou au déploiement nous incombent intégralement. »*

### Pour un dépôt onusien (BIE Genève, UNICEF Innocenti, Eurochild)

L'Anthropie peut être citée comme **source CC0** d'une proposition d'extension de la CRC. Le dépôt formel est porté par **votre institution**, pas par l'Anthropie. La paternité de la proposition est juridiquement vôtre une fois reformulée et déposée. Cf. [`LEGAL_BOUNDARIES.md` §3](cadre/).

---

## 7. Évolution de ce nommage

Si dans 5-10 ans la confusion avec Anthropic devient ingérable malgré ces clarifications, possibilité de :

1. **Renommer** sous un terme moins ambigu (vote de la fédération de porteurs ; coût de migration assumé).
2. **Ajouter un sous-titre permanent** *« édifice civilisationnel CC0 — sans lien avec Anthropic »* en métadonnées de toute page.
3. **Disparaître** (auto-effacement progressif, cf. [`DECISIONS.md` ADR-0011](decisions/)) et laisser les forks porter sous d'autres noms.

L'option 3 reste doctrinalement souhaitable : *« si l'édifice n'est plus attribuable à personne dans 5-10 ans, c'est le succès. »*

---

*« Le nom de l'édifice n'est pas l'édifice. Le nom des personnes n'est pas la doctrine. »*
