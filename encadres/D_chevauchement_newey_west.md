# Encadré D — Le chevauchement & Newey-West

> **État : relu** (intégré s.13, harmonisé s.14 — renvois et notation vérifiés) — synthèse transversale ; sources dans les sections citées ; vérification des chiffres à venir.

**Un péché, cinq pénitences.** Le péché est toujours le même : traiter comme indépendantes des observations qui partagent de l'information. Dès que l'horizon de prédiction h dépasse la fréquence d'échantillonnage, les labels consécutifs se recouvrent — y~t~ et y~t+1~ partagent h−1 périodes, la série a une structure **MA(h−1)** — et toute statistique qui divise par √T ment : elle compte T observations là où il n'y en a effectivement que ≈ T/h. Dix ans de labels mensuels chevauchants échantillonnés quotidiennement font ~120 points indépendants, pas 2 500 — le chiffre qui calibre toutes les ambitions de la branche 2. L'ouvrage rencontre le péché cinq fois, et le corrige cinq fois avec le même outil ou son équivalent.

**La correction canonique** est l'estimateur de **Newey-West** (1987) : remplacer la variance naïve de la moyenne par la variance de long terme, en sommant les autocovariances pondérées par le noyau de Bartlett,

> Var~NW~ = Γ₀ + Σ~l=1~^L^ (1 − l/(L+1))·(Γ~l~ + Γ~l~'),  avec L ≥ h

— consistante sous hétéroscédasticité et autocorrélation (HAC). L'alternative non paramétrique est le block bootstrap à blocs plus longs que h. Les cinq apparitions :

**1. Les labels d'entraînement** (§1.4.2, §1.4.4). La structure MA(h−1) du y impose l'inférence corrigée — et côté ML, la pondération d'*unicité* (chaque observation pèse 1/nombre de labels vivants qui la partagent) : sans elle, un modèle sur labels chevauchants sur-apprend les épisodes longs, qui votent h fois.

**2. Fama-MacBeth** (§2.2.1). La régression par date gère la corrélation *cross-sectionnelle* des erreurs (chaque date fournit une observation de γ~t~) mais pas leur corrélation temporelle : dès que h > 1, le t-stat de γ̄₁ exige NW avec lag ≥ h — le partage établi par Petersen (2009).

**3. La série des IC** (§2.1.1, §3.1.3d). Les IC quotidiens à horizon h partagent des rendements : l'erreur type naïve σ̂(IC)/√T sous-estime la vraie d'un facteur ≈ √h — un signal à h = 21 voit son t-stat surestimé d'un facteur 4-5, de quoi transformer du bruit en « signal validé ». NW sur la série des IC, ou blocs > h — et le dénominateur de l'ICIR hérite du même soin.

**4. Le modèle de risque** (§4.1.3). La covariance à h jours n'est pas h fois la covariance quotidienne dès que les rendements factoriels sont autocorrélés (momentum factoriel, liquidité) : F^(h)^ ≈ h·[Γ₀ + Σ(1−l/(L+1))·(Γ~l~+Γ~l~')] — NW appliqué à une matrice, documenté dans les handbooks Barra/USE4.

**5. Le protocole de validation** (§2.3.1). Le purging — retirer du train toute observation dont l'intervalle de label chevauche le bloc de test — et l'embargo — la bande qui suit le test, contre la fuite par les features sériellement corrélées — sont la traduction du même théorème en *protocole* : là où NW corrige l'inférence après coup, le purging empêche la contamination avant. C'est la version chirurgicale ; NW est la version comptable.

La leçon commune, et le réflexe qu'elle fonde : devant tout t-stat, toute erreur type, toute « significativité » calculée sur des données à horizon h > 1, la première question est *le chevauchement a-t-il été payé ?* — par NW, par blocs, par unicité, par purge, ou par sous-échantillonnage assumé. Un pipeline qui le paie partout sauf à un étage a un étage qui fabrique des faux positifs — et c'est typiquement celui qu'on n'a pas listé ici.

**Renvois** : §1.4.2, §1.4.4 (labels, unicité) ; §2.1.1 (IC), §2.2.1 (Fama-MacBeth, Petersen), §2.3.1 (purge/embargo) ; §3.1.3 (σ(IC)) ; §4.1.3 (F du modèle de risque).
