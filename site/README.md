# site/ — anthropie.org

Site statique Astro 6 de l'édifice **L'Anthropie**. Sobriété délibérée : pas de JS, pas de tracking, pas de framework lourd, pas de CTA marketing. Build statique → GitHub Pages → custom domain `anthropie.org`.

## Doctrine du site

- Une seule porte d'entrée (`index.astro`), une 404 (`404.astro`).
- Couleur d'accent unique : `#4a6741` (vert mousse).
- Typo serif système (`Iowan Old Style → Palatino Linotype → Palatino → Hoefler Text → Georgia`), aucune webfont.
- Anonymat strict : footer = *Anthropie Network*, jamais de signature personnelle.
- Anti-marketing : aucun pixel d'analytics, aucun popup, aucun bouton "Sign up".
- Données structurées JSON-LD `CreativeWork` CC0 pour découvrabilité académique.
- Print stylesheet pour les chercheurs qui impriment.

## Structure

```
site/
├── astro.config.mjs           Astro 6 + integration sitemap, site = anthropie.org
├── package.json               astro@^6.1.10, @astrojs/sitemap
├── public/
│   ├── CNAME                  anthropie.org (lu par GitHub Pages)
│   ├── favicon.svg / .ico
│   ├── og-image.svg           1200×630 sobre, CC0 mention visible
│   └── robots.txt             allow + sitemap
└── src/pages/
    ├── index.astro            page unique, 12 couches + 11 articles 31bis-duodecies
    └── 404.astro              "Cette page ne se trouve pas dans l'édifice."
```

## Commandes

```sh
npm install
npm run dev      # dev local sur http://localhost:4321
npm run build    # build statique → dist/
npm run preview  # preview du build
```

Node `>=22.12.0` requis (cf. `engines.node`).

## Déploiement

Workflow GitHub Actions (`.github/workflows/deploy.yml`) sur push de `site/**` ou du workflow lui-même : `npm ci && npm run build` → upload `site/dist/` → GitHub Pages → CNAME → `anthropie.org`.

SSL Let's Encrypt provisionné et auto-renouvelé par GitHub Pages.

## Doctrine éditoriale rappel

Avant tout changement visible, consulter [`README.md`](../README.md) racine et [`ROADMAP.md`](../ROADMAP.md). Le site est une **porte d'entrée**, pas une compression de l'édifice. Le contenu profond reste dans les 12 fichiers `anthropie_couche_*.md` à la racine.

## Issues / contributions

[github.com/SanTiepi/anthropie-edifice/issues](https://github.com/SanTiepi/anthropie-edifice/issues). Critique radicale bienvenue, surtout sur ce qui ne tient pas.
