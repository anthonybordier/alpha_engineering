# -*- coding: utf-8 -*-
"""Assemble le livre : sections + encadrés -> build/livre.md, dans l'ordre du squelette.
Prétraitement : ~x~ -> <sub>, ^x^ / ^{x} -> <sup> (pandoc gère l'échappement LaTeX)."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = lambda name: os.path.join(ROOT, "sections", name)
E = lambda name: os.path.join(ROOT, "encadres", name)

YAML = """---
title: "L'arbre de la recherche d'alphas"
subtitle: "Traité de recherche quantitative — equity cross-sectionnel & crypto"
author: "Anthony Bordier"
date: "Version de travail du 24 juillet 2026 — chiffres et attributions non vérifiés"
lang: fr
documentclass: book
classoption: [oneside, 11pt]
geometry: margin=2.4cm
mainfont: Cambria
sansfont: Segoe UI
monofont: Consolas
toc-depth: 1
colorlinks: true
linkcolor: NavyBlue
urlcolor: NavyBlue
header-includes:
  - \\newfontfamily\\symfont{Segoe UI Symbol}
  - \\usepackage[dvipsnames]{xcolor}
  - \\setlength{\\emergencystretch}{3em}
---

"""

PLAN = [
    (r"\part{Cadre et conventions}", [os.path.join(ROOT, "section_0_cadre_et_conventions.md")]),
    (r"\part{Recherche du signal}", [
        S("1.1_familles_alphas.md"), S("1.2_feature_engineering.md"),
        S("1.3_normalisation.md"), S("1.4_cibles_labels.md"),
        S("2.1_metriques.md"), S("2.2_backtest.md"),
        S("2.3_anti_overfitting.md"), S("2.4_non_stationnarite.md"),
        S("3.1_ponderations_simples.md"), S("3.2_regression_regularisee.md"),
        S("3.3_stacking_meta_modeles.md"), S("3.4_orthogonalisation_pool.md"),
        S("3.4.5_combinaison_sous_couts.md"),
    ]),
    (r"\part{Mise en œuvre}", [
        S("4.1_modeles_de_risque.md"), S("4.2_construction.md"), S("4.3_couts.md"),
        S("4.4_sizing_levier.md"), S("4.5_gestion_des_risques.md"),
        S("5.1_microstructure.md"), S("5.2_impact.md"), S("5.3_scheduling.md"),
        S("5.4_tactique.md"), S("5.5_tca.md"),
        S("6.1_donnees.md"), S("6.2_moteur.md"), S("6.3_production.md"),
        S("6.4_organisation.md"),
    ]),
    (r"\part{Encadrés transversaux}", [
        E("A_shrinkage.md"), E("B_croissance_et_survie.md"), E("C_selection_adverse.md"),
        E("D_chevauchement_newey_west.md"), E("E_surveillance_sequentielle.md"),
    ]),
    (r"\part{Annexes}", [os.path.join(ROOT, "NOTATION.md")]),
]

RE_SUP_BRACE = re.compile(r"\^\{([^}\n]{1,80})\}")
RE_SUP_PAIR = re.compile(r"\^([^\s^][^^\n]{0,50}?)\^")
RE_SUB_PAIR = re.compile(r"(?<=\S)~([^~\n]{1,60}?)~")

def preprocess(txt: str) -> str:
    # protéger les blocs de code (aucun dans le corpus, mais par sûreté)
    txt = RE_SUP_BRACE.sub(lambda m: f"<sup>{m.group(1)}</sup>", txt)
    txt = RE_SUP_PAIR.sub(lambda m: f"<sup>{m.group(1)}</sup>", txt)
    txt = RE_SUB_PAIR.sub(lambda m: f"<sub>{m.group(1)}</sub>", txt)
    return txt

out = [YAML]
for part, files in PLAN:
    out.append(f"```{{=latex}}\n{part}\n```\n\n")
    for f in files:
        txt = open(f, encoding="utf-8").read().strip()
        if f.endswith("NOTATION.md"):
            txt = txt.replace("# NOTATION.md — table des notations de l'ouvrage",
                              "# Annexe — Table des notations", 1)
        out.append(preprocess(txt) + "\n\n")

dest = os.path.join(ROOT, "build", "livre.md")
open(dest, "w", encoding="utf-8", newline="\n").write("".join(out))
print(f"Écrit {dest} ({os.path.getsize(dest)} octets)")
