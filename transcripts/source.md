# Transcript source — « Alpha comme statistique prédictive des cours »

- **Conversation claude.ai** : `8a5d0bf2-891c-43e4-a4e9-53aae0ad61e2`
- **Créée** : 2026-07-22T17:54:34.659963Z — **Dernière mise à jour** : 2026-07-24T11:08:32.681731Z
- **Messages** : 138 (70 humain / 68 assistant)

> Extraction intégrale et ordonnée de `conversations.json` (session 1 du projet).
> Chaque message est numéroté `[M###]` pour l'indexation corpus → squelette dans `AVANCEMENT.md`.
> Les blocs de raisonnement interne (thinking) et les résultats bruts d'outils sont omis ;
> les appels d'outils (fichiers créés, visualisations) sont signalés par un marqueur `[Outil : …]`.

---

## [M001] Humain — 2026-07-22 17:54:35

certains algorithmic funds comme Squarepoint capital définissent un alpha comme une statistique ayant un pouvoir prédictif sur les cours, c est à dire comme une approximation d une esperance, conditionnelle à l information disponible au temps t, des gains ou pertes de certaines instruments. peux tu en dire plus sur cette approche ?

---

## [M002] Assistant — 2026-07-22 17:55:07

Oui, cette définition est au cœur de l'approche dite « alpha capture » ou « signal-based » qu'on retrouve chez Squarepoint, mais aussi chez WorldQuant, Millennium (les pods systématiques), Qube, ou dans l'esprit du papier « 101 Formulaic Alphas » de Kakushadze. L'idée est de formaliser un alpha non pas comme une surperformance ex post (le α de la régression CAPM), mais comme un objet prédictif ex ante :

**L'alpha comme espérance conditionnelle**

Formellement, on cherche une fonction αₜ = f(Fₜ) telle que αₜ ≈ E[rₜ₊ₕ | Fₜ], où Fₜ est la filtration (l'information disponible en t : prix, volumes, carnet d'ordres, fondamentaux, flux, données alternatives) et rₜ₊ₕ le rendement — ou le P&L — sur un horizon h. En pratique on ne cherche jamais à estimer l'espérance conditionnelle complète : on se contente d'une statistique corrélée positivement avec le rendement futur. C'est pour ça que la métrique reine est l'**information coefficient** (IC), la corrélation cross-sectionnelle ou temporelle entre le signal et le rendement réalisé. Un IC de 0,02–0,05 est déjà exploitable si le breadth est suffisant — c'est la loi fondamentale de Grinold-Kahn : IR ≈ IC × √breadth.

**Conséquences structurantes de cette définition**

1. *Séparation signal / portefeuille.* Puisque l'alpha est une prévision et non une position, la construction de portefeuille devient un problème distinct : on combine des alphas (souvent des centaines, faiblement corrélés) via une régression, un modèle de risque et un optimiseur qui intègre coûts de transaction, contraintes de neutralité (beta, secteur, facteurs Barra) et capacité. Le chercheur d'alpha n'a pas à penser au sizing.

2. *Standardisation et industrialisation.* Un alpha devient un objet testable et comparable : on le normalise (z-score cross-sectionnel, rank, winsorisation), on mesure IC, turnover, décroissance (alpha decay — la vitesse à laquelle E[rₜ₊ₕ | αₜ] tend vers zéro quand h grandit), corrélation aux alphas existants, exposition factorielle résiduelle. Cela permet une organisation en « usine à alphas » avec des milliers de signaux soumis par des chercheurs indépendants.

3. *Cadre statistique explicite.* Voir l'alpha comme une approximation de E[r | F] place le problème dans le champ de la régression / de l'apprentissage statistique : le vrai défi est le ratio signal/bruit extrêmement faible (R² de l'ordre de 10⁻³ à 10⁻⁴ en daily), la non-stationnarité, et le multiple testing (des milliers de signaux testés ⇒ contrôle du data mining via déflation du Sharpe, validation out-of-sample stricte, pénalisation de la complexité).

4. *Horizon et conditionnement.* La définition force à préciser h et Fₜ. Un alpha microstructure (h = secondes, Fₜ = carnet d'ordres) et un alpha fondamental (h = mois, Fₜ = comptes publiés) sont le même objet mathématique à des échelles différentes — d'où la possibilité de les combiner dans un même cadre, avec des poids reflétant leur decay et leurs coûts.

**Nuances et limites**

L'espérance conditionnelle n'est qu'un premier moment. Certains desks étendent la définition à la distribution conditionnelle entière (quantiles pour le risk sizing, volatilité conditionnelle pour le vol targeting), ce qui donne un objet plus riche : prévoir E[r | F] sans prévoir Var[r | F] laisse le Kelly sizing aveugle. Par ailleurs, la relation prédictive est auto-destructrice : l'exploitation du signal le fait converger vers zéro net de coûts (crowding), donc l'alpha est mieux modélisé comme E[r | F] *moins l'impact de sa propre exploitation* — c'est là qu'entre l'exécution.

Il y a aussi un point épistémologique intéressant : cette définition rend l'alpha *relatif au modèle de risque*. Ce qui est alpha pour un desk (une prime de portage, un momentum) est beta exotique pour un autre qui inclut ce facteur dans Fₜ ou dans son modèle de risque. La frontière alpha/beta n'est pas absolue, elle dépend de la richesse du conditionnement.

Si tu veux, je peux détailler un des maillons — la combinaison d'alphas (stacking, régression ridge sur IC pondérés), les tests anti-overfitting (deflated Sharpe de Bailey/López de Prado), ou la mécanique concrète d'un pipeline signal → optimiseur avec coûts. Vu ton background FCPO, l'application au cadre futures/commodities (où le cross-section est étroit et le breadth vient du temps plutôt que du nombre d'instruments) a des spécificités qui valent la discussion.

---

## [M003] Humain — 2026-07-22 18:02:04

cette première réponse est très intéressante et foisonne de directions à explorer et de points à détailler, comme un arbre de connaissances avec des branches, des sous branches, etc ...

---

## [M004] Assistant — 2026-07-22 18:03:18

Exactement — et c'est d'ailleurs comme ça que ces firmes organisent leur recherche : le domaine se décompose naturellement en un arbre où chaque nœud est une discipline quasi autonome. Voici la carte telle que je la vois :

> *[Outil : visualize:read_me]*

> *[Outil : visualize:show_widget — arbre_recherche_alpha]*

Chaque nœud est cliquable si tu veux descendre dans une branche. Quelques mots sur la logique de l'arbre : les trois branches « recherche » (génération, évaluation, combinaison) opèrent sur des prévisions pures — on n'y parle jamais de positions. Les trois branches « mise en œuvre » transforment ces prévisions en P&L réel, et c'est là que l'espérance conditionnelle rencontre les frictions : le modèle de risque, les coûts, l'impact. La beauté de l'architecture est que l'interface entre les deux moitiés est minimale — un vecteur d'alphas normalisés passe de l'une à l'autre — ce qui permet de faire travailler des dizaines de chercheurs en parallèle sans qu'ils se marchent dessus.

Chaque branche a ses propres sous-branches profondes. Sous « génération », il y a la taxonomie des familles (price-based, fondamental, flux, alternatif, événementiel), puis pour chaque famille les techniques de features et l'éternelle question de la normalisation cross-sectionnelle vs temporelle. Sous « évaluation », le sous-arbre le plus mathématique : IC et sa décomposition, structure du decay, et tout l'arsenal anti-data-mining (deflated Sharpe, combinatorial purged CV, contrôle du FDR). Sous « combinaison », le passage de N signaux à un forecast unifié — le problème est proche de l'ensembling en ML mais avec des contraintes de stabilité et d'interprétabilité. Côté mise en œuvre, « portefeuille » contient les modèles de risque factoriels et l'optimisation sous coûts, « exécution » va d'Almgren-Chriss jusqu'à la microstructure, et « infra » couvre le moteur de backtest (le point de défaillance le plus sous-estimé : biais de survivance, look-ahead, alignement des timestamps) et l'organisation humaine.

Par où veux-tu commencer ? Vu ton contexte — trading prop solo sur futures, avec Blade comme plateforme — les branches où l'écart entre la théorie « usine à alphas » et la pratique d'un desk individuel est le plus intéressant sont probablement l'évaluation (comment valider des signaux quand ton breadth est limité) et la combinaison (que faire avec 5-10 signaux plutôt que 5000).

---

## [M005] Humain — 2026-07-22 18:07:22

Détaille la branche génération de signaux : familles d alphas, feature engineering, normalisation

---

## [M006] Assistant — 2026-07-22 18:08:50

Voici la structure interne de cette branche — le pipeline qui transforme des données brutes en un alpha standardisé prêt à être combiné :

> *[Outil : visualize:show_widget — pipeline_generation_signal]*

**1. Les familles d'alphas — une taxonomie par nature du conditionnement**

Ce qui distingue les familles, c'est la composante de Fₜ qu'elles exploitent et l'horizon naturel qui en découle :

*Prix et volumes* : la famille la plus dense. Le momentum time-series (le rendement passé sur 3-12 mois prédit le rendement futur — le cœur des CTA) et cross-sectionnel (rang relatif dans l'univers), le mean-reversal court terme (1-5 jours, exploitant la sur-réaction aux flux), et la microstructure (order flow imbalance, déséquilibre bid-ask, trade signing à la Lee-Ready, horizons de secondes à heures). S'y ajoutent les alphas de volatilité (term structure de vol implicite, variance risk premium) et les saisonnalités. Le decay va de secondes (micro) à des mois (momentum) — c'est la même famille de données à des fréquences d'échantillonnage différentes.

*Fondamentaux* : en actions, value, quality, accruals, révisions d'earnings. En commodities — ton terrain — la traduction est directe : niveaux de stocks (le modèle de storage de Working/Kaldor : la convenience yield est fonction convexe décroissante des inventaires), coûts de production comme plancher souple, et surtout la structure de courbe elle-même — le carry (roll yield) est probablement l'alpha fondamental le plus robuste en futures, car il est une lecture directe de l'état des inventaires via le contango/backwardation. Pour le FCPO, les stocks MPOB, les exports SGS/ITS et le différentiel avec le soja (spread POGO côté demande biodiesel) sont les Fₜ canoniques.

*Flux et positionnement* : le COT (positionnement des commercials vs non-commercials, exploitable en contrarian aux extrêmes), l'open interest et sa dynamique, le dealer gamma (positionnement optionnel des market makers qui crée des zones d'amortissement ou d'amplification), les flux de rebalancement d'indices (GSCI/BCOM rolls — prévisibles au jour près). L'idée sous-jacente : la demande à court terme est inélastique, donc les flux non informés déplacent les prix de façon prévisible et réversible.

*Données alternatives* : météo (critique pour le palm oil — précipitations en Malaisie/Indonésie avec le lag de 6-12 mois de l'effet sur les rendements des palmiers, El Niño/La Niña), imagerie satellite (stocks visibles, NDVI des plantations), shipping (fixtures de tankers), et NLP sur news/rapports. Le coût d'acquisition et de nettoyage est élevé ; l'avantage est la faible corrélation avec les familles price-based.

*Événementiel* : comportement autour d'annonces programmées (rapports MPOB le 10 du mois, WASDE, FOMC), effets d'expiration et de roll, changements de composition d'indices. Ces alphas sont conditionnels à un événement plutôt que continus — leur breadth vient de la répétition des événements.

**2. Feature engineering — de la donnée brute au prédicteur**

C'est l'étape où réside l'essentiel de la valeur ajoutée du chercheur, et l'essentiel du risque d'overfitting. Les transformations canoniques : rendements multi-horizons (1j, 5j, 21j, 63j, 252j), écarts à des moyennes mobiles, ratios (prix/coût de production, stocks/usage), z-scores rolling, et — très important — les *résidus* : résidualiser une série contre des facteurs communs (beta marché, dollar, énergie pour les ags) pour isoler la composante idiosyncratique prédictible. Les fenêtres avec décroissance exponentielle dominent les fenêtres plates (moins de discontinuités quand une observation sort de la fenêtre, donc moins de turnover artificiel).

Le conditionnement croisé est une source majeure de signaux : un momentum × régime de volatilité (le momentum marche mieux en vol basse), un carry × niveau de stocks. Mais chaque interaction double l'espace de recherche — d'où la règle des desks sérieux : le nombre d'hypothèses testées doit être comptabilisé, car il détermine le seuil de significativité exigé ensuite.

Le point le plus négligé est la discipline *point-in-time* : chaque feature doit être construite avec exactement l'information disponible à l'instant t. Les données fondamentales sont publiées avec retard (les stocks MPOB de janvier arrivent le 10 février), révisées ex post, et les vendeurs de données réécrivent l'historique. Un backtest qui utilise la version révisée d'une série macro embarque un look-ahead invisible qui peut fabriquer un Sharpe entier à lui seul. En pratique : stocker les vintages, appliquer les lags de publication réels, et winsoriser les outliers (typiquement aux quantiles 1%/99%) *avant* toute estimation, car une seule journée aberrante peut dominer une régression sur dix ans.

**3. Normalisation — rendre le signal combinable**

L'objectif est triple : rendre les signaux comparables entre eux (pour la combinaison), stables dans le temps (pour l'optimiseur), et débarrassés d'expositions non voulues.

En *cross-sectionnel* (le cadre WorldQuant/Squarepoint actions) : à chaque date, on démoyenne et on divise par l'écart-type cross-sectionnel, ou mieux, on passe en rangs puis en quantiles gaussiens — la gaussianisation tue les outliers et rend le signal invariant aux transformations monotones de la feature. On neutralise ensuite par secteur/pays/cluster (démoyennage par groupe) et on résidualise contre les facteurs de risque (Barra), de sorte que l'alpha final soit orthogonal à ce que le modèle de risque considère comme non rémunéré.

En *temporel* — le cadre pertinent pour un desk futures avec un cross-section étroit : le z-score rolling du signal (par rapport à sa propre histoire, fenêtre 1-3 ans) et le vol-scaling de la cible (prédire le rendement divisé par sa volatilité, plutôt que le rendement brut, ce qui stabilise l'IC à travers les régimes). Une transformation de réponse bornée — tanh ou la fonction x·exp(−x²/4) de style AHL — évite que le signal ne demande des positions extrêmes aux extrêmes de son support, là où précisément l'estimation est la moins fiable.

Enfin, le *smoothing* du signal (EMA sur quelques jours) fait partie de la normalisation : il arbitre explicitement entre l'IC (qui se dégrade un peu) et le turnover (qui chute beaucoup). Pour un compte prop où les coûts par trade sont proportionnellement plus élevés que pour un fonds, cet arbitrage est souvent *le* déterminant de la rentabilité nette — un signal avec un IC de 0,04 et un turnover de 20× par an bat presque toujours un signal à IC 0,06 et turnover 200×.

Une remarque de cohérence d'ensemble : la normalisation définit implicitement le contrat d'interface avec la branche « combinaison » — tous les alphas arrivent en unités comparables (z-scores bornés, espérance nulle, échelle unitaire), ce qui permet de les pondérer par leur IC sans que l'un domine par simple différence d'échelle. Si tu veux, on peut descendre dans une des sous-branches cliquables (par exemple les alphas de courbe/carry en commodities, qui est probablement la plus directement actionnable pour Blade), ou passer à la branche évaluation pour voir comment on valide tout ça sans se raconter d'histoires.

---

## [M007] Humain — 2026-07-22 18:15:20

ne suppose pas que je travaille exclusivement sur les commodities, je me suis fait virer mais je considère rentrer dans un fond algo sur equity / crypto

---

## [M008] Assistant — 2026-07-22 18:15:28

---

## [M009] Humain — 2026-07-22 18:17:55

ne suppose pas que je travaille exclusivement sur les commodities, je me suis fait virer mais je considère rentrer dans un fond algo sur equity / crypto. je ne dis pas ça pour que tu m aides à me réorienter, mais pour que tu réorientes tes réponses en sachant que c est ce type de sous jacent qui m intéresse en priorité. Ici et dans toute autre de mes interactions avec claude sous mon compte (claude code inclus).

---

## [M010] Assistant — 2026-07-22 18:18:52

> *[Outil : memory_read — /profile.md]*

> *[Outil : memory_str_replace]*

> *[Outil : memory_write — /profile.md]*

C'est noté, et c'est appliqué partout — je cesse de projeter le prisme commodities sur tes questions. Désolé pour la fin de poste ; le côté positif est que le cadre alpha dont on parle est précisément celui des fonds equity/crypto vers lesquels tu regardes.

La réorientation change d'ailleurs matériellement le contenu de la branche « génération » qu'on vient de couvrir, sur trois points structurels :

**Le breadth s'inverse.** En equity cash, l'univers fait 2000-5000 titres liquides : le breadth vient du cross-section, pas du temps. C'est ce qui rend exploitables des IC minuscules (0,01-0,02) et c'est pourquoi tout le cadre WorldQuant/Squarepoint — normalisation cross-sectionnelle, neutralisation Barra, rank-gaussianisation — s'applique littéralement, alors qu'il fallait le tordre pour un desk futures. Les familles dominantes deviennent le reversal court terme (1-5j, l'alpha le plus capacitaire du stat arb), le momentum cross-sectionnel résidualisé, les révisions d'analystes, les accruals et le post-earnings drift, plus toute la microstructure (imbalance carnet, auction dynamics à l'open/close, short interest et coûts d'emprunt).

**Le crypto a des Fₜ qui n'existent nulle part ailleurs.** Les funding rates des perpétuels sont un carry observable en temps réel, réglé toutes les 8h — l'analogue du roll yield mais avec une fréquence et une transparence sans équivalent ; le basis spot-perp-futures datés, structurellement arbitrable. Les données on-chain (flux vers/depuis les exchanges, comportement des cohortes de wallets, SOPR) forment une famille « flux et positionnement » d'une granularité inaccessible en tradfi. La fragmentation entre venues crée des alphas de latence et de lead-lag (Binance mène généralement le price discovery ; les venues moins liquides suivent avec quelques centaines de ms). Et le marché tourne 24/7 sans auctions : la saisonnalité intra-journalière suit les sessions (heures US vs Asie), les expirations d'options Deribit, les resets de funding.

**Les pathologies de données diffèrent.** En equity : biais de survivance (delistings), corporate actions, univers point-in-time. En crypto : wash trading sur les venues de second rang (les volumes affichés sont partiellement fictifs — le nettoyage des données de volume est une étape à part entière), morts de tokens, changements de contrats de perp, historiques courts et non-stationnarité brutale (un backtest crypto pré-2021 décrit un marché qui n'existe plus, dominé par le retail, alors que le marché actuel est largement institutionnalisé sur BTC/ETH mais pas sur les alts — ce qui fait des alts le segment où l'inefficience résiduelle est la plus forte).

Un point d'interface avec ta réflexion de recrutement, sans t'orienter : les fonds diffèrent beaucoup sur l'endroit de l'arbre où ils mettent leurs chercheurs. Les shops equity stat arb classiques recrutent sur la branche génération + évaluation (le « chercheur d'alphas » pur), les fonds crypto natifs valorisent davantage exécution + infra (parce que l'edge y est encore largement opérationnel : connectivité aux venues, gestion du risque de contrepartie exchange, market making). Ça vaut la peine de savoir sur quelle branche tu veux être évalué en entretien.

On peut reprendre l'exploration de l'arbre avec ce nouveau prisme — par exemple redérouler l'évaluation statistique dans le cadre cross-sectionnel equity (où les outils comme le purged k-fold de López de Prado prennent tout leur sens), ou creuser une famille spécifique côté crypto.

---

## [M011] Humain — 2026-07-22 18:26:12

reprendre l'exploration de l'arbre avec ce nouveau prisme — par exemple redérouler l'évaluation statistique dans le cadre cross-sectionnel equity (où les outils comme le purged k-fold de López de Prado prennent tout leur sens) ... l approche arbre doit prédominer dans tout ce chat, c est une excellente idée qui permet de zoom-in et zoom-out. sans jamais perdre de vue la vision d ensemble. je suis impressionné que tu aies eu cette idée.

---

## [M012] Assistant — 2026-07-22 18:27:28

L'arbre restera notre colonne vertébrale, donc — chaque plongée dans une branche s'ouvrira sur sa propre carte locale, pour toujours savoir où on se situe. Nous voici donc dans la deuxième branche « recherche », zoomée avec le prisme cross-sectionnel equity :

> *[Outil : visualize:show_widget — sous_arbre_evaluation_statistique]*

**1. Métriques du signal — la fiche d'identité d'un alpha**

Dans le cadre cross-sectionnel, la métrique élémentaire est le *rank IC par date* : à chaque jour t, la corrélation de Spearman entre le signal αₜ (vecteur sur les N titres) et les rendements réalisés rₜ₊ₕ. On obtient une série temporelle d'IC dont la moyenne mesure le pouvoir prédictif et dont le ratio moyenne/écart-type — l'ICIR — mesure sa régularité. C'est l'ICIR, pas l'IC moyen, qui prédit le Sharpe : un IC de 0,03 stable bat un IC de 0,05 qui alterne +0,15 et −0,05. Le rank plutôt que Pearson est quasi universel en equity : robuste aux outliers et invariant aux transformations monotones du signal.

Le *profil de decay* s'obtient en calculant l'IC pour h = 1, 2, 5, 10, 21 jours : sa forme dicte tout le reste. Un signal dont l'IC culmine à h=1 puis s'effondre est un signal de reversal qui exige une exécution rapide ; un signal dont l'IC est plat sur 21 jours tolère un turnover faible et des coûts minimes. La demi-vie de l'alpha comparée au turnover qu'il génère est le premier filtre de viabilité nette.

Complément indispensable : les *portfolio sorts* — trier l'univers en déciles du signal, mesurer le rendement de chaque décile. On vérifie la monotonie (un vrai signal produit des rendements croissants du décile 1 au décile 10 ; un signal dont seul le décile extrême performe est suspect — souvent un artefact de micro-caps illiquides) et la symétrie long/short (beaucoup d'anomalies vivent entièrement côté short, donc dans les titres chers à emprunter : l'alpha brut existe, l'alpha net non). Enfin, l'*exposition factorielle résiduelle* : régresser les rendements du signal sur les facteurs standards (marché, taille, value, momentum, vol). Ce qui survit à la régression est l'alpha véritable ; le reste est du beta factoriel réempaqueté, que le fonds possède déjà ailleurs.

**2. Backtest cross-sectionnel — la machinerie**

Deux traditions convergentes : les *sorts* (ci-dessus, non paramétriques) et *Fama-MacBeth* — à chaque date, une régression cross-sectionnelle des rendements futurs sur le signal (et les contrôles) ; la série des coefficients estimés est le « rendement du facteur », et un t-test sur sa moyenne (avec correction Newey-West pour l'autocorrélation induite par le chevauchement des horizons) teste la significativité. L'avantage de Fama-MacBeth est de contrôler simultanément plusieurs caractéristiques — indispensable pour prouver qu'un nouveau signal n'est pas un vieux signal déguisé.

La qualité du backtest se joue dans l'univers : *point-in-time* strict (constituants historiques de l'univers à chaque date, delistings inclus avec leur rendement de sortie — exclure les morts fabrique plusieurs points de Sharpe), filtres de liquidité réalistes (ADV minimal, prix minimal), et lag entre le calcul du signal et l'exécution (signal calculé sur la clôture de t, exécuté à l'open ou à la clôture de t+1 — jamais à la clôture de t elle-même, le look-ahead le plus commun). En crypto, la transposition : univers des tokens vivants à chaque date (le survivorship y est féroce — une large fraction des tokens du top 100 de 2021 a disparu ou perdu 95%+), volumes nettoyés du wash trading, et prise en compte des frais de funding dans tout backtest sur perps.

**3. Anti-overfitting — le cœur épistémologique de la branche**

C'est ici que le purged k-fold prend son sens. Le problème qu'il résout : avec un horizon h > 1, les labels se chevauchent — le rendement cible de la date t partage des jours avec celui de t+1, ..., t+h−1. Un k-fold naïf place des observations du train et du test qui partagent de l'information, et la CV surestime systématiquement la performance. La solution de López de Prado : *purger* du train toutes les observations dont le label chevauche temporellement le test, et ajouter un *embargo* (exclure aussi une fenêtre après le test, car la corrélation sérielle des features fuit dans l'autre sens). Le CPCV (combinatorial purged CV) généralise en testant sur toutes les combinaisons de blocs, produisant une distribution de chemins out-of-sample plutôt qu'un chiffre unique.

Le *deflated Sharpe ratio* attaque l'autre versant : le multiple testing. Si tu testes N variantes d'un signal et gardes la meilleure, le Sharpe maximal attendu sous l'hypothèse nulle (aucun signal réel) croît en √(2 ln N) — avec 100 essais, un Sharpe de ~1 émerge du pur bruit. Le DSR recalcule la p-value du Sharpe observé en tenant compte du nombre d'essais, de leur corrélation, de la longueur de l'échantillon et de la non-normalité des rendements (skew, kurtosis). Le corollaire organisationnel est brutal mais salutaire : il faut *logger chaque backtest*, y compris les échecs, car N est un paramètre du test — un chercheur qui ne compte pas ses essais ne peut pas calculer la significativité de ses succès. Le PBO (probability of backtest overfitting, via CSCV) complète : quelle est la probabilité que la configuration optimale in-sample soit sous-médiane out-of-sample ? Au-delà de ces outils, les corrections de type Benjamini-Hochberg (contrôle du FDR) s'appliquent quand on évalue des familles entières de signaux en parallèle — le cadre naturel d'une usine à alphas.

**4. Non-stationnarité et régimes — la validité a une date de péremption**

Un IC moyen sur 15 ans peut masquer un signal mort depuis 5 ans. D'où le *rolling IC* (fenêtre 1-2 ans) inspecté systématiquement, les tests de rupture structurelle, et l'attention au *crowding* : la publication académique d'une anomalie ampute typiquement une grande partie de son rendement (McLean-Pontiff), et les épisodes de déleveraging simultané (août 2007 pour le stat arb equity) révèlent que des signaux décorrélés en temps calme partagent les mêmes détenteurs. En crypto la question est encore plus aiguë : l'histoire utile fait 5-8 ans, traversée de changements de régime majeurs (institutionnalisation post-2020, effondrement des venues type FTX, arrivée des ETF). La réponse pratique : pondérer le récent, valider par régime plutôt qu'en moyenne globale (un signal doit être compris — sur qui gagne-t-il et pourquoi cette contrepartie persiste — pas seulement mesuré), et accepter qu'en crypto le prior économique remplace partiellement la profondeur statistique qu'on n'a pas.

Vue d'ensemble avant de redescendre : cette branche est le *système immunitaire* de l'usine à alphas — la génération propose, l'évaluation dispose, et la sévérité du filtre détermine directement la qualité de ce qui atteint la combinaison. Les quatre sous-nœuds sont cliquables pour zoomer ; sinon on peut remonter à la racine et descendre dans « combinaison d'alphas », la suite logique — comment agréger les survivants du filtre en un forecast unique.

---

## [M013] Humain — 2026-07-22 18:33:30

je ne comprends pas, ton arbre initial était ainsi:

---

## [M014] Assistant — 2026-07-22 18:33:50

Ton message semble s'être coupé après « ainsi : » — mais laisse-moi anticiper la source probable de confusion, car la mise en page de ce premier arbre peut induire en erreur.

Dans ce diagramme, la disposition en deux colonnes encode une *catégorie*, pas un *ordre* : colonne de gauche (teal) = les trois branches de recherche du signal, colonne de droite (coral) = les trois branches de mise en œuvre. Les six nœuds sont tous des enfants directs de la racine, rattachés à la même épine verticale — ce sont des frères, sans hiérarchie entre eux. Si on le lit ligne par ligne (génération → portefeuille → évaluation → exécution...), l'ordre paraît incohérent, car ce n'est pas le sens de lecture voulu : il faut lire colonne par colonne, et l'ordre séquentiel du pipeline est génération → évaluation → combinaison (gauche, de haut en bas), puis portefeuille → exécution (droite), avec infra en support transversal.

Le second diagramme (« Évaluation statistique » avec ses quatre sous-nœuds) est ensuite un zoom sur le nœud milieu-gauche de celui que tu as capturé : sa racine grise correspond exactement à la boîte teal « Évaluation statistique » de l'arbre initial, dépliée d'un niveau.

Si la confusion porte sur autre chose — une incohérence entre le prose et le diagramme, ou un nœud qui a changé de nom entre deux vues — dis-moi, ou renvoie la suite de ton message. Et si tu préfères, je peux redessiner l'arbre racine en disposition strictement séquentielle (les six branches dans l'ordre du pipeline, sans le regroupement en colonnes), pour que la géométrie et la logique coïncident.

---

## [M015] Humain — 2026-07-22 18:38:21

Détaille le feature engineering : transformations, fenêtres, interactions, pièges point-in-time

---

## [M016] Assistant — 2026-07-22 18:39:48

On descend d'un niveau : nous sommes dans génération de signaux → feature engineering, l'atelier où la donnée brute devient un prédicteur candidat. Voici la carte locale :

> *[Outil : visualize:show_widget — sous_arbre_feature_engineering]*

**1. Transformations — de la série brute au prédicteur**

Le point de départ en equity est presque toujours le rendement, et les choix de construction sont déjà des choix de signal. Les rendements multi-horizons (1, 5, 21, 63, 252 jours) forment la base ; la convention « 12-1 » du momentum (rendement sur 12 mois *en excluant le dernier mois*) illustre le principe général : deux effets de signes opposés cohabitent dans la même donnée (momentum à moyen terme, reversal à court terme), et la transformation sert à les séparer plutôt qu'à les laisser se neutraliser.

La transformation la plus puissante du répertoire est la *résidualisation* : au lieu du rendement brut, on utilise le résidu d'une régression rolling contre le marché, le secteur ou un modèle factoriel complet. Le momentum résiduel (Blitz-Huij-Martens) domine le momentum brut parce qu'il retire la composante factorielle du signal — celle qui cause les crashes de momentum lors des retournements de marché — et ne garde que l'information idiosyncratique. Même logique pour le reversal court terme : le reversal sur rendement résiduel (net du mouvement du secteur ce jour-là) est bien plus propre que sur rendement brut, car un titre qui a baissé *avec* son secteur n'a pas de raison particulière de rebondir relativement.

Deux autres principes transversaux : préférer les *changements aux niveaux* (la révision des estimations d'analystes prédit mieux que le niveau des estimations ; la variation du short interest mieux que son stock) — les niveaux sont déjà dans les prix, les changements sont la nouvelle information ; et standardiser les ratios fondamentaux *par groupe de comparables* (un E/P se lit relativement au secteur, sinon le signal « value » devient un simple pari sectoriel permanent sur les banques contre la tech). En crypto : log-rendements obligatoires (les amplitudes rendent les rendements simples non additifs de façon flagrante), et des transformations spécifiques au domaine — funding rate cumulé comme mesure de positionnement spéculatif, ratios on-chain type MVRV (capitalisation marché / capitalisation réalisée, un « prix/coût de base » des détenteurs), flux nets vers les exchanges normalisés par le supply circulant.

**2. Fenêtres et pondération temporelle — la mémoire du signal**

Le choix technique de base : fenêtre plate vs pondération exponentielle. La fenêtre plate a un défaut structurel — quand une observation extrême *sort* de la fenêtre, le signal saute sans qu'aucune information nouvelle ne soit arrivée, générant du turnover pur et des trades sans espérance. L'EMA (paramétrée en demi-vie plutôt qu'en span, plus interprétable) élimine ces discontinuités de sortie ; c'est le défaut raisonnable pour presque toute feature.

L'approche mûre n'est pas de chercher *la* bonne fenêtre mais d'en construire plusieurs : un momentum se décline en demi-vies de 10, 40, 160 jours (le trio de type MACD popularisé par les papiers AHL), et c'est la branche « combinaison » qui pondérera — optimiser la fenêtre unique en backtest est exactement le genre de degré de liberté qui gonfle N dans le deflated Sharpe. Cas particulier important, l'estimation de volatilité (omniprésente : elle normalise les cibles, conditionne les régimes, dimensionne les positions) : l'EWMA sur rendements carrés est le standard, les estimateurs high-low (Parkinson, Garman-Klass) extraient plus d'information des mêmes journées, et en crypto la realized vol sur données intraday est un luxe accessible partout puisque le marché ne ferme jamais — mais attention à la définition de la « journée » (UTC 00:00 est une convention, pas une clôture économique ; les effets de session US/Asie enjambent cette frontière).

**3. Interactions et conditionnement — où le signal devient contextuel**

L'hypothèse d'un IC constant est presque toujours fausse : le reversal court terme est plus fort quand la volatilité est élevée (la compensation pour fournir de la liquidité augmente avec le risque), le momentum s'affaiblit en haute dispersion cross-sectionnelle, les signaux de flux mordent davantage sur les titres à faible profondeur. Le conditionnement exploite cela : multiplier le signal par une fonction du régime, ou en version non paramétrique, les *double sorts* (trier d'abord par la variable de conditionnement, puis par le signal à l'intérieur de chaque groupe) — l'outil standard pour démontrer qu'une interaction est réelle et pas un artefact de corrélation entre les deux variables.

La généralisation moderne passe par le ML non linéaire : un gradient boosting sur un panel de features apprend les interactions sans qu'on les spécifie (le papier de référence est Gu-Kelly-Xiu sur le ML en asset pricing empirique). Le gain est réel mais le prix est double — interprétabilité réduite, et surtout explosion combinatoire de l'espace exploré, qui doit se payer en sévérité de validation (retour direct à la branche évaluation : purged CV et comptage des essais). Deux garde-fous pratiques : les *contraintes de monotonie* (imposer au modèle que le signal reste croissant dans les features où le prior économique l'exige — on garde la non-linéarité, on interdit les oscillations absurdes apprises du bruit), et la règle selon laquelle toute interaction retenue doit avoir une *histoire économique* énonçable en une phrase — qui perd de l'argent de l'autre côté, et pourquoi ça persiste. Une interaction sans histoire compte comme un essai de data mining, pas comme une hypothèse.

**4. Discipline point-in-time — la comptabilité de l'information**

C'est la sous-branche la moins glamour et celle où se fabriquent les faux Sharpe. En equity, les pièges canoniques : les fondamentaux doivent être indexés par leur *date de publication* (filing date), pas par la fin de la période comptable qu'ils décrivent — un bilan du 31 décembre est connu mi-février, et l'utiliser au 1er janvier injecte six semaines de futur ; les *restatements* réécrivent l'historique (il faut les vintages, pas la série finale) ; les prix ajustés des splits et dividendes sont recalculés rétroactivement par les vendeurs de données, donc un ratio prix/seuil calculé sur prix ajustés d'aujourd'hui n'est pas ce qu'on aurait vu à l'époque ; et l'univers lui-même doit être point-in-time, delistings inclus avec leur rendement terminal.

En crypto, les pièges changent de forme mais pas de nature : les exchanges corrigent ou republient des chandelles historiques (stocker soi-même les flux plutôt que re-télécharger l'histoire), les tokens migrent de contrat ou changent de décimales en cassant silencieusement les séries, les données on-chain sont recalculées quand les heuristiques de clustering des wallets s'améliorent (la série MVRV « actuelle » de 2021 n'est pas celle qu'on voyait en 2021), et les timestamps mélangent les fuseaux et les conventions de règlement du funding. Le test canonique qui coiffe tout : l'infrastructure doit permettre de *rejouer* le calcul du signal à une date passée en n'utilisant que le snapshot des données telles qu'elles existaient ce jour-là, et le résultat doit coïncider avec le backtest au bit près. Si cette reproduction échoue, le backtest mesure autre chose que la stratégie.

Pour situer dans l'ensemble : cette branche produit les candidats que l'évaluation (qu'on a déjà couverte) va filtrer — et tu vois que les deux communiquent en permanence, chaque degré de liberté pris ici étant une dette à rembourser là-bas. Les quatre nœuds sont cliquables pour zoomer encore ; les suites naturelles en largeur sont la sous-branche sœur « normalisation » (dernier étage du pipeline de génération) ou la remontée vers « combinaison d'alphas », qu'on n'a pas encore ouverte.

---

## [M017] Humain — 2026-07-22 18:43:47

Détaille les transformations : rendements multi-horizons, résidualisation factorielle, ratios, changements vs niveaux

---

## [M018] Assistant — 2026-07-22 18:45:27

Nouveau cran de zoom : génération → feature engineering → transformations. La carte locale, avec les quatre familles de transformations :

> *[Outil : visualize:show_widget — sous_arbre_transformations]*

**1. Rendements multi-horizons — la décomposition temporelle du prix**

L'idée fondatrice : un rendement cumulé est une somme télescopique de sous-périodes, et les sous-périodes portent des informations de *signes opposés*. Le rendement 12 mois se décompose en r(t−252, t−21) + r(t−21, t) : la première composante prédit positivement (momentum, sous-réaction à l'information fondamentale), la seconde négativement (reversal, sur-réaction aux chocs de liquidité). Le momentum « 12-1 » n'est donc pas une convention arbitraire mais une chirurgie : utiliser le rendement 12 mois brut, c'est additionner un signal et son antidote. Novy-Marx a poussé la dissection plus loin en montrant que l'essentiel du pouvoir prédictif loge dans la partie *ancienne* de la fenêtre (le rendement des mois 12 à 7 bat celui des mois 6 à 2) — controversé sur sa robustesse hors échantillon US, mais illustratif de la démarche : traiter l'axe temporel du rendement passé comme un spectre dont chaque bande a son propre IC, mesurable séparément.

Au-delà du découpage, les *reparamétrisations* du chemin : le momentum ajusté de la volatilité (rendement/vol réalisée — un titre monté de 30% en ligne droite et un monté de 30% en dents de scie ne portent pas la même information), la fraction de jours positifs sur la fenêtre (l'« information discreteness » de Da-Gurun-Warachka : le momentum issu d'une dérive régulière persiste mieux que celui issu de quelques sauts, cohérent avec une histoire de sous-réaction à un flux continu d'information), et la distance au plus haut 52 semaines (un ancrage comportemental : les titres proches de leur plus haut voient leur bonne nouvelle sous-incorporée car les investisseurs hésitent à « acheter au plus haut »). En crypto, la même grammaire avec des horizons compressés : le time-series momentum vit sur 1 à 4 semaines plutôt que 6 à 12 mois, le reversal court terme sur des heures à quelques jours, et — spécificité structurelle — le rendement pertinent d'une position en perpétuel est le rendement *funding inclus* : un token flat en prix avec un funding à −0,05% par 8h a rapporté du carry substantiel au short ; ignorer cette composante fausse à la fois les features et les cibles.

**2. Résidualisation factorielle — isoler la composante idiosyncratique**

La mécanique : régression rolling (ou EWMA) des rendements du titre sur des facteurs — rᵢ,ₜ = βᵢ'Fₜ + εᵢ,ₜ — puis on construit la feature sur les εᵢ,ₜ (cumulés pour un momentum résiduel, instantanés pour un reversal résiduel). Le choix du modèle factoriel est un curseur : marché seul, marché + secteurs, modèle commercial complet (Barra), ou facteurs statistiques par PCA. Plus le modèle est riche, plus le résidu est « pur » — et plus le signal résultant est orthogonal aux primes de risque que le portefeuille détient déjà par ailleurs, ce qui augmente sa valeur *marginale* dans la combinaison même à IC égal.

Pourquoi ça marche si bien sur le momentum : le momentum brut d'un titre est en grande partie du momentum de son beta (un titre à beta 1,5 dans un marché haussier a mécaniquement un « bon momentum »), et cette composante-là est précisément celle qui se retourne violemment dans les rebonds de marché — les crashes de momentum de 2009 ou 2020 sont des crashes du momentum *factoriel*. Le momentum résiduel garde la sous-réaction à l'information spécifique du titre et jette le pari factoriel déguisé : ICIR supérieur, drawdowns amputés. Même chose pour le reversal : un titre qui a baissé de 3% quand son secteur baissait de 3% n'a subi aucun choc spécifique, donc n'a rien à « reverser » ; le reversal résiduel concentre le signal sur les vrais chocs idiosyncratiques, là où la fourniture de liquidité est effectivement rémunérée.

Les précautions : les betas estimés sont bruités, et résidualiser avec des betas bruités *injecte* du bruit — d'où le shrinkage des betas vers 1 ou vers la moyenne sectorielle (à la Vasicek), et des fenêtres d'estimation qui arbitragent réactivité contre variance. Et un piège point-in-time subtil : des facteurs PCA estimés sur l'échantillon complet contiennent le futur (la structure de corrélation de 2020 « connaît » le Covid) ; les facteurs statistiques doivent être ré-estimés en expanding window comme n'importe quelle feature. En crypto, la résidualisation naturelle est contre BTC et ETH — la paire qui joue le rôle du « marché » — mais les betas y sont remarquablement instables (le beta d'un alt contre BTC change de régime en quelques semaines), ce qui pousse vers des fenêtres courtes, du shrinkage agressif, ou des approches par rangs qui contournent l'estimation de beta. Poussée à sa limite, la résidualisation devient le stat arb classique : les résidus de cointégration d'une paire ou d'un panier ne sont qu'une résidualisation où le « facteur » est l'autre jambe.

**3. Ratios et standardisation — rendre les grandeurs comparables**

Un fondamental brut (bénéfice, book value, volume) n'est pas cross-sectionnellement comparable ; le ratio est ce qui le transforme en signal. Détails de construction qui comptent : préférer E/P à P/E (quand le bénéfice traverse zéro, P/E explose et change de signe de façon discontinue, E/P reste continu et ordonnable), préférer les mesures *hautes* du compte de résultat (la gross profitability de Novy-Marx — marge brute/actifs — prédit mieux que le résultat net, car moins polluée par les choix comptables et les éléments exceptionnels), et traiter les dénominateurs proches de zéro par des rangs ou un signed-log plutôt que de laisser trois micro-caps dominer la queue de distribution.

Le choix de standardisation est un choix de *pari* : un E/P comparé à tout l'univers fait de « value » un pari structurel long banques/énergie contre tech ; un E/P standardisé within-secteur (z-score par industrie GICS) parie sur les titres décotés *relativement à leurs comparables* — deux signaux différents, avec des profils de risque différents, et le second est presque toujours celui qu'on veut dans un portefeuille neutralisé par ailleurs. Côté ratios techniques : prix/moyenne mobile (une reparamétrisation du momentum), volume relatif (volume du jour / ADV — un détecteur d'événement générique), et l'illiquidité d'Amihud |r|/volume monétaire, à la fois signal (prime d'illiquidité) et variable de conditionnement (l'impact attendu de ses propres trades). En crypto, les ratios sont le cœur de l'analyse on-chain : MVRV (valeur de marché / valeur réalisée — le prix moyen d'acquisition de chaque coin au moment de son dernier mouvement, un « cost basis » agrégé dont les extrêmes marquent les zones de capitulation et d'euphorie), NVT (capitalisation / volume on-chain transféré, un « P/E » où les transactions jouent le rôle des bénéfices), et le ratio volume réel / volume reporté par venue — qui est autant un filtre de qualité de données qu'une feature.

**4. Changements vs niveaux — extraire l'innovation**

Le principe théorique découle directement de la définition racine de l'arbre : si αₜ ≈ E[rₜ₊ₕ | Fₜ], alors ce qui prédit doit être ce qui n'est *pas encore* dans les prix — et un niveau public et stable a eu tout le temps d'y entrer. Le contenu prédictif se loge dans l'innovation : la composante surprise du dernier point de donnée. La forme canonique est le SUE (standardized unexpected earnings) : (réalisé − attendu) / écart-type des surprises passées, où l'« attendu » vient du consensus des analystes ou d'un modèle de série temporelle. Le post-earnings announcement drift — la dérive qui suit la surprise pendant des semaines — est l'illustration historique que le marché sous-réagit aux innovations, pas aux niveaux. La même logique produit les révisions d'estimations (le *changement* du consensus, plus puissant que son niveau), le delta du short interest, les changements de recommandations, et en crypto les deltas de flux vers les exchanges, l'accélération du funding (sa dérivée signale la construction de levier plus finement que son niveau), ou les changements de dominance BTC.

La distinction n'est pourtant pas un dogme, et savoir quand elle cède est aussi important : certains niveaux prédisent durablement — la profitabilité, la qualité de bilan, l'illiquidité. La grille de lecture : un *changement* prédit via la sous-réaction (le marché met du temps à digérer l'innovation ; l'alpha decay est rapide, semaines), un *niveau* prédit via une prime de risque ou une friction persistante (le marché rémunère en continu le fait de porter cette caractéristique ; le decay est lent, années). Les deux sont des alphas au sens de la racine, mais tout diffère en aval — turnover, capacité, crowding, et la branche de l'arbre où on ira les combiner.

On est ici à trois niveaux de profondeur — les nœuds restent cliquables si tu veux forer jusqu'aux papiers et aux formules d'une transformation précise. En largeur, les sœurs immédiates sont « fenêtres », « interactions » et « point-in-time » ; en remontant de deux crans, les grandes branches encore vierges sont la combinaison d'alphas et toute la moitié mise en œuvre de l'arbre.

---

## [M019] Humain — 2026-07-22 18:54:21

Détaille le feature engineering : transformations, fenêtres, interactions, pièges point-in-time

---

## [M020] Assistant — 2026-07-22 18:54:32

Ce nœud a déjà été déplié — c'est probablement un re-clic sur le diagramme du pipeline, dont les boîtes restent actives. La carte et le détail complet (transformations, fenêtres et demi-vies, interactions et conditionnement, discipline point-in-time) sont trois messages plus haut, et on a même déjà foré un cran plus bas dans « transformations » avec les quatre familles (multi-horizons, résidualisation, ratios, changements vs niveaux).

Plutôt que de te le resservir, voici où sont les chemins encore inexplorés depuis ce point de l'arbre : en profondeur, les trois sous-nœuds sœurs de « transformations » n'ont pas encore été dépliés au même niveau de détail — fenêtres et pondération temporelle, interactions et conditionnement, discipline point-in-time ont chacun un étage de plus en dessous (par exemple, sous « interactions », le sous-arbre ML avec Gu-Kelly-Xiu, les contraintes de monotonie et le traitement des interactions comme essais multiples mériterait sa propre carte). En largeur, la sous-branche « normalisation » fermerait le pipeline de génération, et en remontant à la racine, « combinaison d'alphas » est la grande branche recherche encore vierge — sans parler de toute la moitié mise en œuvre.

Dis-moi où tu veux zoomer, ou si tu préfères que je redessine la carte globale avec un marquage des nœuds déjà visités pour qu'on voie l'état d'avancement de l'exploration.

---

## [M021] Humain — 2026-07-22 18:56:03

redessine la carte globale

---

## [M022] Assistant — 2026-07-22 18:57:40

Voici l'état d'avancement de l'exploration, en vue dépliée — la profondeur d'indentation reflète la profondeur dans l'arbre :

> *[Outil : visualize:show_widget — carte_globale_etat_exploration]*

Lecture rapide de l'état : on a foré profondément dans la moitié « recherche » — la lignée génération → feature engineering → transformations est descendue sur trois niveaux, et l'évaluation statistique est couverte en détail un cran en dessous. Les nœuds violets ont reçu un traitement substantiel en prose mais n'ont pas encore leur propre carte avec leurs sous-sous-branches. Toute la moitié « mise en œuvre » (combinaison comprise, qui est à cheval entre les deux) reste vierge.

Deux remarques stratégiques sur la suite du parcours : la combinaison d'alphas est le pont naturel — c'est le seul grand nœud gris dont tout l'amont est déjà exploré, donc le déplier maintenant maximise la continuité. Et si l'objectif de fond est la préparation aux entretiens de fonds equity/crypto, la profondeur atteinte côté recherche est déjà celle qu'on attend d'un candidat chercheur ; la moitié mise en œuvre (portefeuille, exécution) est en revanche celle où les questions d'entretien distinguent les candidats qui ont fait tourner de l'argent réel de ceux qui ont seulement backtesté. Chaque nœud de la carte est cliquable — à toi de choisir la direction.

---

## [M023] Assistant — 2026-07-22 19:01:31

Voici la carte globale mise à jour avec l'état d'avancement — la couleur encode désormais la progression de l'exploration, et le bandeau du bas montre le chemin foré en profondeur :

> *[Outil : visualize:show_widget — carte_globale_avancement]*

Deux changements par rapport à la version initiale : les branches sont maintenant numérotées dans l'ordre logique du pipeline (1→2→3 côté recherche, 4→5→6 côté mise en œuvre), ce qui lève l'ambiguïté de lecture qui t'avait gêné, et la couleur encode la progression plutôt que la catégorie.

L'état des lieux se résume ainsi : la moitié recherche est aux deux tiers couverte — génération est la branche la plus profondément forée (jusqu'aux transformations et leurs quatre sous-familles), évaluation a ses quatre sous-nœuds cartographiés et détaillés en prose mais aucun n'a encore été foré individuellement. La frontière d'exploration compte donc trois types de mouvements possibles : boucher les trous en profondeur (normalisation pour clore le pipeline de génération ; les sœurs de feature engineering ; un sous-nœud d'évaluation comme l'anti-overfitting qui mérite ses propres formules), ouvrir la dernière branche recherche (combinaison d'alphas — la suite logique puisqu'elle consomme ce que les deux premières produisent), ou traverser vers la moitié mise en œuvre, entièrement vierge, où portefeuille & risque serait l'entrée naturelle.

Tout est cliquable — y compris les nœuds du chemin foré en bas, qui mènent aux sœurs non visitées. Mon vote, si tu le veux : combinaison d'alphas, pour boucler la moitié recherche avant de franchir l'interface vers la mise en œuvre.

---

## [M024] Humain — 2026-07-22 19:04:06

Détaille les fenêtres et la pondération temporelle : EMA vs fenêtres plates, multi-échelles, estimation de volatilité

---

## [M025] Assistant — 2026-07-22 19:05:44

Cran de zoom sur la deuxième sous-branche du feature engineering : génération → feature engineering → fenêtres & pondération temporelle. La carte locale :

> *[Outil : visualize:show_widget — sous_arbre_fenetres_ponderation]*

**1. EMA vs fenêtres plates — la forme de la mémoire**

La fenêtre plate donne un poids 1/n aux n dernières observations, puis zéro. Ce profil rectangulaire a une pathologie structurelle : quand une observation extrême franchit le bord arrière de la fenêtre, l'estimateur saute — le signal change alors qu'*aucune information nouvelle n'est arrivée*. Concrètement, un momentum 252 jours peut basculer de long à short le jour où le krach d'il y a un an sort de la fenêtre ; le trade déclenché a une espérance nulle par construction et un coût réel. L'EMA, avec ses poids λᵏ décroissants, n'a pas de bord : chaque observation s'éteint continûment. On la paramètre en *demi-vie* h (λ = exp(−ln 2 / h)) plutôt qu'en span ou en λ brut — « la moitié du poids porte sur les h derniers jours » est une phrase qu'on peut raisonner, λ = 0,997 non.

La comparaison rigoureuse se fait à retard égal : le retard moyen d'une fenêtre plate de n jours est (n−1)/2, celui d'une EMA est λ/(1−λ) ≈ h/ln 2 − ½. À retard apparié, la fenêtre plate est l'estimateur de variance minimale *si la quantité estimée est constante* — mais c'est précisément l'hypothèse fausse en finance. La lecture state-space éclaire tout : l'EWMA est le filtre de Kalman en régime permanent du modèle où le paramètre sous-jacent (l'espérance, la vol) suit une marche aléatoire observée avec bruit. Autrement dit, choisir l'EMA n'est pas un choix esthétique, c'est déclarer que le monde dérive — et sa demi-vie optimale est déterminée par le ratio entre la vitesse de dérive du paramètre et le bruit d'observation. Deux détails pratiques : le *warm-up* (les premières valeurs d'une EMA sont dominées par l'initialisation — soit on tronque, soit on renormalise par la somme des poids effectivement disponibles), et le fait que le turnover d'un signal EMA se calcule analytiquement à partir de sa demi-vie, ce qui permet de budgéter les coûts avant même de backtester.

**2. Multi-échelles — le banc de filtres**

L'erreur méthodologique classique est de chercher *la* bonne fenêtre par grid search — chaque valeur testée incrémente le compteur N du deflated Sharpe, et la « meilleure » fenêtre in-sample est presque toujours un artefact d'échantillon. L'approche mûre : construire un *banc* de demi-vies espacées géométriquement (8, 16, 32, 64, 128 jours — l'espacement géométrique, pas arithmétique, car l'information est approximativement log-uniforme en fréquence) et déléguer la pondération à la branche combinaison, qui mesurera l'IC de chaque échelle et les agrégera.

La référence canonique est le trend-following à la AHL (Baz et al., « Dissecting Investment Strategies ») : trois croisements de moyennes exponentielles avec les paires de demi-vies (8, 24), (16, 48), (32, 96), chacun normalisé par la volatilité du prix, puis passé dans la réponse non linéaire x·exp(−x²/4) qui sature et se retourne aux extrêmes. La lecture en traitement du signal est la bonne : la *différence* de deux EMA est un filtre passe-bande — elle annule les composantes très lentes (que les deux EMA capturent identiquement) et les très rapides (que les deux lissent), isolant une bande de fréquences du spectre du prix. Le banc multi-échelles est donc une décomposition spectrale grossière du processus de prix, cousin pauvre mais robuste des ondelettes, et la question « quelle fenêtre ? » devient la question mesurable « quelles bandes de fréquence portent de l'IC ? ». Réponse empirique typique : en equity cross-sectionnel, les bandes lentes portent le momentum et les rapides le reversal, avec une zone morte au milieu ; en crypto, tout le spectre est décalé vers les hautes fréquences — les bandes qui correspondraient à des demi-vies de plusieurs mois en actions vivent sur des semaines.

**3. Estimation de volatilité — l'estimateur le plus consommé de la stack**

La vol apparaît partout : au dénominateur des cibles (vol-scaling), dans les z-scores, dans le sizing, dans les variables de régime — c'est la feature dont la qualité se propage à tout le système. La base est l'EWMA sur rendements carrés (l'héritage RiskMetrics, λ = 0,94 en daily, soit une demi-vie d'environ 11 jours), avec une subtilité d'usage : des demi-vies différentes pour des rôles différents — courte (5-20 j) pour le sizing qui doit réagir, longue (60-120 j) pour la définition de régimes qui doit être stable. Utiliser la même estimation partout couple des décisions qui ne devraient pas l'être.

Les estimateurs *range-based* extraient plus d'information des mêmes journées : Parkinson (à partir du high-low, environ 5 fois plus efficace que le close-to-close, car le range d'un brownien renseigne davantage sur σ que son point d'arrivée), Garman-Klass (OHLC complet), Rogers-Satchell (robuste au drift — important pour les titres en tendance forte), et Yang-Zhang, qui combine composante overnight et intraday et gère les gaps — l'estimateur par défaut raisonnable en equity, où le gap d'ouverture est une part majeure de la variance totale. Au-delà, la *realized volatility* : somme des rendements carrés intraday (échantillonnés à ~5 minutes — en dessous, le bruit de microstructure et le bid-ask bounce biaisent vers le haut). En crypto, la RV est un luxe démocratisé : marché 24/7, pas de gap overnight sur les perps, données tick accessibles — il n'y a aucune raison de se contenter d'un close-to-close. Deux pièges spécifiques : l'annualisation (√252 en equity, √365 en crypto — mélanger les conventions fausse silencieusement tous les ratios de 20%) et les venues (la vol mesurée sur une venue à faible profondeur est contaminée par son propre bruit de microstructure ; mesurer sur la venue directrice ou sur un prix composite).

**4. Fréquence et horizon — la cohérence de la grille temporelle**

Règle d'ordre de grandeur : la demi-vie des features doit être commensurable avec l'horizon h du signal — prédire h = 21 jours avec des features de demi-vie 2 jours produit un signal dont le turnover détruit l'edge, l'inverse produit un signal en retard permanent. Et la symétrie avec la branche évaluation est directe : dès que h > 1 avec des features quotidiennes, les observations se chevauchent — c'est exactement l'autocorrélation des labels qui exigeait le purging et Newey-West ; le choix de grille fait ici détermine la sévérité de la correction là-bas.

L'agrégation intraday → daily est la façon d'enrichir la grille quotidienne sans la quitter : imbalance moyen du carnet, part du volume en fin de séance, RV, asymétrie du profil de volume — des features quotidiennes *fabriquées* à partir de la microstructure. En equity, la décomposition la plus féconde de la journée est overnight vs intraday : ce sont deux régimes économiques distincts (le rendement overnight concentre la dérive et les réactions aux annonces, l'intraday concentre le reversal et les flux), et beaucoup de signaux ont des IC de signes différents sur les deux segments — les traiter comme deux « fenêtres » séparées est une transformation à part entière. En crypto, la journée UTC est une pure convention (aucune clôture économique à minuit UTC), mais le marché a ses grilles naturelles : le funding des perps toutes les 8 heures (00/08/16 UTC) crée des points de synchronisation où le positionnement se règle, les sessions US/Asie structurent la liquidité intra-journalière, et les week-ends — sans être fermés — sont des régimes de profondeur réduite où les mêmes signaux ont des coûts et des IC différents. Les features calendaires (heure de session, distance au prochain funding, jour de semaine) ne sont pas du folklore : elles conditionnent des différences de régime mesurables.

Nous voilà au même niveau de profondeur que « transformations » — il reste deux sœurs non forées sous feature engineering (interactions, point-in-time), la normalisation pour clore le pipeline de génération, et toujours combinaison d'alphas comme prochaine grande branche, vers laquelle ce nœud-ci pointe d'ailleurs deux fois (le banc multi-échelles et le spectre d'IC par bande sont des inputs directs de la combinaison).

---

## [M026] Humain — 2026-07-22 19:06:52

Détaille les interactions et le conditionnement : régimes, double sorts, non-linéarités ML, coût en degrés de liberté

---

## [M027] Assistant — 2026-07-22 19:08:34

On fore la troisième sœur : génération → feature engineering → interactions & conditionnement. La carte locale :

> *[Outil : visualize:show_widget — sous_arbre_interactions_conditionnement]*

**1. Conditionnement par régime — l'IC n'est pas une constante**

Le point de départ empirique : le pouvoir prédictif de presque tous les signaux varie avec l'état du marché, et cette variation a souvent une logique économique. Le reversal court terme paie davantage en haute volatilité — c'est la rémunération de la fourniture de liquidité, et le prix de la liquidité monte avec le risque de la porter. Le momentum s'affaiblit aux points de retournement et en haute dispersion cross-sectionnelle, et son fameux crash est concentré dans les rebonds qui suivent les krachs (le short du momentum devient un short de titres à beta élevé au pire moment). Le carry, dans toutes ses incarnations, gagne petit en régime calme et perd gros en risk-off. Ignorer ces conditionnements, c'est laisser de l'ICIR sur la table ; les modéliser, c'est ouvrir un espace de sur-apprentissage — d'où l'importance de la *forme*.

La forme recommandable est multiplicative et lisse : α_conditionné = α × g(z), où z est la variable de régime (z-score de vol, de dispersion, de liquidité agrégée) et g une fonction douce — sigmoïde, rampe saturée — plutôt qu'un seuil dur. Le seuil dur (« couper le momentum si VIX > 30 ») a trois défauts : il crée des discontinuités de position (trades violents quand z oscille autour de la frontière), le niveau du seuil est un degré de liberté caché optimisé sur une poignée d'épisodes historiques, et il jette l'information ordinale de z. L'alternative par commutation explicite (HMM, Markov-switching) est séduisante conceptuellement mais souffre du *lag de détection* : le régime est identifié avec retard, précisément quand son exploitation ne vaut plus rien — et la version filtrée en temps réel d'un HMM ressemble beaucoup à... une fonction lisse d'un z-score. Règle transversale : la variable de régime est une feature comme une autre, soumise à la même discipline point-in-time (un régime défini avec la vol *future* de l'épisode est le look-ahead le plus élégamment déguisé du répertoire). En crypto, les conditionnements naturels : le niveau et le signe du funding agrégé (un marché à funding extrême positif est un marché où le levier long est empilé — le reversal y mord plus fort), la dominance BTC (les alphas cross-sectionnels sur alts changent de nature selon que le marché est en phase BTC ou en phase alts), et la corrélation réalisée BTC-Nasdaq, qui commute entre des régimes où le crypto est un actif macro et des régimes où il vit sa vie propre.

**2. Double sorts — l'interaction sans forme fonctionnelle**

L'outil non paramétrique canonique, hérité de Fama-French : trier l'univers en quintiles de la variable conditionnante z, puis, *à l'intérieur* de chaque quintile, en quintiles du signal α — 25 cellules, et le spread long-short du signal calculé quintile de z par quintile de z donne le profil complet de l'IC conditionnel, sans imposer de forme à g. Si le spread du reversal croît monotonement du quintile bas-vol au quintile haute-vol, l'interaction est établie ; si elle n'apparaît que dans une cellule, c'est du bruit.

La distinction technique qui compte : sorts *indépendants* (les deux tris faits séparément sur tout l'univers, puis intersection) vs *conditionnels* (tri séquentiel, z d'abord, α dans chaque groupe). Quand α et z sont corrélés — le cas fréquent : la plupart des signaux sont corrélés à la taille ou à la vol — les sorts indépendants produisent des cellules quasi vides (il n'y a presque pas de titres à la fois petits et très liquides), aux rendements dominés par trois noms ; les sorts conditionnels garantissent des cellules équi-peuplées et répondent à la question qu'on pose réellement : « le signal marche-t-il *à z donné* ? ». C'est aussi le test qui départage une vraie interaction d'une simple corrélation de caractéristiques — si « le momentum marche mieux sur les titres illiquides » disparaît en sort conditionnel, c'était juste que momentum et illiquidité sélectionnaient les mêmes titres. La limite est le breadth : 25 cellules exigent un univers de plusieurs milliers de titres pour que chaque cellule soit diversifiée. En crypto, avec 150-300 tokens investissables, on rétrograde en 3×3, et encore — c'est une des raisons structurelles pour lesquelles la recherche crypto s'appuie davantage sur les priors et moins sur la granularité statistique.

**3. Non-linéarités ML — apprendre les interactions au lieu de les spécifier**

Le résultat de référence est Gu-Kelly-Xiu (« Empirical Asset Pricing via Machine Learning ») : sur le panel US complet, les gradient boosted trees et les réseaux peu profonds dominent nettement les modèles linéaires, et la décomposition du gain montre qu'il vient *majoritairement des interactions* — momentum × liquidité, value × taille, signaux × état macro — précisément ce que le linéaire ne peut pas représenter et que le chercheur ne peut pas énumérer. Le message pratique n'est pas « les NN profonds gagnent » (ils ne gagnent pas : au-delà de 2-3 couches, la performance se dégrade sur données financières — le ratio signal/bruit ne finance pas la profondeur) mais « les arbres boostés peu profonds avec régularisation lourde sont l'outil de découverte d'interactions ».

La discipline d'usage : cibles en rangs ou z-scores cross-sectionnels (jamais les rendements bruts — le modèle passerait sa capacité à apprendre la vol), profondeur d'arbre 3-4 (une profondeur d, c'est des interactions d'ordre ≤ d ; l'ordre 2-3 suffit et au-delà on modélise le bruit), subsampling agressif des features et des observations, et *ensembling sur les seeds* — la variance entre deux runs identiques à seed différente est un diagnostic gratuit : si elle est du même ordre que l'IC, le modèle raconte du bruit. Les *contraintes de monotonie*, natives dans XGBoost/LightGBM, sont le pont entre le ML et les priors : imposer que la prédiction reste croissante en E/P ou en momentum résiduel garde la liberté sur les interactions tout en interdisant les zigzags appris de l'échantillon. Enfin l'interprétation — SHAP values, partial dependence sur les paires — n'est pas cosmétique : une interaction *découverte* par le modèle a le statut d'hypothèse, pas de résultat ; le geste correct est de l'extraire, la reformuler comme feature explicite avec une histoire économique, et la re-tester isolément en out-of-sample. Le modèle ML comme générateur d'hypothèses, pas comme boîte de production — c'est la position de la plupart des desks sérieux, et elle enchaîne directement sur le quatrième nœud.

**4. Coût en degrés de liberté — la comptabilité de l'exploration**

C'est la sous-branche qui donne son prix à tout le reste. Chaque choix fait dans ce message — la forme de g, le nombre de quintiles, la profondeur des arbres, chaque hyperparamètre — est un essai, et l'espace des interactions explose combinatoirement : p features offrent p(p−1)/2 paires, chacune déclinable en plusieurs formes. Le lien quantitatif avec la branche évaluation est direct : le Sharpe maximal attendu sous l'hypothèse nulle croît en √(2 ln N), donc explorer 1000 configurations *fabrique* un Sharpe de ~1,2 à partir de rien, et le deflated Sharpe exige N en entrée. Subtilité importante : les essais corrélés comptent moins — mille variantes d'un même momentum ne font pas mille essais indépendants — et le N *effectif* s'estime à partir de la corrélation moyenne entre les backtests de la famille explorée ; c'est plus favorable que le comptage brut, mais seulement si on a effectivement loggé les essais pour pouvoir le calculer.

D'où la hiérarchie de crédibilité qui structure la pratique : au sommet, l'interaction *pré-spécifiée* — hypothèse économique écrite avant le test, forme et paramètres fixés par défaut raisonnable plutôt qu'optimisés, un seul backtest qui confirme ou infirme (le pré-enregistrement, importé de la recherche clinique, existe informellement dans les meilleurs desks : le document d'hypothèse date d'avant les résultats). Au milieu, l'interaction découverte par ML puis re-testée comme hypothèse explicite sur données non utilisées par la découverte. En bas, le grid search assumé, qui n'est acceptable que passé au DSR avec son vrai N. Et la ressource ultime qui contraint tout : les données out-of-sample sont *non renouvelables* — chaque regard sur le holdout le consomme un peu (le « holdout » regardé dix fois est devenu un training set), d'où la règle du holdout intouchable qu'on n'ouvre qu'une fois, en toute fin, sur la version finale. En crypto, où l'histoire utile fait cinq ans, ce budget est dramatiquement plus serré : la tentation de tout tester sur tout est maximale exactement là où on peut se le permettre le moins.

Le sous-arbre feature engineering est maintenant foré aux trois quarts — il ne reste que « discipline point-in-time » (dont on a déjà semé l'essentiel en traversant les autres nœuds). Ce nœud-ci aura été le plus connecté de tous : il pointe vers l'évaluation (DSR, N effectif), vers la combinaison (que faire des IC conditionnels par bande et par régime), et il pose la question organisationnelle du logging des essais qui appartient à la branche infra. Prochain mouvement à ta main — clore le point-in-time, ouvrir la normalisation, ou enfin franchir vers la combinaison d'alphas.

---

## [M028] Humain — 2026-07-22 19:13:29

Détaille la discipline point-in-time : lags de publication, vintages, corporate actions, pièges spécifiques crypto

---

## [M029] Assistant — 2026-07-22 19:14:45

Dernière sœur du sous-arbre feature engineering : génération → feature engineering → discipline point-in-time. La carte locale :

> *[Outil : visualize:show_widget — sous_arbre_point_in_time]*

**1. Lags de publication — dater l'information par son arrivée, pas par son objet**

Le principe unique : chaque donnée porte deux dates — la période qu'elle *décrit* et le moment où elle devient *connaissable* — et seule la seconde compte pour construire Fₜ. En equity, l'écart entre les deux est massif : un bilan clos au 31 décembre est déposé mi-février (10-K américain : jusqu'à 60-90 jours selon la taille de la société), et indexer les fondamentaux par leur date de période injecte six à douze semaines de futur. La convention académique paresseuse — un lag forfaitaire de 3 ou 6 mois à la Fama-French — est conservatrice mais destructrice d'information : elle rate le drift post-publication qui vit précisément dans les semaines suivant le dépôt. La bonne pratique est le *filing date* réel titre par titre (disponible via EDGAR ou les bases point-in-time des vendeurs), avec une subtilité : l'information fuit souvent *avant* le dépôt formel via le communiqué de résultats — pour les signaux d'earnings, la date pertinente est celle de l'annonce, pas du filing.

Les autres flux ont chacun leur calendrier : les estimations d'analystes arrivent en continu mais les agrégateurs consolident avec un délai de traitement (le consensus « du jour » chez certains vendeurs intègre des révisions saisies le lendemain — il faut la date d'*enregistrement* dans la base, pas la date de la révision), le short interest américain est publié deux fois par mois avec ~9 jours ouvrés de retard (la donnée « du 15 » est connaissable vers le 25), les données de prêt-emprunt quotidiennes ont leur propre latence contractuelle, et la macro (CPI, NFP) a des heures de publication à la seconde près qui comptent dès qu'on descend en intraday. La règle opérationnelle : chaque table de la base de features porte une colonne « connaissable à partir de », renseignée par flux, et aucune jointure temporelle ne se fait sur une autre colonne que celle-là.

**2. Vintages et révisions — la donnée n'est pas immuable, il faut stocker ses états successifs**

Deuxième couche du problème : même correctement datée à l'arrivée, une donnée peut être *réécrite* ensuite. Les restatements comptables remplacent les chiffres historiques dans les bases courantes — la série « finale » d'une société qui a restaté ses comptes contient une information (la fraude découverte, l'erreur corrigée) que le marché n'avait pas à l'époque, et un signal de qualité comptable backtesté sur données restatées est structurellement embelli : il « détecte » les fraudes avec les chiffres d'après la détection. La macro est pire encore : le PIB et l'emploi sont révisés sur des années, et l'écart premier-jet / série finale est parfois du même ordre que le signal qu'on cherche — la recherche sérieuse sur signaux macro utilise les bases de vintages (type ALFRED de la Fed de St. Louis) où chaque observation existe en autant de versions qu'il y a eu de publications.

La réponse architecturale est la base *bitemporelle* : chaque enregistrement porte la date de l'événement ET la date de validité de cette version de l'enregistrement, et toute requête historique se fait « telle que la base était au jour t ». Concrètement, pour un desk qui démarre : snapshotter quotidiennement les tables critiques coûte du stockage trivial et rend le problème soluble rétroactivement ; ne pas le faire rend certains backtests *définitivement impossibles à assainir*, car les vintages perdus ne se reconstituent pas. C'est un des rares points de tout l'arbre où une décision d'infrastructure prise au jour 1 conditionne la validité de la recherche des années suivantes — le pont avec la branche infra est ici structurel, pas anecdotique.

**3. Corporate actions et continuité des séries — l'identité des titres est une donnée**

Les prix « ajustés » des splits et dividendes sont recalculés rétroactivement à chaque nouvel événement : le facteur d'ajustement d'aujourd'hui réécrit toute l'histoire du titre, donc toute feature qui compare un prix à un seuil absolu (le filtre « prix > 5$ », la distance à un strike, un niveau rond) doit être calculée sur prix *bruts* contemporains, pas sur la série ajustée téléchargée aujourd'hui. Les dividendes eux-mêmes créent une bifurcation : rendement total vs rendement prix ne diffèrent que de ~2% par an en moyenne, mais systématiquement et avec une structure cross-sectionnelle (les value stocks paient plus) — un backtest de value sur rendements prix sous-estime le facteur.

La continuité de l'identité est l'autre versant : les tickers sont réutilisés (un ticker mort réattribué à une autre société colle deux histoires sans rapport), les fusions et spin-offs exigent des règles de succession explicites, et l'univers doit inclure les morts avec leur *rendement terminal* — le delisting return, souvent −30% à −100%, dont l'omission est le biais de survivance au sens strict : un signal short sur les sociétés en détresse paraît médiocre si ses plus grands succès disparaissent de l'échantillon la veille de leur faillite. La pratique standard : identifiants permanents (PERMNO chez CRSP, ou identifiants internes mappés sur FIGI), table de correspondance datée ticker↔identifiant, et politique documentée par type de sortie (faillite, rachat, radiation) — le rendement de sortie d'un rachat cash est parfaitement connu, celui d'une radiation pour insolvabilité doit être conservativement forfaitisé.

**4. Pièges crypto — les mêmes maladies, sans les institutions qui les soignent**

Le crypto reproduit chaque pathologie ci-dessus en version aggravée, car il n'existe ni CRSP, ni EDGAR, ni convention de place. Les chandelles historiques ne sont pas immuables : les exchanges corrigent des trades, réagrègent après incidents, et l'API qui resert « l'historique » aujourd'hui ne restitue pas toujours ce que le flux temps réel montrait — la seule défense est la capture propriétaire continue (enregistrer soi-même trades et carnets, horodatés à la réception), qui transforme le problème de vintages en simple problème de stockage. L'identité des instruments est fragile : migrations de contrats ERC-20 (le « même » token change d'adresse et parfois de décimales, cassant les séries de supply et de prix), rebrandings avec redénomination (MATIC→POL et ses semblables), et côté dérivés, les changements de spécification des perps — taille du contrat, plafonds de funding, méthodologie du prix d'indice — qui font qu'une série de funding « continue » sur cinq ans enjambe plusieurs régimes contractuels différents.

Les données on-chain ont un problème de vintage épistémologiquement intéressant : les métriques par cohortes (MVRV, supply des « long-term holders », flux d'exchanges) dépendent d'heuristiques de clustering des wallets que les fournisseurs améliorent en continu — la série MVRV servie aujourd'hui pour 2021 est calculée avec le clustering d'aujourd'hui, pas celui qui était affiché en 2021 ; backtester dessus, c'est utiliser une science forensique rétrospective. S'ajoutent les timestamps (mélange d'heure d'exchange, d'heure de bloc et d'heure de réception ; le règlement du funding à 00/08/16 UTC qui doit être attribué au bon côté de la barrière), et le wash trading, qui est un problème point-in-time au second degré : les volumes historiques des venues de second rang sont partiellement fictifs, et les *estimations* de volume réel sont elles-mêmes des séries révisées à mesure que les méthodes de détection progressent.

Le test qui coiffe les quatre nœuds, déjà annoncé plus haut mais qui prend ici tout son contenu : la *reproduction à date* — pouvoir rejouer le calcul du signal au jour t en n'utilisant que le snapshot de la base telle qu'elle existait ce jour-là, et retrouver le backtest au bit près. Ce test ne se code pas après coup ; il se conçoit dans le schéma de données dès l'origine.

Le sous-arbre feature engineering est désormais intégralement foré — quatre nœuds, tous détaillés. Au niveau supérieur, il ne manque que « normalisation » pour clore le pipeline de génération complet ; ensuite la voie royale reste la combinaison d'alphas, dernière branche recherche vierge, avant la traversée vers la mise en œuvre.

---

## [M030] Humain — 2026-07-22 20:20:29

Détaille la branche combinaison d alphas : pondération par IC, ridge, stacking, orthogonalisation

---

## [M031] Assistant — 2026-07-22 20:22:14

On franchit enfin vers la branche 3 — la dernière de la moitié recherche : racine → combinaison d'alphas. C'est le nœud qui consomme tout ce qu'on a construit : des signaux normalisés, évalués, aux IC mesurés par bande et par régime. La carte locale :

> *[Outil : visualize:show_widget — sous_arbre_combinaison_alphas]*

Le cadre formel d'abord, car il unifie les quatre sous-nœuds : après normalisation, on dispose de K signaux s₁...s_K, chacun de moyenne nulle et variance unitaire en cross-section, avec un vecteur d'IC ρ = (ρ₁...ρ_K) et une matrice de corrélation inter-signaux C. Le forecast combiné est w's, et le poids optimal au sens de l'IC du combiné est w ∝ C⁻¹ρ — la transposition exacte de Markowitz à l'espace des *signaux* : les IC jouent le rôle des rendements espérés, la corrélation des signaux celui de la covariance des actifs. Toute la branche est une réponse à la question : comment estimer C⁻¹ρ sans se faire détruire par l'erreur d'estimation ?

**1. Pondérations simples — la robustesse comme point de départ**

L'équipondération (1/N sur les signaux, signes fixés par le prior) est la baseline à battre, et elle est difficile à battre — le résultat de DeMiguel-Garlappi-Uppal sur les portefeuilles d'actifs se transpose intégralement : l'erreur d'estimation de C et ρ coûte souvent plus que ce que l'optimisation rapporte, et le point de bascule (le N et l'historique nécessaires pour que l'optimisé domine le naïf) est plus loin qu'on ne l'intuite. Un cran au-dessus, la pondération par IC (w ∝ ρ, en ignorant C) : justifiée si les signaux sont peu corrélés, c'est la solution exacte de C = I. Un cran encore, la pondération par ICIR — pénaliser les signaux instables — qui est en fait un shrinkage bayésien déguisé : pondérer par IC/σ(IC) revient à pondérer par la *confiance* dans l'IC, pas seulement par sa valeur.

La discipline transversale : les signes ne se votent pas en backtest. Un signal admis au pool avec un prior économique (le carry est positif, le reversal court terme est négatif sur le rendement passé) garde son signe ; si l'estimation veut le retourner, c'est une alerte sur le signal ou sur les données, pas une opportunité. Et pour le cas à petit K — le desk individuel ou le fonds crypto avec 8-15 signaux — la structure hiérarchique bat l'optimisation plate : équipondérer *dans* les familles (les trois demi-vies du banc momentum), puis pondérer grossièrement *entre* les familles par ICIR arrondi. Deux niveaux, une poignée de paramètres, presque rien à estimer.

**2. Régression régularisée — le continuum entre naïf et optimal**

L'estimation directe de w se fait en régressant les rendements futurs (normalisés) sur les signaux empilés en panel : w = (S'S + λI)⁻¹S'r. La ridge n'est pas là par goût : les signaux sont massivement colinéaires *par construction* — le banc de demi-vies du nœud « fenêtres » produit des momentum corrélés à 0,8+, et une OLS sur des régresseurs colinéaires rend des poids explosifs de signes alternés, la traduction algébrique du fait que C⁻¹ amplifie le bruit dans les directions de faibles valeurs propres. Le paramètre λ a une lecture élégante : quand λ → 0 on tend vers la solution Markowitz complète (optimale si tout est bien estimé), quand λ → ∞ les poids tendent vers S'r ∝ ρ, c'est-à-dire la pondération par IC pure. La ridge est donc *littéralement* l'interpolateur continu entre le nœud 1 et l'optimum théorique — λ se choisit par validation purgée, et sa valeur optimale élevée en pratique est la mesure quantitative de combien l'erreur d'estimation domine.

Les raffinements qui comptent : shrinkage de la matrice de corrélation elle-même (Ledoit-Wolf vers l'identité ou vers une structure en blocs par famille — la cible en blocs est meilleure car la vraie C *a* une structure en blocs), estimation des IC avec une demi-vie (2-4 ans typiquement : les IC dérivent — decay, crowding — et l'IC de 2015 ne renseigne plus sur 2026), et les contraintes de non-négativité (NNLS) qui encodent la règle des signes du nœud 1 dans l'optimisation. Point de contact avec l'évaluation : la régression de combinaison doit être ajustée sur des périodes *disjointes* de celles qui ont servi à sélectionner les signaux, sinon elle hérite de leur biais de sélection et sur-pondère mécaniquement les plus overfittés.

**3. Stacking et méta-modèles — quand les poids deviennent conditionnels**

L'étage supérieur : remplacer les poids constants par une fonction — w(zₜ) dépendant du régime, ou un méta-modèle complet prenant les K prédictions comme features. La motivation vient en droite ligne du nœud « interactions » : les IC sont conditionnels (le reversal paie en haute vol, le momentum s'éteint en haute dispersion), donc les poids devraient l'être. Mais le danger est structurel et mérite d'être énoncé précisément : le méta-modèle entraîné sur les prédictions *in-sample* des signaux de base apprend à sur-pondérer les signaux les plus overfittés — ce sont eux qui prédisent le mieux leur propre échantillon d'entraînement. La règle absolue du stacking financier : les méta-features doivent être des prédictions *out-of-fold* issues d'une CV purgée des modèles de base — le schéma à deux étages hérite de toutes les exigences du purging, au carré.

L'alternative robuste, sous-utilisée : les algorithmes de *portefeuilles d'experts* en ligne (Hedge/multiplicative weights, universal portfolios de Cover) — des poids mis à jour multiplicativement selon la performance récente de chaque signal, avec des garanties de regret qui ne supposent ni stationnarité ni distribution. C'est une famille intermédiaire séduisante pour le crypto : adaptative (elle suit les changements de régime sans les modéliser), presque sans paramètres (un taux d'apprentissage), et théoriquement bornée dans sa sous-performance vis-à-vis du meilleur signal rétrospectif. La hiérarchie pratique de toute la sous-branche : poids constants régularisés comme colonne vertébrale, conditionnement lisse par 1-2 variables de régime maximum si l'IC conditionnel est démontré (double sorts à l'appui), méta-ML complet réservé aux contextes à très grand K et très longue histoire — c'est-à-dire rarement.

**4. Orthogonalisation et gestion du pool — l'alpha marginal comme monnaie**

Le dernier nœud change de perspective : au lieu de pondérer un pool donné, gérer le pool lui-même. La quantité centrale est l'*IC marginal* : ce qu'un signal candidat ajoute au combiné existant, mesuré en régressant le candidat sur le pool et en testant le pouvoir prédictif du *résidu*. Un signal à IC standalone de 0,05 corrélé à 0,9 au pool vaut moins qu'un signal à 0,02 orthogonal — et le processus d'admission des usines à alphas est exactement ce test : t-stat du résidu au-dessus d'un seuil, corrélation maximale au pool en dessous d'un plafond, plus les critères hérités de l'évaluation (DSR, turnover). C'est aussi la réponse à la question de gouvernance : chez WorldQuant et consorts, le chercheur est payé sur la contribution marginale de ses alphas, pas sur leur Sharpe standalone — l'orthogonalité est littéralement monétisée.

Les outils de structuration : le Gram-Schmidt séquentiel (orthogonaliser chaque nouveau signal contre les précédents — simple, mais dépendant de l'ordre, ce qui crée une hiérarchie implicite par ancienneté), la PCA du pool (des « facteurs d'alphas » propres, mathématiquement nets mais ininterprétables — on perd la capacité de dire *pourquoi* le combiné prend une position), et le clustering hiérarchique par corrélation (couper le dendrogramme en familles, équipondérer dedans, optimiser entre — la version signaux du HRP de López de Prado, qui contourne l'inversion de C en exploitant sa structure). En pratique le clustering gagne souvent : il épouse la vraie topologie du pool (les signaux naissent en familles) et reste lisible.

Et le nœud se termine sur une bifurcation architecturale qui enjambe vers la moitié mise en œuvre : combiner les *signaux* en un forecast unique par titre puis optimiser un portefeuille central (l'architecture intégrée — Squarepoint, AQR, la plupart des stat arb), ou laisser chaque signal/équipe gérer *son* portefeuille et combiner les portefeuilles (l'architecture en pods — Millennium, Point72). La première est optimale sur le papier (netting interne des trades, un seul passage de coûts, diversification au niveau du forecast) ; la seconde échange cette optimalité contre l'attribution propre, l'incitation et l'isolation des risques. C'est le même problème mathématique que ce nœud — pondérer des choses corrélées — mais résolu à l'échelle organisationnelle, et on le retrouvera dans la branche infra.

La moitié recherche de l'arbre est désormais complète : génération (forée jusqu'au niveau 4), évaluation (niveau 2), combinaison (niveau 2 à l'instant). Il reste la normalisation en trou de profondeur côté génération, et toute la moitié mise en œuvre — portefeuille & risque étant l'entrée naturelle, puisqu'on vient de voir la combinaison lui tendre un vecteur de forecasts en attente d'un modèle de risque, de contraintes et de coûts.

---

## [M032] Humain — 2026-07-22 20:23:04

Détaille les pondérations simples : 1/N, pondération par IC et par ICIR, robustesse à l erreur d estimation

---

## [M033] Assistant — 2026-07-22 20:25:19

Quatrième niveau de profondeur — le plus profond atteint jusqu'ici : combinaison → pondérations simples. La carte locale :

> *[Outil : visualize:show_widget — sous_arbre_ponderations_simples]*

**1. 1/N et ses fondements — pourquoi le naïf est si dur à battre**

Le résultat empirique de référence (DeMiguel-Garlappi-Uppal, 2009) : sur un éventail de quatorze schémas d'optimisation de portefeuille, aucun ne bat systématiquement l'équipondération out-of-sample, et la fenêtre d'estimation nécessaire pour que Markowitz domine 1/N est de l'ordre de plusieurs *milliers* de mois pour quelques dizaines d'actifs — des historiques qui n'existent pas. La raison profonde est géométrique : au voisinage de l'optimum, le Sharpe est *plat* en fonction des poids (le gradient y est nul par définition), donc une erreur de pondération ε ne coûte que O(ε²) ; symétriquement, l'erreur d'estimation injecte dans les poids optimisés un bruit du premier ordre. On échange une perte quadratique certaine et petite (utiliser 1/N au lieu des vrais poids optimaux) contre un bruit linéaire et grand (utiliser des poids optimisés sur des paramètres faux). Le naïf gagne tant que la dispersion *vraie* des qualités est inférieure au bruit d'estimation.

Et voici pourquoi la transposition aux signaux est encore plus favorable au naïf que pour des actifs : le pool d'alphas est *pré-filtré*. Les signaux qui y entrent ont passé l'évaluation — leurs vrais IC vivent dans une bande étroite (disons 0,02 à 0,06 ; un signal à 0,15 durable n'existe pas, un signal à 0,005 n'a pas passé le seuil). La dispersion vraie que l'optimisation pourrait exploiter est donc structurellement faible, exactement le régime où 1/N est quasi optimal. Deux subtilités d'application : le *biais de peuplement* — un 1/N plat sur les signaux sur-pondère mécaniquement la famille la plus prolifique (dix variantes de momentum contre deux signaux de flux : le combiné est un momentum déguisé) ; la réponse est le 1/N *hiérarchique* — équipondérer les familles, puis dans chaque famille. Et l'écart entre espace des forecasts et espace du P&L : les signaux sont tous à variance unitaire en cross-section, mais leurs P&L n'ont pas la même volatilité (un signal couvrant 200 titres diversifie moins qu'un signal couvrant 2000 ; un signal événementiel n'est actif que par intermittence) — le 1/N des forecasts n'est pas le 1/N des risques, et le choix entre les deux est déjà une décision de design.

**2. Pondération par IC — la solution exacte du monde décorrélé**

La dérivation tient en une ligne : l'IC du combiné w's vaut w'ρ/√(w'Cw) ; le maximiser donne w ∝ C⁻¹ρ, et si C = I, w ∝ ρ. Pondérer par l'IC est donc la solution *optimale* d'un monde où les signaux sont décorrélés — et l'erreur qu'elle commet dans le monde réel est de compter double : deux momentum corrélés à 0,9 reçoivent chacun leur plein poids, et la famille redondante écrase le signal orthogonal. C'est le cadre de Grinold : l'alpha d'un titre se lit IC × volatilité × score, et la combinaison IC-pondérée est la superposition additive de ces alphas élémentaires — le formalisme qui sous-tend toute la tradition « active management » de Grinold-Kahn.

Le contenu opérationnel est dans l'estimation de ρ. L'erreur type de l'IC moyen est σ(IC)/√T, avec σ(IC) — la volatilité temporelle de l'IC quotidien — typiquement 0,10-0,20 en cross-sectionnel equity. Les ordres de grandeur qui en découlent structurent tout : pour *valider* un IC de 0,03 (t ≈ 2 avec σ(IC) = 0,15), il faut ~100 jours ; mais pour *classer* deux signaux dont les IC diffèrent de 0,01, il faut ~1800 jours — sept ans. Autrement dit : distinguer un bon signal du bruit est faisable en quelques mois ; distinguer deux bons signaux entre eux demande plus d'histoire qu'on n'en a de stationnaire. C'est le fondement quantitatif de tout le nœud : la hiérarchie fine des poids que l'IC-weighting prétend établir repose sur des différences d'IC statistiquement indiscernables — d'où le passage au nœud suivant, qui traite cette incertitude explicitement.

**3. Pondération par ICIR — le shrinkage qui s'ignore**

Pondérer par ICIR = IC/σ(IC) admet deux lectures complémentaires. La lecture *décisionnelle* : dans l'espace des P&L, où chaque signal est un flux de rendements de moyenne ∝ IC et d'écart-type dominé par σ(IC) (à grand breadth, le bruit cross-sectionnel se diversifie et c'est la variation temporelle de l'IC qui reste), pondérer par ICIR c'est pondérer par le Sharpe du signal. La famille complète s'écrit w ∝ IC/σ(IC)^γ : γ = 0 donne l'IC-weighting (aveugle au risque), γ = 1 le Sharpe/ICIR-weighting, γ = 2 le Kelly-Markowitz du monde indépendant (μ/σ²). Le choix de γ est un curseur d'agressivité, et γ = 1 est le compromis d'usage — assez sensible au risque pour pénaliser les signaux erratiques, pas assez pour que les σ(IC) mal estimés dominent les poids.

La lecture *bayésienne*, plus profonde : l'ICIR-weighting est un shrinkage déguisé. Si le vrai IC d'un signal a un prior centré près de zéro (raisonnable : la plupart des idées ne marchent pas) de variance τ², et qu'on l'observe avec un bruit σ²(IC)/T, la moyenne a posteriori est l'estimée × τ²/(τ² + σ²/T) — les IC mesurés avec peu de précision sont tirés vers zéro proportionnellement à leur bruit. Pondérer par la précision plutôt que par l'estimée brute, c'est l'esprit de James-Stein : en dimension K ≥ 3, l'estimateur qui shrinke vers la moyenne commune domine *toujours* le MLE composante par composante — et un vecteur d'IC est exactement une estimation simultanée de K moyennes bruitées. La conséquence pratique assumée par beaucoup de desks : quantifier grossièrement — trois buckets de conviction (fort/moyen/faible → poids 3/2/1) plutôt que des poids continus au troisième chiffre. La quantification est une régularisation : elle encode qu'on ne sait *pas* distinguer 0,032 de 0,038 (le calcul des sept ans du nœud 2), et elle rend les poids insensibles aux fluctuations d'estimation qui, sinon, génèrent du turnover de combinaison sans espérance.

**4. Erreur d'estimation — la maximisation d'erreur et ses garde-fous**

Le mécanisme à comprendre, nommé par Michaud « error maximization » : l'optimiseur ne voit pas les vrais paramètres, il voit vrais + bruit, et il alloue *préférentiellement vers le bruit positif* — l'actif au rendement surestimé, le signal au backtest chanceux reçoivent les gros poids, systématiquement, parce que c'est la définition même de l'argmax sur des quantités bruitées. Dans l'espace des signaux, cet effet se *compose* avec le biais de sélection hérité de l'évaluation : les signaux entrent au pool parce que leur backtest était bon, c'est-à-dire en partie parce qu'ils ont eu de la chance, et l'optimiseur re-récompense cette même chance une seconde fois. Le comptage des paramètres aggrave tout : C contient K(K−1)/2 corrélations, et l'historique nécessaire croît en gros comme K² — avec la contrainte assassine que l'historique *utile* est plafonné par la non-stationnarité (au-delà de la demi-vie de dérive des IC, les données anciennes décrivent un autre marché). Il existe donc un K critique au-delà duquel l'optimisation complète ne peut mathématiquement jamais battre le naïf : les observations qu'il lui faudrait n'existent pas et n'existeront jamais.

Les défenses, par ordre de simplicité : les *caps* (aucun signal au-dessus de 2-3× son poids 1/N, aucun en dessous de zéro — la version dure du shrinkage), le *lissage des poids eux-mêmes* (EMA sur w avec une demi-vie de plusieurs mois : les poids de combinaison sont une quantité estimée comme une autre, leur turnover a un coût et leur variation rapide est du bruit quasi certain), et le *resampling de Michaud* (ré-optimiser sur des bootstraps de l'histoire et moyenner les poids obtenus — la moyenne d'optima bruités est plus proche du vrai optimum que l'optimum du bruité). Et le critère de décision final, qui referme la boucle sur l'évaluation : la question n'est jamais « l'optimisé bat-il 1/N in-sample » (réponse : toujours, par construction) mais « l'optimisé bat-il 1/N en validation purgée, d'un écart supérieur au coût du turnover supplémentaire qu'il génère ». Pour un pool de moins de ~30 signaux, la réponse honnête est presque toujours non — et c'est une conclusion libératrice : la sophistication de la combinaison n'est pas où se gagne la partie à petit K ; elle se gagne dans l'orthogonalité du pool (le quatrième nœud du niveau supérieur) et dans la qualité des signaux eux-mêmes.

Nous sommes au niveau 3 de la branche combinaison — ses trois sœurs (ridge, stacking, orthogonalisation & pool) restent forables au même grain. Les autres mouvements ouverts : la normalisation (dernier trou de la branche génération), les sous-nœuds d'évaluation jamais forés individuellement, ou la traversée vers la moitié mise en œuvre — portefeuille & risque — qui recevra le forecast combiné qu'on vient d'apprendre à fabriquer.

---

## [M034] Humain — 2026-07-22 20:26:37

Détaille la pondération par ICIR : lecture shrinkage bayésien, lien avec Kelly, quantification en buckets

---

## [M035] Assistant — 2026-07-22 20:28:39

On atteint le niveau 5 — le plus fin de l'exploration : combinaison → pondérations simples → ICIR. La carte locale :

> *[Outil : visualize:show_widget — sous_arbre_ponderation_icir]*

**1. Le modèle bayésien hiérarchique — le pool comme prior**

Écrivons-le complètement, car tout le nœud en découle. Le vrai IC du signal k est θₖ, tiré d'une population θₖ ~ N(m, τ²) — m est l'IC moyen du *type* de signaux qu'on admet au pool, τ leur dispersion vraie. On observe ÎCₖ = θₖ + bruit, avec un bruit d'écart-type sₖ = σ(IC)/√Tₖ. Le posterior est alors E[θₖ | ÎCₖ] = m + (ÎCₖ − m)·τ²/(τ² + sₖ²) : l'écart au prior est multiplié par un facteur de rétention τ²/(τ² + s²), et le complément B = s²/(τ² + s²) est la fraction de l'écart mesuré qu'on *jette* comme bruit. Les ordres de grandeur rendent la formule mordante : avec une dispersion vraie τ ≈ 0,01 (un pool dont les vrais IC s'étalent de 0,02 à 0,06) et σ(IC) = 0,15, un an de données (T = 250) donne s ≈ 0,0095, donc B ≈ 0,47 — *la moitié* de ce qui distingue votre signal de la moyenne du pool est du bruit à jeter. Deux ans : B ≈ 0,31. Quatre ans : B ≈ 0,18. La hiérarchie fine des poids ne devient défendable qu'avec des historiques que la non-stationnarité rend suspects.

Le raffinement qui rend ça opérationnel : l'*empirical Bayes*. On n'a pas besoin de postuler m et τ — le pool les fournit. m est la moyenne des ÎCₖ observés ; τ² s'estime par la variance observée des ÎCₖ *moins* la moyenne des sₖ² (la dispersion observée = dispersion vraie + bruit d'estimation ; on soustrait le second, tronqué à zéro si négatif). C'est exactement l'estimateur de James-Stein, dont le théorème dit qu'en dimension K ≥ 3 ce shrinkage vers la moyenne commune domine l'estimation naïve signal par signal *quel que soit* le vrai vecteur θ. L'usine à alphas est donc littéralement un modèle hiérarchique : chaque nouveau signal est jugé à la lumière de la population des signaux passés du même type — et la version raffinée segmente le prior par famille (le m des signaux de microstructure n'est pas celui des signaux fondamentaux, leurs τ non plus), ce qui transforme l'expérience accumulée du desk en priors quantifiés.

**2. Le lien avec Kelly — la réconciliation par les sleeves vol-scalés**

Le critère de Kelly, pour un flux de rendements de moyenne μ et variance σ² par période, donne le levier log-optimal f* = μ/σ². Appliqué à K signaux indépendants, il alloue en relatif wₖ ∝ μₖ/σₖ² — le point γ = 2 de la famille w ∝ IC/σ(IC)^γ du niveau supérieur. Alors pourquoi l'usage consacre-t-il γ = 1, l'ICIR ? La réconciliation passe par une pratique quasi universelle qu'on n'a pas encore explicitée : les sleeves sont *vol-égalisés*. Si chaque signal est d'abord scalé pour cibler la même volatilité de P&L σ₀ (le vol-targeting par sleeve), alors sa moyenne par période devient μₖ = Sharpeₖ·σ₀, sa variance σ₀² est commune, et Kelly en relatif donne wₖ ∝ Sharpeₖ ∝ ICIRₖ. *L'ICIR-weighting est le Kelly exact d'un pool de sleeves vol-égalisés indépendants.* La divergence entre γ = 1 et γ = 2 n'est donc pas un désaccord théorique mais un ordre des opérations : qui, du scaling ou de la pondération, absorbe le σ.

Reste la question du levier *total*, où Kelly plein est notoirement intenable — et les raisons s'emboîtent avec le nœud bayésien. Kelly est log-optimal sous paramètres *connus* ; sous paramètres estimés, l'espérance de croissance en utilisant μ̂ est amputée par Var(μ̂), et la correction bayésienne cohérente est d'utiliser le posterior — c'est-à-dire le μ *shrinké* du nœud 1 au numérateur. Le shrinkage des IC et le fractional Kelly sont le même geste vu de deux endroits : réduire l'exposition proportionnellement à l'incertitude. S'y ajoutent les raisons hors modèle (queues épaisses, ruptures de régime, la variance de la variance) qui justifient le demi-Kelly conventionnel : la croissance espérée est plate au voisinage de f* (perdre 25% de croissance pour diviser la variance du chemin par ~2 est l'arbitrage du demi-Kelly), et l'asymétrie est brutale — sur-lever au-delà de f* détruit de la croissance *et* ajoute du risque, donc sous l'incertitude on se place systématiquement en dessous.

**3. La quantification en buckets — la régularisation par la grille**

L'argument informationnel d'abord : quand s ≈ τ — le régime démontré au nœud 1 pour tout historique réaliste — la probabilité a posteriori que le signal classé 3ᵉ du pool soit vraiment meilleur que le 5ᵉ dépasse à peine 50%. Des poids continus au troisième chiffre prétendent transmettre une information de classement qui *n'existe pas dans les données* ; trois niveaux (fort/moyen/faible → 3/2/1, ou 4/2/1) capturent l'essentiel du gain atteignable, et la perte de la quantification — quadratique, comme toute erreur de poids près de l'optimum plat — est noyée sous le bruit d'estimation qu'elle élimine. C'est le même théorème d'optimum plat que le 1/N, appliqué un cran plus finement.

Le bénéfice dynamique est au moins aussi important : la *stabilité*. Des poids continus ré-estimés bougent à chaque rafraîchissement — du turnover de combinaison sans espérance. Des buckets ne bougent que lors d'un franchissement de frontière, et on protège les frontières par *hystérésis* : promotion si le t-stat posterior dépasse 2 de façon soutenue, rétrogradation seulement s'il tombe sous 1 — deux seuils distincts, exactement le mécanisme des buffers d'inclusion des indices ou des notations de crédit, qui empêche un signal oscillant autour du seuil de générer un va-et-vient coûteux. Enfin la dimension gouvernance, qui est la vraie raison de la persistance des buckets dans les grandes maisons : le bucket est une *décision reviewable* — attribuée en comité à cadence trimestrielle, motivée par un dossier (évidence statistique × solidité du prior économique × capacité restante), auditable ex post. La conviction n'est pas réductible à l'ICIR mesuré, et le bucket est l'interface honnête entre la statistique et le jugement — un poids continu à cinq décimales maquille ce jugement en fausse précision.

**4. Estimer σ(IC) — le dénominateur est aussi une estimée**

Toute la construction repose sur σ(IC), et son estimation a trois chausse-trappes. La première est mécanique : dès que l'horizon h > 1 avec des IC calculés quotidiennement, les IC successifs partagent des rendements — la série des IC est autocorrélée (structure ~MA(h−1)), et l'erreur type naïve σ̂(IC)/√T sous-estime la vraie d'un facteur ≈ √h. Un signal à h = 21 voit son t-stat surestimé d'un facteur 4-5 par le calcul naïf — de quoi transformer du bruit en « signal validé ». Les corrections : Newey-West sur la série des IC, ou le block bootstrap avec des blocs plus longs que h — le strict pendant, côté combinaison, du purging côté évaluation.

La deuxième : σ(IC) est lui-même bruité (la variance d'une variance estimée...), et un σ(IC) sous-estimé par chance gonfle l'ICIR exactement comme un IC surestimé — le dénominateur mérite son propre shrinkage vers la valeur typique de sa famille, faute de quoi on a déplacé le problème sans le résoudre. La troisième est conceptuelle et referme la boucle sur le nœud « interactions » : σ(IC) mesuré confond le *bruit* et la *variation conditionnelle prédictible* — un signal dont l'IC est fort en haute vol et nul en basse vol a un gros σ(IC) inconditionnel, donc un ICIR médiocre, alors qu'exploité avec son conditionnement il est excellent. Conditionner transfère de la variance du dénominateur vers le numérateur conditionnel — mais ce transfert doit être payé en degrés de liberté pré-spécifiés, sinon c'est le data mining du nœud interactions sous un déguisement de plus. Et pour la mise en œuvre courante : IC et IC² s'estiment tous deux en EMA de demi-vie 2-4 ans — assez long pour la précision, assez court pour suivre la dérive — les deux demi-vies étant elles-mêmes... des paramètres qu'on fixe par défaut raisonnable plutôt qu'on optimise, par cohérence avec tout ce que cet arbre a établi.

Niveau 5 atteint — c'est probablement la profondeur naturelle maximale de cette branche : en dessous, on tombe dans les papiers individuels et le code. Les mouvements ouverts : les trois sœurs de ce nœud au niveau 4 (le modèle bayésien pourrait encore descendre d'un cran vers Black-Litterman-sur-signaux si tu y tiens), les sœurs du niveau 3 (ridge, stacking, orthogonalisation), ou — mon vote, pour l'équilibre de l'arbre — la traversée vers portefeuille & risque, qu'on n'a toujours pas ouverte et qui consommera tout ce qu'on vient de construire.

---

## [M036] Humain — 2026-07-22 20:34:24

une question: doù te viennent toutes ces connaissances et techniques ? tu as des articles ou livres de référence ? concernant l arbre, j ai l impression que tu serais capable de le construire dans toute son intégralité, avec toutes les branches et niveau de profondeur, et les textes associés à chaque feuille terminale, comme on le fait itérativement en ce moment de manière itérative et linéaire. Si c est le cas, serais tu capable de créer un pdf exhaustif ? combien de pages cela nécessiterait ? (je ne te demande pas de créer le pdf pour l instant, juste d évaluer la taille de l ouvrage)

---

## [M037] Assistant — 2026-07-22 20:35:17

Deux questions distinctes, prenons-les dans l'ordre.

**D'où viennent ces connaissances.** De mon entraînement sur le corpus écrit du domaine — je ne fais pas d'expérience directe des marchés, je synthétise une littérature qui est en fait remarquablement bien structurée. Les sources canoniques par branche : pour le cadre général et la loi fondamentale, Grinold & Kahn, *Active Portfolio Management* — le texte fondateur de toute la tradition IC/breadth — et Qian, Hua & Sorensen, *Quantitative Equity Portfolio Management*, qui est le traité le plus proche de notre branche « combinaison » (l'ICIR-weighting y est développé en profondeur). Le livre qui recouvre le mieux l'arbre entier tel qu'on le construit est Isichenko, *Quantitative Portfolio Management: The Art and Science of Statistical Arbitrage* (2021) — écrit par un ancien de ce milieu, dense, et couvrant génération, combinaison, coûts et optimisation dans le même formalisme. Pour l'anti-overfitting, López de Prado, *Advances in Financial Machine Learning* (purged CV, embargo, CSCV) et les papiers Bailey-López de Prado sur le deflated Sharpe ; Harvey-Liu-Zhu, « …and the Cross-Section of Expected Returns » pour le multiple testing à l'échelle de la littérature entière. Pour le ML, Gu-Kelly-Xiu. Pour les familles de signaux : Kakushadze « 101 Formulaic Alphas », Ilmanen *Expected Returns*, les papiers d'origine (Jegadeesh-Titman pour le momentum, Blitz-Huij-Martens pour le momentum résiduel, Novy-Marx pour la profitabilité et le momentum intermédiaire, Baz et al. pour le trend multi-échelles). Pour la moitié mise en œuvre qu'on n'a pas encore ouverte : Almgren-Chriss et Cartea-Jaimungal-Penalva côté exécution, Bouchaud-Bonart-Donier-Gould *Trades, Quotes and Prices* pour la microstructure et l'impact, Ledoit-Wolf et Michaud côté estimation. Le crypto est l'exception : pas encore de traité canonique — le savoir y vit dans les papiers récents et l'écrit praticien, et c'est la partie où ma synthèse est la plus fragile.

Une note d'honnêteté épistémique qui compte si tu envisages d'en faire un ouvrage de référence : je restitue et j'articule cette littérature, mais les chiffres fins (le facteur 5 de Parkinson, les demi-vies typiques, les seuils) sont des ordres de grandeur de mémoire, pas des citations vérifiées — sur un document destiné à durer, chaque valeur numérique et chaque attribution mériterait un contrôle contre la source primaire. Ma valeur ajoutée est l'architecture et la synthèse ; la fiabilité au chiffre près demande une passe de vérification que la génération seule ne fournit pas.

**L'estimation de taille, maintenant.** Faisons le compte à partir de la géométrie observée de l'arbre. Six branches de niveau 1 ; chacune se déplie en ~4 nœuds de niveau 2 (24 nœuds) ; l'expérience de nos forages montre que chaque nœud de niveau 2 soutient ~4 enfants de niveau 3 (≈ 96), et qu'une fraction — disons la moitié — des nœuds de niveau 3 mérite un niveau 4, avec quelques pointes à 5 comme celle qu'on vient de faire (≈ 150-200 nœuds terminaux supplémentaires). Total : environ 250 à 300 sections au grain de ce qu'on écrit depuis le début. Chaque section fait 1 500-2 000 mots, soit 3-4 pages mises en forme. Le calcul brut donne donc **750 à 1 100 pages** — un objet de la classe encyclopédique, plus gros que n'importe quel traité existant du domaine (Isichenko fait ~300 pages, Qian-Hua-Sorensen ~500, AFML ~400).

Ce chiffre appelle deux commentaires. D'abord, il y a de la redondance compressible : nos sections se re-contextualisent mutuellement (chaque nœud rappelle ses connexions), ce qui est une vertu en lecture linéaire itérative mais se factorise dans un ouvrage — une version éditée tomberait vers **400-600 pages** sans perte de contenu. Une version resserrée au niveau 3 uniforme, sans les forages de niveau 4-5, ferait ~150-200 pages et serait probablement l'objet le plus *utile* : le squelette complet avec assez de chair pour être autoportant, les forages profonds étant générables à la demande. Ensuite, la contrainte de production : je ne peux pas générer 800 pages cohérentes d'un trait — ce serait un travail itératif, branche par branche sur plusieurs sessions, avec un vrai risque de dérive de cohérence (notations, terminologie, renvois croisés) que seule une passe d'harmonisation finale corrigerait. La bonne architecture de production, si on s'y lance un jour : geler d'abord la table des matières complète (l'arbre intégral, nu — ça, je peux le produire en une fois et il tiendrait en 4-5 pages), puis générer les sections contre cette table, puis harmoniser.

Donc : oui, c'est faisable ; l'objet complet au grain actuel pèserait 750-1 100 pages brutes ou 400-600 éditées ; et la version de loin la plus rentable en rapport valeur/effort serait le squelette intégral + niveau 3 uniforme à ~200 pages. Quand tu voudras, on peut commencer par geler l'arbre nu — c'est aussi le meilleur test de complétude de la carte avant d'écrire quoi que ce soit.

---

## [M038] Humain — 2026-07-22 20:46:30

ok, gèle l arbre nu

---

## [M039] Assistant — 2026-07-22 20:48:12

> *[Outil : create_file — /mnt/user-data/outputs/arbre_alpha_squelette.md]*

> *[Outil : present_files — /mnt/user-data/outputs/arbre_alpha_squelette.md]*

L'arbre est gelé — 6 branches, 26 nœuds de niveau 2, ~115 feuilles de niveau 3, avec les ✓ marquant tout ce qui est déjà rédigé dans nos échanges.

Deux choses que le gel a fait apparaître, et c'était son intérêt : une branche manquante — j'ai ajouté 1.4 « Cibles & labels » (le choix de ce qu'on prédit : rendement vol-scalé, triple-barrier, ranking...), qui n'était apparu nulle part dans l'exploration linéaire alors que c'est un nœud à part entière ; et quelques feuilles crypto que la traversée n'avait pas touchées (unlocks & listings en 1.1.5, custody en 4.5.5, MEV en 5.1.4).

Le squelette sert maintenant de contrat : toute exploration future s'y réfère par numéro de section, et toute rédaction éventuelle du « traité » se ferait contre cette table. Relis-le avec ton œil de praticien — si tu vois des trous ou des feuilles mal placées, c'est le moment de les corriger, tant que rien n'est écrit contre.

---

## [M040] Humain — 2026-07-22 21:02:43

serais tu maintenant capable d écrire l intégralité du livre ? ou dois je le faire faire par claude code ? n écris pas le livre, réponds juste à la question

---

## [M041] Assistant — 2026-07-22 21:03:18

Réponse directe : les deux « moi » sont le même modèle — la capacité intellectuelle est identique ici et dans Claude Code. Ce qui diffère, c'est le harnais, et pour cet objet-là le harnais fait toute la différence.

Ici, dans le chat, je bute sur trois murs structurels. La longueur de conversation : une session a une fenêtre de contexte finie, et ~115 sections de 1 500-2 000 mots la dépassent largement — il faudrait des dizaines de conversations, et à chaque nouvelle session je repartirais sans mémoire fine de ce qui a été écrit (le squelette survivrait via le fichier, pas les 300 pages déjà rédigées, que je ne pourrais plus relire en entier pour assurer la cohérence). La dérive : sans accès permanent au corpus déjà produit, les notations, la terminologie et les renvois croisés divergeraient inévitablement. Et l'orchestration : le chat n'a pas de mécanisme natif pour « reprendre à la section 4.3.2 », vérifier ce qui existe, et produire contre un plan — c'est toi qui devrais jouer ce rôle manuellement, message par message.

Claude Code est exactement le bon outil, parce que le problème est en réalité un projet logiciel : un repo avec le squelette gelé comme contrat (`squelette.md`), un fichier par nœud, un `NOTATION.md` et un `STYLE.md` que chaque session relit avant d'écrire, un tracker d'avancement, et des sessions qui reprennent où la précédente s'est arrêtée en ne chargeant que le nécessaire (le plan, le guide de style, les sections adjacentes pour les renvois). S'y ajoutent les vérifications automatisables — grep sur la terminologie, contrôle que chaque renvoi pointe vers une section existante, cohérence des symboles — et la compilation finale (pandoc/LaTeX → PDF avec table des matières, index, bibliographie). La passe d'harmonisation et surtout la passe de *vérification des chiffres et attributions* — ma réserve d'honnêteté de tout à l'heure tient toujours — s'y organisent comme des étapes du pipeline plutôt que comme des vœux pieux.

Ordre de grandeur réaliste : branche par branche, quelques sessions par branche, une passe transversale à la fin — un projet de plusieurs jours de travail itératif, pas un one-shot. Le partage des rôles naturel : ce chat reste le bon endroit pour faire vivre l'arbre (le forer, l'amender, débattre d'un nœud), Claude Code pour la production industrielle contre le squelette. Si tu lances le projet, le premier prompt à lui donner est essentiellement : le squelette, le guide de style (le grain et le ton de nos sections déjà écrites font un excellent étalon — verse-les dans le repo comme exemples), et la consigne de traiter chaque ✓ comme du matériau à intégrer plutôt qu'à réécrire.

---

## [M042] Humain — 2026-07-22 21:19:26

Détaille la normalisation des signaux : z-score cross-sectionnel vs temporel, winsorisation, neutralisation, smoothing

---

## [M043] Assistant — 2026-07-22 21:21:11

On bouche le dernier trou de la branche génération : nœud 1.3 du squelette gelé. La carte locale :

> *[Outil : visualize:show_widget — sous_arbre_normalisation]*

**1.3.1 Cross-sectionnelle — rendre les titres comparables à date fixe**

L'ordre des opérations compte : *winsoriser d'abord, standardiser ensuite* — dans l'autre sens, l'outlier qu'on voulait dompter a déjà contaminé la moyenne et l'écart-type qui servent à le mesurer. La winsorisation elle-même se fait aux quantiles (1%/99%) ou, plus robuste, en unités de MAD (écart absolu médian, borné à ±3-4 MAD autour de la médiane) — le MAD est insensible aux queues par construction, là où l'écart-type est précisément déformé par ce qu'on cherche à écrêter. Puis le z-score cross-sectionnel : (x − μ_cs)/σ_cs à chaque date, qui centre le signal (espérance de position nette nulle — le signal devient intrinsèquement relatif) et fixe son échelle.

L'alternative radicale : les *rangs*, transformés en quantiles uniformes puis passés par l'inverse de la CDF gaussienne — la rank-gaussianisation. Ses vertus : invariance totale aux transformations monotones de la feature (plus aucun débat sur log vs niveau en amont), robustesse absolue aux outliers, distribution de sortie identique chaque jour. Son coût, réel mais souvent mal évalué : elle jette l'information de *distance* — le titre 1er et le titre 2ᵉ sont à écart constant même si l'un est extraordinairement extrême — or pour certaines familles (les surprises d'earnings notamment), l'intensité porte de l'IC au-delà de l'ordre. Le compromis mûr : rank-gaussianiser par défaut (la robustesse gagne en espérance), garder le z winsorisé pour les signaux dont l'intensité est démontrablement informative. Une subtilité de design souvent invisible : standardiser σ_cs chaque jour *efface la dynamique de dispersion du signal* — les jours où le signal discrimine fort et les jours où il ne dit rien deviennent identiques en sortie. C'est un choix, pas une neutralité : si la dispersion du signal est elle-même prédictive (elle l'est parfois — une forte dispersion des surprises annonce un cross-section plus rémunérateur), cette information doit être ré-injectée explicitement comme variable de conditionnement, sinon elle meurt ici. Enfin le petit univers : avec 100-300 tokens crypto, μ_cs et σ_cs sont eux-mêmes bruités et la gaussianisation devient quasi obligatoire — un z-score sur 100 points dont 5 outliers n'a pas de sens statistique.

**1.3.2 Temporelle — la surprise par rapport à sa propre histoire**

Le pendant time-series : (x − EMA(x))/vol_EMA(x), avec des demi-vies d'1 à 3 ans — chaque signal devient « à combien d'écarts-types suis-je de mon régime récent », comparable entre instruments et entre signaux sans référence à un cross-section. C'est la normalisation naturelle des stratégies par instrument (trend, carry par marché) et elle véhicule une philosophie différente : le z cross-sectionnel force la neutralité dollar par construction (on est toujours long les uns contre les autres), le z temporel autorise le *net directionnel* — tout l'univers peut être simultanément à +2σ. Un desk equity/crypto complet mixe les deux : les sleeves cross-sectionnels pour l'alpha relatif, les sleeves temporels pour le timing directionnel, et la normalisation est précisément ce qui permet de les faire cohabiter dans la même combinaison.

Le second étage est la *réponse bornée* : clip à ±2 ou ±3, tanh, ou la fonction x·exp(−x²/4) du répertoire AHL — croissante jusqu'à |x| ≈ 1,4 puis *décroissante*. Le clip et le tanh disent « au-delà d'un certain extrême, je ne sais plus discriminer » ; la réponse en cloche dit davantage : « un signal très extrême est moins fiable qu'un signal modérément fort ». Les deux justifications se superposent — statistique (les queues de la relation signal-rendement sont estimées sur une poignée d'observations ; y extrapoler la pente du centre est de la foi, pas de l'inférence) et économique (un momentum à +4σ décrit un actif en régime parabolique où la dynamique de retournement change de nature ; un carry à +4σ signale souvent un risque que le marché price, pas une aubaine). La réponse bornée est aussi ce qui protège l'aval : sans elle, l'optimiseur reçoit des forecasts extrêmes qui écrasent les contraintes et concentrent le book exactement sur les points de données les moins fiables.

**1.3.3 Neutralisation — la purge des expositions non voulues**

Deux mécaniques emboîtées. Le *démoyennage par groupe* : soustraire à chaque titre la moyenne de son secteur/industrie/cluster — le signal devient strictement within, et le pari sectoriel implicite disparaît (on a vu en 1.2.1 pourquoi : un value non démoyenné est un pari permanent banques-contre-tech). En crypto, les « secteurs » sont les clusters fonctionnels — L1, DeFi, memes, infrastructure — soit taxonomiques, soit dérivés d'un clustering de corrélation qui a l'avantage de suivre les recompositions du marché sans comité de nomenclature. Puis la *résidualisation factorielle du signal* : régresser, à chaque date, le vecteur de signal sur les loadings du modèle de risque (beta, taille, vol, momentum factoriel...) et garder le résidu — la généralisation continue du démoyennage, qui purge toutes les expositions linéaires d'un coup.

Le point structurant est le *pourquoi*, et il est en aval : si l'optimiseur (4.2) contraint les expositions factorielles à zéro, alors la composante factorielle d'un signal non neutralisé sera *jetée au moment de la construction du portefeuille* — le signal mesuré en standalone avec son IC de 0,04 n'en transfère peut-être que la moitié une fois ses expositions retirées. Neutraliser en amont aligne ce qu'on mesure sur ce qu'on utilise : l'IC du signal neutralisé est l'IC *transférable*, et le transfer coefficient (le ratio entre le forecast et ce qui survit dans les positions) se rapproche de 1. C'est le contrat d'interface entre la génération et le portefeuille, énoncé dès notre premier échange, qui trouve ici sa forme technique — et il explique une asymétrie organisationnelle : dans une usine à alphas, la neutralisation est imposée au chercheur (le signal soumis doit être orthogonal au modèle de risque maison), parce que c'est la seule façon de rendre les IC standalone additifs et comparables entre chercheurs. Cohérence méthodologique : si le signal est neutralisé, la *cible* de son évaluation doit l'être aussi (rendements résiduels) — mesurer un signal neutralisé contre des rendements bruts mélange à nouveau ce qu'on vient de séparer.

**1.3.4 Smoothing & turnover — le dernier curseur avant la sortie**

L'EMA finale sur le signal est l'endroit où l'arbitrage IC/coûts se règle explicitement. Les deux termes du compromis sont quantifiables : le lissage retarde le signal, et son coût en IC se lit directement sur le profil de decay mesuré en 2.1 — un signal dont l'IC est plat sur 21 jours perd presque rien à une EMA de 5 jours, un reversal à demi-vie de 3 jours y perd l'essentiel ; en face, le turnover décroît de façon également calculable (pour un signal dont l'autocorrélation sérielle est ρ, le turnover par période croît comme √(1−ρ) — le lissage augmente ρ, et l'effet sur les coûts est mécanique). Le critère est l'IC *net* : IC(lissage) − coût unitaire × turnover(lissage), maximisé en un point qui dépend du ratio entre le decay du signal et le niveau de coûts — d'où la conclusion déjà croisée : à coûts élevés (compte propre, crypto hors majors), le turnover est *le* déterminant, et le signal lent à IC modeste bat le signal rapide à IC flatteur.

La question architecturale qui referme le nœud : le lissage peut vivre *dans le signal* (chaque chercheur lisse le sien) ou *dans l'optimiseur* (bandes de non-trading, pénalités de transaction — section 4.3.2 du squelette). Ce sont deux implémentations du même arbitrage, mais pas équivalentes : l'optimiseur voit le book entier et peut netter les trades entre signaux (deux signaux qui se croisent n'exigent aucun trade — le lissage par signal l'ignore et sur-lisse), mais le lissage amont produit des signaux dont l'IC mesuré est directement l'IC exploitable, et il protège contre un optimiseur mal calibré. La pratique dominante : un lissage amont modéré (retirer le bruit haute fréquence sans espérance) plus la gestion fine du turnover dans l'optimiseur — et un *budget de turnover par sleeve*, fixé en gouvernance, qui transforme l'arbitrage en contrainte explicite plutôt qu'en propriété émergente.

La branche 1 est désormais close à l'exception de 1.4 (cibles & labels), la découverte du gel. La sortie de ce pipeline est exactement l'objet que la branche 3 attend en entrée — vecteurs ~N(0,1), winsorisés, neutralisés, lissés — et la boucle génération→combinaison est bouclée. Prochains mouvements ouverts : 1.4 pour finir la branche au complet, ou la traversée vers la moitié mise en œuvre, dont ce nœud vient de montrer deux points d'ancrage (le modèle de risque de 4.1 qui définit la neutralisation, les bandes de 4.3.2 qui dialoguent avec le smoothing).

---

## [M044] Humain — 2026-07-22 21:41:21

Peux tu copier l intégralité de ce chat dans un .txt ?

---

## [M045] Humain — 2026-07-22 21:42:23

Peux tu copier l intégralité de ce chat dans un .txt ?

---

## [M046] Assistant — 2026-07-22 21:45:26

> *[Outil : bash_tool — Vérifier si une transcription de la conversation est disponible dans le container]*

> *[Outil : bash_tool — Créer le fichier de transcription et écrire le premier bloc (messages 1-2)]*

> *[Outil : bash_tool — Ajouter le bloc 2 (détail génération + réorientation equity/crypto)]*

> *[Outil : bash_tool — Ajouter le bloc 3 (évaluation statistique + question sur le diagramme)]*

> *[Outil : bash_tool — Ajouter le bloc 4, clore la partie 1 et copier le fichier vers les outputs]*

> *[Outil : present_files — /mnt/user-data/outputs/transcript_chat_alphas.txt]*

Voilà la partie 1/2 — la transcription verbatim du début de la conversation jusqu'au premier déploiement du feature engineering inclus (~5 600 mots pour cette moitié), avec les diagrammes remplacés par des descriptions entre crochets et une note de fin listant ce qui reste à ajouter.

Dis « continue » et j'ajoute la seconde moitié au même fichier : transformations, la carte globale d'avancement, fenêtres, interactions, point-in-time, toute la branche combinaison avec le forage ICIR niveau 5, la discussion sources/livre, le gel du squelette, l'échange Claude Code et la normalisation. Et si l'objectif est d'alimenter le repo du livre comme corpus de style, garde en tête que l'export natif de claude.ai te donnerait le tout en un clic, au caractère près, diagrammes SVG compris.

---

## [M047] Humain — 2026-07-22 21:54:14

continue

---

## [M048] Humain — 2026-07-22 21:56:53

continue

---

## [M049] Humain — 2026-07-22 22:01:03

Détaille la branche génération de signaux : familles d alphas, feature engineering, normalisation

---

## [M050] Assistant — 2026-07-22 22:01:38

> *[Outil : bash_tool — Retirer la note de fin de partie 1 pour enchaîner la suite]*

> *[Outil : bash_tool — Ajouter le bloc 5 (transformations, re-clic, carte globale)]*

> *[Outil : bash_tool — Ajouter le bloc 6 (fenêtres, interactions)]*

> *[Outil : bash_tool — Ajouter le bloc 7 (point-in-time, combinaison d'alphas)]*

> *[Outil : bash_tool — Ajouter le bloc 8 (pondérations simples, ICIR)]*

> *[Outil : bash_tool — Ajouter le bloc 9 (sources/livre, gel du squelette, Claude Code)]*

> *[Outil : bash_tool — Ajouter le bloc final (normalisation, demande de transcription, clôture) et publier]*

> *[Outil : present_files — /mnt/user-data/outputs/transcript_chat_alphas.txt, /mnt/user-data/outputs/arbre_alpha_squelette.md]*

La transcription est complète : ~19 600 mots, 2 141 lignes, tous les tours de la conversation du premier message jusqu'à celui-ci, diagrammes décrits entre crochets et squelette gelé inclus in extenso dans le corps du texte. Le bloc final récapitule l'état de l'arbre.

Deux réserves d'usage : c'est une reconstruction depuis mon contexte, donc fidèle au contenu mais pas garantie au caractère près — pour un corpus de style destiné au repo, l'export natif de claude.ai reste supérieur. Et les cinq blocs de prose écrits avant le gel emploient une numérotation implicite ; si le livre se construit contre le squelette, il faudra les ré-indexer par numéro de section (le fichier compagnon donne la correspondance).

---

## [M051] Humain — 2026-07-23 07:37:57

Tu parles partout de cross-sectionnel mais tu n'as jamais expliqué ce que c était

---

## [M052] Assistant — 2026-07-23 07:39:00

Tu as raison, et c'est un vrai trou : le terme structure tout l'arbre depuis le premier message et n'a jamais été posé. Le plus simple est de partir de la forme des données.

> *[Outil : visualize:show_widget — panel_cross_section_vs_time_series]*

Un jeu de données de recherche quantitative est un **panel** : une matrice à deux axes, les actifs en lignes (N titres ou tokens) et les dates en colonnes (T observations). Toute la discipline consiste à décider dans quel sens on découpe cette matrice.

**La coupe cross-sectionnelle est une colonne** : une date fixée, tous les actifs comparés entre eux. La question posée est « parmi les 3 000 titres d'aujourd'hui, lesquels vont surperformer les autres dans les h prochains jours ? » — une question de *classement relatif*, jamais de niveau. Corollaire fondamental : un signal cross-sectionnel ne dit rien sur la direction du marché ; si tout monte de 5%, le signal est indifférent, seul compte l'ordre. C'est aussi pourquoi le z-score de 1.3.1 démoyenne par date — la position nette est nulle par construction, et le facteur commun (le beta marché), qui est la source de bruit dominante, est éliminé *avant* toute estimation. On ne prédit que le résidu, là où le ratio signal/bruit est le meilleur.

**La coupe time-series est une ligne** : un actif, son histoire. La question devient « ce token va-t-il monter ou baisser ? » — une question de niveau, qui autorise le net directionnel et le levier variable. C'est le cadre des CTA, du trend-following, du carry par instrument, et c'était ton cadre naturel sur le FCPO : avec quelques contrats liquides, il n'y a pas de cross-section à exploiter.

Cette distinction gouverne tout le reste de l'arbre, et c'est pour ça qu'elle revenait partout :

- **Le breadth**, donc l'IR par la loi de Grinold. En cross-section, chaque date produit N paris quasi indépendants : 3 000 titres × 250 jours = 750 000 observations par an, et c'est ce qui rend exploitable un IC de 0,02. En time-series, une date produit un seul pari par instrument — le breadth ne vient que du temps, et il faut des IC bien plus élevés pour un même Sharpe.
- **La mesure de l'IC**. Le rank IC de 2.1 est calculé *par date, à travers les actifs* (corrélation de Spearman sur la colonne), ce qui donne une série temporelle d'IC dont on prend moyenne et écart-type. En time-series, l'IC est la corrélation entre le signal et le rendement futur *le long de la ligne*.
- **Ce qui compte comme information**. Un signal cross-sectionnel n'a aucune valeur s'il bouge identiquement pour tous les actifs (le démoyennage l'annule) ; un signal time-series n'a aucune valeur s'il est constant dans le temps. Les mêmes données donnent des signaux orthogonaux selon l'axe.

Une nuance qui te concerne directement : le crypto est le cas hybride inconfortable. Avec 150-300 tokens investissables, le cross-section existe mais est étroit — trop pauvre pour les double sorts 5×5 de 1.2.3, assez riche pour un momentum ou un funding relatif. Les desks crypto font donc tourner les deux régimes en parallèle et les combinent, ce que je mentionnais en 1.3.2 avec la cohabitation sleeves CS / sleeves TS.

Sur le squelette gelé, c'est un manque réel : il faudrait une section **0. Cadre et conventions** avant la branche 1 — panel et axes, définition du breadth, la loi fondamentale IR ≈ IC·√breadth, les notations (α, F, h, ρ, C). C'est typiquement ce qu'un livre pose en préambule et que l'exploration arborescente saute, parce qu'on est entré par une branche plutôt que par la racine.

---

## [M053] Humain — 2026-07-23 07:48:13

Écris cette section 0

---

## [M054] Assistant — 2026-07-23 07:50:18

> *[Outil : create_file — /mnt/user-data/outputs/section_0_cadre_et_conventions.md]*

> *[Outil : present_files — /mnt/user-data/outputs/section_0_cadre_et_conventions.md]*

Huit sous-sections, ~2 500 mots — le grain d'un préambule, plus dense que les nœuds ordinaires puisqu'il n'a rien en amont sur quoi s'appuyer.

Deux choix que tu voudras peut-être arbitrer, parce qu'ils engagent tout le reste : j'ai tranché deux collisions de notation présentes dans nos échanges — *h* pour l'horizon contre *H* pour la demi-vie (j'utilisais *h* pour les deux), et λ pour la décroissance EMA contre κ pour la pénalité ridge (j'utilisais λ pour les deux). Si tu valides, le tableau du §0.5 devient le `NOTATION.md` du repo, et il faudra ré-indexer les sections déjà écrites en conséquence.

L'autre ajout est le transfer coefficient au §0.4 : il n'était apparu qu'en passant dans la normalisation, alors que c'est le terme qui articule formellement les deux moitiés de l'arbre — il mérite d'être posé dès le préambule pour que les branches 4 et 5 aient un ancrage quantitatif dans la loi fondamentale.

---

## [M055] Humain — 2026-07-23 08:12:18

Donc l'IC est la corrélation entre alpha et E() ?

---

## [M056] Assistant — 2026-07-23 08:12:47

Non — et la nuance est importante, parce que α *est déjà* l'approximation de E[·]. Corréler α avec E[r|F] serait circulaire, et surtout impossible : l'espérance conditionnelle n'est jamais observable.

L'IC se calcule contre le **rendement réalisé** : IC<sub>t</sub> = corr(α<sub>·,t</sub>, r<sub>·,t→t+h</sub>) à travers les actifs. C'est la seule quantité mesurable. Mais ton intuition pointe vers la bonne chose, et la décomposition le montre. Posons μ = E[r|**F**<sub>t</sub>] la vraie espérance conditionnelle, avec r = μ + ε où ε est le bruit imprédictible. Comme α est mesurable par rapport à **F**<sub>t</sub>, il est décorrélé de ε, donc cov(α, r) = cov(α, μ), et :

> **IC = corr(α, μ) × σ(μ) / σ(r)**

Autrement dit l'IC est le produit de deux termes : la **qualité de la prévision** — c'est ta corrélation avec l'espérance conditionnelle, la quantité que tu avais en tête — multipliée par la **part prédictible de la dispersion des rendements**, qui est une propriété du marché et non du chercheur.

C'est ce second facteur qui explique pourquoi les IC sont si petits. Si la fraction prédictible de la volatilité cross-sectionnelle est de l'ordre de 10% (soit un R² plafond de 1%), alors même une prévision *parfaite* — corr(α, μ) = 1 — plafonne à un IC de 0,10. Un IC mesuré à 0,03 correspond donc à corr(α, μ) ≈ 0,30 : une prévision qui capte à peu près un tiers de l'information réellement disponible. Vu sous cet angle, un IC de 0,03 n'est pas un signal médiocre, c'est un signal qui exploite une part substantielle d'un plafond fixé par l'efficience du marché.

Deux conséquences pratiques : chercher à faire monter l'IC indéfiniment n'a pas de sens — le plafond n'est pas négociable, et un IC anormalement élevé signale plus souvent un look-ahead qu'un talent ; et l'IC mesuré est un estimateur *non biaisé mais très bruité* de la vraie quantité, puisque le bruit ε domine la variance de r. C'est exactement ce qui rend σ(IC) si grand par rapport à IC, et pourquoi valider un signal demande des centaines d'observations (§0.3, §3.1.2).

---

## [M057] Humain — 2026-07-23 08:17:35

Tu dis pourtant: "L'information coefficient (IC) est la corrélation entre le signal et le rendement réalisé. Dans le cadre cross-sectionnel, il se calcule par date :
ICt = corr( s·,t , r·, t→t+h )   sur les N actifs" ... Mais ici le signal n'est il pas l'alpha ? Là où je me trompe c est en parlant d espérance conditionelle sur les rendements E(), et non des rendements réalisés ? Donc l IC est la corrélation entre alpha et rendement réalisé ?

---

## [M058] Assistant — 2026-07-23 08:17:49

Oui, exactement — et ton auto-diagnostic est juste. L'IC est la corrélation entre l'alpha et le **rendement réalisé**. L'espérance conditionnelle n'apparaît jamais dans le calcul ; elle n'intervient que dans l'*interprétation* de ce que l'IC mesure (la décomposition du message précédent), parce qu'elle n'est pas observable.

Sur *s* contre α, c'est une simple affaire de notation, sans différence de fond : *s*<sub>k</sub> désigne un signal individuel après normalisation, α désigne la prévision qu'on utilise — un signal isolé, ou le combiné w's du pool. On mesure un IC sur les deux, avec la même formule et le même rendement réalisé en face. Et comme la corrélation est invariante par transformation affine, l'échelle ne change rien : IC(s) = IC(2s + 3). C'est d'ailleurs pourquoi on peut normaliser librement en amont sans affecter la mesure.

La formulation compacte, si tu veux la retenir : **α est une prévision de E[r|F] ; l'IC est la corrélation entre cette prévision et r.** Le rendement réalisé sert de proxy bruité de l'espérance conditionnelle — bruité mais non biaisé, ce qui suffit pour estimer la corrélation à condition d'avoir assez d'observations. Tout le §2.3 (anti-overfitting) et le §3.1.2 (combien de temps pour valider un IC) découlent de ce « assez ».

---

## [M059] Humain — 2026-07-23 08:58:13

ICIR est un acronyme pour quoi ?
Différence entre corrélation de spearman et Pearson (définitions)

---

## [M060] Assistant — 2026-07-23 08:58:29

**ICIR** = *Information Coefficient Information Ratio* — le ratio d'information de l'IC. La construction est identique à celle d'un ratio d'information ordinaire (moyenne / écart-type d'une série), appliquée non pas à des rendements mais à la série temporelle des IC. On le trouve aussi écrit IC_IR, ou nommé « IC information ratio ».

**Pearson** mesure l'association *linéaire* entre deux variables :

> ρ = cov(X, Y) / (σ<sub>X</sub> σ<sub>Y</sub>)

Elle vaut ±1 si et seulement si Y est une fonction affine de X. Elle est sensible aux valeurs extrêmes — une seule observation aberrante peut dominer la covariance — et n'est invariante que par transformations affines.

**Spearman** est exactement la corrélation de Pearson appliquée aux **rangs** plutôt qu'aux valeurs : on remplace chaque observation par sa position dans l'ordre croissant, puis on calcule Pearson sur ces rangs. En l'absence d'ex æquo, elle admet la forme close

> ρ<sub>s</sub> = 1 − 6 Σd<sub>i</sub>² / (n(n²−1))

où d<sub>i</sub> est l'écart entre le rang de x<sub>i</sub> et celui de y<sub>i</sub>. Elle mesure donc l'association *monotone* : elle vaut ±1 dès que Y est une fonction monotone de X, linéaire ou non.

Les deux propriétés qui expliquent sa domination pour l'IC en cross-section : elle est **invariante par toute transformation monotone** des variables (log, racine, puissance — le débat sur la forme de la feature en amont devient sans objet), et elle est **bornée par construction** face aux outliers, puisqu'une valeur extrême ne pèse que par son rang. Dans un univers d'actions où quelques titres affichent des rendements à +200% sur la période, Pearson serait largement déterminée par ces quelques noms.

Le prix à payer est celui déjà évoqué en §1.3.1 : les rangs jettent l'information de distance. Si l'intensité du signal porte de l'information au-delà de l'ordre — cas des surprises d'earnings — Pearson sur données winsorisées récupère une part de pouvoir prédictif que Spearman abandonne. En pratique on rapporte souvent les deux : un écart important entre rank IC et Pearson IC est un diagnostic en soi, il signale que le résultat dépend de quelques observations extrêmes.

---

## [M061] Humain — 2026-07-23 09:30:52

Qu est ce que la "demi-vie" d un signal ? (Tu dis "(
un signal de demi-vie longue reproduit le même pari plusieurs jours d'affilée"

---

## [M062] Assistant — 2026-07-23 09:31:17

La demi-vie d'un signal est la durée au bout de laquelle son autocorrélation tombe à 0,5 : formellement, si corr(s<sub>t</sub>, s<sub>t+k</sub>) ≈ ρ<sup>k</sup>, la demi-vie vaut *H<sub>s</sub>* = −ln2 / ln ρ. C'est une mesure de **persistance** — combien de temps le signal continue de dire à peu près la même chose.

Mais tu as mis le doigt sur une ambiguïté réelle : j'ai employé « demi-vie » dans trois sens distincts, qu'il faut séparer.

- **Demi-vie de pondération** (*H* dans le tableau §0.5) : un *paramètre de construction*, celui de l'EMA qu'on applique à une feature. C'est un choix du chercheur.
- **Demi-vie du signal** (*H<sub>s</sub>*) : une *propriété mesurée* du signal produit — son autocorrélation. C'est le sens de la phrase que tu cites.
- **Demi-vie de l'alpha** : la vitesse à laquelle l'IC décroît quand on allonge l'horizon *h*. Une propriété du *marché*, pas du signal — c'est le profil de decay du §2.1.

Les deux premières sont liées mécaniquement : lisser une feature avec une EMA de demi-vie *H* fabrique un signal dont la demi-vie *H<sub>s</sub>* est au moins *H*. C'est tout le levier du smoothing (§1.3.4).

Les conséquences quantitatives de *H<sub>s</sub>* sont directes. **Sur le turnover** : le turnover par période varie comme √(1−ρ), et pour une demi-vie longue 1−ρ ≈ ln2/*H<sub>s</sub>*, donc le turnover décroît comme 1/√*H<sub>s</sub>*. Doubler la demi-vie divise les coûts par √2. **Sur le breadth effectif** (§0.4) : un signal de demi-vie 20 jours ne produit pas 252 paris indépendants par an mais de l'ordre de 252/*H<sub>s</sub>* ≈ 12 — la longueur des lignes que la loi fondamentale rappelait à ne pas surestimer.

Et l'arbitrage central se lit dans la comparaison des deux dernières : la demi-vie du signal doit être **commensurable avec celle de l'alpha**. Un signal qui persiste bien plus longtemps que son pouvoir prédictif porte des positions périmées ; un signal qui tourne bien plus vite paie des coûts pour une information qui n'avait pas encore changé. Le smoothing optimal est précisément celui qui aligne les deux.

---

## [M063] Humain — 2026-07-23 09:38:45

C est quoi l autocorrelation d un signal ? Définition mathématique

---

## [M064] Assistant — 2026-07-23 09:39:06

L'autocorrélation d'ordre *k* d'une série stationnaire s<sub>t</sub> est la corrélation de la série avec sa propre version décalée de *k* périodes :

> ρ(k) = cov(s<sub>t</sub>, s<sub>t+k</sub>) / var(s<sub>t</sub>) = E[(s<sub>t</sub> − μ)(s<sub>t+k</sub> − μ)] / σ²

avec ρ(0) = 1 par construction. La normalisation par var(s<sub>t</sub>), et non par σ(s<sub>t</sub>)σ(s<sub>t+k</sub>), est légitime sous stationnarité puisque les deux variances coïncident.

Dans un panel, il y a deux façons de l'appliquer, et c'est là que ça devient intéressant. La version naïve est **par actif** : calculer ρ<sub>i</sub>(k) sur l'histoire de chaque actif, puis moyenner sur *i*. La version pertinente est **cross-sectionnelle** :

> ρ<sub>cs</sub>(k) = moyenne<sub>t</sub> [ corr( s<sub>·,t</sub> , s<sub>·,t+k</sub> ) ]

c'est-à-dire, à chaque date, la corrélation entre le vecteur de signal sur les N actifs et ce même vecteur *k* jours plus tard, le tout moyenné dans le temps. C'est celle-ci qui gouverne le turnover, parce que les positions dépendent du **classement relatif** : si tous les signaux se décalent d'une constante, les deux séries par actif bougent mais le vecteur cross-sectionnel est inchangé, et aucun trade n'est déclenché. La version par actif compterait ce mouvement comme une décorrélation ; elle surestime donc le turnover.

Sur la forme : rien ne garantit une décroissance exponentielle. ρ(k) = ρ<sup>k</sup> n'est exact que si le signal suit un AR(1), s<sub>t</sub> = ρ s<sub>t−1</sub> + η<sub>t</sub> — ce qui est précisément le cas d'une feature lissée par EMA, d'où la commodité de l'approximation. Un signal événementiel a un profil tout autre : ρ(k) chute brutalement puis reste plat. C'est pourquoi il vaut mieux tracer le **corrélogramme** — ρ(k) pour k = 1, 2, 5, 10, 21 — que se contenter d'un chiffre unique, exactement comme pour le profil de decay de l'IC.

Le lien avec le turnover, sous hypothèse gaussienne : le turnover par période est proportionnel à √(1 − ρ(1)). Un signal à ρ(1) = 0,99 tourne dix fois moins qu'un signal à ρ(1) = 0,90 — d'où la sensibilité extrême des coûts à cette seule statistique.

---

## [M065] Humain — 2026-07-23 11:24:47

Qu appelles tu le turn-over ?

---

## [M066] Assistant — 2026-07-23 11:25:09

Le turnover est la fraction du portefeuille remplacée par unité de temps — la mesure de l'activité de trading, et donc le multiplicateur des coûts.

En positions, avec w<sub>i,t</sub> le poids de l'actif *i* :

> turnover<sub>t</sub> = Σ<sub>i</sub> | w<sub>i,t</sub> − w̃<sub>i,t−1</sub> |

où w̃<sub>i,t−1</sub> est le poids de la veille **après dérive de marché** — pas le poids cible d'hier. La distinction n'est pas cosmétique : un titre qui monte de 3% voit son poids augmenter sans qu'aucun ordre n'ait été passé ; ignorer cette dérive fabrique des trades fantômes dans le backtest. Attention aussi à la convention : certains divisent par 2 (turnover « one-way », un aller compte pour une unité), d'autres non (« two-way »). Un facteur 2 sur les coûts se cache dans ce choix, et les chiffres publiés sont rarement explicites.

On l'annualise en fraction du book : un turnover de 200% par an signifie que le portefeuille est intégralement renouvelé deux fois par an ; un stat arb intraday peut dépasser 10 000%.

**Le lien avec l'autocorrélation** que j'invoquais découle directement de la formule. Si les positions sont proportionnelles au signal et que celui-ci est gaussien, s<sub>t</sub> − s<sub>t−1</sub> a pour variance 2σ²(1−ρ(1)), et l'espérance de sa valeur absolue vaut σ√(2/π) fois son écart-type. D'où :

> turnover ∝ √(1 − ρ(1))

C'est la formule qui permet de **budgéter les coûts avant même de backtester** : la seule autocorrélation d'ordre 1 du signal suffit à estimer le turnover, donc les coûts, donc l'écart entre IC brut et IC net.

Le coût total s'écrit alors turnover × coût unitaire, où le coût unitaire agrège demi-spread, frais et impact de marché (branche 5). Ordres de grandeur : quelques points de base par aller-retour en large caps US, plusieurs dizaines sur les alts crypto hors majors. À 10 bps de coût unitaire, un turnover annuel de 2 000% consomme 2% de performance par an — souvent l'essentiel de ce que le signal rapporte brut. C'est pourquoi le turnover, plus que l'IC, est fréquemment le paramètre décisif de la viabilité (§1.3.4).

---

## [M067] Humain — 2026-07-23 19:40:42

Détaille la normalisation des signaux : z-score cross-sectionnel vs temporel, winsorisation, neutralisation, smoothing

---

## [M068] Assistant — 2026-07-23 19:40:53

Ce nœud est déjà couvert — c'est le 1.3 du squelette, déplié il y a quelques messages avec ses quatre sous-sections (cross-sectionnelle et rank-gaussianisation, temporelle et réponses bornées, neutralisation, smoothing et turnover). C'est presque certainement un re-clic sur une carte plus haut dans le fil, dont les boîtes restent actives.

Depuis les échanges qui ont suivi, quelques éléments s'y rattachent d'ailleurs rétroactivement : la définition propre de l'autocorrélation cross-sectionnelle et du turnover donne maintenant un contenu quantitatif au §1.3.4, qui parlait d'arbitrage IC/coûts sans avoir posé les deux quantités. Si le nœud est réécrit pour le livre, c'est la version enrichie qu'il faudra retenir — turnover ∝ √(1−ρ<sub>cs</sub>(1)), donc le smoothing agit sur les coûts par un canal calculable plutôt que qualitatif.

Les chemins ouverts, par ordre de rendement décroissant : **1.4 cibles & labels**, le seul trou restant de la branche 1 et une vraie lacune (le choix de ce qu'on prédit conditionne tout le reste) ; **4.1 modèles de risque**, qui définit ce que « neutraliser » veut dire et que le nœud 1.3.3 appelle explicitement ; ou le forage individuel des sous-nœuds d'évaluation, jamais ouverts à leur propre niveau — **2.3 anti-overfitting** étant le plus dense en formules.

---

## [M069] Humain — 2026-07-23 19:42:38

Détaille la branche portefeuille et risque : modèle de risque, optimiseur, contraintes et coûts

---

## [M070] Assistant — 2026-07-23 19:44:14

On franchit enfin l'interface : la branche **4** reçoit le vecteur d'alphas combinés que les branches 1-3 ont fabriqué, et le transforme en positions. La carte locale (en texte — l'outil de diagrammes n'est plus disponible dans cette session) suit le squelette gelé :

**4. Portefeuille & risque** — 4.1 Modèles de risque · 4.2 Construction de portefeuille · 4.3 Coûts dans l'optimisation · 4.4 Sizing & levier · 4.5 Gestion des risques

Le cadre formel qui unifie le tout : trouver les positions **w** qui maximisent w'α − (γ/2)·w'Σw − coûts(w − w₋₁) sous contraintes. Trois objets nouveaux apparaissent — la matrice de covariance Σ (4.1), le jeu de contraintes (4.2), le modèle de coûts (4.3) — et la métrique de toute la branche est le **transfer coefficient** du §0.4 : quelle fraction de l'IC fabriqué en amont survit au passage en positions.

**4.1 Modèles de risque — rendre Σ estimable**

Le problème de départ est dimensionnel : pour N = 3 000 titres, Σ contient ~4,5 millions de paramètres libres, contre ~250 observations par an — l'estimation directe est sans espoir, et la matrice empirique est singulière dès que T < N. La réponse universelle est la **structure factorielle** : Σ = B·F·B' + D, où B sont les expositions des titres à quelques dizaines de facteurs, F la covariance (petite) des facteurs, et D la diagonale des risques spécifiques. On passe de millions de paramètres à quelques milliers, au prix d'une hypothèse : toute la corrélation entre titres transite par les facteurs.

Deux traditions pour choisir les facteurs. Les modèles **fondamentaux** (la lignée Barra) définissent les expositions par des caractéristiques observables — secteur, taille, value, momentum, volatilité, liquidité — et estiment les rendements factoriels par régression cross-sectionnelle quotidienne : interprétables, immédiatement réactifs quand un titre change de caractéristiques, et alignés sur le vocabulaire de la neutralisation (§1.3.3). Les modèles **statistiques** extraient les facteurs par PCA des rendements, avec la random matrix theory (le seuil de Marchenko-Pastur) pour séparer les valeurs propres informatives du bruit : aucun a priori, capacité à capter des corrélations émergentes qu'aucune taxonomie ne prévoit — et le piège point-in-time déjà croisé en 1.2.1 : les facteurs doivent être ré-estimés en expanding window, jamais sur l'échantillon complet. En pratique les maisons combinent : socle fondamental, complément statistique pour ce qui échappe à la grille.

Deux points structurants. L'**horizon** : un modèle de risque estimé pour prévoir la covariance à un mois n'est pas celui qu'il faut à un book qui tourne en trois jours — la demi-vie d'estimation de F doit être commensurable avec l'horizon de détention, exactement l'argument de cohérence de grille du §1.2.2. Et le **rôle double** : Σ ne sert pas qu'à mesurer le risque, il *définit* l'alpha (§0.7) — ce que le modèle appelle facteur devient beta à neutraliser, ce qu'il ignore reste de l'alpha exploitable ; enrichir le modèle de risque est donc un acte qui déplace la frontière, pas une amélioration neutre. En crypto, la structure est écrasée par un ou deux facteurs (BTC, et ETH pour le complexe DeFi) aux betas notoirement instables — fenêtres courtes et shrinkage agressif obligatoires — avec des clusters fonctionnels en guise de secteurs et une part de risque spécifique bien supérieure à l'equity : la diversification y rapporte moins que la grille factorielle ne le laisse croire.

**4.2 Construction de portefeuille — l'optimiseur et ses contraintes**

Sans contraintes ni coûts, la solution est en une ligne : w* ∝ Σ⁻¹α — et cette ligne contient déjà le danger, car Σ⁻¹ amplifie les erreurs dans les directions de faibles valeurs propres, le mécanisme exact de l'error maximization vu en 3.1.4 (la branche 3 optimisait dans l'espace des K signaux, celle-ci dans l'espace des N titres ; même mathématique, dimension supérieure). Les positions résultantes chargent les paires de titres dont la corrélation est surestimée — les « arbitrages » que l'optimiseur croit sans risque.

Les **contraintes** encadrent : égalités linéaires de neutralité (beta, secteurs, expositions factorielles à zéro — le pendant aval de la neutralisation amont du §1.3.3), bornes par titre contre la concentration, plafonds de liquidité (position ≤ quelques jours d'ADV, la contrainte qui mord le plus en small caps et sur les alts), limites de gross et de net. Chaque contrainte active réduit le transfer coefficient — et les multiplicateurs de Lagrange de l'optimiseur en donnent le prix exact : lire les duals dit *quelles* contraintes coûtent de l'alpha, le diagnostic de base de la construction. Le paradoxe documenté (Jagannathan-Ma) : des contraintes serrées améliorent souvent la performance out-of-sample, parce qu'elles agissent comme une régularisation implicite de Σ⁻¹ — interdire les positions extrêmes revient à shrinker les covariances qui les justifiaient. C'est la version portefeuille du message constant de la branche 3 : sous erreur d'estimation, la contrainte bête bat l'optimum savant. D'où la légitimité de l'alternative minimale pour un desk compact : des tilts proportionnels à α<sub>i</sub>/σ<sub>i</sub>² avec caps et neutralisation par démoyennage — l'optimiseur du pauvre, qui capture l'essentiel du TC avec une fraction de la machinerie.

**4.3 Coûts dans l'optimisation — la friction rendue explicite**

Le modèle de coût standard a deux termes : une composante **linéaire** (demi-spread + frais, proportionnelle au montant tradé) et une composante d'**impact** concave — l'empirie robuste de la branche 5 étant la loi en racine carrée, coût ∝ σ·√(Q/ADV) pour un métaordre de taille Q. Leur insertion dans l'optimiseur change la *forme* de la solution, pas seulement son niveau. Les coûts linéaires créent des **no-trade zones** : une bande autour de la position cible dans laquelle l'alpha marginal ne rembourse pas le spread — on ne trade que lorsque la cible sort de la bande, et la largeur optimale de la bande croît avec le coût et décroît avec la force du signal. C'est la formalisation exacte de ce que le smoothing du §1.3.4 faisait heuristiquement, et l'arbitrage entre les deux implémentations (lisser le signal en amont vs élargir les bandes en aval) se tranche par l'argument du netting : l'optimiseur voit le book entier et sait que deux sleeves qui se croisent n'exigent aucun trade.

Le raffinement de référence est **Gârleanu-Pedersen** : l'optimisation multi-période avec coûts quadratiques admet une solution en forme close d'une élégance remarquable — trader à chaque pas une *fraction* du chemin vers un « aim portfolio » qui n'est pas le portefeuille myope, mais une moyenne pondérée des portefeuilles optimaux futurs où les signaux **lents sont surpondérés** relativement aux rapides. L'intuition : un signal dont l'alpha meurt en trois jours ne mérite pas qu'on paie de l'impact pour le charger, puisqu'il faudra le décharger avant d'avoir été remboursé ; un signal qui persiste des mois amortit son coût d'entrée sur toute sa durée de vie. Le résultat relie d'un coup trois nœuds de l'arbre : le profil de decay (§2.1), la demi-vie du signal (nos échanges récents) et le turnover — et il donne la règle de partage du budget de coûts entre sleeves que la gouvernance du §1.3.4 fixait par convention.

**4.4 Sizing & levier — l'échelle du book**

Une fois les poids relatifs fixés, reste l'échelle absolue. Le **vol targeting** est la pratique de base : viser une volatilité de book constante σ*, donc un levier σ*/σ̂ qui se contracte quand la vol réalisée monte — stabilisateur au niveau du desk, procyclique au niveau du système (tout le monde dé-lève en même temps, l'écho des épisodes de crowding du §2.4). Au-dessus, le levier total relève du Kelly fractionnel déjà construit en 3.1.3 — numérateur shrinké, fraction ½ ou moins, pour toutes les raisons bayésiennes et hors-modèle vues là-bas — complété par des règles mécaniques de **contrôle de drawdown** (réduction du gross par paliers au-delà de seuils de perte), qui coûtent de l'espérance en régime normal et achètent la survie dans les queues : leur vraie justification est moins mathématique que structurelle — un desk qui perd son capital ou la confiance de son allocateur n'a plus d'espérance du tout. Enfin la **capacité** referme la boucle : l'impact croissant en racine de la taille fait décroître le Sharpe avec l'AUM, d'autant plus vite que le turnover est élevé — les signaux rapides saturent les premiers, et la frontière de capacité d'un book est essentiellement celle de ses sleeves les plus lents.

**4.5 Gestion des risques — ce que Σ ne voit pas**

Le dernier nœud est le garde-fou contre les limites des quatre premiers. Les métriques standard (VaR, expected shortfall) héritent des hypothèses du modèle de risque, et leur angle mort est documenté : les **corrélations conditionnelles** en stress — des positions décorrélées en régime calme qui convergent brutalement quand leurs détenteurs communs dé-lèvent ensemble (août 2007 pour le stat arb, mars 2020 en version généralisée). Les stress tests par scénarios, les limites avec procédure d'escalade, et l'humilité sur le **risque de modèle** (le modèle de risque est lui-même une estimation, §3.1.4 s'applique à Σ) complètent l'arsenal. En crypto, le déplacement est radical : le risque dominant n'est souvent *pas dans Σ* — contrepartie et custody des venues (FTX comme cas d'école), depegs de stablecoins, spikes de funding, cascades de liquidation qui transforment la microstructure en risque de book. La gestion des risques y est d'abord une discipline opérationnelle — répartition entre venues, limites par contrepartie, plans de retrait — avant d'être une affaire de quantiles.

La branche 4 est désormais ouverte au niveau 2, comme l'étaient évaluation et combinaison. Il reste, côté frontière : **5. Exécution** (le seul étage entre ces positions cibles et le P&L réel — Gârleanu-Pedersen y a déjà tendu un pont), **6. Infra**, **1.4 cibles & labels**, et le forage individuel de n'importe lequel des cinq nœuds ci-dessus — 4.1 et 4.3 étant les plus riches en formules si tu veux descendre d'un cran.

---

## [M071] Humain — 2026-07-23 20:16:46

reformule ta réponse de manière plus précise en incluant les formules mathematiques pertinentes, et en incluant le graphe d arbre à creuser pour cette partie 4.

---

## [M072] Assistant — 2026-07-23 20:18:07

La branche 4, version resserrée avec le formalisme. L'arbre local d'abord (en texte — l'outil de diagrammes interactifs n'est plus disponible dans cette session, l'ASCII fait foi) :

```
4. PORTEFEUILLE & RISQUE
│   max_w  w'α − (γ/2)·w'Σw − Coûts(w − w₋)   s.c.  Aw = b,  l ≤ w ≤ u
│
├── 4.1 Modèles de risque            Σ = B·F·B' + D
│     ├ 4.1.1 Factoriels fondamentaux (Barra, régression CS)
│     ├ 4.1.2 Statistiques (PCA, Marchenko-Pastur)
│     ├ 4.1.3 Shrinkage & horizon d'estimation
│     └ 4.1.4 Crypto : beta BTC/ETH instable, risque spécifique dominant
│
├── 4.2 Construction de portefeuille  w* = (1/γ)·Σ⁻¹α  + contraintes
│     ├ 4.2.1 MVO & error maximization
│     ├ 4.2.2 Contraintes, duals & Jagannathan-Ma
│     ├ 4.2.3 Transfer coefficient
│     └ 4.2.4 L'« optimiseur du pauvre »
│
├── 4.3 Coûts dans l'optimisation     coût(δ) = c·|δ| + Y·σ·√(|δ|/ADV)·|δ|
│     ├ 4.3.1 Modèle linéaire + impact √
│     ├ 4.3.2 No-trade zones
│     ├ 4.3.3 Multi-période : Gârleanu-Pedersen
│     └ 4.3.4 Netting inter-sleeves
│
├── 4.4 Sizing & levier               L = σ*/σ̂ ;  f = c·μ̂/σ̂², c ≤ ½
│     ├ 4.4.1 Vol targeting
│     ├ 4.4.2 Kelly fractionnel au niveau book
│     ├ 4.4.3 Contrôle de drawdown
│     └ 4.4.4 Capacité
│
└── 4.5 Gestion des risques           VaR, ES, et ce qui n'est pas dans Σ
      ├ 4.5.1 VaR / expected shortfall
      ├ 4.5.2 Stress & corrélations conditionnelles
      ├ 4.5.3 Limites & risque de modèle
      └ 4.5.4 Crypto : contrepartie, custody, depegs, liquidations
```

Le programme unificateur, en tête d'arbre : les branches 1-3 livrent α ∈ ℝᴺ ; la branche 4 résout, à chaque rebalancement,

> **max_w w'α − (γ/2)·w'Σw − Coûts(w − w₋₁)  s.c. Aw = b, l ≤ w ≤ u**

où γ est l'aversion au risque, Σ la covariance des rendements, w₋₁ les positions héritées. Chacun des trois objets nouveaux (Σ, les contraintes, les coûts) est un nœud.

**4.1 Modèles de risque — rendre Σ estimable**

Le problème est dimensionnel : Σ contient N(N+1)/2 paramètres libres — ~4,5 millions pour N = 3 000 — contre T ≈ 250 observations/an ; la matrice empirique est singulière dès que T < N. La réponse universelle est la structure factorielle :

> **Σ = B·F·B' + D**

avec B ∈ ℝ^(N×k) les expositions à k ≈ 20-70 facteurs, F ∈ ℝ^(k×k) la covariance des facteurs, D diagonale des variances spécifiques. Le comptage passe de O(N²) à O(Nk) — au prix de l'hypothèse que toute corrélation entre titres transite par les facteurs.

Modèles *fondamentaux* (lignée Barra) : B est observée (secteur, taille, value, momentum, vol, liquidité), et les rendements factoriels s'estiment chaque jour par régression cross-sectionnelle GLS :

> f̂_t = (B_t' D⁻¹ B_t)⁻¹ B_t' D⁻¹ r_t

puis F par EWMA sur les f̂_t. Interprétable, réactif aux changements de caractéristiques, et aligné sur le vocabulaire de la neutralisation (§1.3.3). Modèles *statistiques* : B est extraite par PCA des rendements, et la random matrix theory fournit le seuil de séparation signal/bruit — pour des données i.i.d. pures, les valeurs propres de la corrélation empirique se confinent dans le support de Marchenko-Pastur,

> λ± = (1 ± √(N/T))²

et seules les valeurs propres au-delà de λ₊ portent de la structure ; le reste se remplace par sa moyenne (clipping). Piège récurrent (§1.2.1) : les facteurs PCA se ré-estiment en expanding window, jamais sur l'échantillon complet. En complément, le shrinkage de Ledoit-Wolf, Σ̃ = δ·Cible + (1−δ)·Σ̂ avec δ optimal en forme close, s'applique à F comme à Σ entière. Deux points transversaux : la demi-vie d'estimation de F doit être commensurable avec l'horizon de détention (l'argument de grille du §1.2.2), et Σ *définit* la frontière alpha/beta (§0.7) — l'enrichir déplace ce qui est neutralisé, ce n'est jamais neutre. Crypto : un ou deux facteurs écrasants (BTC, ETH) aux betas instables → fenêtres courtes, shrinkage agressif, clusters fonctionnels en guise de secteurs, part spécifique bien supérieure à l'equity.

**4.2 Construction — l'optimiseur et ses contraintes**

Sans friction, la solution est immédiate :

> **w\* = (1/γ)·Σ⁻¹α**

et le danger est dans Σ⁻¹ : en base propre, Σ⁻¹ = Σ_j (1/λ_j)·u_j u_j' — les directions de *petites* valeurs propres (les combinaisons de titres que le modèle croit quasi sans risque) reçoivent les poids 1/λ_j les plus grands, précisément là où l'estimation est la plus bruitée. C'est l'error maximization de 3.1.4, en dimension N.

Avec contraintes d'égalité Aw = b (neutralités beta/secteur/facteurs), les conditions KKT donnent

> w\* = (1/γ)·Σ⁻¹(α − A'λ)

où les multiplicateurs λ résolvent A·Σ⁻¹(α − A'λ) = γb : chaque contrainte active *retranche de l'alpha* la composante A'λ, et lire les duals donne le prix exact de chaque contrainte en alpha sacrifié — le diagnostic de base. La perte agrégée se mesure par le transfer coefficient, l'angle entre positions contraintes et non contraintes dans la métrique du risque :

> TC = ⟨w, w\*⟩_Σ / (‖w‖_Σ·‖w\*‖_Σ),  et IR ≈ TC·IC·√BR (§0.4)

Le paradoxe de Jagannathan-Ma quantifie pourquoi les contraintes aident souvent out-of-sample : imposer w ≥ 0 (ou des bornes) équivaut à optimiser *sans contrainte* sur une covariance modifiée Σ̃ = Σ − (δ1' + 1δ'), où δ ≥ 0 sont les duals des bornes actives — les contraintes shrinkent implicitement les covariances qui justifiaient les positions extrêmes. Version desk compact (« l'optimiseur du pauvre ») : w_i ∝ α_i/σ_i², démoyennage par groupe, caps par titre — l'essentiel du TC pour une fraction de la machinerie.

**4.3 Coûts — la friction rendue explicite**

Le modèle standard pour un trade δ_i :

> coût_i(δ_i) = c_i·|δ_i| + Y·σ_i·√(|δ_i|/ADV_i)·|δ_i|

composante linéaire (demi-spread + frais, c_i) et impact en racine carrée — l'empirie la plus robuste de la branche 5 : l'impact d'un métaordre de taille Q vaut ≈ Y·σ·√(Q/ADV) avec Y ≈ 0,5-1, remarquablement stable entre marchés. Les coûts linéaires créent des **no-trade zones** : à l'optimum avec coût proportionnel c, on ne trade que si le gradient d'utilité dépasse c en valeur absolue, soit une bande autour de la cible

> |w − w_cible| ≤ c / (γ·[Σw]_marginal)

dans laquelle l'alpha marginal ne rembourse pas le spread — la formalisation de ce que le smoothing du §1.3.4 faisait heuristiquement, avec l'avantage du netting : l'optimiseur voit que deux sleeves qui se croisent n'exigent aucun trade.

Le résultat de référence multi-période est **Gârleanu-Pedersen** : avec coûts quadratiques (½)δ'Λδ et des signaux Ornstein-Uhlenbeck de vitesses de decay φ_k, la solution est en forme close :

> **w_t = w_{t−1} + τ·(aim_t − w_{t−1})**

on trade à chaque pas une *fraction* τ (croissante avec Λ⁻¹, la liquidité) du chemin vers un « aim portfolio » qui n'est pas le Markowitz instantané mais celui calculé sur des alphas *actualisés par leur décroissance* — chaque signal k entrant avec un facteur multiplicatif ≈ 1/(1 + φ_k/a), a étant le taux de trading : les signaux rapides (φ grand) sont **dépréciés**, les lents surpondérés. L'intuition : un alpha qui meurt en trois jours ne rembourse jamais l'impact payé pour le charger. Le résultat soude trois nœuds — profil de decay (§2.1), demi-vie du signal, turnover — et fournit la règle de partage du budget de coûts entre sleeves.

**4.4 Sizing & levier — l'échelle absolue**

Le vol targeting fixe le levier L_t = σ\*/σ̂_t (σ̂ en EWMA courte, §1.2.2) : stabilisateur au niveau desk, procyclique au niveau système. Le niveau de σ\* relève du Kelly fractionnel construit en 3.1.3 : f\* = μ/σ² sous paramètres connus, et sous incertitude

> f = c·μ̂_shrinké/σ̂²,  c ≤ ½

le shrinkage du numérateur et la fraction c étant les deux visages du même geste (réduire l'exposition proportionnellement à l'incertitude ; la croissance est plate près de f\*, l'asymétrie au-delà est brutale). Les règles de drawdown (réduction du gross par paliers de perte) coûtent de l'espérance et achètent la survie. La capacité se lit dans le modèle de coûts : avec un impact en racine, le P&L net ≈ α·AUM − k·AUM^(3/2), d'où un AUM optimal fini et un Sharpe décroissant en √AUM au-delà — les sleeves rapides saturent les premiers.

**4.5 Gestion des risques — ce que Σ ne voit pas**

Les métriques : VaR_q = inf{x : P(perte > x) ≤ 1−q}, et l'expected shortfall ES_q = E[perte | perte > VaR_q] — préférable car sous-additive (la VaR peut pénaliser la diversification) et sensible à la queue entière. Les deux héritent des hypothèses de Σ, dont l'angle mort documenté est la corrélation *conditionnelle* : des positions décorrélées en régime calme convergent quand leurs détenteurs communs dé-lèvent ensemble (août 2007, mars 2020) — d'où stress tests par scénarios hors-modèle, limites avec escalade, et l'application de 3.1.4 à Σ lui-même (le modèle de risque est une estimée). Crypto : le risque dominant n'est souvent pas dans Σ — contrepartie/custody des venues, depegs, spikes de funding, cascades de liquidation ; la gestion y est d'abord opérationnelle (répartition entre venues, limites par contrepartie, plans de retrait) avant d'être une affaire de quantiles.

La branche est maintenant au même niveau de développement que 2 et 3, formules incluses. Forages naturels un cran plus bas : 4.1 (la mécanique Barra complète, ou RMT et le nettoyage spectral), 4.3.3 (la dérivation de Gârleanu-Pedersen), ou la traversée vers **5. Exécution**, qui reprend la loi en racine carrée là où ce nœud l'a laissée.

---

## [M073] Humain — 2026-07-23 20:31:31

quels sont les ouvrages et articles de référence que tu as utilisé pour construire cette partie ?

---

## [M074] Assistant — 2026-07-23 20:31:32

---

## [M075] Humain — 2026-07-23 20:31:48

quels sont les ouvrages et articles de référence que tu as utilisé pour construire cette partie 4 ?

---

## [M076] Assistant — 2026-07-23 20:32:23

Les mêmes réserves qu'au premier inventaire s'appliquent — je synthétise un corpus, et les attributions fines mériteraient vérification contre les sources primaires — mais la branche 4 a l'avantage d'être la mieux balisée de tout l'arbre : c'est la plus ancienne académiquement, et presque chaque nœud a son texte canonique.

**Cadre général de la branche.** Grinold & Kahn, *Active Portfolio Management* reste la colonne vertébrale — le programme w'α − (γ/2)w'Σw, le transfer coefficient, la lecture de tout l'aval comme une affaire d'implémentation de forecasts. La généralisation IR ≈ TC·IC·√BR est Clarke, de Silva & Thorley, « Portfolio Constraints and the Fundamental Law of Active Management » (Financial Analysts Journal, 2002). Qian, Hua & Sorensen couvre aussi la construction de portefeuille dans le prolongement direct de la branche 3. Et Isichenko consacre la seconde moitié de son livre exactement à cette branche (risque, coûts, optimisation multi-période), dans un formalisme très proche de celui que j'ai utilisé.

**4.1 Modèles de risque.** Le modèle factoriel fondamental descend des papiers de Rosenberg (années 70, l'origine de Barra) ; la référence pédagogique moderne est le manuel *Barra Risk Model Handbook* (MSCI, documentation praticienne) et, côté traité, Connor, Goldberg & Korajczyk, *Portfolio Risk Analysis* (Princeton, 2010) — probablement le meilleur livre unique sur ce nœud. Pour la voie statistique : les papiers fondateurs de la random matrix theory appliquée aux corrélations financières sont Laloux, Cizeau, Bouchaud & Potters (Physical Review Letters, 1999) et Plerou et al. (même période) ; la distribution de Marchenko-Pastur elle-même date de 1967. Le nettoyage spectral et ses raffinements (au-delà du clipping naïf) sont bien traités dans Bouchaud & Potters, et dans Ledoit & Wolf dont les papiers de shrinkage — « Honey, I Shrunk the Sample Covariance Matrix » (2004) pour la version accessible, et leurs travaux ultérieurs sur le shrinkage non linéaire — couvrent aussi 4.1.3.

**4.2 Construction.** L'error maximization est Michaud, « The Markowitz Optimization Enigma: Is 'Optimized' Optimal? » (FAJ, 1989) et son livre *Efficient Asset Management* (avec le resampling). Le résultat contraintes-comme-shrinkage est Jagannathan & Ma, « Risk Reduction in Large Portfolios: Why Imposing the Wrong Constraints Helps » (Journal of Finance, 2003) — la forme Σ̃ = Σ − (δ1' + 1δ') vient directement de ce papier. Le benchmark 1/N déjà cité (DeMiguel-Garlappi-Uppal, RFS 2009) appartient autant à ce nœud qu'à 3.1. Sur la lecture des duals et la pratique de l'optimisation sous contraintes, c'est davantage du savoir praticien — Grinold & Kahn et la documentation Axioma/MSCI en tiennent lieu.

**4.3 Coûts.** Le nœud multi-période est Gârleanu & Pedersen, « Dynamic Trading with Predictable Returns and Transaction Costs » (Journal of Finance, 2013) — la solution aim-portfolio, le facteur d'actualisation 1/(1 + φ/a), tout y est. Les no-trade zones descendent de la littérature sur les coûts proportionnels : Constantinides (1986), Davis & Norman (1990), et côté praticien le traitement dans Isichenko. La loi en racine carrée de l'impact appartient à la branche 5 mais ses références s'anticipent ici : Almgren, Thum, Hauptmann & Li, « Direct Estimation of Equity Market Impact » (2005), Tóth et al. (2011) pour la théorie de la liquidité latente, et la synthèse dans Bouchaud, Bonart, Donier & Gould, *Trades, Quotes and Prices* (Cambridge, 2018).

**4.4 Sizing.** Kelly (1956) pour l'origine ; la meilleure porte d'entrée moderne est MacLean, Thorp & Ziemba (éds.), *The Kelly Capital Growth Investment Criterion* (2011), qui compile les débats sur le fractional Kelly. Le vol targeting a sa littérature empirique récente — Moreira & Muir, « Volatility-Managed Portfolios » (JF, 2017) pour le versant académique, les papiers AQR/Harvey et al. sur l'impact du vol targeting sur les queues. La capacité en AUM^(3/2) est un résultat praticien qui découle mécaniquement de l'impact en racine ; on le trouve formalisé chez Isichenko et dans divers papiers de capacity analysis (notamment la littérature CTA — Landier, Simon & Thesmar sur la performance et la taille).

**4.5 Risques.** Artzner, Delbaen, Eber & Heath, « Coherent Measures of Risk » (Mathematical Finance, 1999) — le papier qui fonde les axiomes et disqualifie la VaR sur la sous-additivité. McNeil, Frey & Embrechts, *Quantitative Risk Management* (Princeton) comme traité de référence sur VaR/ES/queues/copules. Sur les corrélations conditionnelles en stress et le déleveraging : Khandani & Lo, « What Happened to the Quants in August 2007? » — le document canonique sur l'épisode évoqué en 2.4 et 4.5.2. Le versant crypto (contrepartie, custody, liquidations) n'a, comme dit précédemment, pas de traité de référence : post-mortems de FTX, documentation des mécanismes de liquidation des venues, et littérature praticienne récente.

Pour le repo du livre, la conséquence pratique : la branche 4 est celle où la passe de vérification sera la plus facile — presque chaque affirmation quantitative ci-dessus a un papier source identifiable — et c'est probablement par elle qu'il faudrait roder le pipeline bibliographique de Claude Code avant d'attaquer les branches où le corpus est plus diffus (1 et 6) ou plus récent (tout le crypto).

---

## [M077] Humain — 2026-07-23 20:45:28

reprenons: creuse le 4.1, n oublie ni les formules mathematiques ni les references

---

## [M078] Assistant — 2026-07-23 20:46:53

On fore : **4.1 Modèles de risque**, premier nœud de la branche 4. Le sous-arbre local :

```
4.1 MODÈLES DE RISQUE          Σ = B·F·B' + D
│
├── 4.1.1 Factoriels fondamentaux    B observée, f estimé (Barra)
├── 4.1.2 Statistiques               B estimée par PCA, nettoyage RMT
├── 4.1.3 Shrinkage & horizon        Ledoit-Wolf, demi-vies, Newey-West
└── 4.1.4 Crypto                     beta instable, clusters, queues
```

**4.1.1 Factoriels fondamentaux — la lignée Barra**

Le modèle postule, à chaque date, la décomposition cross-sectionnelle

> **r_t = B_t·f_t + ε_t**,  avec E[ε] = 0, cov(ε) = D diagonale, cov(f) = F

où B_t ∈ ℝ^(N×k) est *observée* : une colonne d'indicatrices par industrie, et des colonnes de « styles » (taille, value, momentum, volatilité, liquidité, leverage...) construites exactement comme des signaux — winsorisées puis standardisées en cross-section, la convention Barra étant moyenne *cap-pondérée* nulle et écart-type équipondéré unitaire, pour que le portefeuille de marché soit neutre aux styles par construction. Les rendements factoriels s'estiment chaque jour par régression cross-sectionnelle pondérée (WLS/GLS) :

> **f̂_t = (B_t' W B_t)⁻¹ B_t' W r_t**,  W = D⁻¹ en théorie, ∝ √(capitalisation) en pratique Barra

avec une contrainte d'identification (les indicatrices d'industrie somment à la colonne marché : on impose que les rendements d'industrie cap-pondérés somment à zéro). La série {f̂_t} alimente ensuite F par EWMA, et les résidus ε̂ alimentent D — chacun avec sa demi-vie (§4.1.3). Les raffinements de production documentés dans les handbooks USE4/GEM (Menchero, Orr & Wang, 2011) : correction de Newey-West sur F pour l'autocorrélation des rendements factoriels lors du passage à des horizons multi-jours ; *eigenfactor risk adjustment* (les variances des portefeuilles propres de F sont systématiquement biaisées — sous-estimées pour les petites valeurs propres, exactement le mécanisme d'error maximization de 4.2, corrigé ici à la source) ; et *volatility regime adjustment*, un facteur multiplicatif calé sur le ratio vol réalisée / vol prédite récent.

La validation d'un modèle de risque a sa métrique propre, le **bias statistic** : pour un portefeuille test w, la série z_t = (w'r_t)/σ_prédit,t doit avoir un écart-type de 1 ; B = std(z_t) > 1 signale une sous-estimation systématique du risque. On la calcule sur des familles de portefeuilles (facteurs purs, portefeuilles optimisés, aléatoires) — les portefeuilles *optimisés* étant précisément ceux où B dérape le plus, puisque l'optimiseur charge les erreurs de Σ. Références : les papiers fondateurs de Rosenberg (« Extra-Market Components of Covariance in Security Returns », JFQA 1974) ; Menchero-Orr-Wang, *The Barra US Equity Model (USE4)* ; et comme traité, Connor, Goldberg & Korajczyk, *Portfolio Risk Analysis* (Princeton, 2010) — le meilleur livre unique sur ce nœud.

**4.1.2 Statistiques — PCA et nettoyage spectral**

Ici B est *estimée* : diagonaliser la corrélation empirique E = (1/T)·X'X (X : rendements standardisés), garder les premiers vecteurs propres comme facteurs. Tout le problème est de savoir combien, et la random matrix theory donne la réponse nulle exacte : si les rendements étaient du bruit i.i.d. pur, les valeurs propres de E se distribueraient, pour N, T → ∞ à q = N/T fixé, selon la densité de **Marchenko-Pastur** (1967)

> ρ(λ) = (T/N)·√((λ₊ − λ)(λ − λ₋)) / (2πλ),  **λ± = (1 ± √q)²**

Toute valeur propre au-delà de λ₊ porte de la structure ; le « bulk » en dessous est indiscernable du bruit. Constat empirique fondateur (Laloux, Cizeau, Bouchaud & Potters, PRL 1999 ; Plerou et al., PRL 1999) : sur les actions US, ~90-95% des valeurs propres tombent dans le support MP — quelques dizaines de facteurs réels, le reste est du bruit que la covariance empirique prend pour de la structure. D'où le **clipping** : conserver les λ_j > λ₊ avec leurs vecteurs propres, remplacer toutes les autres par leur moyenne (en préservant la trace), reconstruire. Le raffinement d'état de l'art est le shrinkage *non linéaire* — chaque valeur propre reçoit sa propre correction, dérivée analytiquement — via l'estimateur invariant par rotation (RIE) : Ledoit & Péché (2011), Ledoit & Wolf (« Nonlinear Shrinkage », Annals of Statistics 2012), et la revue complète Bun, Bouchaud & Potters, « Cleaning large correlation matrices » (Physics Reports, 2017). Pour le choix formel du nombre de facteurs hors cadre RMT : les critères d'information de Bai & Ng (Econometrica, 2002) et le test d'Onatski (2010).

Les avantages : aucun a priori taxonomique, capture des corrélations émergentes qu'aucune grille sectorielle ne prévoit. Les coûts : facteurs ininterprétables (on neutralise « PC3 » sans savoir ce que c'est), instabilité des vecteurs propres au-delà des 2-3 premiers, et le piège point-in-time déjà établi en 1.2.1 : estimation en expanding/rolling window exclusivement — des facteurs extraits sur l'échantillon complet connaissent les crises futures. La pratique des grandes maisons est hybride : socle fondamental pour l'interprétabilité et la neutralisation, couche statistique résiduelle pour ce qui échappe à la grille.

**4.1.3 Shrinkage et horizon — les paramètres du paramètre**

Le shrinkage linéaire de **Ledoit-Wolf** (« Honey, I Shrunk the Sample Covariance Matrix », Journal of Portfolio Management 2004) combine la covariance empirique S et une cible structurée T₀ (identité scalée, ou corrélation constante) :

> **Σ̃ = δ\*·T₀ + (1−δ\*)·S**

avec δ\* estimable en forme close — asymptotiquement, δ\* ≈ (Σ_ij var(S_ij)) / (Σ_ij (S_ij − T₀,ij)²) : le numérateur mesure le bruit d'estimation, le dénominateur le biais de la cible ; on shrinke d'autant plus que S est bruitée et que la cible est proche. C'est exactement la logique bayésienne de 3.1.3, appliquée à une matrice — et elle s'applique à chaque étage : à Σ entière (petits univers), à F (toujours), aux betas individuels (Vasicek, cf. 4.1.4).

La question de l'**horizon** a deux volets. Les demi-vies d'estimation d'abord : F et D n'ont aucune raison de partager la même — typiquement F en EWMA de demi-vie 90-250 jours (les corrélations entre facteurs dérivent lentement mais sûrement), D plus courte (60-90 jours, le risque spécifique bouge avec les événements d'entreprise), avec parfois une composante courte + longue combinées pour F (réactivité aux chocs sans amnésie). Le passage à l'horizon de détention ensuite : la covariance à h jours n'est *pas* h fois la covariance quotidienne dès que les rendements factoriels sont autocorrélés — le momentum factoriel l'est positivement, la liquidité aussi — et la correction est l'estimateur de **Newey-West** appliqué à F :

> F^(h) ≈ h·[ Γ₀ + Σ_{l=1}^{L} (1 − l/(L+1))·(Γ_l + Γ_l') ],  Γ_l = cov(f_t, f_{t−l})

C'est le même outil que pour l'inférence sur les IC (§2.2, §3.1.3) — troisième apparition dans l'arbre, à chaque fois pour le même péché : traiter comme indépendantes des observations qui se chevauchent. Règle de cohérence transversale (l'argument de grille du §1.2.2) : un book qui tourne en trois jours n'a que faire d'un modèle mensuel — la demi-vie du modèle de risque, celle des signaux et l'horizon de détention doivent vivre dans le même ordre de grandeur.

**4.1.4 Crypto — un facteur écrasant, des paramètres fuyants**

La structure factorielle du crypto est dégénérée par rapport à l'equity : le modèle de marché

> r_i = α_i + β_i·r_BTC (+ β_i^ETH·r_ETH⊥) + ε_i

capture l'essentiel, avec un premier facteur expliquant régulièrement 50-70% de la variance moyenne des majors (contre ~30% pour le facteur marché equity) — et pourtant une part *spécifique* des alts paradoxalement énorme, car les queues idiosyncratiques (unlocks, exploits, listings, delistings) sont sans équivalent actions. Le problème central est l'instabilité de β : les betas contre BTC changent de régime en quelques semaines (phases BTC vs phases alts, §1.2.3), ce qui impose des fenêtres courtes (30-90 jours) — donc des β̂ très bruités — donc le **shrinkage de Vasicek** comme correction obligatoire :

> β̃_i = w·β̂_i + (1−w)·β̄_groupe,  w = τ²_β / (τ²_β + s²_i)

la mécanique exacte du posterior de 3.1.3 (s²_i : variance d'estimation du beta individuel ; τ²_β : dispersion vraie des betas dans le groupe), qui referme la boucle James-Stein une fois de plus. Les « secteurs », faute de GICS, se construisent par clustering de corrélation : distance d_ij = √(2(1−ρ_ij)) (Mantegna, « Hierarchical structure in financial markets », Eur. Phys. J. B 1999), clustering hiérarchique, coupe du dendrogramme — la même machinerie que le HRP de López de Prado (Journal of Portfolio Management, 2016) côté combinaison, utilisée ici pour définir la grille de neutralisation, avec l'avantage de suivre les recompositions du marché (le cluster « L1 » de 2021 n'est pas celui de 2026) et l'inconvénient d'être lui-même une estimée instable. Dernier écart : les queues. Les rendements crypto ont un kurtosis qui rend les estimateurs de covariance L2 fragiles — winsorisation des rendements *avant* estimation de Σ, ou estimateurs robustes, et bascule du VaR vers l'ES (§4.5) plus impérative encore qu'en equity. Pas de référence canonique, comme toujours sur ce versant : la littérature praticienne et les papiers récents de factor investing crypto (les études de primes momentum/size/value sur tokens) en tiennent lieu provisoirement.

---

Le nœud est foré au niveau 3, aligné sur le grain de 3.1. Trois remarques de couture pour le livre : le bias statistic de 4.1.1 appartient aussi à 6.2 (monitoring de la parité modèle/réalité), Newey-West mérite un encadré transversal unique (trois usages : 2.2, 3.1.3-σ(IC), 4.1.3), et la boucle Vasicek/James-Stein/Ledoit-Wolf est un seul théorème sous trois habits — un candidat naturel pour un appendice « shrinkage » commun aux branches 3 et 4. Suites ouvertes : 4.2 ou 4.3.3 en profondeur (la dérivation Gârleanu-Pedersen), ou la traversée vers la branche 5.

---

## [M079] Humain — 2026-07-23 20:47:52

4.2

---

## [M080] Assistant — 2026-07-23 20:49:05

On fore : **4.2 Construction de portefeuille**. Le sous-arbre local :

```
4.2 CONSTRUCTION DE PORTEFEUILLE     w* = (1/γ)·Σ⁻¹α  + frictions
│
├── 4.2.1 MVO & error maximization     la solution close et son venin
├── 4.2.2 Contraintes & duals          KKT, Jagannathan-Ma
├── 4.2.3 Transfer coefficient         IR = TC·IC·√BR, diagnostic
└── 4.2.4 Robustesse                   resampling, robust opt, heuristiques
```

**4.2.1 MVO et error maximization — la solution close et son venin**

Le programme sans friction, max_w w'α − (γ/2)·w'Σw, donne

> **w\* = (1/γ)·Σ⁻¹α**

et la structure factorielle de 4.1 rend le calcul praticable via l'identité de Woodbury :

> Σ⁻¹ = D⁻¹ − D⁻¹B·(F⁻¹ + B'D⁻¹B)⁻¹·B'D⁻¹

soit O(Nk²) au lieu de O(N³), avec une lecture économique limpide : le premier terme est l'alpha divisé par le risque *spécifique* (w_i ∝ α_i/D_ii — chaque titre pour lui-même), le second est la **correction de hedge factoriel** — l'optimiseur retranche la combinaison de titres qui annule les expositions factorielles induites par le premier terme. Un alpha déjà neutralisé (§1.3.3) rend ce second terme petit : c'est la traduction algébrique du contrat d'interface.

Le venin est dans Σ⁻¹. En base propre, Σ⁻¹ = Σ_j λ_j⁻¹·u_j u_j' : les directions de *petites* valeurs propres — les combinaisons long-short que le modèle croit quasi sans risque — reçoivent les poids les plus grands, or ce sont précisément les directions où λ̂_j et û_j sont les plus bruités (§4.1.2). L'optimiseur alloue vers ses propres erreurs : c'est l'**error maximization** de Michaud (« The Markowitz Optimization Enigma », FAJ 1989), déjà rencontrée en 3.1.4, ici en dimension N. Le résultat quantitatif de référence est Kan & Zhou (« Optimal Portfolio Choice with Parameter Uncertainty », JFQA 2007) : avec μ estimé sur T observations pour N actifs, la perte espérée d'utilité out-of-sample du plug-in croît comme **N/T** — utiliser ŵ = (1/γ)Σ̂⁻¹μ̂ avec N/T proche de 1 peut produire une utilité espérée *négative*, c'est-à-dire pire que ne rien détenir — et la correction optimale est un portefeuille à trois fonds dont les poids shrinkent explicitement vers le minimum-variance. Le message chiffré rejoint DeMiguel et al. (§3.1.1) : l'optimisation ne bat le naïf que quand T ≫ N, régime rare en pratique.

**4.2.2 Contraintes et duals — le prix de chaque interdit**

Avec contraintes d'égalité Aw = b (neutralités beta, secteurs, facteurs ; A ∈ ℝ^(m×N)), le lagrangien donne les conditions KKT et la solution

> **w\* = (1/γ)·Σ⁻¹(α − A'λ)**,  λ = (AΣ⁻¹A')⁻¹·(AΣ⁻¹α − γb)

Lecture : tout se passe comme si on optimisait sans contrainte sur un **alpha amputé** α̃ = α − A'λ — chaque contrainte active retranche de l'alpha sa projection sur la direction contrainte, et le vecteur λ des multiplicateurs donne, ligne par ligne, le prix en alpha de chaque neutralité. Lire les duals est le diagnostic de base : une contrainte au dual élevé et persistant signale soit un vrai désaccord entre l'alpha et le modèle de risque (à arbitrer en gouvernance), soit un signal mal neutralisé en amont. Les inégalités (bornes l ≤ w ≤ u, contraintes de gross Σ|w_i| ≤ G) s'ajoutent avec leurs duals ν ≥ 0 et les conditions de complémentarité — actives seulement là où elles mordent.

Le théorème de **Jagannathan-Ma** (« Risk Reduction in Large Portfolios: Why Imposing the Wrong Constraints Helps », JF 2003) donne aux contraintes leur seconde lecture : le portefeuille minimum-variance sous w ≥ 0 (et bornes supérieures u) est *identique* au portefeuille minimum-variance non contraint calculé sur la covariance modifiée

> **Σ̃ = Σ − (δ·1' + 1·δ') + (ν·1' + 1·ν')**

où δ, ν ≥ 0 sont les duals des bornes inférieures et supérieures actives. Les contraintes *sont* un shrinkage implicite : interdire une position extrême équivaut à réduire les covariances qui la justifiaient. C'est la démonstration formelle du constat empirique que des contraintes « fausses » améliorent l'out-of-sample — elles régularisent Σ̂ là où il est le plus bruité — et le pendant portefeuille du message constant de la branche 3. DeMiguel, Garlappi, Nogales & Uppal (« A Generalized Approach to Portfolio Optimization », Management Science 2009) unifient le tableau : contraindre la norme de w (‖w‖₁ ≤ c ou ‖w‖₂ ≤ c) engendre une famille continue qui interpole entre 1/N, minimum-variance contraint et non contraint — la ridge de 3.2, réapparue dans l'espace des titres.

**4.2.3 Transfer coefficient — mesurer ce qui survit**

La loi fondamentale généralisée (Clarke, de Silva & Thorley, « Portfolio Constraints and the Fundamental Law of Active Management », FAJ 2002) :

> **IR ≈ TC · IC · √BR**,  TC = corr(w_réel, w\*) dans la métrique du risque = ⟨w, w\*⟩_Σ / (‖w‖_Σ‖w\*‖_Σ)

Le TC est le cosinus de l'angle entre les positions effectivement prises et les positions idéales — la fraction de l'information fabriquée par les branches 1-3 qui atteint le P&L. Ordres de grandeur documentés dans le papier et sa suite (Clarke-de Silva-Thorley 2006) : un mandat **long-only** vit avec TC ≈ 0,3-0,4 (l'interdiction du short ampute plus de la moitié de l'information — l'essentiel des signaux cross-sectionnels vit dans la queue basse qu'on ne peut pas vendre), un long-short contraint (neutralités + liquidité + concentration) atteint 0,7-0,9, et chaque contrainte marginale se lit en points de TC. D'où la pratique de diagnostic standard : faire tourner en parallèle le **paper portfolio non contraint** — même alpha, même Σ, zéro contrainte, zéro coût — et décomposer l'écart de performance réel vs papier en une cascade contrainte par contrainte (puis coûts, branche 5 : c'est la naissance de la TCA du §5.5). Un TC qui dérive dans le temps est une alerte en soi : soit les contraintes se durcissent (capacité, §4.4.4), soit l'alpha migre vers des zones que le mandat interdit.

**4.2.4 Robustesse — optimiser en sachant qu'on se trompe**

Trois familles de réponses à l'error maximization, par ordre de sophistication. Le **resampling** de Michaud (*Efficient Asset Management*, 1998) : bootstrapper l'histoire, ré-optimiser sur chaque tirage, moyenner les portefeuilles obtenus — la moyenne d'optima bruités est plus stable que l'optimum du bruité (déjà vue en 3.1.4 ; controverse académique sur ses fondements, efficacité pratique reconnue). L'**optimisation robuste** formalise l'incertitude : maximiser le pire cas sur un ensemble d'incertitude ellipsoïdal U = {α : (α−α̂)'Ω⁻¹(α−α̂) ≤ κ²},

> max_w min_{α∈U} w'α − (γ/2)w'Σw  ⟺  **max_w w'α̂ − κ·√(w'Ωw) − (γ/2)w'Σw**

(Goldfarb & Iyengar, Mathematics of OR 2003 ; Ben-Tal & Nemirovski pour le cadre général ; Ceria & Stubbs 2006 pour la version praticienne) : le pire cas se résout en forme close et ajoute une *pénalité de risque d'estimation* κ·‖w‖_Ω — l'équivalence robuste ⟺ régularisation, une fois encore : choisir κ, c'est choisir un shrinkage, et toute la panoplie (contraintes, normes, robust, resampling, bayésien) converge vers le même geste sous des habits différents. Troisième famille, l'assomption heuristique — « l'optimiseur du pauvre » du desk compact :

> w_i ∝ (α_i − ᾱ_groupe(i)) / σ_i²,  puis caps ±w_max et renormalisation au gross cible

démoyennage par groupe (la neutralisation sectorielle sans matrice A), division par la variance spécifique (le premier terme de Woodbury — on saute le hedge factoriel, que la neutralisation amont a rendu petit), bornes (le Jagannathan-Ma du pauvre). Trois lignes de code qui capturent typiquement 80-90% du TC de l'optimiseur complet quand les alphas sont proprement neutralisés — et qui explicitent le vrai théorème de ce nœud : **la sophistication de l'optimiseur est un substitut à la propreté de l'alpha, jamais un complément**. Un pipeline amont discipliné rend l'aval presque trivial ; un pipeline sale rend l'aval impossible à régler.

---

Nœud foré au niveau 3, aligné sur 4.1. Points de couture pour le livre : l'équivalence contraintes/normes/robust/shrinkage rejoint le futur appendice « shrinkage » proposé au forage précédent (le théorème unique sous ses habits) ; le paper portfolio de 4.2.3 est l'ancêtre de la TCA (§5.5) et du monitoring live-vs-attendu (§6.3.2) — trois instances de la même cascade de décomposition. Suites ouvertes : **4.3** (les coûts, avec la dérivation Gârleanu-Pedersen en 4.3.3 — le forage le plus riche restant de la branche), 4.4/4.5 au même grain, ou la traversée vers la branche 5.

---

## [M081] Humain — 2026-07-23 20:51:53

4.3 ... où devrait on évoquer t on une formulation d une optimisation cross factorielle multipériode pour la construction du portefeuille ?

---

## [M082] Assistant — 2026-07-23 20:53:12

On fore : **4.3 Coûts dans l'optimisation** — et ta question sur l'optimisation cross-factorielle multi-période trouve sa réponse exactement ici : c'est le contenu du nœud 4.3.3, j'y reviens en détail. Le sous-arbre local :

```
4.3 COÛTS DANS L'OPTIMISATION      max  E Σ_t [x_t'α_t − (γ/2)x_t'Σx_t − TC(Δx_t)]
│
├── 4.3.1 Modèles de coût            linéaire + impact en racine carrée
├── 4.3.2 No-trade zones             coûts proportionnels, bande en c^(1/3)
├── 4.3.3 Multi-période              Gârleanu-Pedersen : K facteurs, decays hétérogènes
└── 4.3.4 Netting & implémentation   MPC, crossing interne
```

**4.3.1 Modèles de coût — la fonction TC(δ)**

Pour un trade de taille δ (en fraction d'ADV ou en dollars), la forme standard à trois termes :

> **TC(δ) = c·|δ| + Y·σ·√(|δ|/V)·|δ| + (λ/2)·δ²**

Le premier terme est le coût *proportionnel* : demi-spread + frais + taxes, payé quel que soit le rythme d'exécution. Le deuxième est l'**impact en racine carrée**, l'empirie la plus robuste de la microstructure : le coût moyen d'un métaordre de taille Q vaut ≈ Y·σ_daily·√(Q/ADV), avec Y ≈ 0,5-1, remarquablement stable entre actifs, marchés et époques — mesuré sur données propriétaires par Almgren, Thum, Hauptmann & Li (« Direct Estimation of Equity Market Impact », Risk 2005), théorisé par le modèle de liquidité latente de Tóth et al. (« Anomalous price impact and the critical nature of liquidity », PRX 2011), synthèse dans Bouchaud, Bonart, Donier & Gould, *Trades, Quotes and Prices* (2018). La décomposition temporaire/permanent (la part qui relaxe après l'exécution vs celle qui reste dans le prix) appartient à la branche 5 ; ce qui compte ici est que la racine carrée est *concave* — donc non convexe dans un optimiseur, d'où le troisième terme : l'approximation **quadratique** (λ/2)δ², convexe, qui rend le problème soluble en forme close et sur-pénalise les petits trades / sous-pénalise les gros — un biais connu qu'on accepte pour la tractabilité, ou qu'on corrige par résolution numérique (4.3.4). La calibration relie les deux : λ se cale pour que le coût quadratique coïncide avec la racine carrée à la taille de trade typique du book.

**4.3.2 No-trade zones — la géométrie des coûts proportionnels**

Avec le seul coût proportionnel c, la solution optimale n'est plus un point mais une **bande** : autour de la position cible w\*, une région [w\* − Δ, w\* + Δ] dans laquelle le gradient d'utilité |∂U/∂w| < c ne rembourse pas le spread — on ne trade que lorsque la position sort de la bande, et alors *jusqu'au bord* de la bande, jamais jusqu'à la cible (y aller coûterait du spread pour un gain marginal nul). Le résultat asymptotique classique (Constantinides, JPE 1986 ; Davis & Norman, Math. of OR 1990 ; asymptotiques de Shreve-Soner) : la demi-largeur optimale croît comme la **racine cubique** du coût,

> **Δ ∝ (3c/(2γ)·w\*²·...)^(1/3) ∝ c^(1/3)**

— une dépendance très douce, qui explique un fait d'expérience : même de petits coûts proportionnels justifient des bandes larges, et la perte d'utilité à utiliser une bande approximative est du second ordre (l'optimum plat, encore lui). C'est la formalisation de ce que le smoothing du §1.3.4 faisait heuristiquement, avec deux différences opérationnelles : la bande vit dans l'espace des *positions* (elle voit le netting entre sleeves, §4.3.4), et sa largeur peut se moduler par titre — étroite sur les large caps à 2 bps de spread, large sur les alts à 40 bps.

**4.3.3 Multi-période : Gârleanu-Pedersen — la formulation cross-factorielle que tu demandes**

C'est ici, et exactement ici, que vit l'optimisation cross-factorielle multi-période — le papier est littéralement construit sur ce cahier des charges : *K* facteurs prédictifs de vitesses de décroissance hétérogènes, un modèle de risque, des coûts, et une politique dynamique en forme close (Gârleanu & Pedersen, « Dynamic Trading with Predictable Returns and Transaction Costs », Journal of Finance 2013). La formulation complète :

*Dynamique des signaux.* Les rendements sont pilotés par K facteurs (nos alphas combinés, ou les sleeves individuels) qui mean-revertent chacun à sa vitesse :

> r_{t+1} = **B·f_t** + u_{t+1},  cov(u) = Σ
> Δf_{t+1} = **−Φ·f_t** + ε_{t+1},  Φ = diag(φ₁, ..., φ_K)

φ_k est la vitesse de décroissance du facteur k — le lien direct avec le profil de decay du §2.1 et la demi-vie du signal (φ_k ≈ ln2/H_k). C'est le mot « cross-factoriel » rendu opérationnel : le problème traite *simultanément* des signaux rapides et lents.

*Programme.* Maximiser la valeur actualisée du P&L pénalisé du risque et des coûts quadratiques :

> max E Σ_t (1−ρ)^t [ x_t'·B·f_t − (γ/2)·x_t'Σx_t − (1/2)·Δx_t'·Λ·Δx_t ],  Λ = λ·Σ

*Solution.* Linéaire-quadratique gaussien → forme close en deux équations :

> **x_t = x_{t−1} + (a/λ)·(aim_t − x_{t−1})**
> **aim_t = (γΣ)⁻¹ · Σ_k B_k·f_{k,t} · [ φ_k → 1/(1 + φ_k·a/γ) ]**

La première dit : on ne saute jamais sur la cible, on trade une *fraction* a/λ du chemin — le taux de trading a résolvant une équation quadratique en (γ, λ, ρ), croissant avec la liquidité. La seconde est le cœur cross-factoriel : l'aim portfolio est un **Markowitz sur alphas actualisés**, chaque facteur k entrant multiplié par 1/(1 + φ_k·a/γ) — les signaux rapides (φ grand) sont dépréciés, les lents quasi intacts. Un alpha qui meurt en trois jours ne rembourse jamais l'impact payé pour le charger ; un alpha qui persiste six mois l'amortit sur toute sa vie. Le théorème soude d'un coup trois nœuds de l'arbre — decay (§2.1), demi-vie/turnover (nos échanges), coûts — et remplace par un calcul la règle de gouvernance du §1.3.4 sur le partage du budget de turnover entre sleeves.

*Sur le placement dans l'arbre, pour le livre* : la formulation canonique appartient à **4.3.3** — c'est un problème de construction de portefeuille sous coûts, pas de combinaison — mais elle mérite un renvoi appuyé depuis la branche 3, car elle en modifie une conclusion : la pondération des signaux n'est *pas* séparable de l'implémentation. Le facteur 1/(1+φ_k·a/γ) est une pondération des alphas qui dépend de la liquidité du book — deux desks de tailles différentes doivent pondérer différemment le même pool. Le contrat d'interface (un vecteur d'alphas passe de la recherche à la mise en œuvre) survit, mais l'interface transporte désormais aussi les φ_k : les demi-vies font partie de la spécification d'un alpha au même titre que son IC. Concrètement : une sous-section 3.4.5 « Combinaison sous coûts : le renvoi Gârleanu-Pedersen » dans le squelette, pointant vers 4.3.3 pour la dérivation.

*Extensions documentées* : coûts non quadratiques et impact persistant (Gârleanu-Pedersen 2016, « Dynamic portfolio choice with frictions », JET — coûts proportionnels + quadratiques, impact transitoire) ; contraintes → plus de forme close, résolution numérique (4.3.4).

**4.3.4 Netting et implémentation — MPC et crossing interne**

La pratique de production ne résout pas le programme infini : elle applique le **model predictive control** — à chaque rebalancement, résoudre le problème multi-période sur un horizon fini (avec les contraintes de 4.2, les vraies fonctions de coût, la racine carrée si le solveur le permet), exécuter le premier pas, ré-résoudre au pas suivant avec l'information nouvelle. Le cadre de référence praticien est Boyd et al., « Multi-Period Trading via Convex Optimization » (Foundations and Trends in Optimization, 2017) — qui traite aussi la version stochastique et les certificats de sous-optimalité. Le netting y est automatique et c'est son avantage décisif sur le lissage par sleeve : l'optimiseur voit le book agrégé, donc deux sleeves dont les cibles se croisent (le reversal vend ce que le momentum achète) ne génèrent *aucun* trade externe — un crossing interne à coût nul, qui peut représenter une fraction substantielle du turnover brut d'un book multi-signaux. La comptabilité analytique doit suivre : le P&L par sleeve se calcule sur les positions *théoriques* de chaque sleeve, les coûts réels sur les trades *nets* — et l'écart entre les deux (le « netting benefit ») est une ligne d'attribution à part entière, qui appartient à la TCA (§5.5) et complique l'attribution par chercheur (§3.4.3, §6.4.2) : dans un book intégré, le coût marginal d'un sleeve dépend des autres.

---

Nœud foré au niveau 3. Il reste 4.4 et 4.5 à ce grain pour clore la branche, la traversée vers la 5 (qui reprend la racine carrée là où 4.3.1 l'a laissée), et la mise à jour du squelette avec le 3.4.5 proposé — dis-moi si tu veux que je regénère le fichier squelette amendé.

---

## [M083] Humain — 2026-07-23 20:55:27

4.4

---

## [M084] Assistant — 2026-07-23 20:56:57

On fore : **4.4 Sizing & levier** — la branche 4 quitte les poids relatifs pour l'échelle absolue du book. Le sous-arbre local :

```
4.4 SIZING & LEVIER            l'échelle : L = σ*/σ̂,  f = c·Σ⁻¹μ̂,  A ≤ A*
│
├── 4.4.1 Vol targeting          L_t = σ*/σ̂_t, effets sur les moments
├── 4.4.2 Kelly fractionnel      g(c) = r + (c − c²/2)·SR², drawdowns en x^(2/c−1)
├── 4.4.3 Contrôle de drawdown   Grossman-Zhou, stop-loss & autocorrélation
└── 4.4.4 Capacité               P&L(A) = αA − kA^(3/2),  A* ∝ ADV·α²/τ³
```

**4.4.1 Vol targeting — le levier comme thermostat**

La règle : viser une volatilité de book constante σ\* en appliquant le levier

> **L_t = σ\* / σ̂_t**

avec σ̂_t en EWMA courte (§1.2.2, demi-vie 10-30 jours). La justification est une asymétrie fondamentale : la volatilité est *prévisible* (le clustering, corrélation sérielle de σ² très élevée) alors que les rendements ne le sont presque pas — donc diviser par σ̂ stabilise le dénominateur du Sharpe sans toucher au numérateur en espérance, et fait mieux que ça dès que rendement et vol sont liés. Le résultat académique : Moreira & Muir (« Volatility-Managed Portfolios », JF 2017) montrent qu'un scaling en 1/σ̂² sur le marché et les grands facteurs *augmente* les alphas réalisés — le rendement par unité de risque est plus faible en haute vol, donc réduire l'exposition quand la vol monte est en soi un signal de timing. Harvey et al. (« The Impact of Volatility Targeting », JPM 2018) documentent l'effet sur les moments supérieurs : réduction du kurtosis et de la queue gauche, maximale pour les actifs à effet de levier (actions — la vol monte quand le prix baisse), quasi nulle pour ceux qui n'en ont pas (obligations).

Trois précautions d'implémentation. Le levier est lui-même une position : ses variations sont des trades, et un σ̂ trop réactif fabrique du turnover de levier sans espérance — même arbitrage que le smoothing, résolu par une bande de non-trading sur L (on ne re-lève que si |L_cible/L_actuel − 1| dépasse un seuil). Un plafond L ≤ L_max s'impose indépendamment de la formule : en régime de vol écrasée, σ\*/σ̂ demande des leviers que le risque de saut (que σ̂ ne voit pas) interdit. Et la procyclicité systémique déjà notée : tous les books vol-targetés dé-lèvent ensemble quand la vol saute — le mécanisme amplificateur des épisodes de 2.4, à garder en tête quand on estime sa propre capacité à sortir. En crypto : √365, coût de funding du levier à intégrer dans le net, et un risque de liquidation discret qui impose L_max bien en dessous de ce que le vol target nu suggérerait.

**4.4.2 Kelly fractionnel — le niveau du thermostat**

Le vol targeting fixe la *stabilité* du risque ; Kelly fixe son *niveau*. En temps continu avec K actifs, le levier log-optimal est

> **f\* = Σ⁻¹μ**

— formellement le Markowitz de 4.2.1 avec γ = 1 : le portefeuille growth-optimal est le tangent, levé à l'aversion logarithmique. Le taux de croissance sous fraction c (f = c·f\*) :

> g(c) = r + (c − c²/2)·SR²,  avec au plein Kelly g\* = r + SR²/2

La parabole est le cœur pratique : **à c = ½, on capture 75% de la croissance excédentaire avec la moitié du risque** — et l'asymétrie est brutale au-delà de c = 1 (à c = 2, croissance excédentaire *nulle* ; au-delà, négative avec un risque supérieur). La distribution des drawdowns rend le choix tangible : pour un book en Kelly fractionnel c, la probabilité de jamais perdre une fraction x du capital vaut

> **P(DD ≥ x) = (1 − x)^(2/c − 1)**

— au plein Kelly, perdre 50% a probabilité ½ ; à c = ½, elle tombe à 12,5% ; à c = ⅓, ~3%. Voilà pourquoi « demi-Kelly » est une convention et non une timidité. S'ajoute la couche d'incertitude paramétrique déjà construite en 3.1.3 : sous μ estimé, la croissance espérée du plug-in est amputée d'un terme en Var(μ̂), et la correction bayésienne — Kelly sur le posterior shrinké — équivaut à une fraction c < 1 supplémentaire : le shrinkage des IC et le fractional Kelly sont, une fois encore, le même geste. Références : Kelly (1956), Breiman (1961) pour les théorèmes de croissance, Thorp (« The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market », 2006) pour la pratique, MacLean, Thorp & Ziemba (éds., 2011) pour la compilation des débats.

**4.4.3 Contrôle de drawdown — le plancher explicite**

La formalisation de référence est **Grossman-Zhou** (« Optimal Investment Strategies for Controlling Drawdowns », Mathematical Finance 1993) : maximiser la croissance sous la contrainte W_t ≥ α·M_t (ne jamais perdre plus de 1−α du plus haut historique M_t). La solution est un CPPI sur le coussin :

> **exposition_t ∝ (W_t − α·M_t) / W_t**

— l'exposition est proportionnelle à la distance au plancher, et tend vers zéro quand on s'en approche. Les règles de production par paliers (réduction du gross de 25% à −5%, de 50% à −8%, etc.) en sont des discrétisations. Le coût est réel et double : de l'espérance abandonnée en régime normal, et l'**effet cliquet** — après un drawdown, le plancher relevé maintient l'exposition réduite alors que l'opportunité est souvent maximale ; les règles de ré-entrée (récupération partielle, délai, reset du high-water mark) comptent autant que les règles de coupe et sont systématiquement sous-spécifiées.

Le point analytique qui départage les convictions : **quand un stop-loss ajoute-t-il de l'espérance ?** Kaminski & Lo (« When Do Stop-Loss Rules Stop Losses? », Journal of Financial Markets 2014) donnent la réponse propre — sous rendements i.i.d., jamais (il ne fait que troquer de l'espérance contre du confort) ; sous autocorrélation *positive* (momentum), oui (la perte récente prédit une perte future qu'on évite) ; sous mean reversion, il détruit doublement (on coupe juste avant le rebond). La justification résiduelle est donc structurelle plutôt que statistique : la survie du desk, la clause de rachat de l'allocateur, la préservation de la capacité à opérer — un book qui perd son capital a une espérance nulle quelle que soit celle de ses signaux. Et l'articulation avec 4.4.1 : le vol targeting coupe déjà dans les crises *volatiles* ; le contrôle de drawdown est le filet pour le scénario qu'il rate — la glissade régulière à vol basse, le grind down où σ̂ ne monte jamais.

**4.4.4 Capacité — le Sharpe décroît en √AUM**

Le mécanisme tient en une ligne : l'alpha brut est linéaire en AUM, les coûts sont super-linéaires à cause de l'impact en racine (§4.3.1). Avec un turnover annuel τ et un book A :

> P&L(A) = α·A − Y·σ·τA·√(τA / (252·ADV))  = **α·A − k·A^(3/2)**

La condition marginale donne l'AUM optimal en forme close :

> **A\* = (4/9)·252·ADV · α² / (Y²σ²·τ³)**

et deux enseignements structurants s'y lisent. La capacité croît avec le carré de l'alpha mais décroît avec le **cube du turnover** — les sleeves rapides saturent dramatiquement les premiers, et la frontière de capacité d'un book intégré est essentiellement celle de ses sleeves lents : troisième apparition du même arbitrage vitesse/coûts après le smoothing (§1.3.4) et l'actualisation Gârleanu-Pedersen (§4.3.3), ici en version « combien de capital ». Et au-delà de A\*, le Sharpe net décroît continûment (les coûts croissent en √A par dollar) : la capacité n'est pas un mur mais une pente, et la décision de taille est un choix sur la courbe Sharpe(A) — que l'allocateur et le desk ne tranchent pas au même endroit, l'un maximisant le P&L total (A\*), l'autre souvent les frais sur encours (au-delà). Références : Perold & Salomon (« The Right Amount of Assets Under Management », FAJ 1991) pour le cadre ; Frazzini, Israel & Moskowitz (« Trading Costs of Asset Pricing Anomalies », 2015) pour les capacités empiriques des grands facteurs sur données de trading réelles ; Landier, Simon & Thesmar sur performance et taille ; Isichenko pour la dérivation praticienne. En crypto, l'application numérique est dégrisante : hors BTC/ETH, les ADV réels (nettoyés du wash trading, §1.2.4) donnent des A\* de quelques millions à quelques dizaines de millions pour les stratégies cross-sectionnelles sur alts — la raison structurelle pour laquelle l'edge y persiste : il ne vaut pas la peine d'être arbitré par les grands books.

---

Nœud foré au niveau 3. Points de couture : la parabole de Kelly et Grossman-Zhou partagent le futur appendice « croissance et survie » avec le shrinkage (le triptyque μ̂ shrinké / c < 1 / plancher étant trois réponses au même problème d'incertitude) ; la formule de capacité doit citer 5.2 pour Y et 1.2.4 pour l'ADV nettoyé. Reste **4.5** pour clore la branche, puis la traversée vers la 5 — ou la régénération du squelette amendé (3.4.5, appendices) si tu veux consolider avant de poursuivre.

---

## [M085] Humain — 2026-07-23 20:57:16

4.5

---

## [M086] Assistant — 2026-07-23 20:58:27

On clôt la branche : **4.5 Gestion des risques** — le nœud qui surveille les quatre autres, et surtout ce qu'ils ne voient pas. Le sous-arbre local :

```
4.5 GESTION DES RISQUES        ce que Σ mesure mal, et ce qui n'y est pas
│
├── 4.5.1 VaR & expected shortfall    définitions, cohérence, backtesting
├── 4.5.2 Stress & corrélations       DCC, corrélations d'exceedance, copules
├── 4.5.3 Limites & risque de modèle  hiérarchie, escalade, reverse stress
└── 4.5.4 Crypto                      contrepartie, liquidations, depegs
```

**4.5.1 VaR et expected shortfall — les métriques et leurs tests**

Les définitions, sur la perte L à horizon donné :

> **VaR_q = inf{ x : P(L > x) ≤ 1−q }**,  **ES_q = E[L | L ≥ VaR_q] = (1/(1−q))·∫_q^1 VaR_u du**

La VaR est un quantile — elle dit où commence la queue, rien sur ce qu'elle contient ; l'ES est la moyenne de la queue. Le cadre axiomatique qui les départage est Artzner, Delbaen, Eber & Heath (« Coherent Measures of Risk », Mathematical Finance 1999) : une mesure cohérente doit être monotone, invariante par translation, positivement homogène et **sous-additive** — ρ(X+Y) ≤ ρ(X) + ρ(Y), la diversification ne peut pas augmenter le risque. La VaR viole la sous-additivité (contre-exemples standard avec des positions à défaut discret : la VaR d'un portefeuille de deux obligations peut dépasser la somme des VaR), l'ES la satisfait — d'où la bascule réglementaire (FRTB) et pratique vers l'ES, renforcée par sa sensibilité à toute la queue.

L'estimation, trois familles : paramétrique gaussienne (VaR_q = z_q·√(w'Σw) — hérite intégralement des défauts de Σ en queue), simulation historique (le quantile empirique des P&L rejoués — non paramétrique mais aveugle aux changements de régime), et le compromis dominant, la **simulation historique filtrée** (Barone-Adesi, Giannopoulos & Vosper 1999) : rejouer les rendements passés *rescalés* par le ratio de vol σ̂_t/σ̂_s — la forme de la distribution vient de l'histoire, son échelle du présent. Le backtesting ferme la boucle : le test de couverture de **Kupiec** (POF, 1995) vérifie que la fréquence des exceptions x/T est compatible avec 1−q via LR = −2·ln[(1−p)^(T−x)·p^x / ((1−x/T)^(T−x)·(x/T)^x)] ~ χ²(1), et **Christoffersen** (1998) teste leur *indépendance* — des exceptions groupées signalent un modèle qui rate les régimes même si leur nombre total est correct, le défaut le plus commun. Pour l'ES, longtemps réputée non backtestable (non-elicitability), les tests d'Acerbi & Székely (2014) fournissent la réponse praticienne. Et la couture avec 4.1.1 : le bias statistic est exactement un backtest de Σ — VaR, ES et bias statistic sont trois contrôles du même objet à trois quantiles différents.

**4.5.2 Stress et corrélations conditionnelles — là où Σ ment**

Le fait empirique central : les corrélations ne sont pas constantes, et elles montent *précisément quand on en a besoin*. Deux formalisations. La dynamique : le **DCC** d'Engle (« Dynamic Conditional Correlation », JBES 2002) —

> Q_t = (1−a−b)·Q̄ + a·ε_{t−1}ε'_{t−1} + b·Q_{t−1}

un GARCH sur la matrice de corrélation, qui capture la dérive mais reste un modèle L2. L'asymétrie de queue ensuite : les **corrélations d'exceedance** de Longin & Solnik (« Extreme Correlation of International Equity Markets », JF 2001) — la corrélation conditionnelle aux co-mouvements extrêmes — montrent que les corrélations actions montent dans la queue *basse* et pas dans la haute : la diversification s'évapore à la baisse seulement. Le langage propre est celui des copules : le coefficient de dépendance de queue

> **λ_L = lim_{q→0} P(U ≤ q | V ≤ q)**

vaut *zéro* pour la copule gaussienne quelle que soit la corrélation — le théorème qui condamne toute la machinerie Σ en régime extrême : deux actifs gaussiens corrélés à 0,9 deviennent asymptotiquement indépendants dans la queue ; une copule t (paramètre ν) donne λ_L > 0. Traité de référence : McNeil, Frey & Embrechts, *Quantitative Risk Management* (Princeton, 2015).

D'où les stress tests, dont la version qui compte pour un book systématique n'est pas macro mais *positionnelle* : le scénario « les détenteurs de mes positions dé-lèvent ensemble ». Le document canonique est Khandani & Lo (« What Happened to the Quants in August 2007? », Journal of Investment Management 2007) : en trois jours, les books stat arb — décorrélés en régime normal — ont subi des pertes synchrones massives suivies d'un rebond, la signature d'une liquidation forcée d'un acteur commun se propageant par les positions partagées ; le crowding du §2.4 devenu mécanisme de contagion. La grille de stress complète mélange donc scénarios historiques rejoués (2008, mars 2020, août 2007 pour le style), chocs hypothétiques par facteur (±5σ sur chaque ligne de F), et **reverse stress tests** : partir de la perte inacceptable, chercher le scénario le plus *probable* qui la produit — l'exercice qui révèle les concentrations que la VaR moyenne masque.

**4.5.3 Limites et risque de modèle — la gouvernance du doute**

L'architecture de limites suit la hiérarchie du book : au sommet, vol cible et drawdown max (§4.4) ; puis les limites d'exposition par facteur (|b_k| ≤ b_max, en unités de σ du facteur), par groupe de neutralisation, par titre (le cap de 4.2), par liquidité (jours d'ADV détenus) ; enfin les limites opérationnelles (turnover, gross, net). Deux principes de design : chaque limite doit avoir un *propriétaire* et une procédure d'escalade datée (une limite sans conséquence codifiée est une décoration), et les limites doivent être **mesurées dans le même système que l'optimisation** — une limite factorielle calculée sur un autre modèle de risque que celui de l'optimiseur crée des violations fantômes et des vraies expositions invisibles.

Le risque de modèle est la couche réflexive : Σ, les modèles de coût, la VaR sont des estimées, et 3.1.4 s'applique à chacun. La discipline praticienne (l'esprit de Derman, « Model Risk », 1996, et Rebonato) : inventorier les hypothèses de chaque modèle et le scénario qui les casse ; faire tourner des modèles *concurrents* (un Σ fondamental et un statistique — leur désaccord est une mesure gratuite d'incertitude de modèle, la version matricielle de l'écart rank-IC/Pearson-IC du fil précédent) ; et plafonner ce que le modèle peut demander (les caps de 4.2.4, L_max de 4.4.1 : des bornes *hors modèle* qui restent quand le modèle déraille). La somme est une inversion du fardeau de la preuve : le modèle a raison par défaut en régime normal, tort par défaut en régime extrême.

**4.5.4 Crypto — le risque hors de Σ**

Le déplacement structurel : en crypto, les pertes maximales historiques des books market-neutral ne viennent pas de Σ mais de l'infrastructure. **Contrepartie et custody** d'abord : les fonds sur une venue centralisée sont une créance chirographaire sur elle (FTX, novembre 2022, en cas d'école) — la gestion est un problème de crédit, pas de marché : notation interne des venues (preuves de réserves — nécessaires, non suffisantes : elles montrent les actifs, pas les passifs —, régulation, historique), limites par contrepartie, sweep régulier vers custody, et le calcul explicite du rendement exigé pour chaque unité de risque venue. **Liquidations** ensuite, la mécanique qui transforme la microstructure en risque de book : positions margées → prix de liquidation ; la cascade — liquidations forcées → impact → nouveaux franchissements — est l'amplificateur non linéaire des queues crypto, partiellement amorti par les conventions de *mark price* (médiane multi-venues plutôt que dernier prix local, précisément pour éviter les liquidations sur mèche) et l'assurance/ADL des venues, qui ajoutent leur propre risque (l'auto-deleveraging ferme vos positions *gagnantes* quand le fonds d'assurance est vide — un risque de modèle de la venue, subi). La règle de sizing qui en découle : le levier se calcule contre le scénario de cascade (gap de 15-30% en minutes sur un alt), pas contre σ̂ quotidien. **Depegs** enfin : le collatéral et les jambes « cash » en stablecoins portent un risque de saut discret (USDC mars 2023 à 0,88 ; UST à zéro) corrélé précisément aux stress de venues — diversification des stables, jambes courtes en stables *différents* des jambes de collatéral, et inclusion du depeg dans la grille de reverse stress. Pas de traité canonique, toujours : post-mortems, documentation des moteurs de marge des venues, littérature praticienne.

---

**La branche 4 est close au niveau 3** — cinq nœuds forés au même grain, formules et sources incluses. L'état de l'arbre : branches 1 (sauf 1.4), 2, 3, 4 couvertes ; restent **5. Exécution** (la suite naturelle — 4.3 lui a déjà emprunté la racine carrée et la TCA y attend), **6. Infra**, **1.4 cibles & labels**, et la consolidation du squelette (3.4.5, les deux appendices transversaux « shrinkage » et « croissance et survie », le renvoi bias-statistic → 6.2). Dis-moi le prochain mouvement.

---

## [M087] Humain — 2026-07-23 21:06:32

vas pour 5

---

## [M088] Assistant — 2026-07-23 21:08:06

On traverse : **5. Exécution** — l'étage entre les positions cibles de la branche 4 et le P&L réel. Le sous-arbre local :

```
5. EXÉCUTION                  transformer Δw en trades, au moindre coût total
│
├── 5.1 Microstructure          carnets, auctions, fragmentation ; perps, AMM, MEV
├── 5.2 Impact de marché        loi en racine, temporaire/permanent, propagateur
├── 5.3 Scheduling              Almgren-Chriss, IS/VWAP/POV, urgence vs decay
├── 5.4 Tactique                limit vs market, microprice, Avellaneda-Stoikov
└── 5.5 TCA                     implementation shortfall, markouts, boucle retour
```

**5.1 Microstructure — le terrain de jeu**

Le carnet d'ordres à double enchère continue est l'objet de base : files d'ordres limites par niveau de prix, priorité **prix-temps** (les venues pro-rata étant l'exception, certains futures), et le tick size comme paramètre structurant — un tick large épaissit les files (la priorité temporelle devient l'actif rare, le jeu est la position dans la queue), un tick fin les pulvérise (le jeu devient la surenchère au sous-tick). Le spread coté se décompose classiquement en trois : coût de traitement, **sélection adverse** (Glosten-Milgrom 1985 : le market maker perd contre l'informé, le spread est sa prime d'assurance) et inventaire — décomposition estimable (Huang-Stoll 1997) et qui gouverne toute la tactique de 5.4. Les *auctions* d'ouverture et de clôture concentrent une part croissante du volume equity (la clôture US ~10% du volume quotidien, tirée par l'indexation) : liquidité profonde, impact réduit, le point de passage naturel des rebalancements lents — et un objet d'étude en soi (imbalances publiés, §1.1.1). La fragmentation entre venues (lit, dark, SI) impose le smart order routing et fait de la *consolidation* du carnet un problème de données avant d'être un problème de trading. Références : Harris, *Trading and Exchanges* (2003) pour l'anatomie ; O'Hara, *Market Microstructure Theory* (1995) ; Hasbrouck, *Empirical Market Microstructure* (2007) ; Budish, Cramton & Shim (QJE 2015) sur la course de vitesse et le design des enchères.

Le crypto ajoute trois objets sans équivalent. Les **perps** : le carnet est standard mais le produit porte le funding — exécuter autour des instants de règlement (00/08/16 UTC) a un coût/gain propre, et le *mark price* multi-venues découple le P&L de marge du dernier prix local. Les **AMM** : la liquidité n'est pas un carnet mais une courbe — pour un pool à produit constant x·y = k, exécuter Δx contre le pool donne un prix moyen dégradé de ≈ Δx/x (l'impact est *déterministe et lisible on-chain*, une transparence de coût inédite), les versions concentrées (Uniswap v3) reconstituant de facto un carnet par plages. Le **MEV** enfin : dans la mempool publique, un ordre visible avant inclusion peut être sandwiché (front-run + back-run) — la sélection adverse devenue attaque explicite (Daian et al., « Flash Boys 2.0 », 2020) ; les défenses (routage privé, agrégateurs, limites de slippage serrées) font partie du coût d'exécution on-chain au même titre que le gas.

**5.2 Impact de marché — la physique du coût**

Le fait empirique central, déjà emprunté par 4.3.1 : l'impact moyen d'un métaordre de taille Q exécuté sur la journée suit la **loi en racine carrée**

> **I(Q) ≈ Y · σ_daily · √(Q / ADV)**,  Y ≈ 0,5–1

remarquablement stable entre actifs, capitalisations, marchés et époques — mesurée sur données propriétaires par Almgren, Thum, Hauptmann & Li (2005), confirmée sur métaordres par Bacry et al., Zarinelli et al., et sur le crypto avec le même exposant. La concavité est le scandale théorique : le modèle canonique de **Kyle** (Econometrica 1985) prédit un impact *linéaire* (λ = σ_v/(2σ_u) dans la version statique — le teneur de marché tarife le flux à sa contenance informationnelle) ; la résolution moderne est la **liquidité latente** (Tóth et al., PRX 2011 ; Donier et al. 2015) : le volume disponible près du prix est localement *linéaire* en distance au prix (le carnet latent est vide au prix courant), donc absorber Q pousse le prix comme √Q — l'impact mesure la rareté locale de liquidité, pas l'information du trade.

La structure temporelle se décrit par le **modèle à propagateur** (Bouchaud, Gefen, Potters & Wyart 2004) :

> p_t = Σ_{s<t} G(t−s)·ε_s·v_s^θ + bruit

où ε_s est le signe du trade et G un noyau *décroissant* : l'impact est majoritairement **transitoire** et relaxe en loi de puissance — précisément à la vitesse qui compense l'autocorrélation longue du flux d'ordres signé (les métaordres sont découpés, le flux est persistant ; si l'impact ne décroissait pas, les prix seraient trivialement prévisibles). La part *permanente* résiduelle est la composante informationnelle ; l'ordre de grandeur praticien : le point médian post-relaxation s'établit vers ½–⅔ du pic. Conséquences directes pour l'amont : le coût dépend du *rythme* (étaler laisse relaxer — le levier de 5.3), et l'impact des autres est un signal (§5.4). Synthèse : Bouchaud, Bonart, Donier & Gould, *Trades, Quotes and Prices* (2018) — le traité du nœud.

**5.3 Scheduling — le rythme optimal**

Le cadre fondateur est **Almgren-Chriss** (« Optimal Execution of Portfolio Transactions », Journal of Risk 2000) : liquider X sur [0,T] en arbitrant coût d'impact (trader vite coûte) contre risque de prix (trader lentement expose). Avec impact temporaire linéaire η·v et permanent γ·v, minimiser E[C] + λ_r·Var[C] donne la trajectoire en forme close

> **x(t) = X · sinh(κ(T−t)) / sinh(κT)**,  κ = √(λ_r·σ² / η)

— exponentielle décroissante dont la vitesse κ, l'**urgence**, croît avec l'aversion au risque et la vol, décroît avec le coût d'impact. λ_r = 0 redonne le TWAP ; λ_r grand front-loade. Les benchmarks industriels s'y raccrochent : **IS** (implementation shortfall — viser le prix d'arrivée, la traduction directe d'Almgren-Chriss), **VWAP/TWAP** (suivre le profil de volume/temps — minimiser le tracking à un benchmark plutôt que le coût vrai), **POV** (participation constante au volume). Le raccord avec l'arbre est le terme qu'Almgren-Chriss n'a pas : l'**alpha pendant l'exécution**. Un signal de decay rapide (§2.1) ajoute au programme un terme de coût d'opportunité α(t)·x(t) qui front-loade la trajectoire — l'urgence optimale croît avec φ_k, exactement le paramètre que Gârleanu-Pedersen (§4.3.3) faisait entrer dans l'aim portfolio : les deux résultats sont le même arbitrage aux deux échelles de temps (jours pour le sizing, heures pour l'exécution). Extensions de référence : Almgren & Lorenz (2007) pour les stratégies adaptatives, Cartea, Jaimungal & Penalva, *Algorithmic and High-Frequency Trading* (Cambridge 2015) pour le traitement HJB complet, Obizhaeva & Wang (2013) pour l'exécution contre la résilience du carnet.

**5.4 Tactique — la décision ordre par ordre**

Sous le scheduler, chaque tranche pose le choix limit vs market : l'ordre limite gagne le spread mais porte le **risque de non-exécution** et la sélection adverse (il n'est rempli que quand le marché le traverse — précisément quand on aurait préféré ne pas l'être) ; l'ordre market paie le spread et l'impact mais exécute. La valeur d'un ordre limite dépend de sa **position dans la file** (les remplissages en tête de file sont les moins adverses — la file est un actif, d'où la prime aux venues/moments où on peut la gagner) et se mesure par les *markouts* : le P&L marked-to-mid à 1s, 10s, 1min après remplissage — l'outil de diagnostic universel de la tactique, un markout systématiquement négatif signant la sélection adverse. Le prix de référence lui-même se raffine : le **microprice** pondéré par les tailles

> P_micro = (Q_b·P_a + Q_a·P_b) / (Q_a + Q_b)

(Stoikov 2018 pour la version dynamique) prédit le mid futur mieux que le mid — et l'**order flow imbalance** (Cont, Kukanov & Stoikov 2014 : ΔP ≈ β·OFI, l'imbalance des flux au meilleur niveau) est le signal court terme canonique qui pilote le placement. Le cadre d'optimisation du placement est **Avellaneda-Stoikov** (Quantitative Finance 2008), écrit pour le market making mais structurant pour toute tactique : prix de réservation décalé de l'inventaire

> **r_t = s_t − q·γ·σ²·(T−t)**,  spread optimal δ = γσ²(T−t) + (2/γ)·ln(1 + γ/k)

— on cote autour d'un prix qui penche contre son propre inventaire, arbitrant capture du spread contre risque de stock et sélection adverse (les intensités de remplissage k venant de la microstructure). En crypto : la grille maker/taker (rebates maker fréquents) déplace matériellement l'arbitrage vers le passif sur les venues majeures, la fragmentation fait du **lead-lag inter-venues** (§introduction crypto) un input tactique direct — coter sur la venue retardataire avec le signal de la directrice — et l'exécution on-chain ajoute le tri privé/public de 5.1.

**5.5 TCA — la comptabilité qui referme la boucle**

Le cadre est l'**implementation shortfall** de Perold (« The Implementation Shortfall: Paper Versus Reality », JPM 1988) : l'écart entre le P&L du portefeuille papier (exécuté instantanément au prix de décision, sans coûts) et le réel, décomposé additivement

> **IS = coût de délai + coût de trading (vs arrival) + coût d'opportunité (non-exécuté) + frais**

— chaque terme ayant son propriétaire (le délai : l'infra et le scheduler ; le trading : la tactique ; l'opportunité : la sizing des tranches), ce qui en fait un outil d'*attribution* et pas seulement de mesure. La cascade complète du desk systématique empile les paper portfolios : idéal non contraint → contraint (l'écart = coût des contraintes, le TC de 4.2.3) → exécuté (l'écart = TCA proprement dite) → net de frais ; c'est la même décomposition que le monitoring live-vs-attendu de 6.3.2, aux échelles emboîtées. Les pièges de mesure sont sérieux : le **biais de sélection des non-exécutés** (les ordres limites non remplis sont ceux qui auraient été les meilleurs trades — une TCA qui les ignore embellit la tactique passive), la contamination du benchmark par son propre impact (mesurer vs VWAP quand on *est* 20% du volume), et le bruit — le coût par trade a un écart-type de plusieurs fois sa moyenne, la significativité exige d'agréger des milliers d'ordres (retour aux outils de 2.2). La sortie de la boucle est double : recalibrer le modèle de coûts de 4.3.1 (Y, c par titre — la TCA est la *source des paramètres* de l'optimiseur, pas un rapport de conformité) et alimenter la recherche d'alphas d'exécution de 5.4. Références : Perold 1988 ; Kissell, *The Science of Algorithmic Trading and Portfolio Management* (2013) ; Almgren et al. 2005 (le même papier sert la mesure et le modèle — la boucle incarnée).

---

**La branche 5 est ouverte au niveau 2-3** — cinq nœuds, formules et sources. L'arbre : 1 (sauf 1.4), 2, 3, 4, 5 couverts ; restent **6. Infra & organisation** (la dernière branche vierge), **1.4 cibles & labels**, les forages profonds optionnels (5.2 propagateur, 5.3 HJB), et la consolidation du squelette — qui commence à réclamer sa régénération : 3.4.5, deux appendices transversaux, les renvois TCA↔4.3↔6.3. Un mot et je fore la 6, ou je regénère le squelette consolidé d'abord.

---

## [M089] Humain — 2026-07-24 06:50:25

Fore le 1

---

## [M090] Assistant — 2026-07-24 06:50:29

---

## [M091] Humain — 2026-07-24 06:50:41

Fore le 5.1

---

## [M092] Assistant — 2026-07-24 06:52:10

On fore : **5.1 Microstructure des marchés** — l'anatomie du terrain avant la physique de l'impact. Le sous-arbre local :

```
5.1 MICROSTRUCTURE             où et comment les trades se forment
│
├── 5.1.1 Carnets, priorité, tick     files, spread = sélection adverse, Roll
├── 5.1.2 Auctions                    prix d'équilibre batché, la clôture
├── 5.1.3 Fragmentation & routing     NBBO, dark pools, toxicité des venues
└── 5.1.4 Crypto                      perps & funding, AMM & LVR, MEV
```

**5.1.1 Carnets d'ordres, priorité, tick size — la mécanique des files**

Le carnet est un ensemble de files d'attente par niveau de prix, servi en priorité **prix-temps** (meilleur prix d'abord, puis premier arrivé — le pro-rata de certains futures étant l'exception qui change tout le jeu : on y sur-cote en taille au lieu de courir en temps). L'objet théorique central est le spread, et sa lecture moderne est informationnelle : dans **Glosten-Milgrom** (JFE 1985), le teneur de marché cote ask = E[v | le prochain trade est un achat] et bid = E[v | vente] — le spread est la prime de **sélection adverse**, ce qu'il perd contre les informés facturé aux non-informés ; il croît avec la probabilité d'information et s'effondre... en fermant le marché quand elle est trop haute (le no-trade de Milgrom-Stokey en toile de fond). La décomposition empirique standard (Huang & Stoll, RFS 1997) partage le spread réalisé en traitement / sélection adverse / inventaire ; et l'estimateur de **Roll** (JF 1984) mérite d'être connu pour son élégance : sous spread constant s et valeur fondamentale martingale, le bid-ask bounce crée une autocovariance négative des variations de prix, d'où

> **s = 2·√(−cov(Δp_t, Δp_{t−1}))**

— la mesure du spread sans voir les quotes, encore utile sur données pauvres (et l'explication du biais haussier des vols estimées en tick, §1.2.2).

Le **tick size** structure tout le reste : c'est le pas de prix minimal, et son rapport au spread « naturel » de l'actif classe les marchés. Actif *large-tick* (le spread bute sur son plancher d'un tick) : files profondes, la ressource rare est la **position dans la queue** — la priorité temporelle a une valeur monétisable, le jeu est d'être en tête (5.4). Actif *small-tick* : files minces, surenchère permanente au tick, le jeu se déplace vers le prix. La valeur d'une position de file se calcule d'ailleurs proprement : c'est une option d'exécution dont le sous-jacent est le flux, et les remplissages en tête sont mesurablement moins adverses (markouts, §5.4). Références d'ensemble : Harris, *Trading and Exchanges* (2003) ; Bouchaud et al., *Trades, Quotes and Prices* (2018) pour les régularités empiriques du carnet (profondeur en bosse, flux autocorrélé) ; Cont-Kukanov-Stoikov (2014) pour la sensibilité prix-flux au meilleur niveau, déjà citée côté tactique.

**5.1.2 Auctions — la liquidité batchée**

L'enchère d'appel (call auction) inverse la logique du continu : accumulation d'ordres sans exécution, diffusion d'un prix indicatif et d'un **imbalance**, puis croisement à l'instant T au prix unique qui **maximise le volume exécutable** (avec règles de départage sur l'imbalance résiduel et la proximité du dernier prix). Trois vertus d'exécution : pas de spread (prix unique), pas de course de vitesse (le batching neutralise la latence — l'argument théorique de Budish, Cramton & Shim, QJE 2015, qui proposent d'en faire le mode *permanent* du marché), et une profondeur sans équivalent dans le continu. D'où leur rôle croissant : la clôture US concentre de l'ordre de 10% du volume quotidien (indexation, MOC/LOC), l'ouverture absorbe l'information overnight (§1.2.2 : la décomposition overnight/intraday commence ici), et les enchères de volatilité (reprises post-halt, LULD) gèrent les discontinuités. Pour le desk systématique, deux usages distincts : *canal d'exécution* — le rebalancement lent passe par la clôture, où l'impact par dollar est minimal, au prix d'un risque de prix jusqu'à 16h — et *source de signaux* — les imbalances publiés (Nasdaq dès 15h50) prédisent le mouvement vers la clôture et sa réversion le lendemain, la famille événementielle du §1.1.5. Le piège de backtest associé : un signal « exécuté à la clôture » qui se calcule *sur* la clôture est le look-ahead du §2.2 sous son déguisement le plus fréquent — l'entrée légitime est l'enchère du lendemain ou le prix indicatif à la coupure des MOC.

**5.1.3 Fragmentation et routing — un marché en morceaux**

L'equity US se négocie sur des dizaines de venues : bourses lit (16+), dark pools (~30 ATS), et l'internalisation par les wholesalers (la majorité du flux retail, via payment for order flow). Le ciment réglementaire est Reg NMS : le **NBBO** (meilleur bid/offer consolidé) et l'order protection rule (interdiction d'exécuter à travers un meilleur prix affiché ailleurs) — qui créent eux-mêmes la course : le NBBO officiel (SIP) est en retard sur les flux directs, et « connaître le vrai NBBO avant les autres » est un métier. Le **smart order router** résout, ordre par ordre, un problème d'allocation sous incertitude : répartir entre venues selon la profondeur affichée *et* cachée, les grilles de frais (maker-taker vs taker-maker inversé — le rebate change le signe du coût marginal), la probabilité de remplissage, et la **toxicité** mesurée de chaque venue — les markouts post-exécution par venue, qui révèlent où le flux adverse se concentre. Les dark pools exécutent au midpoint sans pré-trade transparency : spread économisé, mais sélection adverse redistribuée — le résultat de référence est Zhu (« Do Dark Pools Harm Price Discovery? », RFS 2014) : les informés, pressés d'exécuter, migrent vers le lit ; le dark écrème le flux non informé, ce qui *améliore* le price discovery lit tout en dégradant la qualité moyenne du remplissage dark aux moments informés — exactement ce que les markouts par venue mesurent. Sur l'effet net de la fragmentation : O'Hara & Ye (JFE 2011) trouvent qu'elle n'a pas dégradé — plutôt amélioré — la qualité d'exécution consolidée. Version Europe : MiFID II, double volume caps sur le dark, essor des *periodic auctions* — le batching de 5.1.2 en format micro. Pour le desk : la fragmentation est d'abord un problème de **données** (consolider soi-même les feeds, horodater à la réception — le §1.2.4 appliqué au tick) avant d'être un problème de trading.

**5.1.4 Crypto — perps, AMM, MEV**

*Perpétuels.* Le carnet est standard ; le produit ne l'est pas. Le **funding** arrime le perp au spot sans échéance :

> funding = clamp( TWAP(premium index) + taux d'intérêt, ±cap ),  premium = (perp − index)/index

réglé toutes les 8h (00/08/16 UTC) entre longs et shorts — d'où trois objets d'exécution : les instants de règlement comme grille (exécuter juste avant/après un funding extrême a un coût/gain explicite), le **mark price** (médiane ou composite multi-venues) qui gouverne marges et liquidations en découplant le P&L du dernier prix local — la défense anti-mèche déjà vue en 4.5.4 — et l'**index price** (panier de spots) dont la composition est un risque de modèle de la venue. Le basis trade (long spot / short perp, encaisser le funding) est l'arbitrage structurel qui maintient tout l'édifice.

*AMM.* La liquidité on-chain n'est pas un carnet mais une courbe. Pool à produit constant x·y = k : prix spot p = y/x, et l'exécution de Δx contre le pool rend

> **Δy = y·Δx/(x + Δx)**,  prix moyen dégradé de ≈ Δx/x, prix marginal de ≈ 2Δx/x

— un impact **déterministe et lisible on-chain** avant de trader, transparence de coût sans équivalent tradfi. Uniswap v3 (Adams et al., 2021) concentre la liquidité par plages [p_a, p_b] via des réserves virtuelles — reconstituant de facto un carnet, avec des LP devenus market makers à inventaire. Le coût des LP a reçu sa formalisation propre : au-delà de l'« impermanent loss » (IL = 2√r/(1+r) − 1 pour un ratio de prix r), la mesure propre est le **LVR** — loss-versus-rebalancing (Milionis, Moallemi, Roughgarden & Zhang, 2022) : la perte du pool contre les arbitragistes qui le réalignent sur le prix externe, ≈ σ²/8 par unité de temps en produit constant — la sélection adverse de Glosten-Milgrom réécrite pour les courbes : le LP cote un prix figé contre un flux informé par construction.

*MEV.* Dans la mempool publique, une transaction est visible avant inclusion : un ordre swap peut être **sandwiché** — achat inséré avant (front-run), revente après (back-run), la victime exécutant au pire de sa tolérance de slippage. Documenté par Daian et al. (« Flash Boys 2.0 », IEEE S&P 2020) avec les priority gas auctions ; l'architecture post-Merge (proposer-builder separation, blocs construits aux enchères par des builders spécialisés) a industrialisé l'ordonnancement. Les défenses font partie du coût d'exécution on-chain : routage privé (Flashbots Protect et équivalents), agrégateurs, limites de slippage serrées, découpage. S'ajoute, inter-venues, le **lead-lag** : le price discovery vit sur la venue dominante (mesurable par l'information share de Hasbrouck, JF 1995) et les autres suivent à quelques centaines de millisecondes — à la fois un signal tactique (5.4) et une règle de mesure (la vol et les prix de référence se prennent sur la venue directrice, §1.2.2).

---

Nœud foré au niveau 3, aligné sur le grain de la branche 4. Coutures : Glosten-Milgrom → LVR est le même théorème sous deux technologies de marché (candidat pour l'encadré « sélection adverse » transversal à 5.1/5.4) ; le look-ahead d'auction rejoint la liste canonique de 2.2 ; la consolidation des feeds renvoie à 6.1. Restent en frontière : **5.2 en profondeur** (propagateur et ordre de flux autocorrélé), **la branche 6** entière, **1.4**, et la régénération du squelette consolidé qui devient urgente — trois amendements en attente (3.4.5, appendices, renvois).

---

## [M093] Humain — 2026-07-24 06:53:06

Fore le 5.2, inclue bien les formules mathématiques essentielles

---

## [M094] Assistant — 2026-07-24 06:54:28

On fore : **5.2 Impact de marché** — la physique du coût, le nœud le plus « lois d'échelle » de tout l'arbre. Le sous-arbre local :

```
5.2 IMPACT DE MARCHÉ           comment mes trades déplacent les prix
│
├── 5.2.1 La loi en racine carrée     I ∝ σ√(Q/V), universalité, liquidité latente
├── 5.2.2 Temporaire vs permanent     Kyle linéaire, relaxation, fair pricing
├── 5.2.3 Le modèle à propagateur     G(l), mémoire longue du flux, condition de diffusion
└── 5.2.4 Mesure empirique            métaordres, biais de conditionnement, crypto
```

**5.2.1 La loi en racine carrée — l'empirie et sa théorie**

Le fait, déjà emprunté deux fois par l'amont (4.3.1, 4.4.4), énoncé maintenant avec ses conditions : pour un **métaordre** — une intention parente de taille Q, découpée en ordres enfants et exécutée sur une durée T de l'ordre de la fraction de journée — l'impact moyen au moment de la complétion vaut

> **I(Q) = Y · σ_daily · (Q/V_daily)^δ**,  δ ≈ 0,4–0,6, Y ≈ 0,5–1

avec σ_daily la volatilité quotidienne et V_daily le volume quotidien. Trois propriétés remarquables. L'**universalité** : le même exposant et le même ordre de grandeur de Y sur les actions de toutes capitalisations, les futures, les options, le FX, et le bitcoin (Donier & Bonart, « A million metaorder analysis of market impact on the Bitcoin », Market Microstructure and Liquidity 2015 — même δ ≈ 0,5 sur un marché sans aucune institution commune avec l'equity) — la signature d'un mécanisme indépendant des détails institutionnels. La **quasi-indépendance en T** : à Q fixé, exécuter en 2h ou en 6h change peu l'impact au premier ordre (elle gouverne en revanche la part qui relaxe, 5.2.2). Et la **concavité**, qui est le scandale théorique : doubler la taille coûte √2, pas 2 — le millionième dollar impacte moins que le premier.

Le scandale, parce que le modèle canonique prédit du linéaire. **Kyle** (Econometrica 1985), version statique : un informé connaissant v ~ N(p₀, σ_v²) trade x, noyé dans le flux bruité u ~ N(0, σ_u²) ; le market maker efficient cote p = E[v | x+u], et l'équilibre linéaire donne

> **p = p₀ + λ·(x + u)**,  **λ = σ_v / (2σ_u)**

— l'impact est linéaire en taille, de pente le ratio information/bruit ; le « Kyle's lambda » reste l'unité de mesure de l'illiquidité. La résolution de la contradiction est la théorie de la **liquidité latente** (Tóth et al., PRX 2011 ; formalisée en réaction-diffusion par Donier, Bonart, Mastromatteo & Bouchaud, « A fully consistent, minimal model for non-linear market impact », Quantitative Finance 2015) : la liquidité *affichée* au carnet est une fraction infime des intentions ; le carnet **latent** a une densité de volume ρ(p) qui s'annule *linéairement* au prix courant — ρ(p) ≈ ρ'·|p − p_t| — parce que les intentions proches du prix sont exécutées ou révélées en permanence. Absorber Q consomme alors l'aire sous la densité :

> Q = ∫₀^I ρ'·x dx = (ρ'/2)·I²  ⟹  **I = √(2Q/ρ')**

— la racine carrée tombe de la géométrie, et l'impact mesure la *rareté locale de liquidité*, pas le contenu informationnel du trade. Le raccord des deux mondes : Kyle décrit la composante permanente/informationnelle agrégée, la racine carrée décrit le coût mécanique d'exécution — 5.2.2 fait le partage.

**5.2.2 Temporaire vs permanent — ce qui relaxe et ce qui reste**

Le profil temporel type d'un métaordre : pendant l'exécution, l'impact courant croît en racine de la fraction exécutée — I(q) ≈ Y·σ·√(q/V), trajectoire concave — culmine au pic I_peak = I(Q) à la complétion, puis **relaxe** sur des heures vers un plateau

> **I_∞ ≈ (½ à ⅔)·I_peak**

L'ordre de grandeur du plateau n'est pas un hasard : sous la condition de *fair pricing* (le prix post-relaxation égale le prix moyen payé par le métaordre — l'équilibre où ni l'exécutant ni ses contreparties ne gagnent mécaniquement l'un sur l'autre ; Farmer, Gerig, Lillo & Waelbroeck, « How efficiency shapes market impact », Quantitative Finance 2013), le plateau vaut exactement le coût moyen, soit pour un impact courant en √q :

> I_∞ = (1/Q)·∫₀^Q Y·σ·√(q/V) dq = (2/3)·I_peak

Le partage conceptuel s'ensuit : la composante **permanente** est informationnelle (le marché a appris quelque chose du flux — le λ de Kyle, agrégé), la composante **transitoire** est mécanique (la pression sur la liquidité latente, qui se reconstitue). Deux conséquences opérationnelles directes. Pour le *coût* : ce que paie le desk est l'impact moyen pendant l'exécution (~⅔ du pic pour δ = ½), pas le pic — c'est ce nombre que le modèle de 4.3.1 doit calibrer. Pour le *signal* : la relaxation post-métaordre est une prédiction de prix — l'écho du reversal court terme du §1.1.1, dont une part substantielle n'est que la relaxation de l'impact des flux d'autrui ; la frontière entre « alpha de reversal » et « fourniture de liquidité aux métaordres » est purement sémantique, et c'est l'articulation profonde entre les branches 1 et 5.

**5.2.3 Le modèle à propagateur — la dynamique complète**

Le cadre qui unifie (Bouchaud, Gefen, Potters & Wyart, « Fluctuations and response in financial markets », Quantitative Finance 2004) : le prix comme somme des empreintes de tous les trades passés,

> **p_t = p_{−∞} + Σ_{s<t} G(t−s)·ε_s·f(v_s) + Σ_{s<t} η_s**

avec ε_s = ±1 le signe du trade s, f(v) ≈ v^θ (θ ≈ 0,1–0,3 : l'impact d'un trade *individuel* dépend à peine de sa taille — l'information est dans le signe), et G(l) le **propagateur** : l'empreinte résiduelle d'un trade l pas après. Le fait empirique qui contraint tout : le flux signé a une **mémoire longue** —

> C(l) = corr(ε_t, ε_{t+l}) ~ c·l^{−γ},  **γ ≈ 0,5**

(Lillo & Farmer, « The long memory of the efficient market », Studies in Nonlinear Dynamics & Econometrics 2004) — l'autocorrélation des signes décroît si lentement que sa somme diverge, conséquence directe du découpage des métaordres (la distribution de leurs tailles en loi de puissance produit exactement ce γ). Le paradoxe : un flux aussi prévisible devrait rendre les prix prévisibles. La résolution est la **condition de diffusion** : pour que p_t reste une quasi-martingale malgré le flux persistant, le propagateur doit décroître à la vitesse qui compense exactement,

> Var(p_{t+l} − p_t) ∝ l  ⟹  **G(l) ~ l^{−β},  β = (1−γ)/2 ≈ 0,25**

— l'impact *doit* être transitoire, et sa vitesse de relaxation n'est pas libre : elle est cousue à la mémoire du flux. C'est le théorème central du nœud : la forme de G, la persistance du flux et l'efficience des prix sont une seule contrainte à trois inconnues. Raffinements documentés : le modèle à propagateur unique sur-relaxe aux longs horizons — versions à deux composantes (transitoire + permanente, le HDIM de Lillo et al.), et le **cross-impact** : la généralisation matricielle p_t = Σ G_ij(t−s)·ε_j,s couple les actifs (trader l'un déplace l'autre via les arbitragistes et les facteurs communs — Benzaquen, Mastromatteo, Tóth & Bouchaud 2017) ; la matrice de cross-impact recoupe la structure factorielle de 4.1, et l'ignorer sous-estime le coût des trades *de facteur* (le rebalancement simultané de 500 titres du même secteur impacte le facteur, pas 500 idiosyncrasies). Synthèse de tout le nœud : Bouchaud, Bonart, Donier & Gould, *Trades, Quotes and Prices* (2018), chapitres impact.

**5.2.4 Mesure empirique — les biais avant les chiffres**

La mesure exige des **métaordres** reconstitués — des données propriétaires (les ordres parents d'un broker ou du desk), car le flux public ne montre que les enfants anonymes. Les jeux de référence : Almgren, Thum, Hauptmann & Li (2005, Citigroup — le papier fondateur, forme fonctionnelle : impact temporaire ∝ (Q/VT)^{3/5}, permanent ≈ linéaire), Bacry, Iuga, Lasnier & Lehalle (2015), Zarinelli, Treccani, Farmer & Lillo (« Beyond the square root », 2015 — le plus grand échantillon public, confirmant δ ≈ 0,5 avec une dépendance logarithmique résiduelle en participation), et côté crypto Donier-Bonart 2015. Les biais de mesure sont le vrai sujet, car ils sont tous du même côté. Le **conditionnement à l'information** : les métaordres ne sont pas aléatoires — on achète parce qu'on prédit la hausse — donc le drift observé pendant l'exécution mélange impact et alpha ; la séparation exige soit des trades non informés identifiables (rebalancements mécaniques, rolls), soit le profil de *relaxation* (l'alpha ne relaxe pas, l'impact mécanique si). L'**endogénéité de la taille** : le desk trade gros quand la liquidité est bonne — la taille est choisie en fonction du coût anticipé, ce qui aplatit la courbe mesurée (les gros Q observés sont ceux des jours faciles). Et le **biais de survie des enfants passifs** hérité de 5.5 : les tranches limites non remplies manquent à l'appel côté coût. La conséquence de design, qui referme la boucle sur 6.2 : la calibration propre exige de **logger l'intention** (le parent, sa taille décidée, son heure de décision) et pas seulement les exécutions — le pendant exécution du registre d'hypothèses de la recherche ; et l'étalon-or, coûteux mais sans biais, est l'**expérience randomisée** (une fraction des métaordres tirée au sort en taille/rythme — la pratique des grands desks pour calibrer Y hors conditionnement). En crypto, la mesure est paradoxalement plus facile (données tick publiques complètes, AMM à impact déterministe comme référence) et plus piégée (wash trading dans V_daily, §1.2.4 : un ADV gonflé sous-estime Q/V donc sous-estime les coûts réels — l'erreur qui fabrique des capacités fictives en 4.4.4).

---

Nœud foré au niveau 3, le plus dense en lois d'échelle de l'arbre — δ ≈ ½, γ ≈ ½, β = (1−γ)/2, le triplet à retenir. Coutures : reversal ↔ relaxation (1.1.1/5.2.2) mérite un encadré ; cross-impact ↔ modèle factoriel (5.2.3/4.1) ; wash trading ↔ capacité (1.2.4/4.4.4/5.2.4). En frontière : **5.3 en profondeur** (la dérivation Almgren-Chriss complète et son extension HJB), **la branche 6** — dernière vierge —, **1.4**, et le squelette consolidé en attente. La branche 6 fermerait l'arbre au niveau 2 partout : mon vote pour elle.

---

## [M095] Humain — 2026-07-24 06:55:14

Pareil pour le 5.3

---

## [M096] Assistant — 2026-07-24 06:56:38

On fore : **5.3 Scheduling** — le rythme optimal d'exécution, le nœud le plus « contrôle optimal » de l'arbre. Le sous-arbre local :

```
5.3 SCHEDULING                 répartir Q sur [0,T] : impact vs risque vs alpha
│
├── 5.3.1 Almgren-Chriss            la dérivation complète, κ, frontière
├── 5.3.2 Benchmarks                IS / VWAP / TWAP / POV, le dilemme du trader
├── 5.3.3 Alpha & urgence           drift, decay, le raccord Gârleanu-Pedersen
└── 5.3.4 Extensions                Obizhaeva-Wang, Gatheral, HJB, adaptatif
```

**5.3.1 Almgren-Chriss — la dérivation complète**

Le programme (Almgren & Chriss, « Optimal Execution of Portfolio Transactions », Journal of Risk 2000) : liquider X unités sur [0, T], découpé en pas τ, avec x_k la position résiduelle (x_0 = X, x_N = 0) et v_k = (x_{k−1} − x_k)/τ le rythme. Deux impacts, tous deux linéaires dans la version canonique : **permanent** — le prix dérive de −γ·v_k·τ à chaque pas — et **temporaire** — le prix d'exécution est dégradé de h(v) = ε·sgn(v) + η·v, subi seulement par la tranche courante. Le prix diffuse par ailleurs : σ√τ·ξ_k. Le coût total (l'implementation shortfall vs prix de décision) a alors pour moments

> **E[C] = ½·γX² + ε·X + η̃·Σ_k τ·v_k²**,  η̃ = η − γτ/2
> **Var[C] = σ²·Σ_k τ·x_k²**

Première leçon, lisible avant toute optimisation : le terme permanent ½γX² est **indépendant du chemin** — avec un impact permanent linéaire, seule compte la taille totale, et l'optimisation ne porte que sur l'arbitrage temporaire/risque (la linéarité du permanent n'est pas gratuite : c'est une condition de non-arbitrage, cf. 5.3.4). Le programme moyenne-variance min E[C] + λ_r·Var[C] donne par calcul des variations l'équation d'Euler η̃·ẍ = λ_r σ²·x, d'où la trajectoire en forme close

> **x(t) = X · sinh(κ(T−t)) / sinh(κT)**,  **κ = √(λ_r σ² / η̃)**

— exponentielle décroissante de constante de temps 1/κ, l'**urgence** : elle croît avec l'aversion au risque et la vol (le risque de prix presse), décroît avec le coût d'impact (la friction freine). Cas limites éclairants : λ_r = 0 redonne la ligne droite (TWAP — c'est le résultat antérieur de Bertsimas & Lo 1998, coût espéré seul) ; λ_r → ∞ donne l'exécution immédiate. Et la propriété la plus utile en pratique : quand κT ≫ 1, la trajectoire devient x(t) ≈ X·e^{−κt} — **indépendante de T** : le problème a une échelle de temps intrinsèque 1/κ, et fixer une deadline lointaine ne change rien au comportement effectif. En variant λ_r, on trace la **frontière efficiente d'exécution** (E[C], Var[C]) — l'objet que le desk montre à l'allocateur pour transformer « exécutez bien » en un point choisi sur une courbe.

**5.3.2 Benchmarks — le dilemme du trader**

Chaque benchmark industriel est un objectif d'optimisation déguisé, et les nommer révèle ce qu'ils minimisent. **IS/arrival** : viser le prix de décision — l'objectif d'Almgren-Chriss lui-même, le seul benchmark aligné sur le coût économique vrai (Perold, §5.5). **TWAP** : rythme constant — optimal à aversion nulle et impact linéaire. **VWAP** : suivre le profil de volume intra-journalier u(t) = V(t)/V_total (le U de la journée equity) — sous l'hypothèse standard que la liquidité suit le volume, trader v(t) ∝ u(t) minimise l'impact à participation constante *effective* ; c'est l'objectif de *tracking* (minimiser Var[prix payé − VWAP]), pas de coût — un ordre à 20% du volume « bat son VWAP » en le fabriquant. **POV** : participation fixe v(t) = p·V_marché(t) — le benchmark adaptatif minimal, sans deadline garantie. Le **dilemme du trader** structure le choix : exécuter vite minimise le risque vs arrival mais maximise l'impact ; lentement l'inverse — et chaque benchmark est une position sur ce spectre, IS assumant l'arbitrage explicitement, VWAP/POV le déléguant au profil de marché. La cohérence d'ensemble (Kissell, *The Science of Algorithmic Trading*, 2013 ; Guéant, *The Financial Mathematics of Market Liquidity*, 2016) : le benchmark de la TCA (§5.5) doit être celui de l'objectif — mesurer vs VWAP un ordre schedulé en IS fabrique du bruit d'attribution. Crypto : pas de clôture, un profil u(t) par sessions (US/Asie) et par grille de funding, et un V_marché contaminé par le wash trading (§1.2.4) qui rend le POV naïf dangereux — participer à 10% d'un volume à moitié fictif, c'est participer à 20% du vrai.

**5.3.3 Alpha et urgence — le terme manquant**

Le programme d'Almgren-Chriss suppose le prix martingale ; or le desk exécute *parce qu'il a un signal*. Ajouter un drift attendu μ(t) sur le prix (positif pour un achat motivé par un alpha) modifie le coût espéré de −∫₀ᵀ μ(t)·x_rest(t)·dt côté vendeur — chaque unité non encore exécutée manque le mouvement prédit : c'est le **coût d'opportunité**, et l'équation d'Euler devient

> η̃·ẍ(t) = λ_r σ²·x(t) + μ(t)/2

Avec un alpha à décroissance exponentielle μ(t) = μ₀·e^{−φt} (φ = ln2/H, la demi-vie du §2.1), la solution ajoute à la trajectoire sinh un terme particulier en e^{−φt} : la trajectoire est **front-loadée**, d'autant plus que φ est grand — un signal qui meurt vite s'exécute vite, quitte à payer l'impact ; un signal lent s'étale. La règle d'ordre de grandeur qui en sort : l'urgence effective est max(κ, ~φ) — le scheduling est borné en dessous par la vitesse de péremption de l'information. Et le raccord annoncé : c'est le **même arbitrage que Gârleanu-Pedersen** (§4.3.3) aux deux échelles — GP décide *combien* charger d'un signal selon son φ_k (l'aim portfolio actualisé), Almgren-Chriss augmenté décide *à quel rythme* l'atteindre selon le même φ ; dans le cadre unifié, le facteur d'actualisation 1/(1+φa/γ) et le front-loading sont les deux projections d'une seule politique dynamique. Le point organisationnel qui en découle : l'interface portefeuille → exécution doit transporter **l'urgence du trade** (le φ du signal qui l'a causé), pas seulement sa taille — un ticket d'exécution sans urgence force le scheduler à une aversion moyenne fausse pour tout le monde.

**5.3.4 Extensions — résilience, non-arbitrage, HJB, adaptatif**

*Obizhaeva-Wang* (« Optimal trading strategy and supply/demand dynamics », Journal of Financial Markets 2013) : remplacer l'impact temporaire instantané par un carnet qui se **reconstitue à vitesse ρ** (impact transitoire à décroissance exponentielle — la version exécutable du propagateur de 5.2.3). La solution optimale change de forme : deux **blocs** discrets aux extrémités et un rythme constant entre,

> bloc initial = bloc final = X/(ρT + 2),  taux intermédiaire = ρX/(ρT + 2)

— l'haltère : on consomme d'emblée la profondeur disponible, on trade ensuite exactement au rythme où elle se régénère, on finit en absorbant ce qui reste. *Gatheral* (« No-dynamic-arbitrage and market impact », Quantitative Finance 2010) fournit la police des modèles : impact instantané f(v) et noyau de décroissance G(l) ne sont pas librement combinables — un impact permanent **non linéaire** crée un arbitrage dynamique (acheter puis revendre en profitant de la convexité), et les paires admissibles sont contraintes (permanent ⟹ linéaire ; racine carrée ⟹ transitoire avec décroissance compatible — la cohérence exacte avec la condition de diffusion de 5.2.3).

*Le traitement HJB complet* (Cartea, Jaimungal & Penalva, *Algorithmic and High-Frequency Trading*, 2015 ; Guéant 2016) pose la fonction valeur H(t, x, S, q) et l'équation d'Hamilton-Jacobi-Bellman associée ; l'apport n'est pas la re-dérivation d'AC (qu'on retrouve en cas particulier, avec l'ansatz exponentiel-quadratique des utilités CARA) mais l'ouverture du menu des contrôles : exécuter **aussi en ordres limites** — avec intensité de remplissage λ(δ) = A·e^{−kδ} à distance δ du mid, le contrôle optimal de la version liquidation donne des cotes du type δ*(t,q) = 1/k + composante d'inventaire — le pont formel avec Avellaneda-Stoikov (§5.4) : liquidation et market making sont le même problème HJB avec des conditions terminales différentes. *L'adaptatif* enfin (Almgren & Lorenz, « Adaptive arrival price », 2007) : la trajectoire statique re-résolue à chaque pas n'est **pas** la politique dynamique optimale — la vraie solution est « aggressive in the money » : accélérer quand l'exécution est en avance sur son budget de coût (dépenser les gains de prix en réduction de risque), ce qui améliore strictement la frontière moyenne-variance ; le principe se retrouve dans tous les schedulers de production sous forme de bandes autour de la trajectoire cible — le MPC de 4.3.4, descendu à l'échelle intra-journalière.

---

Nœud foré au niveau 3. Le triplet à retenir : κ = √(λ_rσ²/η̃) (l'urgence), l'haltère X/(ρT+2) (la résilience), max(κ, φ) (l'alpha borne le rythme). Coutures : GP↔AC mérite l'encadré « une politique, deux échelles » ; Gatheral↔condition de diffusion (5.2.3) ; le ticket-avec-urgence rejoint l'interface de 6.3. Reste en frontière : **5.4** et **5.5** au grain de forage si tu veux clore la branche 5 uniformément, **la branche 6** — dernière vierge — et le squelette consolidé. La 6 fermerait l'arbre : mon vote inchangé.

---

## [M097] Humain — 2026-07-24 06:57:32

5.4

---

## [M098] Assistant — 2026-07-24 06:58:57

On fore : **5.4 Tactique & alphas d'exécution** — la décision ordre par ordre, sous le scheduler. Le sous-arbre local :

```
5.4 TACTIQUE                   chaque tranche : où, comment, à quel prix
│
├── 5.4.1 Limit vs market           l'arbitrage, la file comme actif
├── 5.4.2 Signaux de microstructure  microprice, OFI, signes de trades
├── 5.4.3 Anti-sélection adverse     markouts, spread réalisé, défenses
└── 5.4.4 Making vs taking           Avellaneda-Stoikov, GLFT, crypto
```

**5.4.1 Limit vs market — l'arbitrage fondamental et la file comme actif**

La comparaison en espérance, pour une tranche d'achat au meilleur bid contre un ordre market à l'ask :

> **E[coût_limit] = P_fill·(−s/2 + AS) + (1 − P_fill)·C_chase**  vs  **E[coût_market] = +s/2 + impact**

L'ordre limite *gagne* le demi-spread s'il est rempli, mais paie deux termes cachés : la **sélection adverse** AS — il n'est rempli que quand le marché le traverse, donc conditionnellement à une information défavorable — et le **coût de chasse** C_chase en cas de non-remplissage (re-coter plus haut, ou finir en market à un prix dégradé, le biais de sélection des non-remplis de §5.5). L'arbitrage bascule avec le régime de tick (§5.1.1) : sur un actif large-tick, s/2 est gros et la file profonde — le passif domine *si* on obtient une bonne position de file ; sur un actif small-tick, s/2 est mince et l'AS relative énorme — l'agressif raisonné reprend l'avantage.

La file est donc un actif, et sa valeur se calcule : **Moallemi & Yuan** (« The Value of Queue Position in a Limit Order Book », 2016) modélisent la position q dans la file comme une option d'exécution dont la valeur *décroît* avec q — les remplissages de tête de file arrivent sur le flux « normal » (peu informé), ceux de fond de file n'arrivent que dans les balayages (très informés) ; l'écart de markout entre tête et queue de file atteint une fraction significative du spread, et il justifie toute la tactique d'acquisition de priorité : coter tôt, ne jamais annuler-recoter sans raison (on repart en fond de file), viser les instants où la file se reconstruit (post-trade, post-tick-change). La quantité de contrôle est P_fill, estimable par first-passage sur la dynamique de file (arrivées, annulations, exécutions devant soi — le cadre de files d'attente de Cont-de Larrard 2013).

**5.4.2 Signaux de microstructure — les prédicteurs à horizon de secondes**

Le prix de référence d'abord : le mid ignore les tailles, or un bid de 10 000 contre un ask de 500 n'est pas un marché symétrique. Le **microprice** pondère en croix :

> **P_micro = (Q_b·P_a + Q_a·P_b) / (Q_a + Q_b)**

— proche de l'ask quand le bid est lourd (la pression acheteuse pousse vers le haut), et démontrablement meilleur prédicteur du mid futur que le mid ; Stoikov (« The Micro-Price », Quantitative Finance 2018) en donne la version propre — l'espérance martingale du mid à l'équilibre de la chaîne imbalance/spread — dont la forme croisée est l'approximation au premier ordre. Le signal de flux ensuite : l'**order flow imbalance** de Cont, Kukanov & Stoikov (« The Price Impact of Order Book Events », Journal of Financial Econometrics 2014) agrège les événements au meilleur niveau —

> OFI_t = Σ (ΔQ_b·1{contribution bid} − ΔQ_a·1{contribution ask}),  **ΔP ≈ β·OFI,  β ∝ 1/profondeur**

— la relation prix-flux la plus robuste de la microstructure : *linéaire* en OFI (contrairement à l'impact des volumes tradés seuls), de pente inverse de la profondeur, stable intra-jour. S'y ajoutent la classification des trades (**Lee & Ready** 1991 : signer par rapport au mid, tick test en cas d'égalité — trivial en crypto où l'agresseur est dans le flux), l'autocorrélation des signes (§5.2.3, exploitable à ces horizons), la détection de *sweeps* (un ordre qui traverse plusieurs niveaux signe un métaordre pressé — son suiveur immédiat est rentable, sa relaxation ensuite), et la déplétion de file (une file qui fond sans trades annonce le tick). Ces prédicteurs à IC élevé et decay en secondes ne sont pas des « signaux » au sens des branches 1-3 — leur capacité est absorbée par leur propre exploitation tactique — mais ils gouvernent chaque décision de placement : c'est l'alpha *d'exécution*, dont la monnaie est le coût évité, pas le P&L directionnel.

**5.4.3 Anti-sélection adverse — mesurer, puis se défendre**

La mesure universelle est le **markout** : pour une exécution de signe ε au prix p,

> **M(τ) = ε·(mid_{t+τ} − p)**,  τ ∈ {100ms, 1s, 10s, 1min}

— le P&L marked-to-mid de l'exécution après τ. La décomposition canonique en découle : le *spread effectif* 2ε(p − mid_t) se partage en **spread réalisé** 2ε(p − mid_{t+τ}) — ce que le passif gagne vraiment — et **sélection adverse** 2ε(mid_{t+τ} − mid_t) — ce que le mouvement post-trade lui reprend (Glosten 1987 pour le cadre ; c'est la version mesurable du spread de Glosten-Milgrom de §5.1.1, et la métrique par laquelle 5.1.3 note la toxicité des venues). Un profil M(τ) systématiquement négatif et croissant en |τ| signe un flux contre lequel on ne devrait pas coter.

Les défenses, par ordre de coût : les **filtres de fair value** — ne pas laisser reposer un ordre quand le microprice ou l'OFI lui sont contraires (l'essentiel de l'AS se concentre dans des fenêtres identifiables : la cote « stale » après un mouvement de la venue directrice est le repas gratuit des arbitragistes de latence) ; les **annulations conditionnelles** (retirer sur déplétion de file, sur sweep adjacent, sur signal de la venue leader — le lead-lag de §5.1.4 utilisé en bouclier) ; l'évitement des **fenêtres toxiques** programmées — annonces macro (§1.2.4), instants de funding crypto, ouvertures — où l'AS explose ; et les protections de structure de marché quand elles existent (speed bumps, last look en FX — avec leur propre coût de rejet). La limite de l'exercice est un théorème d'équilibre : l'AS ne s'élimine pas, elle se *tarife* — un passif parfaitement défendu ne remplit plus rien (P_fill → 0 dans l'équation de 5.4.1) ; l'optimum est un niveau d'AS assumé et payé en connaissance, pas zéro.

**5.4.4 Making vs taking — le cadre d'Avellaneda-Stoikov et sa descendance**

La frontière tactique ultime : à chaque instant, l'edge espéré de *faire* le marché vaut spread/2 + rebate − AS − coût d'inventaire, celui de le *prendre* vaut signal − spread/2 − frais − impact — et le desk systématique vit des deux côtés selon le titre, l'heure et le signal. Le cadre d'optimisation du côté maker est **Avellaneda-Stoikov** (« High-frequency trading in a limit order book », Quantitative Finance 2008) : un agent CARA(γ) cote autour d'un **prix de réservation** décalé par son inventaire q,

> **r_t = s_t − q·γ·σ²·(T−t)**

(détenir q unités rend vendeur : on décale les deux cotes contre son propre stock), avec des intensités de remplissage exponentielles λ(δ) = A·e^{−kδ} à distance δ de r, et le spread total optimal en forme close

> **δ_a + δ_b = γσ²(T−t) + (2/γ)·ln(1 + γ/k)**

— premier terme : la prime de risque d'inventaire ; second : l'arbitrage fréquence/marge dicté par l'élasticité k du flux. La descendance opérationnelle est **Guéant-Lehalle-Fernandez-Tapia** (« Dealing with the inventory risk », Mathematics and Financial Economics 2013) : bornes d'inventaire dures |q| ≤ Q, horizon infini, et le système se réduit à des équations linéaires donnant des cotes stationnaires δ\*(q) par niveau d'inventaire — la forme sous laquelle le market making se code réellement ; Cartea-Jaimungal-Penalva (2015) ajoutent l'ambiguïté de modèle et les signaux (coter *avec* l'OFI de 5.4.2 dans la dérive : le pont formel entre making et alpha court terme). Et le raccord annoncé en 5.3.4 tient : liquidation (AC augmenté d'ordres limites) et market making (AS/GLFT) sont **le même problème HJB** à conditions terminales près — un scheduler qui exécute en passif *est* un market maker à cible d'inventaire mobile.

Côté crypto, trois déplacements matériels. La grille **maker/taker** : les rebates maker des venues majeures (jusqu'à rendre le making net-positif hors AS) déplacent structurellement l'optimum vers le passif — le paramètre « rebate » entre dans l'équation de 5.4.1 au même titre que s/2. Le **lead-lag inter-venues** comme signal tactique premier : coter sur la venue retardataire avec la dérive de la directrice (l'information share de Hasbrouck, §5.1.4, transformée en fair-value filter) — la source d'AS dominante y étant précisément les cotes stales cross-venues. Et la **grille de funding** : autour de 00/08/16 UTC, flux de rebalancement prévisibles (§5.1.4) — fenêtre toxique pour le maker naïf, opportunité pour le maker informé du signe du funding. Le tout sur des carnets dont la profondeur affichée est moins fiable qu'en equity (spoofing moins policé, §1.2.4 côté données) : les filtres de 5.4.3 s'y règlent plus paranoïaques.

---

Nœud foré au niveau 3. Le fil conducteur à retenir : **le spread est un prix d'assurance contre l'information** — Glosten-Milgrom le théorise (5.1.1), le markout le mesure (5.4.3), Avellaneda-Stoikov le tarife dynamiquement (5.4.4), et le LVR le réécrit pour les AMM (5.1.4) ; c'est l'encadré transversal « sélection adverse » désormais complet sur ses quatre faces. Reste **5.5** pour clore la branche 5 uniformément, puis **la branche 6** — toujours la dernière vierge — et le squelette consolidé. Un chiffre suffit.

---

## [M099] Humain — 2026-07-24 06:59:25

5.5

---

## [M100] Assistant — 2026-07-24 07:00:36

On clôt la branche : **5.5 Transaction cost analysis** — la comptabilité qui referme la boucle exécution → recherche. Le sous-arbre local :

```
5.5 TCA                        mesurer ce que coûte vraiment l'implémentation
│
├── 5.5.1 Implementation shortfall     Perold, la décomposition additive
├── 5.5.2 La cascade d'attribution     paper portfolios emboîtés, netting, Shapley
├── 5.5.3 Pièges de mesure             biais de sélection, bruit, Simpson
└── 5.5.4 La boucle de retour          calibration, A/B, scorecards, gouvernance
```

**5.5.1 Implementation shortfall — la décomposition de Perold**

Le cadre (Perold, « The Implementation Shortfall: Paper Versus Reality », JPM 1988) : comparer le P&L du **portefeuille papier** — la décision exécutée instantanément, intégralement, sans frais, au prix de décision p_d — au P&L réel. Pour un ordre d'achat de Q titres décidé en p_d, dont les tranches q_j s'exécutent aux prix p_j et dont Q_u = Q − Σq_j reste non exécuté à l'horizon de mesure (prix p_T) :

> **IS = Σ_j q_j·(p_j − p_d) + Q_u·(p_T − p_d) + frais**

soit, en insérant le prix d'arrivée p_a (premier instant où l'ordre atteint le marché) :

> **IS = Q_exec·(p_a − p_d)** [délai] **+ Σ_j q_j·(p_j − p_a)** [trading] **+ Q_u·(p_T − p_d)** [opportunité] **+ frais**

Quatre termes, quatre propriétaires : le *délai* appartient à l'infra et au circuit de décision (le lag signal→ordre du §2.2, mesuré en production) ; le *trading* au scheduler et à la tactique (c'est lui que 5.2-5.4 optimisent) ; l'*opportunité* au dimensionnement des tranches et à la politique de complétion — le terme que les mesures naïves omettent et qui porte l'essentiel du fameux « iceberg des coûts » de Wagner : sur un signal vrai, ne pas exécuter coûte en espérance, et une tactique ultra-passive au trading flatteur se paie intégralement ici. La somme est le seul chiffre économiquement honnête : c'est l'écart exact entre le backtest (qui vit en papier) et le compte en banque — l'IS *est* la définition opérationnelle du terme de coûts que toutes les branches amont pénalisent.

**5.5.2 La cascade d'attribution — les paper portfolios emboîtés**

Le desk systématique généralise Perold en empilant les portefeuilles fictifs, chaque étage isolant une décision :

> P&L(idéal non contraint) → P&L(contraint) → P&L(schedulé) → P&L(exécuté) → P&L net

Écart 1 : le **coût des contraintes** — la mesure en euros du transfer coefficient de 4.2.3, ventilable contrainte par contrainte via les duals. Écart 2 : le délai et le rythme (la trajectoire d'AC vs l'exécution instantanée fictive). Écart 3 : la tactique (limit/market, venues — les markouts de 5.4.3 agrégés). Écart 4 : frais, financement, emprunt de titres. La télescopie est la même que le monitoring live-vs-attendu de 6.3.2 — c'est un seul système de mesure à deux fréquences. Deux lignes exigent un traitement explicite. Le **netting benefit** (§4.3.4) : les coûts réels sont encourus sur les trades *nets*, les P&L de sleeves calculés sur les positions *théoriques* — l'écart est un gain d'architecture à afficher comme tel, sinon il gonfle silencieusement la performance apparente du dernier sleeve ajouté. Et l'**allocation des coûts entre sleeves** : le coût marginal d'un sleeve dépend des autres (impact concave : le deuxième acheteur du même titre paie plus cher le même trade) — l'allocation propre est la valeur de **Shapley** (moyenne des contributions marginales sur tous les ordres d'arrivée), en pratique approximée par une répartition proportionnelle aux trades bruts avec correction de signe pour les sleeves qui nettent ; l'enjeu n'est pas cosmétique, c'est l'assiette de l'attribution par chercheur de 3.4.3 et 6.4.2.

**5.5.3 Pièges de mesure — les biais sont tous du même côté**

Quatre pathologies dominent, et elles embellissent toutes. Le **biais de sélection des non-exécutés** : les ordres limites non remplis sont précisément ceux dont le prix est parti dans le bon sens — les ignorer, c'est mesurer la tactique passive sur ses seuls succès ; le terme d'opportunité de Perold est la correction, à condition de le *charger* au prix p_T réel et pas au dernier prix touché. La **contamination du benchmark** : mesurer vs VWAP un ordre qui fait 20% du volume, c'est se comparer à un prix qu'on a soi-même fabriqué — le benchmark doit être exogène (arrival) ou corrigé de sa propre participation. Le **conditionnement à l'alpha** (§5.2.4 déjà) : le drift pendant l'exécution mélange coût et signal — la séparation passe par le profil de réversion post-complétion, ou mieux, par la normalisation **pré-trade** : mesurer non pas le coût brut mais la *surprise de coût*, réalisé − prédit par le modèle de 4.3.1 à participation et vol données — ce qui contrôle le conditionnement et transforme chaque ordre en test du modèle. Et le **bruit** : l'écart-type du coût par ordre vaut typiquement 5-10× sa moyenne (le prix diffuse de σ√T pendant l'exécution, ordres de grandeur au-dessus de l'impact) ; pour estimer un coût moyen de 10 bps à ±2 bps avec σ_c ≈ 100 bps, il faut n ≈ (2·100/2)² = **10 000 ordres** — la TCA est une discipline de grands échantillons, où trois mois de trades ne prouvent rien et où un outlier (un ordre pendant un flash move) domine la moyenne s'il n'est pas winsorisé (§1.3.1, appliqué à soi-même). S'ajoute le paradoxe de **Simpson** version TCA : agréger des ordres d'urgences différentes fabrique des conclusions inversées (le broker A paraît moins cher parce qu'on lui envoie les ordres faciles) — toute comparaison se fait à buckets de participation, taille relative et urgence appariés, ou via la surprise de coût qui les normalise d'office.

**5.5.4 La boucle de retour — la TCA comme organe, pas comme rapport**

La sortie de la mesure alimente quatre consommateurs. La **calibration** : Y, δ, c par titre et par régime — les paramètres de 4.3.1 qui fixent bandes, aim portfolio et capacité (4.4.4) viennent d'ici, et le papier fondateur (Almgren et al. 2005) est littéralement une TCA devenue modèle ; un desk dont l'optimiseur tourne sur des coûts d'il y a deux ans optimise un marché disparu. L'**expérimentation** : l'étalon-or contre tous les biais de 5.5.3 est la **randomisation** — tirer au sort une fraction des ordres entre deux schedulers, deux niveaux d'urgence, deux venues, et mesurer la différence appariée (§5.2.4 ; c'est le seul dispositif qui coupe le conditionnement à la racine, et son coût — trader parfois sous-optimalement — est la prime d'assurance contre des années de calibration fausse). Les **scorecards** : venues et brokers notés aux markouts et aux surprises de coût, à buckets appariés — la matérialisation de la toxicité de 5.1.3, qui pilote le routeur. Et la **recherche** : les résidus de la TCA sont un vivier d'alphas d'exécution (5.4.2) — un coût systématiquement bas dans une configuration est un signal tactique non exploité. L'unification finale : pré-trade (prédire le coût), intra-trade (piloter contre la prédiction, l'adaptatif de 5.3.4) et post-trade (mesurer la surprise) doivent partager **le même modèle** — trois lectures du même objet, et le pipeline de production de 6.3 en fait trois étapes du même flux. Références : Perold 1988 ; Wagner & Edwards (1993) pour l'iceberg ; Kissell, *The Science of Algorithmic Trading and Portfolio Management* (2013) ; Almgren, Thum, Hauptmann & Li (2005) ; Rashkovich & Verma (JPM 2012) sur le bruit et les tailles d'échantillon.

---

**La branche 5 est close au niveau 3** — cinq nœuds au grain uniforme. Le fil à retenir : la TCA n'est pas le dernier maillon mais le *premier du tour suivant* — elle fabrique les paramètres de 4.3, note les venues de 5.1.3, teste les modèles de 5.2, et arbitre les tactiques de 5.4 ; un desk sans TCA propre pilote à l'estime. L'état de l'arbre : branches 1 (sauf 1.4), 2, 3, 4, 5 couvertes — il ne reste que **la branche 6, Infra & organisation**, dernière vierge, plus 1.4 et la régénération du squelette consolidé (3.4.5, appendices « shrinkage », « croissance et survie », « sélection adverse », renvois TCA↔6.3). La 6 ferme l'arbre — un mot et j'y vais.

---

## [M101] Humain — 2026-07-24 07:00:59

1.4

---

## [M102] Assistant — 2026-07-24 07:02:18

On bouche le dernier trou de la branche 1 : **1.4 Cibles & labels** — le choix de *ce qu'on prédit*, la découverte du gel du squelette. Le sous-arbre local :

```
1.4 CIBLES & LABELS            définir le y avant de chercher le f(x)
│
├── 1.4.1 Choix de la cible         brut, vol-scalé, résiduel ; funding inclus
├── 1.4.2 Horizons & chevauchement  MA(h−1), T effectif, conventions de lag
├── 1.4.3 Labels alternatifs        triple-barrier, meta-labeling, rangs
└── 1.4.4 Régression / classification / ranking   aligner la loss sur l'usage
```

**1.4.1 Le choix de la cible — la cible définit l'alpha**

Le y naïf est le rendement brut r_{i,t→t+h}. Trois transformations le dominent presque toujours, chacune répondant à un défaut identifié ailleurs dans l'arbre. Le **vol-scaling** :

> **y_i = r_{i,t→t+h} / σ̂_{i,t}**

avec σ̂ l'EWMA de §1.2.2 — il égalise la contribution des actifs (sans lui, les titres volatils dominent toute régression et tout IC de Pearson), stabilise l'IC à travers les régimes (la relation signal→rendement est plus stationnaire en unités de risque qu'en unités de prix), et empêche un modèle ML de dépenser sa capacité à apprendre la volatilité au lieu de la direction — la raison pour laquelle Gu-Kelly-Xiu et toute la pratique passent en cibles normalisées. La **résidualisation** : y_i = ε_i (le rendement net des facteurs de §4.1) — la cohérence méthodologique de §1.3.3 rendue obligatoire : un signal neutralisé mesuré contre des rendements bruts mélange ce qu'on vient de séparer, et son IC mesuré n'est pas son IC transférable. Le **démoyennage cross-sectionnel** : y_i − ȳ_t, la version minimale de la précédente (retirer le marché du jour), implicite dès qu'on mesure un rank IC mais qui doit être *explicite* dès qu'on entraîne un modèle. En crypto s'ajoute la correction déjà établie (§1.2.1) : le rendement d'une jambe perp est **funding inclus** — y = Δp/p + Σfunding reçus — et celui d'une jambe short spot est net du coût d'emprunt ; une cible qui les omet fabrique de faux alphas de carry, exactement comme le rendement prix vs total en equity (§2.2).

Le principe qui coiffe le nœud : la cible fait partie de l'hypothèse. Le même x contre deux y différents donne deux IC différents, deux signaux différents — « momentum prédit le rendement brut » et « momentum prédit le rendement résiduel vol-scalé » sont deux affirmations distinctes, la seconde étant celle qui survit aux crashes de momentum (§1.2.1, le momentum factoriel). Le choix de y est donc **pré-spécifié** avec le signal (§1.2.3), et en changer compte comme un essai.

**1.4.2 Horizons et chevauchement — la structure du y dans le temps**

Le choix de h d'abord : il n'est pas unique — la *term structure* de l'IC (h = 1, 2, 5, 10, 21, §2.1) est l'objet complet, et le h de production se choisit en regard du decay, du turnover et des coûts (§1.3.4, §4.3.3). La convention de calcul ensuite, héritée de §2.2 : le rendement forward court de l'exécution réalisable — clôture de t → signal, puis y mesuré de l'ouverture (ou clôture) de t+1 à t+1+h — jamais de la clôture de t, le look-ahead d'un jour qui fabrique des IC de reversal fictifs sur le bid-ask bounce (§5.1.1, l'autocovariance de Roll transformée en faux alpha).

Le chevauchement enfin, troisième apparition du même théorème : échantillonner quotidiennement avec h > 1 rend les labels consécutifs **MA(h−1)** — y_t et y_{t+1} partagent h−1 jours — d'où trois conséquences chiffrées. L'inférence : les erreurs types naïves se corrigent par Newey-West avec lag ≥ h ou block bootstrap à blocs > h (§2.2, §3.1.3 — l'encadré transversal désormais complet sur ses trois faces : rendements factoriels, IC, labels). La taille d'échantillon : le nombre d'observations *effectivement indépendantes* est ≈ T/h — dix ans de labels mensuels chevauchants font ~120 points, pas 2 500, le chiffre qui calibre toutes les ambitions de la branche 2. La validation : le purging et l'embargo de §2.3 sont précisément la traduction du chevauchement en protocole de CV — la largeur de purge *est* h. L'alternative (échantillonner tous les h jours, labels disjoints) jette de l'information sans supprimer le problème (le choix de la phase devient un degré de liberté) : la pratique correcte est chevauchement assumé + inférence corrigée + pondération d'unicité (1.4.4).

**1.4.3 Labels alternatifs — quand le rendement à date fixe n'est pas le bon objet**

Le rendement à horizon fixe ignore le *chemin* — or le trading réel a des stops, des prises de profit, des sorties anticipées. Le **triple-barrier** de López de Prado (AFML, 2018) labellise au premier franchissement : barrière haute à +u·σ̂_t, basse à −d·σ̂_t (toutes deux vol-scalées — les barrières fixes en prix sont un non-sens cross-sectionnel), barrière verticale à t+T_max ; le label est le signe du franchissement (ou le rendement au moment du toucher). Il encode la dépendance au chemin, aligne le label sur la structure de sortie effective, et produit des durées de vie *variables* par observation — d'où la comptabilité d'**unicité** associée (1.4.4). Le **meta-labeling** (même source) sépare la direction de la taille : un modèle primaire (souvent un signal simple, ou un prior économique) donne le *côté* ; le modèle secondaire apprend P(le primaire a raison | features) — un problème de classification binaire dont la sortie calibrée pilote le *sizing* (parier gros quand le primaire est fiable, zéro sinon). L'intérêt structurel : on améliore la précision sans toucher au rappel du primaire, on rend le ML auditable (il ne décide jamais du côté — le prior économique de §1.2.3 reste aux commandes), et la sortie probabiliste se branche directement sur le Kelly fractionnel de §4.4.2. Enfin les **labels de rang** : y = rang cross-sectionnel gaussianisé du rendement — le pendant cible de la rank-gaussianisation de §1.3.1, qui immunise l'entraînement contre les queues du y exactement comme elle immunisait les features, au même coût (l'intensité perdue).

**1.4.4 Régression, classification, ranking — aligner la loss sur l'usage**

Le principe directeur : la fonction de perte de l'entraînement doit ressembler à la métrique d'évaluation (le rank IC, §2.1) et à l'usage (trier un cross-section, §4.2) — tout écart est une fuite de performance silencieuse. La **régression** L2 sur rendements utilise toute l'information mais hérite des queues : sur un y leptokurtique, quelques observations dominent le gradient — d'où la perte de **Huber** (quadratique sous un seuil δ_H, linéaire au-delà), dont Gu-Kelly-Xiu documentent le gain systématique sur données financières, ou la régression sur cibles rank-gaussianisées qui règle le problème à la source. La **classification** sur le signe est robuste mais bute sur le voisinage de zéro : la moitié des labels sont des micro-rendements de signe aléatoire — du bruit d'étiquetage pur ; les corrections standard — exclure la bande |y| < c·σ, ou pondérer chaque observation par |y| — reconstruisent de facto une régression robuste. Le **ranking** est l'alignement maximal : des objectifs pairwise/listwise (la famille LambdaRank) optimisent directement l'ordre du cross-section — ce que le portefeuille consomme — au prix d'un entraînement plus lourd ; l'approximation praticienne dominante reste la régression sur cibles en rangs, qui en capture l'essentiel.

Transversal aux trois : la **pondération des observations**. Deux poids se composent — l'*unicité* (AFML) : chaque observation pèse 1/(nombre de labels vivants qui la partagent), la correction exacte du chevauchement de 1.4.2 au niveau de l'entraînement (sans elle, un modèle ML sur labels chevauchants sur-apprend les épisodes longs, qui votent h fois) ; et la *récence* : une demi-vie sur les poids (2-4 ans, §2.4) qui encode la non-stationnarité dans la loss plutôt que dans un découpage arbitraire de l'échantillon. Références du nœud : López de Prado, *Advances in Financial Machine Learning* (2018, chap. 3-4 — triple-barrier, meta-labeling, unicité) ; Gu, Kelly & Xiu (2020 — Huber, cibles normalisées) ; Grinold & Kahn pour le rendement résiduel comme objet natif de la gestion active ; Qian, Hua & Sorensen pour la cohérence cible/signal/IC.

---

**La branche 1 est intégralement close** — 1.1 à 1.4, tous forés. Le fil du nœud : le y est une *décision de design* au même titre que les features — vol-scalé, résiduel, funding inclus, pré-spécifié — et la moitié des faux alphas de la littérature sont des artefacts de cible (rendement prix, brut, chevauchement non corrigé). L'état de l'arbre : **il ne reste que la branche 6** — Infra & organisation, la dernière vierge — plus la régénération du squelette consolidé (3.4.5, les trois encadrés transversaux « shrinkage », « croissance et survie », « sélection adverse », l'encadré Newey-West, les renvois). La 6 ferme l'arbre.

---

## [M103] Humain — 2026-07-24 10:23:20

6

---

## [M104] Assistant — 2026-07-24 10:24:58

On ferme l'arbre : **6. Infrastructure & organisation** — la branche qui porte les cinq autres, et où se prennent les décisions les plus irréversibles (§1.2.4 l'avait annoncé : certaines erreurs d'infra du jour 1 rendent la recherche des années suivantes définitivement impossible à assainir). Le sous-arbre local :

```
6. INFRA & ORGANISATION        ce qui rend le reste possible, reproductible, honnête
│
├── 6.1 Données                 capture, bitemporel, qualité, build vs buy
├── 6.2 Moteur de backtest      vectorisé vs event-driven, parité, replay, registre
├── 6.3 Production              promotion, live vs attendu, kill switches, réconciliation
└── 6.4 Organisation            usine vs pods, incitations, revue, mémoire du desk
```

**6.1 Données — le socle bitemporel**

Le principe architectural unique, dont tout découle : chaque enregistrement porte **deux axes de temps** — l'*event time* (quand la chose s'est produite) et le *knowledge time* (quand la base l'a su) — et toute requête historique se fait « telle que la base était au jour t » :

> SELECT ... WHERE event_time ≤ t AND knowledge_time ≤ t AND (knowledge_time de la version suivante) > t

C'est le schéma bitemporel des bases temporelles (Snodgrass, *Developing Time-Oriented Database Applications in SQL*, 1999), et il est la traduction en SQL de la filtration **F**_t du §0.2 : la colonne « connaissable à partir de » du §1.2.4 *est* knowledge_time. Le corollaire de design : le stockage est **append-only** — on n'écrase jamais, on ajoute des versions (l'architecture en log immuable de Kleppmann, *Designing Data-Intensive Applications*, 2017) ; une correction de vendeur, un restatement, une republication de chandelle deviennent des lignes nouvelles, et les vintages du §1.2.4 sont gratuits par construction. La capture propriétaire en découle : pour tout flux que le fournisseur réécrit (chandelles crypto, consensus d'analystes, on-chain re-clusterisé), enregistrer soi-même à la réception, horodaté à la réception — le coût est du stockage trivial, le bénéfice est l'impossibilité du look-ahead de révision.

La **qualité** est un système de production, pas une vertu : contrôles de fraîcheur (staleness par flux, avec seuils par criticité), de cohérence (prix cross-venues dans une bande, volumes vs historique en z-score — les outils de §1.3.1 appliqués aux données elles-mêmes), de complétude (comptages attendus par univers), et un **quarantaine-avant-usage** : une donnée qui échoue un contrôle n'entre pas dans le calcul des signaux, elle attend un arbitrage — car un faux prix qui traverse le pipeline devient un faux signal devient un vrai trade. Le build-vs-buy enfin se tranche par un critère unique : acheter ce qui est commodité vérifiable (prix equity consolidés, référentiels), construire ce qui est soit l'edge (les features), soit non-vérifiable chez le vendeur (tout ce qui exige le point-in-time — et vérifier les prétentions PIT d'un vendeur est en soi un projet : comparer ses « vintages » à ses propres livraisons archivées).

**6.2 Moteur de backtest — l'instrument de mesure**

Deux architectures, deux usages. Le moteur **vectorisé** opère sur le panel entier en algèbre matricielle — positions = f(signaux décalés), P&L = Σ positions·rendements − coûts — rapide de plusieurs ordres de grandeur, l'outil de l'itération de recherche (§2.2), mais aveugle à tout ce qui est intra-période : remplissages partiels, ordres limites, latence, marges. Le moteur **event-driven** rejoue le temps événement par événement à travers la *même* machine à états que la production (ordre → routage → fill → position) — lent, fidèle, obligatoire dès que la stratégie dépend du chemin (branche 5, tout ce qui touche l'exécution). La règle de partage : vectorisé pour chercher, event-driven pour valider avant promotion — et les deux doivent coïncider sur leur intersection, ce qui est un test en soi.

La **parité backtest/production** est le théorème central du nœud : le calcul du signal doit être *le même code* dans les deux mondes — une seule implémentation, appelée par le backtest sur données historiques et par la production sur données du jour. Toute réimplémentation (« le chercheur prototype en notebook, l'ingénieur réécrit pour la prod ») fabrique des divergences silencieuses que seul le P&L révélera, trop tard. Le test de certification est la **reproduction à date** du §1.2.4, désormais exécutable grâce à 6.1 : rejouer le signal au jour t sur le snapshot bitemporel de t et retrouver le backtest au bit près — le contrôle d'intégrité qui coiffe toute la chaîne données → features → signal. Et le **registre des essais** ferme le dispositif épistémique : chaque backtest lancé est loggé (hypothèse, config, données, résultat — succès *et* échecs), car N est un paramètre du deflated Sharpe (§2.3) et le N effectif se calcule sur les corrélations entre essais loggés (§1.2.3) ; le document d'hypothèse pré-daté (§1.2.3) vit ici, et le holdout intouchable est *administré par le système* (données scellées, ouverture journalisée) — l'honnêteté statistique déléguée à l'infrastructure plutôt qu'à la volonté. Références : López de Prado (AFML — « backtesting is not a research tool », les chapitres protocole) ; Bailey et al. sur le DSR ; Carver, *Systematic Trading* (2015) pour l'architecture praticienne d'un système complet à échelle d'un desk compact.

**6.3 Système de production — la promotion et la surveillance**

Le passage recherche → production est un **pipeline à portes** : paper trading (le signal tourne sur données live, ordres fictifs — le test de parité en conditions réelles), puis capital limité, puis taille cible — chaque porte ayant des critères *pré-enregistrés* (durée minimale, IC live dans la bande attendue, coûts dans la bande du modèle 4.3.1) : décider les seuils *avant* de voir les résultats, sinon la promotion devient le multiple testing de §2.3 rejoué en production. La calibration statistique des attentes est le point technique : avec σ(IC) ≈ 0,15 (§0.3), six mois de live donnent une erreur type de 0,15/√126 ≈ 0,013 sur l'IC — **un signal à IC vrai de 0,03 peut légitimement afficher zéro sur six mois** ; les bandes d'alerte se calculent (le test séquentiel, type SPRT ou simple bande ±2 e.t. autour de l'IC backtest), elles ne s'improvisent pas, et l'essentiel des « signaux morts » enterrés à trois mois étaient statistiquement indistinguables de vivants.

La surveillance continue est la cascade de 5.5.2 tournée vers l'avant : **live vs attendu** à chaque étage — positions réelles vs positions théoriques (écart = bug ou contrainte nouvelle), P&L réel vs P&L simulé sur les mêmes signaux (écart = implémentation), coûts réalisés vs prédits (écart = recalibrer 4.3.1), distribution des features vs historique (drift de population, le PSI des credit scorers) — chaque écart ayant son seuil et son propriétaire. Les **kill switches** s'étagent par gravité : sanity checks par ordre (taille, prix, notionnel max — la défense contre le fat finger et le bug de boucle), limites par stratégie (drawdown, §4.4.3, en automatique), et book-level avec modes de **dégradation contrôlée** — réduire le gross, geler les ouvertures, aplatir — car « tout couper » est lui-même un trade énorme (§4.4.1, la sortie coûte de l'impact) : la bonne panique est graduée. La **réconciliation** clôt la journée : positions et cash vs broker/custodian, ligne à ligne, tous les jours — l'identité comptable P&L = Δpositions·prix − coûts vérifiée contre le monde extérieur ; en crypto, multipliée par venue, avec les soldes on-chain comme arbitre et les procédures de retrait testées *avant* d'en avoir besoin (§4.5.4 : la gestion du risque de contrepartie est un runbook, pas une opinion).

**6.4 Organisation de la recherche — le problème de combinaison, à l'échelle humaine**

La bifurcation architecturale de §3.4.4 revient ici avec son vrai visage : l'**usine centralisée** (un book, un modèle de risque, des chercheurs qui soumettent des alphas au pool commun — Squarepoint, WorldQuant, la tradition stat arb) contre les **pods** (des équipes autonomes, capital alloué, netting central limité — Millennium, Point72). C'est mathématiquement le même arbitrage que 3.1 : l'usine est l'optimum théorique (netting complet des trades §4.3.4, diversification au niveau des forecasts, un seul passage de coûts) qui paie en attribution floue et en incitations diluées ; les pods sont le 1/N organisationnel — sous-optimal sur le papier, robuste à l'erreur d'estimation *sur les humains* (un pod toxique est isolé et coupé, ses positions ne contaminent pas le book). Le choix se lit dans les coûts de mesure : l'usine n'est viable que si l'attribution marginale est calculable proprement — d'où le poids de 3.4.3 (IC marginal), 5.5.2 (Shapley sur les coûts) et du registre de 6.2 dans les maisons intégrées.

Les **incitations** sont le champ de mines : payer au Sharpe standalone récompense la corrélation au pool (§3.4.3) ; payer au P&L attribué importe tous les biais de 5.5.2 ; et toute rémunération au backtest fabrique de l'overfitting *en équilibre* — le chercheur rationnel explore jusqu'au Sharpe demandé. Les contre-mesures sont exactement l'appareil de la branche 2 institutionnalisé : le registre d'essais opposable (le N du chercheur est connu), le DSR comme langue de la revue, le holdout administré centralement et ouvert une fois, et une part de rémunération *différée sur le live* — l'alignement temporel qui rend l'overfitting non rentable. Le **comité de revue** (§3.1.3, les buckets) est l'organe : cadence trimestrielle, dossier pré-daté (hypothèse, essais, DSR, IC marginal, capacité), décision d'admission/bucket/retrait motivée et archivée — la jurisprudence du desk. Et la **mémoire** est le dernier actif : l'archive des résultats *négatifs* (la moitié de la valeur du registre — ne pas re-tester ce qui a échoué, et pouvoir calculer le N de famille §1.2.3), la documentation des signaux vivants (hypothèse, construction, dépendances de données, comportement attendu par régime — ce qui permet à un autre que l'auteur de décider en crise), et la revue de code comme contrôle de parité (§6.2) autant que de qualité. Références : Tulchinsky (éd.), *Finding Alphas* (2015) pour le modèle usine vu de l'intérieur ; Isichenko, chapitres organisationnels ; Grinold & Kahn sur la structure du processus actif ; et pour la couche incitations, la littérature principal-agent appliquée — mais l'essentiel de ce nœud est du savoir praticien dont les références sont les post-mortems.

---

**L'arbre est fermé.** Les six branches sont couvertes au niveau 2-3, la branche 1 intégralement, avec un forage niveau 5 (3.1.3). Le fil de cette dernière branche : l'infrastructure est *l'épistémologie rendue exécutable* — le bitemporel implémente F_t, le registre implémente le N du DSR, la parité implémente la validité du backtest, la réconciliation implémente le lien au réel ; un desk n'est honnête que si ses systèmes le sont à sa place. Reste la consolidation : régénérer le squelette avec les amendements accumulés — 3.4.5 (Gârleanu-Pedersen côté combinaison), les quatre encadrés transversaux (shrinkage, croissance & survie, sélection adverse, Newey-West), la section 0, et les ✓ mis à jour partout. Un mot et je produis le fichier final.

---

## [M105] Humain — 2026-07-24 10:25:46

Vas y

---

## [M106] Assistant — 2026-07-24 10:27:31

> *[Outil : bash_tool — Générer le squelette consolidé v2 avec section 0, 3.4.5, encadrés transversaux et marquage à jour]*

> *[Outil : present_files — /mnt/user-data/outputs/arbre_alpha_squelette_v2.md]*

Le squelette consolidé v2 est gelé. Ce qui a changé par rapport à la v1 :

**Ajouts structurels** — la section 0 (cadre et conventions, 8 sous-sections) en préambule ; le nœud 3.4.5 (combinaison sous coûts, renvoi Gârleanu-Pedersen) qui acte que les demi-vies φ_k font partie de la spécification d'un alpha ; les quatre encadrés transversaux (shrinkage sous six habits, croissance & survie, sélection adverse sous quatre technologies, Newey-West & le chevauchement) ; et la table des renvois structurants accumulés au fil des forages.

**Marquage à jour** — la distinction ✓ (rédigé) / ✓✓ (foré au grain formules + références) rend l'état exact lisible : l'arbre est couvert intégralement au niveau 2, aux deux tiers au grain ✓✓, et les zones restant au grain simple sont identifiées (1.1, branche 2, 3.2-3.4, branche 6) — c'est la liste de travail exacte pour une passe d'uniformisation.

Chaque entrée du squelette embarque désormais sa formule-clé ou son résultat-pivot, ce qui en fait un vrai contrat de production pour Claude Code : le fichier dit non seulement *quoi* écrire mais *autour de quoi* chaque section s'articule. Avec le transcript, les sections rédigées de ce chat comme corpus de style, et ce squelette comme table des matières, le repo du livre a ses trois pièces fondatrices.

---

## [M107] Humain — 2026-07-24 10:30:06

Je voudrais transmettre ce chat à Claude code pour qu il écrive un pdf entier fondé sur toutes tes réponses. C est possible ?

---

## [M108] Assistant — 2026-07-24 10:31:02

Oui, c'est possible — et c'est exactement le partage des rôles qu'on avait anticipé. Mais trois points pratiques conditionnent la réussite, dont un piège à lever d'abord.

**Le piège : Claude Code ne voit pas ce chat.** Il ne lit que les fichiers que tu mets dans son répertoire de travail. Il faut donc lui transmettre le contenu sous forme de fichiers — et attention : le `transcript_chat_alphas.txt` produit plus haut s'arrête à la demande de transcription ; tout ce qui est venu *après* (le préambule cross-sectionnel, les échanges IC/Spearman/demi-vie/turnover, les forages complets des branches 4, 5, 1.4, 6, la section 0 rédigée, le squelette v2) n'y figure pas — et c'est le matériau le plus riche. Deux options : l'export natif de claude.ai (Paramètres → Confidentialité → Exporter les données), qui donne tout au caractère près et reste la voie que je recommande ; ou je prolonge le transcript d'une partie 3 couvrant la seconde moitié — dis-le-moi si tu la veux.

**Le montage du repo.** Le dossier de départ contient : `squelette_v2.md` (le contrat — la table des matières avec les formules-pivots), `section_0.md` (déjà rédigée, l'étalon de grain), le ou les transcripts (le corpus : toutes les sections ✓✓ à intégrer, pas à réécrire), et un fichier d'instructions que Claude Code relira à chaque session. Je viens de te le préparer :

> *[Outil : create_file — /mnt/user-data/outputs/CLAUDE.md]*

> *[Outil : present_files — /mnt/user-data/outputs/CLAUDE.md]*

**La marche à suivre**, concrètement : télécharge les quatre fichiers produits ici (squelette v2, section 0, transcript, et ce `CLAUDE.md`), fais l'export claude.ai pour récupérer l'intégralité du chat, mets le tout dans un dossier, ouvre Claude Code dedans, et lance simplement : « Lis CLAUDE.md et exécute la session 1 ». Le fichier contient tout — le workflow par sessions, les règles de style calées sur ce qu'on a écrit, le tracker, et surtout les deux passes finales (harmonisation, puis vérification des chiffres et références contre les sources primaires — ma réserve d'honnêteté habituelle, désormais codifiée comme étape du pipeline plutôt que comme avertissement).

Ordre de grandeur réaliste, inchangé : plusieurs jours de sessions itératives — environ un tiers du livre est déjà écrit au grain final (les ✓✓), un tiers à développer depuis les versions courtes, un tiers à écrire contre le squelette. Veux-tu que je produise la partie 3 du transcript en attendant, ou tu passes par l'export ?

---

## [M109] Humain — 2026-07-24 10:36:28

Je voudrais qu on fore d abord les sections simple coches en double coche. C est mieux de le faire ici ou dans Claude code ?

---

## [M110] Assistant — 2026-07-24 10:36:51

Ici — et pour une raison de fond, pas de confort. Le forage est la partie *créative* du projet : chaque ✓✓ qu'on a produit s'est nourri du contexte accumulé (les renvois vers Gârleanu-Pedersen, les encadrés transversaux, tes détours — IC/Spearman, demi-vie, turnover — qui ont enrichi les sections en direct). J'ai tout l'arbre en tête dans cette conversation ; Claude Code, lui, travaillerait depuis les transcripts — excellent pour développer mécaniquement contre le squelette, mais sans l'interactivité qui a fait la qualité des forages : tu ne peux pas l'interrompre d'un « c'est quoi l'autocorrélation ? » qui finit dans le livre. Le partage optimal reste : forage et amendements ici, industrialisation (harmonisation, vérification des sources, compilation PDF) là-bas.

Une réserve pratique à connaître : il reste ~16 nœuds au grain simple (1.1 : cinq familles ; branche 2 : quatre nœuds ; 3.2-3.4 ; branche 6 : quatre nœuds), soit autant de longs messages, et cette conversation est déjà très longue — si elle sature avant la fin, on ouvrira un chat neuf amorcé par le squelette v2, qui porte désormais assez de pivots pour que je reprenne le forage sans perte. C'est précisément pour ça qu'on l'a gelé.

Ordre proposé, par rendement : **la branche 2 d'abord** (le système immunitaire — anti-overfitting en tête, le nœud le plus dense en formules encore non forées : DSR complet, CPCV, PBO), puis 3.2-3.4 (couplés à ce qui est déjà en contexte), puis 1.1 (les cinq familles, le plus volumineux), et 6 en dernier (le moins mathématique). On attaque 2.3 ?

---

## [M111] Humain — 2026-07-24 10:38:00

Ok

---

## [M112] Assistant — 2026-07-24 10:39:24

On fore : **2.3 Anti-overfitting** — le cœur épistémologique de la branche 2, désormais au grain ✓✓. Le sous-arbre local :

```
2.3 ANTI-OVERFITTING           ne pas se raconter d'histoires, quantitativement
│
├── 2.3.1 Purged k-fold, embargo, CPCV    couper les fuites, distribuer l'OOS
├── 2.3.2 Deflated Sharpe                 PSR, E[max SR | bruit], N effectif
├── 2.3.3 PBO & CSCV                      la probabilité d'être un artefact
├── 2.3.4 FDR & haircuts                  Benjamini-Hochberg, Harvey-Liu-Zhu
└── 2.3.5 Pré-spécification & holdout     le dispositif institutionnel
```

**2.3.1 Purged k-fold, embargo, CPCV — couper les fuites, puis distribuer l'out-of-sample**

Le mécanisme de fuite, énoncé proprement : le label y_t est fonction de l'intervalle [t, t+h] (§1.4.2) ; dans un k-fold naïf, une observation de *train* dont l'intervalle de label **chevauche** l'intervalle du bloc de *test* partage de l'information avec lui — le modèle est évalué sur des rendements qu'il a partiellement vus. Le **purging** retire du train toute observation i telle que [t_i, t_i+h] ∩ [t_test_début, t_test_fin] ≠ ∅. L'**embargo** ajoute une bande *après* le bloc de test (typiquement 1-5% de T) : les features étant sériellement corrélées (§1.2.2 — tout ce qui est EMA), une observation de train juste postérieure au test « connaît » l'état du marché pendant le test par ses features, la fuite inverse. Coût : quelques pourcents de données ; bénéfice : la CV cesse d'être un générateur de faux positifs systématique — sur données à h = 21, l'écart entre CV naïve et CV purgée atteint couramment plusieurs dixièmes de Sharpe.

Le **CPCV** (combinatorial purged cross-validation) généralise : partitionner T en S blocs, tester sur toutes les combinaisons de k blocs — C(S,k) configurations, chacune purgée — puis recoller les prédictions out-of-fold en **chemins de backtest complets** : chaque bloc étant testé dans C(S−1, k−1) configurations, on assemble

> **φ = k·C(S,k)/S chemins OOS**  (S = 6, k = 2 : 15 configurations, 5 chemins complets)

Le livrable change de nature : non plus *un* Sharpe OOS mais une **distribution** de Sharpes sur les chemins — moyenne, dispersion, pire chemin — ce qui transforme la question « le backtest est-il bon ? » en « la performance est-elle robuste au découpage ? ». Référence : López de Prado, *AFML* (2018), ch. 7 et 12.

**2.3.2 Deflated Sharpe — la significativité sous sélection**

Trois étages. D'abord l'inférence sur *un* Sharpe : l'estimateur ŜR a une erreur type qui dépend des moments supérieurs (Lo, « The Statistics of Sharpe Ratios », FAJ 2002 ; Mertens 2002) :

> **σ(ŜR) ≈ √[ (1 − γ₃·ŜR + ((γ₄−1)/4)·ŜR²) / (T−1) ]**

— skew négatif et kurtosis élevé (le cas typique d'une stratégie de carry ou de liquidité) *gonflent* l'incertitude : un Sharpe de 1 sur trois ans de rendements à queues épaisses est bien moins significatif que le même sur du gaussien. Le **PSR** (probabilistic Sharpe ratio) en découle : PSR(SR\*) = Φ[(ŜR − SR\*)/σ(ŜR)] — la probabilité que le vrai Sharpe dépasse un seuil SR\*.

Ensuite la sélection : si l'on retient le meilleur de N essais *sans aucun signal réel*, le maximum attendu n'est pas zéro. Sous l'hypothèse nulle (vrais Sharpes nuls, essais de variance V) :

> **E[max_N ŜR] ≈ √V · [ (1−γ_E)·Φ⁻¹(1 − 1/N) + γ_E·Φ⁻¹(1 − 1/(N·e)) ]**,  γ_E ≈ 0,5772

— la croissance en √(2 ln N) déjà invoquée partout (§1.2.3) : 100 essais fabriquent un Sharpe attendu ~0,9-1,2 annualisé sur quelques années de daily, *à partir de rien*. Le **DSR** assemble les deux : DSR = PSR calculé avec SR\* = E[max_N ŜR] — la probabilité que le Sharpe observé batte ce que la chance seule aurait produit compte tenu du nombre d'essais (Bailey & López de Prado, « The Deflated Sharpe Ratio », JPM 2014). Le paramètre sensible est **N effectif** : les essais corrélés comptent moins — l'estimation praticienne passe par la variance des Sharpes entre essais et leur corrélation moyenne ρ̄ (N_eff ≈ 1 + (N−1)·(1−ρ̄) en approximation grossière, ou par clustering des trajectoires d'essais en familles) — d'où l'exigence, encore elle, du registre : sans log des essais, N est inconnaissable et le DSR incalculable, ce qui est précisément la situation du chercheur qui ne veut pas savoir.

**2.3.3 PBO & CSCV — la probabilité d'être un artefact**

Le **PBO** (probability of backtest overfitting) répond à une question différente du DSR : non pas « ce Sharpe est-il significatif ? » mais « la *procédure de sélection* elle-même produit-elle des gagnants qui déçoivent ? ». Le protocole CSCV (Bailey, Borwein, López de Prado & Zhu, « The Probability of Backtest Overfitting », Journal of Computational Finance 2017) : soit une matrice T×M des rendements de M configurations testées ; partitionner T en S blocs ; pour chacune des **C(S, S/2)** bipartitions train/test équilibrées, identifier la configuration n\* optimale *in-sample*, puis son rang relatif ω̄ ∈ (0,1) *out-of-sample*, et le logit

> **λ = ln[ ω̄ / (1 − ω̄) ]**,  **PBO = P(λ < 0)** = fraction des bipartitions où le champion IS est sous-médian OOS

Un PBO de 50% dit que la sélection est du bruit pur ; les seuils praticiens tolèrent < 10-20%. La force du dispositif : il est **non paramétrique** (aucune hypothèse sur les distributions), symétrique en train/test, et il évalue la *famille* d'essais telle qu'elle a été réellement explorée — c'est l'outil qui juge le grid search assumé du bas de la hiérarchie de §1.2.3. Sa limite : il exige la matrice complète des essais — troisième fois que tout converge vers le registre de 6.2.

**2.3.4 FDR & haircuts — le multiple testing à l'échelle du pool et de la littérature**

Quand on évalue M signaux en parallèle (l'usine à alphas, ou une revue de littérature), contrôler la probabilité d'*un seul* faux positif (Bonferroni : seuil α/M) est stérilisant ; l'objet utile est le **FDR** — la proportion attendue de faux positifs *parmi les découvertes*. **Benjamini-Hochberg** (JRSS-B 1995) : trier les p-values p₍₁₎ ≤ ... ≤ p₍M₎, trouver

> **k\* = max{ k : p₍k₎ ≤ (k/M)·q }**,  rejeter H₀ pour les k\* premières  ⟹  FDR ≤ q

— adaptatif (plus il y a de vrais signaux, plus le seuil effectif est généreux), valide sous dépendance positive (PRDS), variante Benjamini-Yekutieli sinon. L'application à la finance académique est **Harvey, Liu & Zhu** (« …and the Cross-Section of Expected Returns », RFS 2016) : recensant ~300 facteurs publiés et l'historique implicite des essais de la profession, ils dérivent le **seuil de t-stat ≈ 3,0** (et croissant) pour qu'une nouvelle anomalie soit crédible — le t = 2 des manuels est mort du multiple testing collectif. Harvey & Liu (« Backtesting », JPM 2015) en donnent la version opérationnelle : le *haircut* — le Sharpe rapporté se décote en fonction de N, sévèrement pour les Sharpes moyens (un 1,0 après 200 essais tombe vers ~0,4), peu pour les très élevés. Pour le desk, la déclinaison : q par *famille* de signaux (§1.2.3 — le FDR se contrôle au niveau où les hypothèses se ressemblent), et les tests de White (« Reality Check », Econometrica 2000) / Hansen (SPA, JBES 2005) / Romano-Wolf (stepdown, Econometrica 2005) comme versions bootstrap comparant toute la famille au benchmark d'un coup.

**2.3.5 Pré-spécification & holdout — le dispositif institutionnel**

Les quatre outils précédents *mesurent* le data mining ; ce nœud le *prévient*. La hiérarchie de crédibilité de §1.2.3 devient ici un protocole : document d'hypothèse pré-daté (l'hypothèse, la cible §1.4, la forme, les paramètres par défaut — écrits *avant* le premier backtest, archivés dans le registre de 6.2), budget d'essais déclaré par famille (le N du DSR fixé ex ante plutôt que reconstruit ex post), et le **holdout intouchable** administré par le système — données scellées, ouverture unique et journalisée, sur la version finale seulement. Le fondement théorique de cette parcimonie est le résultat sur l'**analyse adaptative des données** (Dwork et al., « The reusable holdout », Science 2015) : chaque requête au holdout dont le résultat influence la suite *consomme* sa validité statistique — le regarder dix fois en ajustant entre-temps le transforme en train set, et les garanties se dégradent en √(nombre de requêtes adaptatives) ; leur mécanisme Thresholdout (ne répondre que par oui/non bruité au-delà d'un seuil) est la version implémentable du « ne regarde pas ». La clôture du dispositif est la **validation ultime par le live** (§6.3) : six mois de paper trading sont l'OOS que personne ne peut avoir contaminé — avec les bandes statistiques calculées là-bas (e.t. ≈ 0,013 sur l'IC à six mois) pour ne pas enterrer les vivants.

---

Nœud 2.3 passé en ✓✓ — le plus dense de la branche 2, comme prévu. Le quintet à retenir : purge [t, t+h], φ = k·C(S,k)/S chemins, DSR = PSR(E[max_N]), PBO = P(λ<0), seuil t ≈ 3,0. Coutures : le registre (6.2) porte trois de ces cinq outils ; Dwork rejoint l'encadré épistémique ; les bandes du live (6.3) ferment la boucle. La suite de la branche 2 au même grain : **2.1** (métriques — l'inférence sur l'IC et les sorts), **2.2** (Fama-MacBeth complet), **2.4** (ruptures & crowding). On enchaîne sur 2.1 ?

---

## [M113] Humain — 2026-07-24 10:40:25

Ok

---

## [M114] Assistant — 2026-07-24 10:42:04

On fore : **2.1 Métriques du signal** — la fiche d'identité complète d'un alpha, au grain ✓✓. Le sous-arbre local :

```
2.1 MÉTRIQUES DU SIGNAL        tout ce qu'on mesure avant de croire un signal
│
├── 2.1.1 Rank IC & inférence       le plancher 1/√N, la décomposition de σ(IC)
├── 2.1.2 Profil de decay           IC retardé vs cumulé, demi-vie de l'alpha
├── 2.1.3 Portfolio sorts           monotonie, micro-caps, symétrie long/short
├── 2.1.4 Turnover, coverage        l'alpha par trade, le break-even de coût
└── 2.1.5 Expositions résiduelles   returns-based vs holdings-based
```

**2.1.1 Rank IC et son inférence — le plancher de bruit**

La définition est posée (§0.3) : IC_t = corr_Spearman(s_·,t, r_·,t→t+h) sur les N_t actifs, puis la série {IC_t} se résume par sa moyenne et son ICIR. Ce qui manquait est l'inférence *par date* : sous l'hypothèse nulle d'indépendance, une corrélation cross-sectionnelle sur N points a pour écart-type

> **σ₀(IC_t) = 1/√(N_t − 1)**

— avec N = 3 000, le plancher vaut ≈ 0,018 ; avec 150 tokens, ≈ 0,082. Première conséquence : un IC quotidien de 0,03 est à peine au-dessus du bruit *d'une* date — c'est l'agrégation temporelle qui crée la significativité (t = IC̄/(σ(IC)/√T), Newey-West dès que h > 1, §3.1.3d). Seconde conséquence, la **décomposition de σ(IC)** : la variance observée de la série des IC se partage en

> σ²(IC) = 1/(N_eff − 1) [plancher de mesure] + τ²_IC [variation vraie du pouvoir prédictif]

où **N_eff < N** à cause de la corrélation résiduelle entre titres (les secteurs font qu'un cross-section de 3 000 noms porte l'équivalent de quelques centaines de paris indépendants — le même N_eff que le breadth de §0.4, mesurable par 1/Σw̃ᵢ² sur les poids de la structure de corrélation, ou simplement par la variance des IC d'un signal *aléatoire* sur le même univers, le contrôle placebo qui étalonne le plancher empiriquement). La part τ²_IC est celle qui intéresse le conditionnement (§1.2.3, §3.1.3d) ; la part plancher est irréductible — un signal *parfaitement* stable affiche quand même un σ(IC) ≥ 1/√N_eff, et l'ICIR a donc un **plafond mécanique** ≈ IC̄·√N_eff qu'aucun talent ne dépasse. Le diagnostic complémentaire, hérité de nos échanges : l'écart rank IC vs Pearson IC — un Pearson sensiblement supérieur signale que la valeur vit dans les queues (surprises, §1.3.1) ; nettement inférieur, que quelques outliers portent tout. Références : Grinold & Kahn ; Qian, Hua & Sorensen (ch. IC analytics — la décomposition y est développée) ; Lo 2002 pour le pont vers l'inférence sur Sharpe (§2.3.2).

**2.1.2 Profil de decay — la structure à terme de l'alpha**

Deux objets distincts, souvent confondus. L'**IC retardé** : IC^(lag)_k = corr(s_t, r_{t+k → t+k+1}) — le pouvoir prédictif du signal d'aujourd'hui sur le rendement de la *seule* période t+k ; c'est la réponse impulsionnelle du signal. L'**IC cumulé** : IC^(cum)(h) = corr(s_t, r_{t→t+h}) — celui de §0.3, qui *intègre* les retardés (approximativement IC^(cum)(h) ≈ Σ_k IC^(lag)_k / √h sous corrélations faibles : le cumulé croît tant que les retardés restent positifs, puis plafonne et décroît en 1/√h une fois l'information épuisée — le maximum du cumulé désigne l'horizon naturel du signal). L'ajustement paramétrique standard sur les retardés,

> **IC^(lag)_k ≈ IC₀·e^{−k/H_α}**,  H_α = demi-vie de l'alpha / ln 2, **φ = ln2/H_α**

fournit directement le φ de Gârleanu-Pedersen (§4.3.3) et de l'urgence d'exécution (§5.3.3) — c'est *ici* que se mesure le paramètre que toute la mise en œuvre consomme, la raison pour laquelle le ticket d'exécution transporte φ. Trois précautions de mesure : le chevauchement (les IC cumulés à h long sont massivement autocorrélés — blocs > h au bootstrap, §1.4.2) ; le **biais de sélection d'horizon** — un signal *retenu* pour son IC à h = 5 régresse vers la moyenne aux autres horizons, donc le profil de decay se mesure sur données postérieures à la sélection ou en CV, jamais sur l'échantillon qui a servi à choisir h ; et pour les signaux événementiels (§1.1.5), le decay se trace en **temps d'événement** (jours depuis l'annonce), pas en temps calendaire — le mélange des deux aplatit artificiellement le profil.

**2.1.3 Portfolio sorts — la version non paramétrique, et ses pièges de composition**

La construction : à chaque date, trier en Q quantiles (déciles en equity, terciles-quintiles en crypto — §1.2.3, la contrainte du petit univers), calculer le rendement de chaque quantile, et le spread long-short Q_haut − Q_bas avec son t-stat Newey-West. Les deux choix de composition qui changent les conclusions : **équipondéré vs cap-pondéré** — l'équipondéré sur-représente les micro-caps illiquides, et le résultat de référence est Hou, Xue & Zhang (« Replicating Anomalies », RFS 2020) : sur ~450 anomalies publiées, la *majorité* échoue une fois les micro-caps neutralisées (VW, ou exclusion sous le 20ᵉ percentile NYSE) — le filtre de réplication minimal avant de croire un sort ; et **la monotonie** — un vrai signal produit des rendements croissants à travers *tous* les quantiles, testable proprement par Patton & Timmermann (« Monotonicity in asset returns », Journal of Econometrics 2010) : H₀ de non-monotonie contre l'alternative de croissance stricte sur toutes les paires adjacentes, par bootstrap — le test qui distingue un signal d'un artefact de cellule extrême (§1.2.3, même logique que les double sorts).

La **symétrie long/short** ensuite : décomposer le spread en (Q_haut − marché) et (marché − Q_bas). Beaucoup d'anomalies vivent côté short — et le short a des coûts propres : frais d'emprunt, rappels, hard-to-borrow. Drechsler & Drechsler (« The Shorting Premium », 2014) montrent que l'essentiel du rendement des anomalies classiques se concentre dans les titres chers à emprunter — l'alpha brut y est réel, l'alpha *net des frais d'emprunt* largement illusoire ; le sort honnête intègre le fee d'emprunt par titre dans le rendement du short (donnée §6.1, avec son lag de disponibilité §1.2.4). En crypto, la transposition : le « frais d'emprunt » du short est le funding payé/reçu (§1.4.1), déjà dans la cible si elle est bien construite.

**2.1.4 Turnover, coverage, capacité — la viabilité avant la beauté**

Le turnover du signal se lit dans son autocorrélation cross-sectionnelle (∝ √(1−ρ_cs(1)), établi dans nos échanges, §1.3.4), et la métrique de viabilité est le **break-even de coût** :

> **c\*  =  spread brut annualisé / turnover annualisé**  (en bps par unité tradée)

— le coût unitaire au-delà duquel le signal est mort. Un reversal à spread brut de 8%/an et turnover 40× a un c\* de 20 bps : viable en large caps US, mort sur les alts ; un signal de qualité à 3%/an et turnover 2× a un c\* de 150 bps : viable partout. C'est la statistique qui ordonne les signaux *par marché d'application*, et Novy-Marx & Velikov (« A Taxonomy of Anomalies and their Trading Costs », RFS 2016) en donnent la cartographie systématique — anomalies classées par turnover, coûts effectifs mesurés, et l'effet des techniques d'atténuation (bandes, §4.3.2 : elles sauvent une classe entière de signaux moyens-fréquence). La **coverage** ensuite : la fraction de l'univers où le signal est défini — une coverage partielle et *variable* (données fondamentales manquantes, événements) réduit le breadth effectif, biaise la normalisation cross-sectionnelle (§1.3.1 : le z-score d'un sous-univers n'est pas celui de l'univers), et exige la règle : normaliser sur l'univers couvert, positionner zéro hors couverture, et *mesurer* la stabilité de la couverture dans le temps. La capacité enfin renvoie à §4.4.4 (A\* ∝ ADV·α²/τ³), avec le diagnostic rapide au niveau signal : recalculer le spread sous filtres de liquidité croissants et en VW — la pente de dégradation *est* le profil de capacité, et un spread qui s'effondre au premier filtre annonce un A\* dérisoire.

**2.1.5 Expositions résiduelles — ce qui reste quand les facteurs sont servis**

Deux mesures complémentaires du même objet. **Returns-based** : régresser la série du spread long-short sur les rendements factoriels,

> r^{LS}_t = α + β'F_t + ε_t,  F = {MKT, SMB, HML, RMW, CMA, MOM, ...}

— le t(α) Newey-West est la statistique finale (« l'anomalie survit-elle aux facteurs ? »), les β diagnostiquent le déguisement (un « nouveau » signal à β_HML = 0,8 est du value réempaqueté), et le R² dit quelle part du sort est du beta recyclé. Cadres : Fama-French (1993, JFE ; 2015, JFE pour le cinq-facteurs), Carhart (1997) pour MOM. **Holdings-based** : à chaque date, les expositions du portefeuille de signal b_t = B_t'w_t via le modèle de risque de §4.1 — instantané là où le returns-based est moyen, il capte le *style drift* (un signal dont le β momentum oscille entre −0,5 et +0,5 a un β moyen nul et un problème réel) et c'est lui que l'optimiseur contraindra (§4.2.2). La cohérence des deux est un test en soi ; leur divergence signale un modèle de risque incomplet ou des expositions non linéaires. Et la clôture conceptuelle, triple renvoi : ce qui survit ici est l'alpha *au sens du modèle choisi* (§0.7 — changer de F déplace la frontière), c'est l'IC *transférable* que la neutralisation amont visait (§1.3.3), et c'est l'entrée du test d'admission au pool (§3.4 — l'IC marginal étant l'exposition résiduelle *au pool lui-même* plutôt qu'aux facteurs).

---

Nœud 2.1 passé en ✓✓. Le quintet à retenir : plancher 1/√(N_eff−1) et plafond d'ICIR ; IC retardé vs cumulé et φ = ln2/H_α mesuré ici ; le filtre Hou-Xue-Zhang avant de croire un sort ; c\* = spread/turnover ; t(α) Newey-West comme juge de paix. Coutures : φ vers 4.3.3/5.3.3 (le paramètre traverse l'arbre) ; le placebo aléatoire comme étalon du plancher rejoint 6.2 (outillage du backtest) ; Drechsler ↔ coût d'emprunt dans la cible (1.4.1). La suite au même grain : **2.2** (Fama-MacBeth complet, protocole de simulation) puis **2.4**. On enchaîne ?

---

## [M115] Humain — 2026-07-24 10:43:25

Oui

---

## [M116] Assistant — 2026-07-24 10:44:55

On fore : **2.2 Backtest cross-sectionnel** — la machinerie de simulation, au grain ✓✓. Le sous-arbre local :

```
2.2 BACKTEST CROSS-SECTIONNEL   mesurer proprement ce qu'on aurait gagné
│
├── 2.2.1 Fama-MacBeth complet      deux passes, Shanken, NW, portefeuille miroir
├── 2.2.2 Protocole & lags          la timeline signal → exécution → rendement
├── 2.2.3 Univers PIT & delistings  breakpoints, Shumway, filtres
├── 2.2.4 Coûts dans le backtest    la courbe Sharpe(c), l'atténuation simulée
└── 2.2.5 Nettoyage crypto          wash trading, tokens morts, funding
```

**2.2.1 Fama-MacBeth — la régression qui est un portefeuille**

La procédure (Fama & MacBeth, « Risk, Return, and Equilibrium », JPE 1973), dans sa version caractéristiques (la nôtre — le signal *est* le régresseur, pas un beta estimé) : à chaque date, la régression cross-sectionnelle

> **r_{i,t→t+h} = γ₀,t + γ₁,t·s_{i,t} + γ'₂,t·Z_{i,t} + e_{i,t}**

avec Z les contrôles (taille, book-to-market, momentum, secteurs — tout ce dont on veut prouver qu'on n'est pas le déguisement). Puis l'inférence sur la série {γ₁,t} :

> **γ̄₁ = (1/T)·Σ γ₁,t**,  t = γ̄₁ / (σ_NW(γ₁,t)/√T)

— Newey-West avec lag ≥ h dès que les horizons se chevauchent (quatrième face de l'encadré D). La beauté structurelle, à énoncer explicitement : γ₁,t est le **rendement d'un portefeuille** — la solution γ_t = (X'X)⁻¹X'r_t fait de chaque coefficient le rendement du portefeuille long-short de coût nul, d'exposition unitaire au signal et *nulle aux contrôles* (le portefeuille miroir, factor-mimicking) ; Fama-MacBeth est donc un sort multivarié continu, et avec un signal standardisé (§1.3.1), γ̄₁ ≈ IC̄ × σ_cs(r) — le pont quantitatif exact avec §2.1.1. La mécanique gère d'office la corrélation *cross-sectionnelle* des erreurs (chaque date fournit une observation de γ) mais pas leur corrélation temporelle — c'est le partage établi par Petersen (« Estimating Standard Errors in Finance Panel Data Sets », RFS 2009) : FM + NW pour les effets de date, clustering bidirectionnel si les deux dimensions corrèlent. Deux raffinements praticiens : la version **WLS** (pondérer par √cap ou 1/σ_i² — la régression équipondérée est dominée par les micro-caps, le même mal que les sorts EW de §2.1.3) et la version **robuste** (régresser sur les rangs du signal, ou perte de Huber — §1.4.4 appliqué à l'inférence). Enfin, pour mémoire, la version originale à deux passes (betas estimés en première passe, primes en seconde) exige la correction d'**errors-in-variables** de Shanken (RFS 1992, facteur multiplicatif (1 + γ̄'Σ_f⁻¹γ̄) sur les variances) — et le débat Daniel-Titman (JF 1997) — caractéristiques vs covariances — tranche pour nous : le desk prédit avec des caractéristiques, la question « est-ce une prime de risque ? » appartient à §0.7.

**2.2.2 Protocole et lags — la timeline exacte**

La chronologie contractuelle du backtest, à écrire noir sur blanc car chaque flèche est un piège :

> features gelées à knowledge time ≤ close(t) → signal calculé sur close(t) → ordre transmis → **exécution à open(t+1)** (ou close(t+1), ou VWAP(t+1)) → rendement couru depuis le prix d'exécution → sortie selon la même convention

Les violations canoniques, par ordre de fréquence : l'exécution au close(t) même (le look-ahead d'un jour — sur un reversal, il capture le bid-ask bounce de Roll §5.1.1 et fabrique plusieurs Sharpes fictifs : le test d'acide d'un backtest de reversal est sa survie au passage close(t) → open(t+1)) ; les **prix stale** des illiquides (un close qui date de 14h30 rend le titre faussement prévisible par le marché de fin de journée — corrections à la Scholes-Williams, ou filtre d'ADV qui évacue le problème) ; et l'incohérence entrée/sortie (entrer au VWAP et sortir au close mélange deux benchmarks, §5.3.2). Le choix du prix d'exécution est lui-même une déclaration de stratégie : close-to-close simule un ordre MOC (§5.1.2 — avec son look-ahead d'auction propre : le signal utilisant l'imbalance de clôture ne peut pas s'exécuter à cette clôture), open-to-open un ordre à l'ouverture, et l'écart entre les deux backtests *mesure* la composante overnight/intraday du signal (§1.2.2). Dernier étage : la **fréquence de rebalancement** est un paramètre distinct de h — rebalancer chaque jour un signal à h = 21 revient à détenir 21 tranches superposées (le portefeuille « overlapping » de Jegadeesh-Titman 1993, qui lisse et diversifie le point d'entrée) ; l'alternative — une seule tranche mensuelle — introduit une dépendance à la phase du calendrier qui doit être testée sur les 21 phases (et leur dispersion est un diagnostic de robustesse gratuit).

**2.2.3 Univers point-in-time et delistings — qui a le droit d'être là**

La construction : l'univers de la date t contient les titres *vivants et éligibles au knowledge time de t* — constituants historiques (pas la liste actuelle rétro-projetée : backtester sur le S&P 500 d'aujourd'hui, c'est conditionner sur la survie et le succès), filtres appliqués avec les données d'époque (prix > 5$, ADV minimal, âge de cotation), et les **breakpoints NYSE** pour les tris (les quantiles calculés sur NYSE seul puis appliqués à tous — la convention Fama-French qui empêche les micro-caps Nasdaq de peupler les extrêmes, complémentaire du filtre Hou-Xue-Zhang de §2.1.3). Les sorties ensuite, avec leurs chiffres : Shumway (« The Delisting Bias in CRSP Data », JF 1997) — les rendements de radiation manquants pour cause de performance valent en moyenne **≈ −30%** sur NYSE/AMEX ; Shumway & Warther (JF 1999) : **≈ −55%** sur Nasdaq ; les omettre transforme tout signal short-distress en machine à Sharpe fictif, et la règle d'imputation (rendement observé si disponible, forfait conservateur sinon, selon le code de radiation) fait partie du protocole écrit. En crypto : l'univers « top N par capitalisation » se reconstruit point-in-time (le top 100 de 2021 contient les morts — §1.2.4), les delistings d'exchange sont l'événement terminal (souvent −50 à −90% *avant* la radiation effective : la date pertinente est l'annonce), et l'éligibilité inclut la venue (un token liquide seulement sur une venue douteuse n'est pas investissable au sens du backtest).

**2.2.4 Coûts dans le backtest — la courbe, pas le chiffre**

Le net se simule avec le modèle de §4.3.1 en version réduite — coût par trade = c_i (spread/2 + frais) + terme d'impact si les tailles simulées le justifient — et le livrable honnête est la **courbe Sharpe(c)** : le Sharpe net en fonction du coût unitaire, de 0 à 50 bps, dont la pente est le turnover (§2.1.4, c\* en est l'intersection avec zéro) ; un signal se présente avec sa courbe, pas avec son point le plus flatteur. Le raffinement décisif, documenté par Novy-Marx & Velikov (RFS 2016) : les techniques d'atténuation — bandes d'hystérésis dans le tri (entrer au décile 10, ne sortir qu'au 7 — le §3.1.3c appliqué aux titres), rebalancement espacé, filtres de liquidité — se simulent **dans** le backtest, car elles changent le signal effectif (son turnover *et* son spread brut) ; comparer le signal brut à coûts nuls puis « promettre » l'atténuation en production est l'écart backtest/réalité le plus commun après le look-ahead. La cohérence transversale : les paramètres de coût du backtest et ceux de l'optimiseur (§4.3.1) sortent de la même TCA (§5.5.4) — un desk dont le backtest suppose 5 bps et dont la TCA mesure 15 a un pipeline qui se ment à lui-même.

**2.2.5 Nettoyage crypto — l'univers hostile**

Quatre opérations spécifiques, dans l'ordre. Le **wash trading** : Cong, Li, Tang & Yang (« Crypto Wash Trading », Management Science 2023) estiment que sur les venues non régulées la majorité — jusqu'à ~70% — du volume rapporté est fictive, détectable par les régularités statistiques du trading réel (Benford sur les premiers chiffres, sur-représentation des tailles rondes, distribution des tailles de trades) ; la conséquence en cascade est établie (§5.2.4, §4.4.4) : un ADV gonflé sous-estime Q/V donc les coûts donc surestime la capacité — le nettoyage (volumes des seules venues de confiance, ou ADV corrigé par les tests) précède *tout* filtre de liquidité et tout modèle de coût. La **continuité des instruments** : migrations de contrats, redénominations, changements de spécification des perps (§1.2.4) — la table de correspondance datée est un actif de §6.1. Les **cibles funding-incluses** (§1.4.1) : un backtest cross-sectionnel sur perps qui omet le funding fabrique de faux alphas exactement là où le positionnement est extrême — c'est-à-dire là où le signal semble le meilleur. Et les **conventions temporelles** : close UTC 00:00 arbitraire (§1.2.2 — la robustesse se teste en décalant la grille de quelques heures, le pendant crypto du test de phase de 2.2.2), timestamps hétérogènes entre venues, et la grille de funding comme frontière d'attribution des rendements. Le placebo final, qui coiffe le nœud des deux côtés : faire tourner le protocole complet sur un signal aléatoire — l'IC doit être au plancher de §2.1.1, le Sharpe net négatif du coût ; tout écart mesure la fuite résiduelle du protocole lui-même.

---

Nœud 2.2 passé en ✓✓. Le quintet : γ_t est un portefeuille (et γ̄ ≈ IC×σ_cs) ; la timeline close(t) → open(t+1) comme contrat ; −30/−55% de Shumway ; la courbe Sharpe(c) ; le placebo comme certification du protocole. Coutures : le placebo rejoint 6.2 (outillage), la courbe Sharpe(c) rejoint 2.1.4 (c\*) et 5.5.4 (calibration commune), le test de phase UTC rejoint 1.2.2. Reste **2.4** pour clore la branche 2 en ✓✓ — puis 3.2-3.4, 1.1, et la branche 6. On continue ?

---

## [M117] Humain — 2026-07-24 10:46:09

Ok

---

## [M118] Assistant — 2026-07-24 10:47:40

On clôt la branche 2 en ✓✓ : **2.4 Non-stationnarité & régimes** — la validité a une date de péremption, et ça se mesure. Le sous-arbre local :

```
2.4 NON-STATIONNARITÉ & RÉGIMES   un IC est daté ; le surveiller, le comprendre
│
├── 2.4.1 Rolling IC & ruptures      Bai-Perron, CUSUM de Page, ARL
├── 2.4.2 Crowding & publication     McLean-Pontiff, comomentum, capital d'arbitrage
├── 2.4.3 Validation par régime      carry vs revalorisation, taxonomie de persistance
└── 2.4.4 Histoires courtes          le cas crypto : N = 4 cycles, priors transférés
```

**2.4.1 Rolling IC et ruptures — détecter la mort d'un signal**

L'outil de base est le rolling IC (fenêtre 1-2 ans) avec ses bandes : sous stabilité, IC̄_rolling fluctue autour de sa moyenne avec un écart-type σ(IC)/√T_fen — pour σ(IC) = 0,15 et 252 jours, ±0,019 par écart-type ; la moitié des « signaux morts » du folklore vivent à l'intérieur de ces bandes (§6.3, le même calcul qui protège les signaux en paper trading). Pour l'analyse *ex post*, les tests de rupture structurelle : **Bai-Perron** (Econometrica 1998 ; Journal of Applied Econometrics 2003) estime le nombre et les dates de ruptures multiples de moyenne dans la série {IC_t} par programmation dynamique, avec les valeurs critiques du sup-F — l'outil qui répond à « le signal a-t-il changé de régime, et quand » ; l'ajustement paramétrique concurrent, plus doux, est la décroissance continue IC(t) = IC₀·e^{−t/T_decay}, et départager rupture vs décroissance est en soi informatif (une rupture pointe vers un événement — changement de microstructure, publication, arrivée d'un gros acteur ; une décroissance vers l'érosion par crowding).

Pour la *surveillance en ligne* — le vrai besoin du desk —, le cadre correct est le contrôle séquentiel : le **CUSUM de Page** (Biometrika 1954),

> **S_t = max(0, S_{t−1} + (μ₀ − IC_t − k))**,  alerte si S_t > h_c

accumule les écarts sous la moyenne de référence μ₀ (moins une tolérance k, typiquement δ/2 pour une dégradation cible δ) et sonne au franchissement de h_c ; le réglage (k, h_c) arbitre le délai de détection contre le taux de fausses alertes via l'**ARL** (average run length — l'espérance du temps entre fausses alertes sous H₀, calculable par les approximations de Siegmund). La leçon quantitative est dégrisante et referme la boucle sur §3.1.2 : détecter *rapidement* qu'un IC est passé de 0,03 à 0 exige des mois même avec le test optimal — le bruit σ(IC) est tel que la réponse rationnelle à la suspicion n'est pas binaire (couper/garder) mais graduelle : c'est exactement ce que le bucket avec hystérésis de §3.1.3c et la pondération bayésienne implémentent — la rétrogradation *est* le test séquentiel rendu décision.

**2.4.2 Crowding et publication — l'alpha comme ressource épuisable**

Le résultat de référence est **McLean & Pontiff** (« Does Academic Research Destroy Stock Return Predictability? », JF 2016) : sur 97 anomalies publiées, les rendements baissent d'environ **26% entre l'échantillon d'origine et le hors-échantillon pré-publication** (la part attribuable au data mining des auteurs — la mesure *empirique* du biais que §2.3 corrige a priori) et de **58% après publication** — soit ~32 points imputables à la publication elle-même, avec les signatures de l'arbitrage : la baisse est plus forte sur les anomalies liquides et peu coûteuses à trader, et volumes/short interest montent dans les jambes concernées. L'alpha est une rente informationnelle : la révéler la fait consommer — la moitié environ survit, ce qui calibre le prior de long terme sur tout signal de la littérature (le m du modèle hiérarchique de §3.1.3a, segmenté « publié vs propriétaire »).

La mesure du crowding *en temps réel* ensuite. **Lou & Polk** (« Comomentum », JPE 2022) : la corrélation anormale des *résidus* des titres d'une même jambe (momentum entre eux, net des facteurs) mesure la densité de capital d'arbitrage sur la stratégie — le comomentum élevé prédit des rendements faibles puis des crashes de la stratégie : la corrélation intra-jambe est l'empreinte digitale des détenteurs communs. **Hanson & Sunderam** (« The Growth and Limits of Arbitrage », RFS 2014) utilisent le short interest agrégé des jambes short comme proxy du capital alloué, avec la même conclusion en coupe : plus de capital, moins de rendement. Et la dynamique de crise est celle déjà documentée (Khandani-Lo, §4.5.2 ; le cadre théorique : Stein, « Presidential Address: Sophisticated Investors and Market Efficiency », JF 2009 — l'arbitrage désancré devient déstabilisant sous contrainte de capital) : le crowding transforme le profil d'un signal — espérance érodée, corrélation conditionnelle accrue, queue gauche épaissie — c'est-à-dire exactement les trois quantités que σ(IC), le comomentum et les stress tests de §4.5 surveillent. Pour le desk : le monitoring de crowding par sleeve (corrélation résiduelle intra-jambe, coût d'emprunt des shorts, funding pour les jambes crypto) appartient au tableau de bord de §6.3 au même titre que l'IC.

**2.4.3 Validation par régime — comprendre avant de moyenner**

Le geste minimal : recalculer IC et spread par régime pré-spécifié (vol haute/basse, dispersion, liquidité — les conditionneurs de §1.2.3, *déclarés avant* : chaque découpage ex post est un essai de plus au compteur du DSR). Le geste profond : la **décomposition carry/revalorisation** d'Arnott, Beck & Kalesnik (« How Can 'Smart Beta' Go Horribly Wrong? », 2016) — le rendement historique d'une caractéristique se partage en

> **rendement = carry structurel + Δvalorisation**

(pour un facteur value : le rendement du portefeuille = l'écart de yield entre jambes + le resserrement/écartement du multiple relatif). La part *revalorisation* n'est pas répétable — un facteur dont le backtest vit du renchérissement de sa propre jambe longue a un rendement espéré prospectif bien moindre que son historique, et le test honnête est le rendement **net de revalorisation** (à écart de valorisation constant). C'est le pendant « niveau facteur » du changements-vs-niveaux de §1.2.1, et un filtre d'admission au pool à part entière. La grille de lecture finale est la **taxonomie de persistance** (l'esprit d'Ilmanen, *Expected Returns*, et de la question de §1.2.3 — « qui perd, et pourquoi ça continue ») : prime de risque (le rendement paie un risque réel — persistant, mais avec ses crashes par construction), friction structurelle (contrainte réglementaire, flux mécaniques — persistant tant que la structure tient, et *datable* : la rupture de 2.4.1 correspond à un changement de structure identifiable), inefficience comportementale (persistante si les limites à l'arbitrage tiennent — la plus exposée au crowding de 2.4.2). Trois espérances de vie différentes, trois demi-vies d'estimation différentes (§3.2 : l'EMA des IC se paramètre *par famille de persistance*), et la réponse à « combien d'histoire utiliser » cesse d'être un chiffre unique.

**2.4.4 Histoires courtes — le cas crypto**

Le problème en chiffres : l'histoire investissable sérieuse commence vers 2017-2018, traversée de ruptures structurelles majeures — institutionnalisation post-2020, effondrements de venues (FTX, 2022), ère des ETF (2024) — soit, au sens de Bai-Perron, quatre ou cinq régimes de 1-2 ans chacun : la « longue histoire » crypto est une collection de courtes histoires non stationnaires. Les pseudo-saisonnalités populaires en sont le symptôme : le « cycle du halving » repose sur **N = 4 observations** — aucune inférence n'y survit (σ d'une moyenne sur 4 tirages...), et le traiter comme un signal est le multiple testing de §2.3 à l'état chimiquement pur. Les réponses structurelles, par ordre : **le breadth spatial remplace le temps** — 200 tokens × 5 ans portent plus d'information cross-sectionnelle que 2 actifs × 50 ans, à condition de valider en coupe (§2.1, §2.2) plutôt qu'en série ; **les priors transférés** — les caractéristiques validées sur un siècle d'equity (momentum, taille, liquidité, carry) arrivent avec leur m et τ hiérarchiques (§3.1.3a) et l'histoire crypto ne fait que les mettre à jour, ce que la littérature confirme : Liu & Tsyvinski (« Risks and Returns of Cryptocurrency », RFS 2021) et Liu, Tsyvinski & Wu (« Common Risk Factors in Cryptocurrency », JF 2022) établissent que taille et momentum structurent le cross-section des tokens — les mêmes primes, sur un marché neuf ; **la pondération du récent** enfin, poussée plus loin qu'en equity (demi-vies d'IC de 1-2 ans, §1.4.4 côté entraînement), avec l'aveu épistémique que §2.4 impose de rendre explicite : en crypto, la part du jugement (priors, mécanismes, « qui perd ») dans la conviction est structurellement plus élevée que la part de la statistique — le nier en empilant les tests sur cinq ans de données, c'est fabriquer de la fausse précision.

---

**La branche 2 est intégralement en ✓✓.** Le quatuor du nœud : CUSUM/ARL (la détection a un coût en délai incompressible) ; −26%/−58% de McLean-Pontiff (le data mining et le crowding, mesurés) ; rendement net de revalorisation ; N = 4 du halving comme memento. Coutures : la rétrogradation de bucket = test séquentiel (3.1.3c ↔ 2.4.1) ; le comomentum au tableau de bord de 6.3 ; la taxonomie de persistance pilote les demi-vies de 3.2. Restent au grain simple : **3.2-3.4**, **1.1**, **branche 6**. On enchaîne sur 3.2 ?

---

## [M119] Humain — 2026-07-24 10:48:48

Ok, continue, et n oublie pas de donner les formules et explications mathématiques quand c est pertinent

---

## [M120] Assistant — 2026-07-24 10:50:07

On fore : **3.2 Régression régularisée** — le continuum entre le naïf et l'optimal, au grain ✓✓. Le sous-arbre local :

```
3.2 RÉGRESSION RÉGULARISÉE      estimer w ∝ C⁻¹ρ sans se faire tuer par C⁻¹
│
├── 3.2.1 Ridge & le continuum       spectre, lecture bayésienne, df(κ)
├── 3.2.2 Shrinkage de C             Ledoit-Wolf, cible en blocs, RIE
├── 3.2.3 Signes & NNLS              KKT, priors durs, familles d'abord
└── 3.2.4 Fenêtres & disjonction     demi-vies par persistance, nested CV
```

**3.2.1 Ridge — le continuum, rendu formel**

Le cadre : régresser en panel la cible normalisée (vol-scalée, résidualisée — §1.4.1) sur les K signaux empilés, y = S·w + e. Avec signaux et cible standardisés (§1.3), les moments empiriques s'identifient aux objets de la branche : (1/n)·S'S ≈ **C** (la corrélation inter-signaux) et (1/n)·S'y ≈ **ρ** (le vecteur des IC). L'OLS donne donc w ∝ C⁻¹ρ — littéralement le Markowitz de l'espace des signaux (§3, cadre de tête) — et la ridge :

> **w(κ) = (S'S + κI)⁻¹·S'y ∝ (C + κ̃I)⁻¹·ρ**

Les deux limites, désormais démontrées et plus seulement énoncées : κ̃ → 0 rend C⁻¹ρ (l'optimum théorique, §3.1.2) ; κ̃ → ∞ rend w ∝ ρ (l'IC-weighting, la solution du monde décorrélé). La lecture **spectrale** dit pourquoi l'interpolation est la bonne : en base propre C = Σ_j λ_j·u_j u_j', la ridge multiplie chaque direction propre par

> **λ_j / (λ_j + κ̃)**

— les directions à grande valeur propre (les contrastes entre familles, bien estimés) passent presque intacts ; les directions à petite λ_j (les différences fines *au sein* d'un banc de momentum corrélé à 0,9 — précisément ce que C⁻¹ amplifiait en poids explosifs de signes alternés, §3.1.4) sont écrasées. La ridge est un filtre passe-haut sur le spectre de C — le pendant combinaison du clipping RMT de §4.1.2. La lecture **bayésienne** referme l'encadré A : la ridge est le MAP du modèle w ~ N(0, τ²I), avec κ = σ²_e/τ² — régulariser fort, c'est déclarer un prior serré sur les poids, et le κ optimal élevé qu'on trouve en pratique par CV purgée (§2.3.1) est la *mesure* de la domination du bruit d'estimation. Le degré de liberté effectif df(κ) = Σ_j λ_j/(λ_j+κ̃) quantifie la complexité réellement dépensée — typiquement une fraction de K, à logger comme tel au registre (§2.3). Variante à éviter en général : le **lasso** — sa sparsité est séduisante mais sa sélection parmi des signaux corrélés est instable (il choisit *un* momentum du banc arbitrairement, et un autre au resample suivant) ; l'elastic net (Zou & Hastie, JRSS-B 2005) mitige, mais la structure correcte est ailleurs (3.2.3). Référence de fond : Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*.

**3.2.2 Shrinkage de C — la cible en blocs**

L'autre moitié du problème : Ĉ elle-même est bruitée (K(K−1)/2 paramètres, §3.1.4). Le shrinkage linéaire de Ledoit-Wolf (§4.1.3, transposé) :

> **C̃ = δ\*·T₀ + (1−δ\*)·Ĉ**,  δ\* ≈ Σ_ij Var(ĉ_ij) / Σ_ij (ĉ_ij − t₀,ij)²

— proportion de bruit sur distance à la cible. Le choix de T₀ est le vrai levier : l'identité est agnostique, la corrélation constante (le « Honey » de LW 2004) déjà meilleure, mais la cible **en blocs par famille** domine parce que la vraie C *a* cette topologie (§3.4 : les signaux naissent en familles) —

> t₀,ij = ρ̄_intra si i, j même famille ; ρ̄_inter sinon

— deux paramètres estimés sur toutes les paires, au lieu de K²/2 : le biais de la cible est faible là où le bruit de Ĉ est fort. Pour K grand, le shrinkage **non linéaire** (RIE, Ledoit-Péché ; Bun-Bouchaud-Potters, §4.1.2) corrige chaque valeur propre individuellement. Et la parenté avec 3.2.1 mérite d'être écrite : shrinker C vers l'identité *puis* inverser donne (δI + (1−δ)C)⁻¹ρ — la même famille de solutions que (C + κ̃I)⁻¹ρ à reparamétrisation près ; ridge et shrinkage-de-C sont deux paramétrages du même estimateur, et on n'empile pas les deux à pleine dose (le κ de CV se choisit *après* avoir fixé la cible de C, sinon on double-régularise à l'aveugle). L'estimation de Ĉ elle-même suit les conventions du §1.2.2 : EWMA, demi-vie cohérente avec celle des IC.

**3.2.3 Contraintes de signe et NNLS — le prior dur**

La règle des signes (§3.1.1 : un signal admis garde son signe économique) devient contrainte d'optimisation :

> **w\* = argmin ‖y − Sw‖²  s.c.  w ≥ 0**   (NNLS, algorithme actif de Lawson-Hanson)

Les conditions KKT en donnent la lecture : pour chaque k, soit w_k > 0 et le gradient s'annule, soit w_k = 0 et le gradient est ≥ 0 — un signal dont la corrélation *partielle* avec la cible, sachant les autres, est négative reçoit **exactement zéro**, jamais un poids négatif. C'est le comportement voulu : la régression qui « veut » retourner un carry signale un problème de données ou de redondance (§3.1.1), pas une opportunité — le NNLS transforme l'alerte en plancher. La parenté avec Jagannathan-Ma (§4.2.2, encadré A) est exacte : les contraintes de signe équivalent à un shrinkage implicite des entrées de C qui justifiaient les poids négatifs — le même théorème, dans l'espace des signaux. La précaution d'emploi : sur un banc corrélé, le NNLS aussi concentre (il met à zéro la plupart des variantes d'une même famille — moins arbitrairement que le lasso, mais concentration quand même) ; la structure correcte est **hiérarchique**, héritée de §3.1.1 : agréger *d'abord* les familles en composites (1/N intra-famille — le niveau où l'estimation n'a rien à dire), puis NNLS/ridge *entre* les composites (le niveau où les données discriminent). Deux étages, chacun réglé à la granularité que l'information supporte.

**3.2.4 Fenêtres et disjonction — quand estimer, sur quoi**

Les demi-vies d'estimation des IC et de C (2-4 ans, §3.1.3d) se raffinent par la taxonomie de persistance de §2.4.3 : longues pour les primes de risque (le m et le τ du prior y sont stables), courtes pour les signaux comportementaux exposés au crowding (McLean-Pontiff impose de pondérer le post-publication) — la réponse à « combien d'histoire » est *par famille*, pas globale. La **disjonction** ensuite, le piège central du nœud : les signaux du pool ont été *sélectionnés* sur leurs backtests (branche 2), donc E[ρ̂_k | k admis] > ρ_k — le conditionnement à la sélection gonfle les IC mesurés sur l'échantillon de sélection, et une régression de combinaison ajustée sur ce même échantillon sur-pondère mécaniquement les plus chanceux : la chance est payée deux fois (§3.1.4, l'error maximization composée avec le biais de sélection). Les remèdes, par ordre de propreté : estimer w sur données strictement *postérieures* à l'admission de chaque signal ; ou utiliser comme ρ̂ les prédictions **out-of-fold** de la CV purgée (§2.3.1 — la règle que le stacking de §3.3 érigera en absolu) ; ou au minimum, shrinker les ρ̂ post-sélection par le facteur bayésien de §3.1.3a avec un prior durci. La validation de la *procédure* entière — le choix de κ, de la cible T₀, des demi-vies — relève de la **CV imbriquée** : boucle interne pour estimer (w, κ), boucle externe purgée pour juger la règle de combinaison elle-même ; c'est la règle, pas les poids, qu'on valide — les poids changeront, la règle reste. Et la stabilité se mesure comme tout le reste : le turnover de w (EMA sur les poids, §3.1.4) est une ligne du tableau de bord de §6.3.

---

Nœud 3.2 passé en ✓✓. Le quatuor : λ_j/(λ_j+κ̃) (la ridge est un filtre spectral) ; la cible en blocs (deux paramètres contre K²/2) ; KKT du NNLS (zéro, jamais négatif — familles d'abord) ; la disjonction (la chance ne se paie qu'une fois). Coutures : ridge ↔ clipping RMT (4.1.2) et encadré A enrichi ; demi-vies par persistance ↔ 2.4.3 ; out-of-fold ↔ 2.3.1 et 3.3. Restent : **3.3**, **3.4**, **1.1**, **branche 6**. J'enchaîne sur 3.3.

---

## [M121] Humain — 2026-07-24 10:50:16

Ok

---

## [M122] Assistant — 2026-07-24 10:51:28

On fore : **3.3 Stacking & méta-modèles** — les poids qui cessent d'être constants, au grain ✓✓. Le sous-arbre local :

```
3.3 STACKING & MÉTA-MODÈLES     apprendre à combiner, sans payer deux fois
│
├── 3.3.1 Le stacking propre        Wolpert, out-of-fold, poids convexes
├── 3.3.2 Poids conditionnels       w(z) = dictionnaire augmenté, rien de plus
├── 3.3.3 Algorithmes d'experts     Hedge, regret en √(T ln K), fixed share
└── 3.3.4 Hiérarchie de complexité  quand chaque étage gagne sa place
```

**3.3.1 Le stacking propre — la règle out-of-fold, démontrée**

Le cadre (Wolpert, « Stacked Generalization », Neural Networks 1992) : un méta-modèle régresse la cible sur les *prédictions* des modèles de base, y = Σ_k β_k·ŝ_k + e. Le danger annoncé en version courte se démontre en une ligne : si ŝ_k est la prédiction **in-sample** d'un modèle de base, elle s'écrit ŝ_k = signal vrai + une part ajustée sur le bruit *de ce même échantillon* — sa corrélation mesurée avec y contient donc le terme d'overfit, et elle est d'autant plus haute que le modèle k est plus surajusté ; le méta-modèle, qui alloue à la corrélation, **récompense l'overfitting en proportion exacte de sa gravité**. La règle absolue en découle : les méta-features sont les prédictions **out-of-fold** d'une CV purgée (§2.3.1) — chaque ŝ_{k,t} produit par un modèle qui n'a jamais vu la période de t, purge et embargo compris ; le schéma à deux étages hérite du purging au carré (la fuite peut passer par l'un ou l'autre étage).

Deux résultats structurent la pratique. **Breiman** (« Stacked Regressions », Machine Learning 1996) : la contrainte de non-négativité sur les β est ce qui fait marcher le stacking — sans elle, la colinéarité des prédictions (nos signaux corrélés, §3.2.1) produit les poids explosifs habituels ; avec elle, on retombe sur le NNLS de §3.2.3, appliqué aux prédictions. La version complète — poids convexes, β ≥ 0 et Σβ = 1 — est le **super learner** (van der Laan, Polley & Hubbard, 2007), avec sa propriété d'oracle : la combinaison convexe sélectionnée par CV fait asymptotiquement aussi bien que le meilleur élément de la bibliothèque — la garantie qui justifie d'*empiler* les candidats plutôt que d'en élire un. La traduction pour nous : le stacking financier propre est un NNLS out-of-fold sur composites de familles — c'est-à-dire exactement la machinerie de 3.2, nourrie de prédictions décontaminées ; le « méta-modèle » n'est pas un objet nouveau, c'est la même régression avec la seule hygiène qui la rende honnête.

**3.3.2 Poids conditionnels — une équivalence qui dégonfle le sujet**

Le désir : w(z_t) dépendant du régime, puisque les IC sont conditionnels (§1.2.3, §3.1.3d). La formalisation minimale : modéliser ρ_k(z) = a_k + b_k·g(z), d'où w(z) ∝ C⁻¹ρ(z). Et l'équivalence qui remet le sujet à sa place :

> **w(z)·s  =  Σ_k [a_k·s_k + b_k·(s_k·g(z))]**

— une combinaison à poids conditionnels est une combinaison à poids **constants sur le dictionnaire augmenté** {s_k, s_k·g(z)}. Rien de nouveau sous le soleil : les « poids dynamiques » sont des signaux d'interaction (§1.2.3) versés au pool, toute la machinerie de 3.1-3.2 s'applique telle quelle (ridge sur le dictionnaire augmenté, NNLS par familles, shrinkage), et surtout le **coût en degrés de liberté devient explicite** : m conditionneurs multiplient le dictionnaire par (1+m) — c'est le N du DSR qui gonfle, comptabilisé au registre, et non une sophistication gratuite. Les garde-fous hérités tiennent : 1-2 conditionneurs *pré-spécifiés* maximum, g lisse (sigmoïde de z-score — jamais de seuil dur, §1.2.3), et l'interaction admise seulement si l'IC conditionnel est démontré par double sorts (§1.2.3) sur données antérieures à la spécification. Le cas dégénéré utile : g(z) = z-score de vol du *propre* P&L du sleeve — le conditionnement le plus défendable est souvent le vol-scaling par sleeve déjà imposé par §3.1.3b, qui est un poids conditionnel qui ne dit pas son nom.

**3.3.3 Algorithmes d'experts — la robustesse sans hypothèses**

Le cadre adversarial : K experts (les sleeves), des gains g_{k,t} révélés séquentiellement, aucune hypothèse — ni stationnarité, ni distribution. **Hedge** / poids exponentiels (Freund & Schapire, JCSS 1997 ; la tradition multiplicative weights) :

> **w_{k,t+1} ∝ w_{k,t}·exp(η·g_{k,t})**  ⟺  w_{k,t} ∝ exp(η·Σ_{s≤t} g_{k,s})

avec la garantie de **regret** : contre le meilleur expert *rétrospectif*,

> **Regret_T = max_k Σ g_{k,t} − Σ ⟨w_t, g_t⟩ ≤ √((T/2)·ln K)**  (η\* = √(8 ln K / T))

— sous-linéaire en T : le regret *par période* tend vers zéro quoi que fassent les marchés. Les **universal portfolios** de Cover (Mathematical Finance 1991) donnent la version richesse : le portefeuille universel atteint la richesse du meilleur portefeuille constamment rebalancé à un facteur polynomial en T près — asymptotiquement, on ne perd rien face au meilleur mix fixe choisi *avec le recul*. La traduction praticienne dégonfle et éclaire à la fois : les poids exponentiels sur gains cumulés récents ≈ **pondérer par une EMA de performance** — l'ICIR-weighting de §3.1.3 avec η jouant le rôle de la demi-vie ; la nouveauté n'est pas la formule mais la *garantie* (elle tient sans stationnarité — précieux là où §2.4 a détruit l'hypothèse) et la variante **fixed share** (Herbster & Warmuth, Machine Learning 1998) : mélanger à chaque pas une fraction α vers l'uniforme, w ← (1−α)·w + α/K, ce qui borne le regret contre le meilleur expert *par segments* — la version algorithmique du suivi de régimes, sans HMM ni détection (§2.4.1 : on ne détecte pas la rupture, on reste toujours prêt à en payer une). Les limites, honnêtement : la garantie est contre le meilleur *expert*, pas la meilleure *combinaison* (Hedge ne diversifie pas, il traque) ; sur des gains aussi bruités que des P&L quotidiens, η\* est minuscule et la trajectoire des poids quasi constante — l'algorithme converge vers... l'équipondération lentement inclinée, ce qui est peut-être sa vraie leçon.

**3.3.4 La hiérarchie de complexité — chaque étage paie son loyer**

L'empilement rationnel, du bas vers le haut : (i) poids constants régularisés — composites de familles, ridge/NNLS, shrinkage bayésien (§3.1-3.2) : la colonne vertébrale ; (ii) l'overlay adaptatif — fixed share à η petit sur les composites : le filet anti-régime, quasi gratuit en degrés de liberté (deux hyperparamètres, pré-spécifiables) ; (iii) le conditionnement explicite — 1-2 interactions démontrées, versées au dictionnaire (§3.3.2) ; (iv) le méta-ML complet — GBM peu profond sur méta-features out-of-fold — réservé aux contextes à grand K et longue histoire, avec un fait d'expérience pour calibrer les attentes : les gains du non-linéaire documentés par Gu-Kelly-Xiu vivent dans la relation *features → rendements* (§1.2.3), beaucoup moins dans la couche *prédictions → combinaison*, où la structure vraie (des experts positivement corrélés, aux qualités voisines — §3.1.1) est presque linéaire par nature. Le critère d'admission d'un étage est uniforme et non négociable : battre l'étage inférieur en **CV imbriquée purgée** (§3.2.4), *net du turnover des poids* qu'il ajoute (§3.1.4 — la complexité qui fait bouger w se paie en coûts avant de rapporter en IC), l'écart jugé au DSR avec le N de la couche compté au registre. En pratique et pour clore : la plupart des books vivent aux étages (i)+(ii) ; l'étage (iv) est celui dont on parle dans les conférences et qu'on éteint discrètement l'année suivante.

---

Nœud 3.3 passé en ✓✓. Le quatuor : la démonstration out-of-fold (l'overfit se paie au carré sinon) ; w(z) = dictionnaire augmenté (le sujet dégonflé) ; Regret ≤ √((T/2)ln K) et fixed share (la robustesse sans détection) ; le loyer par étage en CV imbriquée nette de turnover. Coutures : NNLS partout (3.2.3 ↔ Breiman) ; fixed share ↔ 2.4.1 (l'alternative au CUSUM) ; η ↔ demi-vie (3.1.3d). Reste **3.4** pour clore la branche 3, puis **1.1** et la **branche 6**. J'enchaîne.

---

## [M123] Humain — 2026-07-24 10:51:39

Ok

---

## [M124] Assistant — 2026-07-24 10:52:41

On clôt la branche 3 en ✓✓ : **3.4 Orthogonalisation & gestion du pool** — l'alpha marginal comme monnaie, désormais avec les formules. Le sous-arbre local :

```
3.4 ORTHOGONALISATION & POOL    gérer la collection, pas seulement la pondérer
│
├── 3.4.1 IC marginal & admission     le test du résidu, le gain en ICIR²
├── 3.4.2 Gram-Schmidt, PCA, HRP      trois géométries du pool
├── 3.4.3 Attribution & incitations   Shapley, la contribution marginale payée
├── 3.4.4 Centralisé vs pods          le même Markowitz, à l'échelle humaine
└── 3.4.5 Combinaison sous coûts      le renvoi Gârleanu-Pedersen (→ 4.3.3)
```

**3.4.1 IC marginal et admission — le test du résidu, quantifié**

Le candidat s_new face au pool {s₁...s_K} : régresser le candidat sur le pool, s_new = Σ b_k·s_k + u, et tester le pouvoir prédictif du **résidu** u. La quantité décidante en forme close : soit ρ_new l'IC standalone du candidat, ρ_pool le vecteur des IC du pool, c le vecteur de ses corrélations au pool ; l'IC du résidu normalisé vaut

> **ρ_⊥ = (ρ_new − c'C⁻¹ρ_pool) / √(1 − c'C⁻¹c)**

— numérateur : ce que le candidat prédit *au-delà* de ce que le pool prédit déjà à travers lui ; dénominateur : la part de variance du candidat que le pool n'explique pas. Le gain systémique s'écrit alors proprement : dans le monde décorrélé après orthogonalisation, l'ICIR² du combiné est additif,

> **ICIR²_combiné = ICIR²_pool + ICIR²(u)**

— la version signaux de la loi d'addition des ratios d'information sur composantes orthogonales (Grinold-Kahn), et la démonstration que le critère d'admission *est* ρ_⊥, pas ρ_new : un candidat à ρ_new = 0,05, c'C⁻¹c = 0,85 apporte moins qu'un ρ_new = 0,02 orthogonal. L'inférence sur ρ_⊥ suit §2.1.1-§3.1.2 (erreur type σ(IC_⊥)/√T, Newey-West), avec le durcissement de sélection de §3.2.4 (le candidat arrive avec un ρ̂ gonflé par sa propre admission en branche 2 — le prior hiérarchique s'applique au *résidu*). Le protocole d'admission complet empile donc : DSR du standalone (§2.3.2), t(ρ_⊥) contre le pool, corrélation maximale plafonnée (c_max ≈ 0,7-0,8 — le garde-fou grossier qui évite de payer l'inférence fine sur des quasi-doublons), et les critères de viabilité (§2.1.4 : c\*, capacité).

**3.4.2 Gram-Schmidt, PCA, clustering — trois géométries pour un pool**

**Gram-Schmidt séquentiel** : s̃_k = résidu de s_k sur {s̃₁...s̃_{k−1}} — chaque signal ne garde que sa nouveauté par rapport aux *précédents*. Vertu : les IC des s̃ sont additifs par construction (3.4.1 itéré) ; vice : la dépendance à l'ordre — l'ancien capte tout le contenu commun, le récent est jugé sur ses miettes ; c'est une *hiérarchie déguisée en algèbre*, défendable seulement si l'ordre encode un vrai prior (ancienneté validée en live, §6.3). **PCA du pool** : diagonaliser C, combiner les portefeuilles propres — mathématiquement propre (directions décorrélées, chacune pondérable par son ICIR propre), mais les vecteurs propres mélangent les familles en objets ininterprétables et *instables* (§4.1.2, les mêmes maux), et un pool piloté en composantes principales ne sait plus répondre à « pourquoi sommes-nous longs ce titre » — le coût de gouvernance excède le gain d'orthogonalité. **Clustering hiérarchique** : distance d_ij = √(2(1−ρ_ij)) (§4.1.4), linkage, coupe du dendrogramme en familles — puis l'allocation récursive du **HRP** de López de Prado (« Building Diversified Portfolios that Outperform Out-of-Sample », JPM 2016) : bissection descendante de l'arbre, variance inverse entre les deux sous-arbres à chaque nœud,

> α_gauche = 1 − Var(gauche)/(Var(gauche)+Var(droite))

— jamais d'inversion de C, seulement sa *topologie* : la robustesse vient de ce qu'on n'estime que ce que l'arbre supporte. Raffinements documentés : Raffinot (« Hierarchical Clustering-Based Asset Allocation », JPM 2017), et la sélection du nombre de clusters par gap statistic. Le verdict pratique, inchangé mais désormais motivé : le clustering gagne parce qu'il épouse la topologie *vraie* du pool (les signaux naissent en familles, §3.1.1) tout en restant lisible — c'est la structure en deux étages de §3.2.3, avec l'arbre estimé plutôt que déclaré ; l'écart entre la taxonomie déclarée et le dendrogramme estimé est d'ailleurs un diagnostic en soi (une « famille » qui se disperse dans l'arbre est mal définie).

**3.4.3 Attribution et incitations — Shapley, ou payer la marginalité**

Le problème : attribuer l'ICIR² (ou le P&L) du combiné à des signaux corrélés — la contribution de k dépend de qui d'autre est dans le pool. L'axiomatique propre est la valeur de **Shapley** (1953) : la moyenne des contributions marginales sur tous les ordres d'arrivée,

> **φ_k = Σ_{S ⊆ Pool∖{k}} [ |S|!·(K−|S|−1)! / K! ] · [ v(S ∪ {k}) − v(S) ]**

avec v(S) = ICIR²(S) — le seul partage satisfaisant efficacité (Σφ_k = v(Pool)), symétrie, et joueur nul ; pour v quadratique (notre cas, ICIR² = ρ'C⁻¹ρ), φ_k admet des formes semi-closes et l'approximation par échantillonnage d'ordres suffit en pratique (le même Shapley que §5.5.2 côté coûts — les deux faces de la même comptabilité). La comparaison éclaire : payer au **standalone** rémunère la corrélation au pool (dix momentum se partagent dix fois le même mérite) ; au **Gram-Schmidt** rémunère l'ancienneté ; au **dernier entrant** (v(Pool) − v(Pool∖k)) sous-paie tout le monde dans un pool redondant (la somme des marginales < v total — le cœur du problème) ; **Shapley** est l'unique point fixe équitable entre ces extrêmes. La conséquence organisationnelle (Tulchinsky, *Finding Alphas*, pour le modèle WorldQuant) : rémunérer à la marginalité oriente la *recherche* — les chercheurs désertent les familles saturées pour les données vierges, l'orthogonalité du pool devient une propriété émergente des incitations ; avec l'effet pervers symétrique à surveiller : la sur-production de signaux exotiques faiblement validés, que le filtre DSR + différé-sur-live de §6.4 contient.

**3.4.4 Centralisé vs pods — le même théorème, à l'échelle humaine**

La bifurcation, désormais formulable dans le langage de la branche : l'usine centralisée résout *un* Markowitz global (netting complet §4.3.4, diversification au niveau des forecasts, un passage de coûts) — c'est l'optimum du monde aux paramètres connus ; les pods résolvent K Markowitz locaux agrégés à la 1/N — le portefeuille de la robustesse (§3.1.1), avec en prime la propriété que l'usine n'a pas : l'**isolation des défaillances humaines** (un pod qui dérive est coupé à ses limites, §4.4.3, sans contaminer le book — le drawdown control appliqué aux personnes). Le coût du modèle pods se chiffre avec les outils de la branche : double comptage des expositions communes (les pods détiennent les mêmes crowded trades — le comomentum de §2.4.2 *intra-firme*, que le netting central partiel et les limites factorielles firm-wide de §4.5.3 viennent plafonner) et frottement de coûts (pas de crossing interne complet). Le critère de choix est celui de 3.1 transposé : l'usine domine si et seulement si l'attribution marginale est *mesurable proprement* (registre §6.2, Shapley §3.4.3, IC marginal §3.4.1) — sans cette infrastructure de mesure, les incitations de l'usine s'effondrent et le 1/N organisationnel gagne, exactement comme le 1/N statistique gagne quand C est inestimable.

**3.4.5 Combinaison sous coûts — le renvoi, et ce qu'il change ici**

Le contenu formel vit en §4.3.3 (Gârleanu-Pedersen) ; ce qui appartient à la branche 3 est sa conséquence sur *l'interface* : l'aim portfolio pondère chaque signal par 1/(1 + φ_k·a/γ) — une fonction de la **liquidité du book** (a) — donc la pondération optimale du pool n'est pas séparable de l'implémentation : deux desks de tailles différentes doivent pondérer différemment le même pool, et la spécification complète d'un alpha transmise à l'aval comprend **(s_k, ρ_k, σ(IC_k), φ_k, τ_k)** — le signal, sa force, sa fiabilité, son decay (§2.1.2), son turnover. Le contrat d'interface de §0.8 s'enrichit sans se rompre : un vecteur passe toujours de la recherche à la mise en œuvre, mais c'est un vecteur d'objets datés et profilés, pas de nombres nus.

---

**La branche 3 est intégralement en ✓✓.** Le quatuor du nœud : ρ_⊥ = (ρ_new − c'C⁻¹ρ_pool)/√(1−c'C⁻¹c) et l'additivité des ICIR² ; le HRP comme structure à deux étages estimée ; Shapley comme unique partage cohérent ; l'interface enrichie (s, ρ, σ(IC), φ, τ). Restent au grain simple : **1.1** (les cinq familles — le plus volumineux, probablement deux messages) et la **branche 6**. On attaque 1.1, ou tu préfères finir par lui ?

---

## [M125] Humain — 2026-07-24 10:52:54

1.1

---

## [M126] Assistant — 2026-07-24 10:54:37

On fore le plus volumineux : **1.1 Familles d'alphas** — la taxonomie complète, au grain ✓✓. Le sous-arbre local :

```
1.1 FAMILLES D'ALPHAS          les cinq gisements, classés par nature de F_t
│
├── 1.1.1 Prix & volumes        momentum, reversal, micro, vol, saisonnalités
├── 1.1.2 Fondamentaux          value, profitabilité, accruals, révisions, carry
├── 1.1.3 Flux & positionnement short interest, indices, gamma, on-chain
├── 1.1.4 Données alternatives  NLP, satellite, transactions, cohortes on-chain
└── 1.1.5 Événementiel          event studies, PEAD, recompositions, unlocks
```

**1.1.1 Prix & volumes — le gisement le plus dense**

Le **momentum cross-sectionnel** : Jegadeesh & Titman (« Returns to Buying Winners and Selling Losers », JF 1993) — trier sur r_{t−252, t−21} (la chirurgie 12-1 de §1.2.1), spread décile ≈ 1%/mois sur l'échantillon d'origine, répliqué sur ~40 marchés et deux siècles (Geczy-Samonov). Son talon : les **momentum crashes** (Daniel & Moskowitz, JFE 2016) — dans les rebonds post-krach, la jambe short (les perdants, devenus des quasi-options sur la survie, à beta conditionnel élevé) explose à la hausse : les pires mois du momentum sont des −40%, concentrés, prévisibles par l'état (marché baissier + vol haute — le conditionnement de §1.2.3 n'est pas optionnel ici, et le momentum résiduel de §1.2.1 en est la chirurgie préventive). Le **time-series momentum** : Moskowitz, Ooi & Pedersen (JFE 2012) — sign(r_{12m}) par instrument, vol-scalé, positif sur 58 futures ; la version continue est le banc multi-échelles AHL (§1.2.2). Le **reversal court terme** : Jegadeesh (JF 1990), Lehmann (QJE 1990) — le rendement à 1 semaine-1 mois prédit négativement ; la lecture économique qui organise tout est Nagel (« Evaporating Liquidity », RFS 2012) : les profits du reversal *sont* la rémunération de la fourniture de liquidité — ils co-varient avec le VIX (le conditionnement canonique de §1.2.3) et le signal propre est le reversal *résiduel* (§1.2.1), miroir en daily de la relaxation d'impact de §5.2.2 (l'encadré « reversal ↔ relaxation » du squelette). La **microstructure** en famille daily : les features agrégées de §1.2.2 (OFI moyen, imbalance de clôture, part du volume en auction) — le pont vers §5.4.2. La **volatilité** : le variance risk premium — VRP_t = IV²_t − E_t[RV²] (implicite moins réalisée anticipée), positif en moyenne (on paie pour l'assurance), prédicteur du marché à quelques mois (Bollerslev, Tauchen & Zhou, RFS 2009) ; et en cross-section le **betting against beta** (Frazzini & Pedersen, JFE 2014) : les contraintes de levier des investisseurs aplatissent la security market line — long low-beta levé / short high-beta délevé, le facteur BAB, avec sa cousine low-vol. Les **saisonnalités** enfin : Heston & Sadka (JFE 2008) — le rendement d'un titre au même mois calendaire des années passées prédit (une périodicité à 12 mois dans le cross-section) ; et la décomposition overnight/intraday de §1.2.2 comme saisonnalité intra-journalière structurelle.

**1.1.2 Fondamentaux — la comptabilité comme F_t**

Le **value** : E/P, B/P, FCF yield, standardisés within-secteur (§1.2.1) — le facteur HML de Fama-French (JFE 1993), avec l'avertissement de §2.4.3 : son rendement historique se décompose en carry structurel + revalorisation, et le test honnête est net de revalorisation. La **profitabilité** : Novy-Marx (« The Other Side of Value », JFE 2013) — la gross profitability (revenus − COGS)/actifs prédit autant que le value en étant *négativement* corrélée à lui (l'orthogonalité de §3.4.1, offerte par la nature) ; institutionnalisée en RMW dans le cinq-facteurs (Fama-French, JFE 2015). Les **accruals** : Sloan (« Do Stock Prices Fully Reflect Information in Accruals and Cash Flows? », TAR 1996) —

> accruals = (ΔActif circulant − ΔCash) − (ΔPassif circulant − ΔDette CT − ΔImpôts dus) − Dotations

— la part *non-cash* du résultat ; élevée, elle prédit négativement (le marché sur-évalue les bénéfices de faible qualité comptable) : l'anomalie qui a fondé la quality investing, et le cas d'école du vintage (§1.2.4 : les restatements réécrivent précisément ces lignes). Les **révisions** : le changement du consensus (§1.2.1, changements vs niveaux) et le PEAD qui vit en 1.1.5. Le **carry**, généralisé : Koijen, Moskowitz, Pedersen & Vrugt (« Carry », JFE 2018) — définition unifiée : *le rendement si les prix ne bougent pas*,

> **C_t = (S_t − F_t) / F_t**

(la base spot-future : dividendes-taux en equity index, différentiel de taux en FX, convenience yield en commodities), prédictif dans *toutes* les classes d'actifs — et en crypto, le funding des perps en est l'incarnation la plus pure : observable en temps réel, réglé toutes les 8h, sans estimation (§1.4.1 : il est déjà dans la cible si elle est bien construite — le signal et la cible doivent se partager le funding sans double compte).

**1.1.3 Flux & positionnement — la demande comme information**

Le fondement théorique qui a changé d'échelle : les courbes de demande des actifs sont *inélastiques* — Gabaix & Koijen (« In Search of the Origins of Financial Fluctuations: The Inelastic Markets Hypothesis », 2021) estiment qu'un dollar de flux entrant dans le marché actions agrégé déplace la capitalisation d'environ **cinq dollars** (multiplicateur ~5, contre ~0 dans le monde sans frictions) — les flux non informés déplacent les prix, durablement, et les prévoir est un alpha à part entière. Les instances : le **short interest** — Rapach, Ringgenberg & Zhou (JFE 2016) : l'agrégat est l'un des meilleurs prédicteurs du marché ; en cross-section, le niveau, le delta (§1.2.1), les days-to-cover, et le *coût d'emprunt* qui à la fois signale et ampute (Drechsler-Drechsler, §2.1.3) ; les **flux de fonds** — Coval & Stafford (« Asset Fire Sales », JFE 2007) : les rachats forcent des ventes prévisibles dans les positions concentrées des fonds en décollecte (pression puis réversion — le profil type du flux non informé), généralisé par Lou (RFS 2012) en flow-induced trading ; les **recompositions d'indices** (le versant flux de 1.1.5) ; le **dealer gamma** — le positionnement optionnel agrégé des market makers : gamma net positif ⟹ leurs hedges *contrarient* le marché (amortisseur), négatif ⟹ ils l'amplifient — cartographiable depuis l'open interest optionnel, largement praticien (les flux vanna/charm autour des expirations, la littérature étant surtout de recherche broker) ; le **COT** sur futures (positionnement commercials/non-commercials, contrarian aux extrêmes) ; et côté crypto les **flux d'exchanges** on-chain (net inflows = pression de vente latente, §1.1.4 pour la mesure) et le funding comme positionnement spéculatif en temps réel (§1.2.3, le conditionneur naturel).

**1.1.4 Données alternatives — l'information avant qu'elle soit un prix**

Le **NLP** : la fondation est lexicale — Loughran & McDonald (« When Is a Liability Not a Liability? », JF 2011) : les dictionnaires génériques classent mal le langage financier (« liability » n'est pas négatif dans un 10-K), d'où leurs lexiques spécifiques, standard de l'industrie ; Tetlock (JF 2007) avait établi le lien pessimisme médiatique → rendements ; la génération moderne (embeddings, LLM) extrait le ton des earnings calls, la similarité des filings (le *changement* de langage d'un 10-K à l'autre prédit — encore §1.2.1), la nouveauté d'une news — avec le piège point-in-time propre : le modèle de langage lui-même a une date d'entraînement, et scorer 2015 avec un modèle de 2024 est un look-ahead sémantique (§1.2.4, version NLP). Le **satellite et le physique** : comptage de parkings pour les retailers (Katona et al. — l'imagerie prédit les surprises de revenus), réservoirs pétroliers, shipping AIS — la famille où l'avantage est le *délai* (savoir avant la publication) et le coût d'entrée la barrière. Les **transactions consommateurs** (cartes, e-mails de reçus) : prédire le chiffre d'affaires trimestriel avant l'annonce — le PEAD de 1.1.5 pris à revers. La dynamique économique commune, documentée : l'alpha d'un jeu de données décroît avec sa *commercialisation* — le McLean-Pontiff des données (§2.4.2) : le vendeur qui démarche dix fonds a déjà distribué l'érosion ; d'où la prime au *sourcing* propriétaire et au nettoyage différencié (§6.1, build vs buy). Les **cohortes on-chain** enfin, avec leurs définitions :

> **MVRV = market cap / realized cap**,  realized cap = Σ (coins × prix de leur *dernier* mouvement)
> **SOPR = valeur réalisée à la vente / valeur payée à l'achat** (par coins dépensés, agrégé)

— MVRV est un prix/coût-de-base agrégé (extrêmes = euphorie/capitulation), SOPR < 1 signale des ventes à perte (capitulation en cours) ; les deux portent le piège de vintage établi en §1.2.4 (le clustering des wallets est recalculé rétroactivement).

**1.1.5 Événementiel — le breadth par la répétition**

Le formalisme commun (MacKinlay, « Event Studies in Economics and Finance », JEL 1997) : en temps d'événement τ, le rendement anormal AR_{i,τ} = r_{i,τ} − E[r_{i,τ}|F] (le benchmark : modèle de marché ou facteurs, §2.1.5), cumulé en **CAR(τ₁,τ₂) = Σ AR** — la courbe de CAR moyenne est la signature de l'événement (saut à l'annonce = efficience ; dérive post-annonce = sous-réaction exploitable), et l'inférence se fait en coupe d'événements (le breadth vient de la répétition, §1.1 intro). L'instance canonique : le **PEAD** — Bernard & Thomas (« Post-Earnings-Announcement Drift », JAR 1989) : après une surprise (le SUE de §1.2.1), la dérive se poursuit ~60 jours dans le sens de la surprise, avec la structure d'autocorrélation saisonnière des surprises elles-mêmes (le marché naïf extrapole mal la saisonnalité des bénéfices) — l'anomalie la plus documentée de la littérature, érodée mais vivante en small caps. Les **recompositions d'indices** : l'inclusion achète, l'exclusion vend, mécaniquement et en taille connue (Shleifer 1986, Harris & Gurel 1986 pour le S&P ; la reconstitution Russell de juin comme événement le plus prévisible du calendrier) — le double statut de la famille : signal (front-runner la demande) et coût (les flux indiciels *sont* le §1.1.3), avec la date d'*annonce* vs date d'*effet* comme structure temporelle exploitable et comme piège de timeline (§2.2.2). Les **expirations optionnelles** : le pinning autour des strikes à fort open interest — le dealer gamma de §1.1.3 concentré dans le calendrier. Et le versant **crypto**, où le calendrier est public et on-chain : les **unlocks** (les cliffs de vesting libèrent une offre connue à date connue — l'offre prévisible rencontre la demande inélastique de Gabaix-Koijen : pression avant/pendant, mesurable en % du float débloqué), les **listings** (l'inclusion version exchange : pump à l'annonce Binance, fade documenté ensuite — l'event study se réplique tel quel), airdrops et forks — chacun avec sa courbe de CAR type et son érosion par publication (§2.4.2 : les calendriers d'unlocks sont désormais des produits de données — le McLean-Pontiff y opère en années, pas en décennies).

---

**La branche 1 est intégralement en ✓✓** — familles, features, normalisation, cibles. Le fil du nœud : chaque famille a son *mécanisme de persistance* (§2.4.3 — crash risk pour le momentum, liquidité pour le reversal, contraintes de levier pour BAB, inélasticité pour les flux, limites d'arbitrage pour le PEAD) et c'est lui, pas le t-stat, qui fonde l'admission au pool. Il ne reste plus qu'un chantier au grain simple : **la branche 6** (quatre nœuds). On la passe en ✓✓ et l'arbre entier sera uniforme.

---

## [M127] Humain — 2026-07-24 10:55:10

Réécris 1.1 en donnant plus de formules et descriptions mathématiques

---

## [M128] Assistant — 2026-07-24 10:56:42

Version révisée, au formalisme aligné sur le reste des ✓✓ — elle remplace la précédente dans le corpus :

```
1.1 FAMILLES D'ALPHAS          les cinq gisements, classés par nature de F_t
│
├── 1.1.1 Prix & volumes        momentum, reversal, micro, vol, saisonnalités
├── 1.1.2 Fondamentaux          value, profitabilité, accruals, révisions, carry
├── 1.1.3 Flux & positionnement inélasticité, short interest, gamma, on-chain
├── 1.1.4 Données alternatives  NLP, satellite, transactions, cohortes on-chain
└── 1.1.5 Événementiel          AR/CAR, PEAD, recompositions, unlocks
```

**1.1.1 Prix & volumes**

Le **momentum cross-sectionnel** (Jegadeesh-Titman, JF 1993) : la caractéristique canonique est

> MOM_i = P_{i,t−21}/P_{i,t−252} − 1,  puis z-score cross-sectionnel (§1.3.1)

— le skip-month excluant la zone de reversal (§1.2.1). Son risque de queue est *conditionnel* : Daniel & Moskowitz (JFE 2016) montrent que le beta de la jambe perdante explose en marché baissier (les perdants deviennent des options sur la survie), et dérivent le remède en forme close — le momentum dynamique pondéré par son propre ratio moyenne/variance conditionnel,

> **w\*_t = (1/2λ)·μ̂_{MOM,t}/σ̂²_{MOM,t}**

avec μ̂ prédit par l'état (indicateur bear × vol) et σ̂² par GARCH — qui double environ le Sharpe en amputant les crashes : le conditionnement de §1.2.3 avec ses paramètres. Le **time-series momentum** (Moskowitz-Ooi-Pedersen, JFE 2012) : position_i,t = sign(r_{i,t−252:t})·σ\*/σ̂_{i,t} — le vol-scaling est constitutif du résultat ; la version continue est le banc AHL de §1.2.2, x_k = (EMA_{S_k} − EMA_{L_k})/σ_P passé dans R(x) = x·e^{−x²/4}. Le **reversal** : REV_i = −ε_{i,t−5:t} (le résidu factoriel de la semaine, §1.2.1), avec la loi de Nagel (RFS 2012) : E[profits du reversal] ≈ a + b·VIX_t, b > 0 — la rémunération de la liquidité est proportionnelle au prix du risque de la porter ; miroir daily de la relaxation de §5.2.2. La **microstructure agrégée** en features quotidiennes : l'illiquidité d'Amihud ILLIQ_i = (1/D)·Σ_d |r_{i,d}|/Vol$_{i,d} (à la fois prime et conditionneur), l'OFI moyen, l'imbalance de clôture. La **volatilité** : le variance risk premium VRP_t = IV²_t − E_t[RV²_{t→t+21}] (implicite moins réalisée prévue), positif en moyenne — le prix de l'assurance — et prédicteur du marché : r_{t→t+h} = a + b·VRP_t avec R² maximal vers h ≈ 3-6 mois (Bollerslev-Tauchen-Zhou, RFS 2009). Le **betting-against-beta** (Frazzini-Pedersen, JFE 2014) : le facteur auto-financé et beta-neutre

> **BAB_t = (1/β_L)·(r_L − r_f) − (1/β_H)·(r_H − r_f)**,  β̃_i = 0,6·β̂_i + 0,4

(le shrinkage de Vasicek de §4.1.4, dans la définition même du facteur) — long low-beta levé, short high-beta délevé : la prime des contraintes de levier. Les **saisonnalités** (Heston-Sadka, JFE 2008) : s_i = (1/K)·Σ_k r_{i, même mois, année t−k} — la moyenne des rendements aux mêmes mois calendaires passés prédit positivement, une raie spectrale à 12 mois dans le cross-section.

**1.1.2 Fondamentaux**

Le **value** : composite z de {E/P, B/P, CF/P} within-secteur (§1.2.1, §1.3.1) ; la construction factorielle de référence (Fama-French, JFE 1993) est le double tri 2×3,

> HML = ½(SV + BV) − ½(SG + BG)

— la neutralisation de taille par construction, l'ancêtre artisanal du §1.3.3. La **profitabilité** (Novy-Marx, JFE 2013) : GP_i = (Revenus − COGS)/Actifs — corr(GP, B/P) < 0 en coupe : l'orthogonalité au value est native (§3.4.1), d'où RMW au cinq-facteurs. Les **accruals** (Sloan, TAR 1996) :

> ACC_i = [(ΔCA − ΔCash) − (ΔPC − ΔDette_CT − ΔImpôts_dus) − Dotations] / Actifs_moyens

— la part non-cash du résultat, prédicteur *négatif* (spread décile ~10%/an sur l'échantillon d'origine) : le résultat comptable se décompose en cash-flow + accruals, et le marché tarife mal la persistance inférieure du second terme. Les **révisions** : REV_i = Δ(consensus EPS)/P_i (ou /σ_i) — le changement, pas le niveau (§1.2.1). Le **carry** unifié (Koijen-Moskowitz-Pedersen-Vrugt, JFE 2018) :

> **C_i = (S_i − F_i)/F_i** = le rendement à prix spot inchangé

— en equity index C ≈ (q − r_f)/(1+r_f) (dividendes moins taux), en FX le différentiel de taux, en commodities la convenience yield nette ; prédictif partout avec des t > 3 en coupe globale. En crypto : le funding annualisé d'un perp, C = E[funding]×1095 (3 règlements/jour ×365), est un carry *observé* — zéro estimation, la version la plus pure de la famille, avec la discipline de non-double-compte de §1.4.1 (le funding vit dans la cible *ou* dans le signal selon la construction, jamais les deux).

**1.1.3 Flux & positionnement**

Le fondement quantitatif (Gabaix-Koijen, 2021) : l'hypothèse des marchés inélastiques,

> **ΔP/P ≈ M·f**,  f = flux net / capitalisation,  **M ≈ 5**

— un multiplicateur macro d'ordre 5 (contre M → 0 en marché parfaitement élastique), estimé par identification granulaire ; en coupe micro, l'élasticité par titre est plus grande mais finie — le pont avec l'impact de §5.2 (la loi en racine est la version métaordre du même fait). Les instances mesurables : le **short interest** — SIR_i = actions vendues à découvert / flottant, DTC_i = SI/ADV ; en agrégé, Rapach-Ringgenberg-Zhou (JFE 2016) : r_{mkt,t→t+1} = a − b·SII_t (l'agrégat détrendé), l'un des R² out-of-sample les plus élevés de la littérature de prédiction du marché ; en coupe, niveau et Δ, avec le fee d'emprunt qui ampute (§2.1.3). Les **fire sales** (Coval-Stafford, JFE 2007) : la pression par titre

> PRESSURE_i,t = Σ_{j : flux_j < percentile 10} ventes forcées_{j,i} / Vol_i

— les fonds en décollecte extrême vendent leurs positions communes : baisse pendant, réversion complète en ~12-18 mois, le profil type du flux non informé. Le **dealer gamma** : l'exposition agrégée

> **GEX = Σ_options OI·Γ·S²·(±1 selon le côté dealer présumé)**

— gamma net positif ⟹ le hedging vend les hausses et achète les baisses (flux ∝ −Γ_net·ΔS : amortisseur, vol réalisée comprimée) ; négatif ⟹ amplificateur — un conditionneur de régime intraday plus qu'un signal directionnel. Le **COT** : l'index de positionnement (net_t − min₃ₐ)/(max₃ₐ − min₃ₐ), contrarian aux extrêmes. Et l'**on-chain** : netflow_exchanges/float comme pression latente — la mesure vivant en 1.1.4, le mécanisme étant Gabaix-Koijen appliqué à un actif à flottant fin.

**1.1.4 Données alternatives**

Le **NLP** : la mesure lexicale de base (Loughran-McDonald, JF 2011, dictionnaires financiers) :

> TONE_d = (N_pos − N_neg)/(N_pos + N_neg),  pondération tf-idf des termes

— et le signal le plus robuste de la famille n'est pas le ton mais le *changement* : Cohen-Malloy-Nguyen (« Lazy Prices », JF 2020) — la similarité cosinus entre filings successifs,

> sim(d_t, d_{t−1}) = ⟨x_t, x_{t−1}⟩ / (‖x_t‖·‖x_{t−1}‖)

(x = vecteurs tf-idf) : les sociétés qui *réécrivent* leur 10-K sous-performent — le marché ne lit pas les diffs ; §1.2.1 (changements vs niveaux) appliqué au langage. Piège propre à la génération LLM : le look-ahead sémantique (§1.2.4) — scorer 2015 avec un embedding entraîné en 2024 injecte du futur par le vocabulaire. Le **physique** (satellite, AIS) : la forme générique est la régression de nowcasting, Revenus_q = a + b·(comptage physique_q) + e, dont le résidu de consensus fait un SUE anticipé (§1.1.5 pris à revers) ; l'edge est le délai, le coût d'entrée la barrière. Les **transactions** : même structure, panel de cartes → CA trimestriel. La dynamique d'érosion commune : α(t) = α₀·e^{−t/T_commercialisation} — le McLean-Pontiff des données (§2.4.2), T se comptant en années depuis la mise en vente. L'**on-chain par cohortes** :

> **MVRV = MC / RC**,  RC = Σ_coins (quantité × prix du dernier mouvement)
> **SOPR = Σ valeur au spend / Σ valeur à l'acquisition** (coins dépensés du jour)

— MVRV est un P/coût-de-base agrégé (z-score long comme signal de cycle, §1.3.2), SOPR < 1 = ventes à perte en cours (capitulation) ; les deux sous le piège de vintage du §1.2.4 (clustering recalculé rétroactivement).

**1.1.5 Événementiel**

Le formalisme (MacKinlay, JEL 1997) : en temps d'événement τ,

> AR_{i,τ} = r_{i,τ} − (α̂_i + β̂_i·r_{m,τ}),  **CAR_i(τ₁,τ₂) = Σ_{τ₁}^{τ₂} AR_{i,τ}**,  t = CAR̄ / (σ_AR·√L·√(1/n))

— l'inférence en coupe d'événements (n événements, fenêtre de L jours), le breadth par répétition ; la courbe de CAR moyenne est la signature (saut sec = efficience ; dérive = sous-réaction). L'instance canonique, le **PEAD** (Bernard-Thomas, JAR 1989) : après SUE_i = (E_i − Ê_i)/σ_i(surprise) (§1.2.1), CAR(+2, +60) ≈ +2% pour le décile haut vs bas — et la structure fine : les surprises sont *autocorrélées saisonnièrement* (corr(SUE_q, SUE_{q−4}) > 0), le marché extrapolant mal la composante saisonnière des bénéfices. Les **recompositions d'indices** : la demande mécanique se chiffre, Q_i = Δw_{i,index}·AUM_indexé, et l'impact attendu passe par la loi en racine (§5.2.1) : I ≈ Y·σ_i·√(Q_i/ADV_i) — le signal (front-run entre annonce et effet, réversion après) et le coût (§1.1.3) dans la même formule ; la timeline annonce/effet comme piège de §2.2.2. Le **pinning** d'expiration : P(clôture au strike de max OI) excède le hasard — le GEX de 1.1.3 concentré dans le calendrier. Et le **crypto** : les unlocks — ratio u = tokens libérés/float, impact attendu par la même racine carrée avec l'ADV *nettoyé* (§2.2.5), CAR type négatif de l'annonce à l'effet ; les listings (event study de l'inclusion, version exchange) ; l'érosion par publication des calendriers en années (§2.4.2).

---

Le fil inchangé, désormais outillé : chaque famille porte son mécanisme de persistance *et* sa formule de construction — c'est le couple (mécanisme, formule) qui entre au registre comme hypothèse pré-spécifiée (§2.3.5). Reste la **branche 6** pour uniformiser l'arbre entier en ✓✓.

---

## [M129] Humain — 2026-07-24 10:57:14

Continue.

---

## [M130] Assistant — 2026-07-24 10:58:23

On uniformise l'arbre : **la branche 6 en ✓✓** — la moins mathématique, mais pas sans formules : c'est la branche où l'épistémologie des cinq autres devient exécutable. Le sous-arbre local :

```
6. INFRA & ORGANISATION        l'honnêteté statistique, déléguée aux systèmes
│
├── 6.1 Données                 bitemporel, append-only, qualité quantifiée
├── 6.2 Moteur de backtest      parité, replay, placebo, registre → N_eff
├── 6.3 Production              SPRT, PSI, kill switches, réconciliation
└── 6.4 Organisation            incitations formalisées, usine vs pods
```

**6.1 Données — le bitemporel, avec sa sémantique exacte**

Le schéma (Snodgrass, 1999) : chaque ligne porte (event_time **e**, knowledge_time **k**, k_fin) — k_fin étant le knowledge_time de la version qui la remplace (+∞ pour la version courante). La requête « telle que la base était en t », qui *implémente* F_t (§0.2) :

> **AS-OF(t) : { lignes | e ≤ t, k ≤ t < k_fin }**

— et le test de cohérence fondamental du système : AS-OF(t) exécutée aujourd'hui doit être *invariante* dans le temps (une base append-only la garantit par construction ; toute mutation en place la casse silencieusement). La qualité se quantifie avec les outils qu'on possède déjà, retournés vers les données elles-mêmes : **fraîcheur** — pour chaque flux f, le retard d_f,t = now − max(k) comparé à sa distribution historique, alerte si z(d) > 3 ; **cohérence** — prix cross-venues dans une bande |p_v/p_médian − 1| < seuil(σ_i), volumes en z-score contre leur EWMA (§1.2.2) ; **intégrité statistique** — les tests anti-wash-trading de §2.2.5 (Benford sur premiers chiffres : fréquence attendue log₁₀(1+1/d), sur-représentation des tailles rondes) appliqués en *continu* comme contrôle qualité, pas seulement en nettoyage initial. La **quarantaine** est un état du pipeline, pas une opinion : une ligne qui échoue un contrôle porte un flag qui la rend invisible aux AS-OF de production jusqu'à arbitrage — le faux prix ne devient jamais un vrai trade. Build vs buy, le critère inchangé, avec son test : la vérifiabilité PIT d'un vendeur se mesure en comparant ses « vintages » livrés à vos propres captures archivées — l'écart est son taux de réécriture, et il se chiffre avant de signer.

**6.2 Moteur de backtest — la parité, certifiée par le placebo**

Les invariants, désormais tous outillés. La **parité** : un seul artefact de code pour le calcul du signal, appelé par les deux mondes — la propriété testable étant signal_backtest(t, AS-OF(t)) ≡ signal_prod(t) au bit près, vérifiée en continu sur la fenêtre récente (le **replay quotidien** : rejouer hier avec le snapshot d'hier, comparer à ce que la prod a réellement calculé — l'écart est un bug *ou* une donnée réécrite, et 6.1 dit lequel). Le **placebo** de §2.2.5, promu en certification chiffrée du protocole : sur M signaux aléatoires passés dans le pipeline complet,

> **IC̄_placebo ≈ 0 ± 1/√(N_eff−1)** (§2.1.1),  Sharpe_net,placebo ≈ −coûts×turnover

— tout excès mesure la fuite résiduelle du protocole *en unités d'IC* ; c'est l'étalonnage du plancher de §2.1.1 et le test de non-régression qu'on relance à chaque modification du moteur. Le **registre** enfin, avec sa fonction statistique explicite : chaque essai loggé (hypothèse pré-datée, config, hash des données AS-OF, résultat) alimente le calcul du N effectif du DSR (§2.3.2) —

> N_eff ≈ 1 + (N−1)·(1−ρ̄),  ρ̄ = corrélation moyenne des trajectoires de P&L des essais de la famille

— incalculable sans les trajectoires archivées ; et le **holdout administré** : données scellées par hash, ouverture unique journalisée — la traduction système du théorème de Dwork (§2.3.5 : chaque requête adaptative consomme la validité en √(nombre de requêtes) ; l'administration rend le compteur *matériel*). Références : Carver, *Systematic Trading* (l'architecture à l'échelle d'un desk) ; AFML pour le protocole ; §2.2-2.3 pour tout ce que ce moteur exécute.

**6.3 Production — la surveillance, aux bons seuils**

La promotion à portes avec ses critères pré-enregistrés, et l'outil séquentiel propre : le **SPRT de Wald** (1945) sur la série des IC live — tester H₀ : IC = IC_backtest contre H₁ : IC = 0 par le log-rapport de vraisemblance cumulé,

> **Λ_T = Σ_t ln[ f₁(IC_t)/f₀(IC_t) ] = (T/σ²(IC))·[ (IC₀²/2) − IC₀·ĪC_T ]** (cas gaussien),
> continuer tant que ln(β/(1−α)) < Λ_T < ln((1−β)/α)

— le test qui *minimise le temps de décision espéré* à erreurs (α, β) données, et dont les bornes disent l'essentiel : avec IC₀ = 0,03 et σ(IC) = 0,15, distinguer « vivant » de « mort » à α = β = 10% demande E[T] de l'ordre de **grandes centaines de jours** — la quantification définitive du « six mois ne prouvent rien » de la version courte, et la justification du bucket-avec-hystérésis (§3.1.3c) comme décision sous test inachevé. La dérive de population se mesure au **PSI** (population stability index, l'outil des credit scorers) : pour chaque feature, distribution live q vs référence p sur B buckets,

> **PSI = Σ_b (q_b − p_b)·ln(q_b/p_b)**  — seuils praticiens : < 0,1 stable, 0,1-0,25 à surveiller, > 0,25 drift majeur

— la divergence de Jeffreys entre hier et aujourd'hui, feature par feature : le signal peut mourir *par ses entrées* avant de mourir par son IC, et le PSI le voit des mois plus tôt. Les kill switches gardent leur gradation (§4.4.3, §6.3 v1), la réconciliation son identité comptable vérifiée ligne à ligne — Position_t = Position_{t−1} + fills_t (vs broker), P&L_t = Σ w·r − coûts (vs custodian) — et le tableau de bord agrège désormais tout ce que l'arbre a produit comme instruments : IC live avec bandes SPRT, PSI par feature, comomentum par sleeve (§2.4.2), bias statistic du modèle de risque (§4.1.1), surprises de coût (§5.5.3), turnover des poids (§3.2.4). La surveillance n'est pas une liste de chiffres : c'est la branche 2 exécutée en continu sur le présent.

**6.4 Organisation — les incitations, écrites comme des contrats**

Le problème principal-agent, formalisé a minima : un chercheur rémunéré R = f(performance mesurée) optimise f, pas la performance vraie — et chaque f naïve a son exploit documenté par l'arbre lui-même : f(Sharpe backtest) ⟹ maximiser N jusqu'au Sharpe demandé (E[max_N] ≈ √(2 ln N), §2.3.2 — l'overfitting est la *réponse rationnelle* au contrat) ; f(Sharpe standalone live) ⟹ répliquer le pool (le mérite corrélé compté K fois, §3.4.3) ; f(P&L attribué) ⟹ importer les biais de §5.5.2. Le contrat robuste combine les correctifs déjà construits : assiette = **contribution marginale** (Shapley §3.4.3, ou ρ_⊥ §3.4.1 en approximation), déflatée du N du registre (le DSR *dans* la formule de bonus — le chercheur paie ses propres essais), et **différée sur le live** — R_t = part immédiate + part indexée sur les années live suivantes, ce qui aligne l'horizon du chercheur sur la demi-vie réelle de ses signaux (§2.1.2) et rend l'overfitting non rentable en espérance : la version incitative du fractional Kelly — réduire la part payée sur l'estimé, proportionnellement à son incertitude. L'arbitrage usine/pods garde sa formulation (§3.4.4) avec le critère rendu opérationnel : l'usine exige que la chaîne de mesure (registre → N_eff → ρ_⊥ → Shapley → différé) soit *auditable de bout en bout* — c'est une exigence d'infrastructure, pas de culture ; les pods sont ce qu'on choisit quand on ne peut pas la construire. Et la mémoire du desk ferme l'arbre sur lui-même : l'archive des négatifs (le N des familles, §1.2.3), la documentation par signal — le quintuple de l'interface (s, ρ, σ(IC), φ, τ, §3.4.5) *plus* le mécanisme de persistance (§2.4.3, §1.1) et le comportement attendu par régime — c'est-à-dire exactement ce qu'il faut pour qu'un autre que l'auteur décide en crise, et pour que le comité de revue (§3.1.3c) juge sur pièces.

---

**L'arbre est intégralement en ✓✓.** Sections 0 à 6, familles, features, cibles, évaluation, combinaison, portefeuille, exécution, infra — tout est au grain formules + références, avec les quatre encadrés transversaux nourris en route. Le squelette v2 mérite sa v3 (les ✓✓ partout, les pivots ajoutés : ρ_⊥, SPRT, PSI, Shapley, la loi de Nagel, Gabaix-Koijen M ≈ 5, Daniel-Moskowitz...) — dis-le et je la génère ; ensuite le dossier complet part chez Claude Code pour l'industrialisation : harmonisation, vérification des sources, compilation PDF. Le forage créatif, lui, est terminé.

---

## [M131] Humain — 2026-07-24 10:59:00

Génère la v3

---

## [M132] Assistant — 2026-07-24 11:01:07

> *[Outil : bash_tool — Générer le squelette v3 : grain ✓✓ uniforme, pivots des derniers forages, encadré E, renvois enrichis]*

> *[Outil : present_files — /mnt/user-data/outputs/arbre_alpha_squelette_v3.md]*

La v3 est gelée — l'état final de l'arbre. Ce qui change par rapport à la v2 :

**Grain uniforme.** Plus de distinction ✓/✓✓ : chaque nœud de l'arbre porte désormais ses formules-pivots dans le squelette lui-même — ρ_⊥ et l'additivité des ICIR², le SPRT et le PSI, la loi de Nagel, le M ≈ 5 de Gabaix-Koijen, le momentum dynamique de Daniel-Moskowitz, les −26%/−58% de McLean-Pontiff, AS-OF(t) comme implémentation de F_t...

**Un cinquième encadré.** « La surveillance séquentielle » (CUSUM, SPRT, hystérésis, fixed share) a émergé des derniers forages comme un fil transversal à part entière — détecter coûte du délai, la réponse rationnelle est graduelle. Et l'encadré A est passé de six à huit habits du shrinkage, le différé incitatif de 6.4 étant le dernier.

**Le renvoi maître.** La trajectoire de φ — mesuré en 2.1.2, consommé en 4.3.3 et 5.3.3, transporté par l'interface, documenté en 6.4 — est promue en tête des renvois : c'est le paramètre qui coud les deux moitiés de l'arbre.

Le dossier Claude Code est maintenant complet : ce squelette v3 comme contrat, le CLAUDE.md comme protocole, la section 0 comme étalon, et l'export du chat comme corpus — n'oublie pas que le transcript .txt s'arrête à mi-conversation, tout le forage des branches 2 à 6 et la révision de 1.1 ne vivent que dans l'export claude.ai. Le forage créatif est clos ; place à l'industrialisation.

---

## [M133] Humain — 2026-07-24 11:03:06

Comment j exporte l intégralité de ce chat ?

---

## [M134] Assistant — 2026-07-24 11:03:26

> *[Outil : web_search — claude.ai export data conversations support]*

Deux précisions importantes après vérification, car tu es sur mobile :

**L'export officiel ne se fait pas depuis l'app mobile.** L'export des données est accessible depuis Paramètres → Confidentialité sur l'app web ou Claude Desktop — il n'est pas possible de le lancer depuis Claude pour iOS ou Android. Il faut donc te connecter à claude.ai depuis un navigateur d'ordinateur, puis : cliquer sur tes initiales en bas à gauche, ouvrir « Settings », aller dans la section « Privacy », cliquer sur « Export data » — et une fois l'export traité, tu reçois un lien de téléchargement par e-mail.

**Le format de sortie est du JSON brut.** Le téléchargement est un ZIP de fichiers JSON — un tableau où chaque élément est une conversation complète avec ses messages horodatés. Ce n'est pas lisible tel quel pour un humain, mais c'est en réalité *idéal* pour notre usage : Claude Code parsera le `conversations.json` sans difficulté — il suffira d'ajouter une ligne au CLAUDE.md du type « extraire de conversations.json la conversation intitulée [le titre de ce chat] et la convertir en markdown dans transcripts/ » — et le JSON préserve tout, y compris l'ordre exact des messages et les artefacts.

Alternative légère si tu veux éviter l'export complet : ouvrir cette conversation sur claude.ai en desktop et copier son contenu manuellement (Ctrl+A ou via les boutons de copie par message) dans un fichier texte. Fonctionnel, mais pour ~60 messages dont beaucoup très longs, l'export officiel est plus fiable et exhaustif.

Le chemin complet, donc : desktop → Settings → Privacy → Export data → e-mail → dézipper dans le dossier du projet à côté du squelette v3, du CLAUDE.md et de la section 0 → lancer Claude Code avec « Lis CLAUDE.md, extrais la conversation source de conversations.json, puis exécute la session 1 ».

---

## [M135] Humain — 2026-07-24 11:05:27

Quels fichiers je donne dans le projet ?

---

## [M136] Assistant — 2026-07-24 11:05:41

Le dossier minimal, cinq pièces :

1. **`arbre_alpha_squelette_v3.md`** — le contrat. C'est la seule version à donner : les v1 et v2 sont obsolètes, ne les mets pas (deux squelettes concurrents = conflits garantis).
2. **`CLAUDE.md`** — le protocole de production. ⚠️ Il référence `squelette_v2.md` et `section_0.md` : soit tu renommes les fichiers en conséquence, soit tu corriges les deux références dans CLAUDE.md vers `arbre_alpha_squelette_v3.md` et le nom réel du fichier section 0 — et ajoute la ligne : « Session 1 : extraire de `conversations.json` la conversation source [titre de ce chat] et la convertir en markdown dans `transcripts/` ».
3. **`section_0_cadre_et_conventions.md`** — l'étalon de grain et la source du futur NOTATION.md.
4. **`conversations.json`** (dézippé de l'export) — le corpus intégral. C'est lui qui contient tout le forage des branches 2-6, la révision de 1.1, et les échanges pédagogiques (IC, Spearman, demi-vie, turnover) qui méritent d'être versés au livre.
5. **`transcript_chat_alphas.txt`** — optionnel puisque redondant avec le JSON, mais utile comme échantillon de conversion lisible ; range-le dans `transcripts/` si tu le gardes.

Ne donne pas le CLAUDE.md à la racine d'un dossier fourre-tout : crée un répertoire propre dédié au projet, avec juste ces fichiers — Claude Code lit le CLAUDE.md du répertoire où il est lancé, et un environnement minimal évite qu'il se disperse.

Premier prompt une fois dedans : « Lis CLAUDE.md et exécute la session 1 ». La session 1 initialisera le reste (arborescence par nœud, NOTATION.md, STYLE.md, AVANCEMENT.md) — tout est spécifié dans le protocole.

---

## [M137] Humain — 2026-07-24 11:07:45

Redonne moi les fichiers 1 à 4 amendés ici

---

## [M138] Assistant — 2026-07-24 11:08:32

> *[Outil : bash_tool — Réécrire CLAUDE.md amendé (références v3, extraction du JSON, index corpus, encadré E)]*

> *[Outil : present_files — /mnt/user-data/outputs/CLAUDE.md, /mnt/user-data/outputs/arbre_alpha_squelette_v3.md, /mnt/user-data/outputs/section_0_cadre_et_conventions.md, /mnt/user-data/outputs/transcript_chat_alphas.txt]*

Les quatre fichiers, avec un point d'honnêteté sur le n°4.

**1. `arbre_alpha_squelette_v3.md`** — inchangé (il était déjà final). C'est le contrat.

**2. `CLAUDE.md`** — amendé en profondeur : références corrigées vers la v3 et le vrai nom du fichier section 0 ; session 1 réécrite avec l'extraction depuis `conversations.json` *et* la construction d'un index corpus → squelette (avec les points d'attention critiques : les deux versions de 1.1 dont la seconde fait foi, la localisation du matériau des branches 2-6 dans la seconde moitié, les échanges pédagogiques à verser en §0) ; 5 encadrés au lieu de 4 ; et la clarification que le transcript partiel ne fait pas foi contre le JSON.

**3. `section_0_cadre_et_conventions.md`** — inchangé, l'étalon.

**4.** Ici, une limite : le fichier 4 de la liste était `conversations.json`, et celui-là, **je ne peux pas te le donner** — il n'existe que dans l'export claude.ai que toi seul peux déclencher (desktop → Settings → Privacy → Export data). Ce que je te redonne à la place est le `transcript_chat_alphas.txt` — la première moitié de la conversation en format lisible, à ranger dans `transcripts/` — mais il ne remplace pas le JSON : tout le forage des branches 2 à 6, la révision de 1.1 et la section 0 n'existent que dans l'export. Sans le JSON, le projet démarre avec un tiers du corpus manquant.

Récapitulatif du dossier à constituer : ces quatre fichiers + `conversations.json` de l'export, dans un répertoire dédié, puis « Lis CLAUDE.md et exécute la session 1 ». Les v1/v2 du squelette restent hors du dossier.

---
