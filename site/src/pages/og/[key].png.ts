import type { APIRoute } from 'astro';
import { Resvg } from '@resvg/resvg-js';
import path from 'node:path';

// Images Open Graph de l'édifice (accueil + chaque page /lire/).
// Les plateformes sociales (WhatsApp, LinkedIn, X, Slack…) ignorent les og:image
// en SVG : ces PNG 1200×630 rendent chaque page partageable avec un aperçu.
// Gabarit sobre conforme à la doctrine du site : fond papier, barre vert mousse,
// serif Cardo, aucune signature personnelle.
const FONT_DIR = path.join(process.cwd(), 'src', 'og-fonts');
// `fontFiles` et non `fontBuffers` : dans resvg-js 2.6.2, fontBuffers est ignoré
// et le rendu retombe sur un sans-serif de secours au lieu de Cardo.
const fontFiles = [
  path.join(FONT_DIR, 'Cardo-Bold.ttf'),
  path.join(FONT_DIR, 'Cardo-Regular.ttf'),
];

const ACCENT = '#4a6741';
const TEXT = '#1a1a1a';
const MUTED = '#5a5a5a';
const BG = '#fdfdfb';
const BORDER = '#e2dfd6';

type Card = { kicker: string; title: string; sub: string };

export function getStaticPaths() {
  const cards: Record<string, Card> = {
    home: {
      kicker: 'Domaine public · CC0 1.0',
      title: "L'Anthropie",
      sub: "Édifice civilisationnel d'apprentissage humain à 12 couches — de 0 à l'infini.",
    },
  };
  // Mêmes sources que /lire/[slug].astro : le contenu dérivé par prepare-content.mjs.
  const files = import.meta.glob('../../content-md/*.md', { eager: true }) as Record<string, any>;
  for (const [p, mod] of Object.entries(files)) {
    const slug = p.split('/').pop()!.replace('.md', '');
    const fm = mod.frontmatter ?? {};
    const min = fm.readingMinutes;
    const lecture = min ? (min === 1 ? 'lecture ~1 min' : `lecture ~${min} min`) : '';
    cards[slug] = {
      kicker: "L'Anthropie · édifice CC0",
      title: String(fm.title ?? slug),
      sub: ['Édifice d’apprentissage humain · domaine public', lecture].filter(Boolean).join(' · '),
    };
  }
  return Object.entries(cards).map(([key, card]) => ({ params: { key }, props: { card } }));
}

function esc(s: string) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// Découpe un texte en au plus `maxLines` lignes d'environ `maxChars` caractères.
// Si le texte déborde, la dernière ligne se termine par une ellipse.
function wrap(s: string, maxChars: number, maxLines: number): string[] {
  const ws = s.trim().split(/\s+/);
  const lines: string[] = [];
  let cur = '';
  let overflow = false;
  for (const w of ws) {
    const t = cur ? cur + ' ' + w : w;
    if (t.length > maxChars && cur) {
      if (lines.length === maxLines - 1) {
        overflow = true;
        break;
      }
      lines.push(cur);
      cur = w;
    } else cur = t;
  }
  if (cur && lines.length < maxLines) lines.push(cur);
  if (overflow || (lines.length === maxLines && lines[maxLines - 1].length > maxChars)) {
    const last = lines[maxLines - 1];
    lines[maxLines - 1] = (last.length > maxChars ? last.slice(0, maxChars - 1) : last).replace(/[ ,;:./+(—-]+$/, '') + '…';
  }
  return lines;
}

export const GET: APIRoute = ({ props }) => {
  const c: Card = (props as any).card;
  const titleLines = wrap(c.title, 30, 3);
  const titleSize = titleLines.length > 2 ? 54 : titleLines.length > 1 ? 64 : 84;
  const titleLh = titleSize * 1.22;
  const titleTop = titleLines.length > 2 ? 240 : titleLines.length > 1 ? 268 : 318;
  const titleSvg = titleLines
    .map((l, i) => `<text x="92" y="${titleTop + i * titleLh}" font-family="Cardo" font-weight="700" font-size="${titleSize}" fill="${TEXT}">${esc(l)}</text>`)
    .join('');
  const subLines = wrap(c.sub, 72, 2);
  const subTop = titleTop + titleLines.length * titleLh + 18;
  const subSvg = subLines
    .map((l, i) => `<text x="94" y="${subTop + i * 38}" font-family="Cardo" font-weight="400" font-size="27" fill="${MUTED}">${esc(l)}</text>`)
    .join('');

  const svg = `<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
  <rect width="1200" height="630" fill="${BG}"/>
  <rect x="0" y="0" width="14" height="630" fill="${ACCENT}"/>
  <text x="92" y="98" font-family="Cardo" font-weight="700" font-size="25" letter-spacing="3" fill="${ACCENT}">${esc(c.kicker.toUpperCase())}</text>
  <rect x="92" y="120" width="1016" height="2" fill="${BORDER}"/>
  ${titleSvg}
  ${subSvg}
  <rect x="92" y="524" width="1016" height="2" fill="${BORDER}"/>
  <text x="92" y="566" font-family="Cardo" font-weight="700" font-size="29" fill="${TEXT}">anthropie.org</text>
  <text x="92" y="599" font-family="Cardo" font-weight="400" font-size="22" fill="${MUTED}">Anthropie Network · CC0 1.0 Universal · sans auteur · cherche porteurs</text>
</svg>`;

  const png = new Resvg(svg, {
    font: { fontFiles, loadSystemFonts: false, defaultFontFamily: 'Cardo' },
    fitTo: { mode: 'width', value: 1200 },
  }).render().asPng();
  return new Response(png, {
    headers: { 'Content-Type': 'image/png', 'Cache-Control': 'public, max-age=31536000, immutable' },
  });
};
