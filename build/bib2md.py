# -*- coding: utf-8 -*-
"""Rend bibliographie.bib en chapitre markdown trié (auteur, année) pour le PDF.
Parseur minimal suffisant pour nos entrées (champs 'clef = {valeur}' sur une ligne)."""
import re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "bibliographie.bib")
OUT = os.path.join(ROOT, "build", "bibliographie.md")

LATEX_MAP = {
    r"{\'o}": "ó", r"{\'e}": "é", r"{\'a}": "á", r"{\'i}": "í", r"{\'u}": "ú",
    r"{\^a}": "â", r"{\^o}": "ô", r"{\`e}": "è", r"{\c c}": "ç", r"{\v c}": "č",
    r"{\"o}": "ö", r"{\"u}": "ü", r"{\"e}": "ë", r"\ldots": "…", r"\&": "&",
    r"{\'E}": "É", r"$\approx$": "≈", r"$-30\%$": "−30%", r"$-55\%$": "−55%",
    r"$-26\%$": "−26%", r"$-58\%$": "−58%", r"$\geq$": "≥", r"$\sim$": "~",
    r"\%": "%", "``": "« ", "''": " »", "--": "–",
}

def unlatex(s):
    for k, v in LATEX_MAP.items():
        s = s.replace(k, v)
    return s.replace("{", "").replace("}", "")

entries = []
raw = open(BIB, encoding="utf-8").read()
for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", raw, re.S):
    kind, key, body = m.group(1), m.group(2).strip(), m.group(3)
    fields = dict()
    for fm in re.finditer(r"(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}", body):
        fields[fm.group(1).lower()] = unlatex(fm.group(2).strip())
    entries.append((kind.lower(), key, fields))

def fmt(kind, f):
    auth = f.get("author") or f.get("editor", "")
    if f.get("editor") and not f.get("author"):
        auth += " (éd.)"
    year = f.get("year", "s.d.")
    title = f.get("title", "")
    parts = [f"**{auth}** ({year}). *{title}*."]
    if kind == "article":
        j = f.get("journal", "")
        vol = f.get("volume", "")
        num = f.get("number", "")
        pg = f.get("pages", "")
        loc = j + (f" {vol}" if vol else "") + (f"({num})" if num else "") + (f", {pg}" if pg else "")
        if loc:
            parts.append(loc + ".")
    elif kind in ("book", "incollection", "inproceedings"):
        if f.get("booktitle"):
            parts.append(f"Dans *{f['booktitle']}*.")
        if f.get("publisher"):
            ed = f" (éd. {f['edition']})" if f.get("edition") else ""
            parts.append(f"{f['publisher']}{ed}.")
    elif kind == "techreport":
        if f.get("institution"):
            parts.append(f"{f['institution']}.")
    if f.get("note"):
        parts.append(f"[{f['note']}]")
    return " ".join(parts)

def sort_key(e):
    _, _, f = e
    auth = (f.get("author") or f.get("editor", "")).lower()
    return (auth, f.get("year", ""))

entries.sort(key=sort_key)
lines = ["# Bibliographie", "",
         f"*{len(entries)} références — une entrée par référence citée dans le corps.",
         "Les entrées marquées [S16]/[S17] ont vu leur affirmation associée vérifiée contre",
         "la source ; celles marquées « À vérifier » attendent la passe de vérification complète.*", ""]
for kind, key, f in entries:
    lines.append(f"- {fmt(kind, f)}")
lines.append("")

open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print(f"Écrit {OUT} : {len(entries)} entrées")
