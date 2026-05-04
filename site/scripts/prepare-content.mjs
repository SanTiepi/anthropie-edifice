#!/usr/bin/env node
/**
 * Prebuild step for anthropie.org.
 *
 * Copies a curated subset of root-level .md files into `site/src/content-md/`,
 * adds minimal frontmatter (slug + title + sourceFile), and rewrites internal
 * .md→.md cross-links to the corresponding /lire/<slug>/ URLs.
 *
 * Astro then renders each file as a static page via `site/src/pages/lire/[slug].astro`.
 * The directory `site/src/content-md/` is gitignored — it is fully derived from root.
 *
 * Run via `npm run prebuild` (auto-invoked before `npm run build`).
 */

import { existsSync } from 'node:fs';
import { mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..', '..');
const DEST = join(__dirname, '..', 'src', 'content-md');

// [sourceFile, slug, displayTitle]
const FILES = [
  // 12 couches
  ['anthropie_couche_01_matrice.md',     'couche-01-matrice',     'Couche 1 — LA MATRICE (0-3)'],
  ['anthropie_couche_02_sanctuaire.md',  'couche-02-sanctuaire',  'Couche 2 — LE SANCTUAIRE (3-7)'],
  ['anthropie_couche_03_atelier.md',     'couche-03-atelier',     "Couche 3 — L'ATELIER (5-12)"],
  ['anthropie_couche_04_parole.md',      'couche-04-parole',      'Couche 4 — LA PAROLE (7-15)'],
  ['anthropie_couche_05_ville.md',       'couche-05-ville',       'Couche 5 — LA VILLE (10-18)'],
  ['anthropie_couche_06_regard.md',      'couche-06-regard',      'Couche 6 — LE REGARD (10-18)'],
  ['anthropie_couche_07_seuils.md',      'couche-07-seuils',      'Couche 7 — LES SEUILS (12-22)'],
  ['anthropie_couche_08_mycologie.md',   'couche-08-mycologie',   'Couche 8 — LA MYCOLOGIE (15-25)'],
  ['anthropie_couche_09_archive.md',     'couche-09-archive',     "Couche 9 — L'ARCHIVE VIVANTE (0-∞)"],
  ['anthropie_couche_10_morts.md',       'couche-10-morts',       'Couche 10 — LE CONSEIL DES MORTS (4-∞)'],
  ['anthropie_couche_11_parente.md',     'couche-11-parente',     'Couche 11 — LA PARENTÉ ÉLARGIE (3-25)'],
  ['anthropie_couche_12_brisure.md',     'couche-12-brisure',     'Couche 12 — LE SEUIL DE LA BRISURE (9-∞)'],
  // Documents structurants
  ['WELCOME.md',                 'accueil',     "Pacte d'accueil (90 secondes)"],
  ['anthropie_brief_3pages.md',  'brief',       "Brief (3 minutes)"],
  ['ANTHROPIE_KERNEL.md',        'noyau',       "Noyau — l'édifice en 10 minutes"],
  ['SAFETY.md',                  'garde-fous',  "Garde-fous éthiques (SAFETY)"],
  ['PROTOTYPES.md',              'prototyper',  "Prototyper localement"],
  ['GLOSSARY.md',                'glossaire',   "Glossaire minimal"],
  ['REFUTATION.md',              'refutation',  "Critères de réfutation"],
  ['DECISIONS.md',               'decisions',   "Décisions doctrinales (mini-ADR)"],
  ['FORKING.md',                 'forker',      "Reprendre l'édifice (fork CC0)"],
  ['ADEQUATION.md',              'adequation',  "Test d'adéquation (90 secondes)"],
  ['LEGAL_BOUNDARIES.md',        'cadre',       "Cadre de publication (limites juridiques)"],
  ['OBJECTIONS.md',              'objections',  "Objections fréquentes (11 attaques + réponses)"],
  ['MANDATES.md',                'mandats',     "Mandats fonctionnels (rôles sans personnes)"],
  ['EVIDENCE_MAP.md',            'preuves',     "Carte des preuves (statut épistémique)"],
  ['CHOKE_POINTS.md',            'etouffement', "Carte des points d'étouffement (résilience)"],
  ['ENTRY_SCENARIOS.md',         'scenarios',   "Trois scénarios d'entrée concrets"],
  ['REPRODUCE.md',               'reproduire',  "Reconstruire et mode dégradé"],
  ['OPEN_GRIEVANCES.md',         'griefs',      "Griefs ouverts (critiques externes non closes)"],
  ['INSTITUTIONAL_TRANSLATION.md', 'traduction',  "Traduction institutionnelle"],
  ['HOSTILE_DRILL.md',           'audit-adverse', "Exercice prise hostile + audit adverse gelé"],
  ['NEGATIVE_BIBLIO.md',         'biblio-negative', "Bibliographie négative (sources refusées)"],
  ['TRANSMISSION.md',            'transmission', "Statut de transmission (transmissible / pas)"],
  ['NOT_AN_AI_LAB.md',           'pas-un-labo-ia', "Ce que ce projet n'est PAS (anti-confusion)"],
  ['NAMING.md',                  'nommage',     "Nommage canonique et clauses de non-affiliation"],
  ['LICENSES.md',                'licences',    "Matrice de licences par artefact"],
  ['EVAL_PROTOCOL.md',           'evaluation',  "Protocole d'évaluation empirique (90j / 6-12-24m)"],
  ['KIT_CERCLE_45.md',           'kit-cercle-45', "Kit Cercle 45 minutes (animation A4 recto-verso)"],
  ['PAV_TOOLKIT.md',             'pav-toolkit', "Toolkit PAV (sabliers + cartes + relève binôme)"],
  ['RPU_TOOLKIT.md',             'rpu-toolkit', "Toolkit RPU Couche 1 (intergénérationnel 70+ / 0-3)"],
  ['SCHOOL_RETREAT.md',          'retrait-ecole', "Retrait d'école 30 jours (atelier témoin + voisinage)"],
  ['PASSEPORT_12_LIEUX.md',      'passeport-12-lieux', "Passeport 12 lieux Couche 5 (apprentissage urbain solo)"],
  ['SEUIL_72H.md',               'seuil-72h', "Seuil 72H Couche 7 (liminalité protégée solo)"],
  ['BOITE_DES_ABSENTS.md',       'boite-des-absents', "Boîte des Absents Couches 9-10 (archive + audiences)"],
  ['CARNET_3_PARENTS.md',        'carnet-3-parents', "Carnet 3 Parents Non-Humains Couche 11 (12 saisons sur 3 ans)"],
  ['KINTSUGI_PAPIER.md',         'kintsugi-papier', "Kintsugi de papier Couche 12 (brisure visible)"],
  ['VEILLEE_DES_PAPIERS_REPARES.md', 'veillee-papiers-repares', "Veillée des Papiers Réparés (groupe 10-30, 4 jours)"],
  ['RELAIS_DES_72_ABSENTS.md',   'relais-72-absents', "Relais des 72 Absents (chaîne anonyme 12 jours, 4 toolkits orchestrés)"],
  ['HORLOGE_DES_12_SEUILS.md',   'horloge-12-seuils', "Horloge des 12 Seuils (audit personnel 12 minutes)"],
  ['SAS_DES_3_RESTES.md',        'sas-3-restes', "Sas des 3 Restes (dispositif 7 minutes collectif)"],
  ['TOOLKIT_MATRIX.md',          'matrice-dispositifs', "Matrice des dispositifs (par situation)"],
  ['MODE_DEGRADE_72H.md',        'mode-degrade-72h', "Mode Dégradé 72H (carte A6 porteur fatigué)"],
  ['MEDIA_DEFENSE.md',           'defense-mediatique', "Défense face aux interlocuteurs hostiles ou pressés"],
  ['CELLULE_M0.md',              'cellule-m0', "Cellule Mycéliale Mois Zéro (binôme + 3 lieux + 1 relais)"],
  ['CLOTURE_TOOLKIT.md',         'cloture', "Toolkit de Clôture (3 rituels de fin : prototype / mandat / cellule)"],
  ['PONT_DE_POLLEN.md',          'pont-de-pollen', "Pont de Pollen (connexion entre 2 cellules sans fusion)"],
  ['CLASS_TOOLKIT.md',           'toolkit-classe', "Toolkit Classe (3 dispositifs en milieu scolaire)"],
  ['WORK_TOOLKIT.md',            'toolkit-travail', "Toolkit Travail (2 dispositifs en entreprise)"],
  ['SOIN_TOOLKIT.md',            'toolkit-soin', "Toolkit Soin (3 dispositifs hôpital / EHPAD / palliatif)"],
  ['DETENTION_TOOLKIT.md',       'toolkit-detention', "Toolkit Détention (2 dispositifs en milieu fermé)"],
  ['RURAL_TOOLKIT.md',           'toolkit-rural', "Toolkit Rural / Isolé (3 dispositifs bas-tech)"],
  ['HUMANITARIAN_TOOLKIT.md',    'toolkit-humanitaire', "Toolkit Humanitaire (2 dispositifs zone précaire)"],
  ['MAINTENANCE.md',             'maintenance', "Maintenance de l'édifice (registre / élagage / archive)"],
  ['AUTO_CRITIQUE.md',           'auto-critique', "Auto-critique anticipative (accusations futures + erreurs prévisibles)"],
  ['REGISTRY.md',                'registre', "Registre des dispositifs (29 fiches : promesse / preuve / garde-fous)"],
  ['APERCU_12_COUCHES.md',       'apercu-12-couches', "Aperçu des 12 couches (lecture intermédiaire 15 min)"],
  ['AUDIT_COUCHE_04_PAROLE.md',  'audit-couche-04-parole', "Audit Couche IV LA PAROLE (promesse / preuve / provenance, audit pilote)"],
  ['AUDIT_COUCHE_11_PARENTE.md', 'audit-couche-11-parente', "Audit Couche XI LA PARENTÉ ÉLARGIE (promesse / preuve / provenance + diagnostic métabolique)"],
  ['AUDIT_COUCHE_12_BRISURE.md', 'audit-couche-12-brisure', "Audit Couche XII LE SEUIL DE LA BRISURE (ferme-t-elle l'arc d'Anthropie ?)"],
  ['AUDIT_COUCHE_02_SANCTUAIRE.md', 'audit-couche-02-sanctuaire', "Audit Couche II LE SANCTUAIRE (examen de la sensibilité 🟡)"],
  ['AUDIT_COUCHE_01_MATRICE.md',   'audit-couche-01-matrice', "Audit Couche I LA MATRICE (examen de la robustesse 🟢, RPU comme 6e invention propre)"],
  ['AUDIT_COUCHE_03_ATELIER.md',   'audit-couche-03-atelier', "Audit Couche III L'ATELIER (Pont des Certifications comme 7e invention propre potentielle)"],
  ['AUDIT_COUCHE_05_VILLE.md',     'audit-couche-05-ville', "Audit Couche V LA VILLE (sensibilité 🟡 justifiée, Pont étendu universitaire)"],
  ['AUDIT_COUCHE_06_REGARD.md',    'audit-couche-06-regard', "Audit Couche VI LE REGARD (sensibilité géopolitique, ouverture G-010 risque Diaspora Visuelle)"],
  ['ROADMAP.md',                 'roadmap',     "Roadmap — 4 phases"],
  ['CONTRIBUTING.md',            'contribuer',  "Contribuer à l'édifice"],
];

// Source filename → /lire/<slug>/ — built from FILES above
const linkMap = new Map(FILES.map(([src, slug]) => [src, `/lire/${slug}/`]));

// Maturité épistémique par couche (synchrone avec site/src/data/couches.ts)
// `robuste` = convergence empirique ou précédent juridique fort
// `sensible` = arbitrages culturels / juridiques / opérationnels en cours
const MATURITE_PAR_COUCHE = {
  'couche-01-matrice':     'robuste',
  'couche-02-sanctuaire':  'sensible',
  'couche-03-atelier':     'robuste',
  'couche-04-parole':      'robuste',
  'couche-05-ville':       'sensible',
  'couche-06-regard':      'sensible',
  'couche-07-seuils':      'robuste',
  'couche-08-mycologie':   'sensible',
  'couche-09-archive':     'robuste',
  'couche-10-morts':       'sensible',
  'couche-11-parente':     'robuste',
  'couche-12-brisure':     'sensible',
};

const MATURITE_DESC = {
  robuste:  '🟢 **Maturité épistémique : robuste** — convergence empirique forte ou précédent juridique en vigueur. Voir [carte des preuves](/lire/preuves/) pour le détail des claims classés.',
  sensible: '🟡 **Maturité épistémique : sensible** — arbitrages culturels, juridiques ou opérationnels en cours. Voir [carte des preuves](/lire/preuves/) pour les claims qui restent à étayer empiriquement.',
};

/**
 * Injecte une callout *Maturité épistémique* juste après le premier `# Titre` du fichier,
 * uniquement pour les fichiers de couche.
 * Pour les autres fichiers, retourne le contenu inchangé.
 */
function injectMaturiteBadge(slug, content) {
  const maturite = MATURITE_PAR_COUCHE[slug];
  if (!maturite) return content;
  const desc = MATURITE_DESC[maturite];
  if (!desc) return content;
  // Trouver la première ligne `# ...` et injecter après
  const lines = content.split(/\r?\n/);
  for (let i = 0; i < lines.length; i++) {
    if (/^#\s+\S/.test(lines[i])) {
      // Insérer la callout après la ligne de titre + une ligne vide éventuelle
      const insertAt = (i + 1 < lines.length && lines[i + 1].trim() === '') ? i + 2 : i + 1;
      lines.splice(insertAt, 0, '', desc, '');
      return lines.join('\n');
    }
  }
  // Pas de H1 trouvé : préfixer la callout
  return desc + '\n\n' + content;
}

/**
 * Rewrite internal markdown links.
 *
 * Handles:
 *  - `[label](anthropie_couche_04_parole.md)`         → `[label](/lire/couche-04-parole/)`
 *  - `[label](SAFETY.md#section-anchor)`              → `[label](/lire/garde-fous/#section-anchor)`
 *  - `[label](./SAFETY.md)` and `[label](../SAFETY.md)` (paranoid)
 *
 * Files whose name is NOT in linkMap are left untouched (e.g. LICENSE.md, CITATION.cff).
 */
function rewriteLinks(content) {
  return content.replace(
    /\(((?:\.{0,2}\/)?)([A-Za-z0-9_\-]+\.md)(#[^)]*)?\)/g,
    (match, prefix, file, anchor) => {
      const target = linkMap.get(file);
      if (!target) return match;
      return `(${target}${anchor || ''})`;
    }
  );
}

function makeFrontmatter({ slug, title, sourceFile, readingMinutes, density }) {
  const escape = (s) => String(s).replace(/"/g, '\\"');
  return `---\nslug: "${escape(slug)}"\ntitle: "${escape(title)}"\nsourceFile: "${escape(sourceFile)}"\nreadingMinutes: ${readingMinutes}\ndensity: "${density}"\n---\n\n`;
}

/**
 * Estime le temps de lecture en minutes à partir du contenu Markdown.
 * Vitesse cible : 220 mots/minute (lecture attentive plutôt que survol).
 * Strip les tokens Markdown (headers, listes, liens, code) avant de compter.
 */
function estimateReadingMinutes(content) {
  const stripped = content
    .replace(/```[\s\S]*?```/g, ' ')          // blocs de code
    .replace(/`[^`]+`/g, ' ')                 // code inline
    .replace(/!\[[^\]]*\]\([^)]+\)/g, ' ')    // images
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')  // liens (garder le label)
    .replace(/^[#>*\-_=+|]+\s*/gm, '')        // markers de bloc en début de ligne
    .replace(/[*_~`]/g, '')                   // marqueurs inline
    .replace(/\s+/g, ' ');
  const wordCount = stripped.trim().split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.round(wordCount / 220));
}

function classifyDensity(minutes) {
  if (minutes < 3) return 'court';
  if (minutes <= 10) return 'moyen';
  return 'dense';
}

async function main() {
  if (existsSync(DEST)) {
    await rm(DEST, { recursive: true, force: true });
  }
  await mkdir(DEST, { recursive: true });

  let copied = 0;
  let skipped = 0;
  for (const [src, slug, title] of FILES) {
    const srcPath = join(ROOT, src);
    if (!existsSync(srcPath)) {
      console.warn(`[prepare-content] missing: ${src} (skipped)`);
      skipped++;
      continue;
    }
    const raw = await readFile(srcPath, 'utf8');
    const rewritten = rewriteLinks(raw);
    const withBadge = injectMaturiteBadge(slug, rewritten);
    const readingMinutes = estimateReadingMinutes(withBadge);
    const density = classifyDensity(readingMinutes);
    const out = makeFrontmatter({ slug, title, sourceFile: src, readingMinutes, density }) + withBadge;
    await writeFile(join(DEST, `${slug}.md`), out, 'utf8');
    copied++;
  }
  console.log(`[prepare-content] ${copied}/${FILES.length} files prepared in src/content-md/${skipped ? ` (${skipped} missing)` : ''}`);
}

main().catch((err) => {
  console.error('[prepare-content] error:', err);
  process.exit(1);
});
