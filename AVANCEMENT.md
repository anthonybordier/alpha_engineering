# AVANCEMENT.md — état par nœud & index corpus → squelette

États : **indexé** (sources identifiées) → **intégré** (corps rédigé depuis le corpus) →
**relu** (harmonisation notation/renvois) → **vérifié** (chiffres & attributions contrôlés).

Corpus : `transcripts/source.md` — messages numérotés `[M001]`–`[M138]`
(conversation claude.ai `8a5d0bf2-891c-43e4-a4e9-53aae0ad61e2`, extraite de `conversations.json` en session 1).

## Notes structurantes (à relire avant toute intégration)

- **§1.1 existe en DEUX versions** : M126 (première) et **M128 (seconde, plus mathématique,
  qui la REMPLACE)**. Intégrer depuis M128 ; M126 ne sert qu'en secours si un passage manque.
- **Branche 4 en deux passes** : M070 (survol initial) puis **M072 (version resserrée avec
  formules, qui remplace M070)**. Les références de la branche 4 sont dans M076.
- **Branche 6 en deux passes** : M104 (première passe) puis **M130 (grain ✓✓, version de référence)**.
- Messages assistants **vides** (tentatives avortées/régénérées) : M008, M074, M090 — sans contenu.
- Re-clics / messages de navigation sans contenu nouveau : M020, M022, M023 (cartes d'avancement),
  M068 (re-clic 1.3), M014 (lecture de l'arbre v1), M041 (chat vs Claude Code).
- Méta-projet (pas du corpus de l'ouvrage) : M036–M041 (sources & taille), M044–M050
  (transcription partielle .txt — obsolète, le JSON fait foi), M107–M110 (transfert Claude Code),
  M133–M138 (export & fichiers du projet).
- Gels du squelette : **M039** (v1), **M106** (v2 : +section 0, +3.4.5, +encadrés A–D),
  **M132** (v3 : grain uniforme, +encadré E — version contractuelle).
- Les échanges pédagogiques M051–M066 alimentent §0 et §1.3.4 (voir index).

## Index corpus → squelette

| Nœud | Fichier | Sources principales | Sources secondaires | État |
|---|---|---|---|---|
| §0 (0.1–0.8) | `section_0_cadre_et_conventions.md` | M054 (rédaction complète) | M002 (définition, →0.2), M004 (plan de l'arbre, →0.8), M052 (cross-section/panel, →0.1), M056+M058 (IC vs E[·], →0.3), M060 (ICIR, Spearman/Pearson, →0.3), M066 (turnover, →0.8) | **relu** (session 2 : + φ en §0.5, renvois loggés) |
| §1.1 | `sections/1.1_familles_alphas.md` | **M128** (remplace M126) | M126, M006 (survol), M010 (prisme equity/crypto) | **intégré** (session 2) |
| §1.2 | `sections/1.2_feature_engineering.md` | M018 (1.2.1), M025 (1.2.2), M027 (1.2.3), M029 (1.2.4) | M016 (vue d'ensemble) | **intégré** (session 2) |
| §1.3 | `sections/1.3_normalisation.md` | M043 | M062 (demi-vie), M064 (autocorrélation), M066 (turnover) → §1.3.4 | **intégré** (session 3) |
| §1.4 | `sections/1.4_cibles_labels.md` | M102 | — | **intégré** (session 3) |
| §2.1 | `sections/2.1_metriques.md` | M114 | M012 (survol branche 2) | **intégré** (session 4) |
| §2.2 | `sections/2.2_backtest.md` | M116 | M012 | **intégré** (session 4) |
| §2.3 | `sections/2.3_anti_overfitting.md` | M112 | M012 | **intégré** (session 5) |
| §2.4 | `sections/2.4_non_stationnarite.md` | M118 | M012 | **intégré** (session 5) |
| §3.1 | `sections/3.1_ponderations_simples.md` | M033 ; **M035 (forage niveau 5 : 3.1.3)** | M031 (survol branche 3) | **intégré** (session 6) |
| §3.2 | `sections/3.2_regression_regularisee.md` | M120 | M031 | **intégré** (session 6) |
| §3.3 | `sections/3.3_stacking_meta_modeles.md` | M122 | M031 | **intégré** (session 7) |
| §3.4 | `sections/3.4_orthogonalisation_pool.md` | M124 | M031 | **intégré** (session 7) |
| §3.4.5 | `sections/3.4.5_combinaison_sous_couts.md` | M124 (sous-section finale) | M082 (§4.3.3 Gârleanu-Pedersen) | **intégré** (session 7) |
| §4.1 | `sections/4.1_modeles_de_risque.md` | M078 | **M072** (survol formel, remplace M070), M076 (références br. 4) | **intégré** (session 8) |
| §4.2 | `sections/4.2_construction.md` | M080 | M072, M076 | **intégré** (session 8) |
| §4.3 | `sections/4.3_couts.md` | M082 | M072, M076 | **intégré** (session 9) |
| §4.4 | `sections/4.4_sizing_levier.md` | M084 | M072, M076 | **intégré** (session 9) |
| §4.5 | `sections/4.5_gestion_des_risques.md` | M086 | M072, M076 | **intégré** (session 9) |
| §5.1 | `sections/5.1_microstructure.md` | M092 | M088 (survol branche 5) | **intégré** (session 10) |
| §5.2 | `sections/5.2_impact.md` | M094 | M088 | **intégré** (session 10) |
| §5.3 | `sections/5.3_scheduling.md` | M096 | M088 | **intégré** (session 11) |
| §5.4 | `sections/5.4_tactique.md` | M098 | M088 | **intégré** (session 11) |
| §5.5 | `sections/5.5_tca.md` | M100 | M088 | **intégré** (session 11) |
| §6.1 | `sections/6.1_donnees.md` | **M130** | M104 (première passe) | **intégré** (session 12) |
| §6.2 | `sections/6.2_moteur.md` | **M130** | M104 | **intégré** (session 12) |
| §6.3 | `sections/6.3_production.md` | **M130** | M104 | **intégré** (session 12) |
| §6.4 | `sections/6.4_organisation.md` | **M130** | M104 | **intégré** (session 12) |
| Encadré A | `encadres/A_shrinkage.md` | M035, M078, M080, M120, M122, M130 | M132 (définition v3) | **intégré** (session 13) |
| Encadré B | `encadres/B_croissance_et_survie.md` | M035, M084, M130 | M132 | **intégré** (session 13) |
| Encadré C | `encadres/C_selection_adverse.md` | M092, M098 | M132 | **intégré** (session 13) |
| Encadré D | `encadres/D_chevauchement_newey_west.md` | M102, M116, M035, M114, M078, M112 | M132 | **intégré** (session 13) |
| Encadré E | `encadres/E_surveillance_sequentielle.md` | M118, M130, M035, M122 | M132 (ajout en v3) | **intégré** (session 13) |

## Références bibliographiques (pour la passe de vérification)

- M037 : inventaire des sources canoniques par branche (à recouper à la compilation BibTeX).
- M076 : références de la branche 4.
- Rappel garde-fou : le corpus vient de mémoire de modèle — architecture fiable, chiffres
  fins et attributions **à contrôler contre les sources primaires** ou marquer `[à vérifier]`.

## Journal de session

### Session 1 — 2026-07-24 (initialisation)
- Extraction de la conversation source (« Alpha comme statistique prédictive des cours »,
  138 messages) depuis `_export/conversations.json` → `transcripts/source.md`.
- Génération : `NOTATION.md` (depuis §0.5), `STYLE.md` (règles + 2 étalons),
  arborescence `sections/` (27 nœuds) + `encadres/` (A–E), `TODO_renvois.md`, ce fichier.
- Tous les nœuds passés à l'état **indexé** ; §0 déjà **intégré** (préambule rédigé).
- Prochaine session (workflow) : branche 0 (relecture/harmonisation du préambule) puis
  branche 1 — commencer par §1.1 depuis M128.

### Session 2 — 2026-07-24 (branche 0 + demi-branche 1 : §1.1, §1.2)
- §0 **relu** : ajout de la ligne φ à la table §0.5 (harmonisation avec NOTATION.md et
  l'en-tête du squelette v3) ; renvois vers sections non écrites loggés dans TODO_renvois.md.
- §1.1 **intégré** depuis M128 (M126 écartée conformément à la note « deux versions ») ;
  mini-titres interprétatifs repris de M126 ; chiffres fins marqués `[à vérifier]`
  (spread accruals ~10%/an, PEAD CAR(+2,+60) ≈ +2%).
- §1.2 **intégré** depuis M018/M025/M027/M029, cadrage depuis M016 ; chiffres marqués
  `[à vérifier]` (efficacité ×5 de Parkinson, Sharpe ~1,2 pour 1 000 essais, Novy-Marx 12-7).
- **Collisions de notation traitées** (NOTATION.md fait foi) :
  (a) M025 paramétrait l'EMA « en demi-vie h » → corrigé en **H** dans §1.2.2 ;
  (b) le λ de Daniel-Moskowitz (w\* = μ̂/2λσ̂²) est une aversion au risque, pas la
  décroissance EMA → noté **λ_a** avec glose dans §1.1.1, proposition loggée dans
  `PROPOSITIONS_squelette.md` (le squelette, gelé, garde λ).
- Prochaine session : fin de branche 1 — §1.3 (depuis M043 + M062/M064/M066) et
  §1.4 (depuis M102).

### Session 3 — 2026-07-24 (fin de branche 1 : §1.3, §1.4)
- §1.3 **intégré** depuis M043 ; §1.3.4 enrichi des définitions quantitatives de
  M062/M064/M066 (ρ_cs, turnover ∝ √(1−ρ_cs(1)), les trois demi-vies H / H_s / H_α),
  conformément à la consigne rétroactive de M068 (« c'est la version enrichie qu'il
  faudra retenir »).
- §1.4 **intégré** depuis M102 (triple-barrier, meta-labeling, MA(h−1), Huber,
  unicité & récence).
- **La branche 1 est complète** (1.1 → 1.4, tous intégrés) ; la branche 0 est relue.
- Prochaine session : branche 2 (ou demi-branche) — §2.1 (M114) et §2.2 (M116),
  puis §2.3 (M112) et §2.4 (M118) ; survol M012 en cadrage.

### Session 4 — 2026-07-24 (demi-branche 2 : §2.1, §2.2)
- §2.1 **intégré** depuis M114 (plancher σ₀(IC), décomposition de σ(IC), plafond d'ICIR,
  IC retardé vs cumulé et φ, HXZ, Patton-Timmermann, Drechsler, c\*, t(α) NW).
- §2.2 **intégré** depuis M116 (Fama-MacBeth = portefeuille miroir, γ̄₁ ≈ IC̄·σ_cs(r),
  timeline contractuelle, Shumway −30%/−55%, courbe Sharpe(c), nettoyage crypto,
  placebo = certification).
- Chiffres marqués `[à vérifier]` : majorité des ~450 anomalies HXZ, −55% Nasdaq
  (Shumway & Warther), ~70% wash trading (Cong et al.).
- Prochaine session : fin de branche 2 — §2.3 (M112) et §2.4 (M118).

### Session 5 — 2026-07-24 (fin de branche 2 : §2.3, §2.4)
- §2.3 **intégré** depuis M112 (purge/embargo/CPCV, σ(ŜR) de Lo, PSR/DSR, PBO/CSCV,
  BH/FDR, t ≈ 3,0 Harvey-Liu-Zhu, Dwork/Thresholdout). Le φ des chemins CPCV est noté
  **φ_CPCV** avec glose, conformément à la règle 3 de NOTATION.md.
- §2.4 **intégré** depuis M118 (rolling IC & bandes, Bai-Perron, CUSUM/ARL,
  McLean-Pontiff −26%/−58%, comomentum, carry vs revalorisation, taxonomie de
  persistance, N = 4 du halving, priors transférés Liu-Tsyvinski).
- **La branche 2 est complète** (2.1 → 2.4). Branches 0-2 : relue/intégrées.
- Chiffres marqués `[à vérifier]` : écart CV naïve/purgée en dixièmes de Sharpe,
  Sharpe ~0,9-1,2 pour 100 essais, haircut 1,0 → 0,4, −26%/−58% McLean-Pontiff.
- Prochaine session : branche 3 — §3.1 (M033 + forage M035) et §3.2 (M120),
  puis §3.3 (M122) et §3.4 + §3.4.5 (M124).

### Session 6 — 2026-07-24 (demi-branche 3 : §3.1, §3.2)
- §3.1 **intégré** depuis M033 + M035, cadrage M031 en ouverture (w ∝ C⁻¹ρ).
  Le forage niveau 5 (§3.1.3 a-d : posterior B = s²/(τ²+s²), Kelly/sleeves,
  buckets-hystérésis, σ(IC)) est restitué en sous-sections a)-d).
- §3.2 **intégré** depuis M120 (filtre spectral λ_j/(λ_j+κ̃), df(κ), cible en blocs,
  NNLS/KKT, disjonction sélection/combinaison, CV imbriquée). Glose ajoutée sur les
  λ_j (valeurs propres, usage local ≠ λ EMA).
- Prochaine session : fin de branche 3 — §3.3 (M122) et §3.4 + §3.4.5 (M124).

### Session 7 — 2026-07-24 (fin de branche 3 : §3.3, §3.4, §3.4.5)
- §3.3 **intégré** depuis M122 (out-of-fold démontré, Breiman/NNLS, super learner,
  dictionnaire augmenté, Hedge/regret, fixed share, hiérarchie (i)-(iv)).
- §3.4 **intégré** depuis M124 (ρ_⊥, additivité ICIR², Gram-Schmidt/PCA/HRP,
  Shapley noté **φ^Sh** avec glose, usine vs pods).
- §3.4.5 **intégré** depuis M124 (l'interface (s, ρ, σ(IC), φ, τ) ; τ_k = turnover
  glosé contre le τ du prior).
- **Collisions de notation** : P2 (φ Shapley) et P3 (τ turnover) loggées dans
  PROPOSITIONS_squelette.md ; sections conformes via gloses.
- **La MOITIÉ RECHERCHE est close** : branches 0-3 intégrées/relues (13 nœuds).
- Prochaine session : branche 4 (demi-branche) — §4.1 (M078) et §4.2 (M080),
  avec M072 (survol formel) et M076 (références) en cadrage.

### Session 8 — 2026-07-24 (demi-branche 4 : §4.1, §4.2)
- §4.1 **intégré** depuis M078 (Barra/USE4, bias statistic, Marchenko-Pastur &
  clipping/RIE, Ledoit-Wolf, NW sur F, Vasicek & clustering crypto).
- §4.2 **intégré** depuis M080 (Woodbury, Kan-Zhou N/T, KKT & duals,
  Jagannathan-Ma, TC 0,3-0,4 long-only, robust opt, optimiseur du pauvre).
- M076 (bibliographie de la branche 4) exploité pour les références ; M078 note que
  la branche 4 est la plus facile à vérifier — roder le pipeline biblio par elle.
- Chiffres `[à vérifier]` : ~90-95% des valeurs propres dans le bulk MP, 50-70% de
  variance expliquée par BTC, 80-90% du TC pour l'optimiseur du pauvre.
- Prochaine session : fin de branche 4 — §4.3 (M082), §4.4 (M084), §4.5 (M086).

### Session 9 — 2026-07-24 (fin de branche 4 : §4.3, §4.4, §4.5)
- §4.3 **intégré** depuis M082 (TC(δ) à trois termes, bandes en c^(1/3),
  **Gârleanu-Pedersen complet** — aim, actualisation 1/(1+φ_k·a/γ) —, MPC/netting).
  Le λ de coût quadratique est noté **λ_c** (usage local glosé).
- §4.4 **intégré** depuis M084 (vol targeting Moreira-Muir/Harvey, parabole de Kelly,
  P(DD ≥ x) = (1−x)^(2/c−1), Grossman-Zhou/CPPI, Kaminski-Lo, capacité
  A\* ∝ ADV·α²/τ³). Le turnover de la formule de capacité est noté **τ_to** (cf. P3).
- §4.5 **intégré** depuis M086 (VaR/ES & Artzner, FHS, Kupiec/Christoffersen/
  Acerbi-Székely, DCC, exceedance, λ_L = 0 gaussien, Khandani-Lo, reverse stress,
  crypto : contrepartie/liquidations/depegs).
- **La branche 4 est complète** (4.1 → 4.5). Chiffres `[à vérifier]` : A\* crypto en
  millions, USDC 0,88, capacités Frazzini-Israel-Moskowitz.
- Prochaine session : branche 5 (demi-branche) — §5.1 (M092) et §5.2 (M094),
  survol M088 en cadrage.

### Session 10 — 2026-07-24 (demi-branche 5 : §5.1, §5.2)
- §5.1 **intégré** depuis M092 (Glosten-Milgrom, Huang-Stoll, Roll, tick & files,
  auctions/Budish, NBBO/dark/Zhu, perps & funding, AMM x·y = k, LVR ≈ σ²/8, MEV,
  lead-lag Hasbrouck).
- §5.2 **intégré** depuis M094 (loi en racine I = Yσ√(Q/V), Kyle λ_K, liquidité
  latente I = √(2Q/ρ'), plateau ⅔ & fair pricing, propagateur G(l) ~ l^−β avec
  β = (1−γ)/2, cross-impact, biais de mesure & randomisation).
- Gloses : λ_K (Kyle), ρ_v (densité latente) — usages locaux vs NOTATION.md.
- Chiffres `[à vérifier]` : ~10% du volume US en clôture.
- Prochaine session : fin de branche 5 — §5.3 (M096), §5.4 (M098), §5.5 (M100).

### Session 11 — 2026-07-24 (fin de branche 5 : §5.3, §5.4, §5.5)
- §5.3 **intégré** depuis M096 (AC complet — x(t) en sinh, κ_AC —, benchmarks,
  front-loading & urgence = max(κ_AC, φ), Obizhaeva-Wang, Gatheral, HJB, adaptatif).
- §5.4 **intégré** depuis M098 (E[coût limit vs market], Moallemi-Yuan, microprice,
  OFI, Lee-Ready, markouts M(τ), Avellaneda-Stoikov, GLFT, crypto rebates/lead-lag).
- §5.5 **intégré** depuis M100 (Perold 4 termes/4 propriétaires, cascade des paper
  portfolios, netting benefit, Shapley des coûts, n ≈ 10⁴ ordres, boucle pré/intra/post).
- **La branche 5 est complète** (5.1 → 5.5). Encadré C complet sur ses quatre faces.
- **P4 loggée** : κ (AC) vs κ (ridge) → κ_AC en section ; γ d'impact permanent → γ_p.
- Prochaine session : branche 6 — §6.1-§6.4 depuis M130 (référence), M104 (1ère passe).

### Session 12 — 2026-07-24 (branche 6 complète : §6.1-§6.4)
- Les quatre nœuds **intégrés** par fusion M130 (formules ✓✓ : AS-OF, placebo
  étalonné, N_eff = 1+(N−1)(1−ρ̄), SPRT & bornes, PSI, contrat Shapley-déflaté-différé)
  × M104 (prose détaillée : append-only/Kleppmann, vectorisé vs event-driven,
  pipeline à portes, kill switches gradués, réconciliation, comité de revue, mémoire).
- **L'ARBRE ENTIER EST INTÉGRÉ** : §0 (relu) + 27 nœuds (branches 1-6). Restent les
  5 encadrés transversaux (A-E), puis les passes d'harmonisation et de VÉRIFICATION.
- Chiffres `[à vérifier]` : E[T] du SPRT en centaines de jours.
- Prochaine session : encadrés A-E (matière déjà rédigée dans les sections —
  travail de synthèse), puis passe d'harmonisation (grep terminologie/symboles,
  résolution TODO_renvois), puis passe de vérification, puis compilation pandoc.

### Session 13 — 2026-07-24 (encadrés A-E)
- Les cinq encadrés **intégrés** (synthèses transversales, ~700-900 mots chacun) :
  A (huit habits du shrinkage), B (trois échelles de croissance & survie),
  C (quatre technologies de la sélection adverse), D (un péché, cinq pénitences),
  E (détecter coûte du délai — la gradualité comme design).
- **L'OUVRAGE ENTIER EST À L'ÉTAT « INTÉGRÉ »** : §0 (relu) + 27 nœuds + 5 encadrés.
- TOUS les renvois de TODO_renvois.md pointent désormais vers des cibles existantes
  (vérification renvoi par renvoi = passe d'harmonisation).
- Prochaines étapes : (1) passe d'HARMONISATION — grep symboles h/H/λ/κ/φ/τ,
  vérification des renvois, conventions §0.6 ; (2) passe de VÉRIFICATION —
  ~25 marqueurs [à vérifier] + attributions contre sources primaires ;
  (3) compilation pandoc → LaTeX → PDF (TdM = squelette, index notations, BibTeX).
