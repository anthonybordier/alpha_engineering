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

## P2 — §3.4 : le φ_k de Shapley collisionne avec φ = decay de l'alpha

- **Localisation** : squelette v3, ligne 3.4 — « **Shapley** φ_k = unique partage cohérent ».
- **Problème** : φ est réservé au decay de l'alpha (φ = ln2/H_α), qui apparaît dans le
  MÊME nœud (3.4.5 : « l'interface transporte (s, ρ, σ(IC), φ, τ) »). Deux φ_k de sens
  différents à cinq lignes d'écart.
- **Proposition** : noter la valeur de Shapley φ^Sh_k (choix retenu dans la section
  rédigée) ou v_k.
- **Statut** : proposé (session 7), non appliqué ; section conforme via glose.

## P3 — §3.4.5 : le τ de l'interface (turnover) collisionne avec τ = dispersion du prior

- **Localisation** : squelette v3, lignes 3.4.5 et 6.4 — « l'interface transporte
  (s, ρ, σ(IC), φ, τ) » ; « doc par signal = (s, ρ, σ(IC), φ, τ) ».
- **Problème** : §0.5 définit τ = dispersion vraie des IC dans le prior hiérarchique
  (§3.1.3) ; dans l'interface, τ désigne le turnover du signal. Les deux objets
  coexistent dans la branche 3.
- **Proposition** : noter le turnover de l'interface τ^to (ou « to_k ») dans le corps
  du texte ; le squelette gelé garde (s, ρ, σ(IC), φ, τ).
- **Traitement en attendant** : §3.4.5 écrit τ_k avec glose explicite d'homonymie.
- **Statut** : proposé (session 7), non appliqué.
