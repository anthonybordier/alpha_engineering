# 0. Cadre et conventions

*Préambule au squelette gelé. Cette section pose les objets, les axes, les métriques et les notations que les six branches suivantes tiennent pour acquis.*

---

## 0.1 Le panel et ses deux axes

Toute la recherche d'alphas opère sur un **panel** : une matrice dont les lignes sont les actifs — indexés par *i* ∈ {1, …, N} — et les colonnes les dates, indexées par *t* ∈ {1, …, T}. Chaque cellule contient les observations disponibles pour l'actif *i* à la date *t* : prix, volume, fondamentaux, flux, métriques on-chain. Cette matrice est l'unique matière première ; toutes les décisions méthodologiques qui suivent découlent de la façon dont on la découpe.

**La coupe cross-sectionnelle** est une colonne : une date fixée, tous les actifs comparés entre eux. Elle pose la question « parmi les N actifs d'aujourd'hui, lesquels vont surperformer les autres sur les h prochaines périodes ? ». C'est une question de *classement relatif*, jamais de niveau : un signal cross-sectionnel est indifférent à la direction du marché — si tous les actifs montent de 5%, seul compte l'ordre dans lequel ils montent. Cette propriété n'est pas un accident, elle est construite : la standardisation par date (§1.3.1) démoyenne le signal à travers les actifs, ce qui annule la position nette et élimine le facteur commun — la source de variance dominante — *avant* toute estimation. On ne prédit que le résidu, là où le ratio signal/bruit est le plus favorable.

**La coupe time-series** est une ligne : un actif, son histoire. La question devient « cet instrument va-t-il monter ou baisser ? » — une question de niveau, qui autorise l'exposition nette directionnelle et le levier variable. C'est le cadre des CTA, du trend-following, du carry par instrument, et le seul disponible lorsque l'univers est trop étroit pour offrir un cross-section (un desk sur quelques contrats futures liquides).

Les deux régimes ne sont pas concurrents mais orthogonaux, et un book complet fait tourner les deux en parallèle : sleeves cross-sectionnels pour l'alpha relatif, sleeves time-series pour le timing directionnel, la normalisation (§1.3) étant ce qui permet de les faire cohabiter dans une même combinaison. Un même jeu de données produit des signaux différents selon l'axe : un signal qui bouge identiquement pour tous les actifs est nul en cross-section (le démoyennage l'efface) et peut être excellent en time-series ; un signal constant dans le temps est nul en time-series et peut être excellent en cross-section.

Le prisme dominant de cet ouvrage est cross-sectionnel, pour deux raisons : c'est le cadre de l'equity statistical arbitrage, qui a produit l'essentiel de la littérature et du formalisme, et c'est celui où le breadth (§0.4) rend exploitables des pouvoirs prédictifs très faibles. Le crypto est le cas hybride : avec un univers investissable de l'ordre de 150 à 300 tokens, le cross-section existe mais reste étroit — assez riche pour un momentum ou un funding relatif, trop pauvre pour les partitions fines (double sorts 5×5, §1.2.3). Les spécificités crypto sont signalées au fil des sections plutôt que reléguées dans un chapitre séparé.

---

## 0.2 La définition de l'alpha

L'objet central de l'ouvrage est défini une fois pour toutes :

> **α**<sub>i,t</sub> ≈ **E**[ r<sub>i, t→t+h</sub> | **F**<sub>t</sub> ]

Un alpha est une **statistique ayant un pouvoir prédictif sur les cours** — l'approximation d'une espérance de rendement futur, conditionnelle à l'information disponible à l'instant *t*. Trois termes méritent d'être explicités.

**F**<sub>t</sub> est la *filtration* : l'ensemble de l'information légitimement connaissable en *t*. Sa définition est le premier acte de discipline de tout le processus, et l'objet de la section 1.2.4 : une donnée n'entre dans **F**<sub>t</sub> qu'au moment où elle devient *connaissable*, pas au moment où elle décrit. Un bilan clos le 31 décembre n'entre dans **F** que mi-février.

*h* est l'**horizon** de prédiction. Il n'existe pas d'alpha sans horizon : le même conditionnement produit des prévisions de signes différents selon qu'on regarde à une seconde ou à six mois (le reversal court terme et le momentum moyen terme sont extraits des mêmes prix). Préciser *h* est donc constitutif de la définition, pas un détail d'implémentation.

Le signe ≈ porte tout le poids pratique. On ne cherche jamais à estimer l'espérance conditionnelle complète : on se contente d'une statistique **positivement corrélée** avec le rendement futur. C'est ce déplacement — de l'estimation d'une espérance vers la construction d'un prédicteur corrélé — qui rend le problème soluble, et qui fait de la corrélation la métrique reine (§0.3).

Deux conséquences architecturales découlent immédiatement de cette définition et gouvernent l'organisation de l'ouvrage :

1. **La prévision n'est pas une position.** L'alpha est un nombre attaché à un actif et une date, pas un ordre. La transformation prévision → portefeuille est un problème distinct, avec ses propres objets (modèle de risque, contraintes, coûts) — d'où la séparation des branches 1-3 (recherche du signal) et 4-6 (mise en œuvre), et l'interface minimale entre les deux : un vecteur d'alphas normalisés.
2. **L'alpha est un objet standardisable.** Puisque c'est une prévision et non une stratégie, il devient testable, mesurable et comparable selon un protocole uniforme — condition nécessaire à l'organisation industrielle de la recherche (§6.4), où des centaines de signaux produits indépendamment doivent être évalués et agrégés selon la même grille.

L'espérance conditionnelle n'est cependant que le premier moment. Prévoir **E**[r | **F**] sans prévoir **Var**[r | **F**] laisse le dimensionnement aveugle : la volatilité conditionnelle intervient dans la normalisation des cibles (§1.3.2), le sizing (§4.4) et le conditionnement par régime (§1.2.3). L'objet complet est la distribution conditionnelle ; l'alpha en est la partie qu'on estime le mieux.

---

## 0.3 Mesurer le pouvoir prédictif : IC et ICIR

L'**information coefficient** (IC) est la corrélation entre le signal et le rendement réalisé. Dans le cadre cross-sectionnel, il se calcule **par date** :

> IC<sub>t</sub> = corr( s<sub>·,t</sub> , r<sub>·, t→t+h</sub> )   sur les N actifs

On obtient donc une **série temporelle d'IC**, dont on résume la moyenne — le pouvoir prédictif — et l'écart-type — sa régularité. Le rapport des deux est l'**ICIR** :

> ICIR = moyenne(IC<sub>t</sub>) / écart-type(IC<sub>t</sub>)

C'est l'ICIR, et non l'IC moyen, qui gouverne le Sharpe du sleeve : un IC de 0,03 stable domine un IC de 0,05 qui alterne +0,15 et −0,05. La convention dominante est le **rank IC** (corrélation de Spearman plutôt que de Pearson) : robuste aux outliers et invariant aux transformations monotones du signal, ce qui rend la mesure indépendante des choix d'échelle faits en amont.

Trois repères d'ordre de grandeur, valables en equity cross-sectionnel quotidien :

- Un IC exploitable vit entre **0,02 et 0,06**. Au-delà de 0,10 de façon durable, suspecter un look-ahead avant de célébrer.
- Puisque R² ≈ IC², un IC de 0,03 correspond à un R² d'environ 10<sup>−3</sup>. Le régime de travail est celui du **très faible ratio signal/bruit** — c'est la contrainte structurante de toute la branche 2.
- L'écart-type temporel de l'IC quotidien, σ(IC), se situe typiquement entre **0,10 et 0,20**, ce qui fixe la précision de tout ce qu'on peut affirmer (§3.1.2 : valider un IC demande des mois, classer deux IC voisins demande des années).

En time-series, la même quantité se calcule le long de la ligne — corrélation entre le signal et le rendement futur sur l'historique d'un instrument — et s'agrège ensuite entre instruments. Les formules diffèrent, l'interprétation est identique.

---

## 0.4 Breadth et loi fondamentale

Le lien entre pouvoir prédictif unitaire et performance du portefeuille est donné par la **loi fondamentale de la gestion active** (Grinold) :

> IR ≈ IC × √BR

où IR est l'information ratio du portefeuille et **BR le *breadth*** — le nombre de paris indépendants pris par unité de temps. C'est l'équation qui explique pourquoi un pouvoir prédictif dérisoire produit une stratégie viable : en cross-section, chaque date fournit N paris quasi simultanés, et 3 000 actifs × 250 jours donnent un breadth annuel de plusieurs centaines de milliers. Un IC de 0,02 devient alors un IR à un chiffre confortable. En time-series sur quelques instruments, le breadth ne vient que de la répétition dans le temps : il faut des IC d'un ordre de grandeur supérieur pour le même résultat.

Deux corrections importantes doivent accompagner tout usage de cette loi :

**L'indépendance est une fiction.** BR n'est pas N × T mais le nombre de paris *effectivement indépendants*. La corrélation cross-sectionnelle entre actifs (les titres d'un même secteur ne sont pas des paris distincts) et l'autocorrélation du signal dans le temps (un signal de demi-vie longue reproduit le même pari plusieurs jours d'affilée) réduisent toutes deux le breadth effectif, souvent d'un ordre de grandeur. La loi donne un plafond, pas une prévision.

**Le transfer coefficient.** La formulation généralisée (Clarke, de Silva & Thorley) insère un terme supplémentaire :

> IR ≈ TC × IC × √BR

où **TC**, le *transfer coefficient*, est la corrélation entre les prévisions et les positions effectivement prises. Il vaut 1 si le portefeuille est exactement proportionnel aux alphas, et chute dès qu'interviennent contraintes, coûts, limites de liquidité ou interdiction de vendre à découvert. C'est le terme qui relie les branches 1-3 aux branches 4-5 : un alpha ne vaut que ce que la mise en œuvre en transfère, et une neutralisation faite en amont (§1.3.3) sert précisément à ce que l'IC mesuré soit un IC transférable.

---

## 0.5 Notations

Symboles utilisés uniformément dans tout l'ouvrage.

| Symbole | Signification |
|---|---|
| *i*, *N* | indice d'actif ; taille de l'univers à une date |
| *t*, *T* | indice de date ; longueur de l'historique |
| *h* | **horizon de prédiction** (en périodes) |
| *H* | **demi-vie** d'une pondération exponentielle (§1.2.2) |
| **F**<sub>t</sub> | filtration : information connaissable en *t* |
| r<sub>i, t→t+h</sub> | rendement de l'actif *i* entre *t* et *t*+*h* |
| α<sub>i,t</sub> | prévision (alpha) pour l'actif *i* en *t* |
| s<sub>k</sub> | signal *k* après normalisation (moyenne 0, variance 1) |
| *K* | nombre de signaux dans le pool |
| ρ<sub>k</sub> | IC du signal *k* |
| **C** | matrice de corrélation entre signaux (§3) |
| **w** | vecteur des poids de combinaison (§3) |
| β<sub>i</sub>, **F**<sup>fac</sup> | expositions factorielles ; rendements des facteurs (§4.1) |
| ε<sub>i,t</sub> | rendement résiduel (idiosyncratique) |
| σ | volatilité (contexte précisé localement) |
| λ | **facteur de décroissance** d'une EMA, λ = exp(−ln2 / *H*) |
| κ | **pénalité de régularisation** (ridge, §3.2) |
| τ | dispersion vraie des IC dans le prior hiérarchique (§3.1.3) |
| *B* | facteur de shrinkage bayésien, *B* = s²/(τ² + s²) |
| IC, ICIR, IR, TC | cf. §0.3 et §0.4 |

Deux collisions de notation sont fréquentes dans la littérature et **évitées ici** : *h* désigne l'horizon et jamais une demi-vie (notée *H*) ; λ désigne la décroissance exponentielle et jamais la pénalité ridge (notée κ).

---

## 0.6 Conventions de calcul

**Rendements.** Log-rendements par défaut pour l'agrégation temporelle et l'estimation de volatilité ; rendements simples pour l'agrégation cross-sectionnelle (un portefeuille est une moyenne pondérée de rendements simples, pas de log-rendements). En equity, les rendements sont *totaux* (dividendes réinvestis) sauf mention contraire. En crypto, le rendement pertinent d'une position en perpétuel est **funding inclus** : ignorer cette composante fausse simultanément les features et les cibles.

**Annualisation.** √252 en equity (jours de bourse), √365 en crypto (marché continu). Mélanger les deux conventions fausse silencieusement tous les ratios d'environ 20% — la source d'erreur la plus commune et la plus discrète des comparaisons inter-classes d'actifs.

**Dates.** Toute table de données porte une colonne « connaissable à partir de », et aucune jointure temporelle ne se fait sur une autre colonne. Le signal calculé sur la clôture de *t* est exécuté au plus tôt à l'ouverture de *t*+1. Les horodatages crypto sont en UTC, avec mention explicite lorsque la grille du funding (00/08/16 UTC) intervient.

**Univers.** Point-in-time strict : les constituants sont ceux qui existaient à la date considérée, les sorties (radiations, faillites, rachats, tokens morts) sont conservées avec leur rendement terminal. Les filtres de liquidité sont appliqués avec les données connaissables à la date, jamais rétrospectivement.

**Signes.** Chaque signal est publié avec un signe fixé par un prior économique explicite. Un signe déterminé par backtest est un degré de liberté supplémentaire, comptabilisé comme tel (§1.2.3, §2.3).

---

## 0.7 La relativité de la frontière alpha / beta

Un dernier point, épistémologique mais aux conséquences pratiques constantes : **la définition §0.2 rend l'alpha relatif au conditionnement**. Ce qui est alpha pour un desk est beta exotique pour un autre qui inclut ce facteur dans son modèle de risque ou dans sa filtration. Une prime de portage est un alpha tant qu'aucun facteur « carry » ne figure au modèle de risque ; elle devient une exposition rémunérée dès qu'il y figure.

Il n'existe donc pas de frontière absolue entre alpha et beta, seulement une frontière *relative à un modèle de risque donné* — celui de la section 4.1. C'est pourquoi la neutralisation (§1.3.3) et la mesure des expositions résiduelles (§2.1) ne sont pas des raffinements mais des étapes constitutives : elles définissent, opérationnellement, ce que la maison choisit d'appeler alpha. Deux desks aux modèles de risque différents peuvent légitimement porter des jugements opposés sur le même signal.

---

## 0.8 Plan et mode de lecture

L'ouvrage suit le pipeline dans son ordre logique, en deux moitiés séparées par une interface étroite — un vecteur d'alphas normalisés.

**Recherche du signal**, qui opère exclusivement sur des prévisions : la branche **1** construit les signaux (familles, feature engineering, normalisation, cibles) ; la branche **2** les valide et sert de système immunitaire (métriques, backtest, anti-overfitting, non-stationnarité) ; la branche **3** les agrège en une prévision unique (pondérations, régularisation, orthogonalité du pool).

**Mise en œuvre**, où les prévisions rencontrent les frictions : la branche **4** transforme les prévisions en positions (modèle de risque, optimisation, coûts, levier) ; la branche **5** transforme les positions en transactions (microstructure, impact, scheduling, TCA) ; la branche **6** porte l'ensemble (données, backtest, production, organisation de la recherche).

Chaque section est rédigée pour être lisible isolément, avec des renvois explicites vers les nœuds dont elle dépend. Deux fils traversent l'ouvrage de bout en bout et méritent d'être suivis dès la première lecture : le **budget de degrés de liberté** — chaque choix pris en branche 1 est une dette remboursée en branche 2 — et le **budget de turnover** — chaque unité de pouvoir prédictif capturée en branche 1 se paie en coûts dans les branches 4 et 5. La recherche d'alphas est, pour l'essentiel, la gestion disciplinée de ces deux budgets.
