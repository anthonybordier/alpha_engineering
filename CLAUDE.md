# CLAUDE.md — Projet : traité « L'arbre de la recherche d'alphas »

## Mission
Produire un ouvrage PDF complet à partir du squelette gelé (`arbre_alpha_squelette_v3.md`)
et du corpus de la conversation source (`conversations.json`). Langue : français.
Prisme : equity cross-sectionnel & crypto. Public : praticien quantitatif.

## Fichiers de référence (à relire au début de CHAQUE session)
- `arbre_alpha_squelette_v3.md` — la table des matières contractuelle, avec les
  formules-pivots de chaque nœud, 5 encadrés transversaux et les renvois structurants.
  L'arbre entier y est au grain ✓✓ : TOUT le contenu correspondant existe dans le corpus.
  On n'écrit RIEN hors de cette table.
- `section_0_cadre_et_conventions.md` — le préambule rédigé : étalon de grain, de ton
  et de notation.
- `NOTATION.md` — à générer en session 1 depuis §0.5, puis faire respecter partout
  (h = horizon, H = demi-vie, λ = décroissance EMA, κ = pénalité ridge, φ = ln2/H_α).
- `conversations.json` — l'export claude.ai. Contient la conversation source intégrale :
  c'est LE corpus. Le fichier `transcripts/transcript_chat_alphas.txt`, s'il est présent,
  n'en couvre que la première moitié (jusqu'à la normalisation §1.3) — le JSON fait foi.

## Session 1 (initialisation)
1. Extraire de `conversations.json` la conversation source (la plus longue traitant de
   l'arbre de la recherche d'alphas) et la convertir en markdown lisible dans
   `transcripts/source.md`, en préservant l'ordre et l'attribution des messages.
2. Construire l'index corpus → squelette : pour chaque nœud de la table, noter dans
   `AVANCEMENT.md` le(s) message(s) du transcript qui le rédigent. Points d'attention :
   1.1 existe en DEUX versions (la seconde, plus mathématique, remplace la première) ;
   les branches 4, 5, 2, 3.2-3.4, 1.4, 6 et la section 0 sont dans la seconde moitié
   de la conversation ; les échanges pédagogiques (cross-section, IC/Spearman, demi-vie,
   autocorrélation, turnover) alimentent §0 et §1.3.4.
3. Générer NOTATION.md (depuis §0.5), STYLE.md (règles ci-dessous + 2 sections modèles),
   l'arborescence un fichier .md par nœud, et AVANCEMENT.md
   (état par nœud : indexé / intégré / relu / vérifié).

## Règles d'écriture
1. Grain cible : 1 500-2 000 mots par nœud de niveau 2-3, formules essentielles et
   2-5 références primaires par nœud. Modèle : section_0 et les forages du corpus.
2. Prose continue, pas de listes à puces dans le corps ; mini-titres gras par sous-nœud.
3. Chaque section situe son nœud dans l'arbre en ouverture et liste ses renvois en clôture.
4. Renvois par numéros du squelette (§4.3.3, §1.2.4...). Renvoi vers section non écrite :
   autorisé, loggé dans `TODO_renvois.md`.
5. Les 5 encadrés transversaux (shrinkage, croissance & survie, sélection adverse,
   chevauchement/Newey-West, surveillance séquentielle) sont des appendices séparés ;
   les sections y renvoient au lieu de répéter.
6. Spécificités crypto intégrées dans chaque section concernée, pas de chapitre ghetto.
7. Le corpus est à INTÉGRER (nettoyage, notation, renvois), pas à réécrire.

## Workflow (sessions suivantes)
- Une branche (ou demi-branche) par session, ordre 0 → 1 → 2 → 3 → 4 → 5 → 6 → encadrés.
  À chaque session : relire CLAUDE.md, NOTATION.md, AVANCEMENT.md, et les sections
  adjacentes (pour les renvois).
- Passe d'harmonisation : grep terminologie & symboles ; chaque renvoi pointe vers une
  section existante ; conventions §0.6 uniformes.
- Passe de VÉRIFICATION (obligatoire, séparée) : chaque valeur numérique, chaque
  attribution (auteur, revue, année) est contrôlée contre la source primaire, ou marquée
  [à vérifier]. Le corpus vient de mémoire de modèle : l'architecture est fiable, les
  chiffres fins ne le sont pas par défaut.
- Compilation : pandoc → LaTeX → PDF. TdM et numérotation = squelette, index des
  notations, bibliographie BibTeX (une entrée par référence citée).

## Garde-fous
- Ne jamais modifier arbre_alpha_squelette_v3.md sans instruction explicite ; toute
  proposition d'amendement va dans `PROPOSITIONS_squelette.md`.
- Ne pas inventer de références. Une affirmation sans source connue reste sans citation.
- Conflit corpus vs squelette : le squelette gagne ; logger le conflit.
- Chaque session se termine par : mise à jour d'AVANCEMENT.md + commit.
