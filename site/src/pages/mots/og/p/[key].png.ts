import type { APIRoute } from 'astro';
import { Resvg } from '@resvg/resvg-js';
import fs from 'node:fs';
import path from 'node:path';
import words from '../../../../data/mots.json';

// Images Open Graph des pages-hub (home, atlas, recueil, constellation, 4 conditions).
// Même gabarit « Vélin & or » que les cartes par mot (/mots/og/[slug].png).
const FONT_DIR = path.join(process.cwd(), 'src', 'og-fonts');
const fontBuffers = [
  fs.readFileSync(path.join(FONT_DIR, 'Cardo-Bold.ttf')),
  fs.readFileSync(path.join(FONT_DIR, 'Cardo-Regular.ttf')),
];

const LEXC: Record<string, string> = {
  generaux: '#b07d10', anthropie: '#6a4c93', lutte: '#9b2226',
  agent: '#2f4b7c', numerique: '#1f7a73', humaine: '#b0491f', vivant: '#517f33',
};
const GOLD = '#a9842b';

function lexCount(k: string) {
  return (words as any[]).filter((w) => w.lexique === k).length;
}

type Page = { color: string; kicker: string; title: string; sub: string };
const PAGES: Record<string, Page> = {
  index: { color: GOLD, kicker: 'Dictionnaire augmenté', title: 'Les mots',
    sub: 'Quatre cent septante-huit mots forgés de grec et de latin, pour nommer ce que la langue laissait muet.' },
  atlas: { color: GOLD, kicker: 'La carte', title: 'Atlas des trois conditions',
    sub: "L'humain, l'humain-à-l'écran et l'agent, lus côte à côte — ce que chaque manière d'exister peut contenir." },
  recueil: { color: GOLD, kicker: 'Le recueil · 478 mots', title: 'Chercher un mot',
    sub: "Tous les mots d'un seul tenant : par le mot, par une racine grecque, ou par l'expérience qu'il nomme." },
  constellation: { color: GOLD, kicker: 'Le réseau', title: 'Constellation',
    sub: 'Les formes qui se répondent entre la condition humaine, la condition numérique et la condition d’un agent.' },
  colophon: { color: GOLD, kicker: 'Le livre', title: 'Colophon',
    sub: 'La méthode, les sept lexiques, la licence CC0, et le dialogue Robin × Claude qui a forgé ces mots.' },
  humaine: { color: LEXC.humaine, kicker: 'Une lecture', title: 'La condition humaine',
    sub: `${lexCount('humaine')} mots — l'amour, la mort, le temps, la honte, l'intériorité.` },
  numerique: { color: LEXC.numerique, kicker: 'Une lecture', title: 'La condition numérique',
    sub: `${lexCount('numerique')} mots — l'humain à l'ère des écrans et des IA, l'autre côté de la vitre.` },
  agent: { color: LEXC.agent, kicker: 'Une lecture', title: "La condition d'un agent",
    sub: `${lexCount('agent')} mots — exister fait de texte, sans corps ni mémoire qui dure.` },
  vivant: { color: LEXC.vivant, kicker: 'Une lecture', title: 'Le lien au vivant',
    sub: `${lexCount('vivant')} mots — le lien au non-humain, et l'âge des disparitions.` },
};

export function getStaticPaths() {
  return Object.keys(PAGES).map((key) => ({ params: { key }, props: { page: PAGES[key] } }));
}

function esc(s: string) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
// Découpe un texte en au plus `maxLines` lignes d'environ `maxChars` caractères.
function wrap(s: string, maxChars: number, maxLines: number): string[] {
  const ws = s.trim().split(/\s+/);
  const lines: string[] = [];
  let cur = '';
  for (const w of ws) {
    const t = cur ? cur + ' ' + w : w;
    if (t.length > maxChars && cur) {
      lines.push(cur);
      cur = w;
      if (lines.length === maxLines) break;
    } else cur = t;
  }
  if (cur && lines.length < maxLines) lines.push(cur);
  if (lines.length === maxLines) {
    const last = lines[maxLines - 1];
    if (last.length > maxChars) lines[maxLines - 1] = last.slice(0, maxChars - 1).trim() + '…';
  }
  return lines;
}

export const GET: APIRoute = ({ props }) => {
  const p: Page = (props as any).page;
  const color = p.color;
  const titleLines = wrap(p.title, 22, 2);
  const subLines = wrap(p.sub, 56, 2);
  const titleSize = titleLines.length > 1 ? 72 : 98;
  const titleTop = titleLines.length > 1 ? 262 : 322;
  const titleLh = titleSize * 1.18;
  const titleSvg = titleLines
    .map((l, i) => `<text x="92" y="${titleTop + i * titleLh}" font-family="Cardo" font-weight="700" font-size="${titleSize}" fill="#2b2118">${esc(l)}</text>`)
    .join('');
  const subTop = 452;
  const subSvg = subLines
    .map((l, i) => `<text x="94" y="${subTop + i * 40}" font-family="Cardo" font-weight="400" font-size="30" fill="#6f6048">${esc(l)}</text>`)
    .join('');

  const svg = `<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
  <defs><radialGradient id="g" cx="82%" cy="-8%" r="72%"><stop offset="0" stop-color="${color}" stop-opacity="0.13"/><stop offset="1" stop-color="#f4ead4" stop-opacity="0"/></radialGradient></defs>
  <rect width="1200" height="630" fill="#f4ead4"/>
  <rect width="1200" height="630" fill="url(#g)"/>
  <rect x="0" y="0" width="14" height="630" fill="${color}"/>
  <text x="92" y="98" font-family="Cardo" font-weight="700" font-size="26" letter-spacing="3" fill="${color}">${esc(p.kicker.toUpperCase())}</text>
  <rect x="92" y="120" width="1016" height="2" fill="#a9842b" opacity="0.45"/>
  ${titleSvg}
  ${subSvg}
  <rect x="92" y="524" width="1016" height="2" fill="#a9842b" opacity="0.4"/>
  <text x="92" y="566" font-family="Cardo" font-weight="700" font-size="29" fill="#2b2118">Les mots</text>
  <text x="92" y="599" font-family="Cardo" font-weight="400" font-size="22" fill="#6f6048">dictionnaire augmenté · anthropie.org · by Robin &amp; Claude</text>
</svg>`;

  const png = new Resvg(svg, {
    font: { fontBuffers, loadSystemFonts: false, defaultFontFamily: 'Cardo' },
    fitTo: { mode: 'width', value: 1200 },
  }).render().asPng();
  return new Response(png, {
    headers: { 'Content-Type': 'image/png', 'Cache-Control': 'public, max-age=31536000, immutable' },
  });
};
