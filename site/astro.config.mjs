// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
// Hosting actuel : GitHub Pages → https://santiepi.github.io/anthropie-edifice/
// À migrer vers https://anthropie.org quand le domaine sera actif (changer site, vider base).
export default defineConfig({
	integrations: [],
	site: 'https://santiepi.github.io',
	base: '/anthropie-edifice',
});
