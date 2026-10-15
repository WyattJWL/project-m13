# -*- coding: utf-8 -*-
"""Génère les PDF du tome 3 (plan, livre complet, notes) avec la mise en page du tome 2."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tome2"))
import build_tome2_pdf as b  # noqa: E402

b.HERE = HERE

TITLE = "LES PAGES AJOUTÉES"
LABEL = "PROJECT-M13 — TOME 3"
TOC = ["La page qui se réécrit", "Page 4 : la nuit du seize", "Le canapé d'Aubin", "Évie, onze ans",
       "La carte de la chance", "Page 5 : maman est partie", "La main d'Aubin",
       "L'enfant qui essaie de perdre", "La confession de Vasseur", "La maison de Fondettes",
       "Page 6 : treize ans", "Le choix d'Évie", "Treize"]


def doc_pdf(out_name, pdf_title, sub, md_name):
    md = b.read(md_name)
    story = b.cover("Tome 3", sub, title=TITLE)
    story += [b.Paragraph(b.inline(md.splitlines()[0].lstrip("# ")), b.h1)]
    story += b.render(md.split("\n", 1)[1], narrative=False)
    b.build(out_name, pdf_title, story)


if __name__ == "__main__":
    chapters = [b.chapter(n, LABEL) for n in range(1, 14)]
    toc = [b.Paragraph("Sommaire", b.h1), b.Spacer(1, 4 * b.mm)]
    for n, t in enumerate(TOC, 1):
        toc.append(b.Paragraph("<b>%d.</b>&nbsp;&nbsp;%s" % (n, b.inline(t)), b.doc_body))
    toc.append(b.PageBreak())
    story = b.cover("Tome 3", "Version complète — 13 chapitres", title=TITLE) + toc
    for _, flow in chapters:
        story += flow + [b.PageBreak()]
    b.build("PROJECT-M13_Tome3_complet.pdf", "PROJECT-M13 Tome 3 - Les Pages Ajoutées", story[:-1])
    doc_pdf("PROJECT-M13_Tome3_plan.pdf", "PROJECT-M13 Tome 3 - Plan initial",
            "Plan initial (avant rédaction)", "00_plan_tome3.md")
    doc_pdf("PROJECT-M13_Tome3_notes_de_fin.pdf", "PROJECT-M13 Tome 3 - Notes de fin",
            "Notes de fin &amp; décisions", "01_notes_de_fin.md")
    print("ok")
