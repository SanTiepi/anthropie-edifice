# L'Anthropie — Reprendre l'édifice (fork anonyme CC0)

> *Si vous voulez **reprendre, renommer, héberger** l'édifice — totalement ou partiellement — sans contact avec les auteurs originaux, voici comment. Aucune permission n'est requise.*

CC0 1.0 Universal. *« Si l'édifice n'est plus attribuable à personne dans 5-10 ans, c'est le succès. »*

Vous reprenez sous **votre responsabilité**, dans **votre contexte**, avec **vos termes**. Aucune autorité n'a à valider votre fork. Aucune signature n'est due. Aucune notification n'est demandée.

Avant de prototyper sur le terrain : lire [`SAFETY.md`](SAFETY.md). Les garde-fous (protection mineurs, non-thérapie, anti-secte, co-design souverain) demeurent éthiquement non-négociables, **même** si vous renommez l'édifice.

---

## 1. Pourquoi forker

Vous pourriez vouloir :

- **Continuer l'édifice** sous un autre nom dans un autre contexte culturel.
- **Le renommer** parce qu'« Anthropie » ne résonne pas dans votre langue ou tradition.
- **Le subdiviser** : ne reprendre qu'une couche (ex. seulement la Couche 4 PAROLE pour un projet d'éducation au langage post-LLM).
- **Le traduire intégralement** dans une langue non encore couverte (priorité [`CONTRIBUTING.md`](CONTRIBUTING.md) §5 : EN, ES, AR, ZH, HI, SW, PT).
- **Le reprendre en cas d'arrêt** des mainteneurs initiaux (cf. [`REFUTATION.md`](REFUTATION.md) §1).
- **Le purger** des références autochtones controversées et le republier sans elles, si une communauté le demande.
- **Documenter votre désaccord** — un fork divergent qui critique l'édifice est une contribution légitime.

---

## 2. Démarche technique minimale

```sh
# 1. Cloner sans historique d'identité
git clone --depth 1 https://github.com/SanTiepi/anthropie-edifice.git mon-edifice
cd mon-edifice

# 2. Supprimer l'historique git (anonymat strict)
rm -rf .git
git init
git add .
git commit -m "Reprise CC0 de L'Anthropie — premier commit indépendant"

# 3. Vérifier qu'aucune métadonnée personnelle ne reste
grep -ri "Robin Fragnière" .   # devrait ne rien renvoyer dans les fichiers publics
grep -ri "fragniere" .         # idem
git log                        # un seul commit, identité de votre choix
```

**Vérifications de métadonnées** à faire AVANT premier push :

- [ ] `git config user.name` et `user.email` configurés à l'identité que vous voulez assumer (ou à `Anthropie Network <contact@example.org>` si vous reprenez en anonymat strict).
- [ ] Aucune mention nominative des auteurs initiaux dans les fichiers (les fichiers publics actuels ne devraient pas en contenir, mais vérifier `CITATION.cff`).
- [ ] Aucun fichier privé du clone original n'a été conservé (les `.gitignore`d ne sont pas dans le clone, mais vérifier deux fois).
- [ ] Le `LICENSE.md` reste CC0 1.0 Universal **ou** une licence compatible (CC-BY est compatible si vous voulez exiger attribution sur votre version, mais vous ne pouvez pas restreindre rétroactivement les versions CC0 antérieures).

---

## 3. Choix de licence pour votre fork

CC0 vous donne le droit de relicencer vos modifications. Les options principales :

| Licence | Effet | Quand choisir |
|---|---|---|
| **CC0 1.0 Universal** (identique) | Domaine public, aucune attribution. | *Vous voulez l'auto-effacement progressif. C'est le choix par défaut, le plus aligné avec la doctrine d'origine.* |
| **CC-BY 4.0** | Attribution requise. | *Vous voulez que votre travail soit attribué à votre communauté ou à votre nom.* |
| **CC-BY-SA 4.0** | Attribution + share-alike (toute version dérivée doit aussi être CC-BY-SA). | *Vous voulez empêcher des forks commerciaux fermés.* |
| **CC-BY-NC 4.0** | Attribution + interdiction usage commercial. | *Rare en éducation civilisationnelle, parfois utilisé en co-design autochtone.* |

**Vous ne pouvez PAS** relicencier les versions originales (elles restent CC0). Vous pouvez uniquement relicencier vos *modifications* et la version *fork* que vous publiez.

Pour les co-designs avec communautés autochtones, **demander à la communauté** quelle licence elle préfère pour la version qui mobilise sa tradition. La souveraineté communautaire prime sur la doctrine du commissariat originel.

---

## 4. Anonymat technique du fork

Si vous reprenez en anonymat strict (recommandé pour cohérence doctrinale) :

- **Hébergement** : GitHub avec un compte dédié (ex. `anthropie-network-fr`, `anthropie-suomi`, `anthropy-en`). Évitez votre compte GitHub personnel.
- **DNS** : domaine acheté avec un service qui supporte le whois privacy. Infomaniak (CH), Gandi (FR), Cloudflare Registrar (intl.) supportent.
- **Email de contact** : alias générique (`contact@<votre-domaine>`), pas de boîte personnelle.
- **Commits** : `git config user.name "Anthropie <fork-name>"` + `user.email "contact@<votre-domaine>"`. Pas de PGP signing personnel.
- **CI/CD** : GitHub Actions par défaut OK. Évitez les services qui exigent une identité réelle (Vercel, Netlify si en compte personnel — utiliser GitHub Pages).

Pour reprendre en **identité publique assumée** (par exemple si vous êtes une fondation ou une communauté nommée), c'est aussi un choix légitime — l'édifice CC0 ne vous l'interdit pas. La doctrine d'anonymat était celle du commissariat *originel*, pas une exigence pour les forks.

---

## 5. Structure minimale recommandée pour un fork

Pour qu'un fork reste reconnaissable comme dérivé d'Anthropie sans pour autant en dépendre :

- Garder les **noms canoniques des 12 couches** ou expliciter le mapping si vous renommez (ex. *« Couche 8 LA MYCOLOGIE → notre version : THE WEAVE »*).
- Garder la **charpente juridique 31bis-duodecies** ou expliciter votre alternative (ex. proposition à la Convention africaine sur les droits de l'enfant plutôt qu'à la CRC).
- Garder la **charte anti-appropriation** ou la renforcer (jamais l'affaiblir).
- Garder ou renforcer **`SAFETY.md`** (jamais l'affaiblir).
- Documenter dans un `FORK_NOTES.md` ce qui change par rapport à l'original, et pourquoi.

Ce ne sont pas des obligations légales (CC0). Ce sont des recommandations pour ne pas perdre la cohérence civilisationnelle qui faisait la valeur de l'édifice initial.

---

## 6. Compatibilité communautaire

Les forks divergents sont **bienvenus**. Aucun *true Anthropie* n'existe.

- **Forks complémentaires** (langue, contexte) : la communauté de porteurs initiaux pourra référencer votre fork dans son repo si vous le souhaitez. Ouvrir une Issue tag `lecture-critique` ou `prototype-ou-traduction`.
- **Forks divergents** (désaccord doctrinal) : vous n'avez besoin de rien demander. Documentez votre désaccord dans votre fork ; la communauté originale ne s'opposera pas à votre existence (et n'a pas le pouvoir de s'y opposer juridiquement).
- **Forks abusifs** (marque commerciale, charisme-leader, exploitation mineurs) : la communauté originale se désolidarisera publiquement (cf. [`PROTOTYPES.md`](PROTOTYPES.md) "En cas d'usage abusif"). Mais vous restez juridiquement libre, sous votre responsabilité — autorités civiles éventuellement compétentes selon votre juridiction.

---

## 7. Cas particuliers

### Reprendre uniquement une couche

Vous pouvez extraire une seule couche (ex. `anthropie_couche_04_parole.md` pour son protocole de Discipline de Prédiction-Avant-Vocal) et la republier sous un autre nom (ex. `pav_methodology.md`). Citez le repo d'origine si vous le souhaitez (CC0 ne l'exige pas) ou ne le citez pas (CC0 ne l'interdit pas).

### Reprendre après arrêt des mainteneurs initiaux

Si les mainteneurs initiaux annoncent l'arrêt du portage actif (cf. [`REFUTATION.md`](REFUTATION.md) §1), le repo restera accessible CC0. Vous pouvez en reprendre le portage actif sans avoir à négocier — il vous suffit de faire savoir publiquement que vous continuez (Issue ou PR sur l'ancien repo, ou nouveau repo avec lien vers l'ancien).

### Reprendre en désaccord avec un État-pilote

Si un État-pilote intègre 31bis-duodecies en pervertissant l'esprit (ex. utiliser le droit délibératif des enfants pour faire taire les enfants en assemblée), un fork « anti-capture » documentant publiquement le détournement est une contribution civilisationnelle légitime.

### Reprendre une partie en collaboration avec une communauté autochtone

Si une communauté autochtone souhaite reprendre la Couche 11 (Parenté élargie) avec ses propres traditions, le fork est non seulement permis mais **encouragé**. La charte anti-appropriation (Couche 7 Strate 5) inverse le rapport : initiative communautaire prime, pas autorisation.

---

## 8. Ce que vous ne pouvez pas faire (légalement et éthiquement)

CC0 vous donne énormément, mais **ne vous donne pas** :

- Le droit de prétendre que les auteurs initiaux endossent votre fork. Ils ne signent pas, ne valident pas, ne s'engagent pas.
- Le droit de revendiquer une marque déposée « Anthropie® » (juridiquement vous pourriez essayer, mais l'usage civilisationnel précédent vous y oppose un *prior art* solide).
- Le droit de mettre en danger des mineurs ou des personnes vulnérables au nom de l'édifice. Les garde-fous éthiques (`SAFETY.md`) demeurent contraignants éthiquement, pénalement selon votre juridiction.
- Le droit de violer la souveraineté d'une communauté autochtone qui aurait demandé retrait de sa tradition de l'édifice (cf. charte anti-appropriation).

---

## 9. Si vous reprenez sérieusement

Documentez ce que vous faites. Pas pour la doctrine — pour les générations suivantes qui vous reprendront à leur tour. L'édifice est un *patrimoine civilisationnel*, pas un projet personnel. Chaque fork ajoute une strate à la transmissibilité.

*« Le porteur vient après. Et après le porteur, un autre porteur. »*
