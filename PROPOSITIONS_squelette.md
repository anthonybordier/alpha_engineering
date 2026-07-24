# PROPOSITIONS_squelette.md — amendements proposés (jamais appliqués sans instruction)

Le squelette v3 est gelé ; ce fichier collecte les propositions d'amendement (garde-fou 1
de CLAUDE.md). Chaque entrée : localisation, problème, proposition, statut.

## P1 — §1.1.1 : le λ de Daniel-Moskowitz collisionne avec λ = décroissance EMA

- **Localisation** : squelette v3, ligne 1.1.1 — « momentum dynamique w\* = μ̂/2λσ̂² (Daniel-Moskowitz) ».
- **Problème** : NOTATION.md (§0.5) réserve λ à la décroissance d'une EMA ; dans cette
  formule, λ est une constante d'aversion au risque. C'est précisément le type de collision
  que §0.5 déclare éviter (h/H, λ/κ).
- **Proposition** : écrire w\* = μ̂/(2λ_a·σ̂²) dans le squelette (ou γ, cohérent avec
  l'aversion au risque de la branche 4 : max w'α − (γ/2)w'Σw).
- **Traitement en attendant** : la section §1.1 (fichier `sections/1.1_familles_alphas.md`)
  note λ_a avec une glose explicite ; le squelette reste inchangé.
- **Statut** : proposé (session 2), non appliqué.
