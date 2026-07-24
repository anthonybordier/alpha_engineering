# NOTATION.md — table des notations de l'ouvrage

Source : §0.5 de `section_0_cadre_et_conventions.md` (complétée par l'en-tête du squelette v3).
Cette table fait foi dans TOUTES les sections. Toute collision détectée pendant l'intégration
se résout en faveur de cette table et se logge dans `AVANCEMENT.md`.

## Symboles

| Symbole | Signification |
|---|---|
| *i*, *N* | indice d'actif ; taille de l'univers à une date |
| *t*, *T* | indice de date ; longueur de l'historique |
| *h* | **horizon de prédiction** (en périodes) |
| *H* | **demi-vie** d'une pondération exponentielle (§1.2.2) |
| **F**~t~ | filtration : information connaissable en *t* |
| r~i,t→t+h~ | rendement de l'actif *i* entre *t* et *t*+*h* |
| α~i,t~ | prévision (alpha) pour l'actif *i* en *t* |
| s~k~ | signal *k* après normalisation (moyenne 0, variance 1) |
| *K* | nombre de signaux dans le pool |
| ρ~k~ | IC du signal *k* |
| **C** | matrice de corrélation entre signaux (§3) |
| **w** | vecteur des poids de combinaison (§3) |
| β~i~, **F**^fac^ | expositions factorielles ; rendements des facteurs (§4.1) |
| ε~i,t~ | rendement résiduel (idiosyncratique) |
| σ | volatilité (contexte précisé localement) |
| λ | **facteur de décroissance** d'une EMA, λ = exp(−ln2 / *H*) |
| κ | **pénalité de régularisation** (ridge, §3.2) |
| τ | dispersion vraie des IC dans le prior hiérarchique (§3.1.3) |
| *B* | facteur de shrinkage bayésien, *B* = s²/(τ² + s²) |
| φ | **vitesse de decay de l'alpha**, φ = ln2 / H~α~ (mesurée en §2.1.2, transportée par l'interface §3.4.5) |
| IC, ICIR, IR, TC | cf. §0.3 et §0.4 (rank IC par date ; ICIR = moy(IC)/σ(IC) ; IR ≈ TC·IC·√BR) |

## Collisions interdites (règles dures)

1. *h* désigne l'horizon et **jamais** une demi-vie (notée *H*).
2. λ désigne la décroissance exponentielle d'une EMA et **jamais** la pénalité ridge (notée κ).
3. φ désigne la vitesse de decay de l'alpha (φ = ln2/H~α~) ; ne pas le confondre avec
   le φ de la CPCV (§2.3, nombre de chemins φ = kC(S,k)/S) — préciser « φ (chemins CPCV) »
   à chaque occurrence de ce dernier.
4. **C** est la corrélation entre signaux (branche 3) ; Σ est la covariance entre actifs
   (branche 4). Ne jamais employer l'un pour l'autre.
5. σ est surchargé (vol d'actif, σ(IC), σ_cs…) : chaque occurrence précise son objet
   en indice ou dans le texte immédiat.

## Conventions de calcul associées (rappel §0.6)

- Log-rendements pour l'agrégation temporelle, rendements simples en cross-section ;
  equity = rendements totaux ; crypto = **funding inclus**.
- Annualisation : √252 en equity, √365 en crypto — ne jamais mélanger.
- Knowledge time : jointures uniquement sur « connaissable à partir de » ;
  close(t) → exécution au plus tôt open(t+1) ; horodatages crypto en UTC (grille funding 00/08/16).
- Univers point-in-time strict, sorties conservées avec rendement terminal.
- Signe de chaque signal fixé par prior économique, jamais par backtest.
