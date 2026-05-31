// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
// Hosting : GitHub Pages avec custom domain → https://anthropie.org
// Le fichier site/public/CNAME contient le domaine et est copié dans dist/ par Astro,
// puis détecté par GitHub Pages au déploiement.
export default defineConfig({
	site: 'https://anthropie.org',
	integrations: [
		sitemap({
			// Les endpoints non-HTML (images OG, flux RSS) ne sont pas des pages à indexer.
			filter: (page) => !page.includes('/mots/og/') && !page.endsWith('/feed.xml'),
		}),
	],
});
