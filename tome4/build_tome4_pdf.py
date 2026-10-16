# -*- coding: utf-8 -*-
"""Génère les PDF du tome 4 avec la mise en page du tome 2."""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tome2"))
import build_tome2_pdf as b  # noqa: E402

b.HERE = HERE

TITLE = "LES PAGES EFFACÉES"
LABEL = "PROJECT-M13 — TOME 4"


def titles():
    out = []
    for n in range(1, 14):
        md = b.read("chapitre_%02d.md" % n)
        out.append(re.search(r"^# (?!PROJECT)(.+)$", md, re.M).group(1).strip())
    return out


if __name__ == "__main__":
    chapters = [b.chapter(n, LABEL) for n in range(1, 14)]
    toc = [b.Paragraph("Sommaire", b.h1), b.Spacer(1, 4 * b.mm)]
    for n, t in enumerate(titles(), 1):
        toc.append(b.Paragraph("<b>%d.</b>&nbsp;&nbsp;%s" % (n, b.inline(t.capitalize())), b.doc_body))
    toc.append(b.PageBreak())
    story = b.cover("Tome 4", "Version complète — 13 chapitres", title=TITLE) + toc
    for _, flow in chapters:
        story += flow + [b.PageBreak()]
    b.build("PROJECT-M13_Tome4_complet.pdf", "PROJECT-M13 Tome 4 - Les Pages Effacées", story[:-1])
