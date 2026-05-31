import type { APIRoute } from 'astro';
import words from '../../data/mots.json';

// Flux RSS 2.0 du recueil — écrit à la main (l'écosystème /mots reste zéro-dépendance).
// C'est la représentation « alternate » du dictionnaire : le corpus, abonnable.
const SITE = 'https://anthropie.org';

function xml(s: string) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
function plain(s: string) {
  return String(s).replace(/[`*_]/g, '');
}
function cdata(s: string) {
  return `<![CDATA[${String(s).replace(/\]\]>/g, ']]&gt;')}]]>`;
}

export const GET: APIRoute = () => {
  const seen = new Set<string>();
  const uniq: any[] = [];
  for (const w of words as any[]) if (!seen.has(w.slug)) { seen.add(w.slug); uniq.push(w); }
  uniq.sort((a, b) => a.mot.localeCompare(b.mot, 'fr'));

  const items = uniq.map((w) => {
    const url = `${SITE}/mots/m/${w.slug}/`;
    const desc = plain(`${w.etym} — ${w.corps}`);
    return `    <item>
      <title>${xml(w.mot)}</title>
      <link>${url}</link>
      <guid isPermaLink="true">${url}</guid>
      <category>${xml(w.lexique_label)}</category>
      <description>${cdata(desc)}</description>
    </item>`;
  }).join('\n');

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Les mots — dictionnaire augmenté</title>
    <link>${SITE}/mots/</link>
    <atom:link href="${SITE}/mots/feed.xml" rel="self" type="application/rss+xml"/>
    <description>${xml(`${(words as any[]).length} néologismes gréco-latins forgés de grec et de latin, en sept lexiques. by Robin & Claude. Domaine public CC0.`)}</description>
    <language>fr</language>
${items}
  </channel>
</rss>
`;
  return new Response(body, {
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8', 'Cache-Control': 'public, max-age=3600' },
  });
};
