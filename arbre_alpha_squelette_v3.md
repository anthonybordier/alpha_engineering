# L'arbre de la recherche d'alphas — squelette intégral consolidé (v3, gelé)

**Racine : α ≈ E[ r(t+h) | F(t) ]**

État v3 : **l'arbre entier est au grain ✓✓** (rédigé avec formules-pivots et références primaires).
Prisme : equity cross-sectionnel & crypto, intégré aux feuilles. Notations : §0.5
(h = horizon, H = demi-vie, λ = décroissance EMA, κ = pénalité ridge, φ = ln2/H_α = vitesse de decay de l'alpha).

---

## 0. Cadre et conventions ✓✓
- 0.1 Panel & deux axes (CS vs TS) · 0.2 Définition de l'alpha (F_t, h, ≈ ; prévision ≠ position)
- 0.3 IC & ICIR (rank IC par date ; IC 0,02–0,06 ; σ(IC) 0,10–0,20) · 0.4 Loi fondamentale (IR ≈ TC·IC·√BR)
- 0.5 Notations · 0.6 Conventions (√252 vs √365 ; knowledge time ; univers PIT ; signes)
- 0.7 Frontière alpha/beta relative au modèle de risque · 0.8 Plan ; les deux budgets (degrés de liberté, turnover)

## 1. Génération de signaux ✓✓

### 1.1 Familles d'alphas ✓✓
- 1.1.1 Prix & volumes : MOM 12-1 (z-CS) ; crashes conditionnels & momentum dynamique w\* = μ̂/2λσ̂² (Daniel-Moskowitz) ; TSMOM sign(r₁₂ₘ)·σ\*/σ̂ ; reversal résiduel, profits ∝ VIX (Nagel) ; ILLIQ Amihud ; VRP = IV² − E[RV²] (BTZ) ; BAB (β̃ = 0,6β̂+0,4) ; saisonnalités Heston-Sadka
- 1.1.2 Fondamentaux : value within-secteur, HML 2×3 ; GP = (Rev−COGS)/Actifs (Novy-Marx) ; accruals de Sloan (formule bilancielle, prédicteur négatif) ; révisions Δconsensus/P ; carry unifié C = (S−F)/F (KMPV) — funding perp = carry observé (×1095)
- 1.1.3 Flux & positionnement : inélasticité ΔP/P ≈ M·f, M ≈ 5 (Gabaix-Koijen) ; SIR/DTC & SII agrégé (RRZ) ; fire sales (Coval-Stafford, pression → réversion 12-18 m) ; GEX = ΣOI·Γ·S² (amortisseur/amplificateur) ; COT index ; netflows on-chain
- 1.1.4 Données alternatives : TONE Loughran-McDonald ; Lazy Prices (similarité cosinus des filings — le changement prédit) ; look-ahead sémantique des LLM ; nowcasting physique (satellite, cartes) ; érosion α(t) = α₀e^{−t/T_comm} ; MVRV = MC/RC, SOPR (vintage on-chain)
- 1.1.5 Événementiel : AR/CAR & inférence en coupe (MacKinlay) ; PEAD sur SUE, autocorrélation saisonnière des surprises (Bernard-Thomas) ; recompositions : Q = Δw·AUM puis I ≈ Yσ√(Q/ADV) ; pinning/GEX ; unlocks (u = libéré/float), listings ; érosion par publication des calendriers
- Fil : chaque famille = (mécanisme de persistance, formule de construction) — le couple entre au registre comme hypothèse.

### 1.2 Feature engineering ✓✓
- 1.2.1 Transformations : 12-1 ; résidualisation ; ratios within ; changements vs niveaux (SUE)
- 1.2.2 Fenêtres : EMA/Kalman ; banc multi-échelles x·e^{−x²/4} ; vol (EWMA, range, RV) ; overnight/intraday, grilles UTC & funding
- 1.2.3 Interactions : g(z) lisse ; double sorts ; ML (GKX, monotonie, SHAP) ; N effectif, pré-spécification, holdout
- 1.2.4 Point-in-time : lags de publication ; vintages & bitemporel ; corporate actions & delistings ; pièges crypto

### 1.3 Normalisation ✓✓ : winsorisation (MAD) → z ; rank-gauss ; z rolling & réponses bornées ; neutralisation (IC transférable) ; smoothing, turnover ∝ √(1−ρ_cs(1)), budget par sleeve

### 1.4 Cibles & labels ✓✓ : cible vol-scalée/résiduelle/funding incluse (la cible fait partie de l'hypothèse) ; MA(h−1), T_eff ≈ T/h ; triple-barrier & meta-labeling ; Huber, bande morte, poids d'unicité & récence

## 2. Évaluation statistique ✓✓

### 2.1 Métriques ✓✓ : plancher σ₀(IC) = 1/√(N_eff−1) & plafond d'ICIR ≈ IC̄√N_eff ; placebo étalon ; IC retardé vs cumulé, IC^lag ≈ IC₀e^{−k/H_α} ⟹ **φ mesuré ici** ; sorts VW & filtre Hou-Xue-Zhang ; monotonie Patton-Timmermann ; symétrie L/S & fee d'emprunt (Drechsler) ; **c\* = spread/turnover** ; coverage ; t(α) NW returns-based vs holdings-based
### 2.2 Backtest ✓✓ : Fama-MacBeth — γ_t = portefeuille miroir, γ̄₁ ≈ IC̄·σ_cs(r) ; Petersen (clustering) ; WLS/robuste ; timeline contractuelle close(t)→open(t+1) ; prix stale ; phases de rebalancement ; univers PIT, breakpoints NYSE, delistings **−30% / −55%** (Shumway) ; **courbe Sharpe(c)** & atténuation simulée (Novy-Marx-Velikov) ; crypto : wash trading ~70% (Cong et al.), continuité, funding, grille UTC ; **placebo = certification du protocole**
### 2.3 Anti-overfitting ✓✓ : purge [t,t+h] + embargo ; CPCV, φ = kC(S,k)/S chemins ; σ(ŜR) de Lo (skew/kurtosis) ; PSR ; E[max_N ŜR] ≈ √(2lnN) ⟹ **DSR** ; N_eff d'essais corrélés ; **PBO = P(λ<0)** (CSCV) ; BH : k\* = max{k : p₍k₎ ≤ kq/M} ; **t ≈ 3,0** (Harvey-Liu-Zhu) & haircuts ; Dwork/reusable holdout ; pré-spécification
### 2.4 Non-stationnarité ✓✓ : rolling IC & bandes ; Bai-Perron ; **CUSUM de Page & ARL** (détecter coûte des mois) ; McLean-Pontiff **−26% / −58%** ; comomentum (Lou-Polk) & short interest comme capital d'arbitrage ; rendement **net de revalorisation** (Arnott) ; taxonomie de persistance (prime / friction / comportement) → demi-vies par famille ; crypto : N = 4 du halving, breadth spatial, priors transférés (Liu-Tsyvinski)

## 3. Combinaison d'alphas ✓✓ — cadre : w ∝ C⁻¹ρ

### 3.1 Pondérations simples ✓✓ (forée niveau 5) : 1/N & optimum plat ; IC (valider 100 j, classer 7 ans) ; ICIR — bayésien hiérarchique B = s²/(τ²+s²), Kelly & sleeves vol-égalisés, buckets & hystérésis, σ(IC) (NW, shrinkage du dénominateur) ; erreur d'estimation (Michaud, caps, resampling)
### 3.2 Régression régularisée ✓✓ : ridge = filtre spectral **λ_j/(λ_j+κ̃)** ; lecture bayésienne κ = σ²/τ², df(κ) au registre ; lasso instable ⟹ familles d'abord ; **cible en blocs** (2 paramètres vs K²/2) ; RIE ; **NNLS/KKT** (zéro, jamais négatif) ; demi-vies par persistance (§2.4.3) ; **disjonction** sélection/combinaison (out-of-fold, prior durci) ; CV imbriquée ; turnover de w
### 3.3 Stacking & méta-modèles ✓✓ : la démonstration out-of-fold (l'overfit payé au carré sinon) ; Breiman : convexité = NNLS sur prédictions ; super learner & oracle ; **w(z)·s = dictionnaire augmenté** (poids conditionnels dégonflés, coût en N explicite) ; Hedge : **Regret ≤ √((T/2)lnK)**, η\* ; fixed share (régimes sans détection) ; universal portfolios ; hiérarchie (i)-(iv), loyer en CV imbriquée nette de turnover
### 3.4 Orthogonalisation & pool ✓✓ : **ρ_⊥ = (ρ_new − c'C⁻¹ρ_pool)/√(1−c'C⁻¹c)** ; additivité ICIR² ; protocole d'admission (DSR + t(ρ_⊥) + c_max + c\*) ; Gram-Schmidt (hiérarchie déguisée) vs PCA (illisible) vs **HRP** (bissection variance inverse — la topologie sans l'inversion) ; **Shapley** φ_k = unique partage cohérent, oriente la recherche ; usine vs pods = critère de *mesurabilité* de la chaîne registre → ρ_⊥ → Shapley
### 3.4.5 Combinaison sous coûts ✓✓ : renvoi GP (§4.3.3) ; l'interface transporte **(s, ρ, σ(IC), φ, τ)** — des objets datés et profilés, pas des nombres nus

## 4. Portefeuille & risque ✓✓ — max w'α − (γ/2)w'Σw − TC(Δw) s.c. Aw = b
### 4.1 Modèles de risque ✓✓ : Σ = BFB'+D ; GLS Barra, USE4, bias statistic ; Marchenko-Pastur λ± = (1±√q)², clipping/RIE ; Ledoit-Wolf δ\* ; NW sur F ; crypto : Vasicek, clusters, queues
### 4.2 Construction ✓✓ : Woodbury (alpha/D − hedge factoriel) ; Kan-Zhou (perte ∝ N/T) ; KKT α̃ = α − A'λ, duals = prix des contraintes ; Jagannathan-Ma (contraintes = shrinkage) ; TC (long-only ≈ 0,3-0,4) & paper portfolio ; robust ⟺ régularisation ; l'optimiseur du pauvre
### 4.3 Coûts ✓✓ : TC(δ) = c|δ| + Yσ√(|δ|/V)|δ| (+ quadratique) ; bandes ∝ c^(1/3) ; **Gârleanu-Pedersen** : aim = Markowitz sur alphas actualisés 1/(1+φ_k·a/γ), x_t = x_{t−1} + (a/λ)(aim − x_{t−1}) ; MPC (Boyd), netting, Shapley des coûts
### 4.4 Sizing & levier ✓✓ : L = σ\*/σ̂ (Moreira-Muir ; bandes ; procyclicité) ; g(c) = r + (c−c²/2)SR², **P(DD ≥ x) = (1−x)^(2/c−1)** ; Grossman-Zhou/CPPI ; Kaminski-Lo (stop-loss & autocorrélation) ; capacité **A\* ∝ ADV·α²/τ³** (le cube du turnover)
### 4.5 Gestion des risques ✓✓ : VaR/ES & cohérence (Artzner) ; FHS ; Kupiec/Christoffersen/Acerbi-Székely ; DCC, exceedance, **λ_L = 0 gaussien** ; Khandani-Lo & reverse stress ; limites & duals du même système ; crypto : contrepartie/custody, cascades & mark price, depegs

## 5. Exécution ✓✓
### 5.1 Microstructure ✓✓ : Glosten-Milgrom (spread = assurance) ; Huang-Stoll ; **Roll s = 2√(−cov)** ; large vs small tick, la file comme actif ; auctions (volume max, Budish) & look-ahead d'auction ; NBBO/SIP, dark (Zhu), toxicité par markouts ; crypto : funding & mark/index price ; AMM **x·y = k**, impact déterministe, **LVR ≈ σ²/8** ; MEV/sandwich ; lead-lag (Hasbrouck)
### 5.2 Impact ✓✓ : **I = Yσ√(Q/V)** universel (δ ≈ 0,5, y c. bitcoin) ; Kyle λ = σ_v/2σ_u ; liquidité latente I = √(2Q/ρ') ; plateau ≈ ⅔ pic (fair pricing) ; propagateur G(l) ~ l^{−β}, mémoire du flux γ ≈ 0,5, **β = (1−γ)/2** ; cross-impact ; mesure : métaordres, conditionnement, endogénéité, randomisation ; wash trading → capacité
### 5.3 Scheduling ✓✓ : AC complet **x(t) = X·sinh(κ(T−t))/sinh(κT)**, κ = √(λ_rσ²/η̃) ; permanent linéaire hors chemin ; frontière (E,Var) ; IS/VWAP/TWAP/POV & cohérence benchmark↔objectif ; alpha : η̃ẍ = λσ²x + μ/2, front-loading, **urgence = max(κ, φ)**, le ticket transporte φ ; Obizhaeva-Wang (haltère X/(ρT+2)) ; Gatheral no-arbitrage ; HJB (CJP) ; Almgren-Lorenz adaptatif
### 5.4 Tactique ✓✓ : E[coût limit vs market] complet ; Moallemi-Yuan (valeur de file) ; **microprice** ; **OFI : ΔP ≈ β·OFI** (Cont) ; Lee-Ready ; markouts M(τ), spread réalisé vs AS ; fair-value filters, fenêtres toxiques ; **Avellaneda-Stoikov r = s − qγσ²(T−t)**, spread γσ²(T−t) + (2/γ)ln(1+γ/k) ; GLFT ; crypto : rebates, lead-lag, grille funding
### 5.5 TCA ✓✓ : **Perold : délai + trading + opportunité + frais** (quatre propriétaires) ; cascade des paper portfolios ; netting benefit ; Shapley entre sleeves ; biais (non-exécutés, benchmark contaminé, Simpson) ; surprise de coût ; **n ≈ 10⁴ ordres** ; boucle : calibration 4.3.1, randomisation, scorecards, un seul modèle pré/intra/post

## 6. Infrastructure & organisation ✓✓
### 6.1 Données ✓✓ : bitemporel **AS-OF(t) = {e ≤ t, k ≤ t < k_fin}** (= F_t exécutable), invariance testable ; append-only & capture propriétaire ; qualité quantifiée (z de fraîcheur, bandes cross-venues, Benford en continu) ; quarantaine = état du pipeline ; build vs buy & taux de réécriture des vendeurs
### 6.2 Moteur ✓✓ : parité = un artefact, **replay quotidien** ; **placebo étalonné** (IC̄ ≈ 0 ± 1/√(N_eff−1), Sharpe = −coûts) comme non-régression ; registre → trajectoires → **N_eff = 1 + (N−1)(1−ρ̄)** ; holdout scellé par hash (Dwork rendu matériel)
### 6.3 Production ✓✓ : portes pré-enregistrées ; **SPRT de Wald** sur l'IC live (bornes ln(β/(1−α)), E[T] en centaines de jours — le bucket-hystérésis comme décision sous test inachevé) ; **PSI = Σ(q−p)ln(q/p)** (< 0,1 / 0,25) — le signal meurt par ses entrées d'abord ; kill switches gradués ; réconciliation ligne à ligne ; tableau de bord = la branche 2 en continu (IC/SPRT, PSI, comomentum, bias statistic, surprises de coût, turnover de w)
### 6.4 Organisation ✓✓ : principal-agent — chaque f naïve a son exploit (f(backtest) ⟹ max N) ; contrat robuste = **Shapley déflaté du N, différé sur le live** (le fractional Kelly incitatif) ; usine ⟺ chaîne de mesure auditable, pods sinon ; mémoire : négatifs, doc par signal = (s, ρ, σ(IC), φ, τ) + mécanisme + comportement par régime

---

## Encadrés transversaux
- **A. Le shrinkage, un théorème sous huit habits** : James-Stein (3.1.3a) ; Vasicek (4.1.4, et dans BAB 1.1.1) ; Ledoit-Wolf (4.1.3, 3.2.2) ; ridge spectral (3.2.1) ; NNLS-Breiman (3.2.3, 3.3.1) ; contraintes (Jagannathan-Ma 4.2.2) ; robust opt (4.2.4) ; le différé incitatif (6.4).
- **B. Croissance & survie** : parabole de Kelly, (1−x)^(2/c−1), Grossman-Zhou (4.4) ; posterior shrinké (3.1.3b) ; le contrat différé (6.4). Trois échelles — position, book, organisation — une réponse : réduire l'exposition à l'estimé proportionnellement à son incertitude.
- **C. La sélection adverse, quatre technologies** : Glosten-Milgrom (5.1.1) → markouts (5.4.3) → Avellaneda-Stoikov (5.4.4) → LVR (5.1.4). Le spread est un prix d'assurance contre l'information.
- **D. Le chevauchement & Newey-West** : labels MA(h−1) (1.4.2) ; Fama-MacBeth (2.2.1) ; série des IC (3.1.3d, 2.1.1) ; F du modèle de risque (4.1.3) ; purge/embargo (2.3.1) comme version protocole. Un péché, cinq pénitences.
- **E. [NOUVEAU] La surveillance séquentielle** : CUSUM (2.4.1), SPRT (6.3), hystérésis des buckets (3.1.3c), fixed share (3.3.3). Détecter coûte du délai ; la réponse rationnelle est graduelle, jamais binaire.

## Renvois structurants
- **φ traverse l'arbre** : mesuré en 2.1.2 → pondère l'aim (4.3.3) → borne l'urgence (5.3.3) → voyage dans l'interface (3.4.5) → documente le signal (6.4)
- reversal (1.1.1, Nagel) ↔ relaxation d'impact (5.2.2) : la frontière sémantique
- placebo : nettoyage (2.2.5) → étalon du plancher (2.1.1) → certification du moteur (6.2)
- inélasticité M ≈ 5 (1.1.3) ↔ loi en racine (5.2.1) : macro et métaordre du même fait
- wash trading (1.2.4/2.2.5) → V (5.2.4) → capacité (4.4.4) ; comomentum (2.4.2) → tableau de bord (6.3)
- usine vs pods (3.4.4/6.4) = 1/N vs optimisé (3.1) ; carry vs revalorisation (2.4.3) → demi-vies (3.2.4)

---

**Comptage v3** : préambule (8 §) + 6 branches · 27 nœuds de niveau 2 · ~120 feuilles · **grain ✓✓ uniforme sur l'arbre entier** · 5 encadrés · 1 forage niveau 5 (3.1.3). Corpus rédigé : la totalité des nœuds, dans les transcripts + messages postérieurs de la conversation source. Prochaine étape : industrialisation Claude Code (CLAUDE.md) — intégration, harmonisation, **vérification des chiffres et attributions contre sources primaires**, compilation PDF. Estimation d'ouvrage : 750-1 100 p. brutes, 400-600 éditées.
