// Données canoniques des 12 couches de L'Anthropie + 11 articles 31bis-duodecies.
// Source de vérité partagée entre index.astro et toute page future (/couches, /[slug]…).
// Synchroniser avec ANTHROPIE_KERNEL.md à la racine du repo.

export type Maturite = "robuste" | "sensible";

export interface Couche {
  /** Numéro 1..12 */
  n: number;
  /** Nom canonique en majuscules */
  nom: string;
  /** Tranche d'âge couverte */
  age: string;
  /** Cœur de la couche, 1 ligne */
  coeur: string;
  /** Fichier markdown source à la racine du repo */
  file: string;
  /** Slug pour la route interne `/lire/<slug>/` — doit correspondre à l'entrée dans `site/scripts/prepare-content.mjs` */
  slug: string;
  /** Fichier présent dans le repo (si false, lien désactivé) */
  hasFile: boolean;
  /** Maturité épistémique : robuste = convergence empirique ou précédent juridique fort ; sensible = arbitrages culturels/juridiques/opérationnels en cours */
  maturite: Maturite;
  /** Article CRC associé, si applicable */
  article?: string;
}

export interface Article {
  /** Code de l'article (31bis, 31ter, …) */
  code: string;
  /** Titre du droit ouvert */
  titre: string;
  /** Numéro de la couche source */
  coucheSource: number;
}

export const couches: Couche[] = [
  { n: 1,  nom: "LA MATRICE",            age: "0-3",   coeur: "Présence des aînés (RPU), 7 strates affectives (Pikler-Lóczy, allomaternage)",    file: "anthropie_couche_01_matrice.md",    slug: "couche-01-matrice",    hasFile: true,  maturite: "robuste"  },
  { n: 2,  nom: "LE SANCTUAIRE",         age: "3-7",   coeur: "7 disciplines de la posture adulte, droit à la curiosité préservée",              file: "anthropie_couche_02_sanctuaire.md", slug: "couche-02-sanctuaire", hasFile: true,  maturite: "sensible", article: "31bis"      },
  { n: 3,  nom: "L'ATELIER",             age: "5-12",  coeur: "Constructionnisme Papert + Pont des Certifications (Open Badges 3.0)",            file: "anthropie_couche_03_atelier.md",    slug: "couche-03-atelier",    hasFile: true,  maturite: "robuste",  article: "31ter"      },
  { n: 4,  nom: "LA PAROLE",             age: "7-15",  coeur: "Cercles de Voix + Discipline de Prédiction-Avant-Vocal anti-LLM-flattening",      file: "anthropie_couche_04_parole.md",     slug: "couche-04-parole",     hasFile: true,  maturite: "robuste",  article: "31quater"   },
  { n: 5,  nom: "LA VILLE",              age: "10-18", coeur: "RCI Illich + Big Picture Learning + dual apprenticeship suisse",                  file: "anthropie_couche_05_ville.md",      slug: "couche-05-ville",      hasFile: true,  maturite: "sensible", article: "31quinquies"},
  { n: 6,  nom: "LE REGARD",             age: "10-18", coeur: "CVO Freire + Critique deepfakes + Diaspora Visuelle",                              file: "anthropie_couche_06_regard.md",     slug: "couche-06-regard",     hasFile: true,  maturite: "sensible", article: "31sexies"   },
  { n: 7,  nom: "LES SEUILS",            age: "12-22", coeur: "12 Rites Articulés + Liminalité Protégée juridique",                              file: "anthropie_couche_07_seuils.md",     slug: "couche-07-seuils",     hasFile: true,  maturite: "robuste",  article: "31septies"  },
  { n: 8,  nom: "LA MYCOLOGIE",          age: "15-25", coeur: "Cellules Mycéliales 4-7 personnes 5-10 ans (refondation post-BCI)",               file: "anthropie_couche_08_mycologie.md",  slug: "couche-08-mycologie",  hasFile: true,  maturite: "sensible", article: "31octies"   },
  { n: 9,  nom: "L'ARCHIVE VIVANTE",     age: "0-∞",   coeur: "Maison d'Atomes + Anti-Résurrection AI",                                            file: "anthropie_couche_09_archive.md",    slug: "couche-09-archive",    hasFile: true,  maturite: "robuste",  article: "31novies"   },
  { n: 10, nom: "LE CONSEIL DES MORTS",  age: "4-∞",   coeur: "Maisons des Lignées + Audiences (anti-tabou occidental)",                          file: "anthropie_couche_10_morts.md",      slug: "couche-10-morts",      hasFile: true,  maturite: "sensible", article: "31decies"   },
  { n: 11, nom: "LA PARENTÉ ÉLARGIE",    age: "3-25",  coeur: "3 Parents Non-Humains Choisis (modèle Te Awa Tupua)",                              file: "anthropie_couche_11_parente.md",    slug: "couche-11-parente",    hasFile: true,  maturite: "robuste",  article: "31undecies" },
  { n: 12, nom: "LE SEUIL DE LA BRISURE",age: "9-∞",   coeur: "Hospices des Brisures + Kintsugi + Wounded Healers",                               file: "anthropie_couche_12_brisure.md",    slug: "couche-12-brisure",    hasFile: true,  maturite: "sensible", article: "31duodecies"},
];

export const articles: Article[] = [
  { code: "31bis",       titre: "Droit à la curiosité préservée (3-7 ans)",                                  coucheSource: 2  },
  { code: "31ter",       titre: "Reconnaissance des apprentissages exploratoires",                           coucheSource: 3  },
  { code: "31quater",    titre: "Droit délibératif de l'enfant 9 ans et plus",                              coucheSource: 4  },
  { code: "31quinquies", titre: "Reconnaissance professionnelle des apprentissages urbains",                coucheSource: 5  },
  { code: "31sexies",    titre: "Souveraineté visuelle (regard critique image)",                            coucheSource: 6  },
  { code: "31septies",   titre: "Liminalité Protégée pour rites de passage",                                coucheSource: 7  },
  { code: "31octies",    titre: "Droit à appartenir à une cellule durable d'observation mutuelle",          coucheSource: 8  },
  { code: "31novies",    titre: "Maison d'Atomes Personnelle (extension GDPR Art. 17)",                     coucheSource: 9  },
  { code: "31decies",    titre: "Lien actif avec ses morts, éducation à la mort dès 4 ans",                 coucheSource: 10 },
  { code: "31undecies",  titre: "3 Parents Non-Humains Choisis (extension Te Awa Tupua Act NZ 2017)",       coucheSource: 11 },
  { code: "31duodecies", titre: "Brisure accompagnée non-pathologisée",                                     coucheSource: 12 },
];

/** Repo de référence (utilisé pour générer les liens GitHub blob/master/<file>) */
export const githubBase = "https://github.com/SanTiepi/anthropie-edifice/blob/master";

/** États-pilotes canoniques pour le protocole 31bis-duodecies */
export const etatsPilotes = ["Norvège", "Costa Rica", "Nouvelle-Zélande", "Bhoutan", "Québec"] as const;
