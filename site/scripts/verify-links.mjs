#!/usr/bin/env node
// site/scripts/verify-links.mjs
//
// CI lien-check pour le site anthropie.org. Résout G-008 partiellement (partie CI ;
// partie RAG local différée). Conforme à ADR-0014 (modification d'un fichier existant
// + ajout d'un script utilitaire ; pas un nouveau dispositif doctrinal).
//
// Parcourt tous les .html générés dans site/dist/ après build, extrait les liens
// internes (href commençant par / ou #), vérifie que chaque cible existe.
// Exit code 1 si liens cassés trouvés — fait échouer le build CI.
//
// Usage : node scripts/verify-links.mjs
//         (à appeler après `astro build`)

import { readdir, readFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const DIST_DIR = resolve(__dirname, '..', 'dist');
const BASE = '/anthropie-edifice'; // base path GitHub Pages
const ROOT_DOMAIN = 'anthropie.org';

// Liens externes ignorés (validés autrement, pas en CI lien-check)
const EXTERNAL_PROTOCOLS = ['http:', 'https:', 'mailto:', 'tel:', 'data:'];

// Énumère récursivement tous les .html dans un dossier.
async function walkHtml(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const e of entries) {
    const full = join(dir, e.name);
    if (e.isDirectory()) {
      files.push(...(await walkHtml(full)));
    } else if (e.isFile() && e.name.endsWith('.html')) {
      files.push(full);
    }
  }
  return files;
}

// Extrait href="..." et src="..." (limité aux <a>, <link>, <img>).
function extractLinks(html) {
  const links = [];
  // <a href="..."> et <link href="...">
  const hrefRegex = /<(?:a|link)\b[^>]*?\bhref=("([^"]*)"|'([^']*)')/gi;
  let m;
  while ((m = hrefRegex.exec(html)) !== null) {
    links.push(m[2] ?? m[3]);
  }
  // <img src="...">, <script src="...">
  const srcRegex = /<(?:img|script)\b[^>]*?\bsrc=("([^"]*)"|'([^']*)')/gi;
  while ((m = srcRegex.exec(html)) !== null) {
    links.push(m[2] ?? m[3]);
  }
  return links;
}

function isExternal(link) {
  return EXTERNAL_PROTOCOLS.some((p) => link.startsWith(p)) ||
         link.startsWith('//');
}

function stripFragment(link) {
  const i = link.indexOf('#');
  return i === -1 ? link : link.slice(0, i);
}

function stripQuery(link) {
  const i = link.indexOf('?');
  return i === -1 ? link : link.slice(0, i);
}

// Pour un lien absolu /xxx, retourne le chemin disque attendu dans dist/.
function resolveLink(link) {
  let path = stripQuery(stripFragment(link));
  if (!path) return null; // fragment-only ou query-only — pas une cible fichier
  // Normalisation base path GitHub Pages : /anthropie-edifice/foo -> /foo
  if (path.startsWith(BASE + '/')) path = path.slice(BASE.length);
  if (path === BASE) path = '/';
  // Astro génère /lire/slug/ -> dist/lire/slug/index.html
  let candidate = join(DIST_DIR, path);
  if (path.endsWith('/')) candidate = join(candidate, 'index.html');
  return candidate;
}

async function main() {
  if (!existsSync(DIST_DIR)) {
    console.error(`[verify-links] ERROR: ${DIST_DIR} n'existe pas. Lance 'npm run build' d'abord.`);
    process.exit(2);
  }

  const htmlFiles = await walkHtml(DIST_DIR);
  console.log(`[verify-links] Scan ${htmlFiles.length} fichiers HTML dans ${DIST_DIR}`);

  const broken = []; // [{ source, link, resolved }]
  let totalLinks = 0;
  let totalInternal = 0;

  for (const file of htmlFiles) {
    const html = await readFile(file, 'utf8');
    const links = extractLinks(html);
    totalLinks += links.length;

    for (const link of links) {
      if (isExternal(link)) continue;
      // Ignorer les liens qui ne sont que des fragments (#section) ou queries
      if (link.startsWith('#') || link.startsWith('?')) continue;
      // Ignorer les data URIs (déjà filtrés par isExternal mais double-check)
      if (link.startsWith('data:')) continue;

      // Liens relatifs (sans / initial) : on ne les vérifie pas pour rester simple
      // (le site Astro produit des liens absolus ${base}/lire/...)
      if (!link.startsWith('/')) continue;

      totalInternal++;
      const resolved = resolveLink(link);
      if (!resolved) continue;
      if (!existsSync(resolved)) {
        broken.push({
          source: file.replace(DIST_DIR, '').replace(/\\/g, '/'),
          link,
          resolved: resolved.replace(DIST_DIR, '').replace(/\\/g, '/'),
        });
      }
    }
  }

  console.log(`[verify-links] ${totalLinks} liens totaux, ${totalInternal} internes vérifiés`);

  if (broken.length === 0) {
    console.log(`[verify-links] OK — 0 lien interne cassé.`);
    process.exit(0);
  }

  console.error(`[verify-links] FAIL — ${broken.length} liens cassés détectés :`);
  // Regroupement par source pour lisibilité
  const bySource = new Map();
  for (const b of broken) {
    if (!bySource.has(b.source)) bySource.set(b.source, []);
    bySource.get(b.source).push(b);
  }
  for (const [source, items] of bySource) {
    console.error(`  ${source}`);
    for (const b of items) {
      console.error(`    ↳ ${b.link} → cible inexistante (${b.resolved})`);
    }
  }
  process.exit(1);
}

main().catch((err) => {
  console.error('[verify-links] Erreur inattendue :', err);
  process.exit(2);
});
