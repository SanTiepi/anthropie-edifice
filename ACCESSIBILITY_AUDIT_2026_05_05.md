# Audit accessibilité site — état 2026-05-05

> *Audit rapide WCAG 2.1 AA du site Astro tel que déployé sur anthropie.org au 2026-05-05. Pas une refonte — c'est un état des lieux pour Claude Design (qui s'occupera du design final) et pour contributeurs externes. Document de référence, pas de modification du HTML/CSS Astro existant car réservé Claude Design (cf. Q8).*

CC0 1.0 Universal. Document descriptif.

---

## 1. Synthèse

Le site Astro courant (86 pages, déployé sur anthropie.org) est **majoritairement conforme WCAG 2.1 AA** à l'audit interne. Plusieurs bonnes pratiques sont déjà en place dans `MarkdownLayout.astro` et `index.astro`. Trois points d'amélioration mineurs sont identifiés. **Ne pas modifier avant retour Claude Design** (cf. division des rôles validée 2026-05-04).

## 2. Points conformes ✅

- **Langue déclarée** : `<html lang="fr">` ([MarkdownLayout.astro:8](site/src/layouts/MarkdownLayout.astro#L8))
- **Meta viewport** : `width=device-width, initial-scale=1` ([:12](site/src/layouts/MarkdownLayout.astro#L12))
- **Skip link** : `<a class="skip-link" href="#main">Aller au contenu</a>` ([:229](site/src/layouts/MarkdownLayout.astro#L229)). Position offscreen par défaut + visible au focus ([:49-56](site/src/layouts/MarkdownLayout.astro#L49))
- **Focus visible** : `:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }` ([:57](site/src/layouts/MarkdownLayout.astro#L57))
- **Sémantique HTML** : `<nav aria-label="Navigation site">` ([:230](site/src/layouts/MarkdownLayout.astro#L230)), `<main id="main">` ([:247](site/src/layouts/MarkdownLayout.astro#L247)), `<aside aria-labelledby="contest-title">` ([:250](site/src/layouts/MarkdownLayout.astro#L250)), `<footer>` natif
- **Hiérarchie titres** : `h1` unique par page, h2/h3/h4 cascadés
- **Liens explicites** : aucun *« cliquez ici »*, tous les liens ont du contenu sémantique
- **Image SVG schéma** : `<svg role="img" aria-label="Schéma : les 12 couches d'apprentissage humain par tranche d'âge couverte. Chaque barre représente la fenêtre d'âge d'une couche ; les couches 9, 10 et 12 s'étendent à l'infini.">` ([CouchesSchema.astro:44](site/src/components/CouchesSchema.astro#L44))
- **Reading budget aria-label** : `<span aria-label="Temps de lecture estimé : ..., densité ...">` ([:239](site/src/layouts/MarkdownLayout.astro#L239))
- **Tables sémantiques** : `<th>` avec scope implicite, `<td>` pour data
- **Contraste textuel principal** : `--text #1a1a1a` sur `--bg #fdfdfb` ≈ ratio 17:1 (AAA)
- **Contraste accent** : `--accent #4a6741` sur `--bg #fdfdfb` ≈ ratio 5.6:1 (AA conforme normal text, AAA pour gros texte)
- **Contraste muted** : `--muted #5a5a5a` sur `--bg #fdfdfb` ≈ ratio 6.6:1 (AA conforme)
- **Print stylesheet** : `@media print` ([:219](site/src/layouts/MarkdownLayout.astro#L219)) — borders supprimées, pad ajusté

## 3. Points d'amélioration mineurs (à valider Claude Design)

### A — `prefers-reduced-motion` non explicité

Aucune `@media (prefers-reduced-motion: reduce)` n'est présente dans `MarkdownLayout.astro` ni `index.astro`. Pour l'instant le site n'a pas d'animations significatives donc l'impact est mineur. **Recommandation** : si Claude Design ajoute des animations (fade-in, scroll-spy, hover transitions), inclure systématiquement le bloc `@media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }`.

### B — Image SVG schéma : aria-label sur barres individuelles

Les `<g aria-label="Couche {n} — {nom} — âge {age} — {maturité}{article}">` ([CouchesSchema.astro:73](site/src/components/CouchesSchema.astro#L73)) sont en place pour chaque ligne. **Bon**. Reste à vérifier que les éléments visuels distincts (point/barre/article) ont chacun leur sémantique. Pour l'instant, le schéma est lisible par lecteur d'écran via le label parent.

### C — Densité d'information du `aside.contest-block`

L'aside « Contester cette page » est très dense ([:250-260](site/src/layouts/MarkdownLayout.astro#L250)). Pour utilisateurs cognition lente, considerer ajout d'une `summary`/`details` ou révéler progressivement. **Pas critique** — la structure HTML est déjà sémantique, c'est juste de la lisibilité optique.

## 4. Points non audités (hors périmètre interne)

- **Tests avec lecteurs d'écran réels** (NVDA, JAWS, VoiceOver) : à effectuer par contributeur·trice externe ou Claude Design.
- **Tests navigation clavier complète** : à effectuer en cliquant `Tab` répétée et vérifier que tous les éléments interactifs sont atteignables et visibles.
- **Tests appareils mobiles** : breakpoint `@media (max-width: 600px)` est en place ([:213](site/src/layouts/MarkdownLayout.astro#L213)) mais tests pratiques non effectués.
- **Tests utilisateurs en situation de handicap** : nécessitent collaboration externe, hors session autonome.

## 5. Recommandations pour Claude Design (UI Chrome) lors de l'intégration finale

Quand Claude Design intègre son design Anthropie au site Astro existant (cf. brief envoyé le 2026-05-04), conserver les acquis ci-dessus :

1. **Ne pas régresser** : `lang`, viewport, skip-link, focus-visible, sémantique HTML, hiérarchie titres, contraste textuel.
2. **Ajouter** : `prefers-reduced-motion` pour animations design v3 (rosace hero, scroll-spy, etc.).
3. **Vérifier** : contraste de la palette OKLCH 12 couches sur `--bg-vellum #fbf9f4` (palette Claude Design v3) — ratios à recalculer.
4. **Préserver** : structure `<nav>`, `<main>`, `<aside>`, `<footer>` sémantique en sortie HTML — pas seulement en CSS.
5. **Tester** : navigation clavier sur composants interactifs (rosace hover, topbar progress, scroll-spy).

---

## 6. Limites de cet audit

- **Auto-audit** par le commissariat originel. Pas un audit accessibilité professionnel (audit a11y certifié WCAG par cabinet expert recommandé pour version finale).
- **Périmètre** : layout principal `MarkdownLayout.astro` + composant principal `CouchesSchema.astro`. `index.astro` (homepage) parcouru rapidement seulement.
- **État au 2026-05-05** susceptible d'évoluer significativement quand Claude Design pousse son intégration.

---

*« Une accessibilité conforme aux normes est un minimum. L'accessibilité réelle commence quand des utilisateurs en situation de handicap testent et reportent. »*
