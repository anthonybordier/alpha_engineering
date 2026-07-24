# TODO_renvois.md — renvois vers des sections non écrites

Règle 4 de CLAUDE.md : un renvoi vers une section non écrite est autorisé, mais loggé ici.
Format : `§source → §cible — contexte — statut`. Retirer la ligne quand la cible est intégrée.

## État : PURGÉ (session 14 — passe d'harmonisation)

**Toutes les cibles existent.** La vérification automatique de la session 14
(`check_renvois.py`) a contrôlé les **1 214 occurrences** de renvois `§N.N(.N)` des
27 sections + 5 encadrés + section 0 contre la table des 150 nœuds définis
(squelette v3 + mini-titres des sections) : **aucun renvoi orphelin**.

Chaque section comporte son bloc **Renvois** de clôture (règle 3 de STYLE.md) — vérifié
sur les 27 fichiers.

Le log historique des renvois loggés sessions 2-12 (toutes cibles depuis résolues) est
conservé dans l'historique git de ce fichier (commits `f6b5940` → `6ee29c1`).

*(Ce fichier se rouvre si une future édition introduit un renvoi vers une cible inexistante.)*
