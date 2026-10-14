# -*- coding: utf-8 -*-
"""Génère les PDF du tome 2 (même charte que build_pdf.py du tome 1) à partir des .md."""
import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (HRFlowable, PageBreak, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
styles = getSampleStyleSheet()

title_style = ParagraphStyle("T", parent=styles["Title"], fontName="Helvetica-Bold",
                             fontSize=26, leading=30, alignment=TA_CENTER, spaceAfter=6)
subtitle_style = ParagraphStyle("S", parent=styles["Normal"], fontName="Helvetica-Oblique",
                                fontSize=12, leading=16, alignment=TA_CENTER,
                                textColor=colors.HexColor("#555555"), spaceAfter=4)
credit_style = ParagraphStyle("C", parent=styles["Normal"], fontName="Helvetica", fontSize=10,
                              leading=14, alignment=TA_CENTER, textColor=colors.HexColor("#777777"))
label = ParagraphStyle("L", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=10,
                       leading=13, alignment=TA_CENTER, textColor=colors.HexColor("#888888"),
                       spaceAfter=2)
chapter_title = ParagraphStyle("CT", parent=styles["Title"], fontName="Helvetica-Bold",
                               fontSize=19, leading=23, alignment=TA_CENTER, spaceAfter=18,
                               spaceBefore=2)
body = ParagraphStyle("B", parent=styles["Normal"], fontName="Helvetica", fontSize=10.3,
                      leading=15.5, alignment=TA_JUSTIFY, spaceAfter=9)
doc_body = ParagraphStyle("DB", parent=body, fontSize=9.5, leading=13.5, alignment=0, spaceAfter=6)
h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=16,
                    leading=20, spaceBefore=6, spaceAfter=10, textColor=colors.HexColor("#111111"))
h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12.5,
                    leading=16, spaceBefore=12, spaceAfter=6, textColor=colors.HexColor("#111111"))
h3 = ParagraphStyle("H3", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=10.5,
                    leading=14, spaceBefore=8, spaceAfter=4, textColor=colors.HexColor("#333333"))
quote = ParagraphStyle("Q", parent=doc_body, leftIndent=10, textColor=colors.HexColor("#444444"),
                       fontName="Helvetica-Oblique")
bullet = ParagraphStyle("BL", parent=doc_body, leftIndent=12, bulletIndent=2, spaceAfter=3)
cell = ParagraphStyle("CELL", parent=doc_body, fontSize=8.5, leading=11, spaceAfter=0)


def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"`(.+?)`", r'<font face="Courier">\1</font>', t)
    return t


def rule(w="35%"):
    return HRFlowable(width=w, thickness=0.6, color=colors.HexColor("#999999"),
                      spaceBefore=4, spaceAfter=12, hAlign="CENTER")


def render(md, narrative):
    """Convertit le markdown (sous-ensemble utilisé ici) en flowables."""
    out, lines, i = [], md.splitlines(), 0
    pstyle = body if narrative else doc_body
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1
        elif ln.strip() == "---":
            out.append(rule())
            i += 1
        elif ln.startswith("# "):
            i += 1  # titre géré à part
        elif ln.startswith("## "):
            out.append(Paragraph(inline(ln[3:]), h2))
            i += 1
        elif ln.startswith("### "):
            out.append(Paragraph(inline(ln[4:]), h3))
            i += 1
        elif ln.startswith(">"):
            paras, cur = [], []
            while i < len(lines) and lines[i].startswith(">"):
                t = lines[i].lstrip("> ").strip()
                if t:
                    cur.append(t)
                elif cur:
                    paras.append(cur)
                    cur = []
                i += 1
            if cur:
                paras.append(cur)
            for para in paras:
                out.append(Paragraph("<br/>".join(inline(t) for t in para), quote))
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in cells):
                    rows.append([Paragraph(inline(c), cell) for c in cells])
                i += 1
            ncol = len(rows[0])
            width = A5[0] - 36 * mm
            t = Table(rows, colWidths=[width / ncol] * ncol, repeatRows=1)
            t.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#bbbbbb")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]))
            out += [t, Spacer(1, 8)]
        elif re.match(r"^(\s*[-*]|\s*\d+\.)\s+", ln):
            m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", ln)
            mark = "•" if m.group(2) in "-*" else m.group(2)
            out.append(Paragraph(inline(m.group(3)), bullet, bulletText=mark))
            i += 1
        else:
            buf = [ln.strip()]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(
                    r"^(#|>|\||---|\s*[-*]\s|\s*\d+\.\s)", lines[i]):
                buf.append(lines[i].strip())
                i += 1
            sep = "<br/>" if narrative else " "
            out.append(Paragraph(sep.join(inline(t) for t in buf), pstyle))
    return out


def build(out_name, title, story):
    doc = SimpleDocTemplate(os.path.join(HERE, out_name), pagesize=A5,
                            topMargin=22 * mm, bottomMargin=22 * mm,
                            leftMargin=18 * mm, rightMargin=18 * mm,
                            title=title, author="Wyatt Lapaillerie-Engone")

    def footer(c, d):
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#888888"))
        c.drawCentredString(A5[0] / 2, 12 * mm, str(d.page))

    doc.build(story, onLaterPages=footer)


def read(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return f.read()


def cover(sub1, sub2):
    return [Spacer(1, 55 * mm), Paragraph("PROJECT-M13", title_style),
            Paragraph("LES PAGES RETIRÉES", ParagraphStyle(
                "t2", parent=title_style, fontSize=16, textColor=colors.HexColor("#444444"))),
            Spacer(1, 10 * mm), Paragraph(sub1, subtitle_style), Paragraph(sub2, subtitle_style),
            Spacer(1, 40 * mm), Paragraph("Une histoire de Wyatt Lapaillerie-Engone", credit_style),
            PageBreak()]


def chapter(n):
    """Lit chapitre_NN.md et renvoie (titre, flowables)."""
    md = read("chapitre_%02d.md" % n)
    title = re.search(r"^# (?!PROJECT)(.+)$", md, re.M).group(1).strip()
    body_md = md.split("# " + title, 1)[1]
    story = [Paragraph("PROJECT-M13 — TOME 2", label), Paragraph("Chapitre %d" % n, label),
             Paragraph(inline(title), chapter_title)]
    return title, story + render(body_md, narrative=True)


def doc_pdf(out_name, pdf_title, sub, md_name):
    md = read(md_name)
    story = cover("Tome 2", sub)
    story += [Paragraph(inline(md.splitlines()[0].lstrip("# ")), h1)]
    story += render(md.split("\n", 1)[1], narrative=False)
    build(out_name, pdf_title, story)


# --- PDF 1 : le livre complet ---
chapters = [chapter(n) for n in range(1, 14)]
toc = [Paragraph("Sommaire", h1), Spacer(1, 4 * mm)]
TOC = ["Le couloir", "Nuit blanche à Tours", "Le livre", "Le distributeur s'allume", "Le bienfaiteur",
       "Page 2 : la mère d'Aubin", "Le lien", "Les coïncidences", "Le plan de Vasseur", "Ennemis alliés",
       "Ce que Darius ne savait pas", "Le bon moment", "Le jeudi"]
for n, t in enumerate(TOC, 1):
    toc.append(Paragraph("<b>%d.</b>&nbsp;&nbsp;%s" % (n, inline(t)), doc_body))
toc.append(PageBreak())
story = cover("Tome 2", "Version complète — 13 chapitres") + toc
for _, flow in chapters:
    story += flow + [PageBreak()]
build("PROJECT-M13_Tome2_complet.pdf", "PROJECT-M13 Tome 2 - Les Pages Retirées", story[:-1])

# --- PDF 2 et 3 : bible et notes ---
doc_pdf("PROJECT-M13_Tome2_bible_et_plan.pdf", "PROJECT-M13 Tome 2 - Bible et plan",
        "Bible &amp; plan des chapitres", "00_bible_et_plan.md")
doc_pdf("PROJECT-M13_Tome2_notes_de_fin.pdf", "PROJECT-M13 Tome 2 - Notes de fin",
        "Notes de fin &amp; décisions", "01_notes_de_fin.md")
print("ok")
