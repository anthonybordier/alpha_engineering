# STYLE.md — règles d'écriture et étalons

## Règles (contractuelles, reprises de CLAUDE.md)

1. **Grain cible** : 1 500–2 000 mots par nœud de niveau 2-3, formules essentielles
   et 2–5 références primaires par nœud. Modèles : `section_0_cadre_et_conventions.md`
   et les forages du corpus (voir étalons ci-dessous).
2. **Prose continue** : pas de listes à puces dans le corps ; mini-titres **gras**
   par sous-nœud (forme « **N.N.N Titre — sous-titre interprétatif** »).
3. **Ancrage dans l'arbre** : chaque section situe son nœud en ouverture
   (« ce nœud reçoit X de §A, produit Y pour §B ») et liste ses renvois en clôture.
4. **Renvois** : par numéros du squelette (§4.3.3, §1.2.4…). Renvoi vers une section
   non écrite : autorisé, loggé dans `TODO_renvois.md`.
5. **Encadrés transversaux** (A shrinkage, B croissance & survie, C sélection adverse,
   D chevauchement/Newey-West, E surveillance séquentielle) : appendices séparés ;
   les sections y **renvoient** au lieu de répéter.
6. **Crypto intégré** : les spécificités crypto vivent dans chaque section concernée
   (sous-nœud ou paragraphe dédié), jamais dans un chapitre ghetto.
7. **Intégrer, pas réécrire** : le corpus (`transcripts/source.md`) fournit le texte ;
   le travail d'édition = nettoyage (retirer les marques conversationnelles : « on fore »,
   « la carte locale », adresses au lecteur), mise en conformité NOTATION.md,
   insertion des renvois, raccords entre messages. Le fond, les exemples chiffrés
   et les tournures interprétatives sont conservés.
8. **Notation** : `NOTATION.md` fait foi ; collisions résolues en sa faveur.
9. **Références** : jamais inventées. Une affirmation sans source connue reste sans
   citation ; chaque chiffre fin ou attribution issue du corpus est par défaut
   suspect → passe de vérification (marqueur `[à vérifier]` en attendant).
10. **Conflit corpus vs squelette** : le squelette v3 gagne ; conflit loggé.

## Ton

Prose dense, assertive, à la deuxième personne du pluriel absente : le texte parle
du praticien à la troisième personne ou en « on ». Chaque affirmation quantitative est
suivie de sa conséquence pratique (« …ce qui fixe la précision de tout ce qu'on peut
affirmer »). Les formules sont écrites en toutes lettres dans la phrase qui les entoure :
on annonce ce qu'elles disent, on les pose, on commente ce qu'elles mordent.
Les mini-titres portent une interprétation, pas seulement un libellé
(« Le lien avec Kelly — la réconciliation par les sleeves vol-scalés »).

## Étalon 1 — préambule (extrait de §0.2, `section_0_cadre_et_conventions.md`)

> Le signe ≈ porte tout le poids pratique. On ne cherche jamais à estimer l'espérance
> conditionnelle complète : on se contente d'une statistique **positivement corrélée**
> avec le rendement futur. C'est ce déplacement — de l'estimation d'une espérance vers
> la construction d'un prédicteur corrélé — qui rend le problème soluble, et qui fait
> de la corrélation la métrique reine (§0.3).

Ce que l'étalon montre : la définition d'abord, puis l'explicitation terme à terme,
puis les conséquences architecturales numérotées — et le renvoi précis dès qu'un objet
appartient à un autre nœud.

## Étalon 2 — forage de nœud (extrait de M035, corpus, §3.1.3a)

> Écrivons-le complètement, car tout le nœud en découle. Le vrai IC du signal k est θₖ,
> tiré d'une population θₖ ~ N(m, τ²) […] Les ordres de grandeur rendent la formule
> mordante : avec une dispersion vraie τ ≈ 0,01 […] et σ(IC) = 0,15, un an de données
> (T = 250) donne s ≈ 0,0095, donc B ≈ 0,47 — *la moitié* de ce qui distingue votre
> signal de la moyenne du pool est du bruit à jeter. Deux ans : B ≈ 0,31. Quatre ans :
> B ≈ 0,18. La hiérarchie fine des poids ne devient défendable qu'avec des historiques
> que la non-stationnarité rend suspects.

Ce que l'étalon montre : le modèle posé en entier avant tout commentaire, les ordres
de grandeur qui « mordent » (chiffres → conséquence), et la chute qui relie le calcul
à une contrainte de recherche réelle.

## Nettoyages systématiques lors de l'intégration

- Supprimer : « On fore : », « La carte locale : », « Le sous-arbre local : », les
  marqueurs `[Outil : …]`, les diagrammes ASCII redondants avec le squelette, les
  transitions conversationnelles (« On clôt la branche… », adresses directes « tu »).
- Convertir : HTML (`<sub>`, `<sup>`) → notation LaTeX/pandoc ; indices Unicode → cohérents
  avec NOTATION.md.
- Vérifier à chaque section : h/H/λ/κ/φ conformes ; renvois §N.N.N existants ou loggés ;
  crypto intégré ; 2–5 références primaires présentes.
