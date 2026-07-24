# Encadré A — Le shrinkage, un théorème sous huit habits

> **État : relu** (intégré s.13, harmonisé s.14 — renvois et notation vérifiés) — synthèse transversale ; sources dans les sections citées ; vérification des chiffres à venir.

Un seul théorème traverse cet ouvrage plus souvent qu'aucun autre, et il mérite d'être énoncé une fois pour toutes : **quand on estime simultanément plusieurs quantités bruitées, l'estimateur qui tire chaque estimée vers une cible commune domine l'estimateur naïf composante par composante** — et l'ampleur du tirage optimal est proportionnelle au rapport bruit d'estimation / dispersion vraie. C'est le résultat de James-Stein (1961) : en dimension K ≥ 3, le shrinkage vers la moyenne commune domine le MLE *quel que soit* le vrai vecteur de paramètres. Ce qui rend le théorème structurant pour la recherche d'alphas, c'est que le régime de travail du praticien — beaucoup de quantités voisines, peu d'historique stationnaire, bruit dominant (§0.3, §3.1.2) — est précisément celui où la domination est la plus large. L'ouvrage le rencontre sous huit habits.

**Premier habit — James-Stein sur les IC** (§3.1.3a). Le pool d'alphas est un modèle hiérarchique : θ~k~ ~ N(m, τ²), observé avec bruit s~k~², posterior E[θ~k~|ÎC~k~] = m + (ÎC~k~ − m)·τ²/(τ²+s~k~²). Le facteur B = s²/(τ²+s²) — la fraction de l'écart mesuré qu'on jette — vaut ≈ 0,5 pour un an de données : la moitié de ce qui distingue un signal de la moyenne du pool est du bruit. L'empirical Bayes rend le geste opérationnel : le pool fournit m et τ.

**Deuxième habit — Vasicek sur les betas** (§4.1.4 ; déjà dans la définition du BAB, §1.1.1). β̃~i~ = w~β~·β̂~i~ + (1−w~β~)·β̄~groupe~, w~β~ = τ²~β~/(τ²~β~+s²~i~) — la même formule exactement, appliquée aux expositions ; obligatoire en crypto où les fenêtres courtes rendent les β̂ très bruités, et présente jusque dans la construction du facteur betting-against-beta (β̃ = 0,6β̂ + 0,4).

**Troisième habit — Ledoit-Wolf sur les matrices** (§4.1.3, transposé aux signaux en §3.2.2). Σ̃ = δ\*·T₀ + (1−δ\*)·S, avec δ\* = bruit/distance-à-la-cible en forme close — le posterior hiérarchique devenu matriciel ; et le choix de la cible (identité, corrélation constante, blocs par famille) est le choix du prior.

**Quatrième habit — la ridge spectrale** (§3.2.1). w(κ) ∝ (C + κ̃I)⁻¹ρ multiplie chaque direction propre par λ~j~/(λ~j~+κ̃) : les contrastes bien estimés passent, les directions bruitées sont écrasées — le MAP du prior w ~ N(0, τ²I), avec κ = σ²~e~/τ². Le κ élevé qu'on trouve par CV est la *mesure* de la domination du bruit ; et le clipping RMT de §4.1.2 en est le cousin par seuillage.

**Cinquième habit — NNLS-Breiman** (§3.2.3, §3.3.1). Les contraintes de non-négativité sur les poids de combinaison (et de stacking) sont un prior dur : un signal dont la contribution partielle est négative reçoit zéro, jamais un poids inversé — c'est ce qui fait « marcher » le stacking (Breiman 1996), et c'est un shrinkage implicite des corrélations qui justifiaient les poids négatifs.

**Sixième habit — les contraintes de Jagannathan-Ma** (§4.2.2). Le théorème rend le lien exact : le minimum-variance sous bornes équivaut au minimum-variance non contraint sur Σ̃ = Σ − (δ1'+1δ') + (ν1'+1ν') — interdire une position extrême, c'est réduire les covariances qui la justifiaient. Les contraintes « fausses » améliorent l'out-of-sample parce qu'elles régularisent Σ̂ là où il est le plus bruité.

**Septième habit — l'optimisation robuste** (§4.2.4). max~w~ min~α∈U~ se résout en max~w~ w'α̂ − κ~r~·‖w‖~Ω~ − (γ/2)w'Σw : le pire cas sur un ellipsoïde d'incertitude *est* une pénalité de régularisation — choisir la taille de l'ensemble d'incertitude, c'est choisir un shrinkage.

**Huitième habit — le différé incitatif** (§6.4). Le contrat qui paie le chercheur sur une assiette déflatée du N et différée sur le live réduit la part payée sur l'estimé proportionnellement à son incertitude — le shrinkage appliqué non plus aux paramètres mais aux *personnes* ; le fractional Kelly incitatif (encadré B).

La leçon commune, qui explique pourquoi l'arbre y revient sans cesse : dans un monde où le bruit d'estimation domine la dispersion vraie, presque toutes les « sophistications » qui fonctionnent — bayésien, régularisation, contraintes, robustesse, quantification en buckets (§3.1.3c), gouvernance — sont des paramétrages différents du même geste. Savoir le reconnaître évite de l'empiler en double (§3.2.2 : on ne cumule pas ridge et shrinkage-de-C à pleine dose) et donne le bon réflexe face à toute méthode nouvelle : demander d'abord *vers quoi elle shrinke, et à quel taux*.

**Renvois** : §1.1.1 ; §3.1.2–§3.1.4 ; §3.2.1–§3.2.3 ; §3.3.1 ; §4.1.2–§4.1.4 ; §4.2.2, §4.2.4 ; §6.4 ; encadré B.
