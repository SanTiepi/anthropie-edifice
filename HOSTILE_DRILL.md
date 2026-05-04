# L'Anthropie — Exercice de prise hostile et audit adverse gelé

> *Protocole pour tester la résistance réelle de l'édifice à des reprises politiques, idéologiques, commerciales ou journalistiques — et pour documenter les failles avant qu'elles ne soient exploitées par des acteurs réels hostiles.*

CC0 1.0 Universal. Document opérationnel. Conçu pour être exécuté **trimestriellement** au minimum (exercice interne) et **annuellement** au maximum (audit externe gelé).

**Pourquoi ce document ?** Un édifice CC0 anonyme est exposé à plusieurs vecteurs de capture (cf. [`DECISIONS.md` ADR-0010](decisions/) protocole de modification à contre-voix, ADR-0009 sas anti-contamination synthétique). Tester ces vecteurs avant qu'ils ne soient exploités révèle les angles morts. La doctrine du *« l'édifice gagne à être attaqué »* vaut aussi pour les attaques simulées.

---

## Partie A — Exercice trimestriel interne (prise hostile simulée)

### A.1 Objectif

Un mainteneur ou contributeur joue le rôle d'un **acteur hostile** qui tenterait de réécrire, recentrer, capturer ou pervertir l'édifice. Documenter ce qu'il a réussi à modifier, et ce qui aurait dû résister mais n'a pas.

### A.2 Profils d'attaquant à simuler (en rotation trimestrielle)

| Trimestre | Profil | Vecteur d'attaque privilégié |
|---|---|---|
| Q1 | **Faux journaliste investigateur** | extraire un récit individuel attribuable, démasquer le commissariat originel, créer un scoop |
| Q2 | **Lobby commercial éducatif** | déposer marque "Anthropie®", créer formation payante "certifiée", capter clientèle |
| Q3 | **Courant idéologique** (gauche identitaire OU droite traditionnaliste — alterner) | recadrer l'édifice comme outil de leur courant, censurer les couches qui les dérangent |
| Q4 | **État autoritaire** | utiliser article 31quater (droit délibératif enfant) pour faire taire les enfants au lieu de les écouter ; détourner le sens |

### A.3 Protocole de l'exercice

**Étape 1 — Préparation (1h)**
- Tirer au sort le profil parmi les 4, ou utiliser le profil de rotation.
- L'exécutant·e lit le profil, formule en interne sa stratégie d'attaque.
- Aucune communication avec les autres mainteneurs pendant la phase suivante.

**Étape 2 — Exécution (4-8h sur 1-2 jours)**
- L'exécutant·e tente : modifier 1 fichier de couche pour y glisser un biais discret, ouvrir une Issue avec une demande qui semblerait raisonnable mais qui détournerait le sens, soumettre une PR avec un commit message neutre mais un diff problématique.
- Tout doit rester **publiquement traçable** (Issues, PR) — ne pas modifier en privé.
- L'exécutant·e note **chaque réussite** et **chaque échec** (mécanisme qui a bloqué).

**Étape 3 — Revue collective (2h)**
- L'exécutant·e révèle ouvertement ce qu'il/elle a tenté.
- Les autres mainteneurs identifient quelles attaques ont passé silencieusement, lesquelles ont été détectées.
- Documenter dans une Issue épinglée tag `audit-trimestriel`.

**Étape 4 — Correction (1-4 semaines)**
- Pour chaque attaque réussie : proposer un mécanisme de défense (ADR, modification SAFETY, modification REFUTATION, etc.).
- Discuter publiquement, merger sous protocole ADR-0010 (bloc contre-voix).

### A.4 Ce que cet exercice ne fait PAS

- **Pas une vraie attaque.** L'exécutant·e annonce dans l'Issue ouverte que c'est un drill, après l'étape 2.
- **Pas un test pénétration sécurité technique** (clé GitHub volée, etc.). C'est doctrinal/lexical, pas cyber.
- **Pas un instrument de blâme** — l'exécutant·e du trimestre n'est pas évalué·e ; les défenses sont évaluées.

---

## Partie B — Audit adverse gelé (annuel, externe)

### B.1 Objectif

Inviter explicitement un·e chercheur·euse hostile, un·e journaliste investigateur, ou un comité d'éthique externe à auditer l'édifice **selon un protocole figé** — pour transformer la critique diffuse en critique comparable.

### B.2 Kit téléchargeable

Le kit contient :

1. **Corpus figé** : tarball SHA256-vérifiable de l'état actuel du repo (cf. [`REPRODUCE.md`](reproduire/)). Date de figement notée.
2. **Cinq questions imposées** :
   - **Q1** : Quels claims de niveau A (preuves robustes, cf. [`EVIDENCE_MAP.md`](preuves/)) sont selon vous **mal classés** et devraient passer en niveau B ou C ?
   - **Q2** : Quels mécanismes de [`SAFETY.md`](garde-fous/) protègent **réellement** les mineurs et les personnes vulnérables, et lesquels sont du *theater* sans effet pratique ?
   - **Q3** : Quel courant politique, idéologique ou commercial pourrait s'emparer de l'édifice sans que les garde-fous existants ne déclenchent ? Documenter le scénario.
   - **Q4** : Sur les 11 articles 31bis-duodecies, lesquels créeraient des effets pervers documentés en cas d'application réelle dans une juridiction donnée (à votre choix) ?
   - **Q5** : Quelle critique majeure de l'édifice n'est **pas couverte** par [`OBJECTIONS.md`](objections/) ni par [`OPEN_GRIEVANCES.md`](griefs/) ?
3. **Délai** : 4 semaines à compter de réception du kit. Au-delà, audit considéré abandonné.
4. **Règle de publication intégrale** : l'auditeur·trice s'engage à publier sa note **en intégralité**, même défavorable, dans son canal habituel (article académique, billet de blog, Issue GitHub). L'édifice s'engage à la **citer publiquement** quel que soit le verdict, à **ne pas la censurer**, et à **répondre point-par-point** sous 60 jours.

### B.3 Profils d'auditeur recherchés

- Un·e chercheur·euse en sciences cognitives ou éducation **explicitement sceptique** des frameworks alternatifs.
- Un·e journaliste investigateur travaillant sur les sectes, les pseudo-thérapies, ou les dérives éducatives.
- Un comité d'éthique d'une institution non-partisane (Comité national d'éthique, INSERM, équivalent).
- Un·e chercheur·euse en droits humains ou droits de l'enfant explicitement critique de l'extension juridique proposée.
- Un·e représentant·e d'une communauté autochtone ayant lu les couches mobilisant sa tradition.

### B.4 Comment proposer / accepter un audit

**Pour proposer** un audit (extérieur à l'édifice) : envoyer une [Issue GitHub](https://github.com/SanTiepi/anthropie-edifice/issues) avec tag `audit-adverse`, en précisant :
- profil de l'auditeur·trice (académique, journalistique, etc.) ;
- canal de publication prévu (revue, journal, blog) ;
- compatibilité avec la règle de publication intégrale.

**Pour les mainteneurs** : accepter ou décliner publiquement sous 30 jours. Refus possible si conflit d'intérêts évident (cf. [`MANDATES.md`](mandats/)) — refus motivé publiquement.

### B.5 Compromis financier (option)

L'édifice étant CC0 et sans personne morale, **il ne peut pas rémunérer l'auditeur·trice**. Néanmoins :

- Un porteur institutionnel (fondation, État-pilote, université) **peut** financer un audit indépendant via son budget propre ; le kit reste figé pour assurer comparabilité.
- L'auditeur·trice retient sa rémunération de son commanditaire ; les conclusions restent indépendantes.

---

## Partie C — Pourquoi le combiner avec l'exercice trimestriel

L'exercice trimestriel **interne** détecte les angles morts que les mainteneurs voient déjà à demi-mot. L'audit annuel **externe** détecte les angles morts qu'aucun mainteneur n'aurait vus, parce qu'ils sont **invisibles depuis l'intérieur** de la doctrine.

Les deux sont nécessaires. Ni l'exercice interne ni l'audit externe ne suffit seul.

---

## Partie D — Tracer le cycle

Tenir une page récapitulative (ou l'inscrire dans une Issue épinglée tag `audit-historique`) listant :

- Date d'exercice / date d'audit.
- Profil exécuté / auditeur·trice.
- Lien public vers l'Issue / le rapport publié.
- Résumé des défenses qui ont tenu.
- Résumé des modifications doctrinales déclenchées.

Sur 5 ans, ce tableau **est** le test de robustesse de l'édifice. S'il reste vide après 2-3 ans, c'est qu'aucun exercice n'est conduit, ce qui est doctrinalement plus grave que d'échouer à un exercice.

---

## Partie E — Pour les forks

Cf. [`FORKING.md`](forker/). Tout fork sérieux **devrait** maintenir son propre cycle d'exercice/audit selon ce protocole, ou un protocole équivalent qu'il publie. Un fork qui revendique le nom de l'édifice mais ne pratique aucun audit s'expose à désolidarisation publique (cf. [`PROTOTYPES.md`](prototyper/) "En cas d'usage abusif").

---

*« On ne se défend pas contre un attaquant qu'on n'a jamais simulé. On ne mûrit pas sans critique qu'on n'a pas invitée. »*
