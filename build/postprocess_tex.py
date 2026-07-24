# -*- coding: utf-8 -*-
"""Post-traitement du .tex : route les glyphes hors couverture Cambria vers Segoe UI Symbol."""
import os, sys

RISKY = "∝‖⊥⟹⟺⟨⟩∈✓↔←∖ℝ≫∩∪⊆∅∫∂≡≠∞₊₋₍₎ₐ"

path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "livre.tex")
txt = open(path, encoding="utf-8").read()
for ch in RISKY:
    txt = txt.replace(ch, "{\\symfont " + ch + "}")
open(path, "w", encoding="utf-8", newline="\n").write(txt)
print(f"Post-traité {path} : {len(RISKY)} glyphes routés vers Segoe UI Symbol")
