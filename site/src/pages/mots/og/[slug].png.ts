import type { APIRoute } from 'astro';
import { Resvg } from '@resvg/resvg-js';
import fs from 'node:fs';
import path from 'node:path';
import words from '../../../data/mots.json';

const FONT_DIR = path.join(process.cwd(), 'src', 'og-fonts');
const fontBuffers = [
  fs.readFileSync(path.join(FONT_DIR, 'Cardo-Bold.ttf')),
  fs.readFileSync(path.join(FONT_DIR, 'Cardo-Regular.ttf')),
];

const LEXC: Record<string, string> = {
  generaux: '#b07d10', anthropie: '#6a4c93', lutte: '#9b2226',
  agent: '#2f4b7c', numerique: '#1f7a73', humaine: '#b0491f', vivant: '#517f33',
};
const LEXL: Record<string, string> = {
  humaine: 'La condition humaine', numerique: 'La condition numérique', agent: "La condition d'un agent",
  vivant: 'Le lien au vivant', anthropie: "L'Anthropie", lutte: 'La lutte', generaux: 'Mots nécessaires',
};

export function getStaticPaths() {
  const seen = new Set<string>();
  const out: any[] = [];
  for (const w of words as any[]) {
    if (!seen.has(w.slug)) { seen.add(w.slug); out.push({ params: { slug: w.slug }, props: { w } }); }
  }
  return out;
}

function esc(s: string) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
function trunc(s: string, n: number) { s = s.trim(); return s.length > n ? s.slice(0, n - 1).trim() + '…' : s; }
function lemmaSize(len: number) { return len <= 9 ? 124 : len <= 13 ? 100 : len <= 17 ? 80 : 64; }

export const GET: APIRoute = ({ props }) => {
  const w: any = (props as any).w;
  const color = LEXC[w.lexique] || '#a9842b';
  const ls = lemmaSize(w.mot.length);
  const etym = trunc(w.etym, 64);
  const lexlabel = (LEXL[w.lexique] || w.lexique).toUpperCase();
  const svg = `<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
  <defs><radialGradient id="g" cx="82%" cy="-8%" r="72%"><stop offset="0" stop-color="${color}" stop-opacity="0.12"/><stop offset="1" stop-color="#f4ead4" stop-opacity="0"/></radialGradient></defs>
  <rect width="1200" height="630" fill="#f4ead4"/>
  <rect width="1200" height="630" fill="url(#g)"/>
  <rect x="0" y="0" width="14" height="630" fill="${color}"/>
  <text x="92" y="96" font-family="Cardo" font-weight="700" font-size="26" letter-spacing="3" fill="${color}">${esc(lexlabel)}</text>
  <rect x="92" y="118" width="1016" height="2" fill="#a9842b" opacity="0.45"/>
  <text x="92" y="332" font-family="Cardo" font-weight="700" font-size="${ls}" fill="#2b2118">${esc(w.mot)}</text>
  <text x="94" y="398" font-family="Cardo" font-weight="400" font-size="32" fill="#6f6048">${esc(etym)}</text>
  <rect x="92" y="506" width="1016" height="2" fill="#a9842b" opacity="0.4"/>
  <text x="92" y="558" font-family="Cardo" font-weight="700" font-size="30" fill="#2b2118">Les mots</text>
  <text x="92" y="592" font-family="Cardo" font-weight="400" font-size="23" fill="#6f6048">anthropie.org/mots · mot forgé · racines grecques/latines · CC0</text>
</svg>`;
  const png = new Resvg(svg, {
    font: { fontBuffers, loadSystemFonts: false, defaultFontFamily: 'Cardo' },
    fitTo: { mode: 'width', value: 1200 },
  }).render().asPng();
  return new Response(png, {
    headers: { 'Content-Type': 'image/png', 'Cache-Control': 'public, max-age=31536000, immutable' },
  });
};
