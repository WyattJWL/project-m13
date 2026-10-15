# -*- coding: utf-8 -*-
"""Génère le PDF du plan du tome 3 avec la mise en page du tome 2."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tome2"))
import build_tome2_pdf as b  # noqa: E402

b.HERE = HERE

if __name__ == "__main__":
    md = b.read("00_plan_tome3.md")
    story = b.cover("Tome 3", "Plan complet — 13 chapitres", title="LES PAGES AJOUTÉES")
    story += [b.Paragraph(b.inline(md.splitlines()[0].lstrip("# ")), b.h1)]
    story += b.render(md.split("\n", 1)[1], narrative=False)
    b.build("PROJECT-M13_Tome3_plan.pdf", "PROJECT-M13 Tome 3 - Plan", story)
    print("ok")
