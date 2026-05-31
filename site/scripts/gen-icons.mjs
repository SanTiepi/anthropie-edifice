#!/usr/bin/env node
// Génère les icônes PWA de /mots (Vélin & or) : un « m » serif doré sur parchemin,
// cadre fin doré. Sortie : public/mots-icon-192.png et public/mots-icon-512.png.
// Reproductible : node scripts/gen-icons.mjs  (resvg + fonte Cardo déjà au repo).
import { Resvg } from '@resvg/resvg-js';
import fs from 'node:fs';
import path from 'node:path';

const FONT = fs.readFileSync(path.join(process.cwd(), 'src', 'og-fonts', 'Cardo-Bold.ttf'));
const OUT = path.join(process.cwd(), 'public');

function render(size) {
  const rx = Math.round(size * 0.18);
  const inset = Math.round(size * 0.10);
  const frameRx = Math.round(size * 0.11);
  const glyph = Math.round(size * 0.56);
  const svg = `<svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" xmlns="http://www.w3.org/2000/svg">
  <rect width="${size}" height="${size}" rx="${rx}" fill="#f4ead4"/>
  <rect x="${inset}" y="${inset}" width="${size - inset * 2}" height="${size - inset * 2}" rx="${frameRx}" fill="none" stroke="#a9842b" stroke-opacity="0.55" stroke-width="${Math.max(2, Math.round(size * 0.012))}"/>
  <text x="50%" y="${Math.round(size * 0.62)}" font-family="Cardo" font-weight="700" font-size="${glyph}" fill="#a9842b" text-anchor="middle">m</text>
</svg>`;
  const png = new Resvg(svg, {
    font: { fontBuffers: [FONT], loadSystemFonts: false, defaultFontFamily: 'Cardo' },
    fitTo: { mode: 'width', value: size },
  }).render().asPng();
  const file = path.join(OUT, `mots-icon-${size}.png`);
  fs.writeFileSync(file, png);
  console.log(`wrote ${file} (${png.length} bytes)`);
}

render(192);
render(512);
