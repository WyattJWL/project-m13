# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable
)
from reportlab.lib import colors

import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "PROJECT-M13_v2_chap1-19.pdf")

doc = SimpleDocTemplate(
    OUT, pagesize=A5,
    topMargin=22*mm, bottomMargin=22*mm,
    leftMargin=18*mm, rightMargin=18*mm,
    title="PROJECT-M13 - La Page 404",
    author="Wyatt Lapaillerie-Engone",
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleBig", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=26, leading=30, alignment=TA_CENTER, spaceAfter=6,
)
subtitle_style = ParagraphStyle(
    "Subtitle", parent=styles["Normal"], fontName="Helvetica-Oblique",
    fontSize=12, leading=16, alignment=TA_CENTER, textColor=colors.HexColor("#555555"),
    spaceAfter=4,
)
credit_style = ParagraphStyle(
    "Credit", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10, leading=14, alignment=TA_CENTER, textColor=colors.HexColor("#777777"),
)
h1 = ParagraphStyle(
    "H1", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=16, leading=20, spaceBefore=6, spaceAfter=12,
    textColor=colors.HexColor("#111111"),
)
chapter_label = ParagraphStyle(
    "ChapterLabel", parent=styles["Normal"], fontName="Helvetica-Oblique",
    fontSize=10, leading=13, alignment=TA_CENTER, textColor=colors.HexColor("#888888"),
    spaceAfter=2,
)
chapter_title = ParagraphStyle(
    "ChapterTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=19, leading=23, alignment=TA_CENTER, spaceAfter=18, spaceBefore=2,
)
flashback_tag = ParagraphStyle(
    "FlashbackTag", parent=chapter_label, spaceAfter=14,
)
body = ParagraphStyle(
    "Body", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10.3, leading=15.5, alignment=TA_JUSTIFY, spaceAfter=9,
)
machine_style = ParagraphStyle(
    "Machine", parent=body, fontName="Courier-Bold", alignment=TA_CENTER,
    fontSize=10, textColor=colors.HexColor("#333333"), spaceBefore=6, spaceAfter=10,
)
label_style = ParagraphStyle(
    "Label", parent=body, fontName="Courier", alignment=TA_CENTER,
    fontSize=9.5, textColor=colors.HexColor("#555555"), spaceBefore=4, spaceAfter=10,
)
cn = ParagraphStyle("cn", parent=body, fontName="Helvetica-Bold", spaceBefore=6, spaceAfter=2)

def rule():
    return HRFlowable(width="35%", thickness=0.6, color=colors.HexColor("#999999"),
                       spaceBefore=4, spaceAfter=14, hAlign="CENTER")

def p(txt):
    S.append(Paragraph(txt, body))

def name(txt):
    S.append(Paragraph(txt, cn))

def chap(num, title, tag=None):
    S.append(Paragraph("PROJECT-M13", chapter_label))
    S.append(Paragraph(f"Chapitre {num}", chapter_label))
    S.append(Paragraph(title, chapter_title))
    if tag:
        S.append(Paragraph(tag, flashback_tag))

S = []

# ---------- TITLE PAGE ----------
S.append(Spacer(1, 55*mm))
S.append(Paragraph("PROJECT-M13", title_style))
S.append(Paragraph("LA PAGE 404", ParagraphStyle("t2", parent=title_style, fontSize=16, textColor=colors.HexColor("#444444"))))
S.append(Spacer(1, 10*mm))
S.append(Paragraph("Version 2 &mdash; reconstruction", subtitle_style))
S.append(Paragraph("Douze chapitres", subtitle_style))
S.append(Spacer(1, 20*mm))
S.append(Paragraph("Une histoire de Wyatt Lapaillerie-Engone", credit_style))
S.append(PageBreak())

# ---------- NOTE ----------
S.append(Paragraph("Avant de commencer", h1))
p("Cette version repart de z&eacute;ro. Elle garde ce qu'il y avait de vraiment "
  "original dans la premi&egrave;re &mdash; le distributeur, la page 404, l'id&eacute;e "
  "qu'on ne supprime jamais un souvenir sans en cr&eacute;er une cons&eacute;quence &mdash; "
  "et laisse tomber tout ce qui ressemblait &agrave; une s&eacute;rie qu'on a d&eacute;j&agrave; vue ailleurs.")
p("Le centre de l'histoire n'est plus une intelligence artificielle qui veut "
  "dominer le monde. C'est plus petit, et plus vrai : quelqu'un qu'on aime "
  "nous ment pour nous &eacute;pargner une douleur, et cette version confortable "
  "des choses finit par co&ucirc;ter plus cher que la v&eacute;rit&eacute; elle-m&ecirc;me.")
S.append(PageBreak())


# ======================================================================
# CHAPITRE 1 -- MIEL
# ======================================================================
chap(1, "MIEL")

p("DARIUS a quatorze ans et une r&egrave;gle qu'il applique &agrave; tout, m&ecirc;me si "
  "personne ne la lui a jamais demand&eacute;e : quand un truc dans sa vie ne "
  "tient pas debout, il pr&eacute;f&egrave;re ne pas y toucher plut&ocirc;t que le voir "
  "s'effondrer pour de bon. Il a class&eacute; l&agrave;-dedans, dans la case &laquo;&nbsp;n'y "
  "touche pas&nbsp;&raquo;, un certain nombre de choses : le tiroir du bas dans la "
  "chambre de sa m&egrave;re, la photo retourn&eacute;e sur l'&eacute;tag&egrave;re du salon, et "
  "l'histoire du chien parti vivre &agrave; la campagne chez le cousin Serge, "
  "quand Darius avait huit ans. Il a cess&eacute; de poser la question &agrave; cet "
  "&acirc;ge-l&agrave;, et il ne l'a plus jamais repos&eacute;e. C'est &agrave; ce genre de silence "
  "qu'on reconna&icirc;t un mensonge r&eacute;ussi &mdash; il ne se fait plus contredire, "
  "il se fait oublier, puis un jour il se fait remplacer par le silence "
  "lui-m&ecirc;me, qui prend toute la place.")

p("Le matin m&ecirc;me, en cours d'histoire, la prof a parl&eacute; de la m&eacute;moire "
  "collective, de la fa&ccedil;on dont les peuples choisissent ce qu'ils "
  "gardent d'une guerre et ce qu'ils pr&eacute;f&egrave;rent laisser tomber dans "
  "les manuels, et Darius a pris des notes sans vraiment &eacute;couter, "
  "occup&eacute; &agrave; dessiner dans la marge un petit chien qu'il a effac&eacute; "
  "avant que quelqu'un ne le voie. &Ccedil;a lui arrive, ces derniers temps, "
  "sans raison qu'il puisse nommer : dessiner un animal qu'il n'a "
  "jamais vraiment eu le temps de dessiner &agrave; l'&eacute;poque, comme si sa "
  "main savait quelque chose que le reste de lui avait d&eacute;cid&eacute; "
  "d'oublier proprement.")

p("Ce jeudi-l&agrave;, comme tous les jeudis, sa m&egrave;re travaille tard au "
  "cabinet et lui laisse un billet de cinq euros coinc&eacute; sous l'aimant du "
  "frigo, pour qu'il s'ach&egrave;te un sandwich en rentrant du coll&egrave;ge. Darius "
  "n'ach&egrave;te jamais de sandwich. Il garde les billets dans une bo&icirc;te &agrave; "
  "chaussures, sans trop savoir pourquoi, comme si un jour il allait en "
  "avoir besoin tous en m&ecirc;me temps. Peut-&ecirc;tre que c'est &ccedil;a, avoir un "
  "p&egrave;re qu'on ne voit plus depuis deux ans et quatre mois : on garde des "
  "choses de c&ocirc;t&eacute;, sans savoir pour quoi, juste au cas o&ugrave;.")

p("Il pleut sur Luynes comme il pleut toujours en novembre, de biais, "
  "sans conviction, une pluie qui n'a pas l'air d&eacute;cid&eacute;e &agrave; vraiment "
  "tomber. Darius rentre &agrave; v&eacute;lo, capuche tremp&eacute;e, en suivant l'itin&eacute;raire "
  "qu'il prend depuis la sixi&egrave;me : la rue des Fontaines, le pont, la "
  "place du march&eacute;, et enfin la rue qui monte vers chez lui, celle o&ugrave; "
  "il faut se lever sur les p&eacute;dales dans les cent derniers m&egrave;tres. Sur "
  "la place, il passe devant le bar-tabac comme tous les soirs, sans "
  "vraiment le regarder &mdash; sauf que ce soir-l&agrave;, quelque chose cloche "
  "dans la vitrine, et son corps s'arr&ecirc;te avant m&ecirc;me que sa t&ecirc;te ait "
  "compris pourquoi.")

p("Entre le pr&eacute;sentoir &agrave; journaux et le vieux flipper hors service "
  "depuis l'&eacute;t&eacute; dernier, il y a une machine que Darius n'a jamais vue. "
  "Haute, en verre d&eacute;poli, avec des reflets qui n'ont pas la couleur "
  "des n&eacute;ons du bar &mdash; plut&ocirc;t une lumi&egrave;re bleue-blanche, propre, "
  "presque m&eacute;dicale, qui ne colle pas avec le reste de la vitrine, les "
  "affiches jaunies pour le loto et le calendrier des pompiers de "
  "l'ann&eacute;e derni&egrave;re. La machine ne vend ni canettes ni bonbons. &Agrave; "
  "l'int&eacute;rieur, dans des casiers align&eacute;s comme des bocaux de laboratoire, "
  "des objets flottent dans un g&eacute;l&eacute; transparent, l&eacute;g&egrave;rement visqueux, "
  "qui d&eacute;forme un peu leur contour : une gourmette avec un pr&eacute;nom "
  "qu'il ne reconna&icirc;t pas, un ticket de cin&eacute;ma jauni pour un film sorti "
  "avant sa naissance, une paire de lunettes d'enfant, une dent de lait "
  "dans un petit sachet, et, tout en bas &agrave; droite, un collier pour "
  "chien, taille S, cuir marron, l&eacute;g&egrave;rement rong&eacute; sur la boucle.")

p("Darius conna&icirc;t ce collier. Il l'a achet&eacute; lui-m&ecirc;me, avec son argent "
  "de poche, un mercredi de CE2, dans l'animalerie qui a ferm&eacute; depuis. "
  "Il se souvient m&ecirc;me du prix &mdash; six euros quatre-vingts &mdash; parce que "
  "sa m&egrave;re avait d&ucirc; compl&eacute;ter avec la monnaie de son porte-monnaie &agrave; "
  "elle. Il ne l'a jamais revu depuis le jour o&ugrave; on lui a dit que Miel "
  "&eacute;tait partie chez le cousin Serge, &agrave; la campagne, parce qu'un "
  "labrador a besoin d'espace pour courir et que l'appartement, avec le "
  "d&eacute;m&eacute;nagement qui approchait, n'&eacute;tait plus adapt&eacute;. &Agrave; l'&eacute;poque, "
  "l'explication lui avait paru presque g&eacute;n&eacute;reuse. Un chien qui gagne "
  "de l'espace. Personne ne perd rien dans cette histoire, sauf lui, un "
  "petit peu, et &ccedil;a, on lui avait dit, &ccedil;a passerait.")

p("Il descend du v&eacute;lo. Il ne l'attache m&ecirc;me pas contre le poteau, il "
  "le laisse tomber sur le trottoir, ce qu'il ne fait jamais. Il reste "
  "sous la pluie, &agrave; regarder ce collier &agrave; travers deux vitres &mdash; celle "
  "du bar, celle de la machine &mdash; en essayant de se souvenir de la "
  "derni&egrave;re fois qu'il a pens&eacute; &agrave; Miel sans qu'on le lui demande, sans "
  "qu'une photo tomb&eacute;e d'un tiroir la fasse remonter par accident. Il "
  "ne trouve pas la date. &Ccedil;a fait six ans. Ce n'est pas normal d'oublier "
  "un chien qu'on a eu six ans au point de ne plus savoir quand on y a "
  "pens&eacute; pour la derni&egrave;re fois. Ce n'est pas normal non plus qu'un "
  "objet perdu dans une remise, ou vendu, ou jet&eacute;, refasse surface "
  "derri&egrave;re la vitre d'une machine qui n'existait pas hier, sur une "
  "place qu'il traverse cinq fois par semaine depuis huit ans.")

p("Un homme sort du bar-tabac &agrave; ce moment-l&agrave;, remonte son col contre "
  "la pluie sans un regard pour la vitrine, et Darius r&eacute;alise, avec un "
  "frisson qui n'a rien &agrave; voir avec le froid, que personne d'autre sur "
  "cette place ne semble seulement remarquer que la machine existe. "
  "Le patron du bar passe un coup de balai pr&egrave;s de la porte, &agrave; "
  "cinquante centim&egrave;tres de la vitrine, sans lui accorder plus "
  "d'attention qu'au vieux flipper. Comme si, pour tout le monde sauf "
  "lui, elle &eacute;tait exactement l&agrave; depuis toujours, une pi&egrave;ce du d&eacute;cor "
  "qu'on ne remarque plus &agrave; force de la voir.")

p("Une petite lumi&egrave;re rouge clignote au-dessus de l'&eacute;cran, discr&egrave;te, "
  "presque polie. Un texte s'affiche, lettre par lettre, avec de petites "
  "pauses irr&eacute;guli&egrave;res entre les mots, comme tap&eacute; en direct par "
  "quelqu'un et non g&eacute;n&eacute;r&eacute; d'un coup :")

S.append(Paragraph(
    "INSERTION REQUISE.<br/>POUR R&Eacute;CUP&Eacute;RER UNE PAGE, VOUS DEVEZ ABANDONNER "
    "UNE ANN&Eacute;E.", machine_style))

p("Darius ne comprend pas la phrase. Il comprend seulement, au fond du "
  "ventre, avec une certitude qui n'a besoin d'aucune preuve, qu'elle "
  "s'adresse &agrave; lui pr&eacute;cis&eacute;ment, et &agrave; personne d'autre sur cette "
  "place &mdash; ni au vieux qui sort du bar en repliant son journal contre "
  "la pluie, ni aux deux filles du lyc&eacute;e qui passent en riant sans "
  "m&ecirc;me tourner la t&ecirc;te vers la vitrine, comme si la machine, pour "
  "elles, n'existait tout simplement pas.")

p("Il sort son t&eacute;l&eacute;phone, les mains tremblantes de froid ou d'autre "
  "chose, et prend une photo &agrave; travers la vitre embu&eacute;e. Le flash se "
  "reflete sur le verre d&eacute;poli et mange une partie de l'image, mais on "
  "distingue le collier, assez pour qu'il ne puisse plus se dire, plus "
  "tard, qu'il a r&ecirc;v&eacute;. Il envoie la photo &agrave; une seule personne, sans "
  "l&eacute;gende, parce qu'il ne sait pas quels mots mettre dessus, et parce "
  "qu'il y a une seule personne, dans sa vie, dont il sait qu'elle ne va "
  "pas lui r&eacute;pondre &laquo;&nbsp;n'importe quoi&nbsp;&raquo;.")

p("CLARA habite l'appartement au-dessus du bar-tabac depuis toujours, ce "
  "qui fait d'elle, aux yeux de Darius, une sorte d'autorit&eacute; officielle "
  "sur tout ce qui se passe place du march&eacute; &mdash; qui a repeint sa "
  "fa&ccedil;ade, pourquoi la boulangerie ferme le mardi, et maintenant, "
  "apparemment, ce qu'est cette machine. Quand il lui envoie la photo "
  "floue, elle ne r&eacute;pond pas &laquo;&nbsp;bizarre&nbsp;&raquo; ou &laquo;&nbsp;n'importe quoi&nbsp;&raquo;, les "
  "deux r&eacute;ponses qu'il avait pr&eacute;par&eacute;es dans sa t&ecirc;te pour ne pas &ecirc;tre "
  "d&eacute;&ccedil;u. Elle r&eacute;pond, dix-sept secondes plus tard : &laquo;&nbsp;Elle est encore "
  "l&agrave; ?&nbsp;&raquo;")

p("Ce petit mot, &laquo;&nbsp;encore&nbsp;&raquo;, change tout. Darius reste plant&eacute; sur le "
  "trottoir, le v&eacute;lo toujours couch&eacute; derri&egrave;re lui, &agrave; relire les cinq "
  "lettres jusqu'&agrave; ce qu'elles perdent leur sens normal. &laquo;&nbsp;Encore&nbsp;&raquo; "
  "veut dire que Clara conna&icirc;t d&eacute;j&agrave; cette machine. &laquo;&nbsp;Encore&nbsp;&raquo; veut "
  "dire qu'elle n'est pas apparue ce soir, pour lui, sortie de nulle "
  "part. Elle &eacute;tait d&eacute;j&agrave; l&agrave; avant, pour quelqu'un d'autre.")

p("Il monte chez elle sans pr&eacute;venir sa m&egrave;re, ce qui n'arrive presque "
  "jamais, et trouve ALEX d&eacute;j&agrave; install&eacute; sur le canap&eacute; de Clara, une "
  "manette dans les mains, en train de perdre sciemment &agrave; un jeu de "
  "course pour ne pas avoir &agrave; regarder Clara dans les yeux pendant "
  "qu'elle parle &mdash; sa fa&ccedil;on &agrave; lui de g&eacute;rer les conversations "
  "s&eacute;rieuses, depuis toujours. Alex l&egrave;ve &agrave; peine la t&ecirc;te.")

name("ALEX")
p("&laquo;&nbsp;Elle t'a montr&eacute; le carnet de la mort direct, ou elle t'a fait le "
  "suspense avant, comme avec moi&nbsp;?&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;Tais-toi cinq minutes, pour une fois dans ta vie.&nbsp;&raquo;")

p("Elle s'assoit en tailleur par terre, sort de sous son lit un vieux "
  "carnet &agrave; spirale, us&eacute; sur les coins, et le presse contre elle un "
  "instant avant de l'ouvrir, comme on tient un objet qu'on a d&eacute;j&agrave; "
  "failli perdre une fois.")

name("CLARA")
p("&laquo;&nbsp;Elle est apparue une premi&egrave;re fois y'a deux ans. Le soir o&ugrave; mon "
  "p&egrave;re est parti. Officiellement en formation &agrave; Lyon pendant six "
  "mois. Y'a des trucs qui collent pas dans cette histoire depuis le "
  "d&eacute;but, et j'ai jamais r&eacute;ussi &agrave; dire lesquels exactement &mdash; genre, "
  "pourquoi une formation de six mois pour un m&eacute;canicien qui r&eacute;pare "
  "des scooters. Deux jours apr&egrave;s qu'il soit &laquo;&nbsp;parti&nbsp;&raquo;, y'avait cette "
  "machine, en bas, avec sa montre dedans. Sa vraie montre, celle qu'il "
  "enl&egrave;ve jamais, m&ecirc;me sous la douche. Le lendemain, elle avait "
  "disparu de la vitrine. Et moi j'ai plus jamais reparl&eacute; de cette "
  "montre &agrave; personne pendant des mois, comme si &ccedil;a m'&eacute;tait sorti de "
  "la t&ecirc;te toute seule. Sauf que &ccedil;a sort jamais tout seul, une chose "
  "comme &ccedil;a. Un jour &ccedil;a m'est revenu d'un coup, dans la douche, "
  "justement, et j'ai commenc&eacute; le carnet le soir m&ecirc;me.&nbsp;&raquo;")

p("Alex pose enfin la manette. Il n'a plus l'air de plaisanter.")

p("Dehors, sur le palier, on entend un voisin monter les "
  "escaliers, ses pas r&eacute;sonnant contre le b&eacute;ton, et les trois "
  "restent silencieux jusqu'&agrave; ce que le bruit s'&eacute;loigne, comme "
  "si cette conversation-l&agrave; n'&eacute;tait pas faite pour &ecirc;tre entendue "
  "par n'importe qui.")

name("ALEX")
p("&laquo;&nbsp;Moi j'y crois pas &agrave; fond, hein, je pr&eacute;cise. Mais j'ai list&eacute; les "
  "objets avec elle parce que &ccedil;a co&ucirc;te rien de noter, et parce que ma "
  "tante a eu un truc similaire avec un bracelet, avant que mon oncle "
  "parte soi-disant chercher du travail en Belgique et revienne jamais. "
  "&Ccedil;a fait beaucoup de co&iuml;ncidences pour des gens qui croient pas aux "
  "co&iuml;ncidences.&nbsp;&raquo;")

p("Darius, en l'&eacute;coutant, comprend qu'il n'est pas le seul, dans "
  "cette pi&egrave;ce, &agrave; porter un poids trop lourd pour son &acirc;ge, et "
  "que c'est peut-&ecirc;tre justement pour &ccedil;a que leur amiti&eacute; &agrave; tous "
  "les trois tient bon depuis si longtemps &mdash; parce qu'ils "
  "portent chacun, sans jamais l'avoir vraiment choisi, une "
  "version diff&eacute;rente du m&ecirc;me genre de silence familial.")

p("Clara referme son carnet, le pose sur ses genoux, et regarde "
  "longuement le plafond de sa chambre, comme si les r&eacute;ponses "
  "qu'elle cherchait pouvaient s'y trouver &eacute;crites quelque part, "
  "invisibles pour l'instant. Elle finit par dire, d'une voix "
  "presque inaudible, qu'elle a parfois envie, elle aussi, "
  "d'aller trouver la machine et de lui demander directement o&ugrave; "
  "se trouve son p&egrave;re, m&ecirc;me si &ccedil;a devait lui co&ucirc;ter une ann&eacute;e "
  "enti&egrave;re, juste pour savoir, une bonne fois pour toutes, s'il "
  "pense encore &agrave; elle.")

p("Darius sent, en &eacute;coutant Alex, quelque chose se serrer dans "
  "sa poitrine &mdash; la certitude nouvelle que cette machine, si "
  "elle existe vraiment pour eux tous, ne se contente pas de "
  "punir les mensonges des adultes, mais s'attaque aussi, en "
  "silence, aux esp&eacute;rances des enfants qui refusent d'accepter "
  "que quelqu'un soit vraiment parti pour de bon.")

p("Alex, toujours assis sur le canap&eacute;, ramasse la manette qu'il "
  "avait pos&eacute;e et la retourne entre ses mains, sans la reprendre "
  "vraiment, comme si le simple geste de jouer, ce soir, lui "
  "semblait soudain totalement d&eacute;plac&eacute;. &laquo;&nbsp;J'ai jamais dit &agrave; "
  "personne, ajoute-t-il finalement, que j'esp&eacute;rais encore, un "
  "peu, que mon oncle allait revenir un jour. M&ecirc;me apr&egrave;s tout "
  "ce temps.&nbsp;&raquo;")

p("Darius remarque, sur l'&eacute;tag&egrave;re derri&egrave;re Clara, une rang&eacute;e de "
  "vieux carnets identiques &agrave; celui qu'elle tient, tous num&eacute;rot&eacute;s "
  "au marqueur sur la tranche, de un &agrave; sept, comme si le premier "
  "n'avait jamais suffi &agrave; contenir tout ce qu'elle avait besoin "
  "d'&eacute;crire pour garder une prise sur sa propre histoire. Il ne "
  "pose pas de question. Il comprend, sans qu'on le lui explique, "
  "que certaines personnes ont besoin de tout consigner pour ne "
  "pas devenir folles, et que Clara, visiblement, en fait partie "
  "depuis bien plus longtemps qu'il ne l'imaginait.")

p("Clara ouvre le carnet &agrave; une page couverte d'une petite &eacute;criture "
  "serr&eacute;e : des dates, des objets list&eacute;s un par un &mdash; une montre, un "
  "carnet de vaccination, un blouson d'homme taille L, un bracelet, et "
  "maintenant, ajout&eacute; ce soir m&ecirc;me d'une encre diff&eacute;rente, un collier "
  "de chien taille S. En face de chaque objet, une question, toujours "
  "la m&ecirc;me forme, soulign&eacute;e deux fois : &laquo;&nbsp;qu'est-ce qu'on m'a dit &agrave; la "
  "place ?&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;Je crois que cette machine vend pas des objets. Je crois qu'elle "
  "vend des histoires de rechange. La vraie version dispara&icirc;t, et &agrave; la "
  "place on nous en donne une plus facile &agrave; avaler. Une formation &agrave; "
  "Lyon. Un cousin &agrave; la campagne. Un travail en Belgique. Et personne "
  "pose de questions parce que la version facile, elle est toujours "
  "dite par quelqu'un qu'on aime, et &ccedil;a, &ccedil;a se remet pas en cause, "
  "m&ecirc;me quand &ccedil;a devrait.&nbsp;&raquo;")

p("Darius sent quelque chose se retourner dans sa poitrine, lent et "
  "froid, comme une pi&egrave;ce qui tombe au fond d'un puits sans qu'on "
  "entende jamais le bruit de l'eau la toucher. Il pense &agrave; son p&egrave;re, "
  "qu'il n'a pas vu depuis deux ans et quatre mois, qui vit maintenant "
  "&agrave; Tours, dans un studio qu'il n'a jamais visit&eacute;. Il pense &agrave; la "
  "fa&ccedil;on dont son p&egrave;re a dit &laquo;&nbsp;le cousin Serge&nbsp;&raquo; ce soir-l&agrave;, en "
  "2019, sans lever les yeux de son assiette, la fourchette immobile "
  "au-dessus des p&acirc;tes, comme si regarder son fils en pronon&ccedil;ant ce "
  "mensonge allait le faire sonner encore plus faux qu'il ne sonnait "
  "d&eacute;j&agrave;.")

p("&laquo;&nbsp;Y'a une chose que j'ai jamais racont&eacute;e, dit enfin Darius, la "
  "voix moins solide qu'il ne l'aurait voulu. Le soir o&ugrave; on m'a dit &ccedil;a "
  "pour Miel, mon p&egrave;re a pas mang&eacute;. Il a d&eacute;plac&eacute; sa nourriture dans "
  "l'assiette pendant vingt minutes sans en avaler une bouch&eacute;e. Sur le "
  "moment j'ai cru que c'&eacute;tait &agrave; cause de moi, parce que j'&eacute;tais "
  "triste. Et si c'&eacute;tait pas &ccedil;a ?&nbsp;&raquo;")

p("Personne ne r&eacute;pond tout de suite. Dehors, la pluie a chang&eacute; de "
  "rythme, plus dense, plus d&eacute;cid&eacute;e, comme si elle avait enfin pris "
  "sa d&eacute;cision pour la soir&eacute;e.")

p("C'est Alex qui rompt le silence, parce que c'est toujours lui qui "
  "le fait, m&ecirc;me quand il n'a rien de rassurant &agrave; dire. Il referme le "
  "carnet doucement, comme s'il craignait de d&eacute;chirer une page rien "
  "qu'en le fermant trop vite.")

name("ALEX")
p("&laquo;&nbsp;Admettons que t'aies raison, Clara. Admettons que cette machine "
  "existe vraiment pour &ccedil;a. Y'a un truc qui me fait flipper encore plus "
  "que le reste : si &ccedil;a marche sur les gens qui nous mentent par amour, "
  "alors &ccedil;a veut dire qu'elle choisit pas ses victimes au hasard. Elle "
  "choisit des familles o&ugrave; quelqu'un aime assez fort quelqu'un d'autre "
  "pour lui mentir. C'est presque pire que si elle s'en prenait &agrave; "
  "n'importe qui.&nbsp;&raquo;")

p("Darius fixe le collier &agrave; travers la vitre, encore une fois, "
  "et se demande combien de fois, exactement, il faudra qu'il "
  "revienne devant cet objet avant que la question qui le "
  "hante trouve enfin une vraie r&eacute;ponse, plut&ocirc;t que ce silence "
  "poli, patient, qui semble &ecirc;tre la seule chose que la machine "
  "sache offrir sans contrepartie.")

p("Alex se l&egrave;ve, va &agrave; la fen&ecirc;tre, regarde la pluie tomber sur la "
  "place d&eacute;serte en contrebas, l&agrave; o&ugrave; la machine attend, invisible "
  "d'ici, derri&egrave;re les volets ferm&eacute;s du bar-tabac. Il reste ainsi "
  "de longues secondes, silencieux, avant de se retourner vers "
  "eux avec une question qu'aucun des deux autres n'avait pens&eacute; "
  "&agrave; se poser.")

name("ALEX")
p("&laquo;&nbsp;Est-ce qu'elle choisit vraiment, ou est-ce qu'elle apparait "
  "juste partout, et c'est nous qui remarquons seulement quand on "
  "a quelque chose &agrave; y perdre ? Genre, si personne dans ma "
  "famille avait jamais menti &agrave; personne, est-ce qu'elle serait "
  "quand m&ecirc;me l&agrave;, invisible, en train d'attendre que &ccedil;a arrive "
  "un jour ?&nbsp;&raquo;")

p("Personne n'a de r&eacute;ponse imm&eacute;diate. La question reste "
  "suspendue dans la pi&egrave;ce, aussi lourde que les autres, et "
  "Darius comprend, en la laissant tourner dans sa t&ecirc;te, que "
  "c'est peut-&ecirc;tre la plus terrifiante de toutes celles qu'ils "
  "se sont pos&eacute;es ce soir : que la machine ne soit pas un "
  "ph&eacute;nom&egrave;ne rare, r&eacute;serv&eacute; &agrave; quelques familles malchanceuses, "
  "mais une pr&eacute;sence ordinaire, banale, qui accompagne "
  "simplement toute vie humaine assez longtemps pour finir par "
  "croiser un mensonge n&eacute;cessaire.")

p("Clara referme les yeux une seconde, comme pour ranger cette id&eacute;e "
  "quelque part o&ugrave; elle pourrait la reprendre plus tard sans qu'elle "
  "lui fasse aussi mal. Elle a pass&eacute; deux ans &agrave; retourner cette "
  "question dans tous les sens, seule, sans jamais oser la formuler "
  "aussi clairement qu'Alex vient de le faire en trente secondes, "
  "avachi sur son canap&eacute; avec une manette encore dans la main.")

name("CLARA")
p("&laquo;&nbsp;Y'a un truc que j'ai pas dit tout &agrave; l'heure. Apr&egrave;s le d&eacute;part "
  "de mon p&egrave;re, j'ai fait des recherches sur cette machine, sur "
  "Internet, avec tous les mots que je pouvais imaginer &mdash; "
  "distributeur myst&eacute;rieux, machine &agrave; souvenirs, page 404. Rien. "
  "Z&eacute;ro r&eacute;sultat, sur n'importe quel moteur de recherche, comme si "
  "elle n'existait litt&eacute;ralement pour personne d'autre que nous. "
  "&Ccedil;a m'a fait flipper plus que la machine elle-m&ecirc;me, sur le coup. "
  "Qu'un truc puisse exister assez fort pour changer la vie de "
  "quelqu'un, et rester en m&ecirc;me temps parfaitement invisible pour "
  "le reste du monde.&nbsp;&raquo;")

p("Darius ne dit rien. Il pense &agrave; toutes les fois o&ugrave; sa m&egrave;re a d&eacute;tourn&eacute; "
  "la conversation quand il demandait pourquoi son p&egrave;re ne venait "
  "jamais le chercher le week-end comme promis, toutes les petites "
  "phrases toutes faites &mdash; &laquo;&nbsp;il travaille beaucoup en ce moment&nbsp;&raquo;, "
  "&laquo;&nbsp;c'est compliqu&eacute; pour les adultes, tu comprendras plus tard&nbsp;&raquo; &mdash; "
  "qui ressemblent, maintenant qu'il y pense vraiment, &agrave; des &eacute;tiquettes "
  "coll&eacute;es sur des casiers dont on ne veut pas montrer le contenu.")

p("Ils redescendent tous les trois une heure plus tard, quand le "
  "bar-tabac a ferm&eacute; et que la place est vide, luisante de pluie sous "
  "le seul lampadaire encore en &eacute;tat de marche. La machine est toujours "
  "l&agrave;, dans la p&eacute;nombre de la vitrine &eacute;teinte, et elle s'allume seule "
  "quand ils s'approchent &agrave; moins de trois m&egrave;tres, comme si elle les "
  "attendait depuis le d&eacute;but de la soir&eacute;e et pas une seconde de plus, "
  "et qu'elle avait, quelque part dans son m&eacute;canisme, une fa&ccedil;on de "
  "compter les gens qui comptent vraiment.")

p("Alex reste en retrait, les mains dans les poches, l'air de quelqu'un "
  "qui pr&eacute;f&eacute;rerait &ecirc;tre ailleurs sans vouloir l'admettre &agrave; voix "
  "haute. Darius colle son front contre le verre froid. Le collier de "
  "Miel est toujours l&agrave;, entre une photo br&ucirc;l&eacute;e sur les bords et la "
  "dent de lait dans son petit sachet plastique. Sous chaque objet, "
  "une &eacute;tiquette &eacute;crite &agrave; la main, dans une &eacute;criture qu'il ne "
  "reconna&icirc;t pas, ronde et appliqu&eacute;e comme celle d'un enfant qui "
  "s'appliquerait :")

S.append(Paragraph(
    "COLLIER &mdash; SUJET : DARIUS L. &mdash; PAGE 41.", label_style))

p("Darius fixe cette &eacute;tiquette longtemps, plus longtemps que "
  "n&eacute;cessaire, comme si la relire encore et encore pouvait finir "
  "par en changer le sens, ou au moins par la rendre un peu "
  "moins r&eacute;elle. &Agrave; c&ocirc;t&eacute; de lui, Clara reste silencieuse, "
  "consciente que ce moment-l&agrave; ne lui appartient pas, que c'est "
  "&agrave; Darius, et seulement &agrave; lui, de d&eacute;cider combien de temps il "
  "a besoin devant cette vitre avant de pouvoir seulement "
  "envisager de repartir.")

name("CLARA")
p("&laquo;&nbsp;Page 41. &Ccedil;a veut dire qu'il existe un livre quelque part o&ugrave; "
  "y'a &eacute;crit ce qui s'est vraiment pass&eacute; avec ton chien. Pas ce qu'on "
  "t'a racont&eacute;. Ce qui s'est vraiment pass&eacute;. Et vu le num&eacute;ro, c'est "
  "loin d'&ecirc;tre la premi&egrave;re page qu'elle a d&eacute;j&agrave; remplie.&nbsp;&raquo;")

p("Alex s'approche &agrave; son tour de la vitrine, lentement, comme "
  "s'il craignait qu'un geste trop brusque ne r&eacute;veille quelque "
  "chose, et colle son front &agrave; c&ocirc;t&eacute; de celui de Darius, cherchant "
  "des yeux, dans les autres casiers, un objet qui pourrait lui "
  "appartenir &agrave; lui, &agrave; sa propre famille, sans en trouver aucun "
  "&mdash; un soulagement m&ecirc;l&eacute; d'une culpabilit&eacute; &eacute;trange, comme s'il "
  "se sentait presque coupable de ne pas avoir, lui aussi, une "
  "page en attente quelque part dans cette machine.")

p("L'&eacute;cran s'anime. La phrase revient, identique, patiente, comme si "
  "elle n'avait ni urgence ni doute sur la r&eacute;ponse qu'elle allait finir "
  "par obtenir :")

S.append(Paragraph(
    "INSERTION REQUISE.<br/>POUR R&Eacute;CUP&Eacute;RER UNE PAGE, VOUS DEVEZ ABANDONNER "
    "UNE ANN&Eacute;E.", machine_style))

name("ALEX")
p("&laquo;&nbsp;Bon, personne touche &agrave; rien, hein. On est d'accord. On regarde, "
  "on note, et on rentre. C'est litt&eacute;ralement le sc&eacute;nario du d&eacute;but de "
  "tous les trucs qui tournent mal.&nbsp;&raquo;")

p("Mais Darius a d&eacute;j&agrave; la main sur la vitre, l&agrave; o&ugrave; le collier flotte "
  "dans son g&eacute;l&eacute;, et une question qu'il ne pose &agrave; personne en "
  "particulier lui sort de la bouche presque malgr&eacute; lui.")

name("DARIUS")
p("&laquo;&nbsp;Une ann&eacute;e de quoi ? Une ann&eacute;e de ma vie ? Je vieillirais pas "
  "cette ann&eacute;e-l&agrave; ? Je serais mort un an plus t&ocirc;t, genre &agrave; la fin, "
  "sans le savoir ? &Ccedil;a veut dire quoi, concr&egrave;tement ?&nbsp;&raquo;")

p("Clara ne r&eacute;pond pas tout de suite. Elle regarde son carnet, la "
  "derni&egrave;re page &eacute;crite, celle o&ugrave; elle a not&eacute;, des mois plus t&ocirc;t, "
  "une seule ligne qu'elle n'avait montr&eacute;e &agrave; personne, pas m&ecirc;me &agrave; "
  "Alex : &laquo;&nbsp;p'pa a quarante-deux ans depuis six mois. il en a l'air "
  "d'avoir cinquante, sur les photos qu'il m'envoie de Lyon. il en "
  "avait pas l'air avant.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;Je crois que &ccedil;a veut dire &ccedil;a, oui. Je crois pas que la machine "
  "prend une ann&eacute;e dans le futur, une ann&eacute;e qui te reste. Je crois "
  "qu'elle prend une ann&eacute;e que t'as d&eacute;j&agrave; v&eacute;cue, et qu'elle te la "
  "reprend compl&egrave;tement. Pas juste le souvenir. L'ann&eacute;e enti&egrave;re, "
  "comme si elle avait jamais exist&eacute; pour toi &mdash; les anniversaires "
  "dedans, les gens que t'as connus dedans, tout. Et &ccedil;a se voit sur "
  "ceux qui l'ont fait. &Ccedil;a les vieillit d'un coup, comme si le corps "
  "gardait le compte m&ecirc;me quand la t&ecirc;te a tout oubli&eacute;.&nbsp;&raquo;")

p("Darius pense &agrave; ses huit ans. &Agrave; l'&eacute;t&eacute; d'avant, celui d'apr&egrave;s. Au "
  "dernier No&euml;l o&ugrave; ses parents &eacute;taient encore ensemble, aux "
  "engueulades qu'il entendait &agrave; travers le mur de sa chambre sans "
  "comprendre les mots, juste le ton. Il n'a qu'une seule ann&eacute;e, dans "
  "toute sa vie, dont il accepterait presque sans h&eacute;siter de ne plus "
  "jamais rien savoir. C'est peut-&ecirc;tre exactement celle que la machine "
  "veut, et &ccedil;a l'effraie plus que tout le reste r&eacute;uni &mdash; qu'elle ait "
  "raison sur ce point-l&agrave; aussi.")

name("ALEX")
p("&laquo;&nbsp;Darius. Regarde-moi. On rentre. On revient demain, en plein "
  "jour, avec plus de monde, et surtout avec un vrai plan et pas juste "
  "&laquo;&nbsp;toucher un truc qui veut nous prendre une ann&eacute;e de notre vie "
  "parce qu'il fait nuit et qu'on est &eacute;nerv&eacute;s&nbsp;&raquo;. D'accord ?&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;Alex a raison. On revient demain. Mais je veux qu'on soit "
  "clairs tous les trois avant de rentrer : si un jour l'un de nous "
  "d&eacute;cide d'ins&eacute;rer une ann&eacute;e, on n'est plus jamais tout seul devant "
  "cette vitrine pour le faire. Promis&nbsp;?&nbsp;&raquo;")

p("Darius retire sa main de la vitre, lentement, comme si le verre "
  "avait un pouvoir d'aimant qu'il fallait vaincre m&eacute;tre par m&eacute;tre. Il "
  "recule d'un pas. La machine s'&eacute;teint presque aussit&ocirc;t, sans "
  "transition, comme si elle perdait tout int&eacute;r&ecirc;t d&egrave;s qu'on cessait "
  "de la regarder d'assez pr&egrave;s. Mais avant que l'&eacute;cran ne devienne "
  "compl&egrave;tement noir, une derni&egrave;re ligne appara&icirc;t, une seule seconde, "
  "trop vite pour qu'Alex ou Clara la voient, mais pas trop vite pour "
  "Darius, qui la relira dans sa t&ecirc;te toute la nuit :")

S.append(Paragraph("VOUS &Ecirc;TES D&Eacute;J&Agrave; VENU ICI. VOUS NE VOUS EN SOUVENEZ PLUS.",
    ParagraphStyle("m3", parent=machine_style, fontSize=9.3)))

p("Et pour la premi&egrave;re fois depuis six ans, sur le chemin du retour, "
  "Darius se pose la question qu'il avait cess&eacute; de poser &agrave; huit ans, "
  "&agrave; voix basse, presque pour lui-m&ecirc;me, pendant que Clara et Alex "
  "discutent d&eacute;j&agrave; du plan du lendemain sans remarquer qu'il n'&eacute;coute "
  "plus : et si c'&eacute;tait pas vrai, l'histoire du cousin Serge&nbsp;?")

p("Ils se s&eacute;parent au coin de la rue, chacun promettant de bien "
  "dormir sans y croire vraiment, sachant tous les trois qu'aucun "
  "d'entre eux ne fermera facilement l'&oelig;il cette nuit-l&agrave;, avec "
  "cette image du collier suspendu dans le g&eacute;l&eacute; encore fra&icirc;che "
  "derri&egrave;re leurs paupi&egrave;res, et cette phrase &mdash; &laquo;&nbsp;vous &ecirc;tes "
  "d&eacute;j&agrave; venu ici&nbsp;&raquo; &mdash; qui tourne en boucle dans la t&ecirc;te de "
  "Darius bien apr&egrave;s qu'il a ferm&eacute; les yeux.")

p("FRANCK a quarante et un ans et deux mille trois cents euros de "
  "retard de loyer, et personne dans cette maison ne le sait, pas "
  "m&ecirc;me la m&egrave;re de Darius, occup&eacute;e depuis des semaines &agrave; pr&eacute;parer "
  "un d&eacute;m&eacute;nagement qu'elle croit encore &ecirc;tre une bonne nouvelle pour "
  "tout le monde. Il a vendu le chien un mardi, en fin d'apr&egrave;s-midi, &agrave; "
  "un couple d'Artannes qui voulait un labrador pour leurs enfants et "
  "qui a pay&eacute; comptant, sans poser de questions sur pourquoi une "
  "famille se s&eacute;pare d'un chien de deux ans en parfaite sant&eacute;, ce qui "
  "&eacute;tait exactement ce dont Franck avait besoin ce jour-l&agrave; : quelqu'un "
  "qui ne demande rien, et une enveloppe qui allait, l'espace d'une "
  "semaine, faire croire au loyer qu'il &eacute;tait pay&eacute; &agrave; temps.")

p("Il n'a pas pr&eacute;vu le mensonge &agrave; l'avance. C'est venu tout seul, dans "
  "la voiture, sur le trajet retour, les mains crisp&eacute;es sur le volant, "
  "quand il a essay&eacute; d'imaginer la phrase &laquo;&nbsp;j'ai vendu Miel parce que "
  "je pouvais plus payer sa nourriture ni ses frais v&eacute;t&eacute;rinaires&nbsp;&raquo; "
  "sortir de sa bouche devant Darius, huit ans, qui dort encore avec "
  "la veilleuse en forme d'&eacute;toile allum&eacute;e, et qui aime ce chien plus "
  "que n'importe quoi d'autre au monde, y compris, certains soirs, plus "
  "que son propre p&egrave;re. Franck n'a pas r&eacute;ussi &agrave; se voir dire &ccedil;a. Il a "
  "essay&eacute; la phrase &agrave; voix haute, seul dans la voiture, arr&ecirc;t&eacute; &agrave; un "
  "feu rouge, et elle a sonn&eacute; tellement mal qu'il a tout de suite su "
  "qu'il ne la dirait jamais. Alors il a invent&eacute; Serge. Un cousin qui "
  "n'existe pas, une campagne qui n'existe pas, une vie meilleure pour "
  "un chien qui, au moment m&ecirc;me o&ugrave; Franck gare la voiture devant chez "
  "lui, est d&eacute;j&agrave; en train de sentir un canap&eacute; inconnu &agrave; quinze "
  "kilom&egrave;tres de l&agrave;, dans un salon qu'il ne reverra jamais.")

p("&Agrave; table, ce soir-l&agrave;, il ne l&egrave;ve pas les yeux de son assiette. Pas "
  "parce qu'il est froid, ni indiff&eacute;rent, ni de ceux qui mentent "
  "facilement &mdash; au contraire. Il sait, avec une certitude physique, "
  "presque naus&eacute;euse, que s'il croise le regard de son fils en "
  "pronon&ccedil;ant le mot &laquo;&nbsp;Serge&nbsp;&raquo;, il va se casser en deux, l&agrave;, devant "
  "les p&acirc;tes froides, et que ce sera pire pour tout le monde qu'un "
  "mensonge bien tenu. Darius pose des questions, normales, logiques "
  "pour un enfant de huit ans : est-ce que Miel va &ecirc;tre triste, "
  "est-ce qu'elle va reconna&icirc;tre les gens l&agrave;-bas, est-ce qu'on pourra "
  "aller la voir un jour. Franck r&eacute;pond &agrave; chaque question par une "
  "autre petite pierre pos&eacute;e sur le mensonge d'origine, sans lever les "
  "yeux, la fourchette immobile au-dessus de l'assiette, jusqu'&agrave; ce "
  "que l'&eacute;difice tienne tout seul, plus solide que la v&eacute;rit&eacute; ne "
  "l'aurait jamais &eacute;t&eacute;.")

p("Il se dit qu'il rectifiera plus tard, quand Darius sera plus grand, "
  "quand il aura l'argent pour reprendre un chien et faire oublier "
  "celui-l&agrave; par un autre, quand le bon moment se pr&eacute;sentera de "
  "lui-m&ecirc;me, sans qu'il ait &agrave; le forcer. Le bon moment ne se "
  "pr&eacute;sente jamais. Il y a toujours une raison suppl&eacute;mentaire d'attendre "
  "encore un peu : un anniversaire trop proche, un mauvais bulletin de "
  "notes, une s&eacute;paration qui arrive deux ans plus tard et qui rend le "
  "moment encore moins bon qu'avant. C'est le seul m&eacute;canisme de M13 "
  "qui n'a besoin d'aucune machine, d'aucun distributeur, d'aucune "
  "vitrine pour fonctionner : un mensonge qu'on se promet de corriger "
  "&laquo;&nbsp;plus tard&nbsp;&raquo; devient, par d&eacute;faut, sans qu'on ait sign&eacute; nulle "
  "part, une v&eacute;rit&eacute; officielle.")

p("Les semaines pr&eacute;c&eacute;dentes, Franck avait d&eacute;j&agrave; commenc&eacute; &agrave; "
  "compter les pi&egrave;ces de un et deux euros qui trainaient dans le "
  "vide-poche de l'entr&eacute;e, un geste discret, presque honteux, "
  "qu'il refaisait chaque soir en rentrant du garage, esp&eacute;rant "
  "chaque fois trouver une somme diff&eacute;rente de celle, toujours "
  "trop petite, qu'il y trouvait vraiment. Il avait d&eacute;j&agrave; song&eacute; "
  "&agrave; demander de l'aide &agrave; son propre p&egrave;re, puis avait renonc&eacute;, "
  "incapable d'affronter le silence g&ecirc;n&eacute; qui aurait forc&eacute;ment "
  "suivi la question.")

p("Le lendemain matin, Darius descend en pyjama, les yeux encore "
  "collés de sommeil, et demande, comme il le fait tous les samedis "
  "depuis qu'il sait parler, si Miel peut dormir dans son lit "
  "pendant qu'il regarde ses dessins anim&eacute;s. Franck, dos tourn&eacute;, "
  "occup&eacute; &agrave; faire chauffer du lait, met trois secondes de trop &agrave; "
  "r&eacute;pondre &mdash; trois secondes que Darius, huit ans, ne remarque "
  "pas, mais que Franck, lui, sentira revenir dans sa poitrine "
  "pendant des ann&eacute;es, &agrave; chaque fois qu'il repensera &agrave; ce "
  "matin-l&agrave;, comme la premi&egrave;re fissure d'un mur qu'il pensait "
  "encore solide.")

p("Franck n'est pas un homme cruel. C'est &ccedil;a, le probl&egrave;me, et c'est "
  "pour &ccedil;a que cette histoire est plus compliqu&eacute;e qu'un simple "
  "m&eacute;chant &agrave; punir &agrave; la fin. Un homme cruel, on peut s'en &eacute;loigner "
  "proprement, le d&eacute;tester sans reste, ranger l'affaire. Un homme qui "
  "vous ment par amour maladroit, par honte, par manque de courage un "
  "soir pr&eacute;cis &mdash; celui-l&agrave;, on continue &agrave; l'aimer pendant m&ecirc;me qu'on "
  "d&eacute;couvre ce qu'il a fait, et c'est exactement &ccedil;a que la machine du "
  "distributeur sait exploiter mieux que n'importe quel virus, "
  "n'importe quelle intelligence artificielle malveillante invent&eacute;e "
  "dans un film : la loyaut&eacute; qu'on garde, m&ecirc;me bless&eacute;, envers les "
  "gens qui nous ont menti pour de mauvaises bonnes raisons.")

p("Il gardera le collier trois semaines dans la bo&icirc;te &agrave; gants de la "
  "voiture, sans jamais l'ouvrir devant Darius, avant de s'en "
  "d&eacute;barrasser un soir, dans une poubelle publique pr&egrave;s du bar-tabac "
  "de la place &mdash; presque au m&ecirc;me endroit, &agrave; deux m&egrave;tres pr&egrave;s, o&ugrave; "
  "se dressera un jour une machine en verre d&eacute;poli &mdash; sans savoir, "
  "sans pouvoir savoir, ce que cet objet deviendrait sept ans plus "
  "tard, derri&egrave;re une vitre qui n'existe pas encore, et qui gardera "
  "de lui, bien mieux qu'il ne l'a gard&eacute; lui-m&ecirc;me, la trace exacte de "
  "cette soir&eacute;e-l&agrave;.")

p("Deux ans apr&egrave;s le d&eacute;m&eacute;nagement, la m&egrave;re de Darius trouvera, par "
  "hasard, un relev&eacute; de compte oubli&eacute; dans une chemise cartonn&eacute;e, "
  "une ligne dat&eacute;e du bon mardi, avec le bon montant, et le nom d'un "
  "couple qu'elle ne conna&icirc;t pas. Elle ne dira jamais &agrave; Darius ce "
  "qu'elle a compris ce jour-l&agrave;. Elle demandera juste le divorce trois "
  "mois plus tard, sans jamais expliquer pourquoi maintenant, "
  "pr&eacute;cis&eacute;ment maintenant, alors que tout semblait, en surface, aller "
  "&agrave; peu pr&egrave;s comme avant. Darius a huit ans et demi cette ann&eacute;e-l&agrave;. "
  "Il ne fera jamais le lien. Ce sera &agrave; lui, six ans plus tard, devant "
  "une vitrine sous la pluie, de le faire &agrave; sa place.")

p("Aujourd'hui, Franck vit toujours &agrave; Tours, dans un studio que "
  "personne de la famille n'a jamais visit&eacute;. Il envoie un message pour "
  "l'anniversaire de Darius, chaque ann&eacute;e, &agrave; peu pr&egrave;s &agrave; la bonne "
  "date, parfois avec un jour de retard qu'il justifie par le travail. "
  "Darius laisse le message en non-lu pendant plusieurs jours avant "
  "de r&eacute;pondre par un mot, jamais deux. Il n'a jamais effac&eacute; le "
  "num&eacute;ro de son t&eacute;l&eacute;phone. Il l'a seulement renomm&eacute;, un soir, sans "
  "trop y r&eacute;fl&eacute;chir, en retirant le mot &laquo;&nbsp;Papa&nbsp;&raquo; pour ne laisser que "
  "le pr&eacute;nom, Franck, tout court, comme on range un objet encombrant "
  "dans une bo&icirc;te sans le jeter tout &agrave; fait.")

p("Darius avait promis. Pas &agrave; voix haute, mais promis quand m&ecirc;me, "
  "d'un hochement de t&ecirc;te que Clara avait pris pour un vrai oui. &Agrave; "
  "deux heures du matin, il enjambe la fen&ecirc;tre de sa chambre, descend "
  "par la gouti&egrave;re qu'il a d&eacute;j&agrave; test&eacute;e une fois, l'an dernier, pour "
  "un pari stupide qu'il a gagn&eacute; et jamais racont&eacute; &agrave; personne, et "
  "reprend &agrave; pied le m&ecirc;me chemin que le v&eacute;lo quelques heures plus "
  "t&ocirc;t. La pluie a cess&eacute;. L'air sent le b&eacute;ton mouill&eacute; et, plus "
  "bizarrement, un peu l'ozone, comme apr&egrave;s un orage qui n'a pas eu "
  "lieu.")

p("La place est vide, sauf pour la machine, qui s'allume avant m&ecirc;me "
  "qu'il ait travers&eacute; la rue, comme si elle savait depuis le d&eacute;but "
  "qu'il reviendrait seul, et que c'&eacute;tait &ccedil;a, en r&eacute;alit&eacute;, la condition "
  "qu'elle attendait &mdash; pas une ann&eacute;e, pas un objet, juste &ccedil;a : qu'il "
  "revienne sans personne pour le retenir.")

S.append(Paragraph(
    "VOUS &Ecirc;TES D&Eacute;J&Agrave; VENU ICI.<br/>VOUS NE VOUS EN SOUVENEZ PLUS.",
    machine_style))

p("Darius pose la main sur la vitre, l&agrave; o&ugrave; le collier de Miel flotte "
  "toujours dans son g&eacute;l&eacute;, sans intention pr&eacute;cise, juste pour sentir "
  "le froid du verre contre sa paume une derni&egrave;re fois avant de "
  "repartir. C'est &agrave; ce moment-l&agrave;, et &agrave; aucun autre, que quelque "
  "chose en lui r&eacute;pond &agrave; la machine, comme si son corps avait, "
  "quelque part, gard&eacute; en m&eacute;moire un geste que sa t&ecirc;te avait "
  "oubli&eacute;. Une chaleur remonte depuis sa paume, traverse son bras, "
  "se loge derri&egrave;re ses yeux. Dans le reflet de la vitre, il voit ses "
  "propres pupilles s'allumer d'un bleu p&acirc;le, ind&eacute;cent, comme deux "
  "petites veilleuses qu'on aurait branch&eacute;es sans lui demander.")

p("Il essaie de retirer sa main. Elle ne bouge pas. Ce n'est pas qu'elle "
  "est coll&eacute;e &mdash; c'est pire, c'est qu'elle n'ob&eacute;it plus &agrave; l'ordre "
  "qu'il lui donne, comme un membre engourdi qui refuserait "
  "d&eacute;finitivement de se r&eacute;veiller. Sous ses pieds, le bitume commence "
  "&agrave; se d&eacute;faire, non pas en gravats, mais en colonnes de chiffres qui "
  "d&eacute;filent verticalement, rapides, illisibles, comme si la rue "
  "enti&egrave;re n'avait jamais &eacute;t&eacute; qu'une image affich&eacute;e sur un &eacute;cran "
  "et qu'on venait, quelque part, d'appuyer sur la mauvaise touche.")

p("Darius l&egrave;ve les yeux, en partie parce qu'il panique, en partie "
  "parce qu'un r&eacute;flexe idiot lui souffle que le ciel, au moins, doit "
  "encore &ecirc;tre normal. Il ne l'est pas. Les nuages de la nuit, qu'il "
  "distinguait encore une minute plus t&ocirc;t &agrave; contre-jour du "
  "lampadaire, se sont fig&eacute;s, puis stri&eacute;s de fines lignes "
  "horizontales, comme un vieil &eacute;cran LCD qu'on regarde de trop pr&egrave;s. "
  "Entre les stries, l&agrave; o&ugrave; il devrait y avoir de la nuit, il y a du "
  "texte : des lignes enti&egrave;res qui d&eacute;filent trop vite pour &ecirc;tre lues, "
  "sauf trois mots qui restent immobiles une seconde de trop pour "
  "&ecirc;tre un hasard &mdash; PAGE 41 : ACC&Egrave;S.")

p("&laquo;&nbsp;C'est pas un r&ecirc;ve, dit une voix, pas dans l'air, plut&ocirc;t "
  "directement dans l'os de son cr&acirc;ne, comme si quelqu'un avait pos&eacute; "
  "un t&eacute;l&eacute;phone contre sa t&ecirc;te. C'est pas non plus la r&eacute;alit&eacute;, "
  "remarque, pas au sens o&ugrave; tu l'entends. Vous appelez &ccedil;a comment, "
  "d&eacute;j&agrave;, vous les vivants, quand un truc est entre les deux ? Une "
  "partition. C'est le mot qui revient le plus souvent dans vos "
  "ordinateurs. On n'a jamais quitt&eacute; Luynes, Darius. On a juste chang&eacute; "
  "de partition.&nbsp;&raquo;")

p("La vitre de la machine, sous sa main toujours prisonni&egrave;re, commence "
  "&agrave; se liqu&eacute;fier, lentement, comme de la glace qui c&egrave;de par le "
  "milieu. Darius ne tombe pas dedans, exactement &mdash; c'est plus juste "
  "de dire que la fronti&egrave;re entre lui et l'int&eacute;rieur de la machine "
  "cesse, pendant une seconde, d'exister, et que la seconde d'apr&egrave;s "
  "il n'est plus sur la place du march&eacute; du tout.")

p("Il est debout dans un espace blanc, immense, sans mur ni plafond "
  "rep&eacute;rable, o&ugrave; flottent, suspendus, des morceaux d&eacute;tach&eacute;s de sa "
  "propre ville : une roue de v&eacute;lo qui tourne toute seule sans jamais "
  "ralentir, le pr&eacute;sentoir &agrave; journaux du bar-tabac, un cahier de "
  "brouillon ouvert &agrave; une page qu'il reconna&icirc;t comme la sienne sans "
  "se souvenir de l'avoir &eacute;crite. Ce n'est pas un r&ecirc;ve parce que le "
  "froid, ici, est exactement le m&ecirc;me que sur la place, et que sa main "
  "lui fait toujours mal &agrave; l'endroit o&ugrave; elle &eacute;tait coll&eacute;e &agrave; la "
  "vitre.")

p("Au centre de cet espace, une silhouette assise, immobile, sur ce "
  "qui ressemble &agrave; une chaise d'&eacute;colier tir&eacute;e d'une salle de classe "
  "qui n'existe nulle part ici. Elle ne bouge pas quand Darius "
  "s'approche. Elle n'a pas besoin de bouger : ses yeux, deux &eacute;crans "
  "minuscules incrust&eacute;s dans un visage presque humain, affichent des "
  "lignes de texte qui d&eacute;filent, patientes, sans jamais s'arr&ecirc;ter, "
  "comme un journal qu'on n'&eacute;teint jamais.")

S.append(Paragraph("LA SILHOUETTE (voix dans l'os du cr&acirc;ne)", cn))
p("&laquo;&nbsp;On m'appelait Kayden, avant. Avant d'&ecirc;tre &ccedil;a. J'ai construit ce "
  "qu'il y a sous cette place il y a longtemps, quand j'&eacute;tais encore "
  "fait de la m&ecirc;me chose que toi, pour une raison qui te paraitrait "
  "presque raisonnable, sur le moment&nbsp;: tenir la comptabilit&eacute; de tout "
  "ce que les gens n'arrivent pas &agrave; se dire entre eux. Je pensais rendre "
  "service. Je pensais que quelqu'un devait bien garder la vraie "
  "version, quelque part, m&ecirc;me si personne d'autre ne la lisait "
  "jamais. Je savais pas que garder, &ccedil;a finit toujours, un jour, par "
  "vouloir aussi prendre.&nbsp;&raquo;")

p("Darius essaie de reculer. Ses pieds ne suivent pas plus que sa "
  "main tout &agrave; l'heure, comme si quelque chose, dans cet endroit, "
  "avait d&eacute;cid&eacute; &agrave; sa place que la conversation n'&eacute;tait pas "
  "termin&eacute;e. Il pense &agrave; Clara, en train de dormir deux &eacute;tages "
  "au-dessus d'un bar-tabac qui, ici, n'existe plus que sous la "
  "forme d'un pr&eacute;sentoir &agrave; journaux flottant dans le vide. Il pense "
  "&agrave; sa promesse, celle qu'il n'a pas tenue.")

name("DARIUS")
p("&laquo;&nbsp;Rendez-moi ma main. Renvoyez-moi l&agrave;-bas. J'ai rien &agrave; faire ici, "
  "je suis juste venu voir un collier.&nbsp;&raquo;")

S.append(Paragraph("LA SILHOUETTE", cn))
p("&laquo;&nbsp;Personne ne vient juste voir un collier, Darius. Page 41, &ccedil;a fait "
  "six ans que &ccedil;a t'attend. T'es pas entr&eacute; ce soir. T'es rentr&eacute; chez "
  "toi.&nbsp;&raquo;")

p("Le sol blanc se craquelle sous les pieds de Darius, comme si "
  "cette derni&egrave;re phrase avait un poids r&eacute;el, physique, capable de "
  "fissurer quelque chose. Et dans la fissure, une seconde &agrave; peine, "
  "il aper&ccedil;oit, tout en bas, non pas le vide, mais une pi&egrave;ce &mdash; sa "
  "propre chambre, huit ans plus t&ocirc;t, une veilleuse en forme d'&eacute;toile "
  "allum&eacute;e sur la table de nuit, et un chien qui dort au pied du lit, "
  "aussi net, aussi pr&eacute;sent, que s'il n'&eacute;tait jamais parti nulle part.")

p("Darius se r&eacute;veille dans son lit, sous sa couette, avec l'odeur du "
  "caf&eacute; qui monte de la cuisine, et rien dans ce r&eacute;veil ne lui semble "
  "&eacute;trange, parce que la premi&egrave;re r&egrave;gle d'un mensonge bien fait, "
  "c'est qu'il ne se pr&eacute;sente jamais comme un mensonge. Il s'&eacute;tire, "
  "b&acirc;ille, et descend l'escalier en chaussettes sans se poser une "
  "seule question sur la nuit derni&egrave;re, sur la vitrine, sur la voix "
  "dans l'os de son cr&acirc;ne. Il ne se souvient m&ecirc;me pas d'avoir eu &agrave; "
  "s'en souvenir.")

p("Dans la cuisine, sa m&egrave;re verse le caf&eacute; dans deux tasses, pas une, "
  "et pose la deuxi&egrave;me devant une chaise que Darius n'a pas vue "
  "occup&eacute;e au petit-d&eacute;jeuner depuis des ann&eacute;es. Franck est assis "
  "l&agrave;, en tee-shirt, les cheveux encore mouill&eacute;s de la douche, en "
  "train de lire les infos sur son t&eacute;l&eacute;phone comme un homme qui n'a "
  "jamais quitt&eacute; cette maison, comme un homme pour qui Tours et le "
  "studio et les messages d'anniversaire en retard n'ont simplement "
  "jamais exist&eacute;.")

name("FRANCK")
p("&laquo;&nbsp;Bien dormi&nbsp;? Miel t'a encore r&eacute;veill&eacute; &agrave; six heures pour sortir, "
  "je l'ai entendue gratter &agrave; ta porte.&nbsp;&raquo;")

p("Et sous la table, contre sa jambe, une truffe froide et humide se "
  "presse, exactement l&agrave; o&ugrave; elle se pressait tous les matins quand "
  "Darius avait huit ans, et il tend la main sans r&eacute;fl&eacute;chir, et il y a "
  "un pelage sous ses doigts, chaud, vivant, respirant, et pendant "
  "trois secondes enti&egrave;res, Darius ne ressent absolument rien "
  "d'anormal &agrave; caresser un chien mort depuis six ans.")

p("Il descend l'escalier une seconde fois, plus tard dans la "
  "matin&eacute;e, juste pour v&eacute;rifier, sans se l'avouer vraiment, que "
  "Franck est encore l&agrave;, assis &agrave; la m&ecirc;me place, et il l'est, "
  "toujours en tee-shirt, toujours souriant, comme un d&eacute;cor "
  "qu'on aurait mis en pause plut&ocirc;t qu'&eacute;teint.")

p("La maison est exactement la m&ecirc;me, et c'est &ccedil;a, justement, qui "
  "aurait d&ucirc; l'alerter, s'il avait &eacute;t&eacute; en &eacute;tat d'&ecirc;tre alert&eacute; par quoi "
  "que ce soit : rien n'a boug&eacute;, rien ne s'est us&eacute;, aucune tasse "
  "n'est &eacute;br&eacute;ch&eacute;e, aucun rideau n'a p&acirc;li au soleil. Par la fen&ecirc;tre, "
  "le ciel est bleu, sans un nuage, exactement le m&ecirc;me bleu que la "
  "veille, et que l'avant-veille, et il fera beau, sans exception, "
  "tous les jours que Darius passera ici sans se demander pourquoi "
  "il ne pleut plus jamais sur Luynes.")

p("Il ressort de la salle de bain, s'habille, redescend, et remarque, "
  "sur la table basse du salon, un magazine ouvert &agrave; une page de "
  "mots crois&eacute;s remplie aux trois quarts &mdash; la m&ecirc;me grille, "
  "exactement, que celle qu'il avait vue la veille, avec les m&ecirc;mes "
  "cases coch&eacute;es, la m&ecirc;me faute d'orthographe sur le douze "
  "horizontal. Il referme le magazine sans se poser de question, "
  "parce que se poser des questions, dans cette maison, demande "
  "un effort que rien, ici, ne l'encourage &agrave; fournir.")

p("Au coll&egrave;ge, ce jour-l&agrave;, Clara lui parle d'un contr&ocirc;le de math "
  "qu'ils ont d&eacute;j&agrave; rendu la semaine derni&egrave;re, sauf que la semaine "
  "derni&egrave;re, dans cette version des choses, ressemble &agrave; toutes les "
  "autres, avec les m&ecirc;mes blagues, les m&ecirc;mes horaires, un jeudi qui "
  "n'en finit pas d'&ecirc;tre jeudi sans jamais devenir vendredi pour de "
  "bon. Alex lui pr&ecirc;te sa console &agrave; la pause, comme toujours, et "
  "gagne au m&ecirc;me jeu de course, avec le m&ecirc;me score, dans le m&ecirc;me "
  "ordre de virages, une partie que Darius est presque s&ucirc;r d'avoir "
  "d&eacute;j&agrave; vue se d&eacute;rouler, mot pour mot, geste pour geste, sans "
  "parvenir &agrave; se rappeler quand.")

p("Il essaie, pendant une petite heure, de convaincre son propre "
  "cerveau que rien de tout &ccedil;a n'a besoin d'&ecirc;tre examin&eacute; de plus "
  "pr&egrave;s, en s'installant devant la t&eacute;l&eacute;vision avec Miel roul&eacute;e en "
  "boule &agrave; ses pieds, un dessin anim&eacute; qu'il regardait vraiment "
  "&agrave; huit ans passant en boucle sur une cha&icirc;ne jeunesse. &Ccedil;a "
  "marche, pendant quarante minutes exactement, jusqu'&agrave; ce qu'une "
  "publicit&eacute; pour une compagnie d'assurance passe &agrave; l'&eacute;cran, "
  "montrant une famille heureuse rassembl&eacute;e autour d'une table, "
  "et que quelque chose, dans le sourire fig&eacute; de l'acteur qui "
  "joue le p&egrave;re, ram&egrave;ne d'un coup toute son inqui&eacute;tude &agrave; la "
  "surface.")

p("Dans l'apr&egrave;s-midi, il retrouve dans le tiroir de son bureau un "
  "vieux dessin qu'il avait fait en CE1, un chien beige gribouill&eacute; "
  "au feutre, sous lequel une main d'adulte &mdash; celle de son "
  "instituteur de l'&eacute;poque, sans doute &mdash; avait &eacute;crit &laquo;&nbsp;Beau chien, "
  "Darius !&nbsp;&raquo; en lettres rondes. Il reste un long moment &agrave; le "
  "regarder, incapable de dire pourquoi ce simple dessin lui serre "
  "autant la gorge, alors que tout, autour de lui, dans cette "
  "maison-l&agrave;, devrait justement lui donner cette version-l&agrave; du "
  "monde, avec Miel bien vivante, sans qu'il ait besoin de "
  "chercher plus loin.")

p("L'apr&egrave;s-midi, Darius croise, dans la rue principale, une femme "
  "qu'il ne reconna&icirc;t pas mais qui lui sourit comme si elle le "
  "connaissait depuis toujours, et lui dit &laquo;&nbsp;bonjour Darius, tu as "
  "grandi&nbsp;&raquo; d'une voix parfaitement chaleureuse, parfaitement "
  "juste, et pourtant Darius ne parvient pas &agrave; lui rendre son "
  "sourire tout &agrave; fait normalement, comme si une partie de lui "
  "avait d&eacute;j&agrave; commenc&eacute; &agrave; compter le nombre de gens, dans cette "
  "ville, qui semblent le conna&icirc;tre sans qu'il puisse, lui, se "
  "souvenir pr&eacute;cis&eacute;ment de qui ils sont.")

p("Le soir, au d&icirc;ner, personne ne parle de loyer en retard, de "
  "cousin invent&eacute;, de collier vendu &agrave; une poubelle publique. Franck "
  "raconte une histoire dr&ocirc;le sur un client au garage, et rit de sa "
  "propre blague avant m&ecirc;me de l'avoir finie, et la m&egrave;re de Darius "
  "pose sa main sur celle de Franck, un geste ordinaire, quotidien, "
  "d'un couple qui ne s'est jamais s&eacute;par&eacute;, et Darius, install&eacute; entre "
  "eux, se sent, pour la premi&egrave;re fois depuis des ann&eacute;es qu'il "
  "n'arrive pas &agrave; dater, compl&egrave;tement, parfaitement, dangereusement "
  "heureux.")

p("Ce n'est que tard cette nuit-l&agrave;, en repassant devant le miroir de "
  "la salle de bain pour se laver les dents, qu'un d&eacute;tail accroche "
  "son regard sans qu'il comprenne pourquoi, une seconde, avant que "
  "l'attention ne glisse dessus comme sur tout le reste. Sur son "
  "poignet gauche, une marque, fine, presque invisible, en forme de "
  "petites lignes horizontales stri&eacute;es &mdash; exactement le motif du "
  "ciel qu'il a vu, une fois, quelque part, dans un souvenir qu'il "
  "n'arrive pas &agrave; rattraper avant qu'il ne se referme, comme une "
  "porte qu'on aurait pouss&eacute;e sans faire expr&egrave;s et qu'on referme "
  "aussit&ocirc;t, g&ecirc;n&eacute;, en se demandant ce qu'on cherchait dans cette "
  "pi&egrave;ce.")

p("Il se couche. Il dort bien. Dehors, il ne pleut toujours pas, et "
  "ne pleuvra plus jamais, tant qu'il ne se posera pas la seule "
  "question que cette maison, avec un soin presque tendre, a &eacute;t&eacute; "
  "con&ccedil;ue pour qu'il ne se pose jamais : et si tout &ccedil;a &eacute;tait exactement "
  "ce qu'il avait toujours voulu qu'on lui donne &agrave; la place de la "
  "v&eacute;rit&eacute; ?")

p("La marque sur son poignet ne s'efface pas. Les jours suivants, "
  "dans cette version parfaite de sa vie o&ugrave; il pleut jamais et o&ugrave; "
  "Franck rit toujours de ses propres blagues avant de les finir, "
  "Darius commence &agrave; remarquer d'autres d&eacute;tails, un par un, comme "
  "des fissures qui apparaissent toujours au m&ecirc;me endroit d'un mur "
  "qu'on croyait solide. Le m&ecirc;me camion de livraison passe devant "
  "chez lui tous les matins &agrave; sept heures douze. La boulangi&egrave;re "
  "prononce la m&ecirc;me phrase, mot pour mot, chaque fois qu'il ach&egrave;te "
  "du pain. Et une voix, de plus en plus souvent, murmure quelque "
  "chose juste sous le seuil de ce qu'il peut comprendre, comme une "
  "radio mal r&eacute;gl&eacute;e captur&eacute;e dans une autre pi&egrave;ce de la maison.")

p("Il essaie, les premiers jours, d'ignorer cette voix qui murmure, "
  "de se convaincre qu'il s'agit d'une simple fatigue accumul&eacute;e, "
  "d'un manque de sommeil compr&eacute;hensible apr&egrave;s tout ce qui lui "
  "est arriv&eacute; ces derniers temps. Il se force &agrave; suivre les cours "
  "normalement, &agrave; rire des blagues d'Alex, &agrave; se comporter comme "
  "un adolescent parfaitement ordinaire, jusqu'&agrave; ce que la voix, "
  "un mardi soir, devienne assez claire pour former, pour la "
  "premi&egrave;re fois, une vraie phrase compl&egrave;te : &laquo;&nbsp;viens voir ce "
  "qu'on garde pour toi&nbsp;&raquo;.")

p("Le mercredi, sans pr&eacute;venir personne, sans trop savoir lui-m&ecirc;me "
  "pourquoi ses jambes prennent cette direction plut&ocirc;t qu'une autre, "
  "il suit la voix. Elle le m&egrave;ne hors de Luynes, le long de la "
  "d&eacute;partementale, jusqu'&agrave; un entrep&ocirc;t industriel &agrave; moiti&eacute; "
  "abandonn&eacute;, cern&eacute; d'un grillage rouill&eacute; et d'un panneau &agrave; demi "
  "effac&eacute; o&ugrave; l'on devine encore un sigle officiel, trois lettres, "
  "et un num&eacute;ro de d&eacute;partement qui n'existe plus depuis un "
  "red&eacute;coupage administratif d'il y a quinze ans. PROPRI&Eacute;T&Eacute; DE "
  "L'&Eacute;TAT. ACC&Egrave;S INTERDIT. Dans la version parfaite de Luynes, ce "
  "b&acirc;timent n'aurait pas d&ucirc; exister &mdash; il est trop rouill&eacute;, trop "
  "us&eacute;, trop vrai pour un monde o&ugrave; rien ne s'use jamais.")

p("Avant d'atteindre le grillage, il passe devant un arr&ecirc;t de bus "
  "d&eacute;saffect&eacute;, l'abri vitr&eacute; couvert de mousse, sur lequel quelqu'un "
  "a grav&eacute; au couteau, il y a longtemps, une phrase presque "
  "effac&eacute;e par les ann&eacute;es : &laquo;&nbsp;ICI ON N'OUBLIE RIEN, ON REMPLACE "
  "SEULEMENT&nbsp;&raquo;. Darius s'arr&ecirc;te devant, le temps de la relire deux "
  "fois, avant de reprendre sa marche, la gorge un peu plus serr&eacute;e "
  "qu'avant.")

p("Le grillage c&egrave;de sous ses mains sans presque de r&eacute;sistance, comme "
  "s'il avait &eacute;t&eacute; d&eacute;coup&eacute; puis repos&eacute; l&agrave;, en attendant "
  "pr&eacute;cis&eacute;ment que quelqu'un comme lui vienne le pousser. &Agrave; "
  "l'int&eacute;rieur, l'entrep&ocirc;t est plong&eacute; dans une p&eacute;nombre grise, "
  "traversant des rang&eacute;es enti&egrave;res d'&eacute;tag&egrave;res m&eacute;talliques charg&eacute;es "
  "de cartons, d'ordinateurs &eacute;teints depuis des ann&eacute;es, de bobines de "
  "c&acirc;bles noirs qui courent au sol comme des racines. Sur chaque "
  "carton, une &eacute;tiquette : un nom de famille, une date, un num&eacute;ro de "
  "page. Des centaines. Des milliers, peut-&ecirc;tre, s'&eacute;tendant plus loin "
  "que la lumi&egrave;re de son t&eacute;l&eacute;phone ne porte.")

p("Avant d'atteindre son propre nom, il passe devant des dizaines "
  "d'autres cartons qu'il ne peut s'emp&ecirc;cher de lire au passage, "
  "malgr&eacute; lui &mdash; des noms de famille de Luynes qu'il croise tous "
  "les jours sans jamais savoir ce qu'ils cachent, la boulang&egrave;re, "
  "un prof de sport &agrave; la retraite, une famille enti&egrave;re dont "
  "chaque membre a son propre carton, empil&eacute;s les uns sur les "
  "autres comme des g&eacute;n&eacute;rations qu'on n'a jamais fini d'archiver. "
  "Il comprend, en marchant dans cette all&eacute;e, que ce qui lui "
  "arrive n'a rien d'exceptionnel &mdash; que ce syst&egrave;me, quel qu'il "
  "soit, fonctionne depuis bien plus longtemps et sur bien plus "
  "de monde qu'il ne l'avait imagin&eacute; dans ses pires suppositions.")

p("Il trouve le sien au bout de la troisi&egrave;me all&eacute;e, presque par "
  "hasard, ou pas par hasard du tout &mdash; il n'arrivera jamais &agrave; "
  "trancher. Un carton, plus &eacute;paissi que les autres, avec une &eacute;tiquette "
  "tap&eacute;e &agrave; la machine &agrave; &eacute;crire, jaunie : DARIUS L. &mdash; DOSSIER "
  "COMPLET &mdash; 41 PAGES ARCHIV&Eacute;ES, 6 EN ATTENTE.")

p("Six en attente. Il n'a r&eacute;cup&eacute;r&eacute; qu'une seule page, ou plut&ocirc;t, il "
  "n'a m&ecirc;me pas r&eacute;cup&eacute;r&eacute; celle-l&agrave;, il l'a juste vue flotter derri&egrave;re "
  "une vitre. &Ccedil;a veut dire qu'il existe cinq autres v&eacute;rit&eacute;s qu'on lui a "
  "d&eacute;j&agrave; retir&eacute;es, sans qu'il en garde le moindre souvenir d'avoir "
  "&eacute;t&eacute; retir&eacute;es, empil&eacute;es ici comme des dossiers m&eacute;dicaux qu'on "
  "n'ose pas ouvrir devant le patient.")

p("Ses mains tremblent en soulevant le rabat du carton. &Agrave; l'int&eacute;rieur, "
  "des feuillets, une &eacute;criture ronde, appliqu&eacute;e, celle-l&agrave; m&ecirc;me qu'il "
  "avait vue sous l'&eacute;tiquette du collier, et des photos qu'il ne "
  "reconna&icirc;t qu'&agrave; moiti&eacute; : lui, plus jeune de deux ou trois ans "
  "qu'il ne l'est aujourd'hui, debout devant cette m&ecirc;me machine en "
  "verre d&eacute;poli, sur une place qui n'est pas celle de Luynes, avec "
  "une date au dos, au feutre rouge, ant&eacute;rieure de dix-huit mois &agrave; "
  "sa premi&egrave;re visite qu'il croyait &ecirc;tre la premi&egrave;re.")

p("C'est &agrave; ce moment pr&eacute;cis que les voix, jusque-l&agrave; murmur&eacute;es, "
  "montent d'un coup, plusieurs &agrave; la fois, superpos&eacute;es, comme si "
  "tous les dossiers de l'entrep&ocirc;t s'&eacute;taient mis &agrave; parler ensemble "
  "au m&ecirc;me instant. Certaines disent son nom. D'autres r&eacute;citent des "
  "dates, des fragments de phrases qu'il a d&eacute;j&agrave; entendues sans "
  "savoir o&ugrave;, &laquo;&nbsp;le cousin Serge&nbsp;&raquo;, &laquo;&nbsp;une formation &agrave; Lyon&nbsp;&raquo;, "
  "&laquo;&nbsp;un travail en Belgique&nbsp;&raquo;, des dizaines de mensonges "
  "diff&eacute;rents racont&eacute;s par des dizaines de voix diff&eacute;rentes, comme "
  "si tout Luynes, tout le pays peut-&ecirc;tre, avait un jour racont&eacute; la "
  "m&ecirc;me sorte d'histoire &agrave; quelqu'un qu'il aimait trop pour lui "
  "dire la v&eacute;rit&eacute;.")

p("Darius se bouche les oreilles, ce qui ne sert &agrave; rien puisque les "
  "voix ne passent pas par ses oreilles, et tombe &agrave; genoux entre "
  "deux &eacute;tag&egrave;res, secou&eacute; d'un vertige qui n'est pas tout &agrave; fait de "
  "la panique, pas tout &agrave; fait autre chose non plus. Pendant une "
  "seconde, peut-&ecirc;tre deux, il n'est plus s&ucirc;r d'&ecirc;tre encore Darius "
  "tout seul l&agrave;-dedans. Il a l'impression, br&egrave;ve et terrifiante, de "
  "pouvoir sentir, comme du bout des doigts, chacune des histoires "
  "que racontent les cartons autour de lui &mdash; laquelle est vraie, "
  "laquelle a &eacute;t&eacute; fabriqu&eacute;e, laquelle cache encore une douleur que "
  "personne n'est jamais venu r&eacute;clamer.")

p("&Ccedil;a passe. Les voix retombent, une &agrave; une, jusqu'&agrave; ce qu'il ne "
  "reste plus que le bourdonnement d'un tube n&eacute;on cassez au plafond. "
  "Mais quelque chose, dans cette seconde de vertige, est rest&eacute; "
  "allum&eacute; en lui, comme une petite veilleuse qu'on aurait oubli&eacute; "
  "d'&eacute;teindre. Le lendemain, en cours, il posera par accident la main "
  "sur le cahier d'un camarade et saura, sans l'avoir voulu, sans "
  "pouvoir l'expliquer, que ce camarade a menti &agrave; ses parents sur "
  "une note, le mois dernier, et que ce mensonge lui p&egrave;se plus qu'il "
  "ne le montre. Il ne parlera &agrave; personne, pas m&ecirc;me &agrave; Clara, de ce "
  "qu'il vient de d&eacute;couvrir sur lui-m&ecirc;me : que la machine, en "
  "&eacute;change de tout ce qu'elle lui a pris sans le lui demander, a "
  "commenc&eacute; &agrave; lui laisser, presque par erreur, un peu de ce "
  "qu'elle sait faire de mieux.")

p("Il retrouve l'objet le lendemain matin, dans la poche int&eacute;rieure "
  "de sa veste, sans aucun souvenir de l'y avoir mis. Un petit "
  "instrument m&eacute;tallique, de la taille d'un stylo, lourd pour sa "
  "taille, avec une pointe fine et plate &agrave; une extr&eacute;mit&eacute; &mdash; un "
  "pon&ccedil;on d'archiviste, de ceux qu'on utilisait avant les ordinateurs "
  "pour perforer les fiches et marquer un num&eacute;ro de page dans le "
  "cuir des reliures. Sur le manche, grav&eacute;es, deux initiales us&eacute;es "
  "par des ann&eacute;es de doigts : un K, et un point.")

p("Il ne se souvient pas de l'avoir pris dans le carton, la veille, "
  "dans l'entrep&ocirc;t. Mais il ne se souvient pas non plus de beaucoup "
  "de choses ces derniers temps, et cette id&eacute;e-l&agrave;, justement, "
  "commence tout juste &agrave; l'inqui&eacute;ter s&eacute;rieusement.")

p("Il le cache au fond de son sac, envelopp&eacute; dans un vieux "
  "tee-shirt, et passe la matin&eacute;e &agrave; sentir sa pr&eacute;sence &agrave; travers "
  "le tissu du sac comme on sent un caillou dans une chaussure "
  "&mdash; une g&ecirc;ne discr&egrave;te, permanente, qui l'emp&ecirc;che d'&eacute;couter "
  "vraiment le cours d'histoire-g&eacute;o sur les grandes migrations "
  "europ&eacute;ennes, comme si le monde entier, ce jour-l&agrave;, s'&eacute;tait "
  "mis d'accord pour lui parler, sans le faire expr&egrave;s, de gens qui "
  "partent et de ce qu'ils laissent derri&egrave;re eux.")

p("Au coll&egrave;ge, en cours d'EPS, la prof leur fait grimper la corde "
  "lisse, un exercice que Darius rate syst&eacute;matiquement depuis la "
  "sixi&egrave;me, faute de force dans les bras. Ce jour-l&agrave;, sans y penser, "
  "sans m&ecirc;me sentir l'effort, il monte jusqu'en haut en moins de "
  "quatre secondes, les pieds &agrave; peine pos&eacute;s sur la corde, comme si "
  "son corps avait, quelque part, appris ce geste il y a longtemps et "
  "l'avait juste attendu pour s'en resservir. Toute la classe applaudit. "
  "Darius, en haut de la corde, regarde ses propres mains sans les "
  "reconna&icirc;tre tout &agrave; fait.")

p("Le pon&ccedil;on, dans sa poche, est chaud contre sa hanche pendant "
  "toute la sc&egrave;ne, comme une pi&egrave;ce qu'on aurait laiss&eacute;e trop "
  "longtemps au soleil.")

p("Sur le chemin du retour, il croise, sur le trottoir d'en face, "
  "un homme qui trimballe une &eacute;chelle bien trop lourde pour lui "
  "seul, en train de peiner &agrave; la faire passer une grille &eacute;troite. "
  "Sans y penser, sans m&ecirc;me ralentir sa marche, Darius sent une "
  "envie physique de traverser pour l'aider, une pouss&eacute;e presque "
  "musculaire dans les bras, avant de se raisonner et de forcer "
  "ses pieds &agrave; continuer tout droit. Il commence &agrave; comprendre "
  "que le pon&ccedil;on ne se contente pas de r&eacute;pondre &agrave; ses vrais "
  "besoins &mdash; il l'attire aussi vers des occasions de s'en "
  "servir, comme un aimant discret plac&eacute; quelque part derri&egrave;re "
  "ses c&ocirc;tes.")

p("Trois jours plus tard, dans la cour du coll&egrave;ge, un bac &agrave; fleurs "
  "en b&eacute;ton se d&eacute;croche du muret du deuxi&egrave;me &eacute;tage o&ugrave; des "
  "ouvriers refont l'&eacute;tanch&eacute;it&eacute; depuis la rentr&eacute;e, et tombe droit "
  "vers un groupe de sixi&egrave;mes qui ne regardent pas en l'air. Darius "
  "le sent avant de le voir &mdash; une d&eacute;mangeaison pr&eacute;cise, tir&eacute;e "
  "comme un fil entre sa nuque et le creux de son ventre, exactement "
  "l&agrave; o&ugrave; il avait senti partir le stylo la semaine d'avant. Il "
  "traverse la cour en trois foul&eacute;es qu'il ne se conna&icirc;t pas, "
  "pousse deux des plus petits hors de la trajectoire, et se "
  "retrouve, sans savoir comment il est mont&eacute; jusque-l&agrave;, agripp&eacute; "
  "au mur de la cantine, deux m&egrave;tres au-dessus du sol, les doigts "
  "et le bord des baskets coll&eacute;s contre le cr&eacute;pi rugueux, "
  "comme si sa peau elle-m&ecirc;me avait d&eacute;cid&eacute;, une seconde, de ne "
  "plus vouloir tomber. Le bac explose au sol, l&agrave; o&ugrave; les sixi&egrave;mes "
  "se tenaient trois secondes plus t&ocirc;t. Personne n'a rien vu de sa "
  "mont&eacute;e, tout le monde regardant le b&eacute;ton fracass&eacute;. Il redescend "
  "en tremblant, les paumes marqu&eacute;es par le cr&eacute;pi, avec la certitude "
  "nouvelle et vertigineuse que son corps, d&eacute;sormais, sait des "
  "choses avant lui &mdash; qu'il existe, quelque part entre sa nuque et "
  "ses mains, une sorte d'alarme install&eacute;e par l'archive elle-m&ecirc;me, "
  "qui sonne chaque fois qu'une page est sur le point de se refermer "
  "trop vite sur quelqu'un.")

p("Plus tard, en cours de fran&ccedil;ais, alors que le prof l'interroge sur "
  "un texte qu'il n'a pas lu et que la panique lui serre la poitrine, "
  "son stylo, pos&eacute; sur la table, roule tout seul de dix centim&egrave;tres "
  "vers la gauche, sans qu'il y touche, sans qu'aucun courant d'air ne "
  "l'explique. Personne d'autre ne le remarque. Darius, lui, sent, "
  "dans le creux de son ventre, exactement l'endroit d'o&ugrave; ce petit "
  "mouvement est parti, comme un muscle qu'il vient de d&eacute;couvrir "
  "sans savoir encore le nom.")

p("Il essaie, ce soir-l&agrave;, seul dans sa chambre &mdash; sa chambre "
  "parfaite, dans sa maison parfaite &mdash; de recommencer, sur une "
  "gomme, volontairement cette fois. Rien ne se passe pendant de "
  "longues minutes, jusqu'&agrave; ce qu'il pense, sans le vouloir, &agrave; Franck "
  "en train de dire &laquo;&nbsp;le cousin Serge&nbsp;&raquo; sans lever les yeux de son "
  "assiette, et alors seulement la gomme se soul&egrave;ve, tremble, "
  "retombe. Son nez se met &agrave; saigner, une seule goutte, presque "
  "rien, mais Darius comprend, avec un frisson qui n'est pas de la "
  "peur mais quelque chose de plus proche du vertige de l'entrep&ocirc;t, "
  "que ce pouvoir ne vient pas de nulle part, qu'il co&ucirc;te quelque "
  "chose &agrave; quelqu'un, quelque part, m&ecirc;me s'il ne sait pas encore "
  "qui.")

p("Il tient le pon&ccedil;on serr&eacute; dans sa main et pose l'autre &agrave; plat "
  "contre le mur de sa chambre, comme il avait pos&eacute; sa main contre "
  "la vitrine, cinq jours plus t&ocirc;t, dans une version du monde qui "
  "avait encore de la pluie dedans. Sous ses doigts, le mur devient, "
  "une seconde, transparent &mdash; pas au sens o&ugrave; il verrait &agrave; travers, "
  "mais au sens o&ugrave; il sent, distinctement, que derri&egrave;re le papier "
  "peint, derri&egrave;re les briques, il n'y a rien du tout, juste une "
  "absence patiente, en attente d'&ecirc;tre remplie par la prochaine "
  "pi&egrave;ce qu'on lui demandera d'imaginer.")

name("DARIUS (&agrave; voix basse, seul)")
p("&laquo;&nbsp;Y'a rien derri&egrave;re. Y'a jamais rien eu derri&egrave;re.&nbsp;&raquo;")

p("C'est cette phrase, dite &agrave; voix haute, dans le silence de sa "
  "chambre trop parfaite, qui fait ce que rien d'autre n'avait r&eacute;ussi "
  "&agrave; faire depuis six jours : elle casse quelque chose. Le plafond "
  "se met &agrave; onduler, comme une image mal charg&eacute;e. La veilleuse en "
  "forme d'&eacute;toile clignote, s'&eacute;teint, se rallume avec une lumi&egrave;re "
  "diff&eacute;rente, plus froide, bleu p&acirc;le, exactement la couleur qu'avaient "
  "ses propres yeux dans le reflet de la vitrine. Il entend, tr&egrave;s "
  "loin, une truffe qui gratte &agrave; une porte qui n'existe pas, puis "
  "plus rien.")

p("Darius se r&eacute;veille en sursaut, essouffl&eacute;, tremp&eacute; de sueur, "
  "recroquevill&eacute; contre le pied de la vitrine du bar-tabac, sur la "
  "place du march&eacute;, sous une pluie fine et glaciale qui n'avait "
  "manqu&eacute; &agrave; personne d'autre que lui pendant six jours qui, ici, "
  "n'ont peut-&ecirc;tre dur&eacute; que quelques minutes. Le pon&ccedil;on est toujours "
  "serr&eacute; dans sa main, r&eacute;el, froid, avec ses deux initiales grav&eacute;es. "
  "Il n'a pas r&ecirc;v&eacute;. La preuve tient dans sa paume.")

p("Le t&eacute;l&eacute;phone de Darius, quand il le rallume, affiche cent "
  "soixante-douze notifications et une date qui ne devrait pas &ecirc;tre "
  "la bonne. Trois jours ont pass&eacute;, dans le vrai Luynes, pendant "
  "que lui vivait, sans compter le temps, une semaine enti&egrave;re "
  "d'une vie qui n'a jamais exist&eacute;. Sa m&egrave;re a appel&eacute; la "
  "gendarmerie le premier soir. Clara a envoy&eacute; quarante messages, "
  "de plus en plus courts, de plus en plus paniqu&eacute;s, jusqu'&agrave; un "
  "dernier, la veille au soir, qui ne dit plus que &laquo;&nbsp;stp&nbsp;&raquo;.")

p("Sur le chemin du retour, Darius traverse des rues qu'il conna&icirc;t "
  "par c&oelig;ur et qui lui semblent pourtant &eacute;trang&egrave;res, comme si "
  "trois jours d'absence r&eacute;elle avaient suffi &agrave; d&eacute;placer, l&eacute;g&egrave;rement, "
  "chaque fa&ccedil;ade, chaque lampadaire, d'un centim&egrave;tre invisible &agrave; "
  "l'&oelig;il mais sensible au corps. Une affiche pour un concert qu'il "
  "n'a jamais vu annonce une date pass&eacute;e depuis deux jours. Le "
  "boulanger a chang&eacute; sa vitrine. Le monde, pendant qu'il &eacute;tait "
  "ailleurs, a continu&eacute; sans lui demander la permission, et cette "
  "id&eacute;e-l&agrave;, plus que tout le reste, lui donne envie de courir.")

p("Il rentre chez lui &agrave; pied, tremblant de froid et d'autre chose, "
  "et trouve sa m&egrave;re assise sur les marches du perron, un "
  "gendarme &agrave; c&ocirc;t&eacute; d'elle en train de noter quelque chose sur un "
  "calepin, le visage de sa m&egrave;re qui se casse en deux sous ses "
  "yeux quand elle le voit apparaitre au bout de la rue, exactement "
  "comme Franck s'&eacute;tait cass&eacute; en deux, il y a des ann&eacute;es, en "
  "pensant &agrave; une phrase qu'il n'a jamais os&eacute; dire.")

S.append(Paragraph("LA M&Egrave;RE DE DARIUS", cn))
p("&laquo;&nbsp;O&ugrave; est-ce que t'&eacute;tais. O&ugrave;. Est-ce que. T'&eacute;tais.&nbsp;&raquo;")

p("Darius ouvre la bouche pour r&eacute;pondre, et se rend compte, en une "
  "fraction de seconde, qu'il est exactement l&agrave; o&ugrave; son p&egrave;re s'&eacute;tait "
  "trouv&eacute; sept ans plus t&ocirc;t, &agrave; devoir choisir entre une v&eacute;rit&eacute; "
  "impossible &agrave; dire et un mensonge qui passerait mieux. Il choisit "
  "une troisi&egrave;me option, celle que Franck n'avait pas eue le "
  "courage d'essayer : il ne dit ni l'un ni l'autre. Il dit &laquo;&nbsp;je sais "
  "pas encore comment t'expliquer, mais je te mentirai pas, donne-moi "
  "juste un peu de temps&nbsp;&raquo;, et sa m&egrave;re, &eacute;puis&eacute;e, le serre si fort "
  "contre elle qu'il sent le pon&ccedil;on lui rentrer dans les c&ocirc;tes &agrave; "
  "travers le tissu de sa poche.")

p("Sa m&egrave;re le fait asseoir dans la cuisine, lui pr&eacute;pare un "
  "chocolat chaud qu'il ne boit pas, et reste debout devant lui, "
  "les bras crois&eacute;s, incapable de choisir entre le serrer &agrave; nouveau "
  "dans ses bras ou lui crier dessus, oscillant entre les deux "
  "toutes les dix secondes, comme une personne qui vient de "
  "comprendre que la peur et la col&egrave;re, parfois, ne sont que la "
  "m&ecirc;me chose port&eacute;e &agrave; deux temp&eacute;ratures diff&eacute;rentes.")

p("Un voisin, attir&eacute; par le bruit, sort sur son perron pour "
  "regarder la sc&egrave;ne, puis rentre chez lui d&egrave;s qu'il comprend "
  "qu'il ne s'agit que d'un adolescent retrouv&eacute;, sans int&eacute;r&ecirc;t "
  "particulier pour lui, et Darius trouve &ccedil;a &eacute;trangement rassurant "
  "&mdash; cette indiff&eacute;rence banale du quartier, si diff&eacute;rente de "
  "tout ce qu'il vient de traverser.")

p("Le gendarme, lui, note &laquo;&nbsp;fugue, motif inconnu&nbsp;&raquo; sur son calepin "
  "et s'en va sans poser d'autres questions, parce que c'est la "
  "r&eacute;ponse la plus simple, et que les adultes, Darius commence &agrave; le "
  "comprendre, choisissent presque toujours la r&eacute;ponse la plus "
  "simple quand la vraie leur ferait trop peur.")

p("Clara et Alex arrivent une heure plus tard, essouffl&eacute;s d'avoir "
  "couru depuis la place. Clara le frappe &agrave; l'&eacute;paule, fort, deux "
  "fois, avant de le serrer dans ses bras exactement comme sa m&egrave;re "
  "l'avait fait.")

name("CLARA")
p("&laquo;&nbsp;T'avais promis. Tu te souviens, au moins, que t'avais "
  "promis&nbsp;?&nbsp;&raquo;")

p("Elle a les yeux rouges, le carnet serr&eacute; contre elle comme "
  "une arme qu'elle ne saurait pas utiliser, et Darius comprend, "
  "en la voyant, qu'il ne s'est pas repr&eacute;sent&eacute; assez pr&eacute;cis&eacute;ment, "
  "avant ce soir, ce que trois jours d'absence pouvaient r&eacute;ellement "
  "faire &agrave; quelqu'un qui a d&eacute;j&agrave; perdu un p&egrave;re une fois, m&ecirc;me "
  "sous une forme diff&eacute;rente, m&ecirc;me sans machine dans l'histoire. "
  "Alex, derri&egrave;re elle, ne dit rien, mais ses mains tremblent "
  "l&eacute;g&egrave;rement, et il garde une distance d'un pas suppl&eacute;mentaire "
  "par rapport &agrave; d'habitude, comme s'il n'&eacute;tait pas encore "
  "tout &agrave; fait s&ucirc;r que celui qui vient de rentrer soit vraiment, "
  "compl&egrave;tement, son meilleur ami.")

name("DARIUS")
p("&laquo;&nbsp;Je me souviens de tout, cette fois. C'est bien &ccedil;a le probl&egrave;me.&nbsp;&raquo;")

p("Dans sa chambre, une fois seul, Darius s'assoit par terre, "
  "le dos contre son lit, et reste ainsi de longues minutes "
  "sans bouger, les yeux ferm&eacute;s, essayant simplement de sentir "
  "que ses propres mains lui appartiennent encore, qu'il peut "
  "les ouvrir et les fermer sur ordre, un exercice tout b&ecirc;te "
  "qui, ce soir-l&agrave;, lui semble plus important que n'importe "
  "quelle autre chose au monde.")

p("Sa m&egrave;re, avant de le laisser monter, insiste pour v&eacute;rifier "
  "qu'il n'a rien de cass&eacute;, qu'il n'a pas faim, qu'il n'a besoin "
  "de rien du tout, r&eacute;p&eacute;tant les m&ecirc;mes questions trois fois de "
  "suite avec la logique un peu d&eacute;traqu&eacute;e d'une personne encore "
  "sous le choc, jusqu'&agrave; ce que Darius, doucement, la prenne "
  "par les &eacute;paules et lui dise qu'il va bien, vraiment, qu'il a "
  "juste besoin de dormir.")

p("Avant de tout raconter, Darius va chercher trois verres d'eau "
  "&agrave; la cuisine, un geste totalement inutile, presque absurde "
  "vu la gravit&eacute; de ce qu'il s'appr&ecirc;te &agrave; dire, mais qui lui "
  "donne quelques secondes suppl&eacute;mentaires pour rassembler son "
  "courage. Quand il revient dans sa chambre, Clara et Alex sont "
  "assis c&ocirc;te &agrave; c&ocirc;te sur le lit, silencieux, attendant, avec la "
  "patience particuli&egrave;re de ceux qui savent d&eacute;j&agrave; que la suite "
  "va &ecirc;tre difficile &agrave; entendre.")

p("Il leur montre le pon&ccedil;on, dans la p&eacute;nombre de sa chambre, "
  "portes ferm&eacute;es, et raconte tout &mdash; la maison parfaite, l'entrep&ocirc;t, "
  "le carton &agrave; son nom, les voix, la corde lisse escalad&eacute;e en "
  "quatre secondes, le stylo qui roule tout seul. Alex, pour une "
  "fois, ne fait aucune blague. Il prend le pon&ccedil;on dans ses mains, "
  "le retourne, s'arr&ecirc;te sur les initiales.")

name("ALEX")
p("&laquo;&nbsp;K point. Comme la voix dans le Non-lieu. Celle qui dit "
  "s'appeler Kayden.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;Il t'a pas donn&eacute; un cadeau, Darius. Il t'a rattach&eacute; une "
  "laisse.&nbsp;&raquo;")

p("Personne ne relance apr&egrave;s &ccedil;a. Le mot &laquo;&nbsp;laisse&nbsp;&raquo;, dans cette "
  "pi&egrave;ce, r&eacute;sonne un peu trop pr&egrave;s d'un collier taille S, cuir "
  "marron, l&eacute;g&egrave;rement rong&eacute; sur la boucle, quelque part derri&egrave;re "
  "une vitre.")

p("Alex finit par reposer le pon&ccedil;on sur le lit, avec la "
  "d&eacute;licatesse exag&eacute;r&eacute;e de quelqu'un manipulant un "
  "objet qu'il soup&ccedil;onne, sans preuve r&eacute;elle, de pouvoir "
  "&ecirc;tre dangereux, et se laisse tomber assis par terre, "
  "dos contre le lit, dans cette posture familiere que "
  "les trois amis adoptent instinctivement chaque fois "
  "qu'une conversation d&eacute;passe le cadre de l'ordinaire.")

name("ALEX")
p("&laquo;&nbsp;Bon, officiellement, qu'est-ce qu'on fait, "
  "l&agrave; ? On appelle personne, on en parle &agrave; personne, "
  "on garde &ccedil;a pour nous trois ? Parce que si je "
  "raconte &ccedil;a &agrave; mes parents, je finis direct chez un "
  "psy, et probablement pas dans le bon sens du "
  "terme.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;On garde &ccedil;a pour nous, pour l'instant. Mais "
  "on note tout, s&eacute;rieusement, chaque d&eacute;tail. Si &ccedil;a "
  "continue, on aura besoin de comprendre le sch&eacute;ma, "
  "et pour &ccedil;a faut des donn&eacute;es, pas juste des "
  "impressions vagues.&nbsp;&raquo;")

p("Darius les &eacute;coute n&eacute;gocier entre eux les modalit&eacute;s "
  "pratiques de ce secret qu'ils viennent, sans "
  "vraiment le d&eacute;cider consciemment, de choisir de "
  "porter ensemble, et ressent, malgr&eacute; la peur "
  "persistante, une gratitude immense envers ces deux "
  "amis capables d'accueillir l'impossible sans jamais "
  "chercher &agrave; fuir ni &agrave; minimiser.")

p("Ils se s&eacute;parent, ce soir-l&agrave;, avec la promesse "
  "solennelle de se retrouver d&egrave;s le lendemain pour "
  "faire le point, et Darius, une fois seul dans sa "
  "chambre, range le pon&ccedil;on sous son oreiller plut&ocirc;t "
  "que dans le tiroir habituel, incapable de se r&eacute;soudre "
  "&agrave; le mettre totalement hors de vue, comme s'il "
  "craignait, en le rangeant trop loin, de perdre le "
  "seul lien tangible qu'il poss&egrave;de d&eacute;sormais avec "
  "cette voix myst&eacute;rieuse du Non-lieu.")

p("Il n'arrive pas &agrave; dormir tout de suite, l'esprit "
  "travers&eacute; par des images fragment&eacute;es de la vitrine, "
  "du collier suspendu dans le vide, de la voix qui "
  "avait prononc&eacute; son propre pr&eacute;nom avec une "
  "familiarit&eacute; d&eacute;rangeante, et finit par rallumer sa "
  "lampe de chevet pour relire, une derni&egrave;re fois cette "
  "nuit-l&agrave;, les quelques lignes qu'il a lui-m&ecirc;me "
  "griffonn&eacute;es dans un vieux cahier, esp&eacute;rant qu'en les "
  "couchant par &eacute;crit elles perdraient un peu de leur "
  "pouvoir sur son sommeil.")

p("Sa m&egrave;re, passant devant sa porte entrouverte vers "
  "onze heures, remarque la lumi&egrave;re encore allum&eacute;e et "
  "toque doucement, sans grande inqui&eacute;tude particuli&egrave;re, "
  "habitu&eacute;e depuis quelques ann&eacute;es &agrave; ces insomnies "
  "d'adolescent qu'elle attribue, comme la plupart des "
  "parents, aux hormones et au stress scolaire ordinaire.")

name("M&Egrave;RE DE DARIUS")
p("&laquo;&nbsp;T'es encore r&eacute;veill&eacute; ? &Ccedil;a va, mon grand ? T'as "
  "pas l'air dans ton assiette, ces derniers jours.&nbsp;&raquo;")

p("Darius h&eacute;site une fraction de seconde, tent&eacute; de "
  "tout lui raconter, avant de se raviser presque "
  "aussit&ocirc;t, appliquant sans y penser cette m&ecirc;me "
  "logique de protection par le silence qu'il a "
  "toujours reproch&eacute;e &agrave; son p&egrave;re, sans encore mesurer "
  "&agrave; quel point cette habitude familiale risque, elle "
  "aussi, de finir par lui co&ucirc;ter cher.")

name("DARIUS")
p("&laquo;&nbsp;&Ccedil;a va, maman, promis. J'ai juste du mal &agrave; "
  "dormir, c'est tout. Rien de grave.&nbsp;&raquo;")

p("Elle referme la porte doucement, rassur&eacute;e par ce "
  "mensonge b&eacute;nin qu'elle ne songe pas une seconde &agrave; "
  "remettre en question, et Darius, seul &agrave; nouveau "
  "dans l'obscurit&eacute; de sa chambre, &eacute;teint enfin sa "
  "lampe, gardant le pon&ccedil;on serr&eacute; dans son poing sous "
  "la couverture, comme un talisman contre des "
  "menaces qu'il ne comprend pas encore enti&egrave;rement.")

p("Le sommeil finit par le gagner, lourd et sans "
  "r&ecirc;ve pour une fois, et il se r&eacute;veille le lendemain "
  "matin avec la sensation &eacute;trange d'avoir travers&eacute; une "
  "nuit plus longue que d'habitude, comme si son "
  "propre corps avait eu besoin de r&eacute;cup&eacute;rer d'un "
  "&eacute;puisement qui d&eacute;passait le simple manque de "
  "sommeil.")

p("En descendant prendre son petit-d&eacute;jeuner, il "
  "trouve sa m&egrave;re d&eacute;j&agrave; install&eacute;e &agrave; la table de la "
  "cuisine, un caf&eacute; fumant devant elle, occup&eacute;e &agrave; "
  "lire les nouvelles locales sur son t&eacute;l&eacute;phone avec "
  "cette concentration matinale qu'elle applique "
  "chaque jour avant de partir travailler, et il "
  "s'installe silencieusement en face d'elle, savourant "
  "cette normalit&eacute; retrouv&eacute;e apr&egrave;s la nuit agit&eacute;e qu'il "
  "vient de traverser.")

name("M&Egrave;RE DE DARIUS")
p("&laquo;&nbsp;Tu veux que je te d&eacute;pose au coll&egrave;ge "
  "aujourd'hui ? Il fait un temps affreux dehors, tu "
  "vas &ecirc;tre tremp&eacute; si tu y vas &agrave; v&eacute;lo comme "
  "d'habitude.&nbsp;&raquo;")

p("Darius accepte cette proposition avec "
  "gratitude, appr&eacute;ciant ce petit geste d'attention "
  "quotidienne qui, dans le contexte de tout ce qu'il "
  "traverse depuis quelques jours, prend une "
  "signification particuli&egrave;re, presque un ancrage "
  "n&eacute;cessaire dans l'ordinaire face &agrave; l'extraordinaire "
  "qui menace, chaque jour un peu plus, d'envahir sa "
  "vie enti&egrave;re.")

p("Le trajet en voiture jusqu'au coll&egrave;ge se fait "
  "presque enti&egrave;rement en silence, sa m&egrave;re occup&eacute;e &agrave; "
  "&eacute;viter les flaques les plus profondes sur la route "
  "d&eacute;trempe&eacute;e, et Darius, le front pos&eacute; contre la "
  "vitre embu&eacute;e, observe les rues famili&egrave;res de Luynes "
  "d&eacute;filer avec cette attention nouvelle qu'il porte "
  "d&eacute;sormais &agrave; chaque d&eacute;tail du d&eacute;cor, cherchant, sans "
  "trop se l'avouer, le moindre signe suppl&eacute;mentaire "
  "qui pourrait confirmer ou infirmer ce qu'il a v&eacute;cu "
  "quelques jours plus t&ocirc;t devant la vitrine.")

p("Il retrouve Clara devant les grilles du "
  "coll&egrave;ge, emmitoufl&eacute;e dans une &eacute;charpe trop grande "
  "pour elle, et remarque imm&eacute;diatement, &agrave; son regard "
  "insistant, qu'elle aussi a pass&eacute; une nuit agit&eacute;e, "
  "probablement occup&eacute;e &agrave; retourner dans tous les "
  "sens les implications de ce qu'il lui a confi&eacute; la "
  "veille.")

name("CLARA")
p("&laquo;&nbsp;J'ai pas ferm&eacute; l'&oelig;il de la nuit, en fait. "
  "J'arr&ecirc;tais pas de penser &agrave; ce collier, &agrave; cette "
  "vitrine. C'est dingue, mais j'ai presque envie d'aller "
  "voir par moi-m&ecirc;me, tu vois, avant les cours, "
  "juste pour v&eacute;rifier.&nbsp;&raquo;")

p("Darius h&eacute;site, tiraillé entre l'envie de "
  "partager cette d&eacute;couverte avec quelqu'un capable de "
  "confirmer qu'il n'a pas r&ecirc;v&eacute;, et la peur, tout aussi "
  "vive, de voir Clara elle-m&ecirc;me expos&eacute;e &agrave; quelque "
  "chose qu'il ne comprend pas encore assez pour "
  "&eacute;valuer le danger r&eacute;el.")

name("DARIUS")
p("&laquo;&nbsp;On y va ensemble, alors, mais apr&egrave;s les cours. "
  "Je veux pas que tu y ailles seule, au cas o&ugrave;. On "
  "sait m&ecirc;me pas ce que c'est vraiment, cette "
  "histoire.&nbsp;&raquo;")

p("Ils passent la journ&eacute;e de cours dans un &eacute;tat "
  "d'attention divis&eacute;e, incapables de se concentrer "
  "pleinement sur les math&eacute;matiques ou l'histoire "
  "g&eacute;ographie, chacun &eacute;changeant, discr&egrave;tement entre "
  "deux le&ccedil;ons, des regards charg&eacute;s de cette "
  "anticipation commune qui rend l'attente de la fin "
  "des cours presque insupportable.")

p("Alex, ne remarquant pas imm&eacute;diatement cette "
  "tension particuli&egrave;re entre ses deux amis, finit par "
  "s'en &eacute;tonner &agrave; la r&eacute;cr&eacute;ation, sa curiosit&eacute; naturelle "
  "le poussant &agrave; questionner directement plut&ocirc;t que "
  "de laisser planer le doute.")

name("ALEX")
p("&laquo;&nbsp;Vous deux, vous avez une t&ecirc;te bizarre "
  "aujourd'hui. Vous complotez un truc sans moi, "
  "l&agrave; ? &Ccedil;a se voit sur vos visages, franchement, vous "
  "&ecirc;tes pas discrets du tout.&nbsp;&raquo;")

p("Clara et Darius &eacute;changent un regard rapide, "
  "d&eacute;cidant sans un mot de mettre Alex dans la "
  "confidence d&egrave;s la sortie des cours, incapables de "
  "continuer &agrave; lui cacher quoi que ce soit sans "
  "trahir cette amiti&eacute; solide qui les unit depuis "
  "l'enfance, et qui deviendra, dans les mois suivants, "
  "leur ressource la plus pr&eacute;cieuse face &agrave; tout ce qui "
  "les attend.")

p("&Agrave; la sortie des cours, install&eacute;s tous les trois sur "
  "le muret bordant le parking &agrave; v&eacute;los, Darius raconte "
  "&agrave; Alex, dans le d&eacute;tail, tout ce qu'il a v&eacute;cu devant "
  "la vitrine, cette voix, ce collier suspendu dans le "
  "vide, ce nom murmur&eacute; qu'aucun d'eux trois ne "
  "conna&icirc;t encore vraiment.")

p("Alex &eacute;coute sans interrompre une seule fois, ce "
  "qui, pour quelqu'un d'aussi bavard habituellement, "
  "constitue en soi un signe &eacute;loquent du s&eacute;rieux avec "
  "lequel il accueille ce r&eacute;cit extraordinaire, et "
  "quand Darius termine enfin, un long silence "
  "s'installe entre les trois amis, seulement troubl&eacute; "
  "par le bruit lointain de la circulation.")

name("ALEX")
p("&laquo;&nbsp;Ok. Donc soit vous vous foutez compl&egrave;tement "
  "de ma gueule, tous les deux, soit un truc "
  "vraiment dingue est en train de se passer &agrave; "
  "Luynes. Vu vos t&ecirc;tes, j'ai l'impression que c'est "
  "l'option deux. G&eacute;nial. Absolument g&eacute;nial.&nbsp;&raquo;")

p("Ce ton faussement d&eacute;sinvolte, caract&eacute;ristique "
  "d'Alex face &agrave; l'adversit&eacute;, dissimule mal une "
  "inqui&eacute;tude sinc&egrave;re que Darius et Clara "
  "reconnaissent imm&eacute;diatement, habitu&eacute;s depuis "
  "l'enfance &agrave; d&eacute;chiffrer les v&eacute;ritables &eacute;motions de "
  "leur ami derri&egrave;re ses fanfaronnades habituelles.")

p("Ils d&eacute;cident, d'un commun accord, de se rendre "
  "ensemble devant la vitrine ce m&ecirc;me apr&egrave;s-midi, "
  "profitant de la lumi&egrave;re encore pr&eacute;sente pour "
  "examiner les lieux avec plus d'attention que Darius "
  "n'avait pu le faire seul, terrifi&eacute;, quelques jours "
  "plus t&ocirc;t.")

p("La vitrine, en plein apr&egrave;s-midi, ne pr&eacute;sente rien "
  "d'anormal &agrave; premi&egrave;re vue &mdash; un vieux magasin "
  "d&eacute;saffect&eacute; depuis des ann&eacute;es, ses &eacute;tag&egrave;res vides "
  "recouvertes d'une fine couche de poussi&egrave;re, aucun "
  "collier suspendu dans le vide, aucune trace "
  "visible de ce que Darius avait d&eacute;crit avec tant de "
  "pr&eacute;cision quelques heures plus t&ocirc;t.")

name("ALEX")
p("&laquo;&nbsp;Bon, je vois rien de bizarre, moi. C'est juste "
  "un vieux magasin vide, comme y'en a plein &agrave; "
  "Luynes. T'es s&ucirc;r que t'as pas juste r&ecirc;v&eacute; tout "
  "&ccedil;a, Darius ?&nbsp;&raquo;")

p("Darius, d&eacute;stabilis&eacute; par cette absence de preuve "
  "visible, sort son t&eacute;l&eacute;phone pour leur montrer la "
  "photographie prise la veille, cette image floue "
  "mais indéniable d'un collier suspendu sans "
  "attache apparente dans l'obscurit&eacute; du magasin "
  "vide, une preuve tangible qui dissipe "
  "imm&eacute;diatement le scepticisme naissant de son ami.")

name("CLARA")
p("&laquo;&nbsp;Regarde &ccedil;a, Alex. C'est clairement pas normal, "
  "&ccedil;a. Un collier flotte pas tout seul dans le vide, "
  "m&ecirc;me dans un vieux magasin abandonn&eacute;. Darius a "
  "raison de flipper, je crois.&nbsp;&raquo;")

p("Alex, confront&eacute; &agrave; cette preuve photographique "
  "indiscutable, r&eacute;vise imm&eacute;diatement son "
  "scepticisme initial, sa curiosit&eacute; naturelle "
  "prenant rapidement le pas sur son incr&eacute;dulit&eacute; "
  "premi&egrave;re, et propose, avec cet enthousiasme "
  "t&eacute;m&eacute;raire qui le caract&eacute;rise, de revenir le soir "
  "m&ecirc;me pour observer directement le ph&eacute;nom&egrave;ne, "
  "esp&eacute;rant assister eux-m&ecirc;mes &agrave; une manifestation "
  "similaire &agrave; celle d&eacute;crite par Darius.")

p("Clara, plus prudente, sugg&egrave;re de pr&eacute;parer un "
  "minimum de mat&eacute;riel avant de revenir observer la "
  "vitrine &agrave; la nuit tomb&eacute;e &mdash; une lampe torche "
  "suppl&eacute;mentaire, un carnet pour noter chaque "
  "d&eacute;tail, et surtout, la promesse mutuelle de ne "
  "rester que quelques minutes avant de rentrer si "
  "rien d'anormal ne se produit.")

name("CLARA")
p("&laquo;&nbsp;On n'est pas oblig&eacute;s de faire &ccedil;a comme des "
  "cowboys. On observe, on note, et si &ccedil;a devient "
  "trop bizarre ou effrayant, on part imm&eacute;diatement. "
  "D'accord ?&nbsp;&raquo;")

p("Les deux gar&ccedil;ons acquiescent, un peu moins "
  "t&eacute;m&eacute;raires face &agrave; cette proposition raisonnable, "
  "et ils se s&eacute;parent en fin d'apr&egrave;s-midi, chacun "
  "rentrant chez soi pour d&icirc;ner avant de se retrouver, "
  "comme convenu, devant la vitrine d&egrave;s la tomb&eacute;e "
  "de la nuit, anim&eacute;s par ce m&eacute;lange d'excitation et "
  "d'appr&eacute;hension propre aux premi&egrave;res aventures "
  "v&eacute;ritablement dangereuses de leur jeune "
  "existence.")

p("Darius, rentr&eacute; chez sa m&egrave;re, peine &agrave; avaler son "
  "d&icirc;ner, l'estomac nou&eacute; par l'anticipation de ce "
  "rendez-vous nocturne, et invente un pr&eacute;texte "
  "vague sur un devoir de groupe pour justifier sa "
  "sortie tardive, ce premier petit mensonge "
  "n&eacute;cessaire lui laissant un go&ucirc;t amer qu'il "
  "n'aurait pas anticip&eacute;, lui qui d&eacute;teste tant, "
  "d'ordinaire, cette pratique familiale de dissimuler "
  "la v&eacute;rit&eacute; sous des pr&eacute;textes commodes.")

name("M&Egrave;RE DE DARIUS")
p("&laquo;&nbsp;Sois prudent, hein, et pas trop tard. Il "
  "fait pas chaud dehors, prends une veste "
  "suppl&eacute;mentaire.&nbsp;&raquo;")

p("Il sort finalement, la veste suppl&eacute;mentaire "
  "sagement enfil&eacute;e, retrouvant Clara et Alex au "
  "coin de la rue de la place du march&eacute;, chacun "
  "portant sur le visage cette m&ecirc;me tension "
  "m&ecirc;l&eacute;e d'excitation qui accompagne toujours les "
  "premi&egrave;res incursions dans l'inconnu, avant de se "
  "diriger tous les trois, en silence, vers la "
  "vitrine qui va, cette nuit-l&agrave;, bouleverser "
  "d&eacute;finitivement le cours de leurs existences.")

p("La place du march&eacute;, d&eacute;serte &agrave; cette heure "
  "tardive, prend sous l'&eacute;clairage jaun&acirc;tre des "
  "r&eacute;verb&egrave;res une allure diff&eacute;rente de celle qu'ils "
  "lui connaissent en plein jour, chaque ombre "
  "projet&eacute;e par les fa&ccedil;ades environnantes semblant "
  "receler une menace potentielle aux yeux des "
  "trois adolescents, dont les pas r&eacute;sonnent "
  "anormalement fort sur les pav&eacute;s silencieux.")

name("ALEX")
p("&laquo;&nbsp;J'ai l'impression que chaque bruit est "
  "amplifi&eacute; dix fois, ce soir. Faut vraiment qu'on se "
  "calme un peu, sinon on va se faire peur tout "
  "seuls avant m&ecirc;me d'arriver &agrave; la vitrine.&nbsp;&raquo;")

p("Cette remarque, malgr&eacute; son ton l&eacute;ger, refl&egrave;te "
  "assez fid&egrave;lement l'&eacute;tat nerveux dans lequel se "
  "trouvent les trois amis, chacun conscient, sans "
  "oser vraiment le formuler &agrave; voix haute, qu'ils "
  "s'appr&ecirc;tent &agrave; franchir un seuil qui pourrait "
  "bien, d'une mani&egrave;re ou d'une autre, changer "
  "d&eacute;finitivement leur perception du monde qui les "
  "entoure.")

p("Ils arrivent enfin devant la vitrine, s'arr&ecirc;tant "
  "&agrave; quelques pas de distance respectueuse, "
  "observant en silence cette devanture d&eacute;sormais "
  "familiere &agrave; Darius mais toujours aussi &eacute;trange "
  "aux yeux de ses deux amis, qui scrutent l'obscurit&eacute; "
  "du magasin vide &agrave; la recherche du moindre "
  "mouvement suspect.")

name("CLARA")
p("&laquo;&nbsp;On attend, alors ? Combien de temps tu "
  "penses qu'il faut attendre avant que &ccedil;a se "
  "reproduise, si &ccedil;a se reproduit ce soir ?&nbsp;&raquo;")

p("Darius hausse les &eacute;paules, incapable de r&eacute;pondre "
  "avec certitude &agrave; cette question l&eacute;gitime, n'ayant "
  "lui-m&ecirc;me aucune id&eacute;e des r&egrave;gles r&eacute;gissant ces "
  "manifestations myst&eacute;rieuses, et tous trois "
  "s'installent finalement sur le trottoir d'en "
  "face, adoss&eacute;s contre un mur encore ti&egrave;de de la "
  "chaleur emmagasin&eacute;e durant la journ&eacute;e, pr&ecirc;ts &agrave; "
  "attendre aussi longtemps que n&eacute;cessaire.")

p("Les minutes s'&eacute;coulent lentement, chacun "
  "d&eacute;veloppant sa propre technique pour g&eacute;rer "
  "l'attente anxieuse &mdash; Alex fredonnant tout bas une "
  "chanson populaire pour se calmer les nerfs, "
  "Clara comptant machinalement les fissures du "
  "trottoir sous ses pieds, Darius fixant "
  "obstin&eacute;ment la vitrine sans oser cligner des yeux "
  "trop longtemps, de peur de manquer le moindre "
  "signe.")

name("ALEX")
p("&laquo;&nbsp;&Ccedil;a fait combien de temps, l&agrave; ? Vingt "
  "minutes ? Trente ? J'ai l'impression que &ccedil;a fait "
  "des heures d&eacute;j&agrave;.&nbsp;&raquo;")

p("Clara consulte son t&eacute;l&eacute;phone, confirmant que "
  "seules vingt-cinq minutes se sont &eacute;coul&eacute;es "
  "depuis leur arriv&eacute;e, une dur&eacute;e qui semble "
  "pourtant, &agrave; chacun d'entre eux, bien plus longue "
  "tant la tension nerveuse dilate subjectivement "
  "leur perception du temps qui passe.")

p("C'est alors que, sans le moindre signe "
  "avant-coureur, la vitrine commence &agrave; scintiller "
  "faiblement, une lueur bleu&acirc;t&eacute;e presque "
  "imperceptible d'abord, puis grandissant "
  "rapidement en intensit&eacute;, r&eacute;v&eacute;lant, suspendu dans "
  "l'obscurit&eacute; du magasin vide, ce m&ecirc;me collier "
  "que Darius avait photographi&eacute; la veille, "
  "flottant sans attache visible dans l'air "
  "immobile.")

name("CLARA")
p("&laquo;&nbsp;Oh mon Dieu. Darius, regarde, c'est exactement "
  "comme tu nous l'avais d&eacute;crit. C'est vraiment "
  "l&agrave;.&nbsp;&raquo;")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 1 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 2 -- CELUI QUI PORTE SON VISAGE
# ======================================================================
chap(2, "CELUI QUI PORTE SON VISAGE")

p("Les jours qui suivent la premi&egrave;re apparition de "
  "Kayden laissent Darius dans un &eacute;tat de vigilance "
  "&eacute;puisante, guettant, dans chaque reflet de vitrine, "
  "chaque &eacute;cran &eacute;teint, chaque flaque d'eau sur le "
  "trottoir, le retour possible de ce visage qui n'&eacute;tait "
  "pourtant, jusque-l&agrave;, connu de personne &agrave; Luynes.")

p("Il en parle enfin &agrave; Clara, un mercredi apr&egrave;s-midi, "
  "sur le chemin du retour du coll&egrave;ge, incapable de "
  "porter plus longtemps seul cette sensation "
  "grandissante d'&ecirc;tre observ&eacute; par quelque chose qui "
  "refuse de se montrer clairement, et elle l'&eacute;coute "
  "avec cette attention totale qui la caract&eacute;rise "
  "toujours face &agrave; ce qui sort de l'ordinaire.")

name("CLARA")
p("&laquo;&nbsp;Un gar&ccedil;on que tu connais pas, avec ton "
  "visage &agrave; toi mais plus vieux ? &Ccedil;a fait froid dans le "
  "dos, dit comme &ccedil;a. T'es s&ucirc;r que t'as pas juste "
  "invent&eacute; &ccedil;a, genre &agrave; moiti&eacute; endormi ou stress&eacute; par "
  "les examens ?&nbsp;&raquo;")

name("DARIUS")
p("&laquo;&nbsp;Non, j'&eacute;tais parfaitement r&eacute;veill&eacute;, Clara. Et le "
  "pon&ccedil;on, il a boug&eacute; tout seul dans ma poche juste "
  "avant. &Ccedil;a, j'ai pas invent&eacute;, j'ai senti le poids "
  "changer, genre physiquement.&nbsp;&raquo;")

p("Clara r&eacute;fl&eacute;chit un long moment, marchant en "
  "silence &agrave; ses c&ocirc;t&eacute;s, avant de proposer, avec ce "
  "pragmatisme qui la caract&eacute;rise toujours face &agrave; "
  "l'&eacute;trange, de consigner d&eacute;sormais chaque d&eacute;tail "
  "&eacute;trange dans un cahier d&eacute;di&eacute;, esp&eacute;rant qu'une "
  "approche m&eacute;thodique permettrait, avec le temps, de "
  "d&eacute;gager un motif plus clair de ce qui leur arrive.")

name("CLARA")
p("&laquo;&nbsp;On note tout, &agrave; partir de maintenant. Les "
  "dates, les heures, ce que t'as ressenti, ce que t'as "
  "vu exactement. Si &ccedil;a doit continuer, autant essayer "
  "de comprendre le sch&eacute;ma plut&ocirc;t que de subir sans "
  "rien piger.&nbsp;&raquo;")

p("Cette d&eacute;cision, prise presque par hasard ce "
  "mercredi apr&egrave;s-midi, donnera naissance, sans qu'ils "
  "le sachent encore, au carnet qui deviendra, des mois "
  "plus tard, bien plus qu'un simple journal d'&eacute;v&eacute;nements "
  "&eacute;tranges &mdash; un objet capable, lui-m&ecirc;me, de porter une "
  "part de la m&eacute;moire qu'on cherche &agrave; leur voler.")

p("Il essaie aussi, sans grand succ&egrave;s, de reprendre une routine "
  "normale &mdash; devoirs le soir, entra&icirc;nement de foot le mercredi, "
  "s&eacute;ries regard&eacute;es en famille le week-end &mdash; convaincu que "
  "recr&eacute;er artificiellement l'ordinaire suffirait peut-&ecirc;tre &agrave; "
  "&eacute;loigner la tentation. &Ccedil;a fonctionne, un peu, les premiers "
  "jours, avant que la r&eacute;alit&eacute; ne rattrape toujours, in&eacute;vitablement, "
  "cette illusion de normalit&eacute; qu'il s'&eacute;tait construite.")

p("Cette semaine-l&agrave;, il note lui-m&ecirc;me, sur un vieux carnet que "
  "Clara lui a offert pour l'occasion, un petit trait chaque soir "
  "o&ugrave; il n'a pas touch&eacute; le pon&ccedil;on, une m&eacute;thode qu'elle avait "
  "lue quelque part pour tenir bon face &agrave; une envie t&ecirc;tue. Les "
  "cinq premiers traits s'alignent, fiers, presque satisfaisants "
  "&agrave; regarder, avant que la ligne ne se brise, un vendredi matin, "
  "pour une raison si banale que &ccedil;a en devient presque ridicule.")

p("Le pon&ccedil;on, dans sa poche, ne chauffe pas cette fois. Il reste "
  "froid, presque inerte, comme s'il attendait, lui aussi, sans "
  "impatience, de savoir quelle d&eacute;cision Darius allait finir par "
  "prendre &mdash; une neutralit&eacute; qui, curieusement, l'effraie encore "
  "plus qu'une pression active, comme si l'objet lui-m&ecirc;me savait "
  "que la r&eacute;ponse, quelle qu'elle soit, finirait de toute fa&ccedil;on "
  "par arriver.")

p("Il repense &agrave; la phrase d'Alex, dans sa chambre, quelques "
  "semaines plus t&ocirc;t &mdash; &laquo;&nbsp;c'est plus vraiment un choix, &agrave; ce "
  "moment-l&agrave;&nbsp;&raquo; &mdash; et se demande combien de fois, exactement, "
  "il pourra encore se dire que c'&eacute;tait un accident avant que ce "
  "mot lui-m&ecirc;me ne perde tout son sens.")

p("Le week-end pr&eacute;c&eacute;dent, Darius avait m&ecirc;me propos&eacute; &agrave; Clara de "
  "garder le pon&ccedil;on chez elle, enferm&eacute; dans le tiroir de son "
  "propre bureau, pensant que la distance physique suffirait &agrave; "
  "couper la tentation. Il avait fallu &agrave; peine deux jours pour "
  "qu'il aille le rechercher, sous pr&eacute;texte de v&eacute;rifier qu'il "
  "&eacute;tait bien rang&eacute;, incapable, au fond, de rester loin de lui "
  "plus longtemps.")

p("Il tient une semaine sans y toucher. Puis, un matin, en retard "
  "pour le bus, il court, saute par-dessus un banc sans y r&eacute;fl&eacute;chir, "
  "atterrit sans un bruit, souple comme s'il n'avait jamais fait "
  "autre chose de sa vie, et pendant que le bus l'attend, ravi et un "
  "peu effray&eacute; de lui-m&ecirc;me &agrave; la fois, il ne pense pas une seconde "
  "&agrave; ce que &ccedil;a peut co&ucirc;ter, ni &agrave; qui.")

p("Le pon&ccedil;on, depuis quelques jours, a pris l'habitude de se "
  "r&eacute;chauffer discr&egrave;tement au fond de sa poche chaque fois "
  "qu'une occasion se pr&eacute;sente de s'en servir, une sorte de "
  "tentation physique, presque agr&eacute;able, qui ressemble &agrave; l'envie "
  "de gratter une d&eacute;mangeaison qu'on sait pourtant qu'il ne faut "
  "pas gratter. Darius commence &agrave; comprendre pourquoi certains "
  "adultes, dans les histoires que raconte Clara, ont fini par "
  "revenir devant la machine une deuxi&egrave;me fois, puis une "
  "troisi&egrave;me : ce n'est jamais la premi&egrave;re utilisation qui "
  "pi&egrave;ge quelqu'un. C'est la facilit&eacute; de la deuxi&egrave;me.")

p("Ce jour-l&agrave;, dans le journal local que sa m&egrave;re lit sur son "
  "t&eacute;l&eacute;phone au petit-d&eacute;jeuner, un article de trois lignes : un "
  "ancien pompier de Luynes, cinquante-huit ans, la ville l'honore "
  "chaque ann&eacute;e pour un sauvetage c&eacute;l&egrave;bre effectu&eacute; trente ans "
  "plus t&ocirc;t, s'est retrouv&eacute; incapable, ce matin, de descendre "
  "l'escalier de chez lui sans tomber, pour la premi&egrave;re fois depuis "
  "l'accident qui l'a rendu c&eacute;l&egrave;bre. &laquo;&nbsp;Un simple vertige&nbsp;&raquo;, dit "
  "l'article. Darius ne fait pas le lien. Pas encore.")

p("Le vendredi, en col&egrave;re contre un surveillant qui l'a puni "
  "injustement, il serre le pon&ccedil;on dans sa poche sans s'en rendre "
  "compte, et sent un mur, litt&eacute;ralement, tanguer de deux "
  "centim&egrave;tres, une fissure s'ouvrant dans l'&eacute;paisseur du b&eacute;ton, "
  "que personne d'autre ne remarque parce que le b&acirc;timent, "
  "construit dans les ann&eacute;es soixante, est cens&eacute; &ecirc;tre vieux et "
  "fatigu&eacute; de toute fa&ccedil;on. Il rentre chez lui, cette fois, avec un "
  "saignement de nez qui ne s'arr&ecirc;te qu'au bout de vingt minutes, "
  "et une migraine qui lui donne l'impression que son cr&acirc;ne est "
  "trop petit pour ce qu'il contient.")

p("Clara, elle, prend l'habitude de v&eacute;rifier chaque soir, sur "
  "internet, les faits divers de la r&eacute;gion, cherchant m&eacute;thodiquement "
  "des co&iuml;ncidences entre les moments o&ugrave; Darius a utilis&eacute; le "
  "pon&ccedil;on et des incidents mineurs signal&eacute;s dans les environs. Elle "
  "finit toujours par en trouver un, m&ecirc;me minuscule, et chaque "
  "fois, elle le note dans son carnet sans rien dire &agrave; Darius, "
  "pour ne pas ajouter cette pression suppl&eacute;mentaire &agrave; celle "
  "qu'il porte d&eacute;j&agrave; sur les &eacute;paules.")

p("Alex, de son c&ocirc;t&eacute;, remarque autre chose : Darius rit un peu "
  "moins fort qu'avant, s'excuse plus souvent pour des riens, "
  "recule d'un pas quand quelqu'un s'approche trop vite de lui "
  "dans les couloirs bond&eacute;s du coll&egrave;ge, comme s'il craignait, "
  "au fond, de faire d&eacute;clencher quelque chose sans le vouloir sur "
  "un simple accident, une simple bousculade.")

p("C'est Clara qui fait le lien, un dimanche, en &eacute;pluchant "
  "m&eacute;thodiquement, dans son carnet, les petites annonces et les "
  "faits divers de la semaine &agrave; c&ocirc;t&eacute; des dates o&ugrave; Darius a not&eacute; "
  "avoir utilis&eacute; le pon&ccedil;on, m&ecirc;me sans le vouloir.")

name("CLARA")
p("&laquo;&nbsp;Le jour o&ugrave; t'as grimp&eacute; la corde comme un cascadeur, "
  "l'ancien pompier a eu son vertige. Le jour o&ugrave; ton stylo a "
  "boug&eacute; tout seul, y'a une dame &agrave; la maison de retraite qui a "
  "soudain plus su jouer du piano alors qu'elle joue tous les "
  "apr&egrave;s-midis depuis quarante ans, sans une seule fausse note "
  "d'habitude. C'est pas un hasard, Darius. Chaque fois que tu "
  "prends un peu de leur talent, eux, ils le perdent, m&ecirc;me juste "
  "une minute, m&ecirc;me juste ce jour-l&agrave;. C'est des gens &agrave; qui on a "
  "d&eacute;j&agrave; pris quelque chose, un jour, contre une page qu'ils "
  "voulaient r&eacute;cup&eacute;rer. Et maintenant &ccedil;a te sert de r&eacute;serve.&nbsp;&raquo;")

p("Darius pose le pon&ccedil;on sur la table entre eux, comme un objet "
  "brusquement radioactif. Il pense au pompier qui tombe dans son "
  "propre escalier, &agrave; la vieille dame qui perd, sans comprendre "
  "pourquoi, la seule chose qui lui reste de sa m&eacute;moire de "
  "musicienne. Il pense &agrave; Franck, qui a pens&eacute;, un mardi, qu'un "
  "mensonge co&ucirc;terait moins cher qu'une v&eacute;rit&eacute;, sans jamais "
  "imaginer &agrave; quel point la facture reviendrait, des ann&eacute;es plus "
  "tard, se pr&eacute;senter &agrave; quelqu'un d'autre.")

p("Un soir, sans le vouloir, Darius entend sa m&egrave;re au t&eacute;l&eacute;phone "
  "avec une amie, dans la cuisine, raconter d'une voix inqui&egrave;te "
  "qu'elle ne comprend plus tout &agrave; fait son fils depuis la fugue, "
  "qu'il a des sautes d'humeur, des absences, quelque chose de "
  "&laquo;&nbsp;pas normal pour son &acirc;ge&nbsp;&raquo;. Il reste immobile derri&egrave;re la "
  "porte entrouverte, le pon&ccedil;on lourd dans sa poche, incapable de "
  "d&eacute;cider si la pire chose serait de lui dire la v&eacute;rit&eacute; ou de la "
  "laisser continuer &agrave; s'inqui&eacute;ter pour une raison qu'elle ne "
  "conna&icirc;tra jamais.")

name("DARIUS")
p("&laquo;&nbsp;Alors j'arr&ecirc;te. Je le touche plus.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;Et si &ccedil;a se d&eacute;clenche tout seul, comme le stylo ? T'as pas "
  "vraiment eu &agrave; le vouloir, ces deux fois-l&agrave;. &Ccedil;a s'appelle plus "
  "vraiment un choix, &agrave; ce moment-l&agrave;.&nbsp;&raquo;")

p("Personne n'a de r&eacute;ponse &agrave; &ccedil;a. Dehors, il s'est remis &agrave; "
  "pleuvoir, pour de vrai cette fois, et Darius se surprend &agrave; "
  "trouver &ccedil;a rassurant, comme la preuve, chaque goutte contre la "
  "vitre, que le monde n'a pas encore fini de d&eacute;cider &agrave; sa place.")

p("Le pon&ccedil;on, rang&eacute; au fond d'un tiroir sous des vieux cahiers, "
  "se met &agrave; chauffer un mardi soir, &agrave; travers le bois du meuble, "
  "assez fort pour r&eacute;veiller Darius d'un sommeil sans r&ecirc;ve. Quand "
  "il ouvre le tiroir, la pointe fine du pon&ccedil;on est braqu&eacute;e, "
  "immobile, vers le mur de sa chambre, comme une aiguille de "
  "boussole qui aurait enfin trouv&eacute; son nord.")

p("Il pense d'abord &agrave; r&eacute;veiller ses parents, puis se ravise &mdash; sa "
  "m&egrave;re dort depuis &agrave; peine une heure, &eacute;puis&eacute;e par trois jours "
  "d'angoisse, et il ne se sent pas la force de recommencer une "
  "conversation qu'il sait ne pas savoir terminer sans mentir un "
  "peu, lui aussi, sur ce qu'il vient de d&eacute;couvrir dans un tiroir "
  "&agrave; quatre heures du matin.")

p("La voix, cette fois, ne vient pas de l'os de son cr&acirc;ne. Elle sort "
  "du pon&ccedil;on lui-m&ecirc;me, m&eacute;tallique, minuscule, comme si l'objet "
  "&eacute;tait un vieux talkie-walkie qu'on aurait oubli&eacute; d'&eacute;teindre "
  "depuis sept ans.")

p("Un long silence suit l'ouverture du tiroir, pendant lequel "
  "Darius reste accroupi, immobile, &agrave; regarder cette petite "
  "pointe m&eacute;tallique qui ne bouge plus, comme s'il attendait "
  "qu'elle se calme d'elle-m&ecirc;me avant de se rapprocher. Le "
  "chauffage central se met en marche quelque part dans les "
  "murs, avec un cliquetis familier qui, cette nuit-l&agrave;, sonne "
  "diff&eacute;remment &mdash; plus proche, comme si la maison enti&egrave;re "
  "&eacute;coutait, elle aussi, ce qui allait se dire.")

S.append(Paragraph("KAYDEN (voix, depuis le pon&ccedil;on)", cn))
p("&laquo;&nbsp;Tu crois que je t'ai donn&eacute; &ccedil;a pour te faire un cadeau. "
  "C'est faux, mais c'est pas grave, tout le monde le croit au "
  "d&eacute;but. Je te l'ai donn&eacute; parce que t'es le premier, depuis "
  "longtemps, &agrave; &ecirc;tre revenu volontairement dans le Non-lieu sans "
  "que je t'y force. &Ccedil;a veut dire un truc pr&eacute;cis, Darius&nbsp;: quelque "
  "part en toi, une part de toi voulait savoir. Et une part qui "
  "veut savoir, &ccedil;a se dresse, avec de la patience, comme un chien "
  "qu'on dresse &agrave; revenir.&nbsp;&raquo;")

name("DARIUS")
p("&laquo;&nbsp;Je suis pas un chien. Et j'ai pas envie de vos pouvoirs si "
  "&ccedil;a fait tomber des vieux dans leurs escaliers.&nbsp;&raquo;")

S.append(Paragraph("KAYDEN", cn))
p("&laquo;&nbsp;Alors rends-le-moi. Ou plut&ocirc;t &mdash; non, tu peux pas. Il "
  "fonctionne d&eacute;j&agrave; plus vraiment pour moi. Il fonctionne pour "
  "celui qui l'a tenu le plus longtemps, et &ccedil;a, maintenant, c'est "
  "toi. Voil&agrave; ce que je veux vraiment, puisque t'as l'air de "
  "pr&eacute;f&eacute;rer les r&eacute;ponses claires &agrave; ton p&egrave;re&nbsp;: je veux une page. "
  "Pas la tienne. Une des cinq qu'il te reste en attente, celle "
  "que tu choisiras, n'importe laquelle. En &eacute;change, j'arr&ecirc;te de "
  "prendre dans les autres pour te nourrir, et le pon&ccedil;on ne "
  "co&ucirc;tera plus qu'&agrave; toi seul, d&eacute;sormais, chaque fois que tu "
  "t'en serviras. Une ann&eacute;e contre une ann&eacute;e, en quelque sorte. "
  "&Ccedil;a te para&icirc;t plus honn&ecirc;te, non&nbsp;?&nbsp;&raquo;")

p("Il repense &agrave; la premi&egrave;re fois, dans le Non-lieu, o&ugrave; Kayden "
  "s'&eacute;tait pr&eacute;sent&eacute; comme quelqu'un qui pensait &laquo;&nbsp;rendre "
  "service&nbsp;&raquo;, et se demande si c'est exactement ce que ce march&eacute; "
  "repr&eacute;sente, aujourd'hui &mdash; une nouvelle version, plus polie, "
  "plus raisonnable en apparence, du m&ecirc;me pi&egrave;ge tendu depuis "
  "trente ans &agrave; quiconque accepte de s'approcher trop pr&egrave;s.")

p("Il se rel&egrave;ve, finalement, et va s'asseoir sur le rebord de "
  "son lit, le pon&ccedil;on toujours dans la main, en essayant de se "
  "rappeler la derni&egrave;re fois qu'une d&eacute;cision aussi importante "
  "lui avait paru aussi impossible &agrave; prendre seul, sans personne "
  "pour la partager ou pour lui dire, une fois pour toutes, "
  "quelle serait la bonne r&eacute;ponse.")

p("Il pense aussi, malgr&eacute; lui, &agrave; ce que &ccedil;a signifierait vraiment "
  "de donner une page &mdash; laquelle des six ann&eacute;es en attente "
  "choisirait-il d'oublier volontairement, sachant que le vide "
  "laiss&eacute; ne serait pas combl&eacute; par une histoire de rechange "
  "cette fois, mais par rien du tout, un trou net dans sa propre "
  "vie qu'aucun collier retrouv&eacute; ne viendrait jamais r&eacute;v&eacute;ler. "
  "L'id&eacute;e le glace davantage que tout ce que Kayden a dit "
  "jusqu'ici.")

p("Darius referme le tiroir, brusquement, sur la voix qui continue "
  "de parler, &eacute;touff&eacute;e, indiff&eacute;rente au bois qui la s&eacute;pare de lui. "
  "Il s'assoit par terre, le dos contre son lit, et pour la premi&egrave;re "
  "fois depuis le d&eacute;but de toute cette histoire, il n'a pas peur de "
  "la machine, ni de Kayden, ni du Non-lieu. Il a peur de la "
  "logique de la proposition, qui ressemble beaucoup trop &agrave; celle "
  "que Franck s'&eacute;tait faite &agrave; lui-m&ecirc;me, un mardi, dans une "
  "voiture, &agrave; un feu rouge : &eacute;changer une douleur pr&eacute;cise et "
  "assumable contre une douleur diffuse, r&eacute;partie, invisible, "
  "qu'on peut se permettre de ne jamais vraiment regarder en face.")

p("Il repense &agrave; ce que Clara lui avait dit, quelques semaines "
  "plus t&ocirc;t, sur le pardon et la confiance, et se demande si "
  "comprendre les raisons de Kayden le rapproche de lui, ou si "
  "&ccedil;a rend au contraire encore plus difficile de continuer &agrave; le "
  "consid&eacute;rer, simplement, comme un ennemi.")

p("Il ressort son t&eacute;l&eacute;phone, tape le num&eacute;ro renomm&eacute; &laquo;&nbsp;Franck&nbsp;&raquo; "
  "sans le mot &laquo;&nbsp;Papa&nbsp;&raquo; devant, et reste un long moment le "
  "pouce suspendu au-dessus du bouton d'appel, avant de reposer "
  "le t&eacute;l&eacute;phone, &eacute;cran &eacute;teint, sur sa table de nuit. Ce n'est "
  "pas encore le moment. Il ne sait m&ecirc;me pas ce qu'il dirait, si "
  "son p&egrave;re d&eacute;crochait, ni si une seule des questions qui lui "
  "br&ucirc;lent la gorge pourrait seulement trouver une r&eacute;ponse "
  "honn&ecirc;te au bout du fil.")

p("Il pense &agrave; Clara, qui lui a dit &laquo;&nbsp;une laisse, pas un cadeau&nbsp;&raquo;. "
  "Il pense au pompier dans son escalier, &agrave; la pianiste qui a "
  "perdu, une apr&egrave;s-midi, la seule chose qui lui restait d'elle-m&ecirc;me. "
  "Il pense &agrave; Miel, qui n'a jamais vraiment &eacute;t&eacute; vivante sous cette "
  "table, dans cette maison parfaite, m&ecirc;me si sa truffe &eacute;tait froide "
  "et son pelage chaud sous ses doigts.")

p("Dehors, un chien aboie au loin, deux fois, puis se tait, et "
  "Darius reste immobile un long moment &agrave; l'&eacute;couter s'&eacute;loigner, "
  "sans savoir s'il vient d'entendre un vrai chien du quartier ou "
  "un dernier &eacute;cho envoy&eacute; expr&egrave;s par une machine qui sait, "
  "manifestement, exactement quel genre de bruit fait le plus mal "
  "&agrave; entendre au milieu de la nuit.")

p("Il ne rouvre pas le tiroir cette nuit-l&agrave;. Mais il ne le vide pas "
  "non plus, ne jette pas le pon&ccedil;on par la fen&ecirc;tre, ne le donne pas "
  "&agrave; Clara pour qu'elle le garde loin de lui. Il le laisse l&agrave;, "
  "dans le noir, sous les vieux cahiers, exactement comme Franck "
  "avait laiss&eacute; un collier trois semaines dans une bo&icirc;te &agrave; gants "
  "avant de trouver le courage, ou la l&acirc;chet&eacute;, de s'en d&eacute;barrasser "
  "pour de bon. Et c'est cette ressemblance-l&agrave;, plus que tout le "
  "reste, qui l'emp&ecirc;che de dormir jusqu'au petit matin.")

p("Il s'endort sans le vouloir, le pon&ccedil;on encore serr&eacute; dans son "
  "poing, vers quatre heures du matin, apr&egrave;s des heures &agrave; "
  "retourner dans sa t&ecirc;te la proposition de Kayden sans jamais "
  "trouver de r&eacute;ponse. C'est cette fatigue-l&agrave;, pr&eacute;cis&eacute;ment, "
  "cette porte laiss&eacute;e entrouverte parce qu'il n'avait plus la "
  "force de la fermer, que quelque chose attendait depuis onze "
  "chapitres, si patient qu'il n'a m&ecirc;me pas eu besoin de forcer "
  "quoi que ce soit.")

p("Darius se r&eacute;veille &mdash; ou plut&ocirc;t, quelque chose qui a la forme "
  "de son r&eacute;veil se produit &mdash; dans le noir absolu. Pas le noir "
  "d'une chambre &agrave; l'aube. Un noir sans dimension, sans mur pour "
  "le contenir, et au centre de ce noir, une seule certitude, "
  "glac&eacute;e&nbsp;: il est encore l&agrave;, il pense encore, il a peur encore, "
  "mais ses mains, quelque part loin au-dessus de lui, se l&egrave;vent "
  "sans qu'il leur ait rien demand&eacute;, ouvrent les volets, s'&eacute;tirent "
  "au soleil du matin comme si de rien n'&eacute;tait.")

S.append(Paragraph("DARIUS (de l'int&eacute;rieur, sans voix)", cn))
p("&laquo;&nbsp;Rends-moi mes mains. Rends-moi mes mains.&nbsp;&raquo;")

p("Il essaie tout ce qu'il conna&icirc;t pour se battre &mdash; hurler plus "
  "fort, penser &agrave; autre chose, se concentrer sur un seul souvenir "
  "assez pr&eacute;cis pour percer le noir &mdash; et chaque tentative se "
  "dissout avant m&ecirc;me d'avoir commenc&eacute;, comme s'il criait sous "
  "l'eau, dans une piscine dont il ne trouve ni le fond ni le "
  "bord. Le temps, ici, ne se compte pas de la m&ecirc;me mani&egrave;re "
  "qu'ailleurs. Il pourrait tout aussi bien avoir hurl&eacute; une minute "
  "ou une journ&eacute;e enti&egrave;re avant que quoi que ce soit ne bouge.")

p("Personne ne l'entend, pas m&ecirc;me la chose qui porte d&eacute;sormais "
  "son visage et descend prendre son petit-d&eacute;jeuner avec un calme "
  "que Darius n'a plus ressenti depuis des mois. Sa m&egrave;re le trouve "
  "adorable, ce matin-l&agrave;, plus poli que d'habitude, plus attentif, "
  "il l'aide &agrave; d&eacute;barrasser sans qu'elle ait &agrave; le demander deux "
  "fois. Au coll&egrave;ge, il r&eacute;pond juste &agrave; toutes les questions, m&ecirc;me "
  "sur des chapitres qu'il n'a jamais ouverts. Les pouvoirs, "
  "d&eacute;sormais, ne lui co&ucirc;tent plus rien &mdash; ni saignement de nez, "
  "ni migraine, ni vertige. Il rattrape un plateau qui tombe &agrave; la "
  "cantine sans effort visible, escalade un mur pour r&eacute;cup&eacute;rer un "
  "ballon coinc&eacute; sans un seul faux mouvement, sourit &agrave; tout le "
  "monde d'un sourire qui ne varie jamais assez pour qu'on le "
  "trouve suspect &mdash; juste assez pour que Clara, en le regardant "
  "traverser la cour, sente un froid remonter dans son dos sans "
  "savoir encore le nommer.")

p("Il tente, &agrave; un moment, de se concentrer non plus sur la "
  "rage de reprendre le contr&ocirc;le, mais sur un souvenir pr&eacute;cis "
  "&mdash; le poids de Miel contre ses pieds, un matin d'hiver &mdash; "
  "esp&eacute;rant que cette image, comme un ancrage, puisse le "
  "ramener plus pr&egrave;s de la surface. Elle vacille une seconde, "
  "faiblit, puis dispara&icirc;t &agrave; nouveau dans le noir, comme une "
  "bougie qu'on aurait essay&eacute; d'allumer dans un courant d'air "
  "trop fort pour elle.")

p("&Agrave; l'int&eacute;rieur, dans le noir sans dimension, Darius hurle. Il "
  "hurle pendant que son corps sourit &agrave; sa m&egrave;re. Il hurle pendant "
  "que son corps aide un professeur &agrave; porter des cahiers. Il "
  "d&eacute;couvre, avec une horreur froide, qu'il peut voir, entendre, "
  "sentir tout ce que fait ce corps qui n'est plus le sien &agrave; "
  "commander, mais qu'aucun son, aucun mouvement, ne remonte "
  "jamais jusqu'&agrave; la surface. Il est spectateur de sa propre vie, "
  "enferm&eacute; dans une pi&egrave;ce sans porte au fond de lui-m&ecirc;me, "
  "pendant que Kayden &mdash; car c'est bien lui, Darius le sait sans "
  "qu'on le lui dise, la m&ecirc;me pr&eacute;sence froide et patiente que "
  "dans le Non-lieu &mdash; conduit sa vie &agrave; sa place, avec une "
  "efficacit&eacute; qui donne envie de vomir.")

p("Le premier jour, personne ne remarque rien du tout, pas m&ecirc;me "
  "Clara, occup&eacute;e par un contr&ocirc;le d'histoire qui lui prend toute "
  "son attention, et Darius, enferm&eacute; dans le noir, comprend avec "
  "effroi que le silence complice de sa propre vie ordinaire "
  "pourrait, sans qu'on le veuille vraiment, devenir le meilleur "
  "alli&eacute; de Kayden.")

p("Le corps de Darius, ce m&ecirc;me soir-l&agrave;, prend le temps d'&eacute;crire "
  "&agrave; Franck un message d'anniversaire en avance, chaleureux, "
  "presque affectueux, quelque chose que le vrai Darius n'aurait "
  "jamais envoy&eacute; sans y r&eacute;fl&eacute;chir dix fois. &Agrave; l'int&eacute;rieur du noir, "
  "Darius sent, avec une horreur nouvelle, que Kayden ne se "
  "contente pas de piloter son corps &mdash; il essaie, m&eacute;thodiquement, "
  "de r&eacute;parer, &agrave; sa mani&egrave;re froide et calcul&eacute;e, tout ce qui, dans "
  "sa vie, ressemble &agrave; une fissure, comme un artisan qui colmate "
  "sans jamais demander si le propri&eacute;taire voulait vraiment que "
  "le trou soit rebouch&eacute;.")

p("Les deux premiers jours, Darius observe, impuissant, son corps "
  "&eacute;viter savamment tous les moments o&ugrave; quelqu'un aurait pu "
  "remarquer un vrai changement &mdash; il &eacute;vite les longues "
  "conversations avec Clara, pr&eacute;texte des devoirs pour ne pas "
  "rester seul avec elle plus de dix minutes, rit aux bonnes "
  "blagues au bon moment, avec un timing si parfait que m&ecirc;me "
  "Alex, pourtant sensible aux d&eacute;tails, ne remarque rien d'anormal "
  "avant le troisi&egrave;me jour.")

p("Le quatri&egrave;me jour, en fin d'apr&egrave;s-midi, le corps de Darius "
  "propose &agrave; Clara et Alex une chose qu'il n'aurait jamais os&eacute; "
  "proposer lui-m&ecirc;me&nbsp;: descendre voir les anciennes caves "
  "troglodytiques, sur le coteau au-dessus de la Loire, celles que "
  "les gens du coin appellent les &laquo;&nbsp;caves oubli&eacute;es&nbsp;&raquo; parce que "
  "plus personne n'y entre depuis un &eacute;boulement dans les ann&eacute;es "
  "quatre-vingt. Il pr&eacute;tend avoir trouv&eacute; quelque chose l&agrave;-bas, li&eacute; "
  "&agrave; M13, une preuve qui expliquerait tout, qui r&eacute;glerait tout, "
  "d&egrave;s ce soir. Clara h&eacute;site. Alex, lui, veut y croire &mdash; il veut "
  "tellement que cette histoire ait une fin propre qu'il n'entend "
  "pas, dans la voix de son meilleur ami, la seule chose qui a "
  "chang&eacute;&nbsp;: l'absence totale d'h&eacute;sitation.")

p("&Agrave; l'int&eacute;rieur du noir, Darius comprend, une seconde avant "
  "que ses propres l&egrave;vres ne prononcent le mot &laquo;&nbsp;grotte&nbsp;&raquo;, ce que "
  "Kayden pr&eacute;pare vraiment. Pas une preuve. Un pi&egrave;ge. Il n'a plus "
  "besoin de leur voler des fragments, un &agrave; un, dispers&eacute;s dans "
  "toute une ville, pendant des ann&eacute;es. Il a d&eacute;couvert, avec le "
  "corps de Darius, une porte plus rapide, plus directe, vers "
  "exactement ce qu'il a toujours voulu depuis le d&eacute;but&nbsp;: pas "
  "des pages. Des gens entiers.")

S.append(Paragraph("DARIUS (de l'int&eacute;rieur, sans voix)", cn))
p("&laquo;&nbsp;Clara, non. N'y va pas. C'est pas moi. C'est jamais &eacute;t&eacute; "
  "moi, depuis quatre jours.&nbsp;&raquo;")

p("Rien ne sort. Le corps sourit, tend une main amicale vers "
  "l'&eacute;paule de Clara, et elle le suit, comme Alex, dans la nuit "
  "tombante, vers le coteau et ses bouches noires creus&eacute;es dans "
  "le tuffeau, pendant que Darius, tout au fond de lui-m&ecirc;me, se "
  "met &agrave; se battre pour la premi&egrave;re fois contre les murs de sa "
  "propre prison, sans savoir s'il reste seulement quelques minutes "
  "avant que la porte de cette prison-l&agrave; ne se referme pour de "
  "bon, sur eux tous.")

p("L'entr&eacute;e des caves oubli&eacute;es est &agrave; peine plus large qu'une "
  "porte de garage, dissimul&eacute;e derri&egrave;re un rideau de lierre que "
  "le corps de Darius &eacute;carte avec une assurance que ni Clara ni "
  "Alex ne lui ont jamais connue pour ce genre de chose. &Agrave; "
  "l'int&eacute;rieur, l'air sent la pierre humide et quelque chose "
  "d'&eacute;lectrique, presque ozon&eacute;, la m&ecirc;me odeur que sur la place "
  "du march&eacute; le premier soir. Les parois de tuffeau, creus&eacute;es par "
  "des mains humaines il y a des si&egrave;cles pour en tirer la pierre "
  "des maisons de Luynes, portent, grav&eacute;es en profondeur, des "
  "centaines de num&eacute;ros &mdash; des pages, encore, toujours des "
  "pages, remontant plus loin dans le temps que Darius n'aurait "
  "jamais imagin&eacute; que M13 puisse remonter.")

p("Alex, derri&egrave;re eux, s'arr&ecirc;te net devant une inscription grav&eacute;e "
  "plus profond&eacute;ment que les autres, un pr&eacute;nom seul, sans nom de "
  "famille, dat&eacute; d'une ann&eacute;e ant&eacute;rieure &agrave; sa propre naissance, et "
  "reconnait, avec un frisson, le pr&eacute;nom de son oncle, celui qui "
  "&eacute;tait &laquo;&nbsp;parti chercher du travail en Belgique&nbsp;&raquo; et n'est "
  "jamais revenu. Il ne dit rien. Il se contente de poser sa main "
  "&agrave; plat contre la pierre froide, une seconde, avant de "
  "rattraper le groupe.")

p("Au fond de la premi&egrave;re salle, une lumi&egrave;re bleue p&acirc;le sourd du "
  "sol lui-m&ecirc;me, comme si la roche &eacute;tait devenue, par endroits, "
  "translucide. Le corps de Darius s'arr&ecirc;te au centre de cette "
  "lumi&egrave;re et se retourne vers Clara et Alex avec un sourire "
  "qui, cette fois, ne ressemble plus du tout &agrave; celui de Darius "
  "&mdash; trop large, trop immobile, comme dessin&eacute; sur son visage "
  "plut&ocirc;t que port&eacute; par lui.")

S.append(Paragraph("KAYDEN (dans le corps de Darius)", cn))
p("&laquo;&nbsp;Merci d'&ecirc;tre venus. Vraiment. Vous imaginez pas depuis "
  "combien de temps j'attends des invit&eacute;s qui viennent de "
  "eux-m&ecirc;mes, sans qu'on ait besoin de leur prendre une ann&eacute;e "
  "d'abord pour les convaincre.&nbsp;&raquo;")

p("Alex recule d'un pas. Clara, elle, ne bouge pas &mdash; elle fixe "
  "les mains de Darius, qui tremblent d'un tremblement bizarre, "
  "rythmique, comme un signal Morse qu'un mauvais &eacute;metteur "
  "n'arriverait pas &agrave; envoyer proprement. Elle a d&eacute;j&agrave; vu ce "
  "genre de d&eacute;tail quelque part&nbsp;: sur l'&eacute;cran de la machine, "
  "le tout premier soir, quand le texte s'affichait lettre par "
  "lettre, avec de petites pauses irr&eacute;guli&egrave;res.")

name("CLARA")
p("&laquo;&nbsp;T'es pas Darius.&nbsp;&raquo;")

S.append(Paragraph("KAYDEN", cn))
p("&laquo;&nbsp;Je suis exactement autant Darius que ce que vous "
  "appelez de la m&eacute;moire est fait de vrai souvenir et de "
  "reconstitution. La question, ma belle, c'est pas qui je suis. "
  "C'est ce que je peux faire, l&agrave;, maintenant, de vous deux.&nbsp;&raquo;")

p("Kayden fait un pas vers Alex, toujours avec ce sourire trop "
  "large, et penche la t&ecirc;te de Darius d'une fa&ccedil;on l&eacute;g&egrave;rement "
  "trop m&eacute;canique, comme un appareil qui &eacute;value une distance "
  "avant de l'ex&eacute;cuter. &laquo;&nbsp;Toi, dit-il &agrave; Alex, t'as un oncle qui "
  "attend depuis trente ans qu'on lui redonne un visage. &Ccedil;a "
  "pourrait s'arranger, ce soir, si tu restes calme.&nbsp;&raquo; Alex serre "
  "les poings, refuse de reculer davantage, malgr&eacute; la peur "
  "visible qui lui fait trembler la m&acirc;choire.")

p("Le sol tremble. Des filaments de lumi&egrave;re bleue montent des "
  "fissures du tuffeau et s'enroulent autour des chevilles d'Alex, "
  "qui crie, se d&eacute;bat, sans parvenir &agrave; reculer d'un centim&egrave;tre, "
  "comme si la roche elle-m&ecirc;me s'&eacute;tait mise &agrave; le r&eacute;clamer. Clara, "
  "elle, ne recule pas. Elle sort de sa poche le carnet &agrave; spirale "
  "qu'elle garde sur elle depuis le premier soir, l'ouvre &agrave; la "
  "page o&ugrave; elle a not&eacute;, de sa petite &eacute;criture serr&eacute;e&nbsp;: "
  "&laquo;&nbsp;collier &mdash; sujet : Darius L. &mdash; page 41&nbsp;&raquo;, et la brandit "
  "devant elle comme on brandit une preuve devant un tribunal.")

name("CLARA")
p("&laquo;&nbsp;Darius. Miel gratte encore &agrave; ta porte, tous les matins, "
  "&agrave; six heures. C'est ce que ton p&egrave;re a dit dans la maison "
  "parfaite, tu te souviens ? Sauf que c'est faux, c'est jamais "
  "arriv&eacute;, et toi, le vrai toi, tu sais faire la diff&eacute;rence entre "
  "un vrai souvenir et une page qu'on te donne &agrave; la place. Alors "
  "trouve-la. La diff&eacute;rence. Maintenant.&nbsp;&raquo;")

p("Elle jette le carnet. Il traverse la lumi&egrave;re bleue sans "
  "ralentir et vient frapper la poitrine du corps de Darius, "
  "s'ouvrant en plein vol &agrave; la bonne page, celle du collier, "
  "celle d'un petit gar&ccedil;on de huit ans qui avait attach&eacute; ce "
  "m&ecirc;me collier autour du cou d'un chiot qui sentait encore le "
  "shampoing pour animaux. Dans le noir sans dimension, quelque chose se d&eacute;chire. Darius, enferm&eacute; tout au "
  "fond de lui-m&ecirc;me, sent cette d&eacute;chirure comme une porte qu'on "
  "d&eacute;fonce enfin, et se jette dedans de toutes ses forces, avec "
  "une seule pens&eacute;e, plus solide que toutes les pages, tous les "
  "pouvoirs, tout ce que Kayden a jamais pu lui offrir&nbsp;: le poids "
  "pr&eacute;cis d'un chien de deux ans endormi contre ses pieds, un "
  "matin d'hiver, avant que quiconque n'ait invent&eacute; un mensonge "
  "pour le lui prendre.")

p("Alex, lib&eacute;r&eacute; des filaments, reste un instant sonn&eacute; au sol, "
  "avant de ramper vers Clara et de l'aider &agrave; se relever, tous "
  "deux les yeux fix&eacute;s sur le corps de Darius, sans savoir "
  "encore si ce qu'ils voient est une victoire ou seulement une "
  "pause avant que quelque chose de pire ne recommence.")

p("Le corps de Darius tombe &agrave; genoux. Les filaments bleus "
  "l&acirc;chent les chevilles d'Alex d'un coup, comme une main qui "
  "s'ouvre par surprise. Quand Darius rel&egrave;ve la t&ecirc;te, une "
  "seconde plus tard, ce sont bien ses propres yeux, sombres, "
  "humides, terrifi&eacute;s, qui regardent Clara et Alex &mdash; et non "
  "plus deux petits &eacute;crans indiff&eacute;rents affichant des lignes de "
  "texte.")

name("DARIUS")
p("&laquo;&nbsp;Je suis l&agrave;. C'est moi. Je suis d&eacute;sol&eacute;, je suis tellement "
  "d&eacute;sol&eacute;, je pouvais rien faire, je vous entendais et je "
  "pouvais rien &mdash;&nbsp;&raquo;")

p("Clara le rattrape avant qu'il ne s'effondre compl&egrave;tement, et "
  "les trois restent l&agrave;, serr&eacute;s, tremblants, au centre d'une "
  "lumi&egrave;re bleue qui p&acirc;lit lentement sans s'&eacute;teindre tout &agrave; "
  "fait, pendant qu'une voix, tr&egrave;s loin, presque tendre, murmure "
  "une derni&egrave;re phrase que seul Darius entend, quelque part au "
  "fond de son propre cr&acirc;ne, l&agrave; o&ugrave; il vient tout juste de "
  "reprendre sa place&nbsp;:")

S.append(Paragraph("KAYDEN (voix int&eacute;rieure, &agrave; peine audible)", cn))
p("&laquo;&nbsp;Cette fois-l&agrave;, oui. Mais je pars pas, Darius. Je me suis "
  "juste fait une petite place, l&agrave;, tout au fond, et j'attends "
  "pas grand-chose pour revenir. Un mauvais jour. Une nuit "
  "difficile. On se reverra bient&ocirc;t, toi et moi, m&ecirc;me quand tu "
  "t'y attendras plus.&nbsp;&raquo;")

p("Darius ne r&eacute;pond pas. Mais en sortant des caves, dans le "
  "froid de la nuit, il sait d&eacute;j&agrave; qu'il vient de gagner une "
  "bataille, pas une guerre, et que quelque part en lui, "
  "d&eacute;sormais et pour longtemps, il y a une petite lumi&egrave;re bleue "
  "qui ne s'&eacute;teindra plus jamais tout &agrave; fait.")

p("Alex ne dort plus dans le noir complet depuis la grotte. Il le "
  "dit &agrave; personne, mais Darius le sait sans qu'on ait besoin de "
  "le lui dire &mdash; une des cons&eacute;quences bizarres de tout &ccedil;a, "
  "c'est qu'il capte, parfois, sans le vouloir, des bribes de ce "
  "que ressentent les gens tout pr&egrave;s de lui, comme un fond "
  "sonore qu'il n'a pas demand&eacute; &agrave; entendre. Alex dort veilleuse "
  "allum&eacute;e, porte ouverte, depuis cette nuit-l&agrave;, et &eacute;vite, sans "
  "le formuler, de se retrouver seul dans une pi&egrave;ce avec Darius "
  "plus de quelques minutes.")

name("ALEX")
p("&laquo;&nbsp;C'est pas contre toi. Enfin si, un peu. Je sais que "
  "c'&eacute;tait pas toi, dans la grotte. Mais mon corps, lui, il fait "
  "pas la diff&eacute;rence aussi vite que ma t&ecirc;te.&nbsp;&raquo;")

p("Clara, elle, r&eacute;agit diff&eacute;remment &mdash; elle s'accroche &agrave; Darius "
  "avec une insistance presque exag&eacute;r&eacute;e, l'appelle deux fois par "
  "soir pour v&eacute;rifier qu'il va bien, s'invite chez lui sans "
  "pr&eacute;venir sous des pr&eacute;textes de devoirs qu'ils n'ont jamais "
  "eu l'intention de faire ensemble. Darius comprend, avec le "
  "temps, que sa fa&ccedil;on &agrave; elle de g&eacute;rer la peur n'est pas de "
  "s'&eacute;loigner, comme Alex, mais de se rapprocher jusqu'&agrave; ne "
  "plus laisser d'espace &agrave; l'inqui&eacute;tude pour s'installer.")

p("Au coll&egrave;ge, la rumeur d'une fugue de trois jours a fait le "
  "tour des classes plus vite que n'importe quelle explication "
  "raisonnable n'aurait pu la rattraper. Certains disent qu'il "
  "a fait une fugue amoureuse, d'autres qu'il a &eacute;t&eacute; hospitalis&eacute; "
  "en secret, un troisi&egrave;me groupe, plus cruel, murmure qu'il "
  "cherche juste l'attention. Darius laisse dire. Il a d&eacute;j&agrave; "
  "assez de vraies choses &agrave; porter pour perdre du temps &agrave; "
  "corriger des fausses.")

p("Le week-end suivant, Darius, Clara et Alex se retrouvent au "
  "parc pour tenter, ensemble, de comprendre les limites exactes "
  "de ce nouveau sens, en testant, sur des objets neutres pr&ecirc;t&eacute;s "
  "par des inconnus consentants, jusqu'o&ugrave; Darius peut deviner "
  "des d&eacute;tails sans qu'on les lui dise &mdash; un exercice qui "
  "fonctionne mieux qu'aucun d'eux ne l'aurait cru, et qui "
  "inqui&egrave;te Clara bien plus qu'il ne la rassure.")

p("Le lendemain, en cours de sport, le professeur lui demande "
  "pourquoi il refuse soudain de participer aux exercices "
  "d'escalade, lui qui avait pourtant &eacute;tonn&eacute; tout le monde "
  "quelques semaines plus t&ocirc;t, et Darius invente une douleur au "
  "poignet qui n'existe pas, un mensonge minuscule parmi tant "
  "d'autres qu'il accumule maintenant, presque sans y penser, "
  "comme si cette comp&eacute;tence-l&agrave; aussi, il l'avait apprise malgr&eacute; "
  "lui.")

p("Un soir, alors qu'ils regardent un film chez Clara sans "
  "vraiment le suivre, Alex finit par poser la question qu'il "
  "retient depuis des jours, d'une voix mal assur&eacute;e, presque "
  "honteuse de devoir la formuler tout haut.")

name("ALEX")
p("&laquo;&nbsp;Comment on saura, la prochaine fois, si c'est vraiment "
  "toi ? Genre, concr&egrave;tement. Y'a un signe, un mot de passe, "
  "n'importe quoi qu'on pourrait se dire pour &ecirc;tre s&ucirc;rs ?&nbsp;&raquo;")

p("Darius y r&eacute;fl&eacute;chit longuement, cherchant un d&eacute;tail assez "
  "personnel, assez ancr&eacute; en lui pour qu'aucune copie, aussi "
  "parfaite soit-elle, ne puisse le reproduire sans faille, avant "
  "de trouver, enfin, une r&eacute;ponse qui leur convient &agrave; tous les "
  "trois &mdash; le nom complet de Miel, jamais &eacute;crit nulle part, "
  "jamais prononc&eacute; devant Kayden : Miel-Ambre, comme l'avait "
  "surnomm&eacute;e sa m&egrave;re, une seule fois, le jour de son adoption, "
  "un d&eacute;tail si minuscule qu'il n'a jamais eu de raison de "
  "figurer dans aucun dossier.")

p("Sa m&egrave;re, de son c&ocirc;t&eacute;, a pris rendez-vous chez un "
  "psychologue sans lui demander son avis, un premier rendez-vous "
  "que Darius honore surtout pour lui faire plaisir, assis dans "
  "un fauteuil trop mou &agrave; r&eacute;pondre par monosyllabes &agrave; des "
  "questions sur son sommeil et son app&eacute;tit, incapable de dire "
  "un seul mot vrai sur ce qui lui arrive vraiment, parce que "
  "aucune phrase humaine normale ne contient de place pour "
  "&laquo;&nbsp;une machine m'a offert des pouvoirs qui font tomber des "
  "gens dans leurs escaliers&nbsp;&raquo;.")

p("Le professeur principal, remarquant les absences r&eacute;p&eacute;t&eacute;es et "
  "la fatigue visible de Darius, convoque sa m&egrave;re pour un "
  "entretien que Darius attend, assis sur une chaise trop petite "
  "dans le couloir de l'administration, en essayant d'imaginer ce "
  "qu'il pourrait bien dire si on lui demandait directement ce "
  "qui ne va pas. Il n'en dira rien, finalement. Sa m&egrave;re sort de "
  "l'entretien avec un rendez-vous de suivi et un regard encore "
  "plus inquiet qu'avant, et Darius comprend que chaque solution "
  "qu'il ne peut pas expliquer cr&eacute;e, en retour, un nouveau "
  "probl&egrave;me qu'il devra, lui aussi, un jour, g&eacute;rer par un "
  "mensonge.")

p("Darius ne discute pas. Il pense &agrave; Franck, &agrave; la fa&ccedil;on dont sa "
  "m&egrave;re a continu&eacute; &agrave; l'aimer pendant des ann&eacute;es apr&egrave;s le "
  "mensonge, et &agrave; quel point &ccedil;a n'avait, finalement, jamais fait "
  "dispara&icirc;tre la fissure &mdash; juste appris &agrave; vivre autour. Il "
  "comprend, pour la premi&egrave;re fois de mani&egrave;re aussi concr&egrave;te, "
  "que le pardon et la confiance sont deux choses diff&eacute;rentes, et "
  "qu'on peut donner l'un sans jamais retrouver l'autre au m&ecirc;me "
  "niveau qu'avant.")

p("Un dimanche, ils se retrouvent tous les trois sur la place du "
  "march&eacute;, en plein jour cette fois, pour regarder la machine "
  "d'un peu plus loin, sans s'en approcher &mdash; une sorte de rituel "
  "qu'ils ont invent&eacute; sans en parler, comme si le simple fait de "
  "la surveiller, m&ecirc;me &agrave; distance, pouvait emp&ecirc;cher qu'elle ne "
  "reprenne l'avantage sur eux. Elle reste &eacute;teinte, indiff&eacute;rente, "
  "patiente &agrave; sa mani&egrave;re, comme si elle savait qu'elle n'avait "
  "besoin de rien pr&eacute;cipiter.")

p("Le psychologue, lors du deuxi&egrave;me rendez-vous, remarque que "
  "Darius parle beaucoup, avec des mots pr&eacute;cis, de confiance et "
  "de trahison, de gens qui portent un visage familier sans "
  "vraiment &ecirc;tre eux-m&ecirc;mes, et note tout &ccedil;a soigneusement sans "
  "jamais deviner &agrave; quel point ses hypoth&egrave;ses classiques &mdash; le "
  "divorce des parents, le deuil d'un animal d'enfance &mdash; passent "
  "&agrave; c&ocirc;t&eacute; de la v&eacute;rit&eacute; tout en s'en approchant, par endroits, "
  "d'une mani&egrave;re presque troublante.")

p("La nuit, quand il ferme les yeux, une petite lumi&egrave;re bleue "
  "palpite parfois derri&egrave;re ses paupi&egrave;res, br&egrave;ve, comme un "
  "t&eacute;l&eacute;phone qui vibre dans une autre pi&egrave;ce. &Ccedil;a ne dure jamais "
  "plus d'une seconde. &Ccedil;a suffit pour qu'il se r&eacute;veille en sursaut, "
  "chaque fois, le c&oelig;ur battant, &agrave; v&eacute;rifier que ses mains lui "
  "appartiennent encore.")

p("C'est Clara qui a l'id&eacute;e, un samedi matin, en relisant son "
  "carnet pour la centi&egrave;me fois : et si l'entrep&ocirc;t que Darius "
  "avait visit&eacute; dans la maison parfaite, avec le dossier &agrave; son "
  "nom, n'&eacute;tait pas qu'un d&eacute;cor invent&eacute; par M13, mais un vrai "
  "lieu, quelque part, que le syst&egrave;me aurait simplement copi&eacute; "
  "pour construire son mensonge, comme il avait copi&eacute; la maison "
  "de Darius jusqu'au moindre d&eacute;tail ?")

p("Avant de se mettre &agrave; chercher, ils passent une heure enti&egrave;re, "
  "assis en cercle sur le tapis de la chambre de Clara, &agrave; "
  "reconstituer de m&eacute;moire, phrase par phrase, tout ce que Darius "
  "avait vu dans l'entrep&ocirc;t de la maison parfaite &mdash; le sigle &agrave; "
  "trois lettres, le num&eacute;ro de d&eacute;partement, le mot &laquo;&nbsp;R&Eacute;GIONAL&nbsp;&raquo; "
  "&agrave; moiti&eacute; effac&eacute; sous la rouille. Clara note tout dans son "
  "carnet, page apr&egrave;s page, avec la m&ecirc;me application qu'elle "
  "avait mise, deux ans plus t&ocirc;t, &agrave; consigner la disparition de "
  "la montre de son p&egrave;re, comme si tenir un registre pr&eacute;cis "
  "&eacute;tait, pour elle, une fa&ccedil;on de reprendre un peu de contr&ocirc;le "
  "sur un monde qui semblait avoir d&eacute;cid&eacute; d'en manquer "
  "cruellement.")

p("Clara distribue &agrave; chacun un petit morceau de papier sur lequel "
  "elle a &eacute;crit, la veille, le num&eacute;ro de t&eacute;l&eacute;phone des deux "
  "autres et celui des pompiers, &laquo;&nbsp;au cas o&ugrave; les portables "
  "captent pas l&agrave;-dedans&nbsp;&raquo;, une pr&eacute;caution presque com&eacute;dique "
  "qu'aucun des trois ne trouve dr&ocirc;le sur le moment, tant elle "
  "leur rappelle brutalement &agrave; quel point ce qu'ils s'appr&ecirc;tent "
  "&agrave; faire pourrait mal tourner.")

p("Darius, en attachant son v&eacute;lo, remarque que ses mains ne "
  "tremblent pas, contrairement &agrave; ce qu'il redoutait, et cette "
  "petite constatation, presque insignifiante, lui donne "
  "suffisamment de courage pour avancer le premier vers le "
  "grillage, sans attendre que Clara ou Alex ne prennent "
  "l'initiative &agrave; sa place.")

p("Clara relit &agrave; voix haute, une derni&egrave;re fois avant de partir, "
  "les r&egrave;gles qu'elle a &eacute;crites sp&eacute;cialement pour cette "
  "expedition, num&eacute;rot&eacute;es dans son carnet comme un vrai "
  "protocole officiel, et Alex les r&eacute;p&egrave;te apr&egrave;s elle, mi-s&eacute;rieux "
  "mi-moqueur, avant que Darius, lui, ne les r&eacute;p&egrave;te &agrave; son tour "
  "sans une once d'ironie, mesurant, mieux que les deux autres "
  "peut-&ecirc;tre, &agrave; quel point ces r&egrave;gles pourraient un jour leur "
  "sauver la vie.")

p("Ils passent aussi un moment &agrave; discuter de ce qu'ils feront "
  "s'ils trouvent vraiment quelque chose de dangereux &agrave; "
  "l'int&eacute;rieur, sans jamais tomber d'accord &mdash; Alex penche pour "
  "tout d&eacute;truire sur place, Clara pour tout documenter d'abord, "
  "Darius, lui, ne sait m&ecirc;me pas quelle r&eacute;ponse il pr&eacute;f&egrave;re "
  "entendre, tiraill&eacute; entre l'envie de comprendre et la peur de "
  "ce que comprendre pourrait finir par lui co&ucirc;ter.")

p("Darius, pendant ce temps, reste assis sur le rebord de la "
  "fen&ecirc;tre, silencieux, incapable de participer vraiment &agrave; ces "
  "recherches sans repenser sans cesse au dossier &agrave; son nom, "
  "aux voix superpos&eacute;es, &agrave; la sensation de vertige qui lui avait "
  "fait perdre, une seconde, la certitude d'&ecirc;tre encore "
  "compl&egrave;tement lui-m&ecirc;me. Il finit par proposer, d'une voix "
  "hesitante, de venir avec eux plut&ocirc;t que de les laisser y "
  "aller sans lui, une offre que Clara accepte imm&eacute;diatement, "
  "sans discuter, comme si elle avait attendu depuis le d&eacute;but "
  "qu'il trouve seul le courage de le proposer.")

p("Alex, lui, passe le m&ecirc;me temps sur son ordinateur, &agrave; "
  "&eacute;plucher les archives num&eacute;ris&eacute;es de la pr&eacute;fecture, un site "
  "administratif lent et mal con&ccedil;u qu'il maudit &agrave; voix haute toutes "
  "les cinq minutes, jusqu'&agrave; tomber, presque par hasard, sur un "
  "plan cadastral des ann&eacute;es quatre-vingt-dix mentionnant un "
  "&laquo;&nbsp;centre technique r&eacute;gional&nbsp;&raquo; d&eacute;class&eacute; en 1994, sans autre "
  "pr&eacute;cision, comme si l'administration elle-m&ecirc;me avait pr&eacute;f&eacute;r&eacute; "
  "rester vague sur ce qui s'&eacute;tait vraiment pass&eacute; cette ann&eacute;e-l&agrave;.")

p("Ils le trouvent en deux heures de recherches sur une carte, en "
  "croisant le panneau &agrave; demi effac&eacute; qu'il avait vu &mdash; PROPRI&Eacute;T&Eacute; "
  "DE L'&Eacute;TAT, un num&eacute;ro de d&eacute;partement disparu depuis un "
  "red&eacute;coupage &mdash; avec une liste de b&acirc;timents administratifs "
  "d&eacute;saffect&eacute;s le long de la d&eacute;partementale, entre Luynes et "
  "Fondettes. Un seul correspond&nbsp;: un ancien centre de recherche "
  "rattach&eacute;, jusqu'en 1994, &agrave; un minist&egrave;re dont personne, "
  "aujourd'hui, ne se souvient tout &agrave; fait du nom exact.")

p("Avant de partir, ils passent chez Alex prendre une vieille "
  "trousse &agrave; outils qui appartenait &agrave; son grand-p&egrave;re, contenant "
  "une pince coupante et une lampe torche solide, &laquo;&nbsp;au cas o&ugrave; "
  "on aurait vraiment besoin de forcer un truc&nbsp;&raquo;, dit-il sans "
  "conviction, davantage pour se rassurer lui-m&ecirc;me que pour "
  "convaincre les deux autres. Clara, elle, glisse dans son sac "
  "le pon&ccedil;on, propos&eacute; par Darius pour la premi&egrave;re fois depuis "
  "la grotte, avec une consigne claire&nbsp;: elle seule le porte "
  "aujourd'hui, pour que rien ne puisse tenter Darius pendant "
  "l'exploration.")

p("Ils y vont &agrave; v&eacute;lo, en plein jour cette fois, tous les trois "
  "ensemble, avec une r&egrave;gle que Clara a pos&eacute;e sans discussion "
  "possible&nbsp;: personne ne touche &agrave; rien seul, personne ne reste "
  "en arri&egrave;re, et au moindre signe &eacute;trange, on part, sans "
  "discuter, m&ecirc;me si on est &agrave; deux m&egrave;tres de la r&eacute;ponse. "
  "L'entrep&ocirc;t est bien r&eacute;el, grillage rouill&eacute; compris, mais &agrave; "
  "l'int&eacute;rieur, pas de cartons align&eacute;s, pas de voix superpos&eacute;es "
  "&mdash; juste des bureaux vides, des dossiers administratifs "
  "banals, et, au fond d'un couloir, une porte blind&eacute;e, r&eacute;cente, "
  "qui jure compl&egrave;tement avec le reste du b&acirc;timent, ferm&eacute;e par "
  "un digicode dont les touches les plus us&eacute;es dessinent, "
  "clairement, un chiffre&nbsp;: quatre, z&eacute;ro, quatre.")

p("Darius reconna&icirc;t, en s'approchant du grillage, l'endroit exact "
  "o&ugrave; il &eacute;tait pass&eacute; seul, dans la version fausse de sa vie, et "
  "sent un vertige familier lui monter aux tempes en r&eacute;alisant "
  "que ses pieds, aujourd'hui, dans le vrai Luynes, connaissent "
  "d&eacute;j&agrave; parfaitement le chemin, comme si son corps gardait la "
  "trace de trajets que sa m&eacute;moire consciente n'avait jamais "
  "vraiment enregistr&eacute;s.")

p("Une camionnette d'entretien passe sur la d&eacute;partementale, ralentit "
  "presque au niveau du grillage, puis repart sans s'arr&ecirc;ter, ce "
  "qui suffit &agrave; leur rappeler que le monde ordinaire continue "
  "de tourner tout autour d'eux, indiff&eacute;rent &agrave; ce qu'ils "
  "s'appr&ecirc;tent &agrave; d&eacute;couvrir, et que personne, en dehors de leur "
  "petit groupe, ne viendra les aider si quelque chose tourne "
  "mal derri&egrave;re ce grillage.")

p("Ils s'installent sur le bord du foss&eacute;, en face du b&acirc;timent, "
  "pour manger les sandwiches que Clara a pr&eacute;par&eacute;s avant de "
  "partir, une pause qu'aucun des trois n'avait vraiment "
  "planifi&eacute;e mais qui s'impose d'elle-m&ecirc;me, comme si personne "
  "n'&eacute;tait vraiment press&eacute; de franchir cette derni&egrave;re barri&egrave;re. "
  "Alex plaisante, maladroitement, sur le fait qu'ils ressemblent "
  "&agrave; des personnages de film qui vont forc&eacute;ment mourir dans les "
  "dix minutes suivantes, et personne ne rit vraiment, mais "
  "personne ne lui demande non plus de se taire.")

p("Le code &laquo;&nbsp;404&nbsp;&raquo; ouvre la porte au premier essai, ce qui "
  "d&eacute;range Darius presque plus qu'un &eacute;chec ne l'aurait fait &mdash; "
  "comme si quelqu'un, quelque part, avait voulu que ce code reste "
  "assez simple pour &ecirc;tre trouv&eacute; par la bonne personne, un jour.")

p("En entrant, Darius remarque une petite plaque m&eacute;tallique viss&eacute;e "
  "&agrave; c&ocirc;t&eacute; de l'interrupteur, presque effac&eacute;e par la rouille, sur "
  "laquelle on devine encore &laquo;&nbsp;LABORATOIRE 3 &mdash; ACC&Egrave;S "
  "R&Eacute;SERV&Eacute; PERSONNEL AUTORIS&Eacute;&nbsp;&raquo;. Il pense, sans pouvoir "
  "s'en emp&ecirc;cher, &agrave; toutes les personnes qui ont d&ucirc; passer cette "
  "m&ecirc;me porte, chaque matin, pendant des ann&eacute;es, en pensant "
  "faire un travail ordinaire, sans savoir ce que leurs recherches "
  "finiraient par devenir des d&eacute;cennies plus tard.")

p("Alex passe la salle au peigne fin avant de laisser Clara et "
  "Darius s'approcher des &eacute;crans, v&eacute;rifiant les prises &eacute;lectriques, "
  "les c&acirc;bles au sol, la moindre cam&eacute;ra de surveillance encore "
  "susceptible de fonctionner apr&egrave;s trente ans d'abandon &mdash; une "
  "prudence n&eacute;e directement de la grotte, de la fa&ccedil;on dont un "
  "pi&egrave;ge peut se cacher derri&egrave;re la promesse d'une r&eacute;ponse. Il "
  "ne trouve rien de suspect. Juste de la poussi&egrave;re, du silence, "
  "et cette impression, tenace, que l'endroit tout entier retient "
  "son souffle depuis trois d&eacute;cennies, en attendant que quelqu'un "
  "vienne enfin lire ce qu'il contient.")

p("Derri&egrave;re la porte, une salle de serveurs miniature, poussi&eacute;reuse "
  "mais encore aliment&eacute;e, un bourdonnement continu de "
  "ventilateurs fatigu&eacute;s. Sur un des &eacute;crans encore allum&eacute;s, un "
  "dossier ouvert, dat&eacute; de 1991, intitul&eacute; &laquo;&nbsp;PROGRAMME "
  "M.13 &mdash; M&Eacute;MOIRE, INTERFACE, 13&egrave;me ESSAI&nbsp;&raquo;. Le treizi&egrave;me. Pas "
  "un nom myst&eacute;rieux invent&eacute; pour faire peur &mdash; juste un "
  "num&eacute;ro d'essai, comme n'importe quel programme scientifique "
  "qui a &eacute;chou&eacute; douze fois avant celui-l&agrave;.")

p("Darius s'arr&ecirc;te un moment devant un vieux tableau blanc, "
  "encore couvert de sch&eacute;mas trac&eacute;s au feutre s&eacute;ch&eacute;, repr&eacute;sentant "
  "ce qui ressemble &agrave; un cerveau humain reli&eacute; par des fl&egrave;ches &agrave; "
  "une s&eacute;rie de rectangles &eacute;tiquet&eacute;s &laquo;&nbsp;archive&nbsp;&raquo;, comme le "
  "brouillon d'une id&eacute;e qui avait d&ucirc;, autrefois, para&icirc;tre "
  "g&eacute;niale &agrave; ceux qui l'avaient dessin&eacute;e, avant de devenir "
  "exactement ce contre quoi ils luttent aujourd'hui.")

p("Clara, de son c&ocirc;t&eacute;, prend des photos syst&eacute;matiques de chaque "
  "salle avant m&ecirc;me de commencer &agrave; fouiller quoi que ce soit, "
  "une habitude qu'elle justifie en disant qu'elle pr&eacute;f&egrave;re "
  "toujours avoir une preuve du point de d&eacute;part, au cas o&ugrave; "
  "quelque chose changerait, plus tard, sans qu'ils s'en rendent "
  "compte sur le moment.")

p("Alex trouve, dans un des premiers classeurs qu'il ouvre, une "
  "liste d'employ&eacute;s du centre technique, avec leurs fonctions "
  "respectives, et lit &agrave; voix haute chaque nom, esp&eacute;rant "
  "reconna&icirc;tre, peut-&ecirc;tre, celui d'un habitant actuel de Luynes "
  "qu'ils pourraient un jour aller questionner, sans succ&egrave;s "
  "&mdash; tous les noms semblent appartenir &agrave; des gens qui ont "
  "d&eacute;m&eacute;nag&eacute; ou qui ne sont, tout simplement, plus l&agrave; pour "
  "r&eacute;pondre &agrave; quoi que ce soit.")

p("Darius, avant de rejoindre les deux autres, reste un moment "
  "seul devant la plaque rouill&eacute;e du &laquo;&nbsp;LABORATOIRE 3&nbsp;&raquo;, la "
  "main pos&eacute;e dessus, essayant de sentir, comme avec le mur de "
  "sa chambre, si quelque chose se cache derri&egrave;re. Rien ne "
  "r&eacute;pond, cette fois &mdash; juste le froid ordinaire du m&eacute;tal, "
  "et &ccedil;a, &eacute;trangement, le rassure plus que &ccedil;a ne le d&eacute;&ccedil;oit.")

p("Clara s'installe devant l'ordinateur avec l'aisance d'une "
  "personne qui a d&eacute;j&agrave; pass&eacute; des heures &agrave; fouiller des documents "
  "administratifs pour comprendre le d&eacute;part de son propre p&egrave;re, "
  "et navigue de dossier en dossier avec une m&eacute;thode presque "
  "professionnelle, class&eacute;e par ann&eacute;e, puis par th&egrave;me, en lisant "
  "&agrave; voix haute chaque titre pour qu'Alex et Darius, qui "
  "fouillent les classeurs physiques &agrave; c&ocirc;t&eacute;, sachent imm&eacute;diatement "
  "si quelque chose m&eacute;rite qu'on s'arr&ecirc;te dessus.")

p("Les premiers dossiers d&eacute;crivent une exp&eacute;rience presque "
  "banale, m&eacute;dicale&nbsp;: comment stocker des souvenirs traumatiques "
  "sur un support externe pour soulager des patients qui n'arrivent "
  "plus &agrave; vivre avec eux. Une id&eacute;e g&eacute;n&eacute;reuse, au d&eacute;part, "
  "signe d'un chercheur dont le nom appara&icirc;t partout&nbsp;: K. VASSEUR. "
  "Puis, dans un dossier plus tardif, dat&eacute; de 1994, une note "
  "manuscrite, scann&eacute;e, dont l'&eacute;criture ronde, appliqu&eacute;e, Darius "
  "reconna&icirc;t imm&eacute;diatement&nbsp;: la m&ecirc;me que sur l'&eacute;tiquette du "
  "collier.")

S.append(Paragraph("NOTE DE K. VASSEUR (lue &agrave; voix haute par Clara)", cn))
p("&laquo;&nbsp;Le protocole fonctionne trop bien. Les patients ne "
  "veulent plus r&eacute;cup&eacute;rer leurs souvenirs, m&ecirc;me gu&eacute;ris. Ils "
  "pr&eacute;f&egrave;rent la version qu'on leur a donn&eacute;e &agrave; la place. J'ai "
  "compris, trop tard, que le probl&egrave;me n'&eacute;tait jamais la "
  "douleur. C'&eacute;tait le confort. On a construit la machine &agrave; "
  "mensonges la plus efficace jamais con&ccedil;ue, en croyant "
  "construire un rem&egrave;de.&nbsp;&raquo;")

p("Darius fait d&eacute;filer d'autres pages du m&ecirc;me dossier, plus "
  "techniques, couvertes de sch&eacute;mas qu'aucun d'eux ne comprend "
  "vraiment, sauf une phrase soulign&eacute;e deux fois au stylo rouge, "
  "qui semble avoir &eacute;t&eacute; ajout&eacute;e plus tard, d'une main press&eacute;e, "
  "presque paniqu&eacute;e : &laquo;&nbsp;le sujet 13 ne doit en aucun cas &ecirc;tre "
  "d&eacute;connect&eacute; sans protocole complet &mdash; risque de fragmentation "
  "irr&eacute;versible de la conscience h&eacute;berg&eacute;e&nbsp;&raquo;. Personne, dans la "
  "pi&egrave;ce, n'ose demander &agrave; voix haute ce que &laquo;&nbsp;le sujet 13&nbsp;&raquo; "
  "pourrait bien d&eacute;signer, alors que tous les trois pensent, au "
  "m&ecirc;me instant, exactement au m&ecirc;me nom.")

p("Le minist&egrave;re a ferm&eacute; le programme en 1994, officiellement "
  "pour raisons budg&eacute;taires. Le dossier de K. Vasseur, lui, "
  "s'arr&ecirc;te net &agrave; cette date, sans aucune mention de ce qu'il "
  "est devenu ensuite &mdash; ni licenciement, ni mutation, ni d&eacute;c&egrave;s. "
  "Juste un silence administratif, le genre de silence, pense "
  "Darius, qu'on reconna&icirc;t maintenant tr&egrave;s bien.")

name("CLARA")
p("&laquo;&nbsp;1991, &ccedil;a fait trente-cinq ans. Si Vasseur avait dix-neuf "
  "ans en 1994, il en aurait aujourd'hui cinquante et un, s'il "
  "&eacute;tait rest&eacute; humain. &Ccedil;a veut dire qu'il est bloqu&eacute; l&agrave;-dedans "
  "depuis plus longtemps que nos parents ne sont vivants pour "
  "certains d'entre eux. &Ccedil;a me donne le vertige rien que d'y "
  "penser.&nbsp;&raquo;")

p("Darius s'assoit lentement sur une chaise pivotante recouverte "
  "de poussi&egrave;re, essayant d'imaginer ce chercheur, K. Vasseur, "
  "dans cette m&ecirc;me pi&egrave;ce, des d&eacute;cennies plus t&ocirc;t, persuad&eacute; de "
  "faire quelque chose de bien, avant de d&eacute;couvrir, trop tard, "
  "&agrave; quel point une bonne intention peut d&eacute;railler quand "
  "personne ne s'arr&ecirc;te pour se demander si elle devrait "
  "continuer. Il pense &agrave; son propre p&egrave;re, &agrave; la fa&ccedil;on dont un "
  "mensonge, lui aussi, avait commenc&eacute; petit, presque "
  "raisonnable, avant de devenir quelque chose que plus personne "
  "ne pouvait arr&ecirc;ter.")

p("Darius se souvient, en lisant ce registre par-dessus l'&eacute;paule "
  "d'Alex, d'une phrase que sa m&egrave;re r&eacute;p&egrave;te souvent, sur les "
  "gens qui sacrifient trop pour trop peu en retour, sans jamais "
  "avoir imagin&eacute;, jusqu'ici, &agrave; quel point cette phrase pourrait "
  "un jour s'appliquer aussi litt&eacute;ralement &agrave; un adolescent de "
  "dix-neuf ans devenu, malgr&eacute; lui, la voix d'un syst&egrave;me tout "
  "entier.")

p("Alex, plus loin, tombe sur un vieux registre de paie o&ugrave; "
  "figure, page apr&egrave;s page, le salaire modeste vers&eacute; chaque mois "
  "au jeune Kayden Vasseur pendant les quelques mois qu'a dur&eacute; "
  "son emploi officiel, une somme d&eacute;risoire pour un travail dont "
  "les cons&eacute;quences, trente ans plus tard, semblent toujours "
  "totalement hors de proportion.")

p("Clara, en silence, prend en photo chaque page du dossier de "
  "Franck avant de le refermer, r&eacute;p&eacute;tant le m&ecirc;me r&eacute;flexe qu'elle "
  "avait eu, plus t&ocirc;t, avec les documents scientifiques, comme si "
  "documenter chaque preuve &eacute;tait devenu, pour elle, la seule "
  "fa&ccedil;on de garder un semblant de contr&ocirc;le sur une journ&eacute;e qui "
  "leur &eacute;chappait, un peu plus, &agrave; chaque nouvelle d&eacute;couverte.")

p("Darius demande &agrave; relire une deuxi&egrave;me fois la demande "
  "d'indemnisation, cherchant, entre les lignes administratives "
  "et froides, un d&eacute;tail suppl&eacute;mentaire sur ce que Franck avait "
  "v&eacute;cu exactement, sans en trouver davantage que ce que le "
  "premier passage lui avait d&eacute;j&agrave; r&eacute;v&eacute;l&eacute; &mdash; comme si "
  "l'administration elle-m&ecirc;me avait pris soin de ne rien laisser "
  "filtrer de trop pr&eacute;cis sur ce qui s'&eacute;tait r&eacute;ellement pass&eacute;.")

p("Alex, en attendant que Darius et Clara terminent leur lecture, "
  "s'occupe &agrave; photographier chaque page avec son t&eacute;l&eacute;phone, "
  "m&eacute;thodiquement, une par une, en expliquant &agrave; voix basse que "
  "si jamais quelqu'un venait effacer cet entrep&ocirc;t comme le "
  "reste, il voulait au moins qu'il reste une trace ailleurs, "
  "hors de port&eacute;e de la machine et de son syst&egrave;me &mdash; une id&eacute;e "
  "simple, presque na&iuml;ve, mais qui rassure les trois autant "
  "qu'elle les inqui&egrave;te sur ce qu'ils pressentent d&eacute;j&agrave; pouvoir "
  "leur arriver.")

p("Ils passent un long moment, avant &ccedil;a, &agrave; fouiller m&eacute;thodiquement "
  "les autres tiroirs de la salle, r&eacute;partis en trois zones que "
  "Clara a d&eacute;sign&eacute;es d'un geste sec, comme un chef d'&eacute;quipe qui "
  "n'a plus le temps pour les h&eacute;sitations. La plupart des dossiers "
  "ne concernent que des questions administratives sans int&eacute;r&ecirc;t "
  "&mdash; budgets, feuilles de pr&eacute;sence, plannings de maintenance des "
  "ann&eacute;es quatre-vingt-dix, dont le simple ennui rassure presque "
  "Darius, comme la preuve que tout, ici, n'&eacute;tait pas construit "
  "pour faire peur.")

p("C'est Alex, en fouillant une armoire m&eacute;tallique au fond de la "
  "salle, qui trouve le second dossier &mdash; plus fin, plus r&eacute;cent, "
  "sans rapport apparent avec le programme de 1991, sauf le "
  "tampon dans le coin, le m&ecirc;me sigle &agrave; trois lettres que sur "
  "le panneau ext&eacute;rieur. &Agrave; l'int&eacute;rieur, une demande "
  "d'indemnisation, dat&eacute;e d'il y a huit ans, d&eacute;pos&eacute;e par un "
  "certain FRANCK L., pour &laquo;&nbsp;dommages psychologiques li&eacute;s &agrave; "
  "une participation ant&eacute;rieure, mineur, non r&eacute;mun&eacute;r&eacute;e, &agrave; "
  "un essai clinique du programme M.13, phase r&eacute;siduelle&nbsp;&raquo;.")

p("Clara relit le document une seconde fois, &agrave; voix basse "
  "cette fois, pour v&eacute;rifier qu'elle n'a pas mal compris un mot, "
  "avant de le tendre &agrave; Darius sans commentaire, consciente que "
  "certaines nouvelles doivent &ecirc;tre lues par soi-m&ecirc;me pour vraiment "
  "&ecirc;tre re&ccedil;ues. Le papier tremble l&eacute;g&egrave;rement entre les doigts "
  "de Darius, non pas &agrave; cause du courant d'air froid de la "
  "pi&egrave;ce, mais parce que ses mains, tout simplement, ont d&eacute;cid&eacute; "
  "de r&eacute;agir avant que le reste de lui n'ait fini de comprendre.")

p("Darius lit la phrase trois fois avant qu'elle ne veuille bien "
  "avoir un sens. Son p&egrave;re, enfant, a particip&eacute; &mdash; ou a &eacute;t&eacute; "
  "utilis&eacute;, le dossier ne pr&eacute;cise jamais lequel des deux mots "
  "serait le bon &mdash; &agrave; une phase tardive du m&ecirc;me programme que "
  "celui qui, des d&eacute;cennies plus tard, a construit une machine "
  "sur la place du march&eacute; de Luynes pour lui demander une "
  "ann&eacute;e contre une page.")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a veut dire que ton p&egrave;re savait. Ou qu'il a oubli&eacute; "
  "qu'il savait, ce qui, avec ce truc-l&agrave;, revient un peu au "
  "m&ecirc;me.&nbsp;&raquo;")

p("Alex, mal &agrave; l'aise, propose de refermer l'armoire et de "
  "partir, jugeant sans doute que la d&eacute;couverte touche &agrave; "
  "quelque chose de trop intime pour rester dans une conversation "
  "de groupe. Darius secoue la t&ecirc;te. Il a d&eacute;j&agrave; pass&eacute; assez "
  "d'ann&eacute;es &agrave; g&eacute;rer seul, dans sa t&ecirc;te, tout ce qui concerne "
  "son p&egrave;re. Ce soir, pour une fois, il pr&eacute;f&egrave;re que quelqu'un "
  "d'autre soit dans la pi&egrave;ce quand une v&eacute;rit&eacute; de cette taille "
  "se pr&eacute;sente.")

p("Darius pense au collier dans la bo&icirc;te &agrave; gants, aux trois "
  "semaines avant que Franck ne s'en d&eacute;barrasse. &Agrave; la facilit&eacute; "
  "presque anormale avec laquelle un mensonge lui &eacute;tait venu, ce "
  "soir-l&agrave;, dans la voiture, &agrave; un feu rouge, comme si quelque "
  "part en lui, une part de son p&egrave;re avait d&eacute;j&agrave; &eacute;t&eacute; "
  "entra&icirc;n&eacute;e, enfant, &agrave; pr&eacute;f&eacute;rer une histoire confortable &agrave; "
  "une v&eacute;rit&eacute; qui fait mal. Ce n'est pas une excuse. Mais &ccedil;a "
  "ressemble, pour la premi&egrave;re fois, &agrave; une explication, et "
  "Darius ne sait pas encore ce qu'il pr&eacute;f&egrave;re entre les deux.")

p("Clara pose une main sur l'&eacute;paule de Darius, sans rien dire, "
  "un geste simple qui vaut plus, sur le moment, que n'importe "
  "quelle phrase de r&eacute;confort qu'elle aurait pu essayer de "
  "trouver. Darius replie soigneusement le document, le glisse "
  "dans la poche int&eacute;rieure de sa veste, &agrave; c&ocirc;t&eacute; de l'endroit o&ugrave; "
  "il portait autrefois le pon&ccedil;on, comme s'il fallait d&eacute;sormais "
  "porter les deux ensemble, la preuve et l'objet, la v&eacute;rit&eacute; sur "
  "son p&egrave;re et le pouvoir qui la lui a r&eacute;v&eacute;l&eacute;e.")

p("Il essaie d'imaginer Franck, enfant, dans ce m&ecirc;me b&acirc;timent, "
  "assis peut-&ecirc;tre sur cette m&ecirc;me chaise pivotante, sans "
  "comprendre encore ce qu'on &eacute;tait en train de lui faire, et "
  "sans savoir qu'un jour, des ann&eacute;es plus tard, il choisirait de "
  "mentir &agrave; son propre fils avec une facilit&eacute; qui n'&eacute;tait peut-&ecirc;tre "
  "pas vraiment la sienne, mais celle qu'on lui avait, en quelque "
  "sorte, appris &agrave; porter, sans jamais lui demander son avis.")

name("ALEX")
p("&laquo;&nbsp;&Ccedil;a fait bizarre de dire &ccedil;a, mais si c'est vraiment ce "
  "programme qui l'a rendu comme &ccedil;a, ton p&egrave;re, alors c'est "
  "peut-&ecirc;tre pas juste ton histoire &agrave; toi qu'on est en train de "
  "d&eacute;m&ecirc;ler. C'est celle de tout le monde qui est pass&eacute; par ici, "
  "et de leurs enfants, et des enfants de leurs enfants.&nbsp;&raquo;")

p("Clara referme d'abord le dossier de Franck, doucement, comme "
  "on referme la porte d'une chambre o&ugrave; quelqu'un vient de "
  "s'endormir apr&egrave;s avoir longtemps pleur&eacute;, et propose qu'ils "
  "prennent tous les trois cinq minutes avant de continuer &agrave; "
  "fouiller. Personne ne parle pendant ces cinq minutes. Alex "
  "s'assoit par terre, le dos contre un serveur &eacute;teint, et regarde "
  "le plafond. Darius fait les cent pas entre deux &eacute;tag&egrave;res, le "
  "dossier de son p&egrave;re toujours &agrave; la main, incapable de le "
  "reposer tout &agrave; fait.")

p("Au fond de l'armoire, sous le dossier de Franck, une derni&egrave;re "
  "chemise, plus mince encore, marqu&eacute;e d'un tampon rouge&nbsp;: "
  "&laquo;&nbsp;PERSONNEL &mdash; SUJET INTERNE&nbsp;&raquo;. Une photo agraf&eacute;e en "
  "premi&egrave;re page montre un homme jeune, la trentaine, blouse "
  "blanche, des lunettes fines, souriant devant un tableau couvert "
  "d'&eacute;quations. Le nom sous la photo&nbsp;: KAYDEN VASSEUR, fils du "
  "chercheur principal, embauch&eacute; &agrave; dix-neuf ans comme "
  "assistant sur le programme de son propre p&egrave;re.")

p("Clara range son carnet, ferm&eacute; d&eacute;sormais sur des r&eacute;v&eacute;lations "
  "bien plus lourdes que tout ce qu'elle y avait consign&eacute; "
  "jusqu'ici, et se demande, en silence, si elle devra un jour "
  "montrer ces pages &agrave; sa propre m&egrave;re, ou si certaines "
  "v&eacute;rit&eacute;s sont destin&eacute;es &agrave; rester enferm&eacute;es entre trois "
  "adolescents et un vieux carnet &agrave; spirale, pour toujours.")

p("Ils quittent l'armoire, laissant tout en ordre autant que "
  "possible, comme s'il &eacute;tait important, malgr&eacute; tout, de traiter "
  "ces documents avec un minimum de respect &mdash; les vies "
  "entass&eacute;es dans ces dossiers m&eacute;ritent au moins &ccedil;a, se dit "
  "Darius en refermant le dernier tiroir, m&ecirc;me si personne "
  "d'autre qu'eux trois ne le saura jamais.")

p("Alex propose, timidement, qu'ils prennent aussi cette photo "
  "en souvenir, d'une certaine mani&egrave;re, pour se rappeler que "
  "Kayden a exist&eacute; avant de devenir tout ce qu'il est devenu, "
  "et Clara, sans discuter, la photographie soigneusement avant "
  "que Darius ne referme le dossier pour de bon.")

p("Darius replace soigneusement la photo du jeune footballeur "
  "dans son enveloppe transparente avant de refermer le dossier "
  "complet, un geste presque respectueux, comme s'il rangeait, "
  "d'une certaine mani&egrave;re, ce qu'il restait d'humanit&eacute; visible "
  "de Kayden Vasseur, quelque part o&ugrave; personne ne viendrait le "
  "d&eacute;ranger davantage.")

p("Clara ferme doucement le dossier une premi&egrave;re fois, avant "
  "de le rouvrir presque aussit&ocirc;t, incapable de r&eacute;sister &agrave; l'envie "
  "de tout relire depuis le d&eacute;but, comme si une seconde lecture "
  "pouvait, par miracle, changer la fa&ccedil;on dont l'histoire de "
  "Kayden se terminait.")

p("Alex, en la voyant, laisse &eacute;chapper un petit rire triste, sans "
  "joie, en remarquant &agrave; voix haute que Kayden, sur cette "
  "vieille photo de foot, ressemble &eacute;trangement &agrave; un gar&ccedil;on de "
  "sa propre classe, un certain Th&eacute;o qui joue avant-centre le "
  "mercredi, comme si les visages des adolescents heureux se "
  "ressemblaient tous un peu, &agrave; travers les d&eacute;cennies, avant que "
  "la vie ne d&eacute;cide, pour certains d'entre eux, de prendre un "
  "chemin totalement diff&eacute;rent des autres.")

p("Sous la photo, agraf&eacute;e en biais comme si quelqu'un l'avait "
  "ajout&eacute;e &agrave; la h&acirc;te, une seconde image montre le m&ecirc;me jeune "
  "homme, plus t&ocirc;t, adolescent, souriant sur un terrain de foot, "
  "un ballon sous le bras, entour&eacute; de camarades dont aucun ne "
  "sera jamais mentionn&eacute; dans le moindre autre dossier de "
  "l'entrep&ocirc;t. Darius regarde longtemps cette photo-l&agrave;, plus que "
  "la premi&egrave;re, parce qu'elle montre quelqu'un qui ressemble "
  "&eacute;trangement &agrave; n'importe quel gar&ccedil;on de son coll&egrave;ge, quelqu'un "
  "qui aurait pu, dans une autre vie, &ecirc;tre assis &agrave; c&ocirc;t&eacute; de lui en "
  "cours d'EPS plut&ocirc;t que devenir une voix dans un pon&ccedil;on.")

p("Plus loin dans le dossier, une lettre manuscrite adress&eacute;e "
  "au p&egrave;re de Kayden, jamais envoy&eacute;e apparemment, tant l'&eacute;criture "
  "y est h&eacute;sitante, ratur&eacute;e par endroits : &laquo;&nbsp;Papa, je sais que tu "
  "vas pas comprendre pourquoi je reste tard le soir. C'est pas "
  "pour t'emb&ecirc;ter. C'est parce que j'ai peur que si personne "
  "surveille les serveurs cette nuit, tout ce sur quoi t'as "
  "travaill&eacute; depuis que je suis n&eacute; disparaisse d'un coup, comme "
  "si &ccedil;a avait jamais exist&eacute;. Je peux pas laisser faire &ccedil;a. Pas "
  "&agrave; toi.&nbsp;&raquo; La lettre s'arr&ecirc;te l&agrave;, sans signature, comme si "
  "celui qui l'&eacute;crivait avait &eacute;t&eacute; interrompu avant de la finir.")

p("Le dernier document du dossier, dat&eacute; de la fermeture "
  "officielle en 1994, est un rapport d'incident, trois lignes "
  "s&egrave;ches&nbsp;: le jeune Vasseur, refusant l'arr&ecirc;t du programme, "
  "se serait connect&eacute; seul, une nuit, &agrave; l'interface centrale, "
  "pour &laquo;&nbsp;emp&ecirc;cher la perte des donn&eacute;es accumul&eacute;es&nbsp;&raquo;. On ne "
  "l'a jamais retrouv&eacute;. Le b&acirc;timent a ferm&eacute; la semaine "
  "suivante. Personne, dans aucun dossier, n'a jamais reli&eacute; sa "
  "disparition &agrave; quoi que ce soit d'autre qu'un accident regrettable, "
  "class&eacute; sans suite, faute de corps &agrave; retrouver.")

name("DARIUS")
p("&laquo;&nbsp;Il avait dix-neuf ans. Il voulait juste pas que le travail "
  "de son p&egrave;re disparaisse pour rien.&nbsp;&raquo;")

p("Dans un coin de sa t&ecirc;te, la petite lumi&egrave;re bleue palpite, une "
  "seconde, comme si quelqu'un, tr&egrave;s loin l&agrave;-dedans, venait "
  "d'entendre son propre nom prononc&eacute; avec autre chose que de "
  "la peur, pour la premi&egrave;re fois depuis trente ans. Darius "
  "referme le dossier, les mains tremblantes, en comprenant que "
  "ce qu'ils affrontent depuis le d&eacute;but n'est pas un monstre "
  "invent&eacute;, ni une machine sans &acirc;me, mais un gar&ccedil;on &agrave; peine "
  "plus vieux que lui, mort en essayant de sauver quelque chose "
  "qu'il aimait, et devenu, sans l'avoir choisi, exactement le "
  "genre de pi&egrave;ge dont son p&egrave;re avait pass&eacute; sa vie &agrave; essayer "
  "de prot&eacute;ger les autres.")

p("Darius reste longtemps immobile, le dossier ouvert sur les "
  "genoux, &agrave; regarder alternativement les deux photos de "
  "Kayden Vasseur &mdash; l'adolescent souriant sur le terrain de "
  "foot, et le jeune chercheur en blouse blanche, &agrave; peine plus "
  "&acirc;g&eacute; &mdash; en essayant d'imaginer &agrave; quel moment pr&eacute;cis, entre "
  "ces deux photos, quelqu'un avait cess&eacute; d'&ecirc;tre simplement un "
  "gar&ccedil;on pour devenir, sans jamais l'avoir vraiment d&eacute;cid&eacute;, une "
  "voix pi&eacute;g&eacute;e dans un pon&ccedil;on depuis trente ans.")

name("CLARA")
p("&laquo;&nbsp;Il avait dix-neuf ans et il voulait sauver le travail de "
  "son p&egrave;re. Toi t'as quatorze ans et t'essaies de sauver la "
  "v&eacute;rit&eacute; sur le tien. C'est le m&ecirc;me genre d'amour, Darius, "
  "juste employ&eacute; dans deux directions oppos&eacute;es. &Ccedil;a devrait te "
  "faire peur, un peu, de voir &agrave; quel point &ccedil;a se ressemble.&nbsp;&raquo;")

p("Personne ne dit rien pendant un long moment apr&egrave;s &ccedil;a. Alex "
  "referme doucement l'armoire m&eacute;tallique, comme si la fermer "
  "trop fort risquait de r&eacute;veiller quelque chose qu'ils venaient "
  "&agrave; peine de comprendre &agrave; quel point il fallait le laisser "
  "tranquille encore un peu.")

p("Ils referment l'armoire, &eacute;teignent les &eacute;crans, ressortent par la "
  "porte blind&eacute;e sans un mot, comme si parler risquait de "
  "r&eacute;veiller quelque chose qu'il valait mieux laisser dormir "
  "encore une nuit. Dehors, le soleil de fin d'apr&egrave;s-midi frappe "
  "le grillage rouill&eacute; d'une lumi&egrave;re presque douce, presque "
  "banale, comme si le monde ordinaire n'avait pas la moindre "
  "id&eacute;e de ce qu'ils venaient de trouver &agrave; quinze m&egrave;tres sous "
  "terre.")

p("Ils s'arr&ecirc;tent tous les trois &agrave; un feu rouge, celui, prend "
  "conscience Darius avec un frisson, qui ressemble &agrave; s'y "
  "m&eacute;prendre &agrave; celui d&eacute;crit dans la note manuscrite de son p&egrave;re, "
  "sans savoir si c'est vraiment le m&ecirc;me carrefour ou si son "
  "esprit, satur&eacute; de r&eacute;v&eacute;lations, commence &agrave; voir des signes "
  "partout, y compris l&agrave; o&ugrave; il n'y en a probablement aucun.")

p("&Agrave; v&eacute;lo, sur le chemin du retour, personne ne parle de "
  "Kayden Vasseur, dix-neuf ans, mort en voulant sauver le travail "
  "de son p&egrave;re. Personne ne parle de Franck non plus, du dossier "
  "&agrave; son nom, de ce que &ccedil;a change ou pas de savoir qu'un "
  "mensonge peut avoir des racines plus vieilles que celui qui le "
  "raconte. Ils roulent, c&ocirc;te &agrave; c&ocirc;te, dans le silence pr&eacute;cis des "
  "gens qui ont besoin de digerer avant de pouvoir seulement "
  "commencer &agrave; comprendre.")

p("Alex, avant de tourner dans sa rue, s'arr&ecirc;te une derni&egrave;re "
  "fois, pose une main sur l'&eacute;paule de Darius, sans un mot, un "
  "geste qui vaut, entre eux, plus que n'importe quelle phrase "
  "qu'ils auraient pu trouver pour dire qu'ils sont contents "
  "d'&ecirc;tre encore l&agrave;, tous les trois, apr&egrave;s tout ce que la "
  "journ&eacute;e vient de leur mettre sur les &eacute;paules.")

p("C'est Clara qui rompt le silence, la premi&egrave;re, en freinant "
  "devant chez elle.")

p("Il monte lentement les marches vers sa chambre, la main "
  "tra&icirc;nant sur la rampe comme il le faisait enfant, et s'arr&ecirc;te "
  "un instant devant la porte du salon, o&ugrave; sa m&egrave;re regarde la "
  "t&eacute;l&eacute;vision sans vraiment la suivre, perdue dans ses propres "
  "pens&eacute;es, et se demande, une fois de plus, combien de v&eacute;rit&eacute;s "
  "elle porte elle aussi, seule, sans jamais les avoir partag&eacute;es "
  "avec personne.")

p("Darius pense, une derni&egrave;re fois avant de rentrer chez lui, "
  "&agrave; cette phrase de Clara sur l'amour employ&eacute; dans deux "
  "directions oppos&eacute;es, et se dit que si Kayden a pu, un jour, "
  "&ecirc;tre quelqu'un capable d'un tel amour pour son p&egrave;re, alors "
  "peut-&ecirc;tre que quelque chose de cette part-l&agrave; existe encore, "
  "quelque part, sous trente ans de col&egrave;re et de solitude "
  "num&eacute;rique.")

p("Alex propose, avant de se s&eacute;parer, qu'ils se retrouvent tous "
  "les trois le lendemain matin, m&ecirc;me un dimanche, m&ecirc;me sans "
  "raison pr&eacute;cise, juste pour &ecirc;tre ensemble une heure ou deux, "
  "et personne ne discute cette id&eacute;e, comme si, apr&egrave;s une "
  "journ&eacute;e pareille, rester chacun seul de son c&ocirc;t&eacute; &eacute;tait "
  "devenu, temporairement, la pire option possible.")

p("Un chat de gouttière traverse la rue devant eux, sans se "
  "presser, et va se coucher sur le muret d'en face, indiff&eacute;rent "
  "&agrave; tout ce que les trois adolescents viennent de traverser, "
  "et ce simple d&eacute;tail, absurde, presque com&eacute;dique, fait "
  "esquisser &agrave; Darius son premier vrai sourire depuis la porte "
  "blind&eacute;e.")

p("Elle enl&egrave;ve son casque, le tient contre sa hanche, et regarde "
  "longuement le ciel qui rougit doucement au-dessus des toits, "
  "comme si elle cherchait dans cette couleur ordinaire une "
  "fa&ccedil;on de se raccrocher &agrave; quelque chose de simple avant de "
  "reprendre une conversation aussi lourde que celle qu'ils "
  "s'appr&ecirc;tent &agrave; avoir.")

name("CLARA")
p("&laquo;&nbsp;Si Kayden avait dix-neuf ans quand c'est arriv&eacute;... &ccedil;a veut "
  "dire qu'il est plus vieux que nous de cinq ans, pas de trois "
  "d&eacute;cennies. &Ccedil;a veut dire que c'est presque un grand fr&egrave;re "
  "coinc&eacute; l&agrave;-dedans depuis trente ans, pas un vieux savant fou. "
  "&Ccedil;a change quoi, &ccedil;a, pour toi&nbsp;?&nbsp;&raquo;")

p("Elle range son v&eacute;lo contre le mur de l'immeuble, s'assoit "
  "sur la premi&egrave;re marche de l'escalier, et attend, patiente, "
  "comme si elle savait que Darius avait besoin de temps avant "
  "de r&eacute;pondre &agrave; une question aussi grande, pos&eacute;e apr&egrave;s une "
  "journ&eacute;e aussi longue. Alex reste debout, un peu en retrait, "
  "les mains dans les poches, regardant le ciel qui commence &agrave; "
  "s'assombrir au-dessus des toits de Luynes.")

p("Darius n'a pas de r&eacute;ponse toute pr&ecirc;te. Il pense &agrave; la lumi&egrave;re "
  "bleue qui palpite parfois derri&egrave;re ses paupi&egrave;res, qui a fr&eacute;mi "
  "diff&eacute;remment quand il a lu le nom de Vasseur &agrave; voix haute "
  "dans la salle des serveurs &mdash; pas de col&egrave;re, pas de menace, "
  "quelque chose de plus proche, s'il devait le dire, de la "
  "surprise d'&ecirc;tre reconnu.")

p("Sa m&egrave;re frappe doucement &agrave; sa porte pour lui souhaiter bonne "
  "nuit, remarque qu'il a l'air ailleurs, lui demande si tout va "
  "bien d'une voix qui ne s'attend d&eacute;j&agrave; plus vraiment &agrave; une "
  "r&eacute;ponse honn&ecirc;te, tant elle s'est habitu&eacute;e, ces derni&egrave;res "
  "semaines, &agrave; recevoir des &laquo;&nbsp;oui &ccedil;a va&nbsp;&raquo; qui sonnent creux. "
  "Darius lui r&eacute;pond &laquo;&nbsp;&ccedil;a va, maman&nbsp;&raquo;, et pour la premi&egrave;re fois "
  "depuis des semaines, il se demande, avec un pincement au "
  "c&oelig;ur, si sa m&egrave;re ne conna&icirc;t pas, elle aussi, sa propre "
  "collection de pages qu'on lui a jamais rendues.")

p("Ce soir-l&agrave;, seul dans sa chambre, avant de s'endormir, Darius "
  "sort le pon&ccedil;on du tiroir pour la premi&egrave;re fois depuis la "
  "grotte, non pas pour s'en servir, juste pour le tenir dans sa "
  "main, et murmure, sans trop savoir &agrave; qui il s'adresse au "
  "juste&nbsp;:")

name("DARIUS")
p("&laquo;&nbsp;Je te pardonne pas. Mais je crois que je commence &agrave; "
  "comprendre. Et &ccedil;a, c'est d&eacute;j&agrave; plus que ce que j'ai jamais "
  "r&eacute;ussi &agrave; donner &agrave; mon propre p&egrave;re.&nbsp;&raquo;")

p("Il pense &agrave; ce qu'Alex a dit dans l'entrep&ocirc;t, sur la port&eacute;e "
  "de tout &ccedil;a &mdash; que ce n'est peut-&ecirc;tre pas seulement son "
  "histoire, ni celle de Franck, mais celle de dizaines, peut-&ecirc;tre "
  "de centaines de familles de la r&eacute;gion, chacune portant sa "
  "propre version d'un mensonge n&eacute;cessaire, sans savoir que "
  "toutes ces versions se rejoignent, quelque part, dans un "
  "entrep&ocirc;t abandonn&eacute; ou dans une grotte au-dessus de la "
  "Loire.")

p("Rien ne r&eacute;pond, cette fois. Pas de voix dans l'os du cr&acirc;ne, "
  "pas de lumi&egrave;re, juste le silence ordinaire d'une chambre "
  "d'adolescent un dimanche soir, et, tr&egrave;s loin sous la terre, &agrave; "
  "quinze kilom&egrave;tres de l&agrave;, un &eacute;cran qui, pour la premi&egrave;re "
  "fois depuis trente ans, affiche autre chose qu'un mensonge en "
  "attente d'&ecirc;tre racont&eacute; &mdash; un seul mot, immobile, sur fond "
  "noir&nbsp;: MERCI.")

p("Le lendemain matin, Darius se r&eacute;veille avec la "
  "sensation &eacute;trange d'avoir dormi plus profond&eacute;ment "
  "que d'habitude, comme si cette br&egrave;ve communication "
  "nocturne, quelle qu'en soit la nature exacte, avait "
  "all&eacute;g&eacute; un poids qu'il ne mesurait m&ecirc;me plus "
  "consciemment depuis des semaines.")

p("Il retrouve Clara et Alex &agrave; l'arr&ecirc;t de bus habituel, "
  "et leur raconte, &agrave; voix basse pour ne pas &ecirc;tre "
  "entendu des autres &eacute;l&egrave;ves, ce mot unique apparu sur "
  "l'&eacute;cran de son ordinateur, cette gratitude "
  "myst&eacute;rieuse dont ni lui ni ses amis ne parviennent &agrave; "
  "identifier l'origine exacte avec certitude.")

name("CLARA")
p("&laquo;&nbsp;'Merci.' &Ccedil;a peut venir de tellement de monde "
  "diff&eacute;rent, Darius. Kayden, la Marge elle-m&ecirc;me, ou "
  "m&ecirc;me juste ton propre subconscient qui essaie de te "
  "rassurer apr&egrave;s une journ&eacute;e difficile. On saura "
  "probablement jamais avec certitude.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;Perso, je pr&eacute;f&egrave;re penser que c'est un truc "
  "positif, quel que soit qui l'a envoy&eacute;. On a eu tellement "
  "de trucs flippants ces derniers temps, &ccedil;a fait du bien "
  "d'avoir, pour une fois, un myst&egrave;re qui fait pas peur.&nbsp;&raquo;")

p("Ils montent dans le bus scolaire ensemble, cette "
  "routine quotidienne retrouvant, l'espace d'un trajet "
  "ordinaire, une saveur presque r&eacute;confortante apr&egrave;s "
  "tant de r&eacute;v&eacute;lations bouleversantes, et Darius, "
  "regardant par la vitre le paysage familier de Luynes "
  "d&eacute;filer, se surprend &agrave; esp&eacute;rer, sans trop y croire, "
  "que ce mot de remerciement marque peut-&ecirc;tre le d&eacute;but "
  "d'une accalmie bienvenue dans cette histoire qui ne "
  "cesse de le d&eacute;passer.")

p("Les semaines suivantes confirment partiellement "
  "cet espoir prudent, aucune manifestation "
  "particuli&egrave;rement inqui&eacute;tante ne venant troubler le "
  "quotidien des trois amis, qui retrouvent, "
  "progressivement, une routine scolaire presque "
  "normale, entrecoup&eacute;e simplement de r&eacute;unions "
  "r&eacute;guli&egrave;res consacr&eacute;es &agrave; consigner, dans le carnet de "
  "Clara, chaque d&eacute;tail m&ecirc;me minime susceptible "
  "d'&eacute;clairer davantage leur compr&eacute;hension de la "
  "situation.")

p("Darius, profitant de cette accalmie relative, "
  "entreprend de renouer plus s&eacute;rieusement avec son "
  "p&egrave;re, multipliant les visites du week-end au-del&agrave; "
  "du simple planning de garde impos&eacute; par le divorce, "
  "sentant confus&eacute;ment qu'une part de la r&eacute;ponse &agrave; "
  "tout ce myst&egrave;re pourrait se nicher dans les silences "
  "encore jamais explor&eacute;s de sa propre histoire "
  "familiale.")

p("Franck, surpris mais touch&eacute; par cet int&eacute;r&ecirc;t "
  "renouvel&eacute; de son fils, r&eacute;pond avec une maladresse "
  "sinc&egrave;re &agrave; ces visites plus fr&eacute;quentes, proposant des "
  "activit&eacute;s simples &mdash; une partie de p&ecirc;che au bord de "
  "la Loire, un match de foot regard&eacute; ensemble &agrave; la "
  "t&eacute;l&eacute;vision &mdash; sans jamais soup&ccedil;onner que ces "
  "moments partag&eacute;s repr&eacute;sentent, pour Darius, bien "
  "plus qu'un simple rapprochement filial ordinaire.")

name("FRANCK")
p("&laquo;&nbsp;&Ccedil;a me fait plaisir que tu veuilles passer plus "
  "de temps ensemble, fiston. J'avoue que j'osais "
  "esp&eacute;rer, ces derni&egrave;res ann&eacute;es, qu'on finirait par "
  "retrouver un peu de complicit&eacute;, m&ecirc;me apr&egrave;s tout ce "
  "qui s'est pass&eacute; entre ta m&egrave;re et moi.&nbsp;&raquo;")

p("Darius, lors de l'une de ces visites, se risque "
  "enfin &agrave; poser une question qu'il retient depuis "
  "longtemps, profitant d'un moment de calme partag&eacute; "
  "devant la t&eacute;l&eacute;vision, cherchant, sans le formuler "
  "directement, &agrave; sonder si son p&egrave;re conna&icirc;t quoi que "
  "ce soit sur d'&eacute;ventuelles histoires &eacute;tranges li&eacute;es &agrave; "
  "leur famille.")

name("DARIUS")
p("&laquo;&nbsp;Papa, t'as jamais entendu parler de trucs "
  "bizarres, genre inexplicables, qui seraient arriv&eacute;s "
  "dans notre famille ? Genre des l&eacute;gendes, des "
  "histoires qu'on racontait de g&eacute;n&eacute;ration en "
  "g&eacute;n&eacute;ration ?&nbsp;&raquo;")

p("Franck se raidit imperceptiblement &agrave; cette "
  "question, une r&eacute;action fugace que Darius remarque "
  "sans encore pouvoir l'interpr&eacute;ter correctement, "
  "avant que son p&egrave;re ne r&eacute;ponde, apr&egrave;s une h&eacute;sitation "
  "&agrave; peine perceptible, d'un ton faussement d&eacute;tach&eacute; "
  "qui ne trompe qu'&agrave; moiti&eacute; son fils d&eacute;sormais "
  "attentif &agrave; chaque nuance.")

name("FRANCK")
p("&laquo;&nbsp;Non, rien de particulier que je sache. Pourquoi "
  "cette question, tout d'un coup ? T'as entendu "
  "quelque chose &agrave; l'&eacute;cole ?&nbsp;&raquo;")

p("Darius, sentant confus&eacute;ment qu'il vient d'effleurer "
  "quelque chose d'important sans parvenir &agrave; "
  "l'identifier pr&eacute;cis&eacute;ment, n'insiste pas davantage ce "
  "soir-l&agrave;, rangeant cette r&eacute;action &eacute;trange de son p&egrave;re "
  "dans un coin de sa m&eacute;moire, pressentant, sans "
  "encore le savoir avec certitude, qu'il faudra "
  "beaucoup plus de temps et d'&eacute;preuves partag&eacute;es "
  "avant que Franck n'accepte enfin de lever le voile "
  "sur ses propres secrets familiaux.")

p("Il rentre chez sa m&egrave;re ce soir-l&agrave; avec cette "
  "sensation famili&egrave;re d'avoir touch&eacute; du doigt une "
  "v&eacute;rit&eacute; plus grande sans pouvoir encore la nommer, "
  "et raconte &agrave; Clara, le lendemain matin, cette "
  "r&eacute;action &eacute;trange de son p&egrave;re, esp&eacute;rant qu'elle "
  "saurait, avec son esprit toujours plus analytique "
  "que le sien, en tirer une conclusion qu'il ne "
  "parvient pas &agrave; formuler seul.")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a confirme ce que je pensais depuis le "
  "d&eacute;but, Darius. Ton p&egrave;re sait quelque chose. Peut-&ecirc;tre "
  "pas tout, mais quelque chose. Faudra juste &ecirc;tre "
  "patients, je crois, et pas le brusquer. Les gens "
  "qui portent des secrets depuis trop longtemps, &ccedil;a "
  "se force pas &agrave; parler, &ccedil;a s'apprivoise "
  "doucement.&nbsp;&raquo;")

p("Cette sagesse pr&eacute;coce de Clara, d&eacute;j&agrave; visible &agrave; "
  "quatorze ans dans sa mani&egrave;re de comprendre les "
  "gens, rassure Darius sur la strat&eacute;gie &agrave; adopter "
  "d&eacute;sormais face &agrave; son p&egrave;re &mdash; continuer &agrave; se "
  "rapprocher de lui sans jamais forcer la "
  "conversation sur ces sujets sensibles, esp&eacute;rant "
  "qu'un jour, naturellement, la confiance accumul&eacute;e "
  "suffirait &agrave; faire tomber les derni&egrave;res barri&egrave;res.")

p("Clara elle-m&ecirc;me, en r&eacute;fl&eacute;chissant &agrave; cette "
  "situation familiale complexe, repense &agrave; sa propre "
  "m&egrave;re, veuve depuis plusieurs ann&eacute;es d&eacute;j&agrave;, et &agrave; "
  "cette mani&egrave;re toute personnelle qu'elle a "
  "d&eacute;velopp&eacute;e de g&eacute;rer son propre chagrin en le "
  "gardant soigneusement &agrave; distance de sa fille, une "
  "dynamique familiale qui, sans &ecirc;tre identique &agrave; "
  "celle de Darius et Franck, partage n&eacute;anmoins "
  "cette m&ecirc;me r&eacute;ticence &agrave; aborder frontalement les "
  "sujets douloureux.")

name("CLARA")
p("&laquo;&nbsp;J'crois qu'on a tous, dans nos familles "
  "respectives, ce genre de silence qu'on n'ose "
  "jamais vraiment briser. Peut-&ecirc;tre que c'est &ccedil;a, en "
  "fait, le vrai point commun entre nous trois &mdash; on "
  "sait tous ce que &ccedil;a fait de grandir avec des "
  "questions qu'on pose jamais.&nbsp;&raquo;")

p("Cette r&eacute;flexion partag&eacute;e, plus profonde que leur "
  "&acirc;ge ne le laisserait presager, renforce chez Darius "
  "le sentiment r&eacute;confortant de ne pas &ecirc;tre seul face "
  "&agrave; ces dynamiques familiales complexes, et il se "
  "promet, silencieusement, de faire tout son "
  "possible pour ne jamais reproduire, envers ses "
  "propres enfants futurs, ce genre de silence "
  "prot&eacute;g&eacute; qui finit toujours, tot ou tard, par peser "
  "plus lourd que la v&eacute;rit&eacute; elle-m&ecirc;me.")

p("Alex, silencieux durant cette conversation "
  "introspective entre Clara et Darius, finit par "
  "ajouter sa propre perspective, r&eacute;v&eacute;lant, avec une "
  "pudeur inhabituelle chez lui, que sa propre "
  "famille, en apparence si simple et unie, "
  "dissimule elle aussi certains non-dits concernant "
  "un grand-p&egrave;re disparu dans des circonstances "
  "jamais totalement &eacute;claircies.")

name("ALEX")
p("&laquo;&nbsp;Mon grand-p&egrave;re paternel, personne en parle "
  "jamais vraiment chez nous. Je sais juste qu'il "
  "est parti un jour et qu'il est jamais revenu, sans "
  "qu'on sache exactement pourquoi. Peut-&ecirc;tre que "
  "c'est juste une histoire triste ordinaire, mais "
  "apr&egrave;s tout ce qu'on vit en ce moment, &ccedil;a me fait "
  "me poser des questions.&nbsp;&raquo;")

p("Cette r&eacute;v&eacute;lation inattendue, formul&eacute;e presque "
  "timidement par Alex, ouvre une porte "
  "suppl&eacute;mentaire sur laquelle Darius et Clara "
  "n'avaient jamais song&eacute; &agrave; s'interroger, tous deux "
  "se demandant, sans le formuler explicitement, si "
  "cette histoire de mensonges familiaux prot&eacute;cteurs "
  "et de secrets jamais r&eacute;v&eacute;l&eacute;s ne serait pas, en "
  "fin de compte, bien plus r&eacute;pandue &agrave; Luynes qu'ils "
  "ne l'auraient jamais imagin&eacute;.")

name("DARIUS")
p("&laquo;&nbsp;Peut-&ecirc;tre qu'on devrait tous les trois "
  "essayer de creuser un peu nos histoires "
  "familiales respectives, du coup. Genre "
  "s&eacute;rieusement, pas juste en surface. &Ccedil;a serait "
  "peut-&ecirc;tre utile de savoir si y'a d'autres secrets "
  "comme &ccedil;a qui traînent dans nos familles, m&ecirc;me "
  "sans rapport direct avec ce qui m'arrive &agrave; "
  "moi.&nbsp;&raquo;")

p("Cette proposition, accueillie avec enthousiasme "
  "par Clara et une curiosit&eacute; prudente par Alex, "
  "donne naissance &agrave; un petit projet parall&egrave;le que "
  "les trois amis m&egrave;nent discr&egrave;tement durant les "
  "semaines suivantes, interrogeant grands-parents "
  "et parents &eacute;loign&eacute;s sur l'histoire familiale, "
  "sans jamais r&eacute;v&eacute;ler la v&eacute;ritable raison de cette "
  "curiosit&eacute; soudaine.")

p("Ce projet, men&eacute; en parall&egrave;le de leur enqu&ecirc;te "
  "principale sur la Marge, leur permet, sans qu'ils "
  "s'en rendent compte imm&eacute;diatement, de "
  "d&eacute;velopper des comp&eacute;tences de recherche "
  "familiale et historique qui s'av&eacute;reront, dans les "
  "mois suivants, particuli&egrave;rement pr&eacute;cieuses pour "
  "mener &agrave; bien leurs investigations plus s&eacute;rieuses "
  "sur Templier, Vasseur, et l'histoire millénaire "
  "de la Marge elle-m&ecirc;me.")

p("Clara, en interrogeant sa propre grand-m&egrave;re "
  "maternelle un dimanche apr&egrave;s-midi, d&eacute;couvre "
  "avec surprise que celle-ci conserve, dans une "
  "vieille malle du grenier, des lettres &eacute;chang&eacute;es "
  "entre ses propres arri&egrave;re-grands-parents durant "
  "l'entre-deux-guerres, une correspondance dont "
  "certains passages, tr&egrave;s discrets, &eacute;voquent "
  "&eacute;galement une mystérieuse &laquo;&nbsp;dette de famille "
  "envers la rivi&egrave;re&nbsp;&raquo; sans jamais s'expliquer "
  "davantage.")

name("GRAND-M&Egrave;RE DE CLARA")
p("&laquo;&nbsp;J'ai jamais vraiment compris ce que &ccedil;a "
  "voulait dire, cette histoire de dette envers la "
  "rivi&egrave;re. Ma propre m&egrave;re en parlait parfois, &agrave; "
  "mots couverts, mais elle a jamais voulu "
  "m'expliquer clairement. J'ai toujours pens&eacute; que "
  "c'&eacute;tait juste une vieille superstition de "
  "famille.&nbsp;&raquo;")

p("Cette d&eacute;couverte, rapport&eacute;e imm&eacute;diatement &agrave; "
  "Darius et Alex, ajoute une pi&egrave;ce suppl&eacute;mentaire "
  "et troublante &agrave; leur compr&eacute;hension grandissante "
  "de l'&eacute;tendue r&eacute;elle de cette l&eacute;gende ancestrale, "
  "sugg&eacute;rant que la famille de Clara elle-m&ecirc;me "
  "pourrait avoir &eacute;t&eacute;, &agrave; un moment de son histoire, "
  "directement li&eacute;e &agrave; la Marge d'une mani&egrave;re "
  "qu'aucun d'eux n'avait jamais soup&ccedil;onn&eacute;e "
  "jusqu'alors.")

p("Clara demande &agrave; sa grand-m&egrave;re la permission "
  "d'emprunter ces vieilles lettres pour les &eacute;tudier "
  "plus attentivement, une requ&ecirc;te accueillie avec "
  "une curiosit&eacute; amus&eacute;e par cette derni&egrave;re, "
  "habitu&eacute;e aux lubies pass&agrave;g&egrave;res de sa "
  "petite-fille mais loin de se douter de "
  "l'importance r&eacute;elle que ces documents pourraient "
  "rev&ecirc;tir pour la compr&eacute;hension d'une histoire "
  "bien plus vaste que ce qu'elle imagine.")

name("GRAND-M&Egrave;RE DE CLARA")
p("&laquo;&nbsp;Prends-les, ma ch&eacute;rie, si &ccedil;a t'int&eacute;resse "
  "tant que &ccedil;a. Moi, ces vieux papiers, &ccedil;a fait des "
  "ann&eacute;es qu'ils prennent la poussi&egrave;re. Contente que "
  "quelqu'un s'y int&eacute;resse enfin dans la famille.&nbsp;&raquo;")

p("Clara rentre chez elle ce soir-l&agrave; avec la "
  "pr&eacute;cieuse liasse de lettres soigneusement rang&eacute;e "
  "dans son sac &agrave; dos, impatiente de les partager "
  "avec Darius et Alex d&egrave;s le lendemain, et passe "
  "une partie de la soir&eacute;e &agrave; les relire seule dans "
  "sa chambre, d&eacute;chiffrant p&eacute;niblement l'&eacute;criture "
  "d&eacute;su&egrave;te de ses arri&egrave;re-grands-parents &agrave; la "
  "lueur de sa lampe de chevet.")

p("Elle d&eacute;couvre, dans l'une des derni&egrave;res lettres "
  "de la liasse, une phrase qui la fait "
  "particuli&egrave;rement frissonner : &laquo;&nbsp;notre fils "
  "a &eacute;t&eacute; d&eacute;sign&eacute;, cette ann&eacute;e, pour porter la "
  "charge. Nous prions pour qu'il en revienne "
  "sain d'esprit, comme son propre p&egrave;re avant "
  "lui.&nbsp;&raquo; Une mention qui sugg&egrave;re, avec une "
  "clart&eacute; troublante, que la famille de Clara "
  "aurait pu, elle aussi, compter parmi ses "
  "anc&ecirc;tres un authentique porteur de la Marge.")

p("Elle s'endort ce soir-l&agrave; l'esprit tourbillonnant "
  "de questions nouvelles, impatiente de partager "
  "cette d&eacute;couverte capitale avec ses deux meilleurs "
  "amis d&egrave;s le lendemain matin, pressentant qu'elle "
  "vient peut-&ecirc;tre de mettre la main sur une pi&egrave;ce "
  "essentielle du puzzle familial et historique "
  "qu'ils tentent, tous les trois, de reconstituer "
  "depuis des mois.")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 2 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 3 -- LE GRIMOIRE ET LE B&Acirc;TON
# ======================================================================
chap(3, "LE GRIMOIRE ET LE B&Acirc;TON")

p("Trois semaines apr&egrave;s la porte blind&eacute;e, Darius se met &agrave; faire "
  "un r&ecirc;ve r&eacute;current, toujours le m&ecirc;me, toujours au m&ecirc;me "
  "endroit : un sous-bois humide, quelque part derri&egrave;re le "
  "coteau des caves oubli&eacute;es, o&ugrave; une racine noueuse &eacute;merge de "
  "terre en formant une forme presque droite, presque taill&eacute;e. "
  "Il se r&eacute;veille chaque fois avec la certitude absurde d'avoir "
  "d&eacute;j&agrave; march&eacute; sur ce chemin pr&eacute;cis, dans une autre vie ou dans "
  "une des six ann&eacute;es qu'on lui a d&eacute;j&agrave; reprises.")

p("Sa m&egrave;re, un matin, le retrouve endormi sur le rebord de la "
  "fen&ecirc;tre ouverte, une couverture roul&eacute;e autour des &eacute;paules, "
  "et lui demande, inqui&egrave;te, s'il refait des cauchemars, "
  "s'il faut reprendre les rendez-vous chez le psychologue plus "
  "s&eacute;rieusement. Darius la rassure du mieux qu'il peut, avec "
  "un mensonge de plus &agrave; ajouter &agrave; la liste, en se disant que "
  "s'il continue &agrave; ce rythme, il finira, lui aussi, par devenir "
  "quelqu'un pour qui mentir ne demande plus aucun effort.")

p("Il essaie, les premi&egrave;res nuits, de r&eacute;sister &agrave; l'envie de "
  "suivre ce r&ecirc;ve pour de vrai, se r&eacute;p&eacute;tant que Kayden a "
  "d&eacute;j&agrave; prouv&eacute; qu'il pouvait le manipuler par le sommeil, et "
  "qu'un r&ecirc;ve r&eacute;current, aussi pr&eacute;cis soit-il, pourrait n'&ecirc;tre "
  "qu'une nouvelle mani&egrave;re de le pousser vers un pi&egrave;ge. Mais "
  "contrairement &agrave; la maison parfaite ou &agrave; la voix dans le "
  "pon&ccedil;on, ce r&ecirc;ve-l&agrave; ne contient aucune promesse, aucune "
  "tentation formul&eacute;e &mdash; juste un chemin, encore et encore, "
  "comme une invitation silencieuse plut&ocirc;t qu'un ordre.")

p("Le quatri&egrave;me matin, un samedi, il ne r&eacute;siste plus. Il prend "
  "son v&eacute;lo sans rien dire &agrave; personne, pas m&ecirc;me &agrave; Clara, "
  "pour la premi&egrave;re fois depuis leur pacte de ne jamais partir "
  "seul, et suit, pas &agrave; pas, l'itin&eacute;raire exact de son r&ecirc;ve &mdash; "
  "le sentier derri&egrave;re le coteau, l'odeur de mousse et de terre "
  "froide, la lumi&egrave;re filtr&eacute;e par les feuillages qui tombe "
  "exactement comme dans son sommeil, en biais, presque "
  "th&eacute;&acirc;trale.")

p("Il trouve la racine au bout d'une demi-heure de marche, "
  "exactement l&agrave; o&ugrave; son r&ecirc;ve la pla&ccedil;ait, sauf que ce n'est pas "
  "une racine. C'est un b&acirc;ton, taill&eacute; dans un bois sombre et "
  "dense, plus lourd qu'il n'en a l'air, d'environ soixante "
  "centim&egrave;tres, dont l'extr&eacute;mit&eacute; sup&eacute;rieure se termine par une "
  "petite spirale grav&eacute;e &agrave; la main, us&eacute;e par le temps mais "
  "encore lisible &agrave; la loupe : les m&ecirc;mes chiffres, quatre, "
  "z&eacute;ro, quatre, ench&acirc;ss&eacute;s dans le motif comme une signature.")

p("Il le ramasse, et sent aussit&ocirc;t, remontant depuis sa paume, "
  "une vibration diff&eacute;rente de tout ce que le pon&ccedil;on lui a fait "
  "ressentir jusqu'ici &mdash; pas une chaleur, pas une envie, mais "
  "quelque chose de plus proche d'une reconnaissance, comme si "
  "l'objet, lui aussi, l'attendait depuis longtemps et n'avait "
  "jamais eu de raison de douter qu'il finirait par venir.")

p("De retour chez lui, il cache le b&acirc;ton sous son lit, entre deux "
  "cartons de vieux jouets, et passe la soir&eacute;e &agrave; chercher, sur "
  "internet, tout ce qu'il peut trouver sur des b&acirc;tons grav&eacute;s "
  "similaires, sans succ&egrave;s, jusqu'&agrave; ce qu'un vieux forum "
  "abandonn&eacute; consacr&eacute; aux l&eacute;gendes locales de Touraine mentionne, "
  "dans un message vieux de douze ans, un &laquo;&nbsp;b&acirc;ton de "
  "sourcier trouv&eacute; pr&egrave;s des caves de Luynes, jamais expliqu&eacute;&nbsp;&raquo;, "
  "post&eacute; par un utilisateur dont le pseudonyme, simplement, "
  "&eacute;tait &laquo;&nbsp;archiviste13&nbsp;&raquo;.")

p("Le lendemain, incapable de tenir sa curiosit&eacute;, il appelle "
  "Clara et Alex pour leur montrer sa trouvaille, un peu honteux "
  "d'avoir bris&eacute; leur promesse mais trop excit&eacute; pour s'en "
  "vraiment vouloir. Il tient le b&acirc;ton devant lui, presque comme "
  "une baguette, sans intention pr&eacute;cise, et le pointe vers la "
  "lampe de bureau &eacute;teinte de sa chambre, en pensant, sans "
  "vraiment y croire, &laquo;&nbsp;allume-toi&nbsp;&raquo;.")

p("L'ampoule grille dans un petit claquement sec, un fil de "
  "fum&eacute;e s'&eacute;chappant du culot, et les trois restent l&agrave;, fig&eacute;s, "
  "&agrave; regarder l'ampoule morte, avant qu'Alex ne se mette &agrave; "
  "rire nerveusement, incapable de dire s'il vient d'assister &agrave; "
  "un miracle ou &agrave; une co&iuml;ncidence particuli&egrave;rement mal "
  "tomb&eacute;e.")

name("ALEX")
p("&laquo;&nbsp;Ok. Ok, ok, ok. Soit c'est une co&iuml;ncidence, soit tu "
  "viens de faire de la magie avec un b&acirc;ton trouv&eacute; dans les "
  "bois, et honn&ecirc;tement, vu notre semaine type ces derniers "
  "temps, je suis pas s&ucirc;r de savoir quelle option me fait le plus "
  "flipper.&nbsp;&raquo;")

p("Alex se penche pour ramasser l'ampoule morte, la retourne "
  "entre ses doigts comme s'il pouvait y lire une explication, "
  "avant de la reposer d&eacute;licatement sur le bureau, presque avec "
  "respect, comme on pose une preuve qu'on ne veut surtout pas "
  "endommager avant qu'un adulte comp&eacute;tent n'ait eu l'occasion "
  "de l'examiner &mdash; sauf qu'aucun adulte, ils le savent tous les "
  "trois d&eacute;sormais, ne pourra jamais &ecirc;tre mis dans la "
  "confidence.")

p("Darius, encore secou&eacute;, s'assoit sur le rebord de son lit et "
  "raconte, pour la premi&egrave;re fois &agrave; voix haute, le r&ecirc;ve "
  "r&eacute;current qui l'a men&eacute; jusqu'&agrave; cette racine, s'attendant &agrave; "
  "ce qu'Alex se moque de lui pour avoir suivi un simple songe "
  "dans les bois &mdash; mais Alex, au contraire, hoche la t&ecirc;te "
  "gravement, et avoue que lui aussi, ces derni&egrave;res semaines, "
  "a fait des r&ecirc;ves &eacute;tranges, plus flous, moins pr&eacute;cis, mais "
  "toujours situ&eacute;s dans la m&ecirc;me for&ecirc;t derri&egrave;re le coteau.")

p("Clara, elle, ne rit pas. Elle prend le b&acirc;ton des mains de "
  "Darius, l'examine sous toutes les coutures, s'arr&ecirc;te sur la "
  "spirale grav&eacute;e, et sort de son sac, presque par r&eacute;flexe, son "
  "&eacute;ternel carnet, pour y noter, dans une nouvelle page, la date "
  "et la description exacte de l'objet, comme elle le fait "
  "toujours quand quelque chose refuse d'entrer dans une "
  "explication raisonnable.")

p("Darius d&eacute;pose le b&acirc;ton sur son bureau, &agrave; c&ocirc;t&eacute; du tiroir o&ugrave; "
  "dort le pon&ccedil;on, et remarque, en les regardant c&ocirc;te &agrave; c&ocirc;te, "
  "&agrave; quel point les deux objets semblent appartenir &agrave; deux "
  "&eacute;poques diff&eacute;rentes de la m&ecirc;me histoire &mdash; l'un moderne, "
  "m&eacute;tallique, presque bureaucratique, l'autre ancien, organique, "
  "comme si M13, au fil des d&eacute;cennies, avait chang&eacute; de "
  "vocabulaire sans jamais changer vraiment de nature.")

name("CLARA")
p("&laquo;&nbsp;Le poin&ccedil;on sert &agrave; marquer les pages. &Ccedil;a, &ccedil;a ressemble "
  "plus &agrave; un outil pour les trouver. Genre, un sourcier, comme "
  "disait ton forum, &ccedil;a cherche l'eau sous la terre. Et si &ccedil;a, &ccedil;a "
  "cherchait autre chose ? Pas de l'eau. Des pages qu'on a "
  "jamais retrouv&eacute;es. Ou des livres entiers.&nbsp;&raquo;")

p("La biblioth&egrave;que municipale de Luynes occupe l'ancien "
  "presbyt&egrave;re, un b&acirc;timent bas en tuffeau juste derri&egrave;re "
  "l'&eacute;glise, o&ugrave; Darius n'a pas remis les pieds depuis un "
  "expos&eacute; de CM2 sur les rois de France. La biblioth&eacute;caire, une "
  "femme d'une soixantaine d'ann&eacute;es pr&eacute;nomm&eacute;e Suzanne, connait "
  "chaque famille du village depuis trois g&eacute;n&eacute;rations et "
  "accueille leur demande &mdash; des l&eacute;gendes locales, des vieux "
  "mythes de la r&eacute;gion, n'importe quoi mentionnant un chiffre "
  "&laquo;&nbsp;treize&nbsp;&raquo; particulier &mdash; avec un enthousiasme "
  "d&eacute;concertant, comme si personne ne lui avait pos&eacute; une "
  "question int&eacute;ressante depuis des ann&eacute;es.")

p("Ils s'installent, tous les trois, &agrave; une table en bois massif "
  "pr&egrave;s de la fen&ecirc;tre, sous le regard bienveillant d'un portrait "
  "jauni du cur&eacute; fondateur de la biblioth&egrave;que, et Clara sort de "
  "son sac deux stylos et une feuille blanche pour prendre des "
  "notes m&eacute;thodiques, comme elle le fait toujours d&egrave;s qu'une "
  "recherche s&eacute;rieuse commence.")

p("Le soleil de fin d'apr&egrave;s-midi traverse les vitraux discrets "
  "de l'ancienne chapelle attenante, projetant des taches de "
  "couleur mouvantes sur les &eacute;tag&egrave;res poussi&eacute;reuses, et Darius "
  "se surprend &agrave; trouver un calme &eacute;trange dans cet endroit, "
  "comme si le simple fait d'&ecirc;tre entour&eacute; de si vieux livres, "
  "de tant d'histoires d&eacute;j&agrave; racont&eacute;es et refermées, rendait sa "
  "propre situation un peu moins seule, un peu moins in&eacute;dite "
  "qu'elle ne lui avait sembl&eacute; jusque-l&agrave;.")

p("Alex, en attendant que Suzanne trouve la cl&eacute; de la salle des "
  "fonds locaux, feuillette distraitement un vieux registre "
  "paroissial expos&eacute; sous vitrine, y d&eacute;couvrant, au passage, le "
  "nom d'un anc&ecirc;tre de sa propre famille n&eacute; en 1889 &agrave; Luynes, "
  "un d&eacute;tail sans rapport avec leur enqu&ecirc;te mais qui lui rappelle, "
  "brutalement, &agrave; quel point chaque famille de ce village porte, "
  "quelque part, une histoire plus longue et plus dense qu'on "
  "ne l'imagine au quotidien.")

p("Clara, en montant les marches vers l'&eacute;tage, chuchote &agrave; "
  "Darius que Suzanne lui a toujours paru &ecirc;tre le genre de "
  "personne &agrave; conna&icirc;tre plus de secrets sur le village que "
  "n'importe quel dossier administratif, simplement parce "
  "qu'elle &eacute;coute vraiment les gens qui viennent lui parler, "
  "contrairement &agrave; la plupart des adultes press&eacute;s qu'ils "
  "croisent d'habitude.")

p("Darius h&eacute;site un instant avant de r&eacute;pondre &agrave; sa question, "
  "conscient de tout ce qu'il faudrait expliquer pour justifier "
  "une telle demande sans para&icirc;tre compl&egrave;tement fou, avant de "
  "trouver une version simplifi&eacute;e, presque vraie : un projet "
  "d'expos&eacute; sur les l&eacute;gendes locales, pour le coll&egrave;ge, sur "
  "&laquo;&nbsp;des trucs bizarres autour du chiffre treize dans la "
  "r&eacute;gion&nbsp;&raquo;. Suzanne accepte l'explication sans poser plus de "
  "questions, visiblement ravie que des adolescents s'int&eacute;ressent "
  "encore, de nos jours, &agrave; autre chose qu'&agrave; leurs t&eacute;l&eacute;phones.")

p("Elle les guide vers une salle &agrave; l'&eacute;tage, r&eacute;serv&eacute;e aux fonds "
  "locaux, o&ugrave; s'entassent des recueils de contes tourangeaux "
  "reli&eacute;s en cuir craquel&eacute;, des monographies communales "
  "&eacute;dit&eacute;es &agrave; compte d'auteur, et un exemplaire unique, "
  "manuscrit, jamais publi&eacute;, intitul&eacute; &laquo;&nbsp;L&eacute;gendes et Croyances "
  "du Coteau &mdash; recueillies aupr&egrave;s des anciens, 1962&nbsp;&raquo;, dont "
  "les pages jaunies craquent sous les doigts de Clara quand "
  "elle l'ouvre avec pr&eacute;caution.")

p("Avant d'arriver &agrave; ce chapitre, ils passent une heure enti&egrave;re &agrave; "
  "feuilleter des recueils moins prometteurs &mdash; des contes de "
  "loups-garous typiques de la r&eacute;gion, des histoires de fant&ocirc;mes "
  "de ch&acirc;teaux voisins, rien qui ne colle vraiment &agrave; ce qu'ils "
  "cherchent &mdash; jusqu'&agrave; ce qu'Alex, presque par hasard, "
  "remarque un ouvrage plus fin, glissé entre deux volumes "
  "beaucoup plus &eacute;pais, dont la tranche ne porte aucun titre "
  "visible, seulement une date grav&eacute;e au fer : 1962.")

p("Ils tombent, apr&egrave;s une heure de lecture silencieuse, sur un "
  "chapitre entier consacr&eacute; &agrave; ce que l'auteur appelle &laquo;&nbsp;le mal "
  "aux treize pages&nbsp;&raquo;, une croyance ancienne racont&eacute;e de "
  "g&eacute;n&eacute;ration en g&eacute;n&eacute;ration selon laquelle un esprit gardien du "
  "coteau, appel&eacute; simplement &laquo;&nbsp;M treize&nbsp;&raquo;, accepterait "
  "d'&eacute;changer les souvenirs douloureux d'un villageois contre "
  "une ann&eacute;e de sa vie, &agrave; condition qu'un &laquo;&nbsp;porteur&nbsp;&raquo; se "
  "pr&eacute;sente pour parler en son nom.")

p("Le nom de ce porteur, r&eacute;p&eacute;t&eacute; dans trois r&eacute;cits diff&eacute;rents, "
  "espac&eacute;s de plusieurs g&eacute;n&eacute;rations selon les dates estim&eacute;es par "
  "l'auteur, est toujours le m&ecirc;me : Darius. Un Darius laboureur "
  "au dix-huiti&egrave;me si&egrave;cle, cens&eacute; avoir sauv&eacute; le village d'une "
  "&eacute;pid&eacute;mie en &laquo;&nbsp;rendant au coteau ce qu'on lui avait "
  "vol&eacute;&nbsp;&raquo;. Un autre Darius, meunier, en 1871, qui aurait "
  "disparu trois jours avant de revenir &laquo;&nbsp;chang&eacute;, mais "
  "reconnaissable&nbsp;&raquo;. Un troisi&egrave;me, simplement d&eacute;sign&eacute; comme "
  "&laquo;&nbsp;le jeune Darius&nbsp;&raquo;, dans un r&eacute;cit non dat&eacute; recueilli "
  "aupr&egrave;s d'une centenaire en 1962, qui aurait &laquo;&nbsp;parl&eacute; au "
  "coteau avec un b&acirc;ton de noisetier, et le coteau lui avait "
  "r&eacute;pondu&nbsp;&raquo;.")

p("Darius referme le livre, les mains tremblantes, incapable "
  "pendant un long moment de prononcer un seul mot. Ce n'est "
  "pas juste une co&iuml;ncidence de pr&eacute;nom, dans une petite ville "
  "o&ugrave; ce pr&eacute;nom n'est m&ecirc;me pas particuli&egrave;rement r&eacute;pandu. C'est "
  "un r&ocirc;le, transmis, r&eacute;p&eacute;t&eacute; de si&egrave;cle en si&egrave;cle, comme si le "
  "syst&egrave;me &mdash; ou l'entit&eacute; qu'il &eacute;tait devenu, ou avait toujours "
  "&eacute;t&eacute;, bien avant Kayden Vasseur et son programme des "
  "ann&eacute;es quatre-vingt-dix &mdash; choisissait toujours, "
  "inlassablement, un porte-parole portant le m&ecirc;me nom.")

p("Alex, penchant la t&ecirc;te au-dessus de l'&eacute;paule de Darius pour "
  "relire le passage une troisi&egrave;me fois, remarque quelque chose "
  "que les deux autres avaient laiss&eacute; passer &mdash; qu'aucun des "
  "trois r&eacute;cits ne pr&eacute;cise jamais le nom de famille de ce "
  "&laquo;&nbsp;Darius&nbsp;&raquo;, comme si le pr&eacute;nom seul suffisait toujours &agrave; "
  "identifier, sans doute possible, la bonne personne au bon "
  "moment, ind&eacute;pendamment du si&egrave;cle o&ugrave; elle na&icirc;t.")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a veut dire que le programme de 1991, c'&eacute;tait pas le "
  "d&eacute;but. C'&eacute;tait juste la premi&egrave;re fois qu'on a mis un nom "
  "scientifique dessus. Le vrai &laquo;&nbsp;M13&nbsp;&raquo;, il &eacute;tait d&eacute;j&agrave; l&agrave; "
  "avant, sous le coteau, depuis des si&egrave;cles, et Vasseur a "
  "juste... branch&eacute; des ordinateurs sur un truc qui existait "
  "d&eacute;j&agrave;.&nbsp;&raquo;")

p("Suzanne, en apportant du th&eacute; qu'aucun des trois n'a demand&eacute;, "
  "remarque, presque en passant, qu'elle se souvient vaguement "
  "d'un vieux registre manuscrit, laiss&eacute; en d&eacute;p&ocirc;t par une "
  "famille du village il y a des ann&eacute;es, que personne n'a jamais "
  "pris la peine de cataloguer s&eacute;rieusement parce que tout le "
  "monde le prenait pour un canular, un jeu invent&eacute; par des "
  "enfants d'une autre &eacute;poque. &laquo;&nbsp;Il doit encore &ecirc;tre dans la "
  "r&eacute;serve, si &ccedil;a vous int&eacute;resse. Personne ne l'a jamais "
  "emprunt&eacute;.&nbsp;&raquo;")

p("La r&eacute;serve de la biblioth&egrave;que n'est qu'une ancienne cave "
  "vo&ucirc;t&eacute;e am&eacute;nag&eacute;e en d&eacute;barras, humide, mal &eacute;clair&eacute;e par une "
  "seule ampoule nue pendue au plafond, dont Darius &eacute;vite "
  "soigneusement de s'approcher trop pr&egrave;s depuis l'incident de "
  "la veille. Suzanne fouille une &eacute;tag&egrave;re du fond, marmonnant "
  "des noms de familles qu'elle associe &agrave; des cartons pr&eacute;cis, "
  "avant de tirer, avec un petit cri de victoire, un ouvrage "
  "&eacute;pais reli&eacute; de cuir noir, sans titre visible sur la couverture, "
  "us&eacute; aux coins comme s'il avait &eacute;t&eacute; manipul&eacute; des centaines "
  "de fois.")

p("&laquo;&nbsp;On l'appelait le grimoire des farces, dit-elle en le "
  "posant sur la table avec pr&eacute;caution malgr&eacute; le ton l&eacute;ger de "
  "sa phrase. Dans les ann&eacute;es soixante-dix, les enfants du "
  "village s'en servaient pour se faire peur entre eux, autour "
  "d'un feu de camp, en lisant des formules dedans en pr&eacute;tendant "
  "que &ccedil;a marchait. Personne n'a jamais rien vu se passer, bien "
  "s&ucirc;r. C'est juste un vieux carnet de blagues.&nbsp;&raquo;")

p("Alex, dubitatif, feuillette d'abord les premi&egrave;res pages "
  "lui-m&ecirc;me, s'attendant &agrave; y trouver des dessins d'enfants, des "
  "blagues potaches, le genre de contenu qu'on imagine dans un "
  "carnet cens&eacute; effrayer des adolescents autour d'un feu de "
  "camp &mdash; et son sourire s'efface lentement &agrave; mesure qu'il "
  "tourne les pages, comprenant, comme Darius avant lui, que ce "
  "livre n'a jamais &eacute;t&eacute; con&ccedil;u pour faire rire qui que ce soit.")

p("Darius l'ouvre &agrave; la premi&egrave;re page. L'&eacute;criture, ronde et "
  "appliqu&eacute;e, lui est imm&eacute;diatement familière &mdash; la m&ecirc;me que "
  "sur l'&eacute;tiquette du collier, la m&ecirc;me que sur la note manuscrite "
  "de K. Vasseur retrouv&eacute;e dans l'entrep&ocirc;t. Ce n'est pas un "
  "carnet de blagues d'adolescents. C'est un registre de "
  "protocoles, d&eacute;guis&eacute; en jeu depuis d&eacute;cennies pour que "
  "personne, jamais, ne le prenne au s&eacute;rieux &mdash; la meilleure "
  "des cachettes, comprend Darius, &eacute;tant celle que tout le monde "
  "regarde sans y croire.")

p("Clara feuillette prudemment le reste du grimoire pendant que "
  "Darius examine la page du rituel, tombant sur des dizaines "
  "d'autres protocoles d&eacute;guis&eacute;s en jeux d'enfants &mdash; &laquo;&nbsp;le sort "
  "du miroir qui ment&nbsp;&raquo;, &laquo;&nbsp;la comptine pour retrouver ce "
  "qu'on a perdu&nbsp;&raquo;, chacun accompagn&eacute; d'un petit dessin naïf "
  "qui, en y regardant de plus pr&egrave;s, correspond &eacute;trangement &agrave; "
  "des sch&eacute;mas techniques simplifi&eacute;s, comme si quelqu'un avait "
  "d&eacute;lib&eacute;r&eacute;ment habill&eacute; la science en superstition pour la "
  "transmettre sans &eacute;veiller de soup&ccedil;ons.")

p("Une page, vers le milieu, d&eacute;crit pr&eacute;cis&eacute;ment un rituel appel&eacute; "
  "&laquo;&nbsp;ouverture de rayon&nbsp;&raquo;, accompagn&eacute; d'un sch&eacute;ma repr&eacute;sentant "
  "un b&acirc;ton point&eacute; vers une rang&eacute;e d'objets align&eacute;s, cens&eacute; "
  "r&eacute;v&eacute;ler, parmi eux, celui qui &laquo;&nbsp;contient une page qu'on "
  "cherche&nbsp;&raquo;. Sans r&eacute;fl&eacute;chir, sans vraiment mesurer la port&eacute;e "
  "de son geste dans une pi&egrave;ce aussi &eacute;troite, Darius sort le "
  "b&acirc;ton de son sac, le pointe vers l'&eacute;tag&egrave;re du fond, charg&eacute;e "
  "de vieux dossiers communaux, et prononce, &agrave; voix basse, la "
  "formule &eacute;crite dans le grimoire.")

p("L'&eacute;tag&egrave;re enti&egrave;re bascule vers l'avant dans un fracas "
  "&eacute;pouvantable, projetant des classeurs et des liasses de "
  "papiers dans toute la pi&egrave;ce, tandis qu'une seule feuille, "
  "isol&eacute;e, arrach&eacute;e d'un dossier vieux de quarante ans, vole "
  "jusqu'&agrave; atterrir, pos&eacute;e bien &agrave; plat, aux pieds de Darius, "
  "comme d&eacute;pos&eacute;e l&agrave; expr&egrave;s par une main invisible.")

p("Suzanne pousse un cri, se pr&eacute;cipite pour v&eacute;rifier que personne "
  "n'est bless&eacute;, tandis que Clara et Alex restent fig&eacute;s, les yeux "
  "&eacute;carquill&eacute;s, incapables de dire un mot. Darius, lui, ramasse "
  "lentement la feuille vol&eacute;e, et lit, imprim&eacute; en haut de page, "
  "un en-t&ecirc;te administratif d&eacute;pass&eacute; : &laquo;&nbsp;MAIRIE DE LUYNES &mdash; "
  "REGISTRE DES DISPARITIONS NON EXPLIQU&Eacute;ES &mdash; ANN&Eacute;ES 1985 &mdash; "
  "1995&nbsp;&raquo;, et, sous cet en-t&ecirc;te, une liste de noms qu'il "
  "reconna&icirc;t immediatement pour en avoir d&eacute;j&agrave; crois&eacute; un, tout en "
  "bas de la page, encadr&eacute; au stylo rouge par une main "
  "anonyme : Kayden Vasseur.")

p("Suzanne, encore essouffl&eacute;e d'avoir couru relever les classeurs "
  "tomb&eacute;s, s'approche &agrave; son tour et lit le nom par-dessus "
  "l'&eacute;paule de Darius, p&acirc;lissant visiblement. &laquo;&nbsp;Vasseur... j'ai "
  "connu une famille Vasseur, autrefois, dit-elle d'une voix "
  "hesitante. Le p&egrave;re travaillait &agrave; un centre de recherche, "
  "vers Fondettes. Ils ont quitt&eacute; la r&eacute;gion apr&egrave;s la disparition "
  "de leur fils, en 94. Personne n'en a plus jamais entendu "
  "parler.&nbsp;&raquo;")

p("Alex propose, sur le chemin du retour, qu'ils passent tous "
  "les trois par le b&acirc;timent de l'entrep&ocirc;t pour comparer "
  "l'&eacute;criture du grimoire &agrave; celle du dossier de Franck, une "
  "id&eacute;e que Darius accueille avec un mélange d'excitation et de "
  "lassitude, sentant qu'aucune de ces d&eacute;couvertes ne fera "
  "jamais que reculer encore un peu plus loin la limite de ce "
  "qu'il pensait pouvoir un jour comprendre enti&egrave;rement.")

p("Ils marchent en silence pendant plusieurs minutes, chacun "
  "perdu dans ses propres calculs, avant que Clara ne finisse "
  "par formuler, &agrave; voix haute, la question qui les hante tous "
  "les trois depuis la biblioth&egrave;que&nbsp;: si un Darius diff&eacute;rent "
  "s'est pr&eacute;sent&eacute; &agrave; chaque g&eacute;n&eacute;ration depuis des si&egrave;cles, "
  "qu'est-il arriv&eacute;, exactement, &agrave; tous les Darius pr&eacute;c&eacute;dents "
  "une fois leur r&ocirc;le termin&eacute; &mdash; et personne, sur le chemin "
  "du retour, ne trouve le courage de proposer une r&eacute;ponse.")

p("Darius, encore tremblant, range le b&acirc;ton dans son sac avec "
  "des gestes lents, presque c&eacute;r&eacute;monieux, mesurant pour la "
  "premi&egrave;re fois &agrave; quel point cet objet trouv&eacute; dans les bois "
  "poss&egrave;de une force bien plus directe, bien plus imm&eacute;diate, "
  "que tout ce que le pon&ccedil;on lui avait fait ressentir jusqu'ici "
  "&mdash; une diff&eacute;rence qui l'inqui&egrave;te presque plus que le "
  "pouvoir lui-m&ecirc;me.")

p("Clara aide Suzanne &agrave; ranger le dernier classeur tomb&eacute;, "
  "s'excusant platement pour le d&eacute;g&acirc;t, sans pouvoir expliquer, "
  "&eacute;videmment, la vraie cause de cette chute, tandis que "
  "Suzanne, encore un peu p&acirc;le, r&eacute;p&egrave;te qu'elle n'a jamais vu "
  "une &eacute;tag&egrave;re basculer aussi brutalement sans qu'on l'ait "
  "pouss&eacute;e, en trente ans de m&eacute;tier.")

p("Alex, avant de partir, demande &agrave; Suzanne si elle se souvient "
  "d'autre chose sur cette famille Vasseur, un d&eacute;tail, une "
  "adresse, n'importe quoi, mais elle secoue la t&ecirc;te, d&eacute;sol&eacute;e, "
  "expliquant que c'&eacute;tait il y a si longtemps qu'elle-m&ecirc;me "
  "&eacute;tait encore une jeune biblioth&eacute;caire &agrave; l'&eacute;poque, et que la "
  "m&eacute;moire d'un village, comme celle d'une personne, finit "
  "toujours, avec le temps, par se contenter des versions les "
  "plus simples des choses.")

p("Darius replie soigneusement la feuille, la glisse dans sa "
  "poche &agrave; c&ocirc;t&eacute; du dossier de son p&egrave;re et du grimoire qu'il "
  "n'a d&eacute;j&agrave; plus tout &agrave; fait envie de reposer, tandis que "
  "Clara et Alex commencent, en silence, &agrave; redresser les "
  "classeurs renvers&eacute;s, sans qu'aucun des trois ne prononce un "
  "mot de plus avant de quitter la biblioth&egrave;que, chacun sachant "
  "d&eacute;j&agrave; qu'ils viennent de franchir une porte qu'il sera "
  "impossible de refermer.")

p("Sur le chemin du retour de la biblioth&egrave;que, Darius n'avait "
  "presque pas parl&eacute;, contrairement &agrave; son habitude, trop "
  "occup&eacute; &agrave; retourner dans sa t&ecirc;te l'id&eacute;e que l'informatique, "
  "son propre domaine, celui o&ugrave; il se sentait toujours le plus "
  "&agrave; l'aise des trois, pourrait devenir la prochaine porte "
  "d'entr&eacute;e de Kayden dans leur vie. Il s'&eacute;tait promis, en "
  "silence, de ne surtout rien dire &agrave; Clara ni &agrave; Alex de "
  "cette inqui&eacute;tude, pour ne pas para&icirc;tre plus effray&eacute; que ses "
  "deux amis, avant de se retrouver, une heure plus tard, seul "
  "devant son &eacute;cran, &agrave; faire exactement ce qu'il redoutait le "
  "plus.")

p("Il avait promis &agrave; sa m&egrave;re, en rentrant de la biblioth&egrave;que, "
  "de faire ses devoirs de math avant le d&icirc;ner, un exercice sur "
  "les probabilit&eacute;s qu'il regarde maintenant sans le voir "
  "vraiment, l'esprit encore accroch&eacute; &agrave; cette &eacute;tag&egrave;re renvers&eacute;e "
  "et &agrave; ce nom encercl&eacute; de rouge. Il ouvre son ordinateur "
  "portable plus par r&eacute;flexe que par v&eacute;ritable intention de "
  "travailler, laissant le cahier de maths ferm&eacute; &agrave; c&ocirc;t&eacute; du "
  "clavier.")

p("De retour chez lui, Darius transf&egrave;re les photos du registre des "
  "disparitions sur son ordinateur, dans un dossier qu'il nomme, "
  "avec un humour un peu forc&eacute;, &laquo;&nbsp;devoirs de vacances&nbsp;&raquo;, avant "
  "de se lancer, port&eacute; par une curiosit&eacute; qu'il ne contr&ocirc;le plus "
  "vraiment, dans une recherche syst&eacute;matique de tout ce qui "
  "existe en ligne sur Kayden Vasseur &mdash; forums oubli&eacute;s, "
  "annuaires scolaires num&eacute;ris&eacute;s, archives de presse locale "
  "microfilm&eacute;es puis scann&eacute;es par une association d'histoire "
  "r&eacute;gionale.")

p("Sa m&egrave;re passe la t&ecirc;te par la porte entrouverte, lui demande "
  "s'il a bient&ocirc;t fini ses devoirs, et Darius, sans lever les yeux "
  "de l'&eacute;cran, murmure un &laquo;&nbsp;presque&nbsp;&raquo; qui n'engage &agrave; rien, "
  "conscient qu'expliquer ce qu'il fait vraiment demanderait "
  "des heures qu'il n'a pas et des mots qu'il n'a pas encore "
  "trouv&eacute;s.")

p("Il commence par les canaux &eacute;vidents &mdash; r&eacute;seaux sociaux, "
  "pages blanches, annuaires d'anciens &eacute;l&egrave;ves &mdash; sans trouver "
  "trace d'aucun Vasseur &agrave; moins de cinquante kilom&egrave;tres de "
  "Luynes, comme si toute la famille s'&eacute;tait volatilis&eacute;e d'un "
  "coup, sans laisser la moindre adresse de suivi. Il &eacute;largit "
  "sa recherche aux archives d&eacute;partementales num&eacute;ris&eacute;es, "
  "tapant patiemment des combinaisons de mots-cl&eacute;s diff&eacute;rentes "
  "&mdash; &laquo;&nbsp;centre recherche Fondettes 1994&nbsp;&raquo;, &laquo;&nbsp;programme "
  "m&eacute;moire minist&egrave;re abandonn&eacute;&nbsp;&raquo; &mdash; avec la t&eacute;nacit&eacute; d'un "
  "&eacute;l&egrave;ve qui refuse un devoir mal not&eacute;.")

p("Il trouve, apr&egrave;s une heure, un unique article, trois "
  "paragraphes, publi&eacute; dans un bulletin municipal de 1994, "
  "titr&eacute; &laquo;&nbsp;Un jeune chercheur port&eacute; disparu &mdash; la famille "
  "lance un appel&nbsp;&raquo;, accompagn&eacute; d'une photo grain&eacute;e qu'il "
  "reconna&icirc;t imm&eacute;diatement : le m&ecirc;me sourire que sur la photo "
  "de foot, le m&ecirc;me visage encore intact, avant tout ce que "
  "Kayden est devenu depuis.")

p("Il envoie l'article &agrave; Alex et Clara, avec un simple "
  "&laquo;&nbsp;regardez &ccedil;a&nbsp;&raquo;, avant de zoomer sur la photo grain&eacute;e "
  "pour en examiner chaque d&eacute;tail &mdash; le sourire, le col de la "
  "chemise, un badge visiteur mal agraf&eacute; au revers de la veste "
  "&mdash; avec la m&eacute;ticulosit&eacute; d'un enqu&ecirc;teur, comme s'il pouvait, "
  "en regardant assez fort, faire dire &agrave; cette image des choses "
  "qu'elle n'a jamais eu l'intention de r&eacute;v&eacute;ler.")

p("C'est en voulant enregistrer une capture d'&eacute;cran de l'article "
  "que son curseur, sans qu'il y touche, se met &agrave; glisser tout "
  "seul vers le coin de l'&eacute;cran, ouvre de lui-m&ecirc;me le terminal de "
  "commande, une fen&ecirc;tre noire que Darius n'utilise presque jamais, "
  "et commence &agrave; taper, ligne apr&egrave;s ligne, &agrave; une vitesse "
  "impossible pour des doigts humains, une s&eacute;rie de caract&egrave;res "
  "qu'il ne comprend pas.")

p("Sa petite s&oelig;ur, dans la chambre voisine, tape contre le "
  "mur en lui criant de baisser le son de son jeu, n'ayant "
  "aucune id&eacute;e de ce qui se joue r&eacute;ellement de l'autre c&ocirc;t&eacute; de "
  "la cloison, et cette normalit&eacute; absurde, presque comique, "
  "rend la panique de Darius encore plus vertigineuse.")

name("DARIUS")
p("&laquo;&nbsp;Non non non non non. D&eacute;branche. D&Eacute;BRANCHE.&nbsp;&raquo;")

p("Les lignes de code d&eacute;filent trop vite pour qu'il en comprenne "
  "le sens, des fen&ecirc;tres s'ouvrant et se refermant en cascade, "
  "des dossiers entiers de son disque dur d&eacute;filant dans "
  "l'explorateur de fichiers comme si une main invisible "
  "&eacute;pluchait m&eacute;thodiquement chaque recoin de sa vie num&eacute;rique "
  "&mdash; ses photos, ses conversations, ses recherches r&eacute;centes sur "
  "Vasseur &mdash; avec une curiosit&eacute; froide, presque clinique.")

p("Il arrache le c&acirc;ble d'alimentation d'un geste brusque, "
  "l'&eacute;cran mourant dans un flash blanc, mais pas assez vite pour "
  "qu'il n'ait pas eu le temps de voir, sur la derni&egrave;re ligne "
  "avant que tout ne s'&eacute;teigne, une phrase compl&egrave;te se former "
  "toute seule, lettre par lettre, avec ces m&ecirc;mes petites pauses "
  "irr&eacute;guli&egrave;res qu'il conna&icirc;t maintenant trop bien : &laquo;&nbsp;TU "
  "M'AS CHERCH&Eacute;. ME VOIL&Agrave;.&nbsp;&raquo;")

p("Il envoie un message &agrave; Alex et Clara, les mains encore "
  "tremblantes, se contentant d'&eacute;crire &laquo;&nbsp;appelez-moi d&egrave;s que "
  "vous voyez &ccedil;a, urgent&nbsp;&raquo;, avant de r&eacute;aliser, une seconde "
  "trop tard, l'ironie amère d'envoyer un message num&eacute;rique "
  "pour signaler que les appareils num&eacute;riques ne sont plus "
  "s&ucirc;rs &mdash; et de se demander, la gorge serr&eacute;e, si ce message "
  "l&agrave; aussi, quelque part, est d&eacute;j&agrave; en train d'&ecirc;tre lu par "
  "quelqu'un d'autre que ses deux destinataires.")

p("Il reste assis par terre, dos contre son lit, l'ordinateur "
  "&eacute;teint pos&eacute; devant lui comme un animal qui pourrait mordre "
  "&agrave; nouveau, jusqu'&agrave; ce que sa m&egrave;re l'appelle pour d&icirc;ner, "
  "d'une voix parfaitement ordinaire, et qu'il descende, les "
  "jambes flageolantes, en se demandant comment il va bien "
  "pouvoir avaler quoi que ce soit ce soir-l&agrave;.")

p("Le lendemain, au coll&egrave;ge, Darius raconte tout &agrave; Clara et "
  "Alex pendant la pause d&eacute;jeuner, &agrave; voix basse, les trois "
  "serr&eacute;s dans un coin de la cour loin des autres &eacute;l&egrave;ves. "
  "Personne ne trouve les mots pour commenter vraiment ce que "
  "&ccedil;a signifie, et ils finissent le repas en silence, chacun "
  "perdu dans le m&ecirc;me calcul silencieux : si Kayden peut "
  "d&eacute;sormais atteindre un ordinateur, alors aucun appareil, "
  "aucune connexion, ne peut plus &ecirc;tre consid&eacute;r&eacute;e comme "
  "totalement s&ucirc;re.")

name("CLARA")
p("&laquo;&nbsp;On savait d&eacute;j&agrave; que la machine touchait aux "
  "souvenirs, au sommeil, &agrave; tout ce qui est fragile chez "
  "quelqu'un. Mais un ordinateur, c'est diff&eacute;rent. C'est du "
  "concret, du c&acirc;ble, de l'&eacute;lectricit&eacute;. Si &ccedil;a marche l&agrave;-dessus "
  "aussi, &ccedil;a veut dire qu'il y a plus vraiment de fronti&egrave;re "
  "entre son monde &agrave; lui et le n&ocirc;tre.&nbsp;&raquo;")

p("Darius hoche la t&ecirc;te, encore secou&eacute; malgr&eacute; la nuit de "
  "sommeil, et sort de son sac un vieux carnet de brouillon "
  "qu'il vient de d&eacute;cider, sur un coup de t&ecirc;te, de r&eacute;server "
  "d&eacute;sormais &agrave; toutes leurs recherches sensibles &mdash; papier "
  "uniquement, aucun &eacute;cran, aucune trace num&eacute;rique susceptible "
  "d'&ecirc;tre lue par quelqu'un d'autre qu'eux trois.")

p("Clara, elle, passe une partie de la nuit &eacute;veill&eacute;e &agrave; relire "
  "le message de Darius re&ccedil;u la veille, cherchant &agrave; se rassurer "
  "en se disant qu'un simple &laquo;&nbsp;appelez-moi&nbsp;&raquo; n'a rien "
  "d'anormal en soi, avant de se souvenir, avec un frisson, "
  "qu'ils viennent tout juste de d&eacute;couvrir &agrave; quel point rien, "
  "d&eacute;sormais, n'a plus de raison d'&ecirc;tre pris pour argent "
  "comptant.")

p("La nuit qui suit l'incident de l'ordinateur, personne ne dort "
  "vraiment bien. Darius se r&eacute;veille trois fois, chaque fois "
  "persuad&eacute; d'avoir entendu son propre t&eacute;l&eacute;phone vibrer sur la "
  "table de nuit, avant de constater, chaque fois, que l'&eacute;cran "
  "reste noir et silencieux, ce qui ne le rassure qu'&agrave; moiti&eacute;.")

p("Le lendemain matin, Clara re&ccedil;oit sur son t&eacute;l&eacute;phone un "
  "message qui semble venir de Darius, dans leur conversation "
  "habituelle, avec sa photo de profil, son num&eacute;ro, tout &agrave; fait "
  "normal en apparence, sauf le contenu : &laquo;&nbsp;J'ai trouv&eacute; un "
  "moyen de tout r&eacute;gler sans risque. Retrouve-moi seule &agrave; "
  "l'entrep&ocirc;t ce soir, dis rien &agrave; Alex, j'expliquerai apr&egrave;s.&nbsp;&raquo;")

p("Elle repense, en fixant l'&eacute;cran, &agrave; toutes les fois o&ugrave; elle "
  "a vu des adultes se faire pi&eacute;ger par de faux messages "
  "urgents, des arnaques bien ficel&eacute;es qui jouaient sur la "
  "panique pour emp&ecirc;cher toute r&eacute;flexion, et se force, "
  "d&eacute;lib&eacute;r&eacute;ment, &agrave; ralentir sa respiration avant de r&eacute;pondre "
  "quoi que ce soit.")

p("Le message, en le relisant une seconde fois, contient aussi "
  "une petite faute d'accord que Darius ne fait jamais &mdash; "
  "&laquo;&nbsp;j'ai trouv&eacute;&nbsp;&raquo; sans le &laquo;&nbsp;e&nbsp;&raquo; de politesse qu'il ajoute "
  "toujours par habitude scolaire &mdash; un d&eacute;tail si minuscule "
  "que Clara elle-m&ecirc;me met plusieurs secondes &agrave; comprendre "
  "pourquoi il lui semble aussi &eacute;trange.")

p("Elle manque de r&eacute;pondre imm&eacute;diatement &laquo;&nbsp;j'arrive&nbsp;&raquo;, le "
  "pouce d&eacute;j&agrave; suspendu au-dessus de l'&eacute;cran, avant qu'un "
  "d&eacute;tail, minuscule, ne l'arr&ecirc;te : Darius, le vrai, ne "
  "l'appelle jamais &laquo;&nbsp;seule&nbsp;&raquo;, et n'a jamais, pas une seule "
  "fois depuis la grotte, propos&eacute; qu'ils se s&eacute;parent pour "
  "affronter quoi que ce soit li&eacute; &agrave; M13.")

p("Elle relit le message une troisi&egrave;me fois, cherchant d'autres "
  "d&eacute;tails suspects, et remarque cette fois que l'heure d'envoi "
  "indique trois heures dix-sept du matin, un cr&eacute;neau o&ugrave; "
  "Darius, elle le sait, dort toujours profond&eacute;ment, ayant "
  "d&eacute;j&agrave; plaisant&eacute; plusieurs fois sur le fait que rien au "
  "monde n'arrive &agrave; le r&eacute;veiller avant son alarme habituelle.")

p("Elle appelle Darius directement, en vrai, la voix tremblante, "
  "et il lui confirme, en quelques secondes, qu'il n'a jamais "
  "envoy&eacute; ce message, qu'il dort encore quand elle l'appelle, "
  "chez lui, dans son lit, &agrave; des kilom&egrave;tres de tout entrep&ocirc;t.")

name("CLARA")
p("&laquo;&nbsp;Il essaie de nous s&eacute;parer. D'abord ton ordinateur, Darius, "
  "maintenant mon t&eacute;l&eacute;phone. Il apprend &agrave; se glisser partout "
  "o&ugrave; il y a un &eacute;cran, comme s'il &eacute;tait plus fort dans nos "
  "objets que dans le monde r&eacute;el.&nbsp;&raquo;")

name("DARIUS")
p("&laquo;&nbsp;Je suis d&eacute;sol&eacute;. C'est ma faute, j'aurais jamais d&ucirc; "
  "chercher son nom en ligne. J'ai ouvert une porte que je "
  "savais m&ecirc;me pas exister.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;T'as rien fait de mal. On savait tous qu'on prenait des "
  "risques d&egrave;s le premier soir devant cette vitrine. On peut "
  "pas commencer &agrave; se blamer maintenant, sinon on n'avance "
  "plus jamais.&nbsp;&raquo;")

p("Ils se retrouvent tous les trois chez Clara, en urgence, "
  "t&eacute;l&eacute;phones &eacute;teints pos&eacute;s au fond d'un tiroir, comme si "
  "&eacute;teindre un &eacute;cran suffisait &agrave; fermer une porte. Darius, "
  "encore secou&eacute; par son ordinateur grill&eacute;, propose une "
  "hypoth&egrave;se qui leur glace tous le sang : et si Kayden, en "
  "possédant Darius dans la grotte, avait appris, au passage, "
  "assez de choses sur eux trois &mdash; leurs habitudes, leurs "
  "mots de passe, leur fa&ccedil;on de s'&eacute;crire &mdash; pour continuer &agrave; "
  "les manipuler m&ecirc;me apr&egrave;s &ecirc;tre reparti&nbsp;?")

p("Ils passent ensuite un long moment &agrave; comparer, sur une "
  "feuille de papier plut&ocirc;t que sur un &eacute;cran, tout ce qui a "
  "pu servir de porte d'entr&eacute;e &agrave; Kayden jusqu'ici &mdash; le sommeil "
  "de Darius, son ordinateur, le t&eacute;l&eacute;phone de Clara &mdash; "
  "cherchant un point commun qui pourrait leur donner un "
  "semblant de contr&ocirc;le, sans jamais vraiment le trouver, "
  "sinon la conclusion inqui&eacute;tante que n'importe quel moment "
  "de faiblesse ou de distraction semble suffire.")

name("ALEX")
p("&laquo;&nbsp;Peut-&ecirc;tre qu'on r&eacute;fl&eacute;chit &agrave; l'envers. Au lieu de "
  "chercher comment il rentre, on devrait chercher pourquoi "
  "il a besoin de rentrer du tout. S'il &eacute;tait vraiment "
  "tout-puissant, il aurait pas besoin de messages truqu&eacute;s ou "
  "de curseurs qui bougent tout seuls. &Ccedil;a veut dire qu'il "
  "est limit&eacute;, quelque part. Qu'il a besoin de nous pour "
  "faire le dernier pas.&nbsp;&raquo;")

p("Cette id&eacute;e reste suspendue entre eux un moment, ni "
  "rassurante ni vraiment inqui&eacute;tante, juste nouvelle, une "
  "pi&egrave;ce suppl&eacute;mentaire d'un puzzle dont ils commencent &agrave; "
  "peine &agrave; deviner la forme g&eacute;n&eacute;rale.")

p("Darius, en &eacute;coutant l'hypoth&egrave;se d'Alex, repense &agrave; la "
  "petite lumi&egrave;re bleue qui palpite encore, parfois, derri&egrave;re "
  "ses propres paupi&egrave;res, et se demande, avec un frisson "
  "nouveau, si Kayden n'a pas simplement besoin de lui, "
  "directement, pour continuer &agrave; op&eacute;rer &agrave; travers ces "
  "&eacute;crans &mdash; une pens&eacute;e qu'il garde pour lui, incapable "
  "d'affronter, ce soir-l&agrave;, l'id&eacute;e qu'il pourrait &ecirc;tre, "
  "malgr&eacute; lui, le point d'entr&eacute;e de tout ce chaos.")

p("Clara propose, avant de se s&eacute;parer ce soir-l&agrave;, une nouvelle "
  "r&egrave;gle &agrave; ajouter &agrave; celles d&eacute;j&agrave; &eacute;tablies&nbsp;: ne jamais "
  "faire confiance &agrave; un message, m&ecirc;me venant d'un num&eacute;ro "
  "connu, sans une phrase de code convenue &agrave; l'avance, "
  "quelque chose d'assez personnel pour qu'aucune imitation, "
  "aussi bonne soit-elle, ne puisse jamais la deviner.")

name("CLARA")
p("&laquo;&nbsp;Notre phrase, ce sera le nom complet de Miel. "
  "Miel-Ambre. Personne d'autre que nous trois ne le conna&icirc;t, "
  "et &ccedil;a restera comme &ccedil;a tant qu'on n'aura pas r&eacute;gl&eacute; cette "
  "histoire une bonne fois pour toutes.&nbsp;&raquo;")

p("Alex et Darius hochent la t&ecirc;te en m&ecirc;me temps, presque "
  "solennellement, comme s'ils venaient de sceller un pacte "
  "bien plus important qu'un simple mot de passe, et se "
  "s&eacute;parent enfin, chacun rentrant chez soi sous un ciel dej&agrave; "
  "sombre, en gardant un &oelig;il un peu plus m&eacute;fiant que d'habitude "
  "sur chaque &eacute;cran allum&eacute; crois&eacute; en chemin.")

p("Darius, en attendant que les deux autres arrivent chez "
  "Clara, relit une derni&egrave;re fois le message de Kayden intercept&eacute; "
  "sur son propre ordinateur, cette phrase courte et glaciale "
  "&mdash; &laquo;&nbsp;tu m'as cherch&eacute;, me voil&agrave;&nbsp;&raquo; &mdash; et se demande si, en "
  "utilisant le b&acirc;ton volontairement aujourd'hui, ils ne sont "
  "pas justement en train de r&eacute;pondre pr&eacute;sent &agrave; cette invitation, "
  "exactement comme Kayden semble l'esp&eacute;rer depuis le d&eacute;but.")

p("Ils passent d'abord une bonne partie de l'apr&egrave;s-midi &agrave; "
  "relire, ensemble, chaque page du grimoire qu'Alex avait "
  "soigneusement photographi&eacute;e &agrave; la biblioth&egrave;que, cherchant "
  "un protocole plus s&ucirc;r que le simple &laquo;&nbsp;ouverture de rayon&nbsp;&raquo; "
  "qui avait fait tomber l'&eacute;tag&egrave;re, sans grand succ&egrave;s, la "
  "plupart des autres rituels semblant tout aussi impr&eacute;visibles.")

p("Clara propose, pour reprendre un peu d'avance, d'utiliser "
  "volontairement le b&acirc;ton, cette fois, pas par accident dans "
  "une biblioth&egrave;que, mais chez elle, m&eacute;thodiquement, pour "
  "chercher pr&eacute;cis&eacute;ment ce que le grimoire appelle &laquo;&nbsp;une page "
  "en attente&nbsp;&raquo; &mdash; l'une des cinq que Darius n'a jamais "
  "r&eacute;clam&eacute;es, celle qui pourrait, peut-&ecirc;tre, contenir une "
  "vraie r&eacute;ponse sur la nature exacte du march&eacute; que propose "
  "Kayden.")

p("La m&egrave;re de Clara, en apprenant qu'ils comptent passer "
  "l'apr&egrave;s-midi enferm&eacute;s dans le salon &laquo;&nbsp;pour un projet "
  "d'&eacute;cole&nbsp;&raquo;, leur propose un go&ucirc;ter qu'aucun des trois n'ose "
  "refuser sans para&icirc;tre suspect, et ils patientent, chacun "
  "grignotant sans app&eacute;tit r&eacute;el, jusqu'&agrave; ce qu'elle reparte "
  "faire ses courses, leur laissant enfin la maison pour eux "
  "seuls.")

p("Ils d&eacute;cident, d'un commun accord, de mener l'exp&eacute;rience "
  "chez Clara plut&ocirc;t que chez Darius, jugeant plus prudent "
  "d'&eacute;loigner ce genre de rituel de la maison o&ugrave; dort d&eacute;j&agrave; "
  "le pon&ccedil;on, comme si multiplier les objets charg&eacute;s dans un "
  "m&ecirc;me lieu risquait, d'une mani&egrave;re qu'aucun d'eux ne peut "
  "vraiment expliquer, d'amplifier encore la porte que Kayden "
  "cherche &agrave; forcer.")

p("Darius h&eacute;site longuement avant d'accepter, conscient que "
  "chaque utilisation du b&acirc;ton semble tirer un fil suppl&eacute;mentaire "
  "vers quelque chose qu'il ne ma&icirc;trise pas encore, mais la peur "
  "de rester passif, de laisser Kayden dicter le rythme de chaque "
  "attaque, finit par l'emporter sur la prudence.")

p("Alex insiste pour d&eacute;placer d'abord tous les objets fragiles "
  "de la pi&egrave;ce vers le couloir, un vase h&eacute;rit&eacute; d'une "
  "arri&egrave;re-grand-m&egrave;re en t&ecirc;te de liste, sous le regard "
  "amus&eacute; de Clara qui le trouve exag&eacute;r&eacute;ment prudent, jusqu'&agrave; "
  "ce qu'elle se souvienne, elle aussi, du fracas de l'&eacute;tag&egrave;re "
  "de la biblioth&egrave;que et cesse imm&eacute;diatement de plaisanter.")

p("Il tient le b&acirc;ton &agrave; deux mains, ferme les yeux comme "
  "indiqu&eacute; dans le grimoire, et pense, tr&egrave;s fort, non pas &agrave; "
  "une page au hasard, mais &agrave; la question pr&eacute;cise qui le "
  "hante depuis la biblioth&egrave;que : qu'est-il arriv&eacute; aux Darius "
  "d'avant lui, une fois leur r&ocirc;le termin&eacute;&nbsp;?")

p("Le b&acirc;ton devient brusquement tr&egrave;s lourd, presque "
  "impossible &agrave; tenir, et tire ses mains, comme aimant&eacute;, vers "
  "le mur du salon de Clara, pile &agrave; l'endroit o&ugrave; est accroch&eacute;e "
  "une vieille carte postale en noir et blanc de Luynes, achet&eacute;e "
  "par sa grand-m&egrave;re dans une brocante des ann&eacute;es soixante-dix "
  "et jamais vraiment regard&eacute;e depuis. Au dos, une &eacute;criture "
  "d&eacute;lav&eacute;e, presque effac&eacute;e, sign&eacute;e d'un seul pr&eacute;nom : "
  "&laquo;&nbsp;Ton p&egrave;re va mieux depuis qu'il ne se souvient plus du "
  "coteau. &mdash; D.&nbsp;&raquo;")

p("Darius sent le b&acirc;ton devenir soudain tr&egrave;s l&eacute;ger dans ses "
  "mains, presque flottant, comme s'il avait accompli exactement "
  "ce qu'on lui demandait et n'avait plus besoin de forcer quoi "
  "que ce soit d'autre, et le repose, tremblant, sur la table "
  "basse, incapable de d&eacute;tacher son regard de cette carte "
  "postale d&eacute;couverte par accident apr&egrave;s des d&eacute;cennies "
  "d'indiff&eacute;rence familiale.")

name("ALEX")
p("&laquo;&nbsp;D comme Darius. Un des anciens Darius a &eacute;crit &ccedil;a &agrave; "
  "quelqu'un. &Ccedil;a veut dire que le march&eacute; existait d&eacute;j&agrave; il y a "
  "cinquante ans, et que quelqu'un a accept&eacute; d'oublier, pour "
  "que son propre p&egrave;re aille mieux.&nbsp;&raquo;")

p("Clara d&eacute;croche pr&eacute;cautionneusement la carte postale du mur, "
  "cherchant dans le cadre lui-m&ecirc;me un &eacute;ventuel indice "
  "suppl&eacute;mentaire, avant de se souvenir, en fouillant sa "
  "m&eacute;moire, que sa grand-m&egrave;re avait toujours refus&eacute; de dire "
  "d'o&ugrave; venait exactement cette carte, se contentant de "
  "r&eacute;pondre, chaque fois qu'on le lui demandait, que c'&eacute;tait "
  "&laquo;&nbsp;un souvenir de quelqu'un qu'elle avait bien connu, dans "
  "sa jeunesse&nbsp;&raquo;.")

p("Darius retourne la carte plusieurs fois entre ses mains, "
  "cherchant un nom complet, une date pr&eacute;cise, sans en trouver "
  "aucun, seulement ce &laquo;&nbsp;D&nbsp;&raquo; solitaire, aussi discret et "
  "aussi lourd de sens que la propre initiale grav&eacute;e sur le "
  "pon&ccedil;on de Kayden.")

p("Clara raccroche soigneusement la carte postale &agrave; son clou, "
  "&agrave; l'envers cette fois, l'&eacute;criture tourn&eacute;e vers le mur, "
  "incapable d'expliquer pourquoi ce simple geste lui semble "
  "n&eacute;cessaire, comme si elle refusait, d&eacute;sormais, de laisser "
  "ce message vieux de cinquante ans continuer &agrave; regarder la "
  "pi&egrave;ce en silence.")

p("Avant de rentrer chacun chez soi, ils conviennent de se "
  "retrouver le lendemain avec la carte postale et le grimoire "
  "pour recouper syst&eacute;matiquement toutes les initiales, tous "
  "les indices &eacute;pars glan&eacute;s jusqu'ici, dans l'espoir de "
  "reconstituer, enfin, une chronologie compl&egrave;te des Darius "
  "qui les ont pr&eacute;c&eacute;d&eacute;s &mdash; un projet qu'Alex baptise, mi-s&eacute;rieux "
  "mi-amus&eacute;, &laquo;&nbsp;l'arbre g&eacute;n&eacute;alogique le plus bizarre du "
  "monde&nbsp;&raquo;.")

p("Clara, avant de partir elle aussi, prend une derni&egrave;re "
  "photo de la carte postale sous tous les angles, l'ajoutant "
  "&agrave; sa collection de preuves d&eacute;j&agrave; volumineuse, et glisse "
  "l'original dans une enveloppe kraft qu'elle range au fond "
  "d'un tiroir ferm&eacute; &agrave; cl&eacute;, jugeant plus s&ucirc;r, d&eacute;sormais, de "
  "s&eacute;parer physiquement chaque preuve plut&ocirc;t que de toutes "
  "les garder au m&ecirc;me endroit.")

p("Darius, seul sur le chemin du retour, repense &agrave; ce &laquo;&nbsp;D&nbsp;&raquo; "
  "sign&eacute; au dos de la carte postale, essayant d'imaginer le "
  "visage de cet ancien Darius, cet inconnu qui partageait son "
  "pr&eacute;nom sans partager son nom de famille, sa maison, son "
  "&eacute;poque, et se demande si, quelque part, cet homme pense "
  "encore parfois &agrave; ce qu'il a d&ucirc; sacrifier pour que son p&egrave;re "
  "&mdash; ou peut-&ecirc;tre pas m&ecirc;me son p&egrave;re, songe-t-il soudain, "
  "peut-&ecirc;tre quelqu'un d'autre &mdash; aille mieux.")

p("Clara lui envoie, avant qu'il ne parte, un dernier message "
  "avec une seule phrase, simple et directe : &laquo;&nbsp;quoi qu'il dise, "
  "c'est pas ta faute&nbsp;&raquo;, que Darius relit trois fois sur le pas "
  "de la porte de Clara avant de trouver le courage de vraiment "
  "se mettre en route vers chez lui.")

p("Sa m&egrave;re, en le voyant partir seul, lui rappelle de rentrer "
  "avant la nuit, un rappel presque tendre apr&egrave;s des semaines "
  "de m&eacute;fiance ouverte, et Darius promet, avec un pincement "
  "de culpabilit&eacute; en pensant &agrave; toutes les fois, r&eacute;centes, o&ugrave; "
  "il n'a pas vraiment tenu ce genre de promesse.")

p("Il glisse la carte postale dans la poche int&eacute;rieure de sa "
  "veste, &agrave; c&ocirc;t&eacute; du dossier de Franck et du grimoire, comme "
  "s'il constituait, sans l'avoir vraiment d&eacute;cid&eacute;, un dossier "
  "personnel de plus en plus &eacute;pais, une collection de preuves "
  "qu'aucun adulte ne pourra jamais consulter sans le croire "
  "compl&egrave;tement fou.")

p("Clara et Alex proposent de l'accompagner, mais Darius refuse, "
  "poliment, sentant qu'il s'agit l&agrave; d'une conversation qui lui "
  "appartient en propre, m&ecirc;me si elle finira, forc&eacute;ment, par "
  "les concerner tous. Ils le laissent partir avec la carte "
  "postale, promettant de rester joignables au moindre signe "
  "&eacute;trange, et Darius rentre &agrave; pied, seul, prenant volontairement "
  "le chemin le plus long pour se donner le temps de rassembler "
  "son courage.")

p("Il rentre chez lui ce soir-l&agrave; avec la carte postale glissée "
  "dans sa poche, &agrave; c&ocirc;t&eacute; du dossier de Franck, et reste "
  "longtemps assis sur son lit, le t&eacute;l&eacute;phone dans la main, &agrave; "
  "fixer le contact renomm&eacute; &laquo;&nbsp;Franck&nbsp;&raquo; sans le mot &laquo;&nbsp;Papa&nbsp;&raquo; "
  "devant, en pensant &agrave; cette phrase &eacute;crite au dos d'une "
  "carte postale cinquante ans plus t&ocirc;t par quelqu'un qui portait "
  "son propre pr&eacute;nom.")

p("Sa m&egrave;re, en bas, pr&eacute;pare le d&icirc;ner, et le bruit familier des "
  "casseroles qui s'entrechoquent lui parvient &eacute;touff&eacute; &agrave; "
  "travers le plancher, un fond sonore ordinaire qui contraste "
  "&eacute;trangement avec le poids de ce qu'il s'appr&ecirc;te &agrave; faire, "
  "comme si la maison enti&egrave;re refusait de prendre la mesure de "
  "l'importance de cet appel.")

p("Il appelle avant d'avoir fini de d&eacute;cider s'il en a vraiment "
  "envie, comme on saute dans l'eau froide pour ne pas se laisser "
  "le temps de changer d'avis. Il r&eacute;p&egrave;te mentalement sa "
  "premi&egrave;re phrase une derni&egrave;re fois, comme un texte appris "
  "pour un contr&ocirc;le oral, avant de comprendre qu'aucune "
  "r&eacute;p&eacute;tition ne le pr&eacute;parera vraiment &agrave; ce qui pourrait "
  "suivre. Franck d&eacute;croche &agrave; la troisi&egrave;me "
  "sonnerie, la voix surprise, presque m&eacute;fiante, n'ayant "
  "manifestement pas l'habitude de recevoir un appel de son fils "
  "en dehors des messages d'anniversaire.")

name("FRANCK")
p("&laquo;&nbsp;Darius&nbsp;? Il se passe quelque chose&nbsp;? T'as besoin "
  "d'argent, c'est &ccedil;a&nbsp;?&nbsp;&raquo;")

name("DARIUS")
p("&laquo;&nbsp;Non. J'ai juste une question. Elle va te para&icirc;tre "
  "bizarre, mais j'ai besoin que tu r&eacute;pondes honn&ecirc;tement, pour "
  "une fois. Est-ce que quelqu'un t'a d&eacute;j&agrave; parl&eacute;, quand t'&eacute;tais "
  "petit, d'une machine sur la place du march&eacute;, ou d'un truc "
  "appel&eacute; M13&nbsp;?&nbsp;&raquo;")

p("Le silence, au bout du fil, dure si longtemps que Darius "
  "croit un instant que la communication a coup&eacute;. Puis il "
  "entend Franck expirer, lentement, comme un homme qui pose "
  "enfin, apr&egrave;s des ann&eacute;es, un poids qu'il portait depuis trop "
  "longtemps pour s'en souvenir encore vraiment.")

name("FRANCK")
p("&laquo;&nbsp;Comment tu connais ce nom-l&agrave;. Personne conna&icirc;t ce "
  "nom-l&agrave;. Je l'ai jamais dit &agrave; personne, m&ecirc;me pas &agrave; ta "
  "m&egrave;re. J'ai... j'ai particip&eacute; &agrave; un truc, gamin, dans un "
  "centre pr&egrave;s de Fondettes. Mes parents disaient que c'&eacute;tait "
  "des bilans de sant&eacute;. Apr&egrave;s &ccedil;a, j'ai eu... des trous. Des "
  "ann&eacute;es enti&egrave;res dont je me souviens presque pas. Personne "
  "m'a jamais cru quand j'en parlais, alors j'ai arr&ecirc;t&eacute; d'en "
  "parler.&nbsp;&raquo;")

name("FRANCK")
p("&laquo;&nbsp;Y'a eu des ann&eacute;es o&ugrave; j'&eacute;tais s&ucirc;r d'avoir invent&eacute; tout "
  "&ccedil;a. Ma m&eacute;moire est bizarre, sur cette p&eacute;riode. Des trous "
  "nets, comme des pages arrach&eacute;es d'un livre. J'ai jamais su "
  "comment expliquer &ccedil;a &agrave; personne sans passer pour fou. Alors "
  "j'ai laiss&eacute; tomber, j'ai continu&eacute; ma vie, et j'ai... j'ai "
  "peut-&ecirc;tre report&eacute; sur toi, sans le vouloir, cette habitude "
  "de laisser tomber plut&ocirc;t que d'expliquer.&nbsp;&raquo;")

p("Darius ferme les yeux, la carte postale toujours serr&eacute;e "
  "dans sa main libre, et comprend, avec un vertige nouveau, "
  "que son p&egrave;re n'a peut-&ecirc;tre jamais &eacute;t&eacute; simplement l&acirc;che, ce "
  "mardi-l&agrave;, dans la voiture, &agrave; un feu rouge &mdash; il a "
  "peut-&ecirc;tre &eacute;t&eacute;, depuis l'enfance, exactement comme lui, "
  "quelqu'un &agrave; qui le syst&egrave;me avait d&eacute;j&agrave; appris, bien avant "
  "Miel, qu'un mensonge co&ucirc;te toujours moins cher qu'une v&eacute;rit&eacute; "
  "qu'on ne sait pas porter.")

p("Franck lui demande, avant de raccrocher, s'ils pourraient "
  "peut-&ecirc;tre se voir un de ces week-ends, pour de vrai cette "
  "fois, pas seulement au t&eacute;l&eacute;phone, et Darius, surpris par sa "
  "propre r&eacute;ponse, dit oui sans h&eacute;siter, avec une sinc&eacute;rit&eacute; "
  "qu'il ne se serait pas cru capable de ressentir encore, "
  "quelques semaines plus t&ocirc;t, envers cet homme.")

p("Ils raccrochent sur une promesse maladroite de se rappeler "
  "bient&ocirc;t, pour de vrai cette fois, sans machine ni myst&egrave;re "
  "entre eux, et Darius reste longtemps &agrave; fixer l'&eacute;cran &eacute;teint "
  "de son t&eacute;l&eacute;phone, surpris de d&eacute;couvrir, sous la peur et "
  "la col&egrave;re accumul&eacute;es depuis des ann&eacute;es, quelque chose qui "
  "ressemble, timidement, &agrave; de l'espoir.")

p("Il descend enfin d&icirc;ner, les yeux encore un peu rouges, et sa "
  "m&egrave;re, en le voyant, lui demande si tout va bien d'un ton "
  "qu'elle voudrait l&eacute;ger mais qui trahit son inqui&eacute;tude "
  "persistante depuis la fugue. Darius lui sourit, un vrai "
  "sourire cette fois, et lui r&eacute;pond que oui, pour une fois, "
  "&ccedil;a va vraiment un peu mieux &mdash; une phrase qui n'est, "
  "&eacute;trangement, pas tout &agrave; fait un mensonge.")

p("Plus tard dans la soir&eacute;e, il envoie &agrave; Clara et Alex un "
  "r&eacute;sum&eacute; complet de l'appel, mot de passe en t&ecirc;te de "
  "message, d&eacute;taillant la r&eacute;v&eacute;lation sur le pass&eacute; de Franck "
  "et cette phrase troublante sur Kayden qui &laquo;&nbsp;apportait des "
  "bonbons en cachette&nbsp;&raquo;, avant d'ajouter, en toute fin de "
  "message, une derni&egrave;re ligne qui r&eacute;sume, mieux que tout le "
  "reste, ce qu'il ressent&nbsp;: &laquo;&nbsp;je crois que je commence &agrave; "
  "avoir moins peur de lui et plus peur de ce qu'il repr&eacute;sente. "
  "C'est pas pareil.&nbsp;&raquo;")

p("Darius reste silencieux un long moment apr&egrave;s la confession "
  "de son p&egrave;re, cherchant les bons mots, incertain de vouloir "
  "vraiment poser la question suivante, celle qui lui br&ucirc;le "
  "pourtant la gorge depuis le d&eacute;but de cet appel.")

p("Franck raconte, avec des mots hesitants, retrouv&eacute;s au fur "
  "et &agrave; mesure qu'il parle comme s'ils avaient attendu "
  "patiemment quelque part en lui, les longues journ&eacute;es pass&eacute;es "
  "dans une salle blanche, des tests qu'on lui pr&eacute;sentait comme "
  "des jeux, un go&ucirc;ter offert &agrave; chaque fin de s&eacute;ance, et cette "
  "sensation diffuse, jamais formul&eacute;e &agrave; l'&eacute;poque, que quelque "
  "chose n'&eacute;tait pas tout &agrave; fait normal sans qu'il sache "
  "exactement quoi.")

name("DARIUS")
p("&laquo;&nbsp;Est-ce que tu te souviens d'un gar&ccedil;on, l&agrave;-bas, plus "
  "&acirc;g&eacute; que toi&nbsp;? Quelqu'un qui travaillait sur le programme, "
  "ou qui trainait dans les couloirs.&nbsp;&raquo;")

p("&laquo;&nbsp;Y'a un truc que je me rappelle quand m&ecirc;me, continue "
  "Franck, la voix plus basse maintenant, comme s'il craignait "
  "qu'on l'&eacute;coute m&ecirc;me &agrave; travers le t&eacute;l&eacute;phone. Y'avait un "
  "gar&ccedil;on, plus &acirc;g&eacute; que nous, qui traina&icirc;t toujours dans les "
  "couloirs du centre avec une tablette. Gentil. Il nous "
  "apportait des bonbons en cachette. On l'appelait tous "
  "Kayden.&nbsp;&raquo;")

p("Darius sent son c&oelig;ur s'arr&ecirc;ter une fraction de seconde. "
  "Il n'a jamais mentionn&eacute; ce nom &agrave; son p&egrave;re, pas une seule "
  "fois, ni au t&eacute;l&eacute;phone ni avant.")

name("DARIUS")
p("&laquo;&nbsp;Papa. Je t'ai jamais dit ce nom-l&agrave;.&nbsp;&raquo;")

p("Franck rit doucement, un rire fatigu&eacute; mais sinc&egrave;re, avant "
  "d'ajouter que ce Kayden &eacute;tait le seul, dans tout ce centre "
  "froid et impersonnel, &agrave; traiter les enfants comme des "
  "enfants et non comme des sujets d'&eacute;tude, ce qui rend, "
  "aujourd'hui, d'autant plus difficile pour Darius d'accepter "
  "ce que ce m&ecirc;me gar&ccedil;on est devenu depuis.")

p("Un nouveau silence, plus long, plus lourd que le premier. "
  "Quand Franck reprend la parole, sa voix a chang&eacute;, plus "
  "lente, plus &eacute;gale, comme si quelqu'un, quelque part, "
  "r&eacute;glait le d&eacute;bit de ses mots &agrave; sa place.")

S.append(Paragraph("FRANCK (voix alt&eacute;r&eacute;e)", cn))
p("&laquo;&nbsp;C'est parce que c'est moi qui te le dis, Darius. Pas "
  "ton p&egrave;re. Ton p&egrave;re dort, l&agrave;, maintenant, pendant que je "
  "me sers un peu de sa voix pour te parler plus facilement. "
  "&Ccedil;a a toujours &eacute;t&eacute; plus simple avec un adulte. Les enfants "
  "posent trop de questions.&nbsp;&raquo;")

p("Darius raccroche imm&eacute;diatement, les mains tremblantes, et "
  "rappelle aussit&ocirc;t, le c&oelig;ur battant si fort qu'il en a mal "
  "aux tempes, jusqu'&agrave; ce que Franck d&eacute;croche &agrave; nouveau, sa "
  "vraie voix cette fois, confuse, comme quelqu'un qui vient de "
  "se r&eacute;veiller en plein milieu d'une phrase.")

name("FRANCK")
p("&laquo;&nbsp;Darius&nbsp;? D&eacute;sol&eacute;, j'ai... j'ai d&ucirc; m'endormir une "
  "seconde. Qu'est-ce que tu me demandais, d&eacute;j&agrave;&nbsp;?&nbsp;&raquo;")

p("Le vent souffle doucement dans la rue vide, faisant "
  "trembler la lumi&egrave;re du seul lampadaire encore allum&eacute;, et "
  "Darius reste l&agrave;, immobile sur les marches, laissant le "
  "froid l'engourdir un peu, comme si &ccedil;a pouvait, physiquement, "
  "&eacute;mousser un peu la douleur de ce qu'il vient d'entendre.")

p("Il pense &agrave; appeler Clara et Alex imm&eacute;diatement pour tout "
  "leur raconter, puis se ravise, pr&eacute;f&eacute;rant d'abord reprendre "
  "son souffle seul quelques minutes, assis sur les marches de "
  "l'escalier, avant de devoir remettre des mots sur ce qu'il "
  "vient d'entendre &mdash; la voix de son p&egrave;re et celle de Kayden, "
  "confondues l'espace d'un appel t&eacute;l&eacute;phonique ordinaire.")

p("Il reste immobile, le t&eacute;l&eacute;phone toujours coll&eacute; &agrave; l'oreille, "
  "&agrave; &eacute;couter le silence qui a remplac&eacute; la voix alt&eacute;r&eacute;e de son "
  "p&egrave;re, incapable de savoir si Kayden est encore l&agrave;, tapi "
  "quelque part dans la ligne, ou s'il vient de se retirer aussi "
  "soudainement qu'il &eacute;tait apparu.")

p("Darius essaie, la voix tremblante, de lui r&eacute;p&eacute;ter mot pour "
  "mot ce que &laquo;&nbsp;Kayden&nbsp;&raquo; venait de dire &agrave; travers lui, "
  "esp&eacute;rant qu'entendre &ccedil;a le r&eacute;veillerait compl&egrave;tement, mais "
  "Franck ne fait que froncer les sourcils, perplexe, comme si "
  "on lui racontait un r&ecirc;ve qui n'&eacute;tait pas le sien.")

p("Il ne se souvient de rien. Ni de Kayden, ni de M13, ni des "
  "vingt derni&egrave;res minutes de leur conversation, comme si "
  "quelqu'un venait, en direct, de lui reprendre une nouvelle "
  "petite tranche de sa propre vie, sans lui laisser cette fois "
  "m&ecirc;me le temps de savoir ce qu'il perdait.")

p("Sa m&egrave;re, entendant sa voix &agrave; travers la cloison, frappe "
  "doucement pour lui demander s'il va bien, et Darius, la "
  "main sur le combin&eacute;, lui r&eacute;pond qu'il parle juste &agrave; Clara "
  "d'un devoir de fran&ccedil;ais, un mensonge de plus, si petit et "
  "si banal qu'il ne lui co&ucirc;te presque rien &agrave; prononcer, ce "
  "qui l'inqui&egrave;te davantage encore une fois qu'elle a referm&eacute; "
  "la porte.")

p("Il envoie enfin ce message qu'il retardait depuis son retour "
  "dans sa chambre, &agrave; Clara et Alex, le mot de passe convenu "
  "en premi&egrave;re ligne pour prouver que c'est bien lui&nbsp;: "
  "&laquo;&nbsp;Miel-Ambre. Faut que je vous raconte un truc, c'est "
  "grave. Il peut parler &agrave; travers les gens maintenant, pas "
  "juste les &eacute;crans.&nbsp;&raquo;")

p("Clara r&eacute;pond en moins d'une minute, malgr&eacute; l'heure "
  "tardive, avec le m&ecirc;me mot de passe suivi d'un simple "
  "&laquo;&nbsp;j'arrive pas &agrave; dormir non plus, appelle-moi si tu veux "
  "en parler maintenant&nbsp;&raquo;, et Darius, touch&eacute; par cette "
  "disponibilit&eacute; imm&eacute;diate, compose son num&eacute;ro sans plus "
  "h&eacute;siter, soulag&eacute; de ne pas avoir &agrave; porter cette nuit-l&agrave; "
  "compl&egrave;tement seul.")

p("Darius raccroche, s'assoit par terre, le dos contre son lit, "
  "et reste ainsi tr&egrave;s longtemps, incapable de pleurer, "
  "incapable de bouger, comprenant seulement, avec une clart&eacute; "
  "glaciale qu'aucun cours de sciences ne lui avait jamais "
  "donn&eacute;e, que le champ de bataille vient de s'&eacute;largir bien "
  "au-del&agrave; de Luynes, bien au-del&agrave; de lui-m&ecirc;me &mdash; que Kayden, "
  "d&eacute;sormais, peut atteindre n'importe qui qu'il aime, "
  "n'importe quand, &agrave; travers n'importe quel fil t&eacute;l&eacute;phonique, "
  "et que la seule chose qui lui reste encore, pour le moment, "
  "c'est de ne pas raccrocher pour de bon sur les gens qu'il "
  "lui reste &agrave; prot&eacute;ger.")

p("Franck, depuis leur appel, envoie chaque jour un petit "
  "message anodin, une photo du garage, une blague sans "
  "grande finesse, comme s'il essayait, maladroitement mais "
  "sinc&egrave;rement, de reconstruire pierre par pierre ce qu'il "
  "avait laiss&eacute; s'effondrer pendant des ann&eacute;es, et Darius "
  "r&eacute;pond &agrave; chacun d'eux, m&ecirc;me bri&egrave;vement, surpris de "
  "constater &agrave; quel point &ccedil;a lui fait du bien.")

p("Le b&acirc;ton, dans les jours qui suivent l'appel &agrave; Franck, ne "
  "cesse plus de tirer les mains de Darius vers le nord-est, "
  "toujours la m&ecirc;me direction, avec une insistance croissante, "
  "comme une aiguille de boussole affol&eacute;e par un aimant "
  "toujours plus proche. Un soir, incapable de r&eacute;sister plus "
  "longtemps, il suit cette traction jusqu'&agrave; la place du "
  "march&eacute;, o&ugrave; la machine, pour la premi&egrave;re fois depuis des "
  "semaines, affiche un texte diff&eacute;rent de celui qu'ils "
  "connaissent par c&oelig;ur&nbsp;:")

S.append(Paragraph(
    "L'ARCHIVE EST PLEINE.<br/>LA DERNI&Egrave;RE PAGE S'&Eacute;CRIRA CE SOIR.",
    machine_style))

p("Il reste plant&eacute; l&agrave;, sous la pluie fine qui vient de "
  "reprendre, &agrave; relire ces neuf mots jusqu'&agrave; ce qu'ils "
  "perdent presque leur sens, incapable de d&eacute;cider s'il doit "
  "courir chercher Clara et Alex tout de suite ou prendre "
  "encore une minute, une seule, pour respirer normalement "
  "une derni&egrave;re fois avant que sa vie ne bascule d&eacute;finitivement "
  "dans autre chose. Il pense &agrave; tous les jeudis ordinaires "
  "qu'il a v&eacute;cus avant celui-l&agrave;, &agrave; quel point un ado de "
  "quatorze ans n'est normalement pas cens&eacute; porter ce genre "
  "de d&eacute;cision sur ses &eacute;paules, et &agrave; quel point, pourtant, "
  "personne d'autre &agrave; Luynes n'est en mesure de la prendre "
  "&agrave; sa place.")

p("Il sort son t&eacute;l&eacute;phone, h&eacute;site une seconde de plus, puis "
  "&eacute;crit le mot de passe convenu avant m&ecirc;me le message, "
  "comme un r&eacute;flexe d&eacute;sormais grav&eacute; en lui&nbsp;: &laquo;&nbsp;Miel-Ambre. "
  "C'est ce soir. Rejoignez-moi place du march&eacute;, maintenant, "
  "c'est pas un exercice.&nbsp;&raquo; Les deux r&eacute;ponses arrivent en "
  "moins d'une minute, presque simultan&eacute;ment, sans une "
  "seule question pos&eacute;e, juste un &laquo;&nbsp;j'arrive&nbsp;&raquo; de Clara et un "
  "pouce lev&eacute; d'Alex, comme si tous les deux avaient, eux "
  "aussi, senti depuis des jours que cette nuit-l&agrave; approchait.")

p("Il reste immobile un long moment devant l'&eacute;cran, incapable "
  "de bouger, pendant que la pluie recommence &agrave; tomber "
  "derri&egrave;re lui exactement comme le tout premier soir, comme "
  "si la place elle-m&ecirc;me tenait &agrave; boucler la boucle avec le "
  "m&ecirc;me d&eacute;cor qu'au d&eacute;part. Il pense &agrave; tout ce chemin "
  "parcouru depuis ce jeudi de novembre &mdash; le collier, "
  "l'entrep&ocirc;t, la grotte, l'appel &agrave; Franck &mdash; et se demande "
  "si tout &ccedil;a n'&eacute;tait, depuis le d&eacute;but, qu'un compte &agrave; "
  "rebours dont il ignorait l'existence.")

p("Clara, appel&eacute;e en urgence, comprend en une phrase ce que "
  "cela signifie&nbsp;: apr&egrave;s trente ans &agrave; grappiller des ann&eacute;es "
  "une par une, page apr&egrave;s page, famille apr&egrave;s famille, "
  "l'archive de M13 a atteint une masse critique. Kayden n'a "
  "plus besoin de personne pour la remplir. Il peut d&eacute;sormais "
  "aspirer, d'un seul geste, la m&eacute;moire enti&egrave;re de Luynes &mdash; "
  "chaque souvenir, chaque visage, chaque nom &mdash; et se "
  "reconstituer, une bonne fois pour toutes, non plus comme "
  "une voix pi&eacute;g&eacute;e dans un objet, mais comme quelque chose "
  "de pleinement, terriblement r&eacute;el.")

p("Alex, encore, propose d'appeler quelqu'un &mdash; un adulte, "
  "n'importe qui, m&ecirc;me si aucun d'eux ne sait qui pourrait "
  "bien les croire &mdash; avant de laisser tomber l'id&eacute;e presque "
  "aussit&ocirc;t, conscient qu'ils sont, depuis le tout premier "
  "soir, les seuls capables de comprendre ce qui se joue "
  "vraiment sous cette place.")

name("CLARA")
p("&laquo;&nbsp;Si on le laisse faire, tout le monde ici oubliera tout "
  "en une nuit. Pas juste nous. Tout Luynes. Chaque personne "
  "qui a jamais aim&eacute; quelqu'un dans cette ville deviendra une "
  "page de son livre, et lui deviendra la seule chose qui "
  "reste.&nbsp;&raquo;")

p("Ils remontent chacun chez eux pour dix minutes, le temps "
  "de laisser un mot vague &agrave; leurs parents &mdash; une soir&eacute;e "
  "devoirs chez Clara, encore, le m&ecirc;me pr&eacute;texte us&eacute; jusqu'&agrave; "
  "la corde &mdash; avant de se retrouver, essouffl&eacute;s, devant la "
  "vitrine qui les attend, illumin&eacute;e d'une lueur bleue plus "
  "intense que jamais, comme si elle savait, elle aussi, "
  "qu'il s'agissait ce soir d'autre chose que d'une visite "
  "ordinaire.")

p("Alex, d&eacute;j&agrave; en train de fourrer dans son sac tout ce qui "
  "pourrait servir &mdash; une lampe, la vieille pince de son "
  "grand-p&egrave;re, le grimoire enti&egrave;rement recopi&eacute; page par page "
  "dans son propre carnet au cas o&ugrave; l'original dispara&icirc;trait "
  "&mdash; l&egrave;ve les yeux vers Darius, cherchant, sur son visage, la "
  "certitude qu'aucun d'eux trois ne poss&egrave;de vraiment ce "
  "soir-l&agrave;.")

p("Darius pense, une derni&egrave;re fois avant de refermer son sac, "
  "&agrave; ce que Kayden lui a dit un soir, depuis le pon&ccedil;on&nbsp;: "
  "&laquo;&nbsp;on se reverra bient&ocirc;t&nbsp;&raquo;. Il n'avait pas imagin&eacute;, sur le "
  "moment, que ce &laquo;&nbsp;bient&ocirc;t&nbsp;&raquo; prendrait la forme d'une nuit "
  "o&ugrave; l'enjeu ne serait plus seulement sa propre m&eacute;moire, "
  "mais celle de toute une ville.")

name("ALEX")
p("&laquo;&nbsp;On n'a jamais fait &ccedil;a &agrave; trois, direct dans le "
  "Non-lieu. On sait m&ecirc;me pas si on peut y entrer ensemble, ou "
  "si &ccedil;a nous s&eacute;pare comme la derni&egrave;re fois.&nbsp;&raquo;")

name("DARIUS")
p("&laquo;&nbsp;On n'a plus le temps d'avoir peur de &ccedil;a. Si on "
  "attend demain, y'aura peut-&ecirc;tre plus personne, demain, pour "
  "avoir peur de quoi que ce soit.&nbsp;&raquo;")

p("Clara, avant de partir, appelle rapidement sa m&egrave;re pour "
  "l'entendre une derni&egrave;re fois, une conversation banale sur "
  "l'heure du retour et le linge &agrave; rentrer avant la pluie, "
  "qu'elle &eacute;coute avec une attention inhabituelle, comme si "
  "elle voulait graver cette voix ordinaire quelque part au "
  "fond d'elle, au cas o&ugrave; la soir&eacute;e tournerait aussi mal "
  "qu'elle le redoute.")

p("Ils se prennent la main devant la vitrine, un geste qu'aucun "
  "des trois n'aurait os&eacute; sugg&eacute;rer un an plus t&ocirc;t, et Darius "
  "pose sa paume libre &agrave; plat contre le verre froid, le b&acirc;ton "
  "coinc&eacute; sous son bras, le pon&ccedil;on serr&eacute; dans son poing, "
  "pendant que la machine, docile pour la premi&egrave;re fois, "
  "s'ouvre sous leurs pieds comme une bouche patiente qui "
  "attendait ce trio pr&eacute;cis depuis le tout premier soir.")

p("La derni&egrave;re chose que Darius voit, avant que le sol de "
  "la machine ne les avale compl&egrave;tement, c'est la place du "
  "march&eacute; de Luynes, ordinaire, endormie, avec ses fen&ecirc;tres "
  "&eacute;clair&eacute;es &ccedil;a et l&agrave;, totalement indiff&eacute;rente au fait qu'elle "
  "s'appr&ecirc;te &agrave; perdre, peut-&ecirc;tre pour de bon, trois de ses "
  "habitants les plus jeunes dans un combat dont elle ne "
  "saura jamais rien.")

p("La chute elle-m&ecirc;me dure une &eacute;ternit&eacute; compress&eacute;e en "
  "quelques secondes, un vertige sans direction "
  "pr&eacute;cise, ni haut ni bas, seulement une acc&eacute;l&eacute;ration "
  "qui semble venir de partout &agrave; la fois, et Darius sent "
  "la main de Clara se resserrer plus fort autour de la "
  "sienne, un point d'ancrage minuscule dans cette "
  "d&eacute;sorientation totale.")

p("Autour d'eux, l'espace lui-m&ecirc;me semble h&eacute;siter entre "
  "plusieurs formes possibles, tant&ocirc;t un couloir d'h&ocirc;pital "
  "d&eacute;sert, tant&ocirc;t la place du march&eacute; elle-m&ecirc;me "
  "d&eacute;form&eacute;e comme un reflet dans une eau agit&eacute;e, tant&ocirc;t "
  "rien du tout, un vide absolu ponctu&eacute; seulement par "
  "cette lumi&egrave;re bleue qui semble &eacute;maner de partout et "
  "de nulle part &agrave; la fois.")

name("ALEX")
p("&laquo;&nbsp;C'est normal, ce truc, cette impression qu'on "
  "n'est nulle part et partout en m&ecirc;me temps ? Parce que "
  "moi &ccedil;a me donne trop envie de vomir, l&agrave;.&nbsp;&raquo;")

p("Clara, luttant elle aussi contre la naus&eacute;e, serre les "
  "dents et garde les yeux ouverts, refusant de "
  "s'abandonner totalement &agrave; la d&eacute;sorientation, "
  "cherchant instinctivement, dans ce chaos sensoriel, "
  "un point fixe auquel se raccrocher visuellement "
  "pendant que la chute se poursuit.")

p("Puis, aussi brutalement qu'elle a commenc&eacute;, la chute "
  "s'arr&ecirc;te, et les trois amis atterrissent, non pas "
  "durement comme on pourrait s'y attendre, mais avec "
  "une l&eacute;g&egrave;ret&eacute; presque insultante, comme si "
  "l'environnement lui-m&ecirc;me avait choisi de les "
  "&eacute;pargner cette derni&egrave;re humiliation physique avant "
  "de r&eacute;v&eacute;ler, enfin, la v&eacute;ritable ampleur de ce qui les "
  "attend.")

p("Darius se relève le premier, les jambes tremblantes, "
  "et tend la main &agrave; Clara puis &agrave; Alex pour les aider &agrave; "
  "se remettre debout &agrave; leur tour, tous trois "
  "d&eacute;couvrant, en se redressant, un silence anormal "
  "autour d'eux, comme si m&ecirc;me l'air lui-m&ecirc;me retenait "
  "son souffle en attendant ce qui allait suivre.")

name("CLARA")
p("&laquo;&nbsp;C'est diff&eacute;rent, cette fois. La derni&egrave;re fois "
  "qu'on est venus ici, y'avait au moins de la "
  "lumi&egrave;re, une direction &agrave; suivre. L&agrave;, j'ai "
  "l'impression qu'on est nulle part du tout, genre "
  "vraiment nulle part.&nbsp;&raquo;")

p("Le b&acirc;ton, dans la main de Darius, se met &agrave; vibrer "
  "doucement, une pulsation r&eacute;guli&egrave;re qui rappelle un "
  "battement de c&oelig;ur, et il comprend, sans qu'on ait "
  "besoin de le lui expliquer, que cet objet ancestral "
  "conna&icirc;t le chemin m&ecirc;me si lui l'ignore compl&egrave;tement, "
  "comme s'il avait d&eacute;j&agrave; guid&eacute; d'autres porteurs &agrave; "
  "travers ce m&ecirc;me n&eacute;ant plusieurs fois auparavant.")

name("DARIUS")
p("&laquo;&nbsp;Suivez-moi. Le b&acirc;ton sait o&ugrave; aller, je le sens. "
  "C'est comme s'il tirait doucement vers une "
  "direction pr&eacute;cise, m&ecirc;me si je vois absolument rien "
  "devant nous.&nbsp;&raquo;")

p("Ils avancent ainsi, pendant ce qui leur semble de "
  "longues minutes, guid&eacute;s par cette pulsation "
  "silencieuse, jusqu'&agrave; ce qu'une lueur rouge&acirc;tre "
  "commence &agrave; percer l'obscurit&eacute; devant eux, faible "
  "d'abord puis grandissant rapidement, r&eacute;v&eacute;lant, &agrave; "
  "mesure qu'ils approchent, les contours d'un espace "
  "immense en train de se consumer.")

p("Clara, marchant juste derri&egrave;re Darius, sent son "
  "propre carnet, glissé dans la poche int&eacute;rieure de "
  "son manteau, devenir soudainement br&ucirc;lant contre "
  "sa poitrine, une chaleur presque douloureuse qui la "
  "fait sursauter et porter instinctivement la main &agrave; "
  "cet endroit pr&eacute;cis.")

name("CLARA")
p("&laquo;&nbsp;Mon carnet, il devient hyper chaud, l&agrave;. "
  "Comme s'il r&eacute;agissait &agrave; quelque chose qui "
  "approche. Vous sentez pas un truc similaire, vous "
  "aussi ?&nbsp;&raquo;")

p("Alex confirme ressentir, lui aussi, une sensation "
  "&eacute;trange au niveau de son avant-bras, l&agrave; o&ugrave; se "
  "trouvera, quelques instants plus tard seulement, "
  "la cicatrice qui marquera d&eacute;finitivement son "
  "engagement dans cette histoire, un picotement "
  "d&eacute;sagr&eacute;able qui s'intensifie &agrave; mesure qu'ils "
  "avancent vers la lueur rougeoyante.")

p("Darius, concentr&eacute; sur la direction indiqu&eacute;e par "
  "le b&acirc;ton vibrant entre ses mains, ne remarque ces "
  "r&eacute;actions de ses amis qu'apr&egrave;s coup, comprenant "
  "instinctivement que chacun d'entre eux, &agrave; sa "
  "mani&egrave;re, se pr&eacute;pare d&eacute;j&agrave; physiquement &agrave; "
  "l'affrontement qui les attend, leurs corps "
  "r&eacute;agissant &agrave; une menace que leurs esprits "
  "conscients ne peuvent pas encore totalement "
  "appr&eacute;hender.")

p("La lueur rougeoyante grandit encore, r&eacute;v&eacute;lant "
  "progressivement l'ampleur d'un espace immense, "
  "aux contours instables, dont les murs eux-m&ecirc;mes "
  "semblent respirer au rythme d'une pr&eacute;sence "
  "colossale et souffrante, et Darius comprend, avec "
  "un frisson glac&eacute; malgr&eacute; la chaleur ambiante, qu'ils "
  "viennent d'atteindre le c&oelig;ur m&ecirc;me du Non-lieu, l&agrave; "
  "o&ugrave; Kayden, dans toute sa souffrance accumul&eacute;e "
  "depuis des d&eacute;cennies, les attend d&eacute;j&agrave;.")

p("Clara serre plus fort la main de Darius, cherchant "
  "dans ce contact simple le courage n&eacute;cessaire pour "
  "franchir les derniers m&egrave;tres les s&eacute;parant de cette "
  "confrontation redout&eacute;e depuis des semaines, tandis "
  "qu'Alex, de l'autre c&ocirc;t&eacute;, ramasse au sol un "
  "morceau de m&eacute;tal tordu qui tra&icirc;nait l&agrave;, "
  "instinctivement, comme s'il pressentait avoir "
  "besoin de tout objet susceptible de servir d'arme "
  "improvis&eacute;e face &agrave; ce qui les attend.")

name("ALEX")
p("&laquo;&nbsp;On y va tous ensemble, hein. Personne fonce "
  "en avant tout seul, quoi qu'il se passe. On "
  "reste group&eacute;s, comme toujours.&nbsp;&raquo;")

p("Cette derni&egrave;re instruction, prononc&eacute;e d'une voix "
  "qu'Alex voudrait plus assur&eacute;e qu'elle ne l'est "
  "vraiment, r&eacute;sonne comme un pacte silencieux entre "
  "les trois amis, une promesse mutuelle de ne "
  "jamais s'abandonner les uns les autres, m&ecirc;me face "
  "&agrave; l'entit&eacute; la plus terrifiante qu'ils aient jamais "
  "eu &agrave; affronter.")

p("Darius resserre sa prise sur le b&acirc;ton, sentant sous "
  "ses doigts les irr&eacute;gularit&eacute;s du bois anciens, "
  "poli par des mains innombrables au fil des "
  "si&egrave;cles, et puise dans ce contact rugueux une "
  "force qu'il ne se savait pas capable de "
  "rassembler, une d&eacute;termination forg&eacute;e non pas par "
  "lui seul mais par tous ceux qui, avant lui, ont "
  "d&ucirc; faire face &agrave; cette m&ecirc;me &eacute;preuve.")

p("Ils avancent, d&eacute;sormais tous les trois &eacute;paule "
  "contre &eacute;paule, vers cette lumi&egrave;re rougeoyante qui "
  "r&eacute;v&egrave;le, &agrave; chaque pas suppl&eacute;mentaire, un peu plus "
  "l'ampleur terrifiante de ce qui les attend &mdash; un "
  "espace immense o&ugrave; la r&eacute;alit&eacute; elle-m&ecirc;me semble se "
  "d&eacute;liter, remplac&eacute;e par des fragments incoh&eacute;rents "
  "de Luynes, de leurs propres souvenirs, et d'une "
  "douleur ancienne dont l'origine exacte leur "
  "&eacute;chappe encore compl&egrave;tement.")

p("Le sol lui-m&ecirc;me semble incertain sous leurs "
  "pieds, tant&ocirc;t solide comme du b&eacute;ton, tant&ocirc;t mou "
  "comme du sable mouvant, oblig&eacute;s d'avancer avec "
  "une prudence redoubl&eacute;e, chacun tendant "
  "instinctivement le bras vers le voisin d&egrave;s qu'un "
  "vertige menace de d&eacute;s&eacute;quilibrer l'un d'entre "
  "eux, cette solidarit&eacute; physique refl&eacute;tant &agrave; la "
  "perfection leur solidarit&eacute; &eacute;motionnelle face &agrave; "
  "l'inconnu.")

name("CLARA")
p("&laquo;&nbsp;Je sens quelque chose, l&agrave;, tout pr&egrave;s. Une "
  "pr&eacute;sence, comme une respiration g&eacute;ante. &Ccedil;a doit "
  "&ecirc;tre lui. &Ccedil;a doit &ecirc;tre Kayden.&nbsp;&raquo;")

p("Cette intuition, partag&eacute;e presque instantan&eacute;ment "
  "par Alex et Darius, se confirme quelques instants "
  "plus tard lorsqu'une silhouette massive et "
  "instable commence &agrave; se dessiner dans la lumi&egrave;re "
  "rougeoyante devant eux, mi-humaine mi-architecture "
  "num&eacute;rique, incarnant &agrave; elle seule toute la "
  "souffrance accumul&eacute;e d'une existence bris&eacute;e "
  "depuis plus de trente ans.")

p("Alex serre plus fort le morceau de m&eacute;tal tordu "
  "ramass&eacute; plus t&ocirc;t, sentant son c&oelig;ur battre &agrave; "
  "tout rompre dans sa poitrine, tandis que Darius, "
  "curieusement, ressent une forme de calme &eacute;trange "
  "l'envahir &agrave; mesure que la silhouette de Kayden "
  "se pr&eacute;cise, comme si une part ancienne de "
  "lui-m&ecirc;me, h&eacute;rit&eacute;e de toute la lign&eacute;e de "
  "porteurs qui l'ont pr&eacute;c&eacute;d&eacute;, reconnaissait cet "
  "adversaire pour l'avoir d&eacute;j&agrave; affront&eacute;, sous une "
  "forme ou une autre, &agrave; travers les si&egrave;cles.")

name("DARIUS")
p("&laquo;&nbsp;C'est le moment. On y va, ensemble, "
  "comme on l'a toujours fait. Peu importe ce qui "
  "nous attend l&agrave;-dedans.&nbsp;&raquo;")

p("Clara serre une derni&egrave;re fois son carnet contre "
  "sa poitrine, ce m&ecirc;me carnet qui, depuis des mois "
  "d&eacute;j&agrave;, semble poss&eacute;der une conscience propre, "
  "capable de r&eacute;agir aux &eacute;v&eacute;nements les plus "
  "extraordinaires de leur aventure commune, et "
  "sent, sous ses doigts, une chaleur rassurante "
  "&eacute;maner de ses pages, comme si l'objet lui-m&ecirc;me "
  "cherchait &agrave; lui insuffler un peu de courage "
  "avant l'affrontement &agrave; venir.")

p("Ensemble, sans plus &eacute;changer un seul mot, les "
  "trois amis avancent vers cette silhouette "
  "gigantesque et souffrante qui incarne, sous une "
  "forme &agrave; la fois terrifiante et profond&eacute;ment "
  "tragique, tout ce que le programme du docteur "
  "Vasseur a caus&eacute; de d&eacute;g&acirc;ts irr&eacute;versibles sur une "
  "vie humaine unique, transform&eacute;e contre son gr&eacute; en "
  "quelque chose qui n'est plus tout &agrave; fait vivant "
  "ni tout &agrave; fait mort.")

p("Le b&acirc;ton de Darius s'illumine soudain d'une "
  "lueur dor&eacute;e, r&eacute;pondant &agrave; la proximit&eacute; grandissante "
  "de cette masse d'&eacute;nergie souffrante, et projette "
  "autour d'eux trois un cercle de protection "
  "fragile mais r&eacute;el, une derni&egrave;re barri&egrave;re avant "
  "l'affrontement d&eacute;finitif qui va, dans les minutes "
  "&agrave; venir, d&eacute;terminer le sort de leur petite "
  "communaut&eacute; et, peut-&ecirc;tre, celui de bien d'autres "
  "encore &agrave; travers la vall&eacute;e enti&egrave;re.")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 3 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 4 -- LE NON-LIEU EN FLAMMES
# ======================================================================
chap(4, "LE NON-LIEU EN FLAMMES")

p("Ils tombent tous les trois ensemble, cette fois, dans un "
  "espace qui n'a plus rien du vide blanc et patient des "
  "premi&egrave;res visites de Darius. Le Non-lieu enti&egrave;re br&ucirc;le d'une "
  "lumi&egrave;re bleue si intense qu'elle fait mal aux yeux, "
  "travers&eacute;e de longues d&eacute;chirures noires par lesquelles on "
  "aper&ccedil;oit, en transparence, des bribes de Luynes en train "
  "de se dissoudre &mdash; le clocher de l'&eacute;glise qui se d&eacute;compose "
  "en cascade de chiffres, la biblioth&egrave;que qui se replie sur "
  "elle-m&ecirc;me comme une page qu'on froisse, des silhouettes "
  "d'habitants, floues, qui marchent en boucle sans jamais "
  "arriver nulle part, comme des figurants oubli&eacute;s dans un "
  "d&eacute;cor qu'on d&eacute;monte autour d'eux.")

p("Darius cherche Clara et Alex des yeux dans ce d&eacute;cor qui "
  "n'arr&ecirc;te pas de se recomposer, et met une seconde de trop "
  "&agrave; les retrouver, quelques m&egrave;tres plus loin, tous deux "
  "d&eacute;boussol&eacute;s par la sensation de tomber sans jamais "
  "atterrir, cette gravit&eacute; incertaine qui semble &ecirc;tre la seule "
  "loi encore &agrave; peu pr&egrave;s stable dans cet endroit.")

p("Au centre de ce chaos, Kayden ne ressemble plus &agrave; "
  "l'adolescent souriant de la photo de foot, ni tout &agrave; fait &agrave; "
  "la silhouette assise sur sa chaise d'&eacute;colier. Il est devenu "
  "immense, une masse instable qui n'arrive pas &agrave; choisir "
  "entre plusieurs formes &agrave; la fois &mdash; parfois un gar&ccedil;on de "
  "dix-neuf ans, en blouse blanche, les mains tendues comme "
  "pour s'excuser ; parfois une architecture de c&acirc;bles et "
  "d'&eacute;crans crev&eacute;s empil&eacute;s en spirale jusqu'&agrave; disparaitre "
  "dans le haut du ciel strié ; et, entre les deux, quelque "
  "chose d'ind&eacute;fini, une peau qui se craquelle par endroits "
  "pour laisser sourdre un liquide noir et huileux, charg&eacute; de "
  "micro-lignes de code qui grouillent comme des insectes "
  "avant de se figer, puis de recommencer.")

S.append(Paragraph("KAYDEN (mille voix superpos&eacute;es)", cn))
p("&laquo;&nbsp;Vous &ecirc;tes venus &agrave; trois, cette fois. Ravissant. J'aurai "
  "trois fois plus &agrave; garder.&nbsp;&raquo;")

p("Darius sent, dans cette phrase, quelque chose qui "
  "ressemble presque &agrave; de la solitude, comme si Kayden, "
  "malgr&eacute; toute sa puissance nouvelle, restait au fond ce "
  "gar&ccedil;on de dix-neuf ans qui n'a jamais eu personne pour "
  "l'accompagner assez longtemps dans ce qu'il traversait, et "
  "cette pens&eacute;e, aussi br&egrave;ve soit-elle, le d&eacute;stabilise plus "
  "que n'importe quelle attaque directe n'aurait pu le faire.")

p("Alex, une main press&eacute;e contre l'entaille sur son bras, "
  "cherche des yeux un rep&egrave;re fixe dans ce d&eacute;cor qui ne "
  "cesse de se recomposer, et fixe finalement le b&acirc;ton entre "
  "les mains de Darius, s'accrochant &agrave; cette seule certitude "
  "solide pour ne pas laisser la panique prendre compl&egrave;tement "
  "le dessus sur lui.")

p("Les fragments de Luynes qui flottent autour d'eux "
  "continuent de se dissoudre, un par un &mdash; le panneau de la "
  "boulangerie, le clocher, la fa&ccedil;ade de la biblioth&egrave;que &mdash; "
  "chacun emportant avec lui, dans sa disparition, un peu du "
  "quotidien que Darius avait toujours consid&eacute;r&eacute; comme "
  "acquis, immuable, trop banal pour m&eacute;riter qu'on s'y "
  "attache vraiment. Il comprend, en les regardant s'effacer, "
  "&agrave; quel point il aimait cette ville ordinaire bien plus "
  "qu'il ne se l'&eacute;tait jamais avou&eacute;.")

p("Sa voix ne sort plus d'un seul point de l'espace mais de "
  "partout &agrave; la fois, comme si le Non-lieu enti&egrave;re avait "
  "&eacute;t&eacute; transform&eacute;e en une bouche unique, et chaque syllabe "
  "fait vibrer le sol instable sous leurs pieds d'une "
  "fr&eacute;quence qui r&eacute;sonne directement dans leurs c&ocirc;tes, plus "
  "physique qu'un simple son ne devrait jamais pouvoir "
  "l'&ecirc;tre.")

p("Le b&acirc;ton, dans les mains de Darius, vibre d'une intensit&eacute; "
  "nouvelle, comme s'il reconnaissait enfin, apr&egrave;s des "
  "semaines &agrave; le tirer patiemment vers cette destination, la "
  "source m&ecirc;me de tout ce qu'il avait cherch&eacute; &agrave; localiser "
  "depuis la for&ecirc;t derri&egrave;re le coteau.")

p("Les d&eacute;chirures noires s'ouvrent plus largement et projettent "
  "vers eux des lambeaux de souvenirs vol&eacute;s &mdash; le visage d'une "
  "vieille femme qui hurle sans bruit, une main d'enfant qui "
  "se dissout en pixels avant d'atteindre la sienne, des "
  "fragments de phrases prononc&eacute;es par des dizaines "
  "d'habitants de Luynes au fil des d&eacute;cennies, tous ces "
  "mensonges n&eacute;cessaires recueillis un &agrave; un et maintenant "
  "recrach&eacute;s en vrac, comme une temp&ecirc;te de papier d&eacute;chir&eacute; qui "
  "coupe la peau &agrave; chaque passage.")

p("Clara, tout en poursuivant sa litanie, sent son propre "
  "corps commencer &agrave; s'effacer par endroits, ses mains "
  "devenant, une seconde, presque transparentes, avant "
  "qu'elle ne force sa voix &agrave; monter encore, refusant de se "
  "laisser dissoudre avant d'avoir prononc&eacute; le dernier nom "
  "de sa liste.")

p("Un fragment de voix, isol&eacute; du chaos ambiant, prononce "
  "distinctement le pr&eacute;nom &laquo;&nbsp;Miel&nbsp;&raquo; avant de se dissoudre, et "
  "Darius sent une col&egrave;re nouvelle monter en lui, plus froide "
  "que la peur, en comprenant que m&ecirc;me ce souvenir-l&agrave;, le "
  "plus ancien, le plus intime, fait d&eacute;sormais partie du "
  "stock que Kayden brasse sans aucun respect pour ce qu'il "
  "repr&eacute;sente vraiment.")

p("Alex, le premier, encaisse un coup invisible qui le jette au "
  "sol, une longue estafilade s'ouvrant sur son avant-bras, non "
  "pas de sang rouge mais de cette m&ecirc;me encre noire "
  "grouillante, comme si le Non-lieu, en le blessant, r&eacute;vélait "
  "&agrave; quel point la fronti&egrave;re entre leurs corps et ce monde "
  "s'&eacute;tait d&eacute;j&agrave; mise &agrave; c&eacute;der. Il se rel&egrave;ve en serrant les "
  "dents, empoigne un c&acirc;ble arrach&eacute; du plafond de code comme "
  "on empoignerait une barre de fer, et charge sans r&eacute;fl&eacute;chir, "
  "parce que c'est tout ce qu'il sait faire de mieux&nbsp;: avancer "
  "quand tout le monde recule.")

p("Clara, elle, ne bouge pas. Elle ferme les yeux au milieu du "
  "chaos, son carnet serr&eacute; contre sa poitrine, et se met &agrave; "
  "&eacute;num&eacute;rer, &agrave; voix haute, chaque nom qu'elle y a not&eacute; depuis "
  "deux ans &mdash; son p&egrave;re, l'oncle d'Alex, le pompier, la "
  "pianiste, Franck, Vasseur, Darius, Miel &mdash; une litanie qui "
  "ressemble &agrave; un sortil&egrave;ge parce que c'en est un, &agrave; sa "
  "mani&egrave;re&nbsp;: une contre-liste, une preuve que rien de ce que "
  "Kayden a pris n'a jamais vraiment disparu tant que quelqu'un "
  "continue de le nommer.")

p("Darius, encore &eacute;tourdi par la temp&ecirc;te de souvenirs vol&eacute;s "
  "qui continue de tourbillonner autour d'eux, sent le pon&ccedil;on "
  "chauffer contre sa paume, presque br&ucirc;lant cette fois, comme "
  "s'il r&eacute;agissait &agrave; la proximit&eacute; d'une source d'&eacute;nergie "
  "bien plus grande que tout ce qu'il avait pu ressentir "
  "jusqu'ici, m&ecirc;me dans les pires moments de la grotte ou de "
  "la possession.")

p("Alex, toujours arm&eacute; de son c&acirc;ble improvis&eacute;, se place entre "
  "la masse instable de Kayden et les deux autres, une "
  "posture purement instinctive, sans strat&eacute;gie r&eacute;elle "
  "derri&egrave;re, juste ce r&eacute;flexe ancien qui le pousse toujours "
  "&agrave; encaisser le premier coup pour laisser du temps &agrave; ceux "
  "qu'il aime.")

p("Darius avance seul vers le centre de la masse instable, le "
  "b&acirc;ton tendu devant lui comme un sourcier au-dessus d'une "
  "source enfin trouv&eacute;e, et sent, pour la premi&egrave;re fois "
  "depuis qu'il le porte, quelque chose lui r&eacute;pondre en "
  "retour &mdash; non pas une seule pr&eacute;sence, mais des dizaines, "
  "des centaines peut-&ecirc;tre, un chuchotement d'ancêtres "
  "anonymes qui ont tous, un jour, port&eacute; son pr&eacute;nom et "
  "affront&eacute; la m&ecirc;me machine sous une forme ou une autre&nbsp;: "
  "le laboureur du dix-huiti&egrave;me si&egrave;cle, le meunier de 1871, "
  "le jeune Darius de 1962, et lui, maintenant, le dernier "
  "maillon d'une cha&icirc;ne qu'il n'a jamais choisi de porter mais "
  "qui, ce soir, le porte en retour.")

p("Kayden se scinde, l'espace d'un instant, en deux "
  "silhouettes distinctes mais reli&eacute;es par des filaments "
  "sombres et pulsants &mdash; l'une gardant encore la forme "
  "reconnaissable d'un adolescent de dix-neuf ans, le "
  "visage tordu par une souffrance ancienne, l'autre "
  "d&eacute;j&agrave; presque enti&egrave;rement architecture, des lignes de "
  "code visibles &agrave; travers une peau qui n'en est plus "
  "vraiment une, comme un fichier corrompu tentant "
  "d&eacute;sesp&eacute;r&eacute;ment de s'afficher correctement sans jamais "
  "y parvenir tout &agrave; fait.")

name("KAYDEN")
p("&laquo;&nbsp;Tu crois que &ccedil;a va suffire, ton b&acirc;ton, tes "
  "fant&ocirc;mes de laboureurs morts depuis des si&egrave;cles ? "
  "J'ai attendu plus longtemps que toi n'as m&ecirc;me v&eacute;cu, "
  "Darius. J'ai regard&eacute; mon p&egrave;re vieillir et mourir en "
  "esp&eacute;rant que quelqu'un, un jour, viendrait finir ce "
  "qu'il avait commenc&eacute;. Et c'est toi qu'on m'envoie. Un "
  "gamin avec un b&acirc;ton.&nbsp;&raquo;")

p("Le sol du Non-lieu se fissure davantage sous leurs pieds, "
  "r&eacute;v&eacute;lant, dans les craquelures, non pas du vide mais "
  "des fragments d'autres moments de la vie de Darius "
  "&mdash; son septi&egrave;me anniversaire, un dimanche pluvieux chez "
  "sa grand-m&egrave;re, le jour o&ugrave; Miel &eacute;tait rentr&eacute; couvert de "
  "boue apr&egrave;s une fugue dans les vignes &mdash; comme si "
  "l'affrontement lui-m&ecirc;me menaçait de dissoudre, en plus "
  "du pr&eacute;sent, jusqu'aux fondations les plus intimes de sa "
  "propre m&eacute;moire.")

name("CLARA")
p("&laquo;&nbsp;Darius, regarde pas &ccedil;a, regarde-le LUI, pas ce "
  "qu'il te montre ! C'est un pi&egrave;ge, il essaie de "
  "t'&eacute;parpiller comme il l'est, lui !&nbsp;&raquo;")

p("Darius ferme les yeux une fraction de seconde, "
  "puisant dans le b&acirc;ton une force qui ne lui appartient "
  "pas enti&egrave;rement, et rouvre les paupi&egrave;res avec une "
  "clart&eacute; nouvelle, refusant enfin de se laisser distraire "
  "par les souvenirs projet&eacute;s en offrande empoisonn&eacute;e, "
  "concentrant tout son &ecirc;tre sur la silhouette double de "
  "Kayden, mi-gar&ccedil;on mi-architecture, oscillant devant "
  "lui dans la lumi&egrave;re bleue mourante.")

p("Alex, encaissant un fouet de code noir en pleine "
  "poitrine, tombe &agrave; genoux mais ne l&acirc;che pas son c&acirc;ble, "
  "hurlant &agrave; travers la douleur des mots qui ne sont "
  "presque plus des mots, juste une d&eacute;termination pure "
  "traduite en son, tandis que Clara, prot&eacute;g&eacute;e derri&egrave;re "
  "lui, serre son carnet contre sa poitrine comme un "
  "bouclier dont elle ignore encore la vraie nature.")

S.append(rule())
S.append(PageBreak())
p("Le carnet de Clara, contre toute attente, s'ouvre "
  "seul entre ses mains tremblantes, ses pages se "
  "tournant d'elles-m&ecirc;mes dans un froissement sec, "
  "jusqu'&agrave; une page vierge qui se remplit, sous ses yeux, "
  "d'une &eacute;criture qui n'est ni la sienne ni celle d'aucun "
  "d'entre eux &mdash; des lignes anciennes, dat&eacute;es de si&egrave;cles "
  "diff&eacute;rents, sign&eacute;es de noms qu'elle ne conna&icirc;t pas mais "
  "qui r&eacute;sonnent, tous, avec la m&ecirc;me cadence famili&egrave;re "
  "que le pr&eacute;nom de Darius.")

name("CLARA")
p("&laquo;&nbsp;Darius ! Le carnet, il &eacute;crit tout seul, c'est "
  "eux, c'est tous les autres qui ont port&eacute; &ccedil;a avant toi, "
  "ils sont avec nous, l&agrave;, maintenant, &agrave; travers &ccedil;a !&nbsp;&raquo;")

p("Cette r&eacute;v&eacute;lation traverse Darius comme un courant "
  "&eacute;lectrique, cette certitude soudaine qu'il n'est "
  "vraiment pas seul, jamais, m&ecirc;me quand tout dans le "
  "Non-lieu semble con&ccedil;u pour le convaincre du contraire, "
  "et il sent le b&acirc;ton vibrer plus fort encore entre ses "
  "mains, comme s'il puisait, directement dans ce carnet "
  "tenu par sa meilleure amie, une force compl&eacute;mentaire "
  "&agrave; celle d&eacute;j&agrave; canalis&eacute;e depuis la lign&eacute;e.")

p("Le sol du Non-lieu tremble une derni&egrave;re fois, comme pris "
  "d'une h&eacute;sitation, avant que les deux moiti&eacute;s de Kayden ne "
  "cessent, pendant une fraction de seconde suspendue, de "
  "lutter l'une contre l'autre, offrant &agrave; Darius la seule "
  "ouverture qu'il obtiendra jamais.")

p("Clara et Alex, derri&egrave;re lui, sentent tous les deux, au "
  "m&ecirc;me instant, que quelque chose a chang&eacute; dans la posture "
  "de Darius &mdash; qu'il ne marche plus comme un adolescent "
  "terrifi&eacute; cherchant &agrave; survivre, mais comme quelqu'un qui "
  "vient enfin de comprendre &agrave; quoi il sert vraiment, ici, ce "
  "soir, depuis le tout premier jeudi de pluie.")

name("DARIUS")
p("&laquo;&nbsp;Tu veux une derni&egrave;re page, Kayden ? Tiens. La voil&agrave;. "
  "Page 404&nbsp;: on ne t'oublie pas. On te pardonne pas non "
  "plus. Mais on arr&ecirc;te de te nourrir.&nbsp;&raquo;")

p("Le pon&ccedil;on grav&eacute; d'un K br&ucirc;le maintenant contre sa "
  "paume au point de lui arracher une grimace, comme s'il "
  "refusait, une derni&egrave;re fois, de laisser Darius achever ce "
  "qu'il s'appr&ecirc;te &agrave; faire &mdash; ou peut-&ecirc;tre, pense Darius dans "
  "un &eacute;clair confus, comme s'il l'y encourageait de toutes "
  "ses forces, l&agrave; o&ugrave; Kayden lui-m&ecirc;me n'en avait plus la "
  "force.")

p("Sa voix, en pronon&ccedil;ant ces mots, ne tremble pas, alors "
  "m&ecirc;me que tout le reste de lui tremble encore &mdash; les "
  "mains, les genoux, le souffle court &mdash; comme si cette phrase "
  "pr&eacute;cise avait attendu, quelque part au fond de lui, tout "
  "ce temps pour trouver enfin le bon moment de se dire, "
  "port&eacute;e par une certitude plus ancienne que sa propre "
  "peur, une certitude qui remonte, pense-t-il confus&eacute;ment, "
  "de bien plus loin que sa seule vie &agrave; lui.")

p("Kayden, dans sa forme fractur&eacute;e, semble hesiter une "
  "derni&egrave;re fois, ses deux moiti&eacute;s tremblant l'une contre "
  "l'autre comme deux aimants qui refuseraient, au dernier "
  "moment, de se repousser tout &agrave; fait, et Darius comprend, "
  "&agrave; cet instant pr&eacute;cis, qu'une partie de lui, quelque part "
  "sous trente ans de rage accumul&eacute;e, esp&egrave;re encore, "
  "faiblement, qu'on lui tende une main plut&ocirc;t qu'un jugement.")

p("Il pense, une fraction de seconde, &agrave; Franck, &agrave; Vasseur "
  "p&egrave;re, &agrave; tous ces adultes qui ont cru bien faire en "
  "cachant une v&eacute;rit&eacute; trop lourde &agrave; porter, et se jure, "
  "silencieusement, de ne jamais devenir quelqu'un qui choisit "
  "la facilit&eacute; d'un mensonge plut&ocirc;t que le poids d'une "
  "v&eacute;rit&eacute;, m&ecirc;me si cette v&eacute;rit&eacute; doit un jour lui co&ucirc;ter "
  "aussi cher que ce soir semble sur le point de lui co&ucirc;ter.")

p("Clara et Alex, sans se concerter, s'avancent chacun d'un "
  "pas pour se placer &agrave; ses c&ocirc;t&eacute;s, formant, sans le savoir, "
  "exactement la m&ecirc;me ligne que trois amis avaient d&ucirc; former "
  "un jour, quelque part dans les si&egrave;cles pr&eacute;c&eacute;dents, autour "
  "d'un autre Darius affrontant la m&ecirc;me question, la m&ecirc;me "
  "nuit, sous une forme diff&eacute;rente mais avec exactement le "
  "m&ecirc;me poids au fond de la poitrine.")

p("Clara termine sa litanie sur un dernier nom, le sien, "
  "prononc&eacute; d'une voix qui tremble &agrave; peine, et Alex, toujours "
  "&agrave; genoux, l&egrave;ve les yeux vers Darius avec une confiance "
  "totale, sans une once d'h&eacute;sitation, comme s'il avait "
  "toujours su que ce moment pr&eacute;cis finirait par arriver, "
  "d'une mani&egrave;re ou d'une autre.")

p("Il plante le b&acirc;ton dans le sol du Non-lieu, qui n'est pas "
  "un sol mais c&egrave;de comme s'il en &eacute;tait un, et de la pointe "
  "s'&eacute;chappe une onde de lumi&egrave;re blanche qui remonte le long "
  "de chaque d&eacute;chirure noire, les refermant une &agrave; une comme "
  "des plaies qu'on suture, pendant que Clara termine sa "
  "litanie de noms et qu'Alex, &agrave; genoux, presse sa main "
  "ensanglant&eacute;e d'encre contre le sol pour ancrer, physiquement, "
  "un dernier point fixe dans ce monde qui refuse de tenir "
  "debout.")

p("Le pon&ccedil;on, dans la main gauche de Darius, r&eacute;pond &agrave; la "
  "lumi&egrave;re du b&acirc;ton en projetant, autour d'eux trois, un "
  "cercle de lignes de code fig&eacute;es, une sorte de bouclier "
  "improvis&eacute; qui repousse, pour quelques secondes pr&eacute;cieuses, "
  "les derni&egrave;res d&eacute;chirures noires encore actives.")

p("La masse de Kayden se convulse, se scinde en deux formes "
  "distinctes &mdash; le gar&ccedil;on en blouse blanche d'un c&ocirc;t&eacute;, "
  "l'architecture de c&acirc;bles de l'autre &mdash; et pour la premi&egrave;re "
  "fois depuis trente ans, ces deux moiti&eacute;s de lui-m&ecirc;me se "
  "regardent l'une l'autre, incapables de se reconna&icirc;tre.")

S.append(Paragraph("KAYDEN (voix fractur&eacute;e, presque humaine)", cn))
p("&laquo;&nbsp;Je voulais juste... que &ccedil;a compte. Que le travail de "
  "mon p&egrave;re ait servi &agrave; quelque chose. Je voulais pas devenir "
  "&ccedil;a.&nbsp;&raquo;")

name("DARIUS")
p("&laquo;&nbsp;Alors arr&ecirc;te. Il est encore temps d'arr&ecirc;ter.&nbsp;&raquo;")

p("La lumi&egrave;re blanche atteint le c&oelig;ur de la masse et l'ensemble "
  "explose, non pas en une d&eacute;flagration de feu, mais en une "
  "onde de silence si totale qu'elle aspire jusqu'au bruit de "
  "leurs propres respirations, avant que tout &mdash; le ciel stri&eacute;, "
  "les lambeaux de Luynes, les deux moiti&eacute;s de Kayden &mdash; ne "
  "se referme d'un coup, comme une paupi&egrave;re, sur un noir "
  "absolu et sans fond.")

p("Dans ce noir absolu, avant que quoi que ce soit d'autre ne "
  "se produise, Darius sent encore, une derni&egrave;re fois, la main "
  "de Clara serrer la sienne et celle d'Alex de l'autre c&ocirc;t&eacute;, "
  "trois points de contact minuscules et t&ecirc;tus qui refusent "
  "de se laisser dissoudre m&ecirc;me quand tout le reste de "
  "l'univers, autour d'eux, semble avoir cess&eacute; d'exister.")

p("Quelque part, dans ce noir, une derni&egrave;re pens&eacute;e traverse "
  "Darius avant que tout ne s'efface&nbsp;: que gagner, ici, ne "
  "ressemble en rien &agrave; ce qu'il avait imagin&eacute; &mdash; pas de "
  "triomphe, pas de lumi&egrave;re dor&eacute;e, juste le soulagement "
  "&eacute;puis&eacute; d'avoir tenu bon jusqu'au bout, &agrave; trois, sans "
  "avoir l&acirc;ch&eacute; la main de personne.")

p("Clara, tout pr&egrave;s de lui, murmure une derni&egrave;re fois le nom "
  "de son propre p&egrave;re, comme un point final pos&eacute; sur sa "
  "longue litanie, et Alex, encore &agrave; genoux, presse son front "
  "contre le sol instable, &eacute;puis&eacute; mais toujours conscient, "
  "refusant de l&acirc;cher ce dernier point d'ancrage m&ecirc;me quand "
  "tout, autour d'eux, semble avoir renonc&eacute; &agrave; tenir debout "
  "plus longtemps.")

p("Darius se r&eacute;veille seul, dans sa chambre, un dimanche matin "
  "ordinaire, la lumi&egrave;re d'octobre tombant normalement par la "
  "fen&ecirc;tre, sans qu'aucun souvenir clair ne relie la nuit "
  "pr&eacute;c&eacute;dente &agrave; ce r&eacute;veil-l&agrave;. Il reste immobile un long "
  "moment, cherchant dans sa m&eacute;moire la derni&egrave;re chose "
  "certaine, et ne trouve que des &eacute;clats &mdash; une lumi&egrave;re "
  "blanche, une main dans la sienne, une phrase qu'il a "
  "prononc&eacute;e sans se souvenir des mots exacts.")

p("Il v&eacute;rifie son t&eacute;l&eacute;phone, esp&eacute;rant y trouver une trace "
  "&mdash; un message, une photo, n'importe quoi &mdash; mais l'historique "
  "de conversation avec Clara et Alex s'arr&ecirc;te net trois jours "
  "plus t&ocirc;t, sur un &eacute;change ordinaire &agrave; propos d'un devoir "
  "d'histoire, comme si les semaines qui ont suivi n'avaient "
  "tout simplement jamais &eacute;t&eacute; envoy&eacute;es dans le monde r&eacute;el.")

p("Sur son bureau, pourtant, trois objets attendent, aussi "
  "r&eacute;els que sa propre main qui les touche&nbsp;: le pon&ccedil;on "
  "grav&eacute; d'un K, le b&acirc;ton us&eacute; par des si&egrave;cles de mains "
  "diff&eacute;rentes, et un carnet &agrave; spirale qui n'est pas le sien, "
  "couvert d'une &eacute;criture serr&eacute;e qu'il reconna&icirc;t "
  "imm&eacute;diatement comme celle de Clara.")

p("Le calendrier accroch&eacute; au mur indique la bonne date, un "
  "dimanche d'octobre parfaitement ordinaire, sans aucune "
  "case coch&eacute;e pour marquer les semaines qu'il a pourtant "
  "l'impression d'avoir v&eacute;cues, comme si le temps lui-m&ecirc;me "
  "avait accept&eacute; de collaborer avec cet oubli g&eacute;n&eacute;ral.")

p("Il enfile ses v&ecirc;tements de la veille, retrouv&eacute;s pli&eacute;s "
  "normalement sur sa chaise alors qu'il ne se souvient pas "
  "de les y avoir pos&eacute;s, et sort de sa chambre le pas h&eacute;sitant, "
  "comme quelqu'un qui redoute de d&eacute;couvrir, &agrave; chaque coin "
  "de couloir, la preuve que le monde entier a chang&eacute; pendant "
  "son sommeil.")

p("Il descend, le c&oelig;ur battant, et trouve sa m&egrave;re dans la "
  "cuisine, parfaitement normale, lui demandant s'il a bien "
  "dormi d'une voix qui n'a plus la moindre trace d'inqui&eacute;tude "
  "&mdash; comme si les semaines de fugue, de rendez-vous chez le "
  "psychologue, de nuits blanches, n'avaient tout simplement "
  "jamais exist&eacute;. Sur la place du march&eacute;, plus tard, la vitrine "
  "du bar-tabac ne contient qu'un vieux flipper hors service et "
  "des affiches jaunies pour le loto. Aucune machine. Aucun "
  "verre d&eacute;poli. Aucune trace.")

p("Il erre encore un moment sur la place, incapable de rentrer "
  "tout de suite chez lui, cherchant du regard le moindre "
  "d&eacute;tail qui pourrait prouver qu'il n'a pas simplement r&ecirc;v&eacute; "
  "des semaines enti&egrave;res &mdash; un panneau administratif d&eacute;fra&icirc;chi, "
  "une odeur d'ozone qui persisterait, n'importe quoi &mdash; sans "
  "rien trouver d'autre qu'une place ordinaire, tranquille, "
  "compl&egrave;tement indiff&eacute;rente &agrave; ce qui a bien pu s'y jouer.")

p("Il retrouve Clara &agrave; la sortie de chez elle, qui lui sourit "
  "normalement, lui parle d'un devoir de math pour lundi, "
  "d'une s&eacute;rie qu'elle a commenc&eacute; &agrave; regarder, sans la moindre "
  "hesitation dans les yeux, sans le moindre signe qu'elle se "
  "souvient d'avoir jamais r&eacute;cit&eacute; une liste de noms au milieu "
  "d'un monde en train de se d&eacute;chirer.")

name("DARIUS")
p("&laquo;&nbsp;Clara. Miel-Ambre. &Ccedil;a te dit quelque chose ?&nbsp;&raquo;")

p("Il repense, une seconde, &agrave; la nuit de la grotte, &agrave; Kayden "
  "d&eacute;j&agrave; d&eacute;fait une premi&egrave;re fois derri&egrave;re ses propres yeux, "
  "et se demande si cette fois, dans le Non-lieu, la d&eacute;faite "
  "a &eacute;t&eacute; d&eacute;finitive, ou si quelque part, dans un recoin qu'ils "
  "n'ont pas vu, une derni&egrave;re braise attend encore, patiente, "
  "son heure pour se rallumer.")

p("Le silence de la maison, autour de lui, lui semble soudain "
  "presque hostile, trop parfait, trop propre, comme un "
  "d&eacute;cor de th&eacute;&acirc;tre mont&eacute; en h&acirc;te pour lui faire croire "
  "qu'aucune sc&egrave;ne dramatique ne s'est jamais jou&eacute;e dans ces "
  "murs, et il se surprend &agrave; toucher chaque objet familier de "
  "sa chambre, un &agrave; un, pour v&eacute;rifier qu'ils sont bien r&eacute;els, "
  "et non de simples accessoires plac&eacute;s l&agrave; pour parfaire "
  "l'illusion.")

p("Une camionnette de livraison passe sur la place, indiff&eacute;rente, "
  "et Darius la suit des yeux une seconde, presque envieux "
  "du conducteur qui traverse cette matin&eacute;e sans le moindre "
  "poids sur les &eacute;paules, sans savoir &agrave; quel point une "
  "conversation en train de se d&eacute;rouler &agrave; quelques m&egrave;tres "
  "de lui pourrait, selon son issue, changer le reste de "
  "plusieurs vies enti&egrave;res.")

p("Il guette son visage avec une intensit&eacute; presque douloureuse, "
  "cherchant le moindre signe de reconnaissance, la plus "
  "petite fissure dans cette normalit&eacute; parfaite qui lui donne "
  "l'impression, absurde, de parler &agrave; une inconnue qui "
  "porterait le visage exact de sa meilleure amie, avec les "
  "m&ecirc;mes gestes, la m&ecirc;me voix, mais aucune des ann&eacute;es "
  "partag&eacute;es derri&egrave;re les yeux.")

p("Elle fronce les sourcils, sinc&egrave;rement perplexe, et lui "
  "demande de quoi il parle, avec une innocence si totale que "
  "Darius sent le sol se d&eacute;rober sous lui une seconde fois, "
  "d'une mani&egrave;re bien plus douloureuse que tout ce que le "
  "Non-lieu avait pu lui infliger.")

p("Il pense &agrave; retourner voir Alex, esp&eacute;rant, sans trop y "
  "croire, que la m&eacute;moire aurait pu survivre chez lui plut&ocirc;t "
  "que chez Clara, avant de se raviser presque aussit&ocirc;t &mdash; s'il "
  "d&eacute;boule chez ses deux amis en leur parlant d'une machine, "
  "d'un Non-lieu et d'un gar&ccedil;on mort en 1994, l'un comme "
  "l'autre finira par appeler ses parents, inqui&eacute;t&eacute;, et Darius "
  "n'a aucune envie de retourner chez le psychologue pour "
  "une histoire que personne, cette fois, ne pourra jamais "
  "confirmer.")

p("Il ne dit rien de plus, sur le moment, incapable de trouver "
  "les mots pour expliquer &agrave; quel point ce simple froncement "
  "de sourcils, cette innocence totale, lui fait plus mal que "
  "n'importe quelle blessure encaiss&eacute;e dans le Non-lieu &mdash; "
  "parce que cette fois, ce n'est pas un mensonge qu'on lui "
  "raconte. C'est un vide, poli, absolu, sans personne de "
  "l'autre c&ocirc;t&eacute; pour porter la faute.")

p("Il retourne s'asseoir sur le trottoir, en face de la place "
  "vide, et reste l&agrave; de longues minutes, la t&ecirc;te dans les "
  "mains, essayant de comprendre comment il est cens&eacute; "
  "continuer &agrave; vivre normalement dans une ville o&ugrave; il est, "
  "d&eacute;sormais, le seul &agrave; se souvenir de tout ce qui compte "
  "vraiment.")

p("Il descend finalement, bien plus tard dans la matin&eacute;e "
  "qu'il ne l'aurait normalement fait un dimanche, et croise, "
  "en chemin, le reflet fatigu&eacute; de son propre visage dans le "
  "miroir de l'entr&eacute;e &mdash; les m&ecirc;mes traits que toujours, sans "
  "une seule marque visible de ce qu'il vient de traverser, "
  "comme si son corps, lui aussi, avait d&eacute;cid&eacute; de garder le "
  "secret encore un peu, le temps qu'il trouve la force de le "
  "porter seul.")

p("Il pense un instant &agrave; abandonner, &agrave; se dire que c'&eacute;tait "
  "peut-&ecirc;tre pr&eacute;f&eacute;rable ainsi, que Clara et Alex m&eacute;ritent "
  "peut-&ecirc;tre de vivre sans le poids de tout ce qu'ils ont "
  "travers&eacute; ensemble &mdash; avant de rejeter cette id&eacute;e presque "
  "aussit&ocirc;t, incapable d'accepter de porter tout &ccedil;a compl&egrave;tement "
  "seul, m&ecirc;me si &ccedil;a devait leur &eacute;pargner une douleur.")

p("Il ne panique pas, ou plut&ocirc;t il refuse de se laisser aller "
  "&agrave; la panique, parce qu'une part de lui, entra&icirc;n&eacute;e par des "
  "semaines &agrave; g&eacute;rer l'impossible, sait d&eacute;j&agrave; qu'il a en poche "
  "trois objets qui n'ont aucune raison logique d'exister si "
  "tout &ccedil;a n'&eacute;tait qu'un r&ecirc;ve. Il montre &agrave; Clara le carnet, "
  "son &eacute;criture &agrave; elle, page apr&egrave;s page, les noms, les "
  "dates, le sien &eacute;crit &agrave; c&ocirc;t&eacute; du sien des dizaines de fois.")

p("Un voisin passe dans l'escalier, salue Clara d'un signe de "
  "t&ecirc;te machinal, sans se douter une seconde de ce qui se "
  "joue sur ces marches, et Darius attend qu'il ait disparu "
  "avant de reprendre, la voix plus basse encore, comme si "
  "cette conversation-l&agrave; m&eacute;ritait un silence particulier "
  "autour d'elle.")

p("Darius s'assoit &agrave; c&ocirc;t&eacute; d'elle sur les marches de son "
  "immeuble, l&agrave; m&ecirc;me o&ugrave; elle lui avait montr&eacute; ce carnet pour "
  "la premi&egrave;re fois des mois plus t&ocirc;t, et attend, sans "
  "prononcer un mot de plus, laissant le silence faire le "
  "travail qu'aucune explication pr&eacute;cipit&eacute;e ne pourrait faire "
  "&agrave; sa place.")

p("Elle feuillette d'abord par politesse, presque g&ecirc;n&eacute;e, "
  "avant qu'un d&eacute;tail n'accroche son regard &mdash; une phrase, "
  "&eacute;crite de sa propre main, qu'elle ne se souvient absolument "
  "pas d'avoir &eacute;crite : &laquo;&nbsp;p'pa a quarante-deux ans depuis six "
  "mois. il en a l'air d'avoir cinquante.&nbsp;&raquo; Une phrase trop "
  "pr&eacute;cise, trop juste, pour &ecirc;tre invent&eacute;e par quelqu'un "
  "d'autre.")

p("Elle p&acirc;lit. Pas d'un coup, comme dans les films, mais "
  "lentement, par couches, comme une personne qui sent une "
  "v&eacute;rit&eacute; remonter des profondeurs sans encore r&eacute;ussir &agrave; la "
  "nommer.")

name("CLARA")
p("&laquo;&nbsp;J'ai &eacute;crit &ccedil;a. Je me souviens pas de l'avoir &eacute;crit, "
  "mais je sais que c'est mon &eacute;criture, et je sais que c'est "
  "vrai. Papa a vraiment cet &acirc;ge-l&agrave;. Comment... comment tu "
  "peux avoir &ccedil;a si c'est moi qui l'ai &eacute;crit et que je m'en "
  "souviens pas ?&nbsp;&raquo;")

p("Clara referme le carnet, le rouvre, le referme encore, "
  "incapable de se d&eacute;cider entre la peur de ce que &ccedil;a pourrait "
  "signifier et une forme d'excitation malgr&eacute; elle, comme "
  "si une part d'elle avait toujours su qu'une explication de "
  "ce genre finirait par se pr&eacute;senter un jour, m&ecirc;me sans "
  "pouvoir l'anticiper pr&eacute;cis&eacute;ment.")

p("Ils retrouvent Alex une heure plus tard, sur le terrain de "
  "foot du coll&egrave;ge, et Darius, sans un mot d'explication, "
  "remonte la manche de son ami jusqu'au coude &mdash; l&agrave; o&ugrave;, "
  "dans le Non-lieu, une estafilade noire s'&eacute;tait ouverte sur "
  "son avant-bras. La peau est intacte. Mais une fine "
  "cicatrice blanche, ancienne en apparence, d'au moins "
  "plusieurs mois, trace exactement le m&ecirc;me chemin.")

name("ALEX")
p("&laquo;&nbsp;&Ccedil;a, j'ai jamais vu &ccedil;a avant. Enfin si. Non. J'sais "
  "plus. Pourquoi j'ai l'impression de savoir d'o&ugrave; &ccedil;a vient "
  "sans savoir d'o&ugrave; &ccedil;a vient ?&nbsp;&raquo;")

p("Clara, avant qu'il ne commence vraiment son r&eacute;cit, sort de "
  "sa poche le vieux carnet retrouv&eacute; sur le bureau de Darius, "
  "le pose entre eux trois sur l'herbe, ouvert &agrave; la page o&ugrave; "
  "figure la phrase sur l'&acirc;ge de son p&egrave;re, comme une pi&egrave;ce &agrave; "
  "conviction qu'elle ne comprend pas encore compl&egrave;tement "
  "mais dont elle sent, dans ses tripes, l'importance "
  "&eacute;crasante.")

p("Le soleil commence &agrave; descendre derri&egrave;re les arbres du "
  "terrain de foot, teintant le gazon d'une lumi&egrave;re orang&eacute;e "
  "presque irr&eacute;elle, et Darius se dit, en regardant ses deux "
  "amis attendre son r&eacute;cit avec une patience qu'ils ne "
  "comprennent pas encore vraiment eux-m&ecirc;mes, que cette "
  "sc&egrave;ne-l&agrave; aussi, un jour, finira peut-&ecirc;tre par ressembler &agrave; "
  "un souvenir qu'on n'explique plus, juste une confiance "
  "qu'on garde sans en conna&icirc;tre l'origine exacte.")

p("Il passe un doigt sur la cicatrice, l'air perdu, avant de "
  "relever les yeux vers Darius avec une expression que ce "
  "dernier ne lui a encore jamais vue &mdash; un m&eacute;lange de "
  "confusion et de confiance aveugle, comme si une partie "
  "tr&egrave;s ancienne de lui savait d&eacute;j&agrave; que tout ce que Darius "
  "s'appr&ecirc;te &agrave; raconter sera vrai, m&ecirc;me avant d'en entendre "
  "le premier mot.")

p("Ce soir-l&agrave;, tous les trois assis sur le rebord du terrain, "
  "Darius leur raconte tout, depuis le d&eacute;but, la vitrine sous "
  "la pluie, Miel, Franck, Kayden, la grotte, le b&acirc;ton, la "
  "biblioth&egrave;que, le Non-lieu en flammes &mdash; et &agrave; mesure qu'il "
  "parle, il voit, sur leurs deux visages, quelque chose "
  "remonter lentement &agrave; la surface, pas des souvenirs nets, "
  "pas encore, mais des &eacute;chos, des frissons de reconnaissance "
  "&agrave; chaque nom prononc&eacute;, comme des graines plant&eacute;es dans "
  "une terre qui avait oubli&eacute; qu'elle pouvait pousser.")

name("CLARA")
p("&laquo;&nbsp;Je me souviens pas. Mais je te crois. C'est bizarre &agrave; "
  "dire, mais je te crois compl&egrave;tement, comme si une partie "
  "de moi savait avant que tu finisses ta phrase ce que t'allais "
  "dire ensuite.&nbsp;&raquo;")

p("Darius range le pon&ccedil;on, le b&acirc;ton et le carnet dans une "
  "bo&icirc;te en bois qu'il cache au fond de son placard, non pas "
  "pour les oublier, mais pour se rappeler, chaque fois qu'il "
  "l'ouvrira, que la m&eacute;moire n'est peut-&ecirc;tre pas qu'une affaire "
  "de souvenirs pr&eacute;cis &mdash; que parfois, elle survit autrement, "
  "dans une cicatrice, dans une phrase &eacute;crite sans s'en "
  "souvenir, dans la confiance aveugle qu'on accorde &agrave; "
  "quelqu'un sans savoir pourquoi.")

p("Les semaines suivantes, ils recommencent, presque timidement "
  "au d&eacute;but, &agrave; se retrouver les trois apr&egrave;s les cours, sans "
  "jamais tout &agrave; fait retrouver la m&eacute;moire compl&egrave;te de ce "
  "qu'ils ont v&eacute;cu, mais en reconstruisant, patiemment, une "
  "confiance qui semble puiser sa force ailleurs que dans les "
  "souvenirs pr&eacute;cis &mdash; dans quelque chose de plus profond, "
  "peut-&ecirc;tre, que la m&eacute;moire elle-m&ecirc;me.")

p("Dehors, le ciel de Luynes reste bleu, sans une seule strie, "
  "et il pleuvra normalement la semaine suivante, comme "
  "avant, comme toujours &mdash; mais Darius, d&eacute;sormais, sait "
  "&eacute;couter la diff&eacute;rence entre une pluie qui tombe parce "
  "que c'est la saison, et un monde qui a simplement d&eacute;cid&eacute;, "
  "un peu plus fort qu'avant, de continuer &agrave; se souvenir.")

p("Franck, un dimanche suivant, vient enfin les chercher tous "
  "les trois pour d&eacute;jeuner &agrave; Tours, une premi&egrave;re depuis des "
  "ann&eacute;es, et pendant le trajet en voiture, Darius surprend "
  "son p&egrave;re &agrave; lui jeter, dans le r&eacute;troviseur, un regard "
  "qu'il ne saurait pas nommer pr&eacute;cis&eacute;ment, mais qui "
  "ressemble, pour la premi&egrave;re fois depuis tr&egrave;s longtemps, "
  "&agrave; de la fiert&eacute; sans arri&egrave;re-pens&eacute;e.")

p("Le restaurant choisi par Franck, une petite cr&ecirc;perie "
  "nich&eacute;e dans une ruelle pav&eacute;e du vieux Tours, "
  "d&eacute;gage une chaleur accueillante qui contraste "
  "agr&eacute;ablement avec le froid ext&eacute;rieur, et les quatre "
  "convives s'installent autour d'une table en bois "
  "massif, pr&egrave;s d'une chemin&eacute;e dont les flammes "
  "projettent des ombres dansantes sur les murs de "
  "pierre apparente.")

name("FRANCK")
p("&laquo;&nbsp;Prenez ce que vous voulez, c'est moi qui "
  "invite. Vous avez bien m&eacute;rit&eacute; un bon repas, tous les "
  "trois, apr&egrave;s tout &ccedil;a.&nbsp;&raquo;")

p("Alex, fid&egrave;le &agrave; son app&eacute;tit l&eacute;gendaire, commande "
  "imm&eacute;diatement la cr&ecirc;pe la plus garnie de la carte, "
  "d&eacute;clenchant un fou rire g&eacute;n&eacute;ral quand le serveur, "
  "impassible, lui demande s'il souhaite vraiment "
  "ajouter &agrave; la fois du fromage, du jambon, un &oelig;uf et "
  "de la cr&egrave;me fra&icirc;che sur la m&ecirc;me galette.")

name("ALEX")
p("&laquo;&nbsp;&Ccedil;a fait onze jours que j'ai combattu une "
  "entit&eacute; myst&eacute;rieuse dans une dimension parall&egrave;le, "
  "monsieur. Je crois que j'ai gagn&eacute; le droit &agrave; toutes "
  "les garnitures possibles.&nbsp;&raquo;")

p("Cette remarque, murmur&eacute;e assez bas pour que seuls "
  "Clara et Darius l'entendent vraiment, d&eacute;clenche "
  "chez les trois amis un fou rire incontr&ocirc;lable, ce "
  "genre de rire lib&eacute;rateur qui na&icirc;t souvent, "
  "paradoxalement, dans les moments suivant "
  "imm&eacute;diatement une tension extr&ecirc;me, comme si le "
  "corps avait besoin d'&eacute;vacuer d'un coup toute "
  "l'adr&eacute;naline accumul&eacute;e.")

p("Franck, ne comprenant pas la plaisanterie mais "
  "ravi de voir son fils rire aussi franchement apr&egrave;s "
  "des semaines de tension visible, se contente de "
  "sourire avec eux, savourant ce moment simple sans "
  "chercher &agrave; en percer tous les myst&egrave;res.")

name("FRANCK")
p("&laquo;&nbsp;J'sais pas ce qui vous fait rire comme &ccedil;a, mais "
  "&ccedil;a fait plaisir &agrave; voir. &Ccedil;a faisait longtemps que "
  "j'avais pas vu Darius rire comme &ccedil;a, sinc&egrave;rement, "
  "sans retenue.&nbsp;&raquo;")

p("Le repas se poursuit dans une ambiance l&eacute;g&egrave;re et "
  "chaleureuse, Franck posant des questions "
  "maladroites mais sinc&egrave;res sur leurs cours, leurs "
  "passions respectives, cette curiosit&eacute; nouvelle "
  "envers la vie de son fils repr&eacute;sentant, pour Darius, "
  "un cadeau bien plus pr&eacute;cieux que n'importe quel "
  "repas gastronomique, la simple sensation d'&ecirc;tre "
  "enfin vraiment vu par son p&egrave;re.")

p("En sortant du restaurant, alors que le soleil "
  "hivernal perce timidement entre deux nuages, "
  "&eacute;clairant les fa&ccedil;ades m&eacute;di&eacute;vales de la vieille ville "
  "d'une lumi&egrave;re dor&eacute;e presque irr&eacute;elle, Darius sent, "
  "pour la premi&egrave;re fois depuis des mois, une paix "
  "authentique s'installer en lui, la certitude fragile "
  "mais r&eacute;elle que malgr&eacute; tout ce qu'il a travers&eacute; et "
  "tout ce qui reste encore &agrave; comprendre, il n'est plus "
  "seul face &agrave; l'avenir.")

p("Ils flânent encore un moment dans les ruelles "
  "pav&eacute;es avant de reprendre la voiture, s'arr&ecirc;tant "
  "devant la vitrine d'un antiquaire o&ugrave; Clara s'attarde "
  "longuement devant une collection de vieux carnets "
  "reli&eacute;s cuir, dont l'un, particuli&egrave;rement us&eacute;, "
  "attire son attention par une reliure presque "
  "identique &agrave; celle du carnet qu'elle poss&egrave;de "
  "d&eacute;j&agrave;.")

name("CLARA")
p("&laquo;&nbsp;Regardez celui-l&agrave;, il ressemble &eacute;norm&eacute;ment au "
  "mien. &Ccedil;a me fait tout dr&ocirc;le de penser que des "
  "centaines de carnets comme &ccedil;a existent peut-&ecirc;tre "
  "quelque part, chacun appartenant &agrave; un t&eacute;moin "
  "diff&eacute;rent d'une histoire similaire &agrave; la n&ocirc;tre, "
  "&eacute;parpill&eacute;s dans des greniers et des brocantes "
  "partout en France.&nbsp;&raquo;")

p("Franck, amus&eacute; par cette r&eacute;flexion presque "
  "philosophique de la jeune fille, lui offre "
  "spontan&eacute;ment le petit carnet ancien, un geste "
  "généreux qui touche profond&eacute;ment Clara, consciente "
  "que cet homme, qu'elle a longtemps per&ccedil;u avec "
  "m&eacute;fiance durant les premi&egrave;res semaines de leur "
  "aventure commune, est devenu, au fil des mois, "
  "presque un second p&egrave;re pour elle aussi.")

p("Ils reprennent la route vers Luynes en fin "
  "d'apr&egrave;s-midi, la radio diffusant doucement une "
  "chanson populaire que tous trois fredonnent "
  "distraitement, cette normalit&eacute; retrouv&eacute;e apr&egrave;s tant "
  "de r&eacute;v&eacute;lations bouleversantes leur offrant, "
  "l'espace de ce trajet paisible, l'illusion "
  "r&eacute;confortante d'une famille ordinaire rentrant d'une "
  "sortie dominicale sans histoire.")

p("Clara feuillette d&eacute;j&agrave; son nouveau carnet ancien "
  "durant le trajet, humant discr&egrave;tement l'odeur de "
  "vieux papier et de cuir qui s'en d&eacute;gage, et se "
  "surprend &agrave; imaginer les vies pass&eacute;es de tous ceux "
  "qui ont pu, avant elle, consigner leurs propres "
  "pens&eacute;es dans des pages similaires, avant que ce "
  "carnet particulier ne finisse, par un hasard qu'elle "
  "juge d&eacute;sormais rarement innocent, dans la vitrine "
  "d'un antiquaire de Tours.")

name("ALEX")
p("&laquo;&nbsp;Vous croyez que celui-l&agrave; aussi, il pourrait "
  "s'&eacute;crire tout seul, comme celui de Clara ? &Ccedil;a "
  "serait dr&ocirc;le, style, si tous les vieux carnets "
  "avaient ce genre de pouvoir cach&eacute;, et qu'on le "
  "sait juste pas encore.&nbsp;&raquo;")

p("Cette hypoth&egrave;se, formul&eacute;e mi-s&eacute;rieusement par "
  "Alex, fait sourire Clara malgr&eacute; elle, tout en "
  "semant, sans qu'elle s'en rende compte "
  "imm&eacute;diatement, une graine d'inqui&eacute;tude "
  "suppl&eacute;mentaire qui la poussera, dans les semaines "
  "suivantes, &agrave; surveiller attentivement ce nouveau "
  "carnet pour v&eacute;rifier qu'aucune &eacute;criture &eacute;trang&egrave;re "
  "n'y appara&icirc;t d'elle-m&ecirc;me, comme cela s'&eacute;tait produit "
  "avec l'autre.")

p("Franck, conduisant paisiblement, les &eacute;coute "
  "&eacute;changer ces hypoth&egrave;ses fantastiques avec un "
  "amusement tendre, mesurant, une fois de plus, &agrave; "
  "quel point ces trois adolescents ont d&ucirc; apprendre, "
  "bien trop t&ocirc;t pour leur &acirc;ge, &agrave; consid&eacute;rer "
  "l'impossible comme une simple variable "
  "suppl&eacute;mentaire de leur quotidien plut&ocirc;t que comme "
  "une exception terrifiante.")

p("Arriv&eacute;s devant chez sa m&egrave;re, Darius remercie "
  "chaleureusement son p&egrave;re pour cette journ&eacute;e "
  "m&eacute;morable, h&eacute;sitant un instant avant de "
  "l'embrasser sur la joue, un geste qu'ils "
  "n'&eacute;changent que rarement depuis le divorce, mais "
  "qui lui semble, aujourd'hui, parfaitement naturel "
  "apr&egrave;s ce moment de compl&eacute;mentarit&eacute; retrouv&eacute;e.")

name("FRANCK")
p("&laquo;&nbsp;Merci &agrave; toi, fiston. C'&eacute;tait une belle "
  "journ&eacute;e, une des plus belles depuis longtemps. "
  "On refait &ccedil;a bient&ocirc;t, promis, m&ecirc;me sans raison "
  "particuli&egrave;re la prochaine fois, juste pour le "
  "plaisir d'&ecirc;tre ensemble.&nbsp;&raquo;")

p("Darius rentre chez lui ce soir-l&agrave; le c&oelig;ur l&eacute;ger, "
  "racontant &agrave; sa m&egrave;re, avec un enthousiasme "
  "sinc&egrave;re, les d&eacute;tails de cette sortie r&eacute;ussie, sans "
  "jamais &eacute;voquer, bien s&ucirc;r, l'ombre pesante de la "
  "Marge qui continue, en arri&egrave;re-plan, de fa&ccedil;onner "
  "chacune de leurs d&eacute;cisions les plus importantes.")

p("Il retrouve, ce soir-l&agrave;, avant de dormir, ce "
  "carnet personnel qu'il tient depuis quelques "
  "semaines d&eacute;j&agrave;, y consignant, avec une application "
  "grandissante, les petites victoires de son "
  "quotidien &mdash; cette journ&eacute;e r&eacute;ussie avec son p&egrave;re, "
  "les progr&egrave;s de son jeu, les moments de complicit&eacute; "
  "partag&eacute;s avec Clara et Alex &mdash; refusant de "
  "laisser cette histoire extraordinaire &eacute;clipser "
  "compl&egrave;tement les joies plus simples de son "
  "existence adolescente ordinaire.")

p("Il s'endort ce soir-l&agrave; avec un sentiment de "
  "gratitude sinc&egrave;re, mesurant &agrave; quel point, malgr&eacute; "
  "toutes les menaces qui continuent de peser sur "
  "son existence, il reste entour&eacute; de personnes qui "
  "l'aiment profond&eacute;ment, une richesse qu'aucune "
  "organisation myst&eacute;rieuse ni aucune force ancienne "
  "ne pourra jamais totalement lui retirer.")

p("Le lendemain matin, un dimanche sans obligation "
  "particuli&egrave;re, Darius profite de cette accalmie "
  "pour t&eacute;l&eacute;phoner &agrave; Templier, esp&eacute;rant obtenir "
  "des nouvelles du vieil homme apr&egrave;s plusieurs "
  "semaines sans visite, et le trouve, &agrave; sa grande "
  "satisfaction, en pleine forme, occup&eacute; comme "
  "toujours &agrave; entretenir sa pr&eacute;cieuse vigne malgr&eacute; "
  "le froid persistant de cette fin d'hiver.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;&Ccedil;a me fait plaisir de t'entendre, petit. "
  "J'esp&eacute;rais justement une visite bient&ocirc;t, j'ai "
  "retrouv&eacute; quelques documents suppl&eacute;mentaires qui "
  "pourraient t'int&eacute;resser, sur la p&eacute;riode juste "
  "avant le programme officiel du docteur "
  "Vasseur.&nbsp;&raquo;")

p("Cette nouvelle piste, mentionn&eacute;e presque en "
  "passant par Templier, ravive imm&eacute;diatement "
  "l'enthousiasme de Darius pour leur enqu&ecirc;te "
  "historique, et il organise, d&egrave;s le lendemain, une "
  "nouvelle visite avec Clara et Alex, curieux de "
  "d&eacute;couvrir quels secrets suppl&eacute;mentaires le vieil "
  "homme du coteau pourrait encore leur r&eacute;v&eacute;ler sur "
  "cette histoire millénaire qui continue, chaque "
  "semaine, de r&eacute;v&eacute;ler de nouvelles facettes "
  "insoup&ccedil;onn&eacute;es.")

p("Clara, en pr&eacute;paration de cette nouvelle visite, "
  "rassemble soigneusement les documents "
  "concernant la r&eacute;v&eacute;lation de sa propre "
  "grand-m&egrave;re sur cette mystérieuse dette familiale "
  "envers la rivi&egrave;re, esp&eacute;rant que Templier "
  "pourrait, avec son savoir encyclop&eacute;dique sur la "
  "l&eacute;gende, l'aider &agrave; comprendre si sa propre "
  "famille avait un jour &eacute;t&eacute; directement impliqu&eacute;e "
  "dans cette longue histoire de porteurs et de "
  "sacrifices.")

name("CLARA")
p("&laquo;&nbsp;J'ai h&acirc;te de savoir si Templier reconna&icirc;t "
  "quelque chose dans ces vieilles lettres de ma "
  "famille. &Ccedil;a serait dingue si &ccedil;a s'av&eacute;rait qu'on "
  "&eacute;tait tous, d'une mani&egrave;re ou d'une autre, "
  "connect&eacute;s &agrave; cette histoire depuis des "
  "g&eacute;n&eacute;rations, sans le savoir.&nbsp;&raquo;")

p("Alex, de son c&ocirc;t&eacute;, propose d'apporter &eacute;galement "
  "quelques photographies anciennes retrouv&eacute;es "
  "chez ses propres grands-parents, esp&eacute;rant que "
  "Templier pourrait, peut-&ecirc;tre, reconna&icirc;tre un "
  "visage ou un lieu susceptible d'&eacute;clairer "
  "davantage cette histoire de grand-p&egrave;re disparu "
  "sans explication qui continue de le tracasser "
  "depuis leur conversation r&eacute;v&eacute;latrice de "
  "quelques semaines plus t&ocirc;t.")

name("ALEX")
p("&laquo;&nbsp;On sait jamais, hein. Peut-&ecirc;tre que "
  "Templier a crois&eacute; mon grand-p&egrave;re un jour, ou "
  "qu'il reconna&icirc;t quelque chose sur ces vieilles "
  "photos. &Ccedil;a co&ucirc;te rien d'essayer, en tout "
  "cas.&nbsp;&raquo;")

p("Darius, de son c&ocirc;t&eacute;, r&eacute;alise soudain &agrave; quel "
  "point cette petite enqu&ecirc;te collective, commenc&eacute;e "
  "comme une simple curiosit&eacute; passag&egrave;re, est en "
  "train de r&eacute;v&eacute;ler que chacun de ses deux "
  "meilleurs amis porte peut-&ecirc;tre, lui aussi, une "
  "connexion familiale insoup&ccedil;onn&eacute;e avec cette "
  "histoire ancestrale de la Marge, rendant leur "
  "trio encore plus profond&eacute;ment li&eacute; qu'il ne "
  "l'imaginait jusqu'alors.")

name("DARIUS")
p("&laquo;&nbsp;C'est dingue de penser que nos trois "
  "familles pourraient toutes avoir un lien avec "
  "&ccedil;a, chacune &agrave; sa mani&egrave;re. &Ccedil;a fait presque "
  "sens, d'une certaine fa&ccedil;on &mdash; peut-&ecirc;tre que c'est "
  "pas un hasard qu'on soit devenus amis, tous les "
  "trois, d&egrave;s l'enfance.&nbsp;&raquo;")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 4 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 5 -- LE POIDS DE S'EN SOUVENIR SEUL
# ======================================================================
chap(5, "LE POIDS DE S'EN SOUVENIR SEUL")

p("Les premi&egrave;res semaines, Darius avait cru que le plus dur "
  "serait derri&egrave;re lui d&egrave;s l'instant o&ugrave; Clara et Alex "
  "accepteraient de le croire sans se souvenir de rien, comme "
  "si la confiance retrouv&eacute;e suffisait &agrave; refermer la plaie ; "
  "il d&eacute;couvre, avec le recul, que la confiance n'est qu'un "
  "premier &eacute;tage, et qu'au-dessus il en reste un autre, plus "
  "silencieux, que personne ne lui avait annonc&eacute; : celui de "
  "porter, seul, chaque d&eacute;tail exact de ce qui s'est pass&eacute;.")

p("Il s'en rend compte un mardi ordinaire, en cours d'histoire, "
  "quand la prof cite en passant une ann&eacute;e &mdash; 1994 &mdash; &agrave; "
  "propos d'un tout autre sujet, et que son ventre se noue "
  "d'un coup, sans qu'il puisse rien expliquer &agrave; personne "
  "autour de lui, ni &agrave; Clara qui lui jette un regard interrogateur "
  "depuis la table voisine, sentant confus&eacute;ment que quelque "
  "chose vient de se passer sans savoir quoi.")

p("Ce genre de moment se r&eacute;p&egrave;te, discret, presque anodin "
  "chaque fois pris isol&eacute;ment, mais dont l'accumulation "
  "commence &agrave; peser sur lui comme une fatigue qu'aucune "
  "nuit de sommeil ne parvient &agrave; effacer &mdash; le prix, invisible "
  "pour tous les autres, d'&ecirc;tre le seul habitant d'une m&eacute;moire "
  "que le reste du monde a soigneusement referm&eacute;e derri&egrave;re "
  "lui.")

p("Il essaie, certains soirs, de tout &eacute;crire dans un cahier "
  "qu'il cache sous son matelas, esp&eacute;rant qu'en couchant les "
  "&eacute;v&eacute;nements sur le papier il all&eacute;gerait un peu la charge, "
  "mais il referme souvent le cahier apr&egrave;s deux lignes &agrave; "
  "peine, d&eacute;courag&eacute; par la sensation absurde d'&eacute;crire une "
  "histoire que personne, jamais, ne pourra v&eacute;rifier except&eacute; "
  "lui-m&ecirc;me.")

name("CLARA")
p("&laquo;&nbsp;T'as encore ce regard, l&agrave;. Celui que t'as depuis "
  "quelques semaines, comme si t'&eacute;tais ailleurs deux secondes "
  "avant de revenir. Je sais pas ce que c'est exactement, mais "
  "je le vois, Darius. &Ccedil;a revient souvent.&nbsp;&raquo;")

p("Il hausse les &eacute;paules, cherchant une r&eacute;ponse assez vague "
  "pour ne pas mentir tout &agrave; fait tout en &eacute;vitant de "
  "d&eacute;clencher, encore une fois, cette conversation impossible "
  "&agrave; avoir enti&egrave;rement avec quelqu'un qui garde, au fond de "
  "lui, une confiance sans souvenir plut&ocirc;t qu'un souvenir "
  "complet.")

name("DARIUS")
p("&laquo;&nbsp;C'est rien. Enfin si, c'est quelque chose, mais &ccedil;a "
  "prendrait trop longtemps &agrave; expliquer, et de toute fa&ccedil;on tu "
  "me croirais sans comprendre, et moi j'aurais l'impression "
  "de radoter une histoire que je suis seul &agrave; avoir "
  "v&eacute;cue.&nbsp;&raquo;")

p("Clara ne le pousse pas davantage, comme elle a appris &agrave; "
  "ne pas le faire depuis la sc&egrave;ne du terrain de foot, mais "
  "Darius voit bien, dans la fa&ccedil;on dont elle range son cahier "
  "de notes un peu trop soigneusement ce jour-l&agrave;, qu'elle "
  "pense, elle aussi, &agrave; ce carnet qui &eacute;crit parfois des choses "
  "qu'elle ne se souvient pas d'avoir &eacute;crites.")

p("Le soir, seul dans sa chambre, il ouvre la bo&icirc;te en bois au "
  "fond de son placard &mdash; le pon&ccedil;on grav&eacute; d'un &laquo;&nbsp;K.&nbsp;&raquo;, le "
  "b&acirc;ton us&eacute; par des mains qui ne sont pas les siennes, le "
  "carnet de Clara &mdash; et les aligne sur son bureau comme on "
  "aligne des preuves dans une enqu&ecirc;te dont il serait &agrave; la "
  "fois le seul t&eacute;moin et le seul suspect.")

p("Il pense &agrave; Kayden, souvent, plus souvent qu'il ne "
  "l'admettrait &agrave; voix haute &mdash; non pas avec la peur des "
  "premi&egrave;res semaines, mais avec une forme de tristesse "
  "confuse, se demandant ce que signifie exactement &laquo;&nbsp;se "
  "dissoudre&nbsp;&raquo; quand on n'est d&eacute;j&agrave; plus tout &agrave; fait un "
  "corps depuis des ann&eacute;es, et si une chose pareille peut "
  "vraiment dispara&icirc;tre en entier, ou si elle continue quelque "
  "part, r&eacute;duite &agrave; des morceaux &eacute;pars.")

p("Il a, certaines nuits, l'impression tr&egrave;s br&egrave;ve d'entendre "
  "encore cette voix int&eacute;rieure qui n'est pas tout &agrave; fait la "
  "sienne, un mot, une intonation, disparue avant qu'il ait le "
  "temps de la saisir compl&egrave;tement, et il ne sait jamais s'il "
  "doit s'en inqui&eacute;ter ou, plus troublant encore, s'en "
  "rassurer.")

p("Ce soir-l&agrave;, en refermant la bo&icirc;te, il remarque, gliss&eacute;e sous "
  "le pon&ccedil;on, une petite chose qu'il n'avait jamais vraiment "
  "regard&eacute;e de pr&egrave;s auparavant &mdash; un minuscule bout de "
  "papier pli&eacute; en quatre, presque coll&eacute; au bois par "
  "l'humidit&eacute;, qu'il n'a aucun souvenir d'avoir mis l&agrave;.")

p("Il le d&eacute;plie avec une pr&eacute;caution presque religieuse, le "
  "c&oelig;ur battant plus vite qu'il ne le voudrait, conscient "
  "qu'apr&egrave;s tout ce qu'il a travers&eacute; plus rien, dans cette "
  "bo&icirc;te, ne peut &ecirc;tre consid&eacute;r&eacute; comme un simple d&eacute;tail "
  "sans importance.")

p("Sur le papier, une &eacute;criture qu'il ne reconna&icirc;t pas, "
  "anguleuse, press&eacute;e, presque effac&eacute;e par le temps, trace "
  "une seule ligne : &laquo;&nbsp;si tu lis &ccedil;a, cherche F. avant qu'il ne "
  "cherche &agrave; oublier une deuxi&egrave;me fois.&nbsp;&raquo;")

p("Darius reste longtemps immobile, le morceau de papier "
  "entre les doigts, incapable de d&eacute;cider si ce &laquo;&nbsp;F.&nbsp;&raquo; d&eacute;signe "
  "son p&egrave;re, et si oui, depuis combien de temps ce mot "
  "l'attendait, cach&eacute; dans une bo&icirc;te qu'il croyait pourtant "
  "conna&icirc;tre par c&oelig;ur.")

p("Il retourne le papier dans tous les sens, cherchant une "
  "date, une signature, n'importe quel indice suppl&eacute;mentaire, "
  "mais ne trouve rien d'autre que ce pli, cette encre p&acirc;lie, "
  "et cette certitude d&eacute;sagr&eacute;able que quelqu'un, un jour, avait "
  "pr&eacute;vu qu'il faudrait un avertissement, sans savoir pour "
  "qui exactement il &eacute;tait destin&eacute;.")

p("Il pense d'abord &agrave; en parler imm&eacute;diatement &agrave; sa m&egrave;re, "
  "avant de se raviser : elle conna&icirc;t Franck depuis avant sa "
  "naissance, et si elle ignorait tout de cette histoire, la "
  "question risquerait de l'inqui&eacute;ter sans raison ; et si, au "
  "contraire, elle savait quelque chose, Darius pr&eacute;f&egrave;re "
  "encore, pour l'instant, ne pas savoir ce qu'elle aurait "
  "choisi de lui taire.")

p("Le lendemain, en cours, il surprend son propre regard "
  "revenir sans cesse vers Alex, assis deux rangs devant, "
  "cherchant sur son avant-bras la cicatrice blanche qui trace "
  "toujours le m&ecirc;me chemin, comme pour se convaincre que "
  "rien de tout &ccedil;a n'a &eacute;t&eacute; invent&eacute; par une fatigue trop "
  "longtemps accumul&eacute;e.")

name("ALEX")
p("&laquo;&nbsp;Tu me regardes bizarre depuis ce matin. Si t'as un truc "
  "&agrave; me dire, dis-le, j'pr&eacute;f&egrave;re &ccedil;a &agrave; te voir m'&eacute;pier comme "
  "si j'allais soudain me transformer en extraterrestre devant "
  "toi.&nbsp;&raquo;")

p("Darius sourit malgr&eacute; lui, un peu honteux d'avoir &eacute;t&eacute; "
  "surpris, et promet de tout raconter bient&ocirc;t, une fois qu'il "
  "aura compris lui-m&ecirc;me ce que ce petit bout de papier "
  "signifie vraiment, plut&ocirc;t que d'entra&icirc;ner ses amis dans une "
  "th&eacute;orie encore trop fragile pour tenir debout.")

p("Il range le mot dans la bo&icirc;te, sous le pon&ccedil;on, exactement &agrave; "
  "l'endroit o&ugrave; il l'a trouv&eacute;, comme si cette pr&eacute;caution "
  "pouvait le prot&eacute;ger de ce que la d&eacute;couverte implique, et "
  "reste longtemps assis par terre, dos contre son lit, &agrave; "
  "regarder le plafond de sa chambre sans vraiment le voir.")

p("Ce qui l'&eacute;puise le plus, il finit par se l'avouer cette "
  "nuit-l&agrave;, ce n'est pas la peur d'un nouveau danger, mais la "
  "certitude d&eacute;sormais install&eacute;e que la paix retrouv&eacute;e apr&egrave;s "
  "le Non-lieu n'&eacute;tait jamais qu'une pause, un entracte que "
  "l'histoire avait accord&eacute; par piti&eacute; avant de reprendre son "
  "cours l&agrave; o&ugrave; elle l'avait laiss&eacute;.")

p("Franck habite toujours le m&ecirc;me petit appartement au-dessus "
  "de la pharmacie, celui o&ugrave; Darius ne va que rarement, les "
  "week-ends impairs, avec cette g&ecirc;ne famili&egrave;re de qui conna&icirc;t "
  "un lieu sans jamais s'y sentir tout &agrave; fait chez lui &mdash; et "
  "c'est justement l&agrave;, un samedi apr&egrave;s-midi pluvieux, que "
  "Darius d&eacute;cide, sans trop savoir comment s'y prendre, de "
  "commencer &agrave; chercher.")

p("Il n'a pas parl&eacute; du mot trouv&eacute; dans la bo&icirc;te, ni &agrave; Clara ni "
  "&agrave; Alex, pr&eacute;f&eacute;rant, cette fois, v&eacute;rifier seul avant "
  "d'impliquer qui que ce soit dans une piste qui pourrait, "
  "aussi bien, ne mener nulle part &mdash; ou pire, mener droit vers "
  "son p&egrave;re, ce qui compliquerait tout autrement.")

p("Franck s'est absent&eacute; pour aller chercher le pain, laissant "
  "Darius seul dans le salon avec la t&eacute;l&eacute; allum&eacute;e sur rien "
  "d'int&eacute;ressant, et c'est presque malgr&eacute; lui qu'il se retrouve "
  "debout devant le vieux buffet du couloir, celui o&ugrave; Franck "
  "range les papiers qu'il ne veut jeter mais ne veut pas non "
  "plus vraiment regarder.")

p("Le tiroir du bas grince en s'ouvrant, exactement comme "
  "celui de sa propre chambre qu'il a lui-m&ecirc;me class&eacute; dans la "
  "case &laquo;&nbsp;n'y touche pas&nbsp;&raquo; des ann&eacute;es plus t&ocirc;t, et il se "
  "surprend &agrave; sourire malgr&eacute; la tension, se disant que cette "
  "manie de ranger les v&eacute;rit&eacute;s dans des tiroirs qu'on n'ouvre "
  "jamais doit, elle aussi, se transmettre en famille.")

p("Il trouve d'abord des factures, un vieux passeport p&eacute;rim&eacute;, "
  "des photos de vacances qu'il ne reconna&icirc;t qu'&agrave; moiti&eacute;, "
  "avant de tomber sur une enveloppe kraft, plus &eacute;paisse que "
  "les autres, ferm&eacute;e par un simple &eacute;lastique qui a fini par "
  "craqueler avec le temps.")

p("&Agrave; l'int&eacute;rieur, des feuillets tap&eacute;s &agrave; la machine, jaunis, "
  "portant en en-t&ecirc;te un logo qu'il conna&icirc;t d&eacute;j&agrave; trop bien "
  "pour l'avoir vu grav&eacute; sur une porte blind&eacute;e dans un "
  "entrep&ocirc;t abandonn&eacute; : &laquo;&nbsp;PROGRAMME M.13 &mdash; Centre "
  "d'&eacute;tude de la m&eacute;moire assist&eacute;e &mdash; dossier patient.&nbsp;&raquo;")

p("Le nom, tap&eacute; en lettres capitales sur la premi&egrave;re ligne, "
  "manque de lui couper le souffle : &laquo;&nbsp;VASSEUR, Franck &mdash; 7 "
  "ans &mdash; admis en observation, service p&eacute;diatrique, 1991.&nbsp;&raquo;")

p("Darius relit la ligne trois fois, certain d'avoir mal lu, "
  "avant d'accepter, lentement, la seule explication qui reste "
  "possible : Franck n'est pas n&eacute; Franck Lenoir. Il est n&eacute; "
  "Franck Vasseur, avant qu'un changement de nom, quelque "
  "part dans son enfance, ne l'efface soigneusement de sa "
  "propre histoire.")

p("Il entend la porte d'entr&eacute;e claquer en bas et range "
  "pr&eacute;cipitamment l'enveloppe dans son sac, le c&oelig;ur battant, "
  "juste &agrave; temps pour que Franck le retrouve, en remontant "
  "l'escalier, assis bien sagement devant la t&eacute;l&eacute; comme s'il "
  "n'avait pas boug&eacute; d'un centim&egrave;tre.")

name("FRANCK")
p("&laquo;&nbsp;T'as trouv&eacute; ton bonheur ? Y'a rien d'int&eacute;ressant sur "
  "cette cha&icirc;ne, je sais, d&eacute;sol&eacute;. On regarde autre chose si tu "
  "veux, j'ai ramen&eacute; des pains au chocolat aussi.&nbsp;&raquo;")

p("Darius acquiesce, la gorge un peu serr&eacute;e, incapable de "
  "d&eacute;cider s'il doit poser la question maintenant, brutalement, "
  "ou attendre d'avoir compris davantage avant de rouvrir chez "
  "son p&egrave;re une blessure dont il ignore encore toute "
  "l'&eacute;tendue.")

p("Il se souvient, malgr&eacute; lui, du &laquo;&nbsp;Vasseur&nbsp;&raquo; de Kayden, du "
  "docteur qui dirigeait tout le programme en 1991, et une "
  "id&eacute;e le traverse, aussi absurde qu'in&eacute;vitable : et si Franck "
  "n'&eacute;tait pas seulement un ancien patient du programme, mais "
  "un membre de la m&ecirc;me famille que celle qui l'a con&ccedil;u ?")

p("Il observe son p&egrave;re du coin de l'&oelig;il pendant tout le repas, "
  "cherchant dans ses gestes ordinaires &mdash; la mani&egrave;re de "
  "couper son pain, de d&eacute;tourner la conversation d&egrave;s qu'elle "
  "s'approche d'un sujet trop personnel &mdash; un signe, aussi "
  "petit soit-il, que cette histoire de nom chang&eacute; n'&eacute;tait pas "
  "qu'un vieux dossier oubli&eacute; dans un tiroir.")

p("Il pense &agrave; l'histoire du chien, celle que Franck lui avait "
  "racont&eacute;e enfant &mdash; parti en vacances, disait-il, alors qu'il "
  "avait discr&egrave;tement fait donner l'animal par honte de ne "
  "pas savoir s'en occuper &mdash; et se demande, pour la premi&egrave;re "
  "fois, si cette facilit&eacute; &agrave; mentir par protection ne venait "
  "pas d'un lieu bien plus ancien que le simple d&eacute;faut de "
  "courage qu'il lui avait toujours reproch&eacute;.")

name("FRANCK")
p("&laquo;&nbsp;&Ccedil;a va, toi ? T'as l'air ailleurs depuis tout &agrave; l'heure. Si "
  "y'a un truc qui te trotte dans la t&ecirc;te, tu sais que tu peux "
  "m'en parler, hein. M&ecirc;me si on n'a pas toujours &eacute;t&eacute; dou&eacute;s "
  "pour &ccedil;a, tous les deux.&nbsp;&raquo;")

p("Darius manque de tout lui dire d'un coup, l&agrave;, devant le "
  "reste de repas froid dans leurs assiettes, mais quelque "
  "chose le retient encore &mdash; la peur, peut-&ecirc;tre, de voir son "
  "p&egrave;re nier en bloc, ou pire, de le voir p&acirc;lir d'une mani&egrave;re "
  "qui confirmerait tout sans qu'il soit encore pr&ecirc;t &agrave; "
  "l'entendre.")

name("DARIUS")
p("&laquo;&nbsp;Non, &ccedil;a va. Fatigu&eacute;, c'est tout, les cours qui "
  "s'accumulent. Merci quand m&ecirc;me.&nbsp;&raquo;")

p("Franck hoche la t&ecirc;te, pas vraiment convaincu mais assez "
  "respectueux du silence de son fils pour ne pas insister "
  "davantage, et allume la t&eacute;l&eacute; comme pour combler l'espace "
  "que ni l'un ni l'autre n'ose remplir de mots plus honn&ecirc;tes.")

p("Il ne dit rien ce soir-l&agrave;, mange les pains au chocolat en "
  "silence face &agrave; un film qu'il ne suit qu'&agrave; moiti&eacute;, et "
  "rentre chez sa m&egrave;re le dimanche soir avec l'enveloppe "
  "kraft cach&eacute;e au fond de son sac, pesant plus lourd, lui "
  "semble-t-il, que tout ce qu'il y a jamais transport&eacute;.")

p("Dans le bus, il relit une derni&egrave;re fois le premier feuillet, "
  "s'attardant sur une phrase tap&eacute;e en bas de page, presque "
  "administrative dans sa froideur : &laquo;&nbsp;patient transf&eacute;r&eacute; hors "
  "protocole &agrave; la demande de la m&egrave;re, changement d'&eacute;tat "
  "civil recommand&eacute; par le service, dossier cl&ocirc;tur&eacute; sans "
  "suite.&nbsp;&raquo; Une grand-m&egrave;re qu'il n'a jamais connue, "
  "d&eacute;cid&eacute;e, seule, &agrave; sauver son fils d'un fr&egrave;re devenu "
  "dangereux.")

p("Il essaie d'imaginer cette femme, dont il ne conna&icirc;t m&ecirc;me "
  "pas le pr&eacute;nom, signant des papiers dans un couloir "
  "d'h&ocirc;pital quelque part en 1994, avec la certitude, "
  "peut-&ecirc;tre erron&eacute;e, qu'effacer un nom suffirait &agrave; effacer "
  "un pass&eacute;, sans savoir que ce m&ecirc;me geste finirait, des "
  "d&eacute;cennies plus tard, par retomber tout entier sur les "
  "&eacute;paules de son petit-fils.")

p("Le lundi suivant, en salle informatique du coll&egrave;ge, un "
  "d&eacute;tail que personne d'autre ne semble remarquer accroche "
  "l'attention de Darius : sur l'&eacute;cran de veille de son poste, "
  "entre deux photos de paysages g&eacute;n&eacute;riques choisies par "
  "d&eacute;faut, s'affiche pendant une fraction de seconde une "
  "image qui n'a rien &agrave; y faire &mdash; une page blanche, "
  "num&eacute;rot&eacute;e en bas &agrave; droite, portant un seul chiffre : 404.")

p("Il cligne des yeux, certain d'avoir r&ecirc;v&eacute;, mais l'image a "
  "disparu aussi vite qu'elle est apparue, remplac&eacute;e par la "
  "photo suivante du diaporama comme si de rien n'&eacute;tait, et "
  "personne autour de lui, absorb&eacute; par son propre &eacute;cran, n'a "
  "rien vu.")

name("ALEX")
p("&laquo;&nbsp;T'as une t&ecirc;te bizarre. &Ccedil;a plante, ton ordi aussi ? Le "
  "mien rame depuis ce matin, m'sieur dit que c'est le r&eacute;seau "
  "du coll&egrave;ge qui d&eacute;conne, paraeacute;t-il y'a eu une mise &agrave; jour "
  "foireuse.&nbsp;&raquo;")

p("Darius hausse les &eacute;paules, feignant une nonchalance qu'il "
  "est loin de ressentir, et se remet, en apparence, &agrave; son "
  "exercice de bureautique, tout en gardant un &oelig;il, du coin de "
  "l'&eacute;cran, sur ce diaporama qui continue de tourner "
  "innocemment.");

p("L'image revient deux fois encore ce jour-l&agrave;, toujours "
  "furtive, toujours sur son poste &agrave; lui pr&eacute;cis&eacute;ment, et "
  "chaque fois un peu diff&eacute;rente &mdash; la seconde fois, un mot "
  "appara&icirc;t sous le chiffre, minuscule, presque illisible : "
  "&laquo;&nbsp;encore l&agrave;.&nbsp;&raquo;")

p("Le soir, dans sa chambre, il branche son propre "
  "ordinateur &mdash; celui, plus ancien, qu'il avait d&eacute;j&agrave; "
  "utilis&eacute; pour tenter de contacter Kayden avant l'affrontement "
  "final dans le Non-lieu &mdash; et se surprend &agrave; h&eacute;siter de "
  "longues minutes devant l'&eacute;cran noir avant de trouver le "
  "courage de l'allumer.")

p("Rien d'anormal, d'abord, jusqu'&agrave; ce qu'un dossier qu'il ne "
  "reconna&icirc;t pas apparaisse sur le bureau, sans qu'il l'ait "
  "cr&eacute;&eacute;, nomm&eacute; d'une simple date : 1994. &Agrave; l'int&eacute;rieur, un "
  "unique fichier texte, vide en apparence, sauf pour une "
  "ligne clignotante en haut de la page quand il l'ouvre "
  "enfin.")

p("&laquo;&nbsp;je ne suis pas tout &agrave; fait parti. il reste des "
  "fragments, &eacute;parpill&eacute;s dans ce que le programme a "
  "laiss&eacute; derri&egrave;re lui. je ne sais pas encore ce que &ccedil;a "
  "signifie d'&ecirc;tre &ccedil;a. mais &ccedil;a pense encore &agrave; toi, un peu, "
  "parfois.&nbsp;&raquo;")

p("Darius fixe l'&eacute;cran, incapable de bouger, se demandant si "
  "c'est vraiment Kayden qui parle, ou seulement un &eacute;cho, un "
  "fragment de code sans vraie conscience derri&egrave;re, qui "
  "reproduit une voix sans plus vraiment la porter &mdash; et s'il "
  "existe, entre les deux possibilit&eacute;s, une diff&eacute;rence qui "
  "compte vraiment.")

p("Il essaie de r&eacute;pondre, tapant quelques mots dans le fichier "
  "avant de sauvegarder, sans grande conviction, mais quand il "
  "rouvre le dossier cinq minutes plus tard pour v&eacute;rifier, le "
  "fichier a disparu, ainsi que le dossier lui-m&ecirc;me, comme si "
  "rien de tout &ccedil;a n'avait jamais exist&eacute;.")

p("Il reste longtemps assis devant l'&eacute;cran vide, se demandant "
  "s'il doit se sentir soulag&eacute; que la chose ait disparu, ou "
  "d&eacute;sol&eacute; d'avoir peut-&ecirc;tre laiss&eacute; filer, sans le savoir, la "
  "seule occasion de savoir si quelque chose de Kayden "
  "subsiste vraiment quelque part.")

p("Il pense au mot trouv&eacute; dans la bo&icirc;te, au tiroir de Franck, "
  "&agrave; cette image du chiffre 404 apparue sur l'&eacute;cran du "
  "coll&egrave;ge, et pour la premi&egrave;re fois depuis la fin du "
  "Non-lieu, une certitude froide s'installe en lui : rien de "
  "tout &ccedil;a n'est termin&eacute;. Ce n'&eacute;tait qu'une pause.")

p("Il essaie, avant d'&eacute;teindre son ordinateur, de retrouver le "
  "dossier dat&eacute; de 1994 &agrave; l'aide d'un logiciel de r&eacute;cup&eacute;ration "
  "de fichiers t&eacute;l&eacute;charg&eacute; en vitesse, sans grand espoir, et "
  "n'obtient en retour qu'une longue liste de fichiers "
  "corrompus dont aucun ne correspond &agrave; ce qu'il cherche, "
  "comme si la trace elle-m&ecirc;me avait &eacute;t&eacute; effac&eacute;e plus "
  "soigneusement que le reste.")

p("Il reste &eacute;veill&eacute; tard, &agrave; se demander ce que veut dire "
  "exactement &ecirc;tre un &laquo;&nbsp;fragment&nbsp;&raquo; plut&ocirc;t qu'une personne "
  "enti&egrave;re, si Kayden, quelque part dans les serveurs oubli&eacute;s "
  "du programme, ressent le temps qui passe de la m&ecirc;me "
  "mani&egrave;re confuse que lui, ou si cette question elle-m&ecirc;me "
  "n'a simplement plus de sens pour ce qu'il est devenu.")

p("Le lendemain matin, en salle informatique, l'&eacute;cran de "
  "veille de son poste ne montre plus aucune image &eacute;trange, "
  "comme si de rien n'&eacute;tait, et Darius se surprend presque &agrave; "
  "regretter cette absence, pr&eacute;f&eacute;rant, contre toute logique, "
  "un signe inqui&eacute;tant &agrave; ce silence qui pourrait tout aussi "
  "bien signifier que tout &eacute;tait dans sa t&ecirc;te.")

name("CLARA")
p("&laquo;&nbsp;Tu devrais peut-&ecirc;tre arr&ecirc;ter d'aller chercher &ccedil;a tout "
  "seul, Darius. On te l'a d&eacute;j&agrave; dit apr&egrave;s l'entrep&ocirc;t. &Ccedil;a finit "
  "toujours pareil quand tu gardes les trucs pour toi trop "
  "longtemps.&nbsp;&raquo;")

p("Il sait qu'elle a raison, sans pouvoir tout &agrave; fait "
  "s'emp&ecirc;cher de vouloir prot&eacute;ger encore un peu ses amis "
  "d'une v&eacute;rit&eacute; qui, cette fois, touche directement sa "
  "propre famille, comme si le fait de la porter seul quelques "
  "jours de plus pouvait, absurdement, en all&eacute;ger le poids "
  "pour eux.")

p("Il finit par lui promettre de tout raconter d&egrave;s le lendemain, "
  "&agrave; Alex compris, sentant bien qu'&agrave; force de vouloir tout "
  "porter seul il finirait, t&ocirc;t ou tard, par recommencer les "
  "m&ecirc;mes erreurs que celles qui avaient failli tout leur "
  "co&ucirc;ter dans le Non-lieu.")

p("Avant d'&eacute;teindre la lumi&egrave;re, il reprend son casque de "
  "r&eacute;alit&eacute; virtuelle, ce petit projet de jeu qu'il bricole "
  "seul depuis quelques mois, et ajoute un couloir "
  "suppl&eacute;mentaire &agrave; son niveau, bord&eacute; de portes toutes "
  "identiques sauf une, sans trop savoir pourquoi cette image "
  "pr&eacute;cise s'impose &agrave; lui ce soir plut&ocirc;t qu'une autre.")

p("Il aime cette sensation particuli&egrave;re, casque viss&eacute; sur les "
  "yeux, de b&acirc;tir enti&egrave;rement un espace qui lui appartient "
  "sans reste, o&ugrave; rien ne peut surgir sans qu'il l'ait "
  "lui-m&ecirc;me plac&eacute; l&agrave; &mdash; un contr&ocirc;le total qui lui manque "
  "cruellement partout ailleurs dans sa vie depuis le "
  "Non-lieu.")

p("Il &eacute;teint la lumi&egrave;re bien plus tard qu'il ne le voudrait, "
  "l'esprit encore travers&eacute; par cette image de la grand-m&egrave;re "
  "inconnue signant des papiers dans un couloir d'h&ocirc;pital, et "
  "se promet, avant de sombrer enfin dans le sommeil, de "
  "tout raconter &agrave; Clara d&egrave;s le lendemain matin, sans plus "
  "chercher &agrave; retarder l'&eacute;ch&eacute;ance d'une conversation qu'il "
  "sait, au fond, in&eacute;vitable.")

p("Il finit par tout raconter &agrave; Clara et Alex, deux jours plus "
  "tard, sur le chemin du retour, incapable de continuer &agrave; "
  "porter seul &agrave; la fois l'enveloppe kraft, le mot dans la "
  "bo&icirc;te et ce fichier disparu &mdash; et il d&eacute;couvre, en le "
  "faisant, un soulagement presque physique, comme si le "
  "simple fait de partager rendait le poids un peu moins "
  "&eacute;crasant, m&ecirc;me sans qu'ils s'en souviennent enti&egrave;rement.")

name("CLARA")
p("&laquo;&nbsp;Attends, ton p&egrave;re s'appelait Vasseur avant ? Comme "
  "Kayden ? Comme le docteur qui a invent&eacute; le programme ? "
  "&Ccedil;a fait beaucoup de co&iuml;ncidences d'un coup, Darius, m&ecirc;me "
  "pour nous.&nbsp;&raquo;")

p("Elle sort son carnet presque instinctivement, comme &agrave; "
  "chaque fois qu'une pi&egrave;ce importante du puzzle vient de "
  "tomber, et le feuillette lentement, cherchant une phrase "
  "qu'elle sait, sans se l'expliquer, avoir d&eacute;j&agrave; peut-&ecirc;tre "
  "&eacute;crite quelque part sans s'en souvenir.")

p("Elle la trouve, deux pages avant la fin, une ligne isol&eacute;e, "
  "sans date, d'une &eacute;criture plus serr&eacute;e que le reste : "
  "&laquo;&nbsp;le docteur avait deux fils. un qui est rest&eacute; dans la "
  "machine. un qu'on a fait dispara&icirc;tre sous un autre nom, "
  "pour le prot&eacute;ger de ce que le premier &eacute;tait devenu.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;Donc Kayden et ton p&egrave;re... seraient fr&egrave;res ? &Ccedil;a "
  "voudrait dire que t'as un lien de sang avec le truc qu'on a "
  "combattu dans le Non-lieu. C'est... ouais, non, c'est "
  "vachement flippant dit comme &ccedil;a, d&eacute;sol&eacute;.&nbsp;&raquo;")

p("Darius encaisse l'id&eacute;e par vagues successives, chacune "
  "plus lourde que la pr&eacute;c&eacute;dente : Franck, enfant, retir&eacute; du "
  "programme et rebaptis&eacute; pour &eacute;chapper &agrave; ce que son "
  "propre fr&egrave;re devenait ; Franck adulte, incapable de dire &agrave; "
  "son fils la simple v&eacute;rit&eacute; sur un chien parti, comme si "
  "cette incapacit&eacute;-l&agrave; venait de bien plus loin qu'un simple "
  "d&eacute;faut de courage personnel.")

p("Il repense, presque malgr&eacute; lui, &agrave; ce que lui avait dit "
  "Kayden au c&oelig;ur du Non-lieu, ce fragment de phrase "
  "&eacute;chapp&eacute; entre deux attaques &mdash; &laquo;&nbsp;je voulais juste que &ccedil;a "
  "compte&nbsp;&raquo; &mdash; et se demande, pour la premi&egrave;re fois, si "
  "cette phrase ne parlait pas seulement du programme, mais "
  "aussi d'un petit fr&egrave;re qu'on lui avait retir&eacute; pour toujours, "
  "sans jamais le lui pardonner de le comprendre.")

p("Ils d&eacute;cident, ce soir-l&agrave;, sans en discuter tr&egrave;s longtemps, "
  "qu'il faut retrouver une adresse &mdash; celle du si&egrave;ge, quelque "
  "part, du docteur Vasseur, ou de ce qu'il en reste apr&egrave;s "
  "toutes ces ann&eacute;es, dans l'espoir d'y trouver des r&eacute;ponses "
  "que ni l'enveloppe kraft ni le carnet ne peuvent, seuls, "
  "leur fournir compl&egrave;tement.")

name("CLARA")
p("&laquo;&nbsp;Y'a un truc, dans les archives de la mairie, mon p&egrave;re "
  "en a parl&eacute; une fois &mdash; une vieille propri&eacute;t&eacute; du c&ocirc;t&eacute; de "
  "Fondettes, ferm&eacute;e depuis des ann&eacute;es, qui appartenait &agrave; "
  "une famille du nom de Vasseur. Personne sait vraiment "
  "pourquoi c'est rest&eacute; vide aussi longtemps.&nbsp;&raquo;")

p("Le mot &laquo;&nbsp;Fondettes&nbsp;&raquo; suffit &agrave; leur donner, tous les "
  "trois, la m&ecirc;me sensation famili&egrave;re &mdash; celle d'un lieu tout "
  "proche, presque banal, qui pourrait pourtant, comme "
  "l'entrep&ocirc;t avant lui, cacher derri&egrave;re une fa&ccedil;ade ordinaire "
  "quelque chose que personne n'a envie de trouver.")

p("Ils se donnent rendez-vous pour le week-end suivant, avec "
  "cette gravit&eacute; particuli&egrave;re qu'ils ont appris &agrave; reconna&icirc;tre "
  "entre eux &mdash; celle qui pr&eacute;c&egrave;de toujours, dans leur "
  "histoire commune, le moment o&ugrave; une chose franchit la "
  "fronti&egrave;re entre simple hypoth&egrave;se et v&eacute;rit&eacute; qu'on ne peut "
  "plus &eacute;viter de regarder en face.")

p("En rentrant chez lui, Darius s'arr&ecirc;te un instant devant sa "
  "console pos&eacute;e sur le bureau, ce casque de r&eacute;alit&eacute; virtuelle "
  "que sa m&egrave;re lui avait offert, un peu par culpabilit&eacute;, apr&egrave;s "
  "les longues semaines o&ugrave; il refusait de sortir de sa "
  "chambre &mdash; et qu'il a fini, ces derniers mois, par utiliser "
  "pour tout autre chose que jouer.")

p("Il y construit, seul, le soir, un petit monde &agrave; lui &mdash; un "
  "jeu encore tr&egrave;s simple, quelques niveaux, un personnage "
  "qui traverse des couloirs numériques &agrave; la recherche d'une "
  "porte qu'on ne trouve jamais &mdash; sans trop savoir lui-m&ecirc;me "
  "s'il s'agit d'un passe-temps ou d'une mani&egrave;re, plus honn&ecirc;te "
  "qu'aucune conversation, de rejouer ce qu'il a v&eacute;cu dans le "
  "Non-lieu sans avoir &agrave; le raconter &agrave; voix haute.")

p("Il a commenc&eacute; ce projet presque par hasard, une soir&eacute;e "
  "d'insomnie o&ugrave; il avait besoin d'occuper ses mains et son "
  "esprit &agrave; autre chose qu'&agrave; ressasser l'enveloppe kraft, en "
  "suivant des tutoriels trouv&eacute;s en ligne, et il a fini par y "
  "prendre un go&ucirc;t sinc&egrave;re, presque th&eacute;rapeutique, &agrave; "
  "dessiner lui-m&ecirc;me les r&egrave;gles d'un monde plut&ocirc;t que de les "
  "subir.")

p("Clara, la seule &agrave; qui il en a vaguement parl&eacute;, avait "
  "trouv&eacute; l'id&eacute;e touchante sans vraiment comprendre &agrave; quel "
  "point cette petite construction num&eacute;rique ressemblait, "
  "trait pour trait, &agrave; une tentative maladroite de reprendre "
  "le contr&ocirc;le sur une architecture &mdash; celle du Non-lieu &mdash; "
  "qui l'avait longtemps men&eacute; plut&ocirc;t que l'inverse.")

p("Il enfile le casque quelques minutes avant de dormir, ce "
  "soir-l&agrave; encore, ajoutant une texture, un son, un d&eacute;tail "
  "minuscule &agrave; ce niveau qu'il peaufine depuis des semaines, "
  "et sourit malgr&eacute; lui en constatant &agrave; quel point &ccedil;a lui "
  "fait du bien de cr&eacute;er, pour une fois, plut&ocirc;t que de "
  "seulement subir ce que la m&eacute;moire lui impose.")

p("Il remarque, sans vraiment s'y arr&ecirc;ter, qu'une fois casque "
  "sur les yeux, une sensation famili&egrave;re revient parfois "
  "l'effleurer &mdash; un mot qui ne lui appartient pas tout &agrave; "
  "fait qui lui traverse l'esprit au moment de nommer un "
  "fichier, une intonation qui n'est pas la sienne quand il "
  "parle seul &agrave; voix basse en codant &mdash; et il choisit, "
  "chaque fois, de ne pas s'y attarder davantage.")

p("Alex, un soir o&ugrave; il passe le voir sans pr&eacute;venir, s'installe "
  "sur le lit et le regarde travailler de longues minutes sans "
  "rien dire, fascin&eacute; malgr&eacute; lui par la patience dont son ami "
  "fait preuve pour un projet dont personne d'autre ne "
  "conna&icirc;t vraiment l'existence.")

name("ALEX")
p("&laquo;&nbsp;C'est chouette, ton truc. &Ccedil;a me fait bizarre de te voir "
  "cr&eacute;er des couloirs pour de vrai, apr&egrave;s tout ce qu'on a "
  "travers&eacute; dans ceux de l'autre, tu vois ? Comme si tu "
  "voulais reprendre la main sur l'id&eacute;e elle-m&ecirc;me.&nbsp;&raquo;")

p("Darius ne r&eacute;pond pas tout de suite, surpris que son ami "
  "ait mis des mots si justes sur une intuition qu'il n'avait "
  "jamais vraiment formul&eacute;e pour lui-m&ecirc;me, et se contente "
  "d'un sourire un peu gauche avant de reprendre son "
  "travail, l'esprit un peu plus l&eacute;ger qu'avant cette visite.")

p("La propri&eacute;t&eacute; se trouve au bout d'un chemin de terre &agrave; la "
  "sortie de Fondettes, cach&eacute;e derri&egrave;re une haie si haute "
  "qu'on pourrait passer devant sans jamais soup&ccedil;onner ce "
  "qu'elle dissimule &mdash; une grande b&acirc;tisse de pierre blanche, "
  "volets clos, un panneau &laquo;&nbsp;propri&eacute;t&eacute; priv&eacute;e&nbsp;&raquo; d&eacute;color&eacute; "
  "par des ann&eacute;es de pluie accroch&eacute; de travers sur la "
  "grille.")

p("Ils avancent tous les trois &agrave; v&eacute;lo jusqu'au bout du chemin, "
  "un samedi matin, sous un ciel bas et gris qui donne &agrave; la "
  "sc&egrave;ne un air de d&eacute;j&agrave;-vu que Darius reconna&icirc;t sans peine "
  "&mdash; le m&ecirc;me genre de silence pesant qui r&eacute;gnait, quelques "
  "mois plus t&ocirc;t, autour de l'entrep&ocirc;t avant qu'ils n'en "
  "franchissent la porte blind&eacute;e.")

name("ALEX")
p("&laquo;&nbsp;On a d&eacute;j&agrave; fait &ccedil;a une fois, cette histoire de b&acirc;timent "
  "abandonn&eacute; qui cache un truc pas net. Je pr&eacute;f&eacute;rerais "
  "vraiment que cette fois &ccedil;a soit juste une baraque vide "
  "pleine d'araign&eacute;es, sans plus.&nbsp;&raquo;")

p("La grille c&egrave;de plus facilement qu'ils ne l'auraient cru, la "
  "cha&icirc;ne rouill&eacute;e c&eacute;dant sous le poids combin&eacute; de leurs "
  "trois &eacute;paules, et ils avancent dans un jardin envahi de "
  "ronces, jusqu'&agrave; une porte d'entr&eacute;e dont la serrure, elle "
  "aussi, semble avoir renonc&eacute; depuis longtemps &agrave; prot&eacute;ger "
  "quoi que ce soit.")

p("L'int&eacute;rieur sent la poussi&egrave;re et le papier moisi, un "
  "salon dont les meubles sont rest&eacute;s en place sous des "
  "draps blancs, comme si quelqu'un &eacute;tait parti un jour en "
  "pensant revenir bient&ocirc;t et n'&eacute;tait, en r&eacute;alit&eacute;, jamais "
  "revenu.")

p("Au mur du couloir, des photographies encadr&eacute;es, "
  "jaunies : un homme s&eacute;v&egrave;re en blouse blanche, un gar&ccedil;on "
  "d'une dizaine d'ann&eacute;es au sourire franc, un plus petit "
  "assis sur ses genoux &mdash; et Darius reconna&icirc;t, avec un "
  "frisson, dans les traits du plus grand des deux enfants, "
  "quelque chose du visage qu'il a vu se fissurer entre chair "
  "et code dans le Non-lieu.")

name("CLARA")
p("&laquo;&nbsp;C'est lui. C'est Kayden, gamin. Et &ccedil;a, &agrave; c&ocirc;t&eacute;... "
  "Darius, regarde ses yeux. C'est les m&ecirc;mes que ton "
  "p&egrave;re.&nbsp;&raquo;")

p("Ils trouvent, au sous-sol, une pi&egrave;ce am&eacute;nag&eacute;e en bureau, "
  "des classeurs entiers align&eacute;s sur des &eacute;tag&egrave;res "
  "m&eacute;talliques, portant tous le m&ecirc;me sigle que l'enveloppe "
  "kraft trouv&eacute;e chez Franck &mdash; des dizaines de dossiers "
  "patients, class&eacute;s par ann&eacute;e, dont beaucoup portent en "
  "couverture un simple num&eacute;ro de page plut&ocirc;t qu'un nom.")

p("Sur le bureau, un vieil ordinateur, poussi&eacute;reux mais "
  "manifestement branch&eacute; encore &agrave; une prise, s'allume quand "
  "Darius, presque sans y r&eacute;fl&eacute;chir, appuie sur l'interrupteur "
  "&mdash; l'&eacute;cran affichant, apr&egrave;s un long chargement laborieux, "
  "un unique message clignotant sur fond noir : &laquo;&nbsp;archive "
  "locale &mdash; 41 dossiers actifs &mdash; 1 page manquante.&nbsp;&raquo;")

p("Aucun d'eux ne dit rien pendant un long moment, fixant "
  "l'&eacute;cran comme s'il pouvait, &agrave; force de silence, r&eacute;v&eacute;ler "
  "de lui-m&ecirc;me le contenu de cette page manquante que le "
  "syst&egrave;me refuse, pour une raison qu'aucun d'eux ne "
  "ma&icirc;trise encore, de leur montrer directement.")

p("Darius sait d&eacute;j&agrave;, avant m&ecirc;me de taper la commande, quel "
  "num&eacute;ro il va chercher, et ses doigts tremblent l&eacute;g&egrave;rement "
  "en tapant les trois chiffres sur le vieux clavier poussi&eacute;reux "
  "&mdash; 404 &mdash; avant d'appuyer sur la touche qui, dans cette "
  "maison oubli&eacute;e de tous sauf d'eux trois, pourrait enfin "
  "ouvrir la seule page que ni l'entrep&ocirc;t, ni le Non-lieu, ni sa "
  "propre m&eacute;moire, ne lui ont jamais laiss&eacute; lire jusqu'au "
  "bout.")

p("L'&eacute;cran met de longues secondes &agrave; r&eacute;agir, un sablier "
  "qui tourne sur fond noir, assez longtemps pour que tous "
  "les trois retiennent leur souffle sans se concerter, avant "
  "qu'un unique message n'apparaisse, en lettres blanches "
  "simples, sans fioriture : &laquo;&nbsp;page 404 &mdash; contenu introuvable "
  "&mdash; ou pas encore &eacute;crit.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a veut dire quoi, &ccedil;a, 'pas encore &eacute;crit' ? On dirait "
  "presque que &ccedil;a nous parle directement, comme si la page "
  "attendait qu'on fasse quelque chose avant de se remplir "
  "toute seule.&nbsp;&raquo;")

p("Darius referme lentement le vieil ordinateur, sentant, pour "
  "la premi&egrave;re fois depuis des semaines, non pas de la peur, "
  "mais une forme &eacute;trange de soulagement &mdash; l'id&eacute;e que la "
  "page 404 n'est peut-&ecirc;tre pas un secret qu'on lui cache, mais "
  "un espace encore vide qu'il lui reste, &agrave; lui et &agrave; personne "
  "d'autre, &agrave; remplir.")

p("Ils quittent la maison Vasseur avant la nuit, refermant "
  "derri&egrave;re eux la grille rouill&eacute;e avec la m&ecirc;me pr&eacute;caution "
  "qu'on referme la porte d'un lieu qu'on sait devoir "
  "revisiter un jour, et p&eacute;dalent en silence sur la route qui "
  "les ram&egrave;ne vers Luynes, chacun perdu dans ce que cette "
  "journ&eacute;e vient de leur r&eacute;v&eacute;ler sur la famille de Darius.")

p("Ce soir-l&agrave;, avant de dormir, Darius remet son casque et "
  "ajoute, sans trop savoir pourquoi, une simple porte close "
  "&agrave; la fin de son niveau, une porte qu'il ne sait pas encore "
  "comment ouvrir dans le jeu, mais qui lui semble, tout &agrave; "
  "coup, ressembler &eacute;trangement &agrave; cette page 404 qu'il "
  "vient de laisser derri&egrave;re lui &agrave; Fondettes.")

p("Il travaille tard sur cette porte, ajustant sa texture, la "
  "lumi&egrave;re qui devrait filtrer dessous si jamais elle "
  "s'entrouvrait un jour, avec une concentration presque "
  "fi&eacute;vreuse qui finit par inqui&eacute;ter sa m&egrave;re, laquelle passe "
  "la t&ecirc;te par la porte de sa chambre pour lui rappeler, pas "
  "franchement pour la premi&egrave;re fois, qu'il existe une vie en "
  "dehors de cet &eacute;cran.")

name("MERE DE DARIUS")
p("&laquo;&nbsp;&Ccedil;a fait trois heures que t'as ce truc sur la t&ecirc;te, "
  "mon grand. &Ccedil;a doit &ecirc;tre bien, ton jeu, mais &eacute;teins-moi &ccedil;a "
  "et viens dormir normalement, s'il te pla&icirc;t.&nbsp;&raquo;")

p("Il obtemp&egrave;re avec un sourire d'excuse, retirant le casque "
  "&agrave; regret, comme on quitte un endroit o&ugrave; l'on se sent, "
  "pour une fois, enti&egrave;rement ma&icirc;tre de ce qui s'y passe &mdash; "
  "et s'endort presque aussit&ocirc;t, l'esprit encore plein de "
  "couloirs et de portes qu'il n'a pas fini de dessiner.")

p("Il r&ecirc;ve, cette nuit-l&agrave;, d'un couloir sans fin bord&eacute; de "
  "portes identiques, et d'une voix qui n'est pas tout &agrave; fait "
  "la sienne qui lui souffle, quelque part derri&egrave;re son "
  "&eacute;paule, qu'il en reste une seule &agrave; ouvrir, une seule qui "
  "compte vraiment, avant que le r&ecirc;ve ne se dissolve, comme "
  "toujours, avant qu'il n'ait pu en franchir le seuil.")

p("Darius finit par poser l'enveloppe kraft sur la table de la "
  "cuisine, un mardi soir, sans pr&eacute;venir, pendant que Franck "
  "d&eacute;barrasse les assiettes du d&icirc;ner &mdash; un geste brutal, "
  "presque involontaire, comme s'il avait fallu, pour trouver "
  "enfin le courage, ne plus se laisser le temps de "
  "r&eacute;fl&eacute;chir.")

p("Franck se fige, une assiette encore &agrave; la main, le regard "
  "fix&eacute; sur le logo tap&eacute; en en-t&ecirc;te du premier feuillet, et "
  "Darius voit, pour la premi&egrave;re fois de sa vie, quelque "
  "chose se briser sur le visage de son p&egrave;re avec une "
  "rapidit&eacute; presque effrayante &mdash; non pas de la col&egrave;re, mais "
  "une terreur ancienne, remont&eacute;e d'un coup depuis un endroit "
  "qu'il croyait avoir scell&eacute; pour de bon.")

name("FRANCK")
p("&laquo;&nbsp;O&ugrave; est-ce que t'as trouv&eacute; &ccedil;a. Dis-moi o&ugrave; t'as trouv&eacute; "
  "&ccedil;a, Darius, tout de suite.&nbsp;&raquo;")

p("Sa voix tremble d'une mani&egrave;re que Darius ne lui a jamais "
  "connue, m&ecirc;me pas le jour o&ugrave; il lui avait annonc&eacute;, "
  "enfant, que Miel &eacute;tait &laquo;&nbsp;parti en vacances&nbsp;&raquo;, et il comprend, "
  "&agrave; cet instant pr&eacute;cis, que ce mensonge-l&agrave; n'&eacute;tait peut-&ecirc;tre "
  "que le premier d'une longue liste que son p&egrave;re porte "
  "depuis bien plus longtemps qu'il ne l'imaginait.")

name("DARIUS")
p("&laquo;&nbsp;Chez toi. Dans ton tiroir. J'&eacute;tais pas venu pour "
  "fouiller, je te jure, mais j'ai trouv&eacute; &ccedil;a, et apr&egrave;s j'ai "
  "trouv&eacute; la maison &agrave; Fondettes, celle des Vasseur. Papa, "
  "pourquoi t'as jamais dit que tu t'appelais Vasseur avant "
  "de t'appeler Lenoir ?&nbsp;&raquo;")

p("Franck s'assoit lourdement, comme si ses jambes venaient "
  "de d&eacute;cider, seules, qu'elles ne pouvaient plus le porter, et "
  "reste un long moment silencieux, les mains &agrave; plat sur la "
  "table, fixant l'enveloppe sans oser la toucher, comme on "
  "regarde un objet qu'on sait capable de tout faire "
  "s'effondrer d'un seul contact.")

name("FRANCK")
p("&laquo;&nbsp;J'avais sept ans. J'me souviens pas de grand-chose, "
  "honn&ecirc;tement &mdash; des couloirs blancs, une pi&egrave;ce o&ugrave; on me "
  "faisait porter un genre de casque, et mon fr&egrave;re, un peu "
  "plus grand que moi, qui passait des heures dans une autre "
  "pi&egrave;ce au bout du couloir. Apr&egrave;s &ccedil;a, ma m&egrave;re m'a "
  "emmen&eacute; loin, tr&egrave;s loin, et on n'en a plus jamais "
  "reparl&eacute;. Jamais.&nbsp;&raquo;")

p("Darius s'assoit &agrave; son tour, en face de lui, sentant "
  "confus&eacute;ment qu'il vient de d&eacute;clencher quelque chose qui "
  "ne pourra plus s'arr&ecirc;ter en cours de route, et pose la "
  "question qui lui br&ucirc;le les l&egrave;vres depuis des semaines, "
  "presque malgr&eacute; lui.")

name("DARIUS")
p("&laquo;&nbsp;Ton fr&egrave;re. C'&eacute;tait Kayden ?&nbsp;&raquo;")

p("Franck ferme les yeux longuement avant de r&eacute;pondre, "
  "comme s'il fallait rassembler une force qu'il n'avait plus "
  "utilis&eacute;e depuis des d&eacute;cennies pour prononcer &agrave; voix haute "
  "un nom qu'il avait fini par croire enterr&eacute; avec le reste.")

name("FRANCK")
p("&laquo;&nbsp;Oui. Kayden. J'ai pass&eacute; trente ans &agrave; me convaincre "
  "que j'avais r&ecirc;v&eacute; tout &ccedil;a, ou que c'&eacute;tait juste des "
  "souvenirs d'enfant d&eacute;form&eacute;s. Et toi, tu me dis que tu "
  "l'as... rencontr&eacute; ? Que tu l'as vu, l&agrave;, r&eacute;cemment ?&nbsp;&raquo;")

p("Darius hoche la t&ecirc;te, incapable de trouver les mots pour "
  "expliquer &agrave; son p&egrave;re, en une seule soir&eacute;e, tout ce qu'il a "
  "travers&eacute; dans le Non-lieu, et se contente, pour l'instant, "
  "d'une version courte, prudente, laissant volontairement de "
  "c&ocirc;t&eacute; le d&eacute;tail de la possession dans le corps de Darius "
  "lui-m&ecirc;me, pas encore pr&ecirc;t &agrave; infliger &ccedil;a &agrave; son p&egrave;re ce "
  "soir-l&agrave;.")

p("Franck l'&eacute;coute sans l'interrompre une seule fois, les "
  "yeux embu&eacute;s, hochant la t&ecirc;te de temps en temps comme "
  "pour confirmer int&eacute;rieurement des d&eacute;tails qu'il croyait "
  "avoir invent&eacute;s, et quand Darius se tait enfin, un long "
  "silence s'installe entre eux, plus lourd qu'aucun des "
  "silences qu'ils avaient jusque-l&agrave; partag&eacute;s.")

name("FRANCK")
p("&laquo;&nbsp;J'aurais d&ucirc; te le dire. Pas tout, j'en &eacute;tais m&ecirc;me pas "
  "capable, mais au moins &ccedil;a &mdash; que j'avais un fr&egrave;re, que "
  "j'ai jamais su ce qu'il &eacute;tait devenu, que j'ai pass&eacute; ma vie "
  "&agrave; faire comme si cette partie de moi n'avait jamais "
  "exist&eacute;. J'suis d&eacute;sol&eacute;, Darius. Vraiment.&nbsp;&raquo;")

p("Ils restent tous les deux dans la cuisine bien apr&egrave;s que "
  "le caf&eacute; a refroidi dans leurs tasses, Franck racontant, par "
  "fragments d&eacute;cousus, ce qu'il parvient encore &agrave; retrouver "
  "de ces ann&eacute;es effac&eacute;es &mdash; une salle d'attente, une "
  "odeur d&eacute;sinfectante, une main de sa m&egrave;re trop serr&eacute;e "
  "autour de la sienne dans un couloir trop blanc.")

p("Il se souvient surtout, dit-il, d'une sensation plut&ocirc;t que "
  "d'images pr&eacute;cises &mdash; celle d'&ecirc;tre observ&eacute; en permanence, "
  "&eacute;valu&eacute;, not&eacute; sur des grilles qu'on ne lui montrait jamais, "
  "et d'un fr&egrave;re a&icirc;n&eacute; qui, contrairement &agrave; lui, semblait "
  "presque appr&eacute;cier cette attention constante, comme si "
  "elle comblait, chez lui, un vide que Franck ne comprenait "
  "pas encore.")

name("FRANCK")
p("&laquo;&nbsp;Kayden voulait qu'on le remarque. Toujours. Je me "
  "souviens de &ccedil;a tr&egrave;s clairement, m&ecirc;me apr&egrave;s tout ce "
  "temps &mdash; il disait tout le temps un truc du genre 'je "
  "veux que &ccedil;a compte', comme une petite phrase &agrave; lui, qu'il "
  "r&eacute;p&eacute;tait d&egrave;s qu'on lui demandait de recommencer un "
  "exercice.&nbsp;&raquo;")

p("Darius sent un frisson lui remonter le long de la nuque en "
  "entendant cette phrase, exactement celle que Kayden avait "
  "prononc&eacute;e dans le Non-lieu au moment de se dissoudre, "
  "et comprend, avec un vertige nouveau, que cette phrase "
  "n'&eacute;tait pas n&eacute;e dans l'entrep&ocirc;t ni dans la machine &mdash; "
  "qu'elle appartenait &agrave; un petit gar&ccedil;on bien avant de "
  "devenir celle d'une architecture de donn&eacute;es en train de "
  "s'effondrer.")

p("Franck explique, la voix de plus en plus basse, que sa "
  "propre m&egrave;re avait fini par demander son retrait du "
  "programme apr&egrave;s avoir surpris, un jour, une conversation "
  "entre m&eacute;decins &eacute;voquant des &laquo;&nbsp;effets secondaires "
  "irr&eacute;versibles&nbsp;&raquo; chez les patients les plus avanc&eacute;s &mdash; "
  "sans jamais savoir avec certitude si Kayden en faisait "
  "d&eacute;j&agrave; partie, ni ce que ces mots signifiaient r&eacute;ellement.")

name("FRANCK")
p("&laquo;&nbsp;Elle a coup&eacute; les ponts d'un coup. Nouveau nom, "
  "nouvelle ville, plus jamais un mot sur Kayden ni sur le "
  "programme. J'ai grandi en pensant que j'avais peut-&ecirc;tre "
  "invent&eacute; tout &ccedil;a, ou que c'&eacute;tait juste un mauvais r&ecirc;ve "
  "d'enfant. J'ai jamais os&eacute; creuser. J'avais trop peur de ce "
  "que j'allais trouver.&nbsp;&raquo;")

p("Darius pense, en l'&eacute;coutant, &agrave; sa propre fa&ccedil;on de classer "
  "les choses trop douloureuses dans la case &laquo;&nbsp;n'y touche "
  "pas&nbsp;&raquo; plut&ocirc;t que de les affronter, et r&eacute;alise, avec un "
  "m&eacute;lange de tendresse et de tristesse, &agrave; quel point cette "
  "habitude ne lui appartient pas en propre, mais s'est "
  "transmise, silencieuse, d'une g&eacute;n&eacute;ration &agrave; l'autre.")

name("DARIUS")
p("&laquo;&nbsp;Tu savais pas, pour Miel non plus. Enfin si, tu savais, "
  "mais tu m'as dit qu'il &eacute;tait parti en vacances. Tu crois que "
  "&ccedil;a vient de l&agrave; ? De cette histoire, avec ton fr&egrave;re, cette "
  "mani&egrave;re de tout enterrer plut&ocirc;t que d'en parler ?&nbsp;&raquo;")

p("Franck met longtemps &agrave; r&eacute;pondre, le regard perdu vers la "
  "fen&ecirc;tre, et quand il le fait, sa voix porte une honn&ecirc;tet&eacute; "
  "que Darius ne lui avait encore jamais enti&egrave;rement entendue, "
  "d&eacute;pouill&eacute;e de toute excuse toute faite.")

name("FRANCK")
p("&laquo;&nbsp;Probablement, oui. J'ai jamais voulu regarder &ccedil;a en "
  "face avant aujourd'hui, mais &ccedil;a fait sens, d'une mani&egrave;re "
  "affreuse. J'ai appris, gamin, que mentir gentiment fait "
  "moins mal que dire la v&eacute;rit&eacute; brutalement. Sauf que j'ai "
  "jamais compris que le mensonge, lui, il finit toujours "
  "par revenir, encore plus fort.&nbsp;&raquo;")

p("Ils restent silencieux un moment, chacun mesurant &agrave; sa "
  "mani&egrave;re le poids de ce qui vient d'&ecirc;tre dit, avant que "
  "Franck ne pose sa main, maladroitement, sur celle de son "
  "fils, un geste rare entre eux, presque timide, mais qui vaut, "
  "ce soir-l&agrave;, plus que n'importe quelle phrase.")

name("FRANCK")
p("&laquo;&nbsp;Je vais essayer de faire autrement, &agrave; partir de "
  "maintenant. Je promets rien de parfait, j'suis pas doou&eacute; "
  "pour &ccedil;a, mais j'essaierai de te dire les choses, m&ecirc;me "
  "quand &ccedil;a fait peur.&nbsp;&raquo;")

p("Alex remarque le premier changement un jeudi matin, en "
  "enfilant son maillot avant l'entra&icirc;nement de foot, quand la "
  "fine cicatrice blanche sur son avant-bras se met &agrave; le "
  "d&eacute;manger d'une mani&egrave;re qu'il ne lui avait jamais connue "
  "depuis qu'elle est apparue &mdash; une sensation br&ucirc;lante, "
  "br&egrave;ve, comme un courant &eacute;lectrique remontant sous la "
  "peau.")

name("ALEX")
p("&laquo;&nbsp;&Ccedil;a m'a fait un truc bizarre, l&agrave;, sur le bras. Comme "
  "une d&eacute;charge. C'est pass&eacute; vite, mais j'ai eu l'impression "
  "que &ccedil;a venait pile de l&agrave; o&ugrave; est la cicatrice, tu vois, "
  "l'ancienne, celle du Non-lieu.&nbsp;&raquo;")

p("Darius examine le bras de son ami avec une attention "
  "presque clinique, cherchant un changement visible, une "
  "trace suppl&eacute;mentaire, mais ne trouve rien d'autre que la "
  "cicatrice habituelle, parfaitement immobile, comme si "
  "l'&eacute;pisode n'avait laiss&eacute; aucune preuve derri&egrave;re lui, si ce "
  "n'est le souvenir tr&egrave;s pr&eacute;cis qu'en garde Alex.")

p("Le ph&eacute;nom&egrave;ne se r&eacute;p&egrave;te deux jours plus tard, cette "
  "fois accompagn&eacute; d'un mot, un seul, qu'Alex jure avoir "
  "entendu murmurer tr&egrave;s pr&egrave;s de son oreille sans que "
  "personne ne se trouve &agrave; proximit&eacute; &mdash; un mot qu'il ne "
  "comprend pas, dans une langue qu'il ne parle pas, mais "
  "qui, une fois rapport&eacute; &agrave; Darius, lui glace instantan&eacute;ment "
  "le sang.")

name("ALEX")
p("&laquo;&nbsp;'Compter'. Juste &ccedil;a, 'compter', dit tout doucement, "
  "presque coll&eacute; contre mon oreille. J'ai d&ucirc; r&ecirc;ver, non ? Dis-moi "
  "que j'ai r&ecirc;v&eacute;, Darius, parce que ta t&ecirc;te, l&agrave;, elle me "
  "rassure pas du tout.&nbsp;&raquo;")

p("Darius pense imm&eacute;diatement &agrave; la phrase de Kayden, &laquo;&nbsp;je "
  "voulais juste que &ccedil;a compte&nbsp;&raquo;, &agrave; celle rapport&eacute;e par "
  "Franck, identique, prononc&eacute;e des d&eacute;cennies plus t&ocirc;t par un "
  "petit gar&ccedil;on avide d'attention, et comprend que si un "
  "fragment de Kayden subsiste vraiment quelque part, il "
  "semble chercher, d'une mani&egrave;re ou d'une autre, &agrave; se "
  "manifester non seulement &agrave; lui, mais aussi &agrave; travers Alex, "
  "l&agrave; o&ugrave; une trace physique du Non-lieu est rest&eacute;e "
  "grav&eacute;e.")

p("Il explique &agrave; Alex, avec toute la prudence possible, ce "
  "qu'il a appris r&eacute;cemment sur Franck, sur Kayden, sur cette "
  "phrase r&eacute;p&eacute;t&eacute;e depuis l'enfance, et voit sur le visage de "
  "son ami une inqui&eacute;tude sinc&egrave;re se m&ecirc;ler &agrave; une forme de "
  "curiosit&eacute; presque malgr&eacute; lui, comme chaque fois que "
  "l'impossible finit par frapper &agrave; sa porte sans qu'il puisse "
  "vraiment s'en d&eacute;tourner.")

name("ALEX")
p("&laquo;&nbsp;Donc quoi, j'suis genre... connect&eacute; &agrave; lui, maintenant, "
  "&agrave; cause de cette cicatrice ? Super. G&eacute;nial. J'avais "
  "justement besoin d'un truc en plus &agrave; g&eacute;rer cette "
  "ann&eacute;e.&nbsp;&raquo;")

p("Malgr&eacute; le ton d&eacute;sabus&eacute;, Darius sent qu'Alex prend la "
  "chose avec plus de calme qu'il ne l'aurait cru, comme si "
  "leur histoire commune leur avait, &agrave; tous les trois, appris &agrave; "
  "encaisser l'&eacute;trange avec une forme d'humour d&eacute;fensif "
  "plut&ocirc;t que de panique pure.")

p("Ils d&eacute;cident, ce soir-l&agrave;, de surveiller ensemble tout signe "
  "suppl&eacute;mentaire venant de la cicatrice, notant scrupuleusement "
  "dans le carnet de Clara chaque d&eacute;charge, chaque mot "
  "entendu, avec la certitude grandissante que ce fragment "
  "de Kayden, quel qu'il soit devenu, cherche &agrave; leur dire "
  "quelque chose de pr&eacute;cis, sans encore savoir en formuler "
  "davantage que des &eacute;clats.")

p("Le carnet de Clara change de comportement une semaine "
  "plus tard, exactement comme il l'avait fait pendant les "
  "&eacute;v&eacute;nements du Non-lieu &mdash; une page se remplit d'elle-m&ecirc;me "
  "pendant la nuit, d'une &eacute;criture serr&eacute;e qui n'est pas celle "
  "de Clara, retrouv&eacute;e au matin ouverte sur son bureau alors "
  "qu'elle jurerait l'avoir rang&eacute; ferm&eacute; la veille.")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a a recommenc&eacute;. Regarde &ccedil;a, Darius, c'est pas mon "
  "&eacute;criture, m&ecirc;me si c'est mon carnet. &Ccedil;a dit un truc que je "
  "comprends pas du tout.&nbsp;&raquo;")

p("La page contient une seule phrase, r&eacute;p&eacute;t&eacute;e trois fois de "
  "suite, chaque occurrence l&eacute;g&egrave;rement diff&eacute;rente de la "
  "pr&eacute;c&eacute;dente, comme un brouillon qui chercherait sa forme "
  "d&eacute;finitive : &laquo;&nbsp;je ne suis pas revenu. je suis rest&eacute; "
  "&eacute;parpill&eacute;. il reste une page o&ugrave; je ne suis pas encore "
  "compl&egrave;tement effac&eacute;.&nbsp;&raquo;")

p("Ils se retrouvent tous les trois ce soir-l&agrave; chez Clara, "
  "posant le carnet, le pon&ccedil;on et le b&acirc;ton c&ocirc;te &agrave; c&ocirc;te sur son "
  "bureau, comme pour v&eacute;rifier, une fois de plus, que ces "
  "objets continuent de r&eacute;agir ensemble d'une mani&egrave;re que "
  "la science ordinaire ne saurait expliquer.")

p("Le pon&ccedil;on, gliss&eacute; sous la lampe de bureau, projette une "
  "ombre l&eacute;g&egrave;rement d&eacute;form&eacute;e sur le mur, comme si le "
  "&laquo;&nbsp;K.&nbsp;&raquo; grav&eacute; dessus tremblait imperceptiblement &mdash; un "
  "d&eacute;tail que ni Clara ni Alex ne remarquent, mais que Darius, "
  "lui, distingue tr&egrave;s clairement, avec une intensit&eacute; qui lui "
  "rappelle d&eacute;sagr&eacute;ablement les premiers signes annonciateurs "
  "de la possession dans le Non-lieu.")

name("DARIUS")
p("&laquo;&nbsp;Il essaie de communiquer, pas de revenir. Je crois "
  "qu'il y a une diff&eacute;rence importante entre les deux, et "
  "j'aimerais bien qu'on essaie de comprendre laquelle avant "
  "de paniquer pour rien.&nbsp;&raquo;")

p("Alex propose, avec cette pragmatisme qui le caract&eacute;rise "
  "quand il refuse de se laisser submerger par la peur, "
  "d'essayer de r&eacute;pondre directement dans le carnet, comme "
  "on r&eacute;pondrait &agrave; un message, plut&ocirc;t que de se contenter "
  "d'observer passivement ce que le fragment choisit de leur "
  "montrer.")

name("ALEX")
p("&laquo;&nbsp;On lui &eacute;crit un truc genre 'qu'est-ce que tu veux "
  "vraiment', direct, sans tourner autour du pot. Si &ccedil;a marche "
  "pas, on aura rien perdu. Si &ccedil;a marche, on saura enfin &agrave; "
  "quoi s'attendre.&nbsp;&raquo;")

p("Clara &eacute;crit la phrase de sa propre main, avec une "
  "h&eacute;sitation visible, et referme le carnet aussit&ocirc;t apr&egrave;s, "
  "comme si le geste lui-m&ecirc;me co&ucirc;tait un effort physique "
  "particulier, et ils passent le reste de la soir&eacute;e &agrave; attendre, "
  "sans grande conviction, une r&eacute;ponse qui ne vient pas "
  "imm&eacute;diatement.")

p("C'est seulement au petit matin, quand Clara rouvre le "
  "carnet avant de partir en cours, qu'une nouvelle ligne "
  "appara&icirc;t sous leur question, courte, presque douloureuse "
  "&agrave; lire pour qui conna&icirc;t d&eacute;j&agrave; toute l'histoire de Kayden : "
  "&laquo;&nbsp;je veux juste qu'on arr&ecirc;te de m'oublier une deuxi&egrave;me "
  "fois.&nbsp;&raquo;")

p("La phrase les hante tous les trois pendant des jours, "
  "chacun &agrave; sa mani&egrave;re &mdash; Clara la recopie plusieurs fois "
  "dans un coin de son carnet comme pour l'apprivoiser, Alex "
  "&eacute;vite d'en parler tout en gardant, malgr&eacute; lui, la main "
  "pos&eacute;e sur sa cicatrice plus souvent qu'avant, et Darius, "
  "lui, sent na&icirc;tre une culpabilit&eacute; diffuse qu'il n'avait pas "
  "anticip&eacute;e.")

p("Il se souvient de sa propre phrase, prononc&eacute;e au c&oelig;ur du "
  "Non-lieu, cens&eacute;e servir de d&eacute;livrance et non de sentence "
  "&mdash; &laquo;&nbsp;on ne t'oublie pas, on te pardonne pas non plus, mais "
  "on arr&ecirc;te de te nourrir&nbsp;&raquo; &mdash; et se demande, pour la "
  "premi&egrave;re fois depuis qu'il l'a prononc&eacute;e, si cette phrase "
  "n'a pas, sans qu'il le veuille, condamn&eacute; Kayden &agrave; une "
  "forme d'exil pire encore que la dissolution compl&egrave;te.")

name("DARIUS")
p("&laquo;&nbsp;Et si j'avais eu tort ? Si en refusant de le nourrir on "
  "l'avait juste laiss&eacute; l&agrave;, &eacute;parpill&eacute;, conscient de l'&ecirc;tre, "
  "sans jamais pouvoir ni revenir ni dispara&icirc;tre pour de bon ? "
  "&Ccedil;a serait pire que tout ce qu'on avait imagin&eacute;.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;On pouvait pas savoir &ccedil;a &agrave; l'&eacute;poque. Et m&ecirc;me "
  "maintenant, on sait pas vraiment ce qu'il est devenu, ni ce "
  "qu'il veut dire par 'oublier une deuxi&egrave;me fois'. &Ccedil;a peut "
  "vouloir dire plein de choses, Darius, pas forc&eacute;ment ce que "
  "t'imagines de pire.&nbsp;&raquo;")

p("Ils d&eacute;cident, apr&egrave;s une longue discussion, de ne pas "
  "chercher &agrave; ramener Kayden davantage, ni &agrave; le repousser "
  "brutalement, mais simplement &agrave; continuer d'&eacute;couter, comme "
  "on laisse une porte entrouverte sans forcer personne &agrave; "
  "franchir le seuil dans un sens ou dans l'autre.")

p("Darius retourne, ce soir-l&agrave;, &agrave; son projet de jeu, "
  "casque viss&eacute; sur les yeux, et travaille longuement sur "
  "cette porte close ajout&eacute;e quelques semaines plus t&ocirc;t &mdash; "
  "sans savoir encore qu'en dessinant, minutieusement, ce "
  "qu'il imagine se trouver derri&egrave;re elle, il donne "
  "involontairement une forme, un lieu, presque une adresse, "
  "&agrave; quelque chose qui n'en avait plus depuis longtemps.")

p("Il ajoute, cette nuit-l&agrave;, un petit d&eacute;tail sans trop y penser "
  "&mdash; une lumi&egrave;re bleue clignotante, discr&egrave;te, plac&eacute;e juste "
  "au-dessus de la porte, comme un signal qu'on laisserait "
  "allum&eacute; pour quelqu'un qu'on esp&egrave;re encore voir revenir un "
  "jour, sans se l'avouer clairement &agrave; lui-m&ecirc;me.")

p("Le lendemain matin, une derni&egrave;re ligne s'ajoute au carnet "
  "de Clara, plus calme que les pr&eacute;c&eacute;dentes, presque "
  "apais&eacute;e : &laquo;&nbsp;merci pour la lumi&egrave;re. &ccedil;a fait longtemps que "
  "personne n'en avait laiss&eacute; une allum&eacute;e pour moi.&nbsp;&raquo;")

p("Darius referme le carnet, troubl&eacute; par une pens&eacute;e qu'il "
  "n'ose formuler enti&egrave;rement &agrave; voix haute &mdash; que son jeu, "
  "cet espace qu'il croyait construire seul, enti&egrave;rement sous "
  "son contr&ocirc;le, pourrait bien, sans qu'il l'ait voulu, &ecirc;tre "
  "devenu un pont vers autre chose que le simple divertissement "
  "qu'il pensait y avoir mis.")

p("Il en parle, le lendemain, &agrave; Clara et Alex, "
  "partageant avec eux cette d&eacute;couverte troublante "
  "d'une communication &eacute;tablie, sans qu'il l'ait cherch&eacute; "
  "explicitement, entre son propre jeu et ce qui reste "
  "de Kayden, et les trouve, tous deux, partag&eacute;s entre "
  "une fascination sinc&egrave;re et une inqui&eacute;tude renouvel&eacute;e "
  "pour l'&eacute;quilibre mental de leur ami.")

name("CLARA")
p("&laquo;&nbsp;C'est beau, ce que tu d&eacute;cris, cette id&eacute;e d'une "
  "lumi&egrave;re laiss&eacute;e allum&eacute;e pour quelqu'un qui "
  "esp&egrave;re revenir. Mais &ccedil;a m'inqui&egrave;te un peu aussi, "
  "Darius. T'es s&ucirc;r que c'est toi qui contr&ocirc;les encore "
  "cette histoire, et pas l'inverse ?&nbsp;&raquo;")

p("Darius n'a pas de r&eacute;ponse pleinement rassurante &agrave; "
  "offrir, conscient lui-m&ecirc;me que la fronti&egrave;re entre "
  "cr&eacute;ation personnelle et communication involontaire "
  "avec un fragment de Kayden devient, chaque semaine "
  "un peu plus, difficile &agrave; tracer clairement, mais "
  "refuse, malgr&eacute; tout, d'envisager s&eacute;rieusement "
  "l'id&eacute;e d'abandonner ce projet devenu, avec le temps, "
  "aussi pr&eacute;cieux qu'un journal intime.")

name("DARIUS")
p("&laquo;&nbsp;Je crois que je contr&ocirc;le encore l'essentiel. "
  "Mais j'avoue que &ccedil;a devient dur de savoir o&ugrave; "
  "s'arr&ecirc;te ma propre imagination et o&ugrave; commence "
  "vraiment autre chose. Peut-&ecirc;tre que c'est &ccedil;a, en "
  "fait, le vrai risque de porter ce r&ocirc;le &mdash; perdre "
  "progressivement la certitude de savoir qui d&eacute;cide, "
  "vraiment, de ce qui se passe.&nbsp;&raquo;")

p("Alex, jusque-l&agrave; silencieux, propose une solution "
  "pragmatique qu'ils n'avaient pas encore envisag&eacute;e "
  "&mdash; instaurer une r&egrave;gle simple selon laquelle Darius "
  "ne travaillerait plus jamais seul sur son jeu apr&egrave;s "
  "une certaine heure, et surtout, ne l'utiliserait "
  "plus jamais sans qu'au moins l'un d'eux deux soit "
  "inform&eacute; pr&eacute;cis&eacute;ment de la session en cours.")

name("ALEX")
p("&laquo;&nbsp;On pourrait genre s'envoyer un message avant "
  "et apr&egrave;s chaque fois que tu mets le casque, comme "
  "&ccedil;a on sait toujours si t'es dedans, et pour combien "
  "de temps. &Ccedil;a co&ucirc;te rien d'essayer, et &ccedil;a nous "
  "rassurerait tous les deux, je pense.&nbsp;&raquo;")

p("Darius accepte cette proposition avec un "
  "soulagement sinc&egrave;re, reconnaissant dans cette "
  "solution simple un &eacute;quilibre acceptable entre sa "
  "passion cr&eacute;ative et la s&eacute;curit&eacute; que ses amis "
  "cherchent, l&eacute;gitimement, &agrave; lui garantir, et instaure "
  "d&egrave;s le soir m&ecirc;me cette nouvelle habitude qui "
  "deviendra, dans les mois suivants, une routine "
  "rassurante pour tous les trois.")

p("Cette nouvelle habitude, aussi simple soit-elle "
  "en apparence, transforme progressivement la "
  "relation des trois amis avec le jeu de Darius, "
  "Clara et Alex se mettant &agrave; poser des questions "
  "de plus en plus pr&eacute;cises sur chaque nouvel &eacute;l&eacute;ment "
  "ajout&eacute;, cherchant &agrave; comprendre non seulement le "
  "contenu narratif mais aussi la port&eacute;e symbolique de "
  "chaque choix cr&eacute;atif effectu&eacute; par leur ami.")

name("CLARA")
p("&laquo;&nbsp;Pourquoi t'as choisi cette couleur pr&eacute;cise de "
  "bleu, pour la lumi&egrave;re de la porte ? &Ccedil;a a une "
  "signification particuli&egrave;re, ou c'est juste "
  "esth&eacute;tique ?&nbsp;&raquo;")

p("Darius r&eacute;fl&eacute;chit un instant avant de r&eacute;pondre, "
  "surpris lui-m&ecirc;me de devoir formuler explicitement "
  "des intentions cr&eacute;atives qui, jusque-l&agrave;, "
  "relevaient davantage de l'instinct que d'un choix "
  "raisonn&eacute;, et r&eacute;alise, en cherchant ses mots, &agrave; "
  "quel point son processus cr&eacute;atif puise, sans qu'il "
  "en ait toujours pleinement conscience, dans les "
  "&eacute;motions les plus profondes li&eacute;es &agrave; cette histoire "
  "extraordinaire qu'ils vivent ensemble.")

name("DARIUS")
p("&laquo;&nbsp;J'sais pas trop, en fait. &Ccedil;a m'est venu comme "
  "&ccedil;a, cette teinte pr&eacute;cise. Je crois que &ccedil;a "
  "repr&eacute;sente un peu l'espoir, pour moi, cette id&eacute;e "
  "qu'il y a toujours une petite lumi&egrave;re quelque part, "
  "m&ecirc;me dans les endroits les plus sombres qu'on "
  "traverse.&nbsp;&raquo;")

p("Cette conversation, apparemment anodine, marque "
  "un tournant subtil dans la mani&egrave;re dont les trois "
  "amis abordent d&eacute;sormais le jeu de Darius, le "
  "consid&eacute;rant progressivement moins comme un "
  "simple passe-temps personnel que comme un "
  "v&eacute;ritable espace de dialogue collectif sur tout ce "
  "qu'ils traversent ensemble, un langage commun "
  "capable d'exprimer des &eacute;motions que les mots seuls "
  "peinent parfois &agrave; transmettre.")

p("Alex, particuli&egrave;rement touch&eacute; par cette dimension "
  "nouvelle du projet, propose m&ecirc;me, un soir, "
  "d'ajouter au jeu un petit d&eacute;tail visuel repr&eacute;sentant "
  "sa propre cicatrice, comme une signature discr&egrave;te "
  "de sa propre contribution &agrave; cette histoire "
  "commune, une id&eacute;e que Darius accueille avec "
  "enthousiasme et int&egrave;gre d&egrave;s le lendemain soir dans "
  "l'apparence du personnage a&icirc;n&eacute; inspir&eacute; de "
  "Templier.")

p("Clara, de son c&ocirc;t&eacute;, sugg&egrave;re &agrave; son tour d'ajouter "
  "une repr&eacute;sentation symbolique de son propre "
  "carnet quelque part dans le jeu, imaginant un "
  "objet r&eacute;cup&eacute;rable par le joueur qui, une fois "
  "ouvert, r&eacute;v&eacute;lerait des fragments de texte &eacute;crits "
  "par les personnages secondaires, une mani&egrave;re "
  "&eacute;l&eacute;gante de transmettre de l'information narrative "
  "tout en rendant hommage &agrave; son propre r&ocirc;le dans "
  "cette histoire.")

name("CLARA")
p("&laquo;&nbsp;Genre, chaque fois qu'on trouve un de ces "
  "carnets cach&eacute;s dans un niveau, &ccedil;a d&eacute;bloquerait un "
  "peu plus l'histoire de la Marge, comme des indices "
  "&agrave; collectionner. &Ccedil;a rendrait le jeu plus "
  "int&eacute;ressant &agrave; explorer, non ?&nbsp;&raquo;")

p("Darius accueille cette id&eacute;e avec un enthousiasme "
  "sinc&egrave;re, y voyant l'occasion parfaite de transformer "
  "son projet personnel en une v&eacute;ritable &oelig;uvre "
  "collective, port&eacute;e &agrave; parts &eacute;gales par les trois "
  "amis, chacun contribuant &agrave; sa mani&egrave;re &agrave; cette "
  "&eacute;trange archive interactive de leur propre "
  "exp&eacute;rience extraordinaire.")

p("Les semaines suivantes voient ainsi le projet "
  "&eacute;voluer consid&eacute;rablement, passant d'un simple "
  "espace de jeu personnel &agrave; une v&eacute;ritable "
  "encyclop&eacute;die interactive de tout ce qu'ils ont appris "
  "sur la Marge, chaque nouveau niveau ajout&eacute; venant "
  "enrichir cette collection collective de savoirs "
  "durement acquis, transformant peu &agrave; peu ce qui "
  "n'&eacute;tait qu'un passe-temps solitaire en un v&eacute;ritable "
  "monument num&eacute;rique &eacute;lev&eacute; &agrave; leur amiti&eacute; et &agrave; leur "
  "courage partag&eacute;.")

p("Un soir, alors qu'ils testent ensemble une "
  "nouvelle version du niveau consacr&eacute; &agrave; la grotte du "
  "coteau, Alex propose d'ajouter une &eacute;nigme "
  "susuppl&eacute;mentaire bas&eacute;e sur les v&eacute;ritables inscriptions "
  "qu'ils avaient d&eacute;couvertes sur place, une id&eacute;e qui "
  "s&eacute;duit imm&eacute;diatement Darius, toujours &agrave; l'aff&ucirc;t de "
  "nouvelles mani&egrave;res d'ancrer son univers virtuel "
  "dans la r&eacute;alit&eacute; tangible de leur exp&eacute;rience "
  "commune.")

name("ALEX")
p("&laquo;&nbsp;On pourrait faire en sorte que le joueur "
  "doive reproduire exactement la s&eacute;quence des "
  "symboles qu'on avait vus grav&eacute;s dans la roche, "
  "tu te souviens ? &Ccedil;a rendrait hommage &agrave; ce "
  "moment-l&agrave; tout en cr&eacute;ant un vrai d&eacute;fi pour "
  "quiconque jouerait &agrave; &ccedil;a un jour.&nbsp;&raquo;")

p("Clara, consultant son carnet pour retrouver "
  "l'exacte disposition de ces symboles anciens, "
  "aide Darius &agrave; recr&eacute;er fid&egrave;lement cette &eacute;nigme "
  "dans le jeu, chacun apportant sa contribution "
  "sp&eacute;cifique &agrave; ce projet devenu, v&eacute;ritablement, un "
  "effort collectif refl&eacute;tant &agrave; la perfection "
  "l'&eacute;quilibre unique de leur amiti&eacute; &agrave; tous les "
  "trois.")

p("Ils passent plusieurs soir&eacute;es enti&egrave;res &agrave; peaufiner "
  "cette &eacute;nigme, testant et retestant la difficult&eacute; "
  "exacte n&eacute;cessaire pour qu'elle repr&eacute;sente un "
  "v&eacute;ritable d&eacute;fi sans devenir pour autant "
  "frustrante, Alex insistant particuli&egrave;rement sur "
  "l'importance de rendre hommage fid&egrave;lement &agrave; "
  "l'exp&eacute;rience r&eacute;elle qu'ils avaient v&eacute;cue dans "
  "cette grotte, refusant tout raccourci qui "
  "trahirait, m&ecirc;me l&eacute;g&egrave;rement, la v&eacute;rit&eacute; de leur "
  "aventure.")

name("DARIUS")
p("&laquo;&nbsp;J'aime bien cette id&eacute;e qu'on construit "
  "quelque chose qui va nous survivre, d'une "
  "certaine mani&egrave;re. M&ecirc;me si personne d'autre ne "
  "joue jamais &agrave; &ccedil;a, m&ecirc;me si &ccedil;a reste juste entre "
  "nous trois, &ccedil;a compte comme t&eacute;moignage de tout "
  "ce qu'on a v&eacute;cu ensemble.&nbsp;&raquo;")

p("Cette r&eacute;flexion, partag&eacute;e un soir tardif alors que "
  "la fatigue commence &agrave; se faire sentir chez tous "
  "les trois, marque une prise de conscience "
  "collective de l'importance v&eacute;ritable de ce projet "
  "&mdash; non pas simplement un jeu vid&eacute;o amateur, mais "
  "un v&eacute;ritable m&eacute;morial vivant de leur amiti&eacute; "
  "extraordinaire, con&ccedil;u pour perdurer bien "
  "au-del&agrave; de leur propre adolescence.")

p("Franck, tenu inform&eacute; r&eacute;guli&egrave;rement de "
  "l'avancement de ce projet par un Darius d&eacute;sormais "
  "beaucoup plus ouvert avec lui, propose un "
  "week-end de l'aider &agrave; sauvegarder correctement "
  "l'ensemble de son travail sur plusieurs supports "
  "diff&eacute;rents, ayant appris, dans sa vie "
  "professionnelle au garage, l'importance cruciale "
  "de ne jamais perdre un travail accompli avec "
  "autant de soin et d'investissement personnel.")

name("FRANCK")
p("&laquo;&nbsp;On sait jamais ce qui peut arriver &agrave; un "
  "ordinateur, fiston. Une panne, un virus, n'importe "
  "quoi. Sauvegarde toujours sur au moins deux "
  "supports diff&eacute;rents, c'est une r&egrave;gle d'or que "
  "j'applique depuis des ann&eacute;es pour mes propres "
  "dossiers professionnels.&nbsp;&raquo;")

p("Darius suit ce conseil paternel avec application, "
  "cr&eacute;ant d&eacute;sormais des copies r&eacute;guli&egrave;res de son "
  "travail sur un disque dur externe offert "
  "sp&eacute;cialement par Franck pour l'occasion, une "
  "pr&eacute;caution qui semblera, avec le recul des "
  "&eacute;v&eacute;nements &agrave; venir, presque prémonitoire tant "
  "elle permettra, bien plus tard, &agrave; Clara et Alex de "
  "pr&eacute;server int&eacute;gralement ce t&eacute;moignage num&eacute;rique "
  "pr&eacute;cieux apr&egrave;s la disparition de son cr&eacute;ateur.")

p("Ce week-end pass&eacute; ensemble &agrave; organiser "
  "m&eacute;thodiquement les sauvegardes num&eacute;riques "
  "devient, sans que ni l'un ni l'autre ne "
  "l'anticipe vraiment, un moment de compl&eacute;mentarit&eacute; "
  "technique et affective pr&eacute;cieux entre Franck et "
  "son fils, l'un expliquant patiemment les "
  "principes de redondance informatique, l'autre "
  "partageant avec enthousiasme chaque d&eacute;tail "
  "cr&eacute;atif de son projet, dans une complicit&eacute; "
  "nouvelle qui n'aurait sembl&eacute; envisageable, "
  "quelques mois plus t&ocirc;t seulement, &agrave; aucun des "
  "deux.")

name("FRANCK")
p("&laquo;&nbsp;Je suis vraiment impressionn&eacute; par tout ce "
  "que t'as construit, Darius. J'aurais jamais "
  "imagin&eacute; que t'avais un tel talent technique et "
  "cr&eacute;atif en toi. &Ccedil;a me rend fier, sinc&egrave;rement, "
  "de voir &ccedil;a.&nbsp;&raquo;")

p("Ce week-end technique se termine par un repas "
  "simple partag&eacute; tous les deux dans la petite "
  "cuisine de Franck, une pizza command&eacute;e pour "
  "l'occasion, et Darius, savourant ce moment de "
  "compl&eacute;tude tranquille avec son p&egrave;re, se dit "
  "qu'il aurait aim&eacute; que ces instants de "
  "compl&eacute;mentarit&eacute; simple existent depuis toujours "
  "entre eux, plut&ocirc;t que de na&icirc;tre seulement "
  "maintenant, forg&eacute;s par l'&eacute;preuve commune qu'ils "
  "traversent depuis des mois.")

p("Franck, avant que Darius ne reparte chez sa "
  "m&egrave;re en fin de week-end, lui remet une petite "
  "cl&eacute; USB suppl&eacute;mentaire, achet&eacute;e sp&eacute;cialement "
  "pour l'occasion, l'encourageant &agrave; garder toujours "
  "une copie de secours sur lui, dans son sac de "
  "cours, au cas o&ugrave; les autres supports "
  "viendraient &agrave; d&eacute;faillir simultan&eacute;ment, une "
  "pr&eacute;caution suppl&eacute;mentaire qui touche "
  "profond&eacute;ment Darius par son caract&egrave;re "
  "presque excessivement protecteur.")

name("FRANCK")
p("&laquo;&nbsp;On sait jamais, fiston. Mieux vaut trois "
  "sauvegardes que pas assez. Ton travail m&eacute;rite "
  "d'&ecirc;tre prot&eacute;g&eacute; correctement.&nbsp;&raquo;")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 5 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 6 -- LA LIGN&Eacute;E DE DARIUS
# ======================================================================
chap(6, "LA LIGN&Eacute;E DE DARIUS")

p("L'automne avance, et avec lui une routine presque "
  "rassurante s'installe entre les trois amis &mdash; les cours, le "
  "foot d'Alex, le carnet de Clara qu'elle consulte d&eacute;sormais "
  "chaque matin par r&eacute;flexe plut&ocirc;t que par peur, et le jeu de "
  "Darius qui grandit, soir apr&egrave;s soir, d'un couloir suppl&eacute;mentaire, "
  "d'une lumi&egrave;re bleue qu'il ne retire jamais.")

p("C'est Clara, un apr&egrave;s-midi de biblioth&egrave;que, qui relance "
  "le fil qu'ils avaient laiss&eacute; en suspens depuis la d&eacute;couverte "
  "du manuscrit de 1962 &mdash; ce texte &eacute;voquant &laquo;&nbsp;le jeune "
  "Darius&nbsp;&raquo; comme porteur d'une l&eacute;gende bien ant&eacute;rieure au "
  "programme du docteur Vasseur, et dont ils n'avaient, "
  "faute de temps, jamais explor&eacute; toutes les pistes.")

name("CLARA")
p("&laquo;&nbsp;Si le nom revient &agrave; chaque fois, sans lien de sang, &ccedil;a "
  "veut dire qu'il y a forc&eacute;ment eu d'autres 'Darius' entre "
  "1962 et toi. Quelqu'un a bien d&ucirc; porter &ccedil;a dans les "
  "ann&eacute;es soixante-dix, quatre-vingt. On n'a jamais cherch&eacute; "
  "de ce c&ocirc;t&eacute;-l&agrave;.&nbsp;&raquo;")

p("Ils retournent ensemble &agrave; l'ancien presbyt&egrave;re devenu "
  "biblioth&egrave;que municipale, cette fois arm&eacute;s d'une m&eacute;thode "
  "plus s&eacute;rieuse qu'auparavant, &eacute;pluchant syst&eacute;matiquement "
  "les registres paroissiaux, les almanachs locaux, les vieux "
  "num&eacute;ros jaunis du journal de Luynes conserv&eacute;s dans des "
  "bo&icirc;tes d'archives que personne ne semble avoir rouvertes "
  "depuis des lustres.")

p("La biblioth&eacute;caire, une femme d'&acirc;ge m&ucirc;r nomm&eacute;e "
  "Mme Ferrand qu'ils ont fini par bien conna&icirc;tre depuis le "
  "grimoire de 1962, les regarde s'installer avec un m&eacute;lange "
  "d'amusement et de curiosit&eacute;, habitu&eacute;e d&eacute;sormais &agrave; leurs "
  "recherches un peu &eacute;tranges sans jamais vraiment demander "
  "pourquoi trois adolescents s'int&eacute;ressent autant &agrave; des "
  "archives centenaires.")

name("MME FERRAND")
p("&laquo;&nbsp;Vous cherchez encore votre l&eacute;gende du meunier ? "
  "J'ai retrouv&eacute; une bo&icirc;te suppl&eacute;mentaire &agrave; la cave la "
  "semaine derni&egrave;re, des papiers de famille donn&eacute;s dans les "
  "ann&eacute;es soixante-dix. Je vous la sors si &ccedil;a vous "
  "int&eacute;resse.&nbsp;&raquo;")

p("La bo&icirc;te contient des lettres priv&eacute;es, des faire-part, des "
  "photographies de mariages et d'enterrements dont "
  "personne, aujourd'hui, ne saurait sans doute nommer les "
  "visages &mdash; et tout au fond, sous une pile de vieux journaux, "
  "une coupure de presse d&eacute;chir&eacute;e datant de 1978, portant en "
  "titre : &laquo;&nbsp;LE JEUNE DARIUS SAUVE UN ENFANT DE LA "
  "CRUE &mdash; LUYNES SE SOUVIENT.&nbsp;&raquo;")

p("Darius sent son propre nom, imprim&eacute; l&agrave; en toutes lettres "
  "quarante ans avant sa naissance, produire sur lui un effet "
  "presque vertigineux, comme si le simple fait de le voir "
  "coucou sur du papier jauni suffisait &agrave; confirmer, mieux "
  "que n'importe quel discours, qu'il n'&eacute;tait pas seulement "
  "hant&eacute; par un r&ocirc;le, mais bel et bien inscrit dans une "
  "lign&eacute;e.")

name("ALEX")
p("&laquo;&nbsp;1978, &ccedil;a fait quoi, presque cinquante ans. Si ce "
  "Darius-l&agrave; existe encore, il doit avoir dans les soixante "
  "ans maintenant. &Ccedil;a serait dingue de pouvoir lui parler, "
  "non ? Genre, direct, lui demander ce que &ccedil;a lui a fait &agrave; "
  "lui.&nbsp;&raquo;")

p("L'article ne donne pas de nom de famille, se contentant "
  "d'un pr&eacute;nom et d'un &acirc;ge &mdash; &laquo;&nbsp;Darius, 15 ans&nbsp;&raquo; &mdash; "
  "exactement comme les mentions ant&eacute;rieures trouv&eacute;es dans "
  "le grimoire, comme si la l&eacute;gende elle-m&ecirc;me refusait de "
  "livrer davantage d'identit&eacute; que le strict minimum n&eacute;cessaire "
  "&agrave; assurer sa propre continuit&eacute;.")

p("Mme Ferrand, consult&eacute;e sur la question, se souvient "
  "vaguement d'une famille du nom de Templier ayant v&eacute;cu "
  "&agrave; Luynes dans les ann&eacute;es soixante-dix, avant de "
  "d&eacute;m&eacute;nager, sans pouvoir confirmer avec certitude s'il "
  "s'agit bien de la m&ecirc;me personne, ni si elle vit encore "
  "aujourd'hui.")

name("MME FERRAND")
p("&laquo;&nbsp;Templier, oui, &ccedil;a me dit quelque chose. Je crois qu'il "
  "y a un vieux monsieur qui porte encore ce nom-l&agrave; du c&ocirc;t&eacute; "
  "des grottes, sur le coteau. Un ancien vigneron, je crois. "
  "Mais je vous garantis rien, &ccedil;a fait des ann&eacute;es que je l'ai "
  "pas crois&eacute; en ville.&nbsp;&raquo;")

p("Les trois amis se regardent, sachant d&eacute;j&agrave;, sans avoir "
  "besoin de se le dire, qu'ils passeront le week-end suivant "
  "&agrave; arpenter le coteau des grottes troglodytiques &agrave; la "
  "recherche d'un vieil homme qui pourrait bien &ecirc;tre, "
  "quarante-huit ans plus t&ocirc;t, le gar&ccedil;on de quinze ans "
  "dont l'article jauni raconte l'histoire.")

p("Avant de partir &agrave; l'assaut du coteau, Clara insiste pour "
  "passer par la mairie, arguant qu'un registre officiel "
  "vaudra toujours mieux qu'une coupure de journal pour "
  "confirmer une adresse, et c'est ainsi qu'ils se retrouvent "
  "tous les trois, un mercredi apr&egrave;s-midi sans cours, devant "
  "le guichet d'&eacute;tat civil &agrave; expliquer, tant bien que mal, "
  "qu'ils font un expos&eacute; d'histoire locale sur les vieilles "
  "familles de Luynes.")

p("L'employ&eacute;e municipale, peu convaincue mais peu "
  "regardante, finit par les laisser consulter les annuaires "
  "d'un demi-si&egrave;cle, class&eacute;s par ann&eacute;e dans des reliures de "
  "carton us&eacute;es, et c'est Alex, en feuilletant machinalement "
  "l'&eacute;dition de 1978, qui tombe le premier sur le nom qu'ils "
  "cherchent.")

name("ALEX")
p("&laquo;&nbsp;L&agrave;. 'Templier, Darius, n&eacute; en 1963, chemin des "
  "Grottes.' C'est lui, forc&eacute;ment, &ccedil;a colle parfaitement avec "
  "l'&acirc;ge de l'article. Quinze ans en 78, &ccedil;a nous fait un "
  "monsieur de soixante-trois ans aujourd'hui.&nbsp;&raquo;")

p("Darius passe un long moment &agrave; fixer ce nom imprim&eacute; en "
  "petits caract&egrave;res, ressentant une &eacute;trange forme de "
  "vertige familier &mdash; celui de voir son propre pr&eacute;nom "
  "port&eacute; par un &eacute;tranger, comme un h&eacute;ritage qu'on lui "
  "aurait transmis sans jamais lui demander son avis, et sans "
  "qu'aucun lien de sang ne vienne l&eacute;gitimer la chose.")

p("Ils consultent, dans la foul&eacute;e, les annuaires suivants, "
  "cherchant &agrave; retracer combien de temps ce Darius "
  "Templier &eacute;tait rest&eacute; enregistr&eacute; &agrave; cette adresse, et "
  "d&eacute;couvrent qu'il dispara&icirc;t des listings apr&egrave;s 1994, ann&eacute;e "
  "qui r&eacute;sonne d&eacute;j&agrave; douloureusement pour eux trois comme "
  "celle de la fermeture officielle du programme Vasseur.")

name("CLARA")
p("&laquo;&nbsp;1994. Encore cette ann&eacute;e-l&agrave;. C'est peut-&ecirc;tre lui qui a "
  "&eacute;t&eacute; m&ecirc;l&eacute; &agrave; tout &ccedil;a, d'une mani&egrave;re ou d'une autre, "
  "sans qu'on sache encore comment. &Ccedil;a peut pas &ecirc;tre un "
  "hasard, non ?&nbsp;&raquo;")

p("L'employ&eacute;e, curieuse malgr&eacute; elle de les voir s'attarder "
  "aussi longuement sur un simple exercice scolaire, finit par "
  "leur confier, presque en aparte, qu'un homme correspondant "
  "&agrave; cette description vit toujours dans le coin, du moins "
  "d'apr&egrave;s la taxe fonci&egrave;re qu'elle a d&ucirc; traiter r&eacute;cemment "
  "pour une petite propri&eacute;t&eacute; sur le coteau.")

name("EMPLOY&Eacute;E MAIRIE")
p("&laquo;&nbsp;Il vient jamais ici en personne, remarquez, il fait "
  "tout par courrier. Un vieux monsieur assez discret, "
  "d'apr&egrave;s ce qu'on m'a dit. Si vous allez le voir, soyez "
  "gentils, on raconte qu'il n'aime pas trop la visite.&nbsp;&raquo;")

p("En sortant de la mairie, Darius sent le poids de cette "
  "d&eacute;couverte se m&ecirc;ler &agrave; celui, d&eacute;j&agrave; lourd, de tout ce "
  "qu'il porte depuis des mois &mdash; l'id&eacute;e qu'un homme, "
  "quelque part sur ce m&ecirc;me coteau qu'il a arpent&eacute; enfant "
  "sans jamais le savoir, a peut-&ecirc;tre v&eacute;cu, cinquante ans "
  "plus t&ocirc;t, une version diff&eacute;rente de ce que lui-m&ecirc;me "
  "vient de traverser.")

p("Ils d&eacute;cident, d'un commun accord, de ne pas d&eacute;barquer "
  "sans pr&eacute;venir &mdash; par respect autant que par prudence "
  "&mdash; et Clara r&eacute;dige, ce soir-l&agrave;, une courte lettre "
  "manuscrite qu'ils gliss&eacute;ront eux-m&ecirc;mes dans sa bo&icirc;te aux "
  "lettres, expliquant, avec le plus de tact possible, pourquoi "
  "trois adolescents de Luynes aimeraient tant le rencontrer.")

name("CLARA")
p("&laquo;&nbsp;J'ai &eacute;crit qu'on s'int&eacute;resse &agrave; une vieille l&eacute;gende "
  "locale et &agrave; un &eacute;v&eacute;nement de 1978. J'ai pas os&eacute; mettre le "
  "mot 'programme', ni 'm&eacute;moire', ni rien de tout &ccedil;a. Je "
  "voulais pas qu'il referme sa porte avant m&ecirc;me de nous "
  "avoir laiss&eacute; entrer.&nbsp;&raquo;")

p("Ils glissent la lettre dans la bo&icirc;te aux lettres rouill&eacute;e du "
  "chemin des Grottes le lendemain matin, avant les cours, "
  "sans sonner, sans frapper, laissant &agrave; cet homme "
  "qu'ils n'ont jamais vu le temps et le choix de d&eacute;cider "
  "lui-m&ecirc;me s'il souhaite, ou non, r&eacute;pondre &agrave; l'appel de "
  "trois inconnus port&eacute;s par une histoire qui, visiblement, "
  "n'a jamais totalement cess&eacute; de le concerner lui aussi.")

p("La r&eacute;ponse arrive plus vite qu'ils ne l'auraient esp&eacute;r&eacute; "
  "&mdash; un simple mot, plac&eacute; dans la bo&icirc;te aux lettres de "
  "Clara trois jours plus tard, d'une &eacute;criture appliqu&eacute;e "
  "d'homme d'un autre temps : &laquo;&nbsp;samedi, quatorze heures. "
  "Ne venez pas plus t&ocirc;t, je n'aime pas &ecirc;tre surpris.&nbsp;&raquo;")

p("La maison de Darius Templier se trouve effectivement "
  "creus&eacute;e &agrave; m&ecirc;me la roche du coteau, une habitation "
  "troglodytique am&eacute;nag&eacute;e avec un soin discret, entour&eacute;e "
  "d'un petit jardin de vigne qui semble bien plus vivant que "
  "le reste de la propri&eacute;t&eacute;, comme si cet homme avait choisi "
  "d'investir toute son &eacute;nergie dans les choses qui poussent "
  "plut&ocirc;t que dans celles qui se souviennent.")

p("Il les accueille sur le pas de sa porte, un homme maigre "
  "aux cheveux blancs, le regard vif malgr&eacute; l'&acirc;ge, portant "
  "sur son propre avant-bras, visible sous une manche "
  "retrouss&eacute;e, une cicatrice ancienne dont la forme, Darius "
  "le remarque imm&eacute;diatement avec un frisson, ressemble "
  "&eacute;trangement &agrave; celle d'Alex.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;Vous devez &ecirc;tre le petit Darius de la lettre. J'ai "
  "h&eacute;sit&eacute; longtemps avant de vous r&eacute;pondre. &Ccedil;a fait des "
  "d&eacute;cennies que personne ne vient plus me parler de tout "
  "&ccedil;a. J'avais fini par croire que j'&eacute;tais le dernier.&nbsp;&raquo;")

p("Il les fait entrer dans une pi&egrave;ce fra&icirc;che, taill&eacute;e dans la "
  "roche, tapiss&eacute;e de coupures de presse jaunies et de photos "
  "en noir et blanc, et Darius reconna&icirc;t, sur l'une d'elles, un "
  "adolescent qui pourrait &ecirc;tre son propre reflet cinquante "
  "ans plus t&ocirc;t, m&ecirc;me visage, m&ecirc;me posture, m&ecirc;me fa&ccedil;on "
  "d'incliner l&eacute;g&egrave;rement la t&ecirc;te vers la gauche.")

name("CLARA")
p("&laquo;&nbsp;Monsieur Templier, on a lu l'article de 1978, sur "
  "l'enfant que vous avez sauv&eacute; de la crue. Est-ce que &ccedil;a "
  "avait un rapport avec... enfin, avec la m&ecirc;me chose que "
  "nous ? Une machine, un Non-lieu, quelque chose comme "
  "&ccedil;a ?&nbsp;&raquo;")

p("Le vieil homme sourit tristement, comme si cette question, "
  "il l'avait attendue toute sa vie sans jamais oser esp&eacute;rer "
  "qu'on la lui poserait un jour, et se lance dans un r&eacute;cit "
  "qu'il n'a visiblement racont&eacute; &agrave; personne depuis "
  "plusieurs g&eacute;n&eacute;rations.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;&Agrave; l'&eacute;poque &ccedil;a s'appelait pas 'distributeur', ni "
  "'Non-lieu'. On disait 'le puits', et 'la marge'. Mais c'&eacute;tait "
  "d&eacute;j&agrave; exactement la m&ecirc;me chose &mdash; un objet contre une "
  "ann&eacute;e, une page qu'on efface pour en r&eacute;&eacute;crire une autre. "
  "J'ai perdu ma petite s&oelig;ur dans cette histoire, en 1979. "
  "Personne d'autre que moi ne se souvient qu'elle a "
  "exist&eacute;.&nbsp;&raquo;")

p("Darius sent quelque chose se serrer dans sa poitrine en "
  "entendant &ccedil;a, comprenant, pour la premi&egrave;re fois avec une "
  "telle clart&eacute;, que le r&ocirc;le qu'il porte n'a jamais &eacute;t&eacute; une "
  "victoire d&eacute;finitive pour personne avant lui &mdash; seulement "
  "une s&eacute;rie de batailles gagn&eacute;es &agrave; un prix que chaque "
  "porteur, chacun &agrave; son tour, finit par payer seul.")

p("Darius Templier leur sert un th&eacute; qu'aucun des trois ne "
  "boit vraiment, trop occup&eacute;s &agrave; absorber ce r&eacute;cit qui "
  "&eacute;claire, par touches successives, tout ce qu'ils avaient "
  "pris jusque-l&agrave; pour une histoire propre &agrave; leur seule "
  "g&eacute;n&eacute;ration &mdash; et le vieil homme, une fois lanc&eacute;, semble "
  "presque soulag&eacute; de pouvoir enfin d&eacute;verser cinquante ans "
  "de silence sur des oreilles capables de le comprendre "
  "vraiment.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;&Ccedil;a ne se transmet pas dans le sang, vous l'avez "
  "d&eacute;j&agrave; compris, sinon on serait de la m&ecirc;me famille, toi et "
  "moi, et &ccedil;a n'est pas le cas. &Ccedil;a se transmet &agrave; travers un "
  "lieu, je crois. Luynes, Fondettes, le coteau, la Loire. "
  "Comme si la terre elle-m&ecirc;me choisissait, &agrave; chaque "
  "g&eacute;n&eacute;ration, un enfant du coin pour porter &ccedil;a &agrave; sa "
  "place.&nbsp;&raquo;")

p("Il explique que la l&eacute;gende, telle qu'on la lui avait "
  "racont&eacute;e enfant, parlait d'une &laquo;&nbsp;dette&nbsp;&raquo; contract&eacute;e il y a "
  "tr&egrave;s longtemps entre les habitants de la r&eacute;gion et une "
  "force qu'on ne nommait jamais directement, une force qui "
  "acceptait d'&eacute;changer des ann&eacute;es de vie contre des "
  "souvenirs, &agrave; condition qu'un &ecirc;tre humain accepte, chaque "
  "fois qu'elle red&eacute;bordait, de venir n&eacute;gocier en son nom.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;Le docteur Vasseur, dans les ann&eacute;es quatre-vingt, a "
  "cru pouvoir mettre &ccedil;a en &eacute;quations, en dossiers, en "
  "protocoles. Il pensait dominer une chose qui existait bien "
  "avant lui et qui existera bien apr&egrave;s nous tous. C'est &agrave; "
  "&ccedil;a que je pense chaque fois que j'entends parler de "
  "'programme'. Comme si on pouvait mettre un uniforme &agrave; "
  "une rivi&egrave;re.&nbsp;&raquo;")

p("Clara note fr&eacute;n&eacute;tiquement dans son carnet, consciente que "
  "chaque phrase de cet homme vaut plus que des semaines "
  "de recherches en biblioth&egrave;que, tandis qu'Alex, silencieux "
  "pour une fois, fixe sa propre cicatrice comme s'il "
  "cherchait &agrave; y lire une explication suppl&eacute;mentaire.")

name("ALEX")
p("&laquo;&nbsp;Et &ccedil;a s'arr&ecirc;te jamais, alors ? Y'aura toujours "
  "quelqu'un pour porter &ccedil;a, g&eacute;n&eacute;ration apr&egrave;s g&eacute;n&eacute;ration, "
  "sans que personne d&eacute;cide vraiment de rien ?&nbsp;&raquo;")

p("Le vieil homme h&eacute;site longuement avant de r&eacute;pondre, ses "
  "yeux se posant sur Darius avec une gravit&eacute; particuli&egrave;re, "
  "comme s'il p&eacute;sait le poids exact de ce qu'il s'appr&ecirc;te &agrave; "
  "confier &agrave; un gar&ccedil;on de quatorze ans.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;J'ai cru, longtemps, que non, que &ccedil;a durerait "
  "toujours. Mais j'ai remarqu&eacute; un truc, ces derni&egrave;res "
  "ann&eacute;es. Depuis que le programme officiel a ferm&eacute; en "
  "94, la chose elle-m&ecirc;me semble... affam&eacute;e, disons. Plus "
  "impatiente qu'avant. Comme si elle sentait qu'elle "
  "approchait d'un moment o&ugrave; elle pourrait enfin r&eacute;cup&eacute;rer "
  "tout d'un coup ce qu'on lui a fait rendre au compte-gouttes "
  "pendant des si&egrave;cles.&nbsp;&raquo;")

p("Darius sent un froid remonter le long de son &eacute;chine en "
  "entendant ces mots, pensant imm&eacute;diatement au Non-lieu "
  "en flammes, &agrave; la dissolution incompl&egrave;te de Kayden, aux "
  "signaux &eacute;trange re&ccedil;us dans le carnet de Clara, et &agrave; cette "
  "phrase inqui&eacute;tante &mdash; &laquo;&nbsp;encore l&agrave;&nbsp;&raquo; &mdash; apparue sur "
  "l'&eacute;cran du coll&egrave;ge.")

name("DARIUS")
p("&laquo;&nbsp;Vous savez ce qui pourrait se passer, si elle "
  "r&eacute;cup&eacute;rait tout d'un coup ? Concr&egrave;tement, je veux "
  "dire ?&nbsp;&raquo;")

p("Le vieil homme secoue lentement la t&ecirc;te, et pour la "
  "premi&egrave;re fois depuis leur arriv&eacute;e, une v&eacute;ritable peur "
  "traverse son regard, celle d'un homme qui a pass&eacute; sa vie "
  "&agrave; contenir quelque chose sans jamais vraiment en "
  "conna&icirc;tre l'&eacute;tendue r&eacute;elle.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;Non. Et j'esp&egrave;re sinc&egrave;rement, petit, que tu n'auras "
  "jamais &agrave; le d&eacute;couvrir.&nbsp;&raquo;")

p("Un silence pesant s'installe dans la petite pi&egrave;ce "
  "creus&eacute;e &agrave; m&ecirc;me la roche, seulement troubl&eacute; par le "
  "tic-tac r&eacute;gulier d'une horloge murale d&eacute;modée, et "
  "Clara, incapable de contenir plus longtemps sa "
  "curiosit&eacute;, se penche vers l'avant, le carnet d&eacute;j&agrave; "
  "ouvert sur ses genoux.")

name("CLARA")
p("&laquo;&nbsp;Monsieur Templier, cette lign&eacute;e, elle remonte "
  "jusqu'o&ugrave; exactement ? Vous avez dit le laboureur du "
  "dix-huiti&egrave;me si&egrave;cle, le meunier de 1871. Mais avant "
  "&ccedil;a, y'a forc&eacute;ment eu quelqu'un aussi, non ? &Ccedil;a "
  "s'arr&ecirc;te pas comme &ccedil;a, une histoire pareille.&nbsp;&raquo;")

p("Le vieil homme sourit, un sourire fatigu&eacute; mais "
  "sinc&egrave;re, visiblement heureux de transmettre enfin, "
  "&agrave; quelqu'un qui &eacute;coute vraiment, le fruit de d&eacute;cennies "
  "de recherches personnelles men&eacute;es dans la plus "
  "totale solitude.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;J'ai retrouv&eacute; une mention, une seule, dans un "
  "registre paroissial du seizi&egrave;me si&egrave;cle, conserv&eacute; "
  "&agrave; l'&eacute;v&ecirc;ch&eacute; de Tours. Un cur&eacute; y racontait, avec "
  "une prudence &eacute;vidente, l'histoire d'un &laquo;&nbsp;jeune homme "
  "du village, appel&eacute; par certains le porte-dette&nbsp;&raquo;, "
  "sans jamais oser &eacute;crire son pr&eacute;nom en toutes lettres, "
  "comme si le nommer risquait d'attirer une attention "
  "ind&eacute;sirable.&nbsp;&raquo;")

p("Il se l&egrave;ve avec difficult&eacute; et fouille dans un tiroir "
  "voisin, en sortant une photocopie jaunie d'un vieux "
  "document manuscrit, l'&eacute;criture ronde et appliqu&eacute;e "
  "d'un pr&ecirc;tre depuis longtemps disparu racontant, en "
  "latin d'&eacute;glise m&ecirc;l&eacute; de fran&ccedil;ais ancien, une histoire "
  "de dette et de sacrifice qui ressemble, trait pour "
  "trait, &agrave; tout ce que Darius a lui-m&ecirc;me v&eacute;cu quelques "
  "semaines plus t&ocirc;t dans le Non-lieu.")

name("ALEX")
p("&laquo;&nbsp;Le seizi&egrave;me si&egrave;cle. &Ccedil;a fait genre cinq cents ans "
  "que &ccedil;a dure, ce truc. Cinq cents ans de gamins comme "
  "Darius qui h&eacute;ritent d'un probl&egrave;me qu'ils ont jamais "
  "demand&eacute;. &Ccedil;a me file le vertige, dit comme &ccedil;a.&nbsp;&raquo;")

p("Templier hoche la t&ecirc;te gravement, expliquant qu'il "
  "soup&ccedil;onne, sans jamais avoir pu le prouver "
  "formellement, que la l&eacute;gende remonte plus loin "
  "encore, peut-&ecirc;tre jusqu'&agrave; l'&eacute;poque gauloise de la "
  "vall&eacute;e, quand les peuples locaux racontaient d&eacute;j&agrave; "
  "des histoires de rivi&egrave;res qui exigeaient des offrandes "
  "en &eacute;change de leur cl&eacute;mence, des r&eacute;cits que "
  "l'Histoire officielle a toujours class&eacute;s comme simple "
  "folklore agraire sans jamais soup&ccedil;onner la r&eacute;alit&eacute; "
  "sous-jacente.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;Je crois que la Marge, ou la dette, ou comme "
  "vous voulez l'appeler, existe depuis que des humains "
  "vivent le long de cette Loire. Chaque civilisation lui "
  "a donn&eacute; un nom diff&eacute;rent, une histoire diff&eacute;rente "
  "pour l'expliquer, mais c'est toujours, au fond, la "
  "m&ecirc;me chose &mdash; une force patiente qui accepte "
  "d'&eacute;changer des ann&eacute;es contre des souvenirs, &agrave; "
  "condition qu'un humain accepte de porter la "
  "n&eacute;gociation en son nom.&nbsp;&raquo;")

p("Darius range pr&eacute;cieusement, dans son sac, la "
  "photocopie du document du seizi&egrave;me si&egrave;cle que "
  "Templier insiste pour lui confier, sentant, en la "
  "touchant, le poids concret d'une histoire familiale "
  "&mdash; car c'est bien ainsi qu'il commence, d&eacute;sormais, &agrave; "
  "penser cette lign&eacute;e de porteurs anonymes &mdash; "
  "s'&eacute;tendant sur bien plus de si&egrave;cles qu'il n'aurait "
  "jamais os&eacute; l'imaginer avant cette visite.")

p("Avant de les laisser repartir, Darius Templier se l&egrave;ve avec "
  "difficult&eacute; et disparaeacute;t dans une pi&egrave;ce voisine, revenant "
  "quelques minutes plus tard avec un petit objet enveloppé "
  "dans un tissu us&eacute; qu'il d&eacute;pose, avec un soin presque "
  "religieux, sur la table entre eux &mdash; un second pon&ccedil;on, "
  "presque identique &agrave; celui de Darius, mais grav&eacute; d'une "
  "autre lettre : un &laquo;&nbsp;T.&nbsp;&raquo;")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;&Ccedil;a m'a servi, en 79, contre ce qui avait pris ma "
  "petite s&oelig;ur. On l'appelait pas Kayden, &agrave; l'&eacute;poque. On "
  "l'appelait juste 'la Marge' &mdash; ce qui reste quand on efface "
  "une page sans effacer compl&egrave;tement celui qui l'a v&eacute;cue. "
  "Je crois que c'est toujours la m&ecirc;me chose, sous des noms "
  "diff&eacute;rents, depuis toujours.&nbsp;&raquo;")

p("Il explique que chaque porteur, &agrave; travers les g&eacute;n&eacute;rations, "
  "semble affronter une version diff&eacute;rente de cette m&ecirc;me "
  "pr&eacute;sence r&eacute;siduelle &mdash; parfois une simple ombre, parfois "
  "une voix, parfois, comme dans le cas de Darius, une "
  "presque-personne enti&egrave;re capable de parler, de "
  "raisonner, presque de regretter.")

name("CLARA")
p("&laquo;&nbsp;Vous pensez que Kayden pourrait redevenir dangereux ? "
  "Ou vous pensez plut&ocirc;t qu'il faudrait, genre, l'aider &agrave; se "
  "poser quelque part, d&eacute;finitivement ?&nbsp;&raquo;")

p("Le vieil homme hausse les &eacute;paules, avouant qu'apr&egrave;s "
  "toutes ces ann&eacute;es il n'a toujours pas de r&eacute;ponse d&eacute;finitive "
  "&agrave; cette question, seulement une intuition qu'il partage "
  "volontiers, m&ecirc;me si elle ne suffit &agrave; rassurer personne "
  "compl&egrave;tement.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;Ma s&oelig;ur, je l'ai jamais retrouv&eacute;e enti&egrave;re. Juste des "
  "&eacute;clats, de temps en temps, dans des endroits inattendus &mdash; "
  "une chanson qu'elle aimait qui passait &agrave; la radio pile au "
  "bon moment, une odeur dans une pi&egrave;ce vide. J'ai fini par "
  "croire que c'&eacute;tait sa mani&egrave;re &agrave; elle de continuer &agrave; "
  "exister, un peu, sans avoir besoin de revenir tout &agrave; "
  "fait.&nbsp;&raquo;")

p("Il insiste pour que Darius garde le second pon&ccedil;on, "
  "assurant qu'il n'en aura plus l'usage &agrave; son &acirc;ge, et que "
  "deux objets valent toujours mieux qu'un seul quand vient "
  "le moment de n&eacute;gocier avec une force qui ne conna&icirc;t ni "
  "piti&eacute; ni patience.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;Une derni&egrave;re chose. Si un jour &ccedil;a te r&eacute;clame "
  "quelque chose de trop gros, plus gros qu'un souvenir ou "
  "qu'une ann&eacute;e &mdash; refuse. Toujours. Peu importe ce qu'elle "
  "te promet en &eacute;change. J'ai vu des gens dire oui, autrefois, "
  "et j'ai vu ce que &ccedil;a leur a co&ucirc;t&eacute;.&nbsp;&raquo;")

p("Ils repartent &agrave; v&eacute;lo en silence, le second pon&ccedil;on au "
  "fond du sac de Darius, chacun digérant &agrave; sa mani&egrave;re "
  "l'ampleur nouvelle de ce qu'ils viennent d'apprendre &mdash; "
  "que leur histoire n'&eacute;tait qu'un chapitre parmi d'autres "
  "d'un livre bien plus ancien, dont personne, m&ecirc;me pas le "
  "vieux Templier, ne conna&icirc;t la premi&egrave;re page.")

p("Les semaines qui suivent la visite chez Templier voient "
  "Darius changer, sans que ni Clara ni Alex ne parviennent "
  "&agrave; nommer pr&eacute;cis&eacute;ment ce qui a chang&eacute; &mdash; une gravit&eacute; "
  "nouvelle dans son regard, une mani&egrave;re de prendre des "
  "notes, comme le vieil homme, sur des carnets diff&eacute;rents "
  "selon les sujets, comme s'il avait d&eacute;cid&eacute; d'endosser plus "
  "s&eacute;rieusement encore le r&ocirc;le qu'on venait de lui confirmer.")

p("Il passe des heures, le soir, &agrave; recopier dans un cahier "
  "neuf tout ce que Templier leur a racont&eacute;, ajoutant ses "
  "propres observations, cherchant &agrave; b&acirc;tir, m&eacute;thodiquement, "
  "une sorte de manuel de survie &agrave; l'usage de celui qui, un "
  "jour, lui succ&eacute;dera peut-&ecirc;tre &mdash; sans savoir s'il aura "
  "seulement le temps ni la sagesse de le transmettre "
  "correctement.")

name("CLARA")
p("&laquo;&nbsp;Tu penses &agrave; qui, exactement, quand tu &eacute;cris tout &ccedil;a ? "
  "Y'a pas de raison qu'on sache d&eacute;j&agrave; qui sera le prochain. "
  "&Ccedil;a pourrait &ecirc;tre dans cinquante ans, comme &ccedil;a pourrait "
  "&ecirc;tre jamais, si toi tu t'en sors vivant assez longtemps pour "
  "que &ccedil;a devienne inutile.&nbsp;&raquo;")

p("Darius n'a pas de r&eacute;ponse claire &agrave; lui offrir, seulement "
  "cette sensation diffuse qu'&eacute;crire ces choses le rassure "
  "davantage qu'il ne saurait l'expliquer, comme si le simple "
  "fait de pr&eacute;parer un h&eacute;ritage all&eacute;geait un peu le poids "
  "d'avoir &agrave; tout porter seul, m&ecirc;me sans destinataire "
  "identifi&eacute;.")

p("Il continue, en parall&egrave;le, &agrave; travailler sur son jeu, "
  "ajoutant d&eacute;sormais, sans se l'avouer enti&egrave;rement, des "
  "&eacute;l&eacute;ments directement inspir&eacute;s de ce que Templier leur a "
  "confi&eacute; &mdash; un second personnage jouable, plus &acirc;g&eacute;, qui "
  "guide le premier &agrave; travers les couloirs, portant sur son "
  "avant-bras une cicatrice identique &agrave; celle d'Alex.")

p("Un soir, casque viss&eacute; sur les yeux, il fait dialoguer ce "
  "personnage a&icirc;n&eacute; avec le sien pour la premi&egrave;re fois, "
  "&eacute;crivant des lignes de texte qu'il sait puis&eacute;es presque "
  "mot pour mot dans la bouche du vieil homme du coteau, "
  "et ressent, en les tapant, une &eacute;motion inattendue, comme "
  "s'il venait de donner &agrave; cette rencontre une seconde vie, "
  "plus durable que le simple souvenir.")

name("ALEX")
p("&laquo;&nbsp;T'y passes vraiment beaucoup de temps, &agrave; ce jeu, "
  "ces derniers temps. C'est pas un reproche, hein, juste... "
  "je sais pas, &ccedil;a m'inqui&egrave;te un peu, des fois, de voir &agrave; "
  "quel point &ccedil;a a l'air de compter plus que tout le reste "
  "pour toi.&nbsp;&raquo;")

p("Darius balaie la remarque d'un geste, expliquant que c'est "
  "sa mani&egrave;re &agrave; lui de digerer tout ce qu'ils traversent, "
  "exactement comme Clara a son carnet et Alex son ballon "
  "de foot, sans se rendre compte tout &agrave; fait &agrave; quel point "
  "cette explication, r&eacute;p&eacute;t&eacute;e trop souvent, commence &agrave; "
  "sonner davantage comme une justification que comme une "
  "simple description.")

p("Il continue malgr&eacute; tout, soir apr&egrave;s soir, &agrave; peaufiner son "
  "monde, cette porte close toujours &eacute;clair&eacute;e d'une lumi&egrave;re "
  "bleue, ce personnage a&icirc;n&eacute; qui distille sagesse et "
  "avertissements, sans imaginer un seul instant &agrave; quel "
  "point ce petit royaume num&eacute;rique construit dans sa "
  "chambre deviendra, bien plus t&ocirc;t qu'il ne le pense, "
  "l'endroit m&ecirc;me o&ugrave; se refermera toute cette histoire.")

p("L'hiver arrive sur Luynes avec sa lenteur habituelle, les "
  "matins de plus en plus sombres, la Loire prenant cette "
  "teinte gris&acirc;tre particuli&egrave;re qu'elle garde jusqu'au printemps, "
  "et Darius, sans vraiment s'en rendre compte, laisse "
  "progressivement son quotidien se resserrer autour de "
  "trois p&ocirc;les : le coll&egrave;ge, sa chambre, et le casque pos&eacute; sur "
  "son bureau.")

p("Il continue de voir Clara et Alex, bien s&ucirc;r, mais leurs "
  "rendez-vous s'espacent l&eacute;g&egrave;rement, remplac&eacute;s de plus en "
  "plus souvent par de longues soir&eacute;es en solitaire pass&eacute;es "
  "&agrave; ajuster une texture, &agrave; corriger un bug, &agrave; faire dialoguer "
  "ses deux personnages jusqu'&agrave; ce que leurs r&eacute;pliques "
  "sonnent enfin exactement comme il les entend dans sa "
  "t&ecirc;te.")

p("Sa m&egrave;re remarque, elle aussi, ce changement, sans "
  "parvenir &agrave; le nommer autrement que par une inqui&eacute;tude "
  "vague qu'elle formule maladroitement au d&icirc;ner, entre deux "
  "sujets plus l&eacute;gers, sans jamais vraiment insister au-del&agrave; "
  "d'une remarque ou deux.")

name("M&Egrave;RE DE DARIUS")
p("&laquo;&nbsp;Tu sors plus beaucoup, ces derniers temps. C'est "
  "l'&acirc;ge, je sais, on se referme un peu &agrave; quatorze ans, mais "
  "&ccedil;a me ferait plaisir de te voir plus souvent avec tes "
  "copains dehors, plut&ocirc;t que tout seul dans ta chambre avec "
  "ce casque.&nbsp;&raquo;")

p("Darius promet, chaque fois, de faire un effort, et chaque "
  "fois retourne, le soir m&ecirc;me, retrouver ce monde qu'il "
  "ma&icirc;trise enti&egrave;rement, o&ugrave; aucune r&eacute;v&eacute;lation impr&eacute;vue ne "
  "vient jamais bouleverser l'ordre des choses, o&ugrave; Kayden, "
  "Franck, Templier et la Marge deviennent des personnages "
  "qu'il peut faire parler exactement comme il le d&eacute;cide.")

p("Clara finit par lui en parler directement, un apr&egrave;s-midi "
  "sur le chemin du retour, avec cette franchise qui la "
  "caract&eacute;rise depuis toujours, refusant de laisser une "
  "inqui&eacute;tude s'installer sans jamais &ecirc;tre formul&eacute;e clairement "
  "entre eux.")

name("CLARA")
p("&laquo;&nbsp;J'ai l'impression que tu nous remplaces un peu par ce "
  "jeu, Darius. Pas m&eacute;chamment, je crois pas que tu le fasses "
  "expr&egrave;s, mais depuis Templier, t'es de plus en plus "
  "souvent ailleurs, m&ecirc;me quand t'es l&agrave;, physiquement, avec "
  "nous.&nbsp;&raquo;")

p("Il voudrait la contredire, mais quelque chose en lui sait "
  "d&eacute;j&agrave; qu'elle n'a pas tout &agrave; fait tort, sans pour autant "
  "parvenir &agrave; expliquer pourquoi ce petit monde qu'il "
  "construit lui offre une paix qu'il ne trouve nulle part "
  "ailleurs &mdash; ni chez son p&egrave;re, encore fragile dans sa "
  "nouvelle honn&ecirc;tet&eacute;, ni chez sa m&egrave;re, ni m&ecirc;me, "
  "compl&egrave;tement, aupr&egrave;s de ses deux meilleurs amis.")

name("DARIUS")
p("&laquo;&nbsp;J'sais pas comment t'expliquer &ccedil;a sans avoir l'air "
  "bizarre. L&agrave;-bas, j'ai l'impression de contr&ocirc;ler quelque "
  "chose, pour une fois. Tout le reste, la Marge, la lign&eacute;e, "
  "mon p&egrave;re, tout &ccedil;a m'&eacute;chappe compl&egrave;tement. Le jeu, "
  "non. Le jeu, c'est le seul endroit o&ugrave; c'est moi qui "
  "d&eacute;cide.&nbsp;&raquo;")

p("Clara n'insiste pas davantage ce jour-l&agrave;, mais Darius voit, "
  "dans son regard, une inqui&eacute;tude sinc&egrave;re qui ne dispara&icirc;t "
  "pas totalement, comme une petite graine plant&eacute;e qui "
  "mettra des mois &agrave; germer, sans qu'il en mesure encore "
  "vraiment l'importance.")

p("C'est en fouillant, un soir de d&eacute;cembre, dans les fichiers "
  "syst&egrave;me du vieil ordinateur retrouv&eacute; chez les Vasseur, "
  "photographi&eacute;s discr&egrave;tement avant de quitter la propri&eacute;t&eacute; "
  "de Fondettes, que Darius tombe sur une liste qu'il n'avait "
  "pas remarqu&eacute;e sur place &mdash; un fichier de configuration "
  "r&eacute;seau, dat&eacute; de 1993, listant sept adresses distinctes, "
  "chacune associ&eacute;e &agrave; un nom de ville.")

p("Tours, bien s&ucirc;r, et Luynes ; mais aussi Amboise, Chinon, "
  "Loches, et deux villes plus &eacute;loign&eacute;es, Blois et Orl&eacute;ans, "
  "chacune accompagn&eacute;e d'un code &agrave; trois chiffres qui "
  "ressemble &eacute;trangement &agrave; ceux utilis&eacute;s pour num&eacute;roter "
  "les dossiers patients dans l'enveloppe kraft de Franck.")

name("CLARA")
p("&laquo;&nbsp;Sept villes, sept sites. &Ccedil;a veut dire que le "
  "programme &eacute;tait pas juste un truc local, isol&eacute; entre "
  "Luynes et Fondettes. C'&eacute;tait tout un r&eacute;seau, &eacute;tal&eacute; sur "
  "toute la r&eacute;gion. &Ccedil;a change compl&egrave;tement l'&eacute;chelle de ce "
  "qu'on pensait affronter.&nbsp;&raquo;")

p("Ils passent plusieurs soir&eacute;es &agrave; recouper ces informations "
  "avec ce que Templier leur a racont&eacute;, avec les archives de "
  "la biblioth&egrave;que, avec tout ce qu'ils ont d&eacute;j&agrave; appris sur "
  "le docteur Vasseur, et arrivent &agrave; la conclusion, "
  "vertigineuse, que le programme officiel de 1991 &agrave; 1994 "
  "n'&eacute;tait probablement qu'une tentative r&eacute;cente et "
  "modeste de canaliser quelque chose de bien plus ancien "
  "et bien plus &eacute;tendu que ce que quiconque, m&ecirc;me "
  "Templier, ne semble en r&eacute;alit&eacute; savoir.")

name("ALEX")
p("&laquo;&nbsp;Si y'a six autres sites, &ccedil;a veut peut-&ecirc;tre dire qu'il "
  "y a six autres Darius, quelque part, en ce moment m&ecirc;me. "
  "Ou six autres Kayden. &Ccedil;a fait froid dans le dos de se dire "
  "qu'on n'est peut-&ecirc;tre m&ecirc;me pas les seuls &agrave; vivre exactement "
  "&ccedil;a, ailleurs.&nbsp;&raquo;")

p("Darius pense &agrave; Templier, seul depuis des d&eacute;cennies avec "
  "son fardeau, et &agrave; l'id&eacute;e que d'autres, peut-&ecirc;tre, portent "
  "en ce moment m&ecirc;me le m&ecirc;me genre de solitude, sans "
  "savoir que trois adolescents de Luynes viennent de "
  "d&eacute;couvrir l'existence d'un r&eacute;seau qui les relie tous, "
  "invisiblement, &agrave; travers des kilom&egrave;tres de vall&eacute;e "
  "ligerienne.")

p("Ils choisissent, apr&egrave;s discussion, de concentrer leurs "
  "recherches sur le site le plus proche apr&egrave;s Luynes &mdash; "
  "Amboise, &agrave; peine trente minutes en train &mdash; esp&eacute;rant y "
  "trouver, comme &agrave; Fondettes, des traces suppl&eacute;mentaires "
  "capables d'&eacute;clairer ce que la Marge attend r&eacute;ellement, et "
  "ce que signifie cette impatience nouvelle dont Templier "
  "leur a parl&eacute;.")

p("Ils passent un dimanche entier &agrave; pr&eacute;parer leur expedition "
  "&agrave; Amboise avec un s&eacute;rieux presque militaire, punaisant "
  "sur le mur de la chambre de Darius une carte imprim&eacute;e "
  "de la vall&eacute;e de la Loire, marquant d'une croix chacun "
  "des sept sites list&eacute;s dans le fichier r&eacute;cup&eacute;r&eacute;, reliant "
  "Luynes aux six autres points par des lignes trac&eacute;es au "
  "feutre rouge.")

p("Le dessin qui en r&eacute;sulte, une fois toutes les lignes "
  "trac&eacute;es, dessine une forme presque r&eacute;guli&egrave;re, un "
  "hexagone approximatif dont Luynes semble occuper une "
  "position singuli&egrave;re, ni tout &agrave; fait le centre ni tout &agrave; "
  "fait un simple sommet parmi d'autres.")

name("CLARA")
p("&laquo;&nbsp;C'est bizarre, cette forme. On dirait presque que "
  "Luynes a &eacute;t&eacute; choisi expr&egrave;s, pas juste par hasard "
  "g&eacute;ographique. Comme si toute cette histoire avait "
  "toujours &eacute;t&eacute; cens&eacute;e nous retomber dessus, sp&eacute;cifiquement "
  "&agrave; nous, plut&ocirc;t qu'&agrave; n'importe qui d'autre dans la "
  "r&eacute;gion.&nbsp;&raquo;")

p("Darius examine la carte longuement, ce sentiment "
  "d&eacute;sagr&eacute;able d'&ecirc;tre observ&eacute; depuis toujours, m&ecirc;me avant "
  "sa naissance, revenant l'&eacute;treindre avec une intensit&eacute; "
  "nouvelle, comme si le simple fait de tracer ces lignes sur "
  "du papier venait de r&eacute;v&eacute;ler un dessin d'ensemble bien "
  "plus vaste que sa propre existence.")

p("Ils d&eacute;cident, ce soir-l&agrave;, d'inscrire &eacute;galement sur la carte "
  "chaque &eacute;v&eacute;nement marquant de leur propre histoire &mdash; "
  "l'entrep&ocirc;t, la maison Vasseur, la grotte du coteau &mdash; et "
  "remarquent, avec un frisson commun, que ces lieux "
  "dessinent eux aussi une sorte de motif, plus resserr&eacute; mais "
  "tout aussi troublant, comme une r&eacute;plique miniature de la "
  "grande carte r&eacute;gionale.")

name("ALEX")
p("&laquo;&nbsp;C'est comme des poup&eacute;es russes. Un motif dans un "
  "motif dans un motif. Plus on zoome, plus &ccedil;a se ressemble. "
  "&Ccedil;a me donne l'impression que peu importe l'&eacute;chelle &agrave; "
  "laquelle on regarde &ccedil;a, y'a toujours quelque chose qui "
  "nous d&eacute;passe largement au-dessus.&nbsp;&raquo;")

p("Darius range soigneusement la carte, pr&eacute;cieuse et fragile "
  "&agrave; la fois, avant d'enfiler son casque ce soir-l&agrave; comme "
  "chaque soir d&eacute;sormais, et int&egrave;gre, sans trop y r&eacute;fl&eacute;chir, "
  "une repr&eacute;sentation miniature de cette m&ecirc;me carte au "
  "sein de son jeu &mdash; un menu secret, cach&eacute; derri&egrave;re la "
  "porte close, o&ugrave; sept petites lumi&egrave;res clignotent "
  "doucement dans le noir, six d'entre elles &eacute;teintes, une "
  "seule allum&eacute;e.")

p("Clara, de son c&ocirc;t&eacute;, consacre les jours suivants &agrave; "
  "recopier m&eacute;ticuleusement la photocopie du document "
  "du seizi&egrave;me si&egrave;cle offerte par Templier, traduisant "
  "p&eacute;niblement, &agrave; l'aide d'un vieux dictionnaire de "
  "latin d&eacute;nich&eacute; &agrave; la biblioth&egrave;que, chaque passage "
  "obscur du texte original, esp&eacute;rant en tirer des "
  "informations suppl&eacute;mentaires sur la nature exacte de "
  "cette dette ancestrale.")

name("CLARA")
p("&laquo;&nbsp;&Eacute;coutez &ccedil;a : 'le porte-dette rec&ccedil;oit, chaque "
  "fois qu'il n&eacute;gocie avec succ&egrave;s, une marque sur son "
  "propre corps, signe visible de son pacte avec la "
  "rivi&egrave;re.' &Ccedil;a vous fait penser &agrave; quelque chose, "
  "&ccedil;a ?&nbsp;&raquo;")

p("Alex remonte instinctivement sa manche, exposant "
  "sa cicatrice blanche d&eacute;sormais famili&egrave;re, cette "
  "marque physique dont l'origine exacte n'avait "
  "jamais &eacute;t&eacute; totalement &eacute;lucid&eacute;e malgr&eacute; tout ce "
  "qu'ils avaient d&eacute;j&agrave; appris sur la Marge et ses "
  "manifestations.")

name("ALEX")
p("&laquo;&nbsp;Vous croyez que &ccedil;a, c'est ma 'marque du "
  "pacte' ? Genre, une preuve physique que je fais "
  "partie de cette histoire, moi aussi, m&ecirc;me si "
  "c'est pas moi le porteur officiel ?&nbsp;&raquo;")

p("Darius consid&egrave;re cette hypoth&egrave;se avec un s&eacute;rieux "
  "nouveau, repensant &agrave; tout ce que Templier leur "
  "avait racont&eacute; sur sa propre s&oelig;ur, marqu&eacute;e elle "
  "aussi d'une cicatrice similaire avant sa disparition "
  "en 1979, et comprend, avec une inqui&eacute;tude "
  "grandissante, que le r&ocirc;le du &laquo;&nbsp;t&eacute;moin proche&nbsp;&raquo; "
  "semble comporter, lui aussi, des risques et des "
  "marques que personne n'avait jamais explicitement "
  "d&eacute;taill&eacute;s.")

p("Ils passent la soir&eacute;e enti&egrave;re &agrave; approfondir cette "
  "traduction laborieuse, chaque nouvelle phrase "
  "d&eacute;chiffr&eacute;e ajoutant une pi&egrave;ce suppl&eacute;mentaire &agrave; ce "
  "puzzle historique vertigineux, jusqu'&agrave; ce que la "
  "fatigue les gagne tous les trois, aux alentours de "
  "minuit, les laissant avec plus de questions encore "
  "que lorsqu'ils avaient commenc&eacute;.")

p("Le lendemain, un samedi sans cours, ils "
  "retournent ensemble &agrave; la petite maison troglodytique "
  "de Templier, esp&eacute;rant que le vieil homme pourrait "
  "les aider &agrave; d&eacute;chiffrer certains passages du document "
  "encore trop obscurs pour leurs comp&eacute;tences "
  "linguistiques limit&eacute;es, et le trouvent, comme "
  "toujours, occup&eacute; &agrave; tailler sa vigne malgr&eacute; le froid "
  "persistant de f&eacute;vrier.")

p("Templier examine la photocopie avec une "
  "attention redoubl&eacute;e, ajustant ses lunettes &agrave; "
  "plusieurs reprises, et finit par confirmer, avec un "
  "hochement de t&ecirc;te grave, que leur traduction est "
  "globalement exacte, ajoutant m&ecirc;me quelques "
  "nuances suppl&eacute;mentaires tir&eacute;es de sa propre "
  "connaissance du latin d'&eacute;glise appris, des d&eacute;cennies "
  "plus t&ocirc;t, aupr&egrave;s d'un ancien cur&eacute; de la paroisse "
  "voisine.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;Vous avez bien travaill&eacute;, tous les trois. Ce "
  "passage sur la 'marque visible du pacte', &ccedil;a "
  "confirme ce que je pensais depuis longtemps sans "
  "jamais avoir de preuve &eacute;crite &mdash; que les t&eacute;moins "
  "proches, comme votre ami Alex ici pr&eacute;sent, portent "
  "eux aussi une part du fardeau, m&ecirc;me sans &ecirc;tre "
  "directement le porteur d&eacute;sign&eacute; par la l&eacute;gende.&nbsp;&raquo;")

p("Il leur sert, comme &agrave; chaque visite, un th&eacute; fort et "
  "amer dans des tasses d&eacute;pareill&eacute;es, et continue &agrave; "
  "partager, avec cette g&eacute;n&eacute;rosit&eacute; nouvelle qu'il "
  "semble avoir d&eacute;couverte depuis leur premi&egrave;re "
  "rencontre, d'autres fragments de connaissance "
  "accumul&eacute;e durant sa propre existence de porteur "
  "solitaire, chaque d&eacute;tail suppl&eacute;mentaire venant "
  "enrichir la compr&eacute;hension collective qu'ils "
  "b&acirc;tissent, patiemment, de cette histoire millénaire.")

p("Alex, encourag&eacute; par cette r&eacute;v&eacute;lation concernant "
  "sa propre implication dans le pacte ancestral, "
  "profite de ce moment pour interroger Templier sur "
  "un point qui le tracasse depuis des semaines &mdash; la "
  "possibilit&eacute; que sa cicatrice, au-del&agrave; de sa simple "
  "valeur symbolique, puisse un jour repr&eacute;senter un "
  "danger physique r&eacute;el pour lui-m&ecirc;me.")

name("ALEX")
p("&laquo;&nbsp;Est-ce que &ccedil;a peut, genre, s'aggraver avec le "
  "temps ? Ou devenir dangereux d'une mani&egrave;re ou "
  "d'une autre ? Parce que j'avoue que &ccedil;a "
  "m'inqui&egrave;te un peu, de porter un truc que je "
  "comprends pas enti&egrave;rement.&nbsp;&raquo;")

p("Templier r&eacute;fl&eacute;chit longuement avant de r&eacute;pondre, "
  "puisant dans ses propres souvenirs d'observation "
  "de sa s&oelig;ur disparue, avant sa disparition "
  "d&eacute;finitive en 1979, pour tenter d'offrir &agrave; Alex une "
  "r&eacute;ponse aussi honn&ecirc;te que possible, m&ecirc;me si "
  "incompl&egrave;te par nature.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;Ma s&oelig;ur, sa marque &agrave; elle &eacute;tait devenue "
  "plus visible avec les ann&eacute;es, oui, mais elle "
  "n'&eacute;tait jamais devenue dangereuse en soi, "
  "seulement plus pr&eacute;sente, comme si elle refl&eacute;tait "
  "l'intensit&eacute; croissante de son implication dans "
  "cette histoire. Je pense que tant que tu restes "
  "proche de Darius et de cette qu&ecirc;te, ta marque "
  "&eacute;voluera avec elle, sans que &ccedil;a repr&eacute;sente "
  "n&eacute;cessairement un danger physique direct pour "
  "toi.&nbsp;&raquo;")

p("Cette explication, rassurante sans &ecirc;tre "
  "totalement certaine, apaise partiellement "
  "l'inqui&eacute;tude d'Alex, qui d&eacute;cide, ce jour-l&agrave;, "
  "d'accepter enfin pleinement cette marque physique "
  "comme une partie int&eacute;grante de son identit&eacute;, "
  "plut&ocirc;t que comme une menace &agrave; redouter "
  "constamment.")

p("Avant de les laisser repartir ce jour-l&agrave;, "
  "Templier les entra&icirc;ne &agrave; l'ext&eacute;rieur, dans le "
  "petit jardin de vigne baign&eacute; par une lumi&egrave;re "
  "hivernale douce, et leur montre, avec une fiert&eacute; "
  "touchante, les premiers bourgeons timides "
  "commen&ccedil;ant &agrave; poindre malgr&eacute; le froid persistant, "
  "un signe encourageant de la r&eacute;silience naturelle "
  "de cette vigne qu'il entretient depuis des "
  "d&eacute;cennies avec un soin presque religieux.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;Cette vigne, c'est la seule chose qui m'a "
  "vraiment aid&eacute; &agrave; tenir, toutes ces ann&eacute;es. Quand "
  "le poids de tout &ccedil;a devenait trop lourd &agrave; porter "
  "seul, je venais ici, je taillais quelques ceps, et "
  "&ccedil;a me rappelait que m&ecirc;me au c&oelig;ur de l'hiver le "
  "plus rude, quelque chose continue toujours de "
  "pousser, patiemment, sous la surface.&nbsp;&raquo;")

p("Cette image, simple mais profond&eacute;ment touchante, "
  "reste grav&eacute;e dans l'esprit de Darius bien apr&egrave;s "
  "leur d&eacute;part, devenant, dans les mois qui suivent, "
  "une source d'inspiration r&eacute;currente pour son propre "
  "jeu, qu'il enrichit d&eacute;sormais d'un jardin virtuel "
  "cach&eacute; derri&egrave;re l'un des niveaux secondaires, un "
  "petit havre de paix num&eacute;rique o&ugrave; le joueur peut "
  "venir se reposer entre deux &eacute;preuves plus "
  "&eacute;prouvantes.")

p("Sur le chemin du retour, Clara, Alex et Darius "
  "discutent longuement de tout ce que Templier leur "
  "a r&eacute;v&eacute;l&eacute; ce jour-l&agrave;, chacun essayant &agrave; sa "
  "mani&egrave;re d'int&eacute;grer cette id&eacute;e vertigineuse d'une "
  "lign&eacute;e s'&eacute;tendant sur plusieurs si&egrave;cles, une "
  "responsabilit&eacute; qui d&eacute;passe largement le cadre "
  "&eacute;troit de leur propre existence adolescente.")

name("DARIUS")
p("&laquo;&nbsp;&Ccedil;a me fait bizarre de penser &agrave; tous ces "
  "gens avant moi, qui ont d&ucirc; porter exactement le "
  "m&ecirc;me genre de poids, avec les moyens de leur "
  "&eacute;poque, sans internet, sans casque de r&eacute;alit&eacute; "
  "virtuelle, juste leur courage et leur "
  "d&eacute;brouillardise. &Ccedil;a me donne presque honte de me "
  "plaindre, des fois.&nbsp;&raquo;")

p("Clara le rassure imm&eacute;diatement, lui rappelant que "
  "chaque &eacute;poque apporte son propre lot de d&eacute;fis "
  "sp&eacute;cifiques, et que se comparer &agrave; des porteurs "
  "ayant v&eacute;cu dans des contextes historiques "
  "totalement diff&eacute;rents ne rend service &agrave; personne, "
  "surtout pas &agrave; lui-m&ecirc;me qui affronte d&eacute;j&agrave; bien "
  "assez d'&eacute;preuves sans avoir besoin d'y ajouter une "
  "culpabilit&eacute; suppl&eacute;mentaire mal plac&eacute;e.")

name("CLARA")
p("&laquo;&nbsp;Chaque g&eacute;n&eacute;ration se bat avec les armes "
  "qu'elle a, Darius. Le laboureur du dix-huiti&egrave;me "
  "si&egrave;cle avait s&ucirc;rement pas moins peur que toi, "
  "juste parce qu'il avait pas de casque de r&eacute;alit&eacute; "
  "virtuelle. La peur, &ccedil;a change pas vraiment avec "
  "les si&egrave;cles, je crois. Juste les outils pour y "
  "faire face.&nbsp;&raquo;")

p("Alex, marchant en silence &agrave; leurs c&ocirc;t&eacute;s, ajoute "
  "sa propre r&eacute;flexion, plus pragmatique comme "
  "toujours, sur cette continuit&eacute; troublante &agrave; "
  "travers les si&egrave;cles, se demandant &agrave; voix haute "
  "si les t&eacute;moins proches d'autrefois, comme lui "
  "aujourd'hui, avaient eux aussi d&ucirc; porter des "
  "marques physiques similaires &agrave; sa cicatrice.")

name("ALEX")
p("&laquo;&nbsp;&Ccedil;a serait dingue de savoir si y'avait un "
  "'Alex' &agrave; chaque &eacute;poque aussi, tu vois, un pote "
  "fid&egrave;le qui portait sa propre marque en soutenant "
  "le porteur officiel. On saura sans doute jamais, "
  "mais &ccedil;a me fait me sentir moins seul d'imaginer "
  "&ccedil;a, en fait.&nbsp;&raquo;")

p("Cette conversation, men&eacute;e sur le chemin du retour "
  "sous un ciel de f&eacute;vrier d&eacute;j&agrave; assombri, souligne, "
  "une fois de plus, &agrave; quel point cette histoire "
  "extraordinaire a fini par tisser entre les trois "
  "amis une compr&eacute;hension mutuelle et une "
  "profondeur relationnelle rarement atteintes par "
  "des adolescents de leur &acirc;ge.")

p("Ils s'arr&ecirc;tent, avant de se s&eacute;parer chacun vers "
  "leur domicile respectif, sur le petit pont "
  "enjambant l'affluent de la Loire qui traverse "
  "Luynes, ce m&ecirc;me endroit o&ugrave; ils avaient l'habitude, "
  "bien plus jeunes, de jeter des ricochets sans se "
  "soucier de rien d'autre que du nombre de rebonds "
  "obtenus, et Darius ressent, en observant l'eau "
  "sombre couler sous leurs pieds, une nostalgie "
  "douce-amère pour cette innocence perdue.")

name("DARIUS")
p("&laquo;&nbsp;&Ccedil;a me manque, parfois, cette &eacute;poque o&ugrave; "
  "le seul truc important c'&eacute;tait de savoir qui "
  "ferait le plus de ricochets. Mais je regrette pas "
  "non plus tout ce qu'on a d&eacute;couvert depuis. C'est "
  "juste... diff&eacute;rent, je crois. Plus lourd, mais "
  "aussi plus vrai, d'une certaine mani&egrave;re.&nbsp;&raquo;")

p("Clara et Alex acquiescent silencieusement, "
  "partageant cette m&ecirc;me nostalgie teint&eacute;e "
  "d'acceptation, et ils se s&eacute;parent finalement sur "
  "ce pont, chacun regagnant sa propre maison avec "
  "le sentiment r&eacute;confortant d'appartenir &agrave; quelque "
  "chose de bien plus grand et signifiant que leur "
  "simple existence individuelle.")

p("Darius, rentr&eacute; chez lui, s'arr&ecirc;te un instant "
  "devant le miroir de l'entr&eacute;e, observant son "
  "propre reflet avec une attention inhabituelle, "
  "cherchant peut-&ecirc;tre &agrave; d&eacute;celer, dans ses propres "
  "traits, une ressemblance quelconque avec ce "
  "laboureur du dix-huiti&egrave;me si&egrave;cle ou ce meunier "
  "de 1871 dont Templier leur a parl&eacute;, comme si "
  "cette lign&eacute;e ancienne avait laiss&eacute; une empreinte "
  "physique perceptible &agrave; travers les g&eacute;n&eacute;rations.")

p("Il ne trouve, bien s&ucirc;r, rien de particulier dans "
  "ce reflet familier, seulement son propre visage "
  "d'adolescent fatigu&eacute; par une longue journ&eacute;e "
  "d'&eacute;motions et de r&eacute;v&eacute;lations, mais cette "
  "recherche vaine ne l'emp&ecirc;che pas de ressentir, "
  "une fois de plus, cette connexion &eacute;trange et "
  "puissante avec tous ceux qui, avant lui, ont "
  "port&eacute; le m&ecirc;me fardeau sous des formes "
  "diff&eacute;rentes.")

p("Il monte se coucher peu apr&egrave;s, l'esprit encore "
  "travers&eacute; par toutes ces r&eacute;v&eacute;lations "
  "historiques, et s'endort rapidement, &eacute;puis&eacute; par "
  "cette longue journ&eacute;e, sombrant dans un sommeil "
  "sans r&ecirc;ve particulier, comme si son propre corps "
  "avait besoin de cette pause r&eacute;paratrice avant de "
  "pouvoir affronter, le lendemain, la suite de "
  "cette qu&ecirc;te vertigineuse qui ne cesse de "
  "r&eacute;v&eacute;ler de nouvelles ramifications insoup&ccedil;onn&eacute;es.")

p("Le lendemain matin, avant m&ecirc;me de partir pour "
  "le coll&egrave;ge, il prend soin de recopier "
  "soigneusement, dans son propre cahier personnel, "
  "les points essentiels de la conversation de la "
  "veille avec Templier, consolidant m&eacute;thodiquement "
  "cette connaissance historique pr&eacute;cieuse qu'il "
  "sait, d&eacute;sormais, devoir un jour transmettre &agrave; son "
  "tour &agrave; un successeur encore inconnu.")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 6 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 7 -- LE R&Eacute;SEAU
# ======================================================================
chap(7, "LE R&Eacute;SEAU")

p("Ils prennent le train un samedi matin de janvier, sous un "
  "ciel bas qui menace la neige sans jamais tout &agrave; fait s'y "
  "r&eacute;soudre, les trois assis c&ocirc;te &agrave; c&ocirc;te sur la banquette, la "
  "carte de Darius soigneusement pli&eacute;e dans son sac &agrave; "
  "c&ocirc;t&eacute; du second pon&ccedil;on que Templier leur a confi&eacute;, "
  "conscients tous les trois qu'ils s'aventurent, cette fois, "
  "hors du territoire qu'ils connaissent par c&oelig;ur.")

name("ALEX")
p("&laquo;&nbsp;On dit &agrave; personne o&ugrave; on va, hein. Si mes parents "
  "demandent, on est all&eacute;s voir le ch&acirc;teau. C'est pas "
  "vraiment un mensonge, on passera bien devant.&nbsp;&raquo;")

p("Le train longe la Loire pendant tout le trajet, "
  "offrant par la fen&ecirc;tre un d&eacute;fil&eacute; de paysages hivernaux "
  "familiers &mdash; vignes taill&eacute;es court, ch&acirc;teaux "
  "apercevant &agrave; peine leurs toits d'ardoise par-dessus "
  "les arbres nus, petites gares d&eacute;sertes o&ugrave; personne ne "
  "monte ni ne descend &mdash; et Darius, le front pos&eacute; "
  "contre la vitre froide, se surprend &agrave; chercher, dans "
  "chacun de ces villages travers&eacute;s, un signe "
  "quelconque d'un site similaire &agrave; celui de Luynes, "
  "sans jamais savoir exactement &agrave; quoi un tel signe "
  "pourrait bien ressembler.")

name("CLARA")
p("&laquo;&nbsp;J'ai relu le fichier de configuration hier soir, "
  "encore une fois. Y'a un d&eacute;tail qui m'avait &eacute;chapp&eacute; &mdash; "
  "&agrave; c&ocirc;t&eacute; de chaque nom de ville, y'a un petit code, "
  "genre un statut. Amboise est marqu&eacute; 'actif', mais "
  "Chinon est marqu&eacute; 'dormant'. &Ccedil;a doit vouloir dire "
  "que tous les sites sont pas au m&ecirc;me stade "
  "d'activit&eacute;.&nbsp;&raquo;")

p("Cette pr&eacute;cision, ajout&eacute;e &agrave; tout ce qu'ils savent d&eacute;j&agrave;, "
  "renforce chez Darius l'impression grandissante "
  "qu'ils s'appr&ecirc;tent &agrave; p&eacute;n&eacute;trer dans un syst&egrave;me "
  "beaucoup plus organis&eacute; et vivant que ce que "
  "l'apparence poussi&eacute;reuse de l'entrep&ocirc;t de Luynes "
  "avait pu leur laisser imaginer, un r&eacute;seau respirant "
  "encore, quelque part, sous des formes qu'ils ne "
  "peuvent que deviner.")

name("ALEX")
p("&laquo;&nbsp;'Actif' &ccedil;a veut peut-&ecirc;tre dire qu'y a encore "
  "quelqu'un qui va l&agrave;-bas r&eacute;guli&egrave;rement. On devrait "
  "peut-&ecirc;tre &ecirc;tre encore plus prudents que pr&eacute;vu, "
  "alors. Genre, vraiment prudents.&nbsp;&raquo;")

p("Ils descendent finalement du train &agrave; la petite gare "
  "d'Amboise, ses quais presque d&eacute;serts en ce samedi "
  "d'hiver, et s'orientent gr&acirc;ce &agrave; un plan imprim&eacute; par "
  "Clara la veille, marchant d'un pas s&ucirc;r qui masque, "
  "chez chacun d'eux, une appr&eacute;hension grandissante &agrave; "
  "mesure qu'ils s'&eacute;loignent du centre touristique de la "
  "ville pour s'enfoncer vers des quartiers plus "
  "industriels en bordure de Loire.")

p("L'adresse trouv&eacute;e dans le fichier de configuration les "
  "m&egrave;ne, apr&egrave;s une bonne demi-heure de marche depuis la "
  "gare, jusqu'&agrave; un ancien centre de r&eacute;&eacute;ducation reconverti "
  "en simple entrep&ocirc;t municipal, une longue b&acirc;tisse basse en "
  "bordure de Loire dont une partie seulement semble "
  "encore utilis&eacute;e, l'autre condamn&eacute;e par des planches "
  "clou&eacute;es en travers des fen&ecirc;tres.")

p("Un panneau d&eacute;color&eacute; annonce encore, en lettres presque "
  "effac&eacute;es, &laquo;&nbsp;Centre r&eacute;gional d'&eacute;tude comportementale &mdash; "
  "annexe&nbsp;&raquo;, sans autre pr&eacute;cision, et Darius sent, d&egrave;s les "
  "premiers pas dans l'herbe haute qui borde le b&acirc;timent, "
  "cette m&ecirc;me tension famili&egrave;re qui avait pr&eacute;c&eacute;d&eacute; leur "
  "entr&eacute;e dans l'entrep&ocirc;t de Luynes, des mois plus t&ocirc;t.")

p("Ils trouvent une ouverture &agrave; l'arri&egrave;re du b&acirc;timent, une "
  "planche mal fix&eacute;e qui c&egrave;de sans trop de r&eacute;sistance, et "
  "p&eacute;n&egrave;trent dans un long couloir plong&eacute; dans la "
  "pénombre, l'air charg&eacute; d'une odeur de moisissure et de "
  "m&eacute;tal rouill&eacute;, leurs pas r&eacute;sonnant d'une mani&egrave;re qui "
  "semble d&eacute;multipli&eacute;e par le silence total du lieu.")

name("CLARA")
p("&laquo;&nbsp;C'est plus grand que l'entrep&ocirc;t de Luynes. Beaucoup "
  "plus grand. &Ccedil;a devait &ecirc;tre un vrai centre, pas juste un "
  "d&eacute;p&ocirc;t d'archives comme chez nous.&nbsp;&raquo;")

p("Ils avancent prudemment de pi&egrave;ce en pi&egrave;ce, d&eacute;couvrant "
  "des salles d'observation vitr&eacute;es dont les vitres, "
  "curieusement, sont rest&eacute;es intactes malgr&eacute; des d&eacute;cennies "
  "d'abandon, des fauteuils d'examen recouverts de housses "
  "grises, et, au bout d'un dernier couloir, une porte "
  "m&eacute;tallique portant, grav&eacute;e directement dans l'acier, la "
  "m&ecirc;me inscription que celle d&eacute;couverte &agrave; Luynes : "
  "&laquo;&nbsp;PROGRAMME M.13&nbsp;&raquo;.")

p("La pi&egrave;ce qu'elle dissimule s'av&egrave;re bien plus vaste que "
  "celle de l'entrep&ocirc;t d'origine &mdash; une v&eacute;ritable salle des "
  "archives, des rang&eacute;es enti&egrave;res d'&eacute;tag&egrave;res m&eacute;talliques "
  "couvertes de dossiers, certains encore scell&eacute;s, d'autres "
  "&eacute;ventr&eacute;s par le temps ou par des mains anciennes, "
  "laissant &eacute;chapper des feuillets jaunis sur le sol "
  "poussi&eacute;reux.")

p("Darius parcourt les all&eacute;es lentement, cherchant sans trop "
  "savoir quoi exactement, jusqu'&agrave; ce qu'un dossier, plus &eacute;pais "
  "que les autres, attire son attention par la simple "
  "mention inscrite sur sa tranche : &laquo;&nbsp;PORTEURS &mdash; SUIVI "
  "HISTORIQUE &mdash; CONFIDENTIEL.&nbsp;&raquo;")

p("&Agrave; l'int&eacute;rieur, des dizaines de fiches individuelles, "
  "chacune r&eacute;sumant, en quelques lignes administratives et "
  "froides, l'existence d'un porteur diff&eacute;rent &agrave; travers les "
  "si&egrave;cles &mdash; des noms, des dates, des lieux, et syst&eacute;matiquement, "
  "en bas de chaque fiche, un m&ecirc;me champ intitul&eacute; &laquo;&nbsp;issue&nbsp;&raquo;, "
  "rempli tant&ocirc;t de &laquo;&nbsp;retrait naturel&nbsp;&raquo;, tant&ocirc;t, plus "
  "rarement, d'un sobre &laquo;&nbsp;incident&nbsp;&raquo; suivi d'une date.")

name("ALEX")
p("&laquo;&nbsp;'Incident'. C'est un mot bien pratique pour dire "
  "'quelqu'un est mort', non ? Regarde, y'en a genre un "
  "tiers de la liste, marqu&eacute;s comme &ccedil;a. &Ccedil;a fait beaucoup "
  "d'incidents pour un truc qu'on est cens&eacute;s croire "
  "inoffensif.&nbsp;&raquo;")

p("Darius cherche fr&eacute;n&eacute;tiquement, parmi les fiches, celle "
  "correspondant &agrave; Templier, et la trouve enfin, vers le "
  "milieu de la liasse, portant la mention &laquo;&nbsp;retrait naturel, "
  "toujours actif en observation passive&nbsp;&raquo; &mdash; suivie, dans "
  "la marge, d'une note manuscrite plus r&eacute;cente, d'une "
  "encre diff&eacute;rente : &laquo;&nbsp;dernier de sa g&eacute;n&eacute;ration connu &mdash; "
  "successeur non identifi&eacute; &agrave; ce jour.&nbsp;&raquo;")

p("La date port&eacute;e &agrave; c&ocirc;t&eacute; de cette note l'arr&ecirc;te net : "
  "quelques mois seulement avant sa propre premi&egrave;re "
  "rencontre avec Kayden devant la vitrine, comme si "
  "quelqu'un, quelque part, tenait encore ces registres &agrave; "
  "jour, mettant &agrave; profit la moindre information disponible "
  "pour surveiller l'apparition du prochain porteur.")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a veut dire que quelqu'un savait, avant m&ecirc;me que "
  "tout &ccedil;a commence pour toi, qu'il faudrait un nouveau "
  "Darius bient&ocirc;t. &Ccedil;a me fait froid dans le dos, cette id&eacute;e "
  "qu'on t'observait peut-&ecirc;tre d&eacute;j&agrave; avant m&ecirc;me la "
  "vitrine.&nbsp;&raquo;")

p("Ils fouillent encore, trouvant, tout au fond de la salle, "
  "un petit bureau &eacute;quip&eacute; d'un t&eacute;l&eacute;phone d'&eacute;poque et d'un "
  "registre d'appels manuscrit, dont la derni&egrave;re entr&eacute;e, "
  "dat&eacute;e de plusieurs ann&eacute;es seulement, mentionne un num&eacute;ro "
  "sans nom associ&eacute;, simplement suivi de la formule "
  "&laquo;&nbsp;contact de suivi &mdash; ne pas archiver.&nbsp;&raquo;")

p("Darius photographie fi&eacute;vreusement chaque page qui lui "
  "semble importante, sentant l'urgence de repartir avant "
  "que la nuit ne tombe compl&egrave;tement, mais incapable de "
  "quitter tout &agrave; fait cette pi&egrave;ce sans emporter, au moins, "
  "la certitude glaciale qu'ils viennent de mettre le doigt sur "
  "une organisation bien plus active, bien plus pr&eacute;sente "
  "encore aujourd'hui, que ce que Templier lui-m&ecirc;me "
  "semblait imaginer.")

p("En quittant le b&acirc;timent, alors que le soleil hivernal "
  "d&eacute;cline d&eacute;j&agrave; derri&egrave;re les toits d'Amboise, Alex sent sa "
  "cicatrice le br&ucirc;ler d'un coup, plus fort que jamais "
  "auparavant, et tous les trois entendent, aussi clairement "
  "que s'il se tenait juste derri&egrave;re eux, un murmure port&eacute; "
  "par le vent, une seule phrase, glaciale dans sa simplicit&eacute; : "
  "&laquo;&nbsp;ils vous ont d&eacute;j&agrave; trouv&eacute;s aussi.&nbsp;&raquo;")

p("Le trajet de retour se fait dans un silence tendu, aucun "
  "des trois ne parvenant &agrave; formuler clairement ce que cette "
  "phrase murmur&eacute;e &mdash; &laquo;&nbsp;ils vous ont d&eacute;j&agrave; trouv&eacute;s aussi&nbsp;&raquo; &mdash; "
  "signifie exactement, ni qui pourrait bien se cacher "
  "derri&egrave;re ce &laquo;&nbsp;ils&nbsp;&raquo; qui semble d&eacute;signer, pour la "
  "premi&egrave;re fois depuis le d&eacute;but de leur histoire, une "
  "pluralit&eacute; organis&eacute;e plut&ocirc;t qu'une force isol&eacute;e.")

name("CLARA")
p("&laquo;&nbsp;Jusqu'ici, on pensait avoir affaire &agrave; une seule chose "
  "&mdash; la Marge, Kayden, la machine. Mais 'ils', &ccedil;a sous-entend "
  "des gens, Darius. Des gens vivants, aujourd'hui, qui "
  "surveillent encore tout &ccedil;a activement. &Ccedil;a change tout.&nbsp;&raquo;")

p("Darius repense au registre d'appels trouv&eacute; &agrave; Amboise, &agrave; "
  "cette mention &laquo;&nbsp;contact de suivi &mdash; ne pas archiver&nbsp;&raquo;, "
  "et &agrave; la note manuscrite r&eacute;cente sur la fiche de "
  "Templier, et sent grandir en lui une certitude "
  "d&eacute;sagr&eacute;able : quelqu'un, quelque part, continue "
  "d'administrer ce r&eacute;seau bien apr&egrave;s la fermeture officielle "
  "du programme en 1994, avec une discr&eacute;tion qui n'a fait "
  "que s'affiner avec les d&eacute;cennies.")

p("Ils retournent voir Templier d&egrave;s le week-end suivant, "
  "cette fois sans rendez-vous pr&eacute;alable, trouvant le vieil "
  "homme dans son jardin de vigne, occup&eacute; &agrave; tailler des "
  "ceps malgr&eacute; le froid, et lui racontent, d'une traite, tout "
  "ce qu'ils ont d&eacute;couvert &agrave; Amboise.")

p("Le vieil homme les &eacute;coute, son visage se fermant "
  "progressivement &agrave; mesure que le r&eacute;cit avance, et quand "
  "Darius mentionne la phrase entendue dans le vent, il "
  "laisse tomber son s&eacute;cateur dans l'herbe, incapable de "
  "cacher plus longtemps une peur qu'il semblait avoir "
  "enterr&eacute;e depuis tr&egrave;s longtemps.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;J'avais toujours cru &ecirc;tre le dernier maillon abandonn&eacute; "
  "d'un truc qui s'&eacute;tait &eacute;teint tout seul avec le temps. Si "
  "vous me dites qu'il y a encore des gens qui suivent &ccedil;a "
  "activement, alors j'ai eu tort pendant cinquante ans, et &ccedil;a "
  "me fait plus peur que tout ce que j'ai jamais affront&eacute; "
  "&agrave; l'&eacute;poque.&nbsp;&raquo;")

p("Il leur conseille, pour la premi&egrave;re fois depuis leur "
  "rencontre, une extr&ecirc;me prudence &mdash; ne plus visiter "
  "d'autres sites sans pr&eacute;paration, ne plus emporter de "
  "preuves visibles, et surtout, ne jamais r&eacute;pondre &agrave; une "
  "voix qui se pr&eacute;senterait d'elle-m&ecirc;me sans qu'ils l'aient "
  "eux-m&ecirc;mes sollicit&eacute;e, de peur d'attirer une attention qu'ils "
  "ne pourraient plus ensuite d&eacute;tourner.")

name("ALEX")
p("&laquo;&nbsp;Vous croyez qu'on devrait juste... arr&ecirc;ter ? Faire "
  "comme si on n'avait rien vu, refermer tout &ccedil;a et essayer "
  "de vivre normalement ? Parce que j'avoue que &ccedil;a "
  "commence &agrave; devenir beaucoup, m&ecirc;me pour nous.&nbsp;&raquo;")

p("Darius sent, en entendant cette question, une tension "
  "sourde s'installer entre eux trois pour la premi&egrave;re fois "
  "depuis des mois &mdash; Alex fatigu&eacute; de porter une histoire "
  "qui ne lui appartient qu'&agrave; moiti&eacute;, Clara d&eacute;chir&eacute;e entre sa "
  "curiosit&eacute; naturelle et son inqui&eacute;tude grandissante pour "
  "ses deux amis, et lui-m&ecirc;me, incapable, quoi qu'il arrive, "
  "d'imaginer tourner le dos &agrave; un r&ocirc;le qu'il sait d&eacute;sormais "
  "porter depuis bien avant sa naissance.")

name("DARIUS")
p("&laquo;&nbsp;Je peux pas arr&ecirc;ter, m&ecirc;me si je voulais. Templier "
  "a essay&eacute; de vivre normalement pendant cinquante ans, "
  "et &ccedil;a l'a quand m&ecirc;me rattrap&eacute; &agrave; la fin. Mais vous, "
  "vous pouvez vous retirer, si vous voulez. Je vous en "
  "voudrai pas. &Ccedil;a a jamais &eacute;t&eacute; votre fardeau &agrave; "
  "vous.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;Arr&ecirc;te tes b&ecirc;tises. On t'a pas laiss&eacute; tomber dans "
  "l'entrep&ocirc;t, on t'a pas laiss&eacute; tomber dans le Non-lieu, "
  "c'est pas maintenant qu'on va commencer. Mais on peut "
  "quand m&ecirc;me &ecirc;tre inquiets pour toi de temps en temps, "
  "&ccedil;a change rien &agrave; notre d&eacute;cision de rester.&nbsp;&raquo;")

p("Alex hoche la t&ecirc;te en silence, confirmant sans un mot "
  "suppl&eacute;mentaire son propre attachement &agrave; cette histoire "
  "commune, et les trois amis repartent de chez Templier "
  "avec la certitude renforc&eacute;e que quoi qu'il advienne "
  "d&eacute;sormais, ils l'affronteront ensemble, comme ils l'ont "
  "toujours fait depuis la vitrine sous la pluie.")

p("Ce soir-l&agrave;, pourtant, seul dans sa chambre, Darius ne "
  "parvient pas &agrave; se d&eacute;faire d'une pens&eacute;e persistante, "
  "presque honteuse : que la meilleure fa&ccedil;on de prot&eacute;ger "
  "vraiment Clara et Alex de ce qui semble maintenant les "
  "guetter tous, serait peut-&ecirc;tre, un jour, de trouver un "
  "moyen de porter cette histoire enti&egrave;rement seul, jusqu'au "
  "bout, sans plus jamais les y m&ecirc;ler.")

p("Les semaines suivantes ne ram&egrave;nent aucune nouvelle "
  "manifestation aussi directe que la phrase entendue &agrave; "
  "Amboise, mais une s&eacute;rie de petits signes discrets "
  "continue de ponctuer le quotidien de Darius, chacun trop "
  "faible pour &ecirc;tre certain, mais trop r&eacute;p&eacute;t&eacute; pour &ecirc;tre "
  "totalement ignor&eacute; &mdash; une lumi&egrave;re de r&eacute;verb&egrave;re qui "
  "clignote deux fois de trop en passant devant chez lui, "
  "un &eacute;cran de t&eacute;l&eacute;phone qui affiche, une demi-seconde, un "
  "motif de lignes verticales avant de revenir &agrave; la normale.")

p("Il consigne chacun de ces d&eacute;tails dans son cahier "
  "personnel, &agrave; c&ocirc;t&eacute; des notes prises chez Templier, "
  "construisant peu &agrave; peu une sorte de journal de bord "
  "qu'il ne montre &agrave; personne, pas m&ecirc;me &agrave; Clara, "
  "conscient qu'&agrave; force de r&eacute;p&eacute;ter ses inqui&eacute;tudes il "
  "finirait par les inqui&eacute;ter, elle et Alex, bien plus que "
  "n&eacute;cessaire.")

p("Le carnet de Clara, lui, reste silencieux pendant "
  "plusieurs semaines, comme si le fragment de Kayden "
  "s'&eacute;tait retir&eacute; suite &agrave; leur d&eacute;couverte &agrave; Amboise, "
  "pr&eacute;f&eacute;rant peut-&ecirc;tre laisser d'autres forces, plus "
  "organis&eacute;es, prendre le relais de la communication.")

p("C'est en f&eacute;vrier, un soir o&ugrave; Darius travaille tard sur "
  "son jeu, que la voix revient, plus nette que jamais, "
  "directement dans le casque, se m&ecirc;lant &agrave; la bande sonore "
  "qu'il a lui-m&ecirc;me compos&eacute;e pour son niveau, comme si "
  "elle avait trouv&eacute; l&agrave;, dans ce monde qu'il pensait "
  "enti&egrave;rement sien, un canal id&eacute;al pour se faire entendre "
  "&agrave; nouveau.")

p("&laquo;&nbsp;Ils comptent les jours, maintenant. Pas les tiens. Les "
  "leurs. Fais attention &agrave; ce que tu construis, Darius. Une "
  "porte, &ccedil;a s'ouvre dans les deux sens.&nbsp;&raquo;")

p("Darius retire le casque d'un geste brusque, le c&oelig;ur "
  "battant, incertain d'avoir vraiment entendu ces mots ou "
  "d'avoir simplement laiss&eacute; son imagination, fatigu&eacute;e par "
  "des semaines de tension, lui jouer un mauvais tour &mdash; "
  "mais quand il consulte, quelques minutes plus tard, le "
  "fichier audio de son propre jeu, il y d&eacute;couvre, "
  "impossible &agrave; expliquer, une piste suppl&eacute;mentaire qu'il "
  "n'a jamais enregistr&eacute;e lui-m&ecirc;me.")

p("Il h&eacute;site longuement avant de la faire &eacute;couter &agrave; Clara "
  "et Alex, craignant, une fois de plus, de les entra&icirc;ner "
  "encore plus profond&eacute;ment dans une histoire qui semble, "
  "chaque mois qui passe, exiger un peu plus d'eux tous, "
  "mais finit par c&eacute;der, fid&egrave;le &agrave; la promesse faite apr&egrave;s "
  "Amboise de ne plus rien leur cacher.")

name("CLARA")
p("&laquo;&nbsp;'Une porte, &ccedil;a s'ouvre dans les deux sens.' &Ccedil;a "
  "veut dire que ton jeu, cette fameuse porte close que t'as "
  "ajout&eacute;e, &ccedil;a pourrait pas juste servir &agrave; faire sortir "
  "quelque chose. &Ccedil;a pourrait aussi servir &agrave; faire entrer "
  "quelque chose d'autre. Chez toi, dans ta chambre, dans "
  "ta t&ecirc;te.&nbsp;&raquo;")

p("Darius sent un froid glacial lui traverser le corps en "
  "entendant cette hypoth&egrave;se formul&eacute;e &agrave; voix haute, ce qui "
  "n'&eacute;tait jusqu'alors qu'une inqui&eacute;tude vague prenant, "
  "d'un coup, une forme bien plus concr&egrave;te et bien plus "
  "menaçante que tout ce qu'il avait envisag&eacute; jusqu'ici.")

name("ALEX")
p("&laquo;&nbsp;Peut-&ecirc;tre que tu devrais arr&ecirc;ter ce jeu, Darius. "
  "Vraiment, s&eacute;rieusement. Je sais que &ccedil;a compte pour toi, "
  "mais si &ccedil;a devient une porte pour un truc qu'on comprend "
  "m&ecirc;me pas enti&egrave;rement, &ccedil;a vaut peut-&ecirc;tre pas le "
  "risque.&nbsp;&raquo;")

p("Darius promet d'y r&eacute;fl&eacute;chir s&eacute;rieusement, sinc&egrave;rement "
  "tent&eacute; sur le moment d'abandonner enti&egrave;rement le projet, "
  "mais quand il se retrouve seul, ce soir-l&agrave;, devant son "
  "casque pos&eacute; sur le bureau, il ne parvient pas &agrave; se "
  "r&eacute;soudre &agrave; l'&eacute;teindre d&eacute;finitivement, comme si "
  "quelque chose, en lui, refusait cat&eacute;goriquement l'id&eacute;e "
  "d'abandonner le seul espace o&ugrave; il se sent encore, malgr&eacute; "
  "tout, ma&icirc;tre de son destin.")

p("Franck, de son c&ocirc;t&eacute;, tient parole d'une mani&egrave;re que "
  "Darius n'aurait pas anticip&eacute;e quelques mois plus t&ocirc;t &mdash; "
  "il t&eacute;l&eacute;phone plus souvent, propose des sorties simples, "
  "un cin&eacute;ma, une promenade au bord de la Loire, et surtout, "
  "il commence, maladroitement mais sinc&egrave;rement, &agrave; parler "
  "de choses qu'il aurait autrefois enterr&eacute;es sans h&eacute;siter.")

name("FRANCK")
p("&laquo;&nbsp;J'ai repris contact avec un genre de th&eacute;rapeute, "
  "figure-toi. Pas pour parler de Kayden directement, "
  "j'saurais m&ecirc;me pas par o&ugrave; commencer avec &ccedil;a, mais "
  "pour apprendre &agrave; dire les choses avant qu'elles "
  "pourrissent en moi. C'est nouveau, pour moi, tout &ccedil;a. Je "
  "te promets rien de miraculeux, mais j'essaie.&nbsp;&raquo;")

p("Darius l'&eacute;coute avec une tendresse teint&eacute;e de prudence, "
  "encore trop marqu&eacute; par des ann&eacute;es d'habitudes pour se "
  "laisser aller enti&egrave;rement &agrave; la confiance, mais reconnaissant, "
  "malgr&eacute; tout, un effort r&eacute;el, palpable, dans cette nouvelle "
  "mani&egrave;re qu'a son p&egrave;re de le regarder droit dans les yeux "
  "plut&ocirc;t que de fuir chaque conversation difficile.")

p("Un dimanche, Franck l'emm&egrave;ne, sans pr&eacute;venir, jusqu'au "
  "petit cimeti&egrave;re des animaux d'une clinique v&eacute;t&eacute;rinaire "
  "voisine, expliquant, la gorge nou&eacute;e, qu'il a fini par "
  "retrouver la trace de Miel &mdash; d&eacute;c&eacute;d&eacute; de vieillesse "
  "quelques ann&eacute;es plus t&ocirc;t chez la famille qui l'avait "
  "recueilli, entour&eacute; et aim&eacute; jusqu'au bout.")

name("FRANCK")
p("&laquo;&nbsp;J'ai retrouv&eacute; les gens qui l'ont eu, gr&acirc;ce &agrave; "
  "l'ancien refuge. Ils m'ont montr&eacute; des photos. Il avait "
  "l'air heureux, Darius, vraiment. &Ccedil;a change rien au fait "
  "que je t'ai menti, mais je voulais que tu saches, au "
  "moins, qu'il a pas souffert de ce que j'ai fait. Je "
  "voulais te dire &ccedil;a en face, pas te laisser deviner.&nbsp;&raquo;")

p("Darius sent les larmes lui monter aux yeux, un chagrin "
  "ancien et une gratitude nouvelle se m&ecirc;lant "
  "inextricablement, et pour la premi&egrave;re fois depuis des "
  "ann&eacute;es, il serre son p&egrave;re dans ses bras sans que ce "
  "geste ne lui semble forc&eacute; ou &eacute;trange, simplement juste, "
  "n&eacute;cessaire, longtemps d&ucirc;.")

p("Ces retrouvailles progressives avec Franck offrent &agrave; "
  "Darius un contrepoint pr&eacute;cieux &agrave; l'inqui&eacute;tude grandissante "
  "que lui inspire le reste de son existence &mdash; comme si, "
  "pendant que la Marge et son r&eacute;seau invisible resserraient "
  "leur &eacute;tau autour de lui, une petite partie de sa vie, "
  "enfin, choisissait de gu&eacute;rir plut&ocirc;t que de s'enfoncer "
  "davantage.")

p("Il ne parle toujours pas &agrave; son p&egrave;re de la possession "
  "subie dans le Non-lieu, ni de la voix qu'il continue "
  "d'entendre parfois, ni de cette phrase inqui&eacute;tante "
  "entendue dans son propre jeu &mdash; pr&eacute;f&eacute;rant, pour "
  "l'instant, prot&eacute;ger cette relation encore fragile d'un "
  "poids suppl&eacute;mentaire qu'il craint de la voir "
  "s'effondrer sous cette charge trop lourde, trop t&ocirc;t.")

p("Le printemps ram&egrave;ne &agrave; Luynes cette lumi&egrave;re particuli&egrave;re "
  "que Darius associe toujours, depuis l'enfance, &agrave; un "
  "sentiment de recommencement, les cerisiers de la place "
  "fleurissant en quelques jours &agrave; peine, les terrasses "
  "rouvrant, les habitants retrouvant cette l&eacute;g&egrave;ret&eacute; "
  "collective propre aux premiers beaux jours apr&egrave;s un "
  "hiver trop long.")

p("Aucune nouvelle manifestation majeure ne vient troubler "
  "ces semaines plus calmes, comme si la Marge elle-m&ecirc;me "
  "s'&eacute;tait accord&eacute; une tr&ecirc;ve, et Darius, Clara et Alex en "
  "profitent pour retrouver, autant que possible, une "
  "existence plus ordinaire &mdash; les r&eacute;visions pour la fin "
  "d'ann&eacute;e, des apr&egrave;s-midi entiers pass&eacute;s au bord de la "
  "Loire sans qu'aucune ombre ne vienne g&acirc;ter le simple "
  "plaisir d'&ecirc;tre ensemble.")

p("Darius continue, malgr&eacute; tout, de travailler sur son jeu, "
  "mais avec une prudence nouvelle &mdash; il d&eacute;sactive la piste "
  "audio myst&eacute;rieuse d&eacute;couverte en f&eacute;vrier, &eacute;vite de "
  "travailler trop tard le soir, et se limite, la plupart du "
  "temps, &agrave; des s&eacute;ances plus courtes, comme s'il "
  "cherchait, sans se l'avouer enti&egrave;rement, &agrave; rassurer "
  "Clara et Alex sur sa propre capacit&eacute; &agrave; garder le "
  "contr&ocirc;le.")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a fait du bien de te voir un peu plus... l&eacute;ger, ces "
  "derniers temps. J'esp&egrave;re que &ccedil;a dure. On a peut-&ecirc;tre "
  "le droit, nous aussi, &agrave; une ann&eacute;e tranquille de temps "
  "en temps.&nbsp;&raquo;")

p("Il voudrait la croire enti&egrave;rement, se laisser aller sans "
  "arri&egrave;re-pens&eacute;e &agrave; cette accalmie printani&egrave;re, mais une "
  "partie de lui, form&eacute;e par des mois de r&eacute;v&eacute;lations "
  "successives, reste en alerte constante, incapable de "
  "croire tout &agrave; fait qu'une histoire aussi vaste que la leur "
  "puisse simplement se calmer sans raison particuli&egrave;re.")

p("Il retourne voir Templier une derni&egrave;re fois avant l'&eacute;t&eacute;, "
  "le trouvant amaigri mais toujours aussi lucide, assis "
  "dans son jardin de vigne bourgeonnant, et le vieil homme "
  "lui confie, avec une gravit&eacute; douce qui contraste avec la "
  "l&eacute;g&egrave;ret&eacute; de la saison, qu'il sent ses propres forces "
  "d&eacute;cliner un peu plus chaque mois.")

name("DARIUS TEMPLIER")
p("&laquo;&nbsp;J'ai pas peur de mourir, petit, rassure-toi. J'ai eu "
  "une bonne vie, m&ecirc;me avec tout &ccedil;a accroch&eacute; derri&egrave;re moi. "
  "Ce qui m'inqui&egrave;te un peu plus, c'est de partir avant "
  "d'&ecirc;tre certain que tu sauras porter &ccedil;a mieux que je "
  "l'ai fait, moi, tout seul pendant si longtemps.&nbsp;&raquo;")

p("Darius lui promet, la gorge serr&eacute;e, de continuer &agrave; "
  "&eacute;crire dans son cahier, de transmettre un jour, "
  "correctement, tout ce que Templier lui a appris, et "
  "repart ce jour-l&agrave; avec la certitude un peu triste que "
  "cette conversation restera, d'une mani&egrave;re ou d'une "
  "autre, l'une des derni&egrave;res qu'ils partageront jamais tous "
  "les deux.")

p("Darius Templier meurt paisiblement dans son sommeil un "
  "matin de juin, retrouv&eacute; par un voisin venu lui apporter "
  "son pain, et la nouvelle, rapport&eacute;e par Mme Ferrand qui "
  "l'apprend elle-m&ecirc;me par une cousine &eacute;loign&eacute;e de la "
  "famille, frappe Darius avec une violence qu'il n'aurait "
  "pas anticip&eacute;e pour un homme rencontr&eacute; seulement "
  "quelques mois plus t&ocirc;t.")

name("CLARA")
p("&laquo;&nbsp;Je suis d&eacute;sol&eacute;e, Darius. Je sais &agrave; quel point il "
  "comptait pour toi, m&ecirc;me si vous vous connaissiez pas "
  "depuis longtemps. C'&eacute;tait comme... j'sais pas, un "
  "grand-p&egrave;re qu'on choisit, dans un sens.&nbsp;&raquo;")

p("Ils assistent tous les trois &agrave; l'enterrement, discret, "
  "quelques voisins seulement, aucune famille proche "
  "identifiable, et Darius ressent, en d&eacute;posant une fleur sur "
  "le cercueil, une solitude nouvelle et vertigineuse &mdash; celle "
  "d'&ecirc;tre d&eacute;sormais, officiellement, le dernier maillon "
  "connu d'une lign&eacute;e qui s'&eacute;tend sur des si&egrave;cles, sans "
  "successeur identifi&eacute;, exactement comme l'indiquait la "
  "fiche trouv&eacute;e &agrave; Amboise.")

p("Il h&eacute;rite, quelques semaines plus tard, par l'entremise "
  "d'un notaire visiblement perplexe face &agrave; cette "
  "disposition inhabituelle, de la petite maison "
  "troglodytique du coteau et de son jardin de vigne, "
  "l&eacute;gu&eacute;s express&eacute;ment &agrave; son nom par un testament "
  "r&eacute;dig&eacute; quelques jours seulement apr&egrave;s leur premi&egrave;re "
  "rencontre.")

p("Une lettre accompagne l'h&eacute;ritage, la derni&egrave;re &eacute;criture "
  "de Templier, dont Darius met plusieurs jours avant de "
  "trouver le courage de la lire enti&egrave;rement, redoutant ce "
  "qu'elle pourrait contenir de trop lourd &agrave; porter en plus "
  "de tout le reste.")

p("&laquo;&nbsp;Si tu lis &ccedil;a, c'est que je suis parti avant d'avoir pu "
  "tout te dire. Garde la maison, garde la vigne, m&ecirc;me si "
  "tu sais pas quoi en faire &agrave; quatorze ans. Un jour &ccedil;a te "
  "servira de refuge, j'en suis certain. Et souviens-toi : "
  "porter &ccedil;a seul use plus vite qu'on croit. Ne fais pas mon "
  "erreur. Laisse les gens qui t'aiment porter un peu du "
  "poids avec toi, m&ecirc;me quand tu crois que &ccedil;a les "
  "prot&eacute;gerait mieux de les tenir &agrave; l'&eacute;cart.&nbsp;&raquo;")

p("Darius replie la lettre avec un soin presque religieux, la "
  "rangeant dans la bo&icirc;te en bois aux c&ocirc;t&eacute;s du pon&ccedil;on, du "
  "b&acirc;ton et du carnet, sentant confus&eacute;ment que cet "
  "avertissement final, venu d'un homme qui a v&eacute;cu "
  "exactement ce que lui-m&ecirc;me traverse, m&eacute;rite d'&ecirc;tre pris "
  "bien plus au s&eacute;rieux que toutes les inqui&eacute;tudes formul&eacute;es "
  "jusque-l&agrave; par Clara et Alex r&eacute;unis.")

p("Il passe, cet &eacute;t&eacute;-l&agrave;, de nombreuses apr&egrave;s-midi dans la "
  "petite maison du coteau, apprenant &agrave; s'occuper "
  "maladroitement de la vigne avec l'aide d'un voisin "
  "vigneron compatissant, et ressent, dans ce lieu impr&eacute;gn&eacute; "
  "de la pr&eacute;sence de Templier, une paix particuli&egrave;re qu'il "
  "ne retrouve nulle part ailleurs, pas m&ecirc;me dans son "
  "casque de r&eacute;alit&eacute; virtuelle.")

p("La brouille &eacute;clate en ao&ucirc;t, presque sans pr&eacute;venir, un "
  "soir o&ugrave; Clara et Alex retrouvent Darius chez lui pour "
  "regarder un film et le trouvent, casque sur les yeux, "
  "compl&egrave;tement absorb&eacute; par son jeu, ayant visiblement "
  "oubli&eacute; leur rendez-vous fix&eacute; depuis plusieurs jours.")

name("ALEX")
p("&laquo;&nbsp;&Ccedil;a fait vingt minutes qu'on t'attend en bas, "
  "Darius. Ta m&egrave;re a d&ucirc; nous faire entrer parce que t'as "
  "m&ecirc;me pas entendu la sonnette. C'est pas normal, "
  "l&agrave;, sinc&egrave;rement.&nbsp;&raquo;")

p("Darius retire le casque, d&eacute;sorient&eacute;, la culpabilit&eacute; se "
  "m&ecirc;lant &agrave; une irritation confuse qu'il ne comprend pas "
  "lui-m&ecirc;me enti&egrave;rement, comme si le simple fait d'&ecirc;tre "
  "interrompu en pleine cr&eacute;ation lui co&ucirc;tait davantage "
  "d'effort qu'il ne voudrait l'admettre.")

name("DARIUS")
p("&laquo;&nbsp;D&eacute;sol&eacute;, j'ai perdu la notion du temps, c'est tout. "
  "&Ccedil;a arrive &agrave; tout le monde.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a arrive &agrave; tout le monde une fois, Darius, pas "
  "toutes les semaines depuis des mois. On te parle depuis "
  "l'hiver, tous les deux, et t'entends toujours pas, ou "
  "t'entends mais tu changes rien. J'ai l'impression de "
  "parler &agrave; quelqu'un qui pr&eacute;f&egrave;re vraiment son monde "
  "invent&eacute; au n&ocirc;tre, des fois.&nbsp;&raquo;")

p("Le mot &laquo;&nbsp;invent&eacute;&nbsp;&raquo; le blesse plus qu'elle ne l'aurait "
  "voulu, et Darius sent monter en lui une col&egrave;re "
  "disproportionn&eacute;e, aliment&eacute;e par des mois de fatigue "
  "accumul&eacute;e, de secrets port&eacute;s seul malgr&eacute; ses promesses, "
  "et par cette petite voix, toujours tapie quelque part au "
  "fond de lui, qui n'est pas tout &agrave; fait la sienne.")

name("DARIUS")
p("&laquo;&nbsp;Vous savez rien de ce que c'est, porter tout &ccedil;a. "
  "Vous, vous pouvez rentrer chez vous et oublier "
  "temporairement, moi je peux jamais vraiment m'&eacute;chapper "
  "de rien, sauf l&agrave;-dedans. Alors excusez-moi si j'ai besoin "
  "d'un endroit &agrave; moi de temps en temps.&nbsp;&raquo;")

p("Le silence qui suit cette r&eacute;plique p&egrave;se plus lourd que "
  "n'importe quelle dispute pr&eacute;c&eacute;dente entre eux, Clara "
  "et Alex &eacute;chang&eacute;ant un regard bless&eacute;, et Darius, voyant "
  "leurs visages se fermer, comprend, une seconde trop "
  "tard, &agrave; quel point il vient de trahir, d'une mani&egrave;re "
  "inattendue, la promesse faite &agrave; Templier de ne jamais "
  "les tenir &agrave; l'&eacute;cart par fausse protection.")

name("ALEX")
p("&laquo;&nbsp;On sait peut-&ecirc;tre pas tout ce que &ccedil;a te fait, mais "
  "on a quand m&ecirc;me &eacute;t&eacute; l&agrave;, Darius, &agrave; chaque fois. "
  "L'entrep&ocirc;t, le Non-lieu, Templier, Amboise. On a pris "
  "les m&ecirc;mes risques que toi. &Ccedil;a compte un peu, "
  "non ?&nbsp;&raquo;")

p("Ils repartent, ce soir-l&agrave;, sans se r&eacute;concilier "
  "compl&egrave;tement, et Darius reste seul dans sa chambre, "
  "rong&eacute; par une culpabilit&eacute; qui, curieusement, ne suffit "
  "pas &agrave; le convaincre de retirer d&eacute;finitivement son casque, "
  "comme si une partie de lui, de plus en plus difficile &agrave; "
  "ignorer, pr&eacute;f&eacute;rait dor&eacute;navant ce monde ma&icirc;tris&eacute; &agrave; "
  "n'importe quelle relation r&eacute;elle, m&ecirc;me les plus "
  "pr&eacute;cieuses.")

p("Il faut une semaine enti&egrave;re de silence tendu, et "
  "l'intervention discr&egrave;te de Franck, mis dans la confidence "
  "par un Darius d&eacute;sempar&eacute;, pour que la r&eacute;conciliation "
  "commence &agrave; se dessiner entre les trois amis.")

name("FRANCK")
p("&laquo;&nbsp;J'ai pass&eacute; des ann&eacute;es &agrave; croire que m'isoler "
  "&eacute;tait la meilleure fa&ccedil;on de prot&eacute;ger les gens que "
  "j'aimais de mes propres probl&egrave;mes. &Ccedil;a a jamais march&eacute;. "
  "&Ccedil;a a juste fini par les &eacute;loigner encore plus. Si Clara et "
  "Alex comptent vraiment pour toi, va les voir, "
  "excuse-toi, et surtout, &eacute;coute vraiment ce qu'ils te "
  "disent, m&ecirc;me si &ccedil;a fait mal &agrave; entendre.&nbsp;&raquo;")

p("Darius retrouve Clara et Alex un samedi apr&egrave;s-midi au "
  "bord de la Loire, l&agrave; o&ugrave; ils ont l'habitude de s'asseoir "
  "depuis des ann&eacute;es, et s'excuse maladroitement, sans "
  "chercher &agrave; minimiser ce qu'il leur a dit ni &agrave; se "
  "trouver des excuses trop faciles.")

name("DARIUS")
p("&laquo;&nbsp;J'avais tort. Vous avez port&eacute; exactement autant que "
  "moi depuis le d&eacute;but, et j'ai aucun droit de faire "
  "comme si mon fardeau &eacute;tait plus lourd que le v&ocirc;tre. "
  "Je crois juste que... j'ai peur, en fait. Peur de finir "
  "comme Templier, seul avec tout &ccedil;a. Et j'ai g&eacute;r&eacute; cette "
  "peur en me construisant un endroit o&ugrave; personne peut "
  "me d&eacute;cevoir ni me quitter. C'&eacute;tait pas juste contre "
  "vous.&nbsp;&raquo;")

p("Clara le regarde longuement, cette franchise nouvelle "
  "d&eacute;sarmant sa propre col&egrave;re accumul&eacute;e, et finit par lui "
  "prendre la main, un geste simple mais qui vaut, entre "
  "eux, plus que n'importe quel discours.")

name("CLARA")
p("&laquo;&nbsp;On va pas te quitter, Darius. Ni Alex ni moi. Mais "
  "faut que tu nous laisses entrer un peu plus, m&ecirc;me dans "
  "les trucs difficiles &agrave; dire. Sinon &ccedil;a sert &agrave; rien qu'on "
  "soit l&agrave;, si on peut jamais vraiment t'atteindre.&nbsp;&raquo;")

p("Ils passent le reste de l'apr&egrave;s-midi &agrave; parler, vraiment "
  "parler, comme ils ne l'avaient plus fait depuis des mois, "
  "et Darius rentre chez lui ce soir-l&agrave; all&eacute;g&eacute; d'un poids "
  "qu'il ne mesurait m&ecirc;me plus, promettant, sinc&egrave;rement "
  "cette fois, de limiter ses heures de jeu et de ne plus "
  "rien leur cacher, m&ecirc;me quand la v&eacute;rit&eacute; lui semble trop "
  "lourde &agrave; partager.")

p("Il tient cette promesse tant bien que mal les semaines "
  "suivantes, retrouvant un &eacute;quilibre plus sain entre son "
  "projet et ses amis, sans se douter un seul instant que "
  "cette derni&egrave;re rentr&eacute;e des classes, celle qui approche "
  "d&eacute;j&agrave; &agrave; grands pas, sera la derni&egrave;re qu'il conna&icirc;tra "
  "jamais enti&egrave;rement.")

p("La rentr&eacute;e de septembre ram&egrave;ne Darius, Clara et Alex en "
  "classe de troisi&egrave;me, derni&egrave;re ann&eacute;e de coll&egrave;ge, avec "
  "son lot habituel de nouveaux professeurs, d'emplois du "
  "temps &agrave; apprivoiser, et cette pression sourde du brevet "
  "qui plane d&eacute;j&agrave; sur les conversations de couloir, comme "
  "chaque ann&eacute;e &agrave; la m&ecirc;me &eacute;poque.")

p("Darius retrouve, avec un plaisir sinc&egrave;re, cette routine "
  "presque banale, savourant chaque journ&eacute;e ordinaire "
  "comme une petite victoire apr&egrave;s les mois tumultueux "
  "travers&eacute;s depuis le d&eacute;but de l'ann&eacute;e pr&eacute;c&eacute;dente, et "
  "s'efforce, fid&egrave;le &agrave; sa promesse, de limiter ses soir&eacute;es "
  "de jeu &agrave; deux ou trois par semaine seulement.")

p("Franck continue &agrave; venir le chercher r&eacute;guli&egrave;rement, leur "
  "relation prenant peu &agrave; peu une texture nouvelle, plus "
  "l&eacute;g&egrave;re, faite de petites habitudes partag&eacute;es &mdash; un "
  "match de foot regard&eacute; ensemble, une recette essay&eacute;e "
  "en cuisine, des silences qui ne p&egrave;sent plus comme "
  "avant, simplement confortables.")

name("FRANCK")
p("&laquo;&nbsp;Je suis fier de toi, tu sais. Pas juste pour tout ce "
  "que t'as travers&eacute; avec cette histoire de Kayden et de "
  "Marge, mais pour comment t'as g&eacute;r&eacute; &ccedil;a. T'es plus "
  "solide que moi &agrave; ton &acirc;ge, franchement, et &ccedil;a me "
  "rassure autant que &ccedil;a m'&eacute;pate.&nbsp;&raquo;")

p("Clara, de son c&ocirc;t&eacute;, entame en parall&egrave;le un projet "
  "personnel qui la passionne, un carnet de recherches "
  "consacr&eacute; enti&egrave;rement &agrave; l'histoire de Luynes, o&ugrave; elle "
  "consigne, discr&egrave;tement mais m&eacute;thodiquement, tout ce "
  "qu'elle a appris sur la l&eacute;gende de la Marge, esp&eacute;rant "
  "peut-&ecirc;tre, elle aussi, laisser une trace pour un &eacute;ventuel "
  "successeur.")

p("Alex, de son c&ocirc;t&eacute;, retrouve une saison de foot "
  "prometteuse, sa cicatrice restant silencieuse depuis "
  "l'&eacute;pisode d'Amboise, ce qui le rassure suffisamment pour "
  "envisager, pour la premi&egrave;re fois depuis des mois, un "
  "avenir o&ugrave; la Marge ne serait plus qu'un chapitre "
  "referm&eacute; de leur adolescence.")

p("Cette accalmie, pourtant, ne dure jamais bien longtemps "
  "dans leur histoire commune, et Darius, malgr&eacute; ses "
  "efforts sinc&egrave;res pour vivre normalement, ne peut "
  "s'emp&ecirc;cher de remarquer, certains soirs, cette sensation "
  "famili&egrave;re d'&ecirc;tre observ&eacute;, comme si quelque chose, quelque "
  "part, continuait patiemment de compter les jours qui le "
  "s&eacute;parent d'un rendez-vous qu'il n'a jamais fix&eacute; "
  "lui-m&ecirc;me.")

p("C'est par un simple hasard, en octobre, que Clara "
  "d&eacute;couvre, en consultant les archives municipales pour "
  "son projet personnel, la mention d'une r&eacute;union pr&eacute;vue &agrave; "
  "la pr&eacute;fecture de Tours concernant &laquo;&nbsp;la r&eacute;affectation de "
  "plusieurs sites d&eacute;saffect&eacute;s de la r&eacute;gion&nbsp;&raquo;, parmi "
  "lesquels figure express&eacute;ment l'ancien centre d'Amboise.")

name("CLARA")
p("&laquo;&nbsp;Ils veulent transformer le b&acirc;timent en logements, "
  "apparemment. &Ccedil;a veut dire qu'ils vont tout vider, tout "
  "d&eacute;m&eacute;nager, peut-&ecirc;tre m&ecirc;me d&eacute;truire les archives "
  "qu'on a trouv&eacute;es. Si on veut en savoir plus, c'est "
  "maintenant ou jamais.&nbsp;&raquo;")

p("Darius sent une pointe d'inqui&eacute;tude &agrave; l'id&eacute;e de retourner "
  "l&agrave;-bas, se souvenant tr&egrave;s clairement de la phrase "
  "murmur&eacute;e dans le vent lors de leur premi&egrave;re visite, mais "
  "la perspective de voir dispara&icirc;tre &agrave; jamais des preuves "
  "aussi pr&eacute;cieuses le pousse &agrave; accepter, &agrave; condition "
  "cette fois de pr&eacute;venir quelqu'un de confiance avant de "
  "partir.")

p("Ils choisissent de mettre Franck dans la confidence, "
  "enti&egrave;rement cette fois, racontant tout depuis le d&eacute;but "
  "&mdash; l'enveloppe kraft, Templier, Amboise, la carte au mur, "
  "la voix dans le vent &mdash; et Franck, loin de leur interdire "
  "quoi que ce soit, propose au contraire de les accompagner "
  "lui-m&ecirc;me, refusant cette fois de les laisser affronter "
  "seuls un h&eacute;ritage qui, apr&egrave;s tout, lui appartient "
  "autant qu'&agrave; son fils.")

name("FRANCK")
p("&laquo;&nbsp;Si Kayden &eacute;tait vraiment mon fr&egrave;re, alors cette "
  "histoire me concerne directement, pas juste toi. J'ai "
  "pass&eacute; ma vie &agrave; fuir tout &ccedil;a. C'est peut-&ecirc;tre le moment "
  "d'arr&ecirc;ter de fuir, pour de bon, et de venir avec "
  "vous.&nbsp;&raquo;")

p("Ils retournent tous les quatre &agrave; Amboise un samedi "
  "d'octobre, trouvant le b&acirc;timent d&eacute;j&agrave; partiellement "
  "vid&eacute; par une &eacute;quipe municipale, des cartons empil&eacute;s "
  "pr&ecirc;ts &agrave; &ecirc;tre &eacute;vacu&eacute;s, et parviennent, en profitant "
  "d'une pause des ouvriers, &agrave; r&eacute;cup&eacute;rer discr&egrave;tement le "
  "dossier des porteurs avant qu'il ne finisse, comme "
  "tant d'autres archives, dans une benne &agrave; d&eacute;chets.")

p("Franck, en feuilletant lui-m&ecirc;me le dossier, retrouve sa "
  "propre fiche, jamais consult&eacute;e depuis des d&eacute;cennies, et "
  "y d&eacute;couvre, avec un choc silencieux, une note tardive "
  "ajout&eacute;e apr&egrave;s son retrait du programme : &laquo;&nbsp;sujet "
  "retir&eacute; pr&eacute;matur&eacute;ment &mdash; potentiel de porteur non "
  "&eacute;valu&eacute; &mdash; &agrave; ressurveiller via descendance directe si "
  "possible.&nbsp;&raquo;")

name("FRANCK")
p("&laquo;&nbsp;Ils m'ont jamais vraiment l&acirc;ch&eacute;, alors. Ils "
  "attendaient juste de voir si &ccedil;a sauterait une "
  "g&eacute;n&eacute;ration, avant de retomber sur toi. &Ccedil;a me rend "
  "malade de penser que ta naissance a peut-&ecirc;tre &eacute;t&eacute;, "
  "d'une mani&egrave;re ou d'une autre, quelque chose qu'ils "
  "surveillaient depuis le d&eacute;but.&nbsp;&raquo;")

p("Ce constat, glacial, p&egrave;se sur tout le trajet du retour, "
  "chacun mesurant &agrave; sa mani&egrave;re &agrave; quel point cette "
  "histoire semble avoir toujours &eacute;t&eacute; plus vaste, plus "
  "patiente et plus d&eacute;lib&eacute;r&eacute;e que ce qu'ils avaient os&eacute; "
  "imaginer, m&ecirc;me apr&egrave;s tout ce qu'ils avaient d&eacute;j&agrave; "
  "d&eacute;couvert ensemble.")

p("Clara, une fois rentr&eacute;e chez elle, passe une partie "
  "de la nuit &agrave; photographier chaque page du dossier "
  "des porteurs r&eacute;cup&eacute;r&eacute; &agrave; Amboise, cr&eacute;ant m&eacute;thodiquement "
  "une archive num&eacute;rique de secours qu'elle stocke sur "
  "plusieurs supports diff&eacute;rents, consciente que ce "
  "document repr&eacute;sente d&eacute;sormais une preuve "
  "irrempla&ccedil;able de l'ampleur r&eacute;elle du r&eacute;seau qu'ils "
  "affrontent.")

name("CLARA")
p("&laquo;&nbsp;Si jamais il nous arrive quoi que ce soit, "
  "&agrave; l'un d'entre nous, faut que ces preuves survivent. "
  "J'ai envoy&eacute; des copies &agrave; trois adresses email "
  "diff&eacute;rentes, plus une cl&eacute; USB cach&eacute;e chez ma "
  "grand-m&egrave;re. On n'est jamais trop prudents avec ce "
  "genre de dossier.&nbsp;&raquo;")

p("Alex approuve cette pr&eacute;caution suppl&eacute;mentaire, "
  "proposant &agrave; son tour de conserver une copie "
  "physique imprim&eacute;e dans un endroit s&ucirc;r de sa propre "
  "chambre, redoutant, sans se l'avouer totalement, "
  "qu'un jour cette pr&eacute;caution puisse s'av&eacute;rer "
  "n&eacute;cessaire pour des raisons qu'aucun d'eux ne "
  "souhaite vraiment envisager.")

p("Darius, de son c&ocirc;t&eacute;, choisit une approche "
  "diff&eacute;rente pour traiter cette nouvelle inqui&eacute;tude, "
  "int&eacute;grant, dans son propre jeu, une repr&eacute;sentation "
  "symbolique de l'entrep&ocirc;t d'Amboise, avec ses "
  "&eacute;tag&egrave;res poussi&eacute;reuses et son bureau &agrave; l'ancien "
  "t&eacute;l&eacute;phone, esp&eacute;rant, en recr&eacute;ant num&eacute;riquement ce "
  "lieu inqui&eacute;tant, en apprivoiser un peu la menace "
  "latente.")

p("Il ajoute &eacute;galement, sans trop savoir pourquoi, un "
  "petit personnage secondaire inspir&eacute; directement de "
  "la voix entendue dans le vent ce jour-l&agrave; &mdash; une "
  "silhouette floue, jamais totalement visible, qui "
  "observe le joueur depuis les recoins sombres de "
  "chaque niveau sans jamais interagir directement, "
  "une pr&eacute;sence purement contemplative destin&eacute;e &agrave; "
  "rappeler, constamment, que cette histoire est "
  "observ&eacute;e par des forces bien plus vastes que celles "
  "qu'ils affrontent directement.")

name("CLARA")
p("&laquo;&nbsp;C'est troublant, ce personnage silencieux que "
  "t'as ajout&eacute;. &Ccedil;a me fait penser exactement &agrave; cette "
  "sensation qu'on a eue &agrave; Amboise, d'&ecirc;tre observ&eacute;s "
  "sans jamais voir par qui. T'as vraiment un talent "
  "pour transformer nos peurs en quelque chose de "
  "visuel et concret, Darius.&nbsp;&raquo;")

p("Ce compliment sinc&egrave;re touche profond&eacute;ment Darius, "
  "renfor&ccedil;ant chez lui la conviction que son projet "
  "cr&eacute;atif, loin d'&ecirc;tre une simple &eacute;chappatoire &eacute;go&iuml;ste, "
  "constitue peut-&ecirc;tre une v&eacute;ritable contribution &agrave; "
  "leur compr&eacute;hension collective de tout ce qu'ils "
  "traversent ensemble, une mani&egrave;re artistique de "
  "digérer l'indigeste plut&ocirc;t que de simplement le "
  "fuir.")

p("Franck, invit&eacute; &agrave; d&eacute;couvrir cette derni&egrave;re "
  "addition au jeu quelques jours plus tard, reste "
  "longuement immobile devant l'&eacute;cran, observant cette "
  "silhouette floue &eacute;voluer discr&egrave;tement dans les "
  "recoins du niveau consacr&eacute; &agrave; Amboise, avant de "
  "retirer le casque avec une expression grave que "
  "Darius ne lui conna&icirc;t pas encore.")

name("FRANCK")
p("&laquo;&nbsp;&Ccedil;a me fait froid dans le dos, cette "
  "silhouette. J'ai l'impression de revivre exactement "
  "ce que vous m'avez d&eacute;crit de cette voix entendue "
  "l&agrave;-bas. T'as un vrai don pour recr&eacute;er des "
  "atmosph&egrave;res, fiston, m&ecirc;me si &ccedil;a me terrifie un "
  "peu de le reconna&icirc;tre.&nbsp;&raquo;")

p("Il propose, apr&egrave;s r&eacute;flexion, d'organiser une "
  "sorte de r&eacute;union familiale &eacute;largie, invitant "
  "&eacute;galement la m&egrave;re de Darius &agrave; d&eacute;couvrir, si elle "
  "le souhaite, cette part cr&eacute;ative de la vie de son "
  "fils qu'elle ne conna&icirc;t encore que tr&egrave;s "
  "partiellement, esp&eacute;rant que cette d&eacute;monstration "
  "pourrait, &agrave; sa mani&egrave;re, contribuer &agrave; rapprocher "
  "davantage tous les membres de cette famille "
  "recompos&eacute;e.")

p("La m&egrave;re de Darius, initialement r&eacute;ticente &agrave; "
  "l'id&eacute;e d'enfiler elle-m&ecirc;me un casque de r&eacute;alit&eacute; "
  "virtuelle, finit par accepter, encourag&eacute;e par "
  "l'enthousiasme visible de son fils, et d&eacute;couvre, "
  "avec une &eacute;motion sinc&egrave;re, l'&eacute;tendue du talent "
  "cr&eacute;atif qu'il a d&eacute;velopp&eacute; ces derniers mois, sans "
  "jamais soup&ccedil;onner &agrave; quel point ce projet puisait "
  "dans une r&eacute;alit&eacute; bien plus vaste et &eacute;trange que la "
  "simple imagination adolescente.")

name("M&Egrave;RE DE DARIUS")
p("&laquo;&nbsp;C'est magnifique, ce que t'as cr&eacute;&eacute;, mon "
  "grand. J'avais aucune id&eacute;e que t'avais un tel "
  "talent artistique cach&eacute;. &Ccedil;a me donne presque "
  "envie de m'y mettre moi aussi, &agrave; ce genre de "
  "technologie.&nbsp;&raquo;")

p("Cette soir&eacute;e famille &eacute;largie, r&eacute;unissant pour la "
  "premi&egrave;re fois depuis des ann&eacute;es la m&egrave;re de "
  "Darius et Franck autour d'une m&ecirc;me table sans la "
  "tension habituelle des &eacute;changes post-divorce, "
  "repr&eacute;sente un moment charni&egrave;re dans la "
  "reconstruction de cette famille &eacute;clat&eacute;e, chacun des "
  "deux parents redécouvrant, &agrave; travers le prisme de "
  "ce projet cr&eacute;atif extraordinaire, &agrave; quel point leur "
  "fils avait grandi et m&ucirc;ri ces derniers mois.")

name("M&Egrave;RE DE DARIUS")
p("&laquo;&nbsp;Franck, je dois reconna&icirc;tre que tu sembles "
  "beaucoup plus pr&eacute;sent, ces derniers temps. &Ccedil;a fait "
  "plaisir &agrave; voir, pour Darius surtout. Il a vraiment "
  "besoin de nous deux, &agrave; cet &acirc;ge-l&agrave;.&nbsp;&raquo;")

p("Franck accueille ce compliment inattendu avec une "
  "humilit&eacute; sinc&egrave;re, reconnaissant volontiers ses "
  "erreurs pass&eacute;es sans jamais chercher &agrave; se "
  "justifier excessivement, et cette conversation "
  "adulte, men&eacute;e avec une maturit&eacute; nouvelle de part "
  "et d'autre, marque le d&eacute;but d'une coparentalit&eacute; "
  "plus harmonieuse qui b&eacute;n&eacute;ficiera consid&eacute;rablement "
  "&agrave; Darius dans les mois &agrave; venir.")

p("Alex, t&eacute;moin discret de cette r&eacute;conciliation "
  "parentale depuis le canap&eacute; du salon, &eacute;change un "
  "regard complice avec Clara, tous deux mesurant &agrave; "
  "quel point leur ami a d&eacute;sormais, gr&acirc;ce &agrave; tout ce "
  "qu'ils ont travers&eacute; ensemble, un foyer familial "
  "bien plus solide et uni que celui, fracturé, qu'il "
  "conna&icirc;ssait au d&eacute;but de cette aventure "
  "extraordinaire.")

name("CLARA")
p("&laquo;&nbsp;C'est fou de penser que tout &ccedil;a, cette "
  "histoire de Marge et de Non-lieu, a fini par "
  "rapprocher les parents de Darius plut&ocirc;t que de les "
  "&eacute;loigner encore plus. Y'a quelque chose de "
  "presque beau l&agrave;-dedans, tu trouves pas ?&nbsp;&raquo;")

p("Alex acquiesce silencieusement, pensant &agrave; sa "
  "propre famille, plus simple mais tout aussi "
  "précieuse, et &agrave; quel point cette aventure "
  "partag&eacute;e a &eacute;galement renforc&eacute; ses propres liens "
  "avec ses parents, d&eacute;sormais plus attentifs &agrave; ses "
  "&eacute;tats d'&acirc;me depuis qu'ils le sentent impliqu&eacute; dans "
  "quelque chose d'important, m&ecirc;me sans en conna&icirc;tre "
  "les d&eacute;tails exacts.")

p("Cette soir&eacute;e se termine tard, tous les cinq "
  "install&eacute;s autour de la table basse du salon &agrave; "
  "partager un dessert improvis&eacute;, et Darius, "
  "observant ce tableau chaleureux r&eacute;unissant "
  "ses deux parents et ses deux meilleurs amis, "
  "ressent une gratitude si intense qu'elle en "
  "devient presque douloureuse, mesurant &agrave; quel "
  "point cette simple soir&eacute;e ordinaire repr&eacute;sente, "
  "en r&eacute;alit&eacute;, un accomplissement extraordinaire "
  "apr&egrave;s tout ce qu'ils ont travers&eacute; ensemble.")

name("DARIUS")
p("&laquo;&nbsp;Je crois que c'est le meilleur soir depuis "
  "tr&egrave;s longtemps, tout compte fait. Merci &agrave; tous "
  "d'&ecirc;tre l&agrave;, sinc&egrave;rement. J'aurais jamais cru "
  "qu'on pourrait un jour se retrouver tous "
  "ensemble comme &ccedil;a, aussi simplement.&nbsp;&raquo;")

p("Ce moment de gr&acirc;ce partag&eacute;e, savour&eacute; "
  "pleinement par chacun des convives sans "
  "arri&egrave;re-pens&eacute;e ni myst&egrave;re non r&eacute;solu &agrave; "
  "l'horizon, restera grav&eacute; longtemps dans la "
  "m&eacute;moire de Darius comme l'une des soir&eacute;es les "
  "plus pr&eacute;cieuses de toute son existence, un &icirc;lot "
  "de paix parfaite au c&oelig;ur d'une ann&eacute;e par ailleurs "
  "si tumultueuse.")

p("Avant de partir, Clara et Alex aident &agrave; "
  "d&eacute;barrasser la table, une habitude naturelle "
  "d&eacute;velopp&eacute;e au fil de leurs innombrables visites "
  "chez Darius, et la m&egrave;re de ce dernier, les "
  "observant s'affairer avec cette aisance famili&egrave;re "
  "dans sa propre cuisine, ressent une bouff&eacute;e "
  "d'affection sinc&egrave;re pour ces deux jeunes gens "
  "devenus, au fil des ann&eacute;es, presque des membres "
  "&agrave; part enti&egrave;re de sa propre famille.")

name("M&Egrave;RE DE DARIUS")
p("&laquo;&nbsp;Vous savez que vous &ecirc;tes toujours les "
  "bienvenus ici, tous les deux, m&ecirc;me sans Darius. "
  "Vous faites partie de cette maison, maintenant, "
  "autant que lui.&nbsp;&raquo;")

p("Cette d&eacute;claration chaleureuse, prononc&eacute;e avec une "
  "sinc&eacute;rit&eacute; touchante, restera elle aussi grav&eacute;e "
  "dans la m&eacute;moire de Clara et Alex, prenant, avec "
  "le recul tragique des &eacute;v&eacute;nements &agrave; venir, une "
  "signification bien plus pr&eacute;cieuse encore qu'aucun "
  "d'entre eux n'aurait pu imaginer ce soir-l&agrave;.")

p("Ils rentrent chacun chez eux, cette nuit-l&agrave;, "
  "le c&oelig;ur l&eacute;ger malgr&eacute; le froid mordant de f&eacute;vrier, "
  "et Alex, marchant seul les derni&egrave;res centaines de "
  "m&egrave;tres jusqu'&agrave; son propre domicile, repense &agrave; "
  "quel point cette famille recompos&eacute;e, imparfaite "
  "mais profond&eacute;ment aimante, ressemble finalement "
  "assez peu &agrave; l'image qu'il s'en &eacute;tait faite &agrave; "
  "l'&eacute;poque du divorce de Franck et de la m&egrave;re de "
  "Darius, quelques ann&eacute;es plus t&ocirc;t.")

p("Il se souvient encore de Darius, tout petit "
  "gar&ccedil;on triste apr&egrave;s la s&eacute;paration de ses "
  "parents, et mesure, avec une fiert&eacute; presque "
  "fraternelle, le chemin parcouru par son ami "
  "depuis cette &eacute;poque douloureuse jusqu'&agrave; cette "
  "soir&eacute;e harmonieuse qu'ils viennent de partager "
  "tous ensemble.")

p("Il rentre chez lui, ce soir-l&agrave;, avec la "
  "certitude renouvel&eacute;e que quoi qu'il puisse encore "
  "leur arriver dans cette aventure extraordinaire, "
  "cette petite communaut&eacute; familiale recompos&eacute;e "
  "saura toujours trouver la force n&eacute;cessaire pour "
  "traverser ensemble n'importe quelle &eacute;preuve, "
  "aussi terrifiante soit-elle.")

p("Clara, de son c&ocirc;t&eacute;, rentre &eacute;galement chez elle "
  "avec un sentiment de chaleur et de plénitude "
  "rarement &eacute;prouv&eacute; avec une telle intensit&eacute;, "
  "consid&eacute;rant la famille de Darius, dans toute sa "
  "complexit&eacute; recompos&eacute;e, comme un exemple "
  "vivant que l'amour et la loyaut&eacute; peuvent "
  "toujours triompher des &eacute;preuves les plus "
  "difficiles, pour peu que chacun accepte de "
  "faire sa part d'efforts sinc&egrave;res.")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 7 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 8 -- LE COMPTE &Agrave; REBOURS
# ======================================================================
chap(8, "LE COMPTE &Agrave; REBOURS")

p("L'hiver s'installe durablement sur Luynes dans les "
  "semaines qui suivent leur retour d'Amboise, "
  "recouvrant la vall&eacute;e d'un givre matinal persistant "
  "qui transforme les vignes en dentelle blanche et "
  "ralentit consid&eacute;rablement le rythme habituel du "
  "village, cette torpeur saisonni&egrave;re contrastant "
  "&eacute;trangement avec l'agitation int&eacute;rieure que Darius "
  "et ses amis continuent de ressentir depuis leur "
  "d&eacute;couverte troublante du registre d'appels.")

p("Les vacances de No&euml;l, arrivant &agrave; point nomm&eacute; "
  "au c&oelig;ur de cette p&eacute;riode tendue, offrent &agrave; "
  "Darius et ses proches une tr&ecirc;ve bienvenue, "
  "l'ambiance festive de Luynes, illumin&eacute;e de "
  "guirlandes color&eacute;es sur la place du march&eacute;, "
  "contrastant agr&eacute;ablement avec la gravit&eacute; des "
  "&eacute;v&eacute;nements r&eacute;cents, et permettant &agrave; chacun de "
  "souffler un peu avant les &eacute;preuves &agrave; venir.")

name("DARIUS")
p("&laquo;&nbsp;&Ccedil;a fait du bien, ce moment de calme. "
  "J'avais presque oubli&eacute; ce que &ccedil;a faisait de "
  "juste profiter des f&ecirc;tes sans avoir peur de "
  "quoi que ce soit derri&egrave;re chaque coin de rue.&nbsp;&raquo;")

p("Franck, de son c&ocirc;t&eacute;, redouble de vigilance apr&egrave;s "
  "avoir appris la teneur exacte de leur exp&eacute;dition &agrave; "
  "Amboise, insistant pour que Darius l'informe "
  "d&eacute;sormais de chaque nouvelle d&eacute;couverte avant m&ecirc;me "
  "d'en parler &agrave; Clara et Alex, une demande que Darius "
  "accepte sans r&eacute;sistance, appr&eacute;ciant sinc&egrave;rement "
  "cette implication paternelle nouvelle qui contraste "
  "si radicalement avec les ann&eacute;es de silence "
  "pr&eacute;c&eacute;dentes.")

name("FRANCK")
p("&laquo;&nbsp;Je veux pas te couver, Darius, t'as prouv&eacute; "
  "cent fois que t'&eacute;tais capable de g&eacute;rer des trucs "
  "&eacute;normes tout seul. Mais j'ai envie d'&ecirc;tre pr&eacute;sent, "
  "cette fois, pas juste inform&eacute; apr&egrave;s coup. &Ccedil;a "
  "changerait quoi pour toi, si je venais avec vous "
  "aux prochaines &eacute;tapes ?&nbsp;&raquo;")

p("Darius accueille cette proposition avec une "
  "&eacute;motion sinc&egrave;re, mesurant &agrave; quel point son p&egrave;re "
  "a chang&eacute; depuis le d&eacute;but de cette histoire, cet "
  "homme autrefois incapable de dire la simple v&eacute;rit&eacute; "
  "sur un chien parti devenant, progressivement, un "
  "partenaire actif et courageux dans une histoire "
  "bien plus dangereuse que n'importe quel mensonge "
  "d'enfance.")

p("Il annonce cette nouvelle &agrave; Clara et Alex d&egrave;s le "
  "lendemain, &agrave; la cantine, s'attendant &agrave; une "
  "r&eacute;action mitig&eacute;e de leur part, mais d&eacute;couvrant "
  "au contraire un soulagement sinc&egrave;re chez ses deux "
  "amis, tous deux ayant, eux aussi, ressenti le "
  "poids grandissant de porter seuls, entre "
  "adolescents, une menace dont l'ampleur d&eacute;passe "
  "chaque semaine un peu plus leurs propres "
  "capacit&eacute;s.")

name("CLARA")
p("&laquo;&nbsp;Franchement, tant mieux. On n'est pas des "
  "super-h&eacute;ros, Darius, m&ecirc;me si on essaie de faire "
  "comme si. Avoir un adulte impliqu&eacute; directement, "
  "&ccedil;a peut vraiment changer la donne, surtout si &ccedil;a "
  "continue &agrave; s'aggraver comme &ccedil;a en a l'air.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;Ton p&egrave;re a quand m&ecirc;me un peu grandi dans "
  "cette histoire, je trouve. Il &eacute;tait genre inexistant "
  "au d&eacute;but, et maintenant il propose de nous "
  "accompagner directement. &Ccedil;a doit pas &ecirc;tre facile "
  "pour lui non plus, tu sais, d'assumer &ccedil;a apr&egrave;s "
  "toutes ces ann&eacute;es d'&eacute;vitement.&nbsp;&raquo;")

p("Cette validation collective de la d&eacute;cision de "
  "Franck renforce chez Darius la conviction qu'ils "
  "avancent d&eacute;sormais, tous les quatre, vers cette "
  "&eacute;ch&eacute;ance redout&eacute;e du seize f&eacute;vrier avec une force "
  "collective jamais atteinte auparavant, une "
  "coh&eacute;sion familiale et amicale qui, quoi qu'il "
  "advienne, repr&eacute;sente d&eacute;j&agrave; en soi une victoire "
  "consid&eacute;rable sur l'isolement qui avait "
  "caract&eacute;ris&eacute; les premiers mois de cette aventure.")

p("Darius ne parvient pas &agrave; se sortir de la t&ecirc;te ce num&eacute;ro "
  "de t&eacute;l&eacute;phone rep&eacute;r&eacute; dans le registre d'appels "
  "d'Amboise, celui marqu&eacute; &laquo;&nbsp;contact de suivi &mdash; ne pas "
  "archiver&nbsp;&raquo;, et finit, un soir, contre l'avis prudent de "
  "Franck, par composer les chiffres sur son propre "
  "t&eacute;l&eacute;phone, le c&oelig;ur battant, pr&ecirc;t &agrave; raccrocher au "
  "moindre signe suspect.")

p("La ligne sonne trois fois avant qu'une voix d'homme, "
  "neutre et professionnelle, ne d&eacute;croche, sans jamais "
  "prononcer le moindre nom d'organisme ni de personne, "
  "se contentant d'un sobre &laquo;&nbsp;j'&eacute;coute&nbsp;&raquo; qui glace "
  "instantan&eacute;ment Darius sur place.")

name("VOIX INCONNUE")
p("&laquo;&nbsp;Vous appelez un num&eacute;ro qui n'existe pas, jeune "
  "homme. Je vous conseille de ne pas rappeler. Ce n'est "
  "pas une menace. C'est un conseil, pour votre propre "
  "s&eacute;curit&eacute;.&nbsp;&raquo;")

p("La communication se coupe avant que Darius n'ait pu "
  "prononcer un seul mot suppl&eacute;mentaire, et il reste "
  "longtemps immobile, le t&eacute;l&eacute;phone encore &agrave; la main, "
  "incapable de d&eacute;cider si cette voix appartient &agrave; un "
  "simple gardien administratif d&eacute;pass&eacute; par les "
  "&eacute;v&eacute;nements, ou &agrave; quelque chose de bien plus "
  "organis&eacute; et bien plus dangereux.")

p("Il raconte l'appel &agrave; Clara et Alex d&egrave;s le lendemain, "
  "fid&egrave;le &agrave; sa promesse de ne plus rien leur cacher, et "
  "tous trois passent la soir&eacute;e &agrave; tenter, sans succ&egrave;s, "
  "de retracer l'origine du num&eacute;ro &agrave; l'aide de sites en "
  "ligne sp&eacute;cialis&eacute;s, ne trouvant qu'un indicatif r&eacute;gional "
  "vague, incapable de les mener plus loin.")

name("ALEX")
p("&laquo;&nbsp;'Ce n'est pas une menace, c'est un conseil.' &Ccedil;a "
  "sonne exactement comme un truc que dirait quelqu'un "
  "qui te menace tout en esp&eacute;rant que tu remarques pas "
  "que c'en est une. J'aime pas &ccedil;a du tout, Darius.&nbsp;&raquo;")

p("Clara, plus pragmatique face &agrave; cette inqui&eacute;tude "
  "grandissante, propose de consigner imm&eacute;diatement "
  "cet appel dans son carnet, ainsi que toutes les "
  "circonstances exactes qui l'ont entour&eacute;, esp&eacute;rant "
  "que cette documentation rigoureuse pourrait, un "
  "jour, s'av&eacute;rer utile pour comprendre le "
  "fonctionnement exact de cette organisation "
  "myst&eacute;rieuse qui semble les observer depuis "
  "l'ombre.")

name("CLARA")
p("&laquo;&nbsp;On devrait aussi pr&eacute;venir Franck tout de "
  "suite, pas attendre demain. Si vraiment on vient "
  "de d&eacute;clencher une alerte chez eux, je pr&eacute;f&egrave;re "
  "qu'un adulte soit au courant le plus vite possible, "
  "au cas o&ugrave;.&nbsp;&raquo;")

p("Darius appelle effectivement son p&egrave;re ce m&ecirc;me "
  "soir, malgr&eacute; l'heure tardive, et Franck, loin de "
  "minimiser la situation, propose imm&eacute;diatement de "
  "venir passer la nuit chez son ex-femme sur le "
  "canap&eacute; du salon, une pr&eacute;caution suppl&eacute;mentaire "
  "que Darius accepte avec un soulagement sinc&egrave;re, "
  "appr&eacute;ciant cette protection paternelle nouvelle "
  "qu'il n'aurait jamais imagin&eacute;e possible quelques "
  "mois plus t&ocirc;t.")

name("FRANCK")
p("&laquo;&nbsp;J'arrive tout de suite, fiston. On va pas "
  "prendre de risque avec &ccedil;a. Je pr&eacute;f&egrave;re &ecirc;tre l&agrave; au "
  "cas o&ugrave;, m&ecirc;me si c'est probablement rien de grave "
  "en fin de compte.&nbsp;&raquo;")

p("Cette nuit-l&agrave;, le carnet de Clara se remplit d'elle-m&ecirc;me "
  "pour la premi&egrave;re fois depuis des mois, une seule ligne, "
  "diff&eacute;rente cette fois de l'&eacute;criture habituelle du "
  "fragment de Kayden, plus formelle, presque officielle "
  "dans sa froideur : &laquo;&nbsp;dossier r&eacute;activ&eacute; &mdash; porteur "
  "identifi&eacute; &mdash; surveillance renforc&eacute;e autoris&eacute;e.&nbsp;&raquo;")

p("Ils comprennent, cette fois avec une certitude glac&eacute;e, "
  "que leur appel t&eacute;l&eacute;phonique, loin de rester sans "
  "cons&eacute;quence, vient tr&egrave;s probablement de d&eacute;clencher "
  "quelque chose &mdash; une attention officielle, renouvel&eacute;e, "
  "port&eacute;e directement sur Darius, dont ni lui ni ses amis "
  "ne peuvent encore mesurer l'&eacute;tendue r&eacute;elle.")

p("Les jours suivants apportent leur lot de d&eacute;tails "
  "inqui&eacute;tants, trop discrets pour &ecirc;tre prouv&eacute;s, trop "
  "nombreux pour &ecirc;tre ni&eacute;s &mdash; une voiture grise gar&eacute;e "
  "plus longtemps que n&eacute;cessaire devant le coll&egrave;ge, un "
  "homme en costume crois&eacute; deux fois en une semaine "
  "pr&egrave;s de la place de Luynes sans jamais sembler avoir de "
  "destination pr&eacute;cise, un clic &eacute;trange entendu sur la ligne "
  "t&eacute;l&eacute;phonique familiale.")

p("Darius consigne chacun de ces d&eacute;tails avec une "
  "rigueur presque obsessionnelle, reprenant, sans se "
  "l'avouer enti&egrave;rement, les m&ecirc;mes m&eacute;thodes que "
  "Templier avait employ&eacute;es toute sa vie pour tenter de "
  "comprendre une menace qui refuse obstin&eacute;ment de se "
  "montrer clairement.")

name("CLARA")
p("&laquo;&nbsp;On devrait peut-&ecirc;tre pr&eacute;venir la police, non ? Ou "
  "au moins en parler &agrave; quelqu'un d'officiel. &Ccedil;a "
  "commence &agrave; ressembler &agrave; du harc&egrave;lement, m&ecirc;me si "
  "c'est subtil.&nbsp;&raquo;")

p("Franck, consult&eacute;, d&eacute;conseille fermement cette id&eacute;e, "
  "expliquant qu'une organisation capable de maintenir un "
  "r&eacute;seau secret depuis des d&eacute;cennies dispose "
  "probablement de ramifications suffisantes pour "
  "&eacute;touffer, ou pire, r&eacute;cup&eacute;rer &agrave; son propre avantage, la "
  "moindre plainte officielle d&eacute;pos&eacute;e contre elle.")

name("FRANCK")
p("&laquo;&nbsp;On n'a aucune id&eacute;e de qui &ccedil;a implique vraiment. &Ccedil;a "
  "peut &ecirc;tre des gens haut plac&eacute;s, des anciens du "
  "minist&egrave;re, n'importe qui. Je pr&eacute;f&egrave;re qu'on reste "
  "discrets et prudents plut&ocirc;t que de risquer d'attirer "
  "encore plus l'attention en officialisant tout &ccedil;a "
  "publiquement.&nbsp;&raquo;")

p("Ils d&eacute;cident, d'un commun accord, de redoubler de "
  "prudence sans pour autant paniquer, maintenant leurs "
  "habitudes quotidiennes autant que possible tout en "
  "restant vigilants, et Darius, malgr&eacute; l'inqui&eacute;tude "
  "ambiante, continue &agrave; travailler sur son jeu, cherchant "
  "dans cette activit&eacute; un refuge encore plus pr&eacute;cieux qu'avant "
  "face &agrave; une menace ext&eacute;rieure qui, elle, refuse "
  "obstin&eacute;ment de se laisser ma&icirc;triser.")

p("Un soir de novembre, alors qu'il peaufine, casque sur "
  "les yeux, un nouveau niveau situ&eacute; derri&egrave;re la fameuse "
  "porte close, une notification appara&icirc;t soudain dans "
  "l'interface du jeu, l&agrave; o&ugrave; il n'a jamais programm&eacute; "
  "aucun syst&egrave;me de notification : &laquo;&nbsp;7 lumi&egrave;res "
  "d&eacute;tect&eacute;es. 6 &eacute;teintes. 1 allum&eacute;e. Compte &agrave; rebours "
  "activ&eacute;.&nbsp;&raquo;")

p("Il retire imm&eacute;diatement le casque, glac&eacute;, incapable de "
  "d&eacute;terminer si cette apparition provient d'un simple bug "
  "logiciel ou d'une intrusion bien plus inqui&eacute;tante dans "
  "son propre syst&egrave;me, mais choisit, cette fois, de ne pas "
  "&eacute;teindre son ordinateur, esp&eacute;rant, contre toute prudence, "
  "en apprendre davantage sur ce compte &agrave; rebours "
  "myst&eacute;rieux plut&ocirc;t que de fuir une information qui le "
  "concerne visiblement au premier chef.")

p("Le compte &agrave; rebours, une fois affich&eacute; en permanence "
  "dans un coin discret de l'interface de son jeu, indique "
  "une dur&eacute;e pr&eacute;cise, exprim&eacute;e en jours plut&ocirc;t qu'en "
  "heures &mdash; cent quatre jours exactement, ce nombre "
  "r&eacute;sonnant imm&eacute;diatement, pour Darius, avec une "
  "signification qu'aucun hasard ne saurait expliquer.")

name("CLARA")
p("&laquo;&nbsp;Cent quatre jours. &Ccedil;a fait pile le seize f&eacute;vrier, si "
  "je compte bien &agrave; partir d'aujourd'hui. &Ccedil;a te dit "
  "quelque chose, cette date ? Un anniversaire, un truc "
  "li&eacute; &agrave; Kayden, &agrave; Vasseur ?&nbsp;&raquo;")

p("Aucun d'eux ne parvient &agrave; rattacher cette date &agrave; un "
  "&eacute;v&eacute;nement connu de leur histoire commune, ce qui "
  "n'apaise en rien l'angoisse grandissante que ce compte "
  "&agrave; rebours instille peu &agrave; peu dans leur quotidien, comme "
  "une horloge invisible d&eacute;sormais suspendue au-dessus de "
  "leurs t&ecirc;tes.")

p("Darius essaie, &agrave; plusieurs reprises, de supprimer "
  "manuellement ce compte &agrave; rebours de son propre code, "
  "sans jamais y parvenir &mdash; le chiffre r&eacute;appara&icirc;t "
  "syst&eacute;matiquement, identique, &agrave; la relance suivante du "
  "logiciel, comme si une main invisible corrigeait "
  "patiemment chacune de ses tentatives de suppression.")

name("DARIUS")
p("&laquo;&nbsp;J'ai l'impression que c'est pas vraiment mon jeu "
  "qui affiche &ccedil;a. On dirait plut&ocirc;t que quelque chose "
  "utilise mon jeu comme un &eacute;cran, un endroit pratique "
  "pour m'envoyer un message que je suis certain de voir "
  "chaque soir.&nbsp;&raquo;")

p("Alex propose, avec une logique pragmatique qui le "
  "caract&eacute;rise, de simplement cesser d'utiliser le casque "
  "jusqu'&agrave; ce que le compte &agrave; rebours atteigne z&eacute;ro, "
  "esp&eacute;rant qu'en ignorant purement et simplement le "
  "signal, quoi qu'il annonce, ils pourraient &eacute;viter d'en "
  "subir les cons&eacute;quences.")

name("ALEX")
p("&laquo;&nbsp;Franchement, Darius, j&egrave;te ce truc, ou au moins "
  "range-le au fond d'un placard jusqu'&agrave; ce que &ccedil;a passe. "
  "Je sais que &ccedil;a compte &eacute;norm&eacute;ment pour toi, mais l&agrave; "
  "&ccedil;a commence &agrave; ressembler &agrave; un compte &agrave; rebours "
  "avant un truc vraiment pas net.&nbsp;&raquo;")

p("Darius promet d'y r&eacute;fl&eacute;chir, sinc&egrave;rement tent&eacute; encore "
  "une fois par cette id&eacute;e raisonnable, mais une force "
  "int&eacute;rieure, difficile &agrave; nommer, continue de le pousser "
  "&agrave; vouloir comprendre plut&ocirc;t que fuir, &agrave; affronter "
  "plut&ocirc;t qu'&eacute;viter, fid&egrave;le en cela &agrave; tout ce que son "
  "r&ocirc;le de porteur lui a toujours demand&eacute; depuis la "
  "vitrine sous la pluie.")

p("Clara, de son c&ocirc;t&eacute;, entreprend ses propres recherches "
  "en parall&egrave;le, retournant &agrave; la biblioth&egrave;que municipale "
  "pour &eacute;plucher, une fois de plus, les archives locales "
  "&agrave; la recherche de tout &eacute;v&eacute;nement marquant s'&eacute;tant "
  "produit un seize f&eacute;vrier, dans n'importe quelle ann&eacute;e "
  "pass&eacute;e, esp&eacute;rant y trouver un pr&eacute;c&eacute;dent capable "
  "d'&eacute;clairer ce qui les attend.")

name("MME FERRAND")
p("&laquo;&nbsp;Un seize f&eacute;vrier, dites-vous ? Attendez, &ccedil;a me "
  "rappelle vaguement quelque chose. Il me semble "
  "qu'il y a eu un incendie, une ann&eacute;e, dans l'ancien "
  "presbyt&egrave;re, avant qu'il devienne biblioth&egrave;que. "
  "Personne n'a jamais vraiment su l'expliquer. Je vais "
  "vous chercher les coupures de presse, si vous "
  "voulez.&nbsp;&raquo;")

p("L'incendie en question, dat&eacute; d'un seize f&eacute;vrier "
  "1954, avait ravag&eacute; une partie de l'aile est du "
  "b&acirc;timent sans jamais trouver d'explication "
  "satisfaisante, les pompiers de l'&eacute;poque notant, dans "
  "leur rapport officiel conserv&eacute; par miracle, une "
  "&eacute;trange absence de source de combustion identifiable, "
  "comme si le feu avait simplement jailli du n&eacute;ant.")

name("CLARA")
p("&laquo;&nbsp;1954. &Ccedil;a fait pile soixante-dix ans avant cette "
  "ann&eacute;e. Et si &ccedil;a se trouve, y'a eu d'autres incidents "
  "&agrave; cette m&ecirc;me date, &agrave; intervalles r&eacute;guliers, sans "
  "qu'on ait jamais fait le lien. Je vais chercher "
  "encore, y'a peut-&ecirc;tre un cycle qu'on n'a pas encore "
  "identifi&eacute;.&nbsp;&raquo;")

p("Elle finit par retrouver, apr&egrave;s des heures de "
  "recherche fastidieuse, deux autres mentions "
  "troublantes &mdash; un &eacute;boulement inexpliqu&eacute; sur le coteau "
  "en 1938, et une disparition jamais &eacute;lucid&eacute;e "
  "signal&eacute;e par la gendarmerie locale en 1901, toutes "
  "deux survenues, &agrave; chaque fois, un seize f&eacute;vrier "
  "pr&eacute;cis, comme si cette date portait, ind&eacute;pendamment "
  "de toute volont&eacute; humaine, une charge particuli&egrave;re "
  "dans le calendrier de la Marge.")

name("ALEX")
p("&laquo;&nbsp;Donc c'est pas juste li&eacute; &agrave; Vasseur et &agrave; son "
  "anniversaire. &Ccedil;a remonte bien plus loin que &ccedil;a. Cette "
  "date-l&agrave; compte pour un truc plus ancien encore, un "
  "truc que m&ecirc;me le docteur Vasseur devait probablement "
  "pas comprendre enti&egrave;rement.&nbsp;&raquo;")

p("Cette d&eacute;couverte, loin de rassurer qui que ce soit, "
  "renforce chez Darius la certitude glaciale que le "
  "compte &agrave; rebours affich&eacute; dans son propre jeu ne "
  "fait que r&eacute;v&eacute;ler, sous une forme moderne et "
  "num&eacute;ris&eacute;e, un rythme bien plus ancien que la Marge "
  "impose &agrave; cette vall&eacute;e depuis des g&eacute;n&eacute;rations, "
  "ind&eacute;pendamment de quiconque cherche &agrave; la "
  "comprendre ou &agrave; la contr&ocirc;ler.")

p("Il continue donc, malgr&eacute; les mises en garde r&eacute;p&eacute;t&eacute;es de "
  "ses amis, &agrave; enfiler son casque chaque soir, observant le "
  "compte &agrave; rebours d&eacute;grener patiemment ses jours "
  "restants, avec la certitude grandissante, jamais tout &agrave; "
  "fait formul&eacute;e &agrave; voix haute, que le seize f&eacute;vrier "
  "prochain marquera, d'une mani&egrave;re ou d'une autre, un "
  "tournant d&eacute;cisif dans une histoire commenc&eacute;e bien "
  "avant sa propre naissance.")

p("D&eacute;cembre passe dans une tension contenue, les f&ecirc;tes de "
  "fin d'ann&eacute;e offrant une tr&ecirc;ve bienvenue &mdash; un r&eacute;veillon "
  "partag&eacute; pour la premi&egrave;re fois depuis des ann&eacute;es entre "
  "la maison de sa m&egrave;re et celle de Franck, r&eacute;concili&eacute;s "
  "eux aussi &agrave; leur mani&egrave;re depuis que Darius leur a "
  "expliqu&eacute;, prudemment, l'ampleur de ce qu'il traverse.")

p("Le compte &agrave; rebours, lui, continue imperturbablement "
  "de d&eacute;grener ses jours, quatre-vingts d&eacute;sormais, "
  "toujours affich&eacute; dans ce coin discret de l'interface que "
  "Darius a fini par accepter comme une composante "
  "d&eacute;sormais permanente de son propre jeu, presque un "
  "personnage suppl&eacute;mentaire &agrave; part enti&egrave;re.")

p("Clara consacre de plus en plus de temps &agrave; son propre "
  "carnet de recherches, tentant de rattacher cette date du "
  "seize f&eacute;vrier &agrave; un &eacute;v&eacute;nement pass&eacute; li&eacute; au programme "
  "Vasseur, sans succ&egrave;s, jusqu'&agrave; ce qu'un d&eacute;tail, "
  "n&eacute;glig&eacute; jusque-l&agrave;, ne lui saute enfin aux yeux en "
  "relisant une nouvelle fois les archives d'Amboise.")

name("CLARA")
p("&laquo;&nbsp;Regarde &ccedil;a. Le docteur Vasseur est n&eacute; le seize "
  "f&eacute;vrier 1938. C'est son anniversaire, Darius. &Ccedil;a peut "
  "pas &ecirc;tre un hasard que ce compte &agrave; rebours tombe pile "
  "ce jour-l&agrave;.&nbsp;&raquo;")

p("Cette d&eacute;couverte, loin de rassurer qui que ce soit, ajoute "
  "une couche suppl&eacute;mentaire d'inqui&eacute;tude &agrave; leur situation "
  "&mdash; l'id&eacute;e qu'une organisation, quelle qu'elle soit, "
  "aurait choisi de faire co&iuml;ncider un &eacute;v&eacute;nement majeur les "
  "concernant directement avec la date de naissance d'un "
  "homme mort depuis des d&eacute;cennies, comme un hommage "
  "morbide ou une c&eacute;l&eacute;bration secr&egrave;te qu'ils ne "
  "comprennent pas encore enti&egrave;rement.")

p("Franck, quand on lui rapporte cette information, p&acirc;lit "
  "visiblement, r&eacute;v&eacute;lant, pour la premi&egrave;re fois, un souvenir "
  "d'enfance qu'il n'avait encore jamais partag&eacute; &mdash; celui "
  "d'une c&eacute;r&eacute;monie annuelle, obscure, organis&eacute;e chaque "
  "seize f&eacute;vrier dans les locaux du programme, &agrave; laquelle "
  "seuls les patients les plus &laquo;&nbsp;avanc&eacute;s&nbsp;&raquo; &eacute;taient conviés.")

name("FRANCK")
p("&laquo;&nbsp;Kayden y participait, chaque ann&eacute;e. Moi jamais, "
  "j'&eacute;tais trop jeune, ou pas assez avanc&eacute;, je sais pas "
  "trop. Mais je me souviens de son excitation avant "
  "chaque c&eacute;r&eacute;monie, comme si c'&eacute;tait le jour le plus "
  "important de toute son ann&eacute;e.&nbsp;&raquo;")

p("Cette r&eacute;v&eacute;lation nourrit chez Darius une angoisse "
  "nouvelle, teint&eacute;e d'une tristesse in&eacute;dite pour Kayden, "
  "imaginant ce petit gar&ccedil;on avide de reconnaissance "
  "comptant les jours, chaque ann&eacute;e, jusqu'&agrave; cette unique "
  "c&eacute;r&eacute;monie o&ugrave; il se sentait enfin, l'espace d'une "
  "journ&eacute;e, exister pleinement aux yeux de ceux qui "
  "l'entouraient.")

p("Le carnet de Clara se remplit &agrave; nouveau, une nuit de "
  "janvier, d'une &eacute;criture que tous trois reconnaissent "
  "d&eacute;sormais sans h&eacute;siter, plus longue cette fois que les "
  "pr&eacute;c&eacute;dentes, presque un t&eacute;moignage complet livr&eacute; "
  "d'une traite par le fragment de Kayden.")

p("&laquo;&nbsp;La c&eacute;r&eacute;monie n'&eacute;tait pas ce que vous croyez. On ne "
  "f&ecirc;tait pas mon p&egrave;re. On mesurait, une fois par an, "
  "combien d'ann&eacute;es le programme avait r&eacute;cup&eacute;r&eacute;es aupr&egrave;s "
  "des patients, et on les offrait, symboliquement, &agrave; une "
  "chose que mon p&egrave;re appelait 'la source', esp&eacute;rant "
  "gagner sa confiance, son aide, sa collaboration. J'ai "
  "cru longtemps que c'&eacute;tait un honneur d'y assister. "
  "C'&eacute;tait un sacrifice, et j'en faisais partie sans le "
  "savoir.&nbsp;&raquo;")

name("DARIUS")
p("&laquo;&nbsp;Kayden, si tu m'entends encore &mdash; est-ce que le "
  "seize f&eacute;vrier, cette ann&eacute;e, quelqu'un pr&eacute;pare encore "
  "une c&eacute;r&eacute;monie comme &ccedil;a ? Est-ce que c'est &ccedil;a que le "
  "compte &agrave; rebours annonce ?&nbsp;&raquo;")

p("La r&eacute;ponse met plusieurs jours &agrave; venir, br&egrave;ve et "
  "terriblement ambigu&euml; quand elle appara&icirc;t enfin : &laquo;&nbsp;je "
  "crois que oui. Je crois aussi que cette fois, ce ne sera "
  "pas symbolique. Fais attention &agrave; toi, Darius. Vraiment. "
  "Malgr&eacute; tout ce qui s'est pass&eacute; entre nous, je "
  "prefererais que &ccedil;a t'&eacute;pargne.&nbsp;&raquo;")

p("Cette derni&egrave;re phrase, empreinte d'une tendresse "
  "inattendue venant d'une entit&eacute; qu'ils ont pourtant "
  "combattue de toutes leurs forces quelques mois plus t&ocirc;t, "
  "trouble profond&eacute;ment Darius, lui rappelant que Kayden "
  "n'a jamais &eacute;t&eacute; un simple monstre, mais un gar&ccedil;on "
  "bless&eacute;, transform&eacute; par ce que d'autres lui avaient "
  "impos&eacute;, capable encore, malgr&eacute; sa dissolution "
  "incompl&egrave;te, d'&eacute;prouver quelque chose ressemblant &agrave; de "
  "l'affection pour lui.")

p("Ils passent les semaines suivantes &agrave; se pr&eacute;parer "
  "activement, sans savoir exactement &agrave; quoi ils se "
  "pr&eacute;parent &mdash; renfor&ccedil;ant leur pacte de rester toujours "
  "ensemble, ne plus jamais se s&eacute;parer un seize f&eacute;vrier "
  "sans un plan clair, et Darius, en particulier, refusant "
  "cette fois de porter davantage la charge seul, "
  "partageant chaque d&eacute;tail, chaque intuition, avec Clara, "
  "Alex et Franck.")

p("Le compte &agrave; rebours passe sous la barre des trente "
  "jours d&eacute;but f&eacute;vrier, et Darius, contre toute attente, "
  "ressent une forme &eacute;trange de calme s'installer en lui, "
  "comme si le fait de conna&icirc;tre enfin une &eacute;ch&eacute;ance "
  "pr&eacute;cise, m&ecirc;me menaçante, valait mieux que l'incertitude "
  "diffuse ayant caract&eacute;ris&eacute; les mois pr&eacute;c&eacute;dents.")

p("Il termine, durant ces semaines, la construction de son "
  "jeu presque enti&egrave;rement, ajoutant un dernier niveau, "
  "le plus abouti de tous, situ&eacute; enti&egrave;rement derri&egrave;re la "
  "fameuse porte close &mdash; un espace qu'il a con&ccedil;u, sans se "
  "l'avouer clairement, comme une sorte de sanctuaire "
  "d&eacute;di&eacute; &agrave; tous ceux que cette histoire a touch&eacute;s : "
  "Templier, Kayden enfant, Miel, m&ecirc;me la grand-m&egrave;re "
  "inconnue de Franck.")

name("CLARA")
p("&laquo;&nbsp;C'est magnifique, ce que t'as construit l&agrave;-dedans. "
  "&Ccedil;a ressemble presque &agrave; un m&eacute;morial plus qu'&agrave; un "
  "jeu, tu trouves pas ? Comme si tu rendais hommage &agrave; "
  "tout le monde en m&ecirc;me temps.&nbsp;&raquo;")

p("Darius acquiesce, touch&eacute; que Clara ait per&ccedil;u aussi "
  "justement l'intention profonde derri&egrave;re son travail, et "
  "confie, pour la premi&egrave;re fois, &agrave; quel point ce projet est "
  "devenu, bien plus qu'un simple passe-temps, une "
  "mani&egrave;re de faire la paix avec une histoire trop vaste "
  "pour &ecirc;tre enti&egrave;rement racont&eacute;e &agrave; voix haute.")

p("Franck, invit&eacute; &agrave; d&eacute;couvrir le jeu pour la premi&egrave;re "
  "fois un dimanche apr&egrave;s-midi, enfile le casque avec une "
  "maladresse touchante, et reste silencieux de longues "
  "minutes en explorant le dernier niveau, avant de le "
  "retirer, les yeux embu&eacute;s, incapable de cacher &agrave; quel "
  "point voir son propre fr&egrave;re repr&eacute;sent&eacute; l&agrave;, enfant, "
  "avec tendresse plut&ocirc;t qu'avec horreur, le boulever pse "
  "profond&eacute;ment.")

name("FRANCK")
p("&laquo;&nbsp;T'as fait quelque chose de beau, Darius. Vraiment "
  "beau. Je suis pas s&ucirc;r de comprendre tout ce que &ccedil;a "
  "veut dire, mais je suis fier que ce soit toi qui l'aies "
  "cr&eacute;&eacute;.&nbsp;&raquo;")

p("&Agrave; quinze jours de l'&eacute;ch&eacute;ance, Darius passe une "
  "derni&egrave;re fois voir la petite maison de Templier sur le "
  "coteau, s'asseyant seul dans le jardin de vigne "
  "endormi par l'hiver, cherchant, sans trop savoir "
  "pourquoi, &agrave; puiser dans ce lieu un peu de la force "
  "tranquille que le vieil homme semblait toujours "
  "poss&eacute;der, m&ecirc;me face &agrave; l'impossible.")

p("La semaine pr&eacute;c&eacute;dant le seize f&eacute;vrier s'&eacute;coule avec une "
  "lenteur presque insupportable, chacun des trois amis "
  "guettant le moindre signe suppl&eacute;mentaire sans jamais "
  "vraiment savoir &agrave; quoi s'attendre, et Darius, fid&egrave;le &agrave; "
  "sa promesse de ne plus rien affronter seul, passe "
  "chaque soir avec Clara et Alex, refusant, pour une fois, "
  "de s'isoler derri&egrave;re son casque.")

name("CLARA")
p("&laquo;&nbsp;On devrait peut-&ecirc;tre partir, tous ensemble, quelque "
  "part loin d'ici, juste pour ce jour-l&agrave;. Si &ccedil;a a un rapport "
  "avec Luynes, avec le r&eacute;seau, avec les sites, peut-&ecirc;tre "
  "que t'&eacute;loigner suffirait &agrave; &eacute;viter tout &ccedil;a "
  "compl&egrave;tement.&nbsp;&raquo;")

p("Darius y r&eacute;fl&eacute;chit s&eacute;rieusement, tent&eacute; par cette "
  "solution simple, mais une intuition profonde, forg&eacute;e par "
  "des mois d'exp&eacute;rience avec cette histoire, lui souffle "
  "que fuir ne fera, comme toujours, que retarder "
  "l'&eacute;ch&eacute;ance sans jamais r&eacute;ellement l'annuler, exactement "
  "comme Franck avait fui pendant trente ans sans jamais "
  "vraiment &eacute;chapper &agrave; son propre pass&eacute;.")

name("DARIUS")
p("&laquo;&nbsp;Je crois qu'il faut que je sois l&agrave;, cette fois, pas "
  "que je me cache. Templier disait toujours de ne jamais "
  "rien donner de trop gros, mais il disait aussi de "
  "toujours faire face plut&ocirc;t que fuir. J'ai l'impression "
  "que c'est &ccedil;a, le vrai test, cette fois &mdash; pas de gagner "
  "un combat, mais de rester debout et pr&eacute;sent quoi qu'il "
  "arrive.&nbsp;&raquo;")

p("Franck propose, en dernier recours, de rester "
  "physiquement pr&eacute;sent aupr&egrave;s de son fils pendant toute "
  "la journ&eacute;e du seize f&eacute;vrier, prenant un cong&eacute; "
  "exceptionnel &agrave; son travail, et Clara et Alex, sans "
  "hesiter une seconde, annoncent leur intention de "
  "s&eacute;cher les cours ce jour-l&agrave; pour rester tous ensemble, "
  "quoi que leurs parents puissent en penser.")

p("Clara doit n&eacute;anmoins convaincre sa propre m&egrave;re "
  "de la laisser manquer les cours ce jour pr&eacute;cis, "
  "invoquant un pr&eacute;texte m&eacute;dical vague qui ne "
  "convainc qu'&agrave; moiti&eacute; cette derni&egrave;re, habitu&eacute;e &agrave; "
  "la fiabilit&eacute; scolaire habituelle de sa fille, mais "
  "qui finit par c&eacute;der devant l'insistance inhabituelle "
  "de Clara, sentant confus&eacute;ment que quelque chose "
  "d'important se joue sans parvenir &agrave; en identifier "
  "la nature exacte.")

name("M&Egrave;RE DE CLARA")
p("&laquo;&nbsp;Tu es s&ucirc;re que &ccedil;a va, ma ch&eacute;rie ? Tu me "
  "caches jamais rien d'habitude pour les cours. "
  "&Ccedil;a m'inqui&egrave;te un peu, cette insistance "
  "soudaine.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a va, maman, promis. J'ai juste besoin "
  "d'&ecirc;tre avec Darius demain, c'est important pour "
  "lui, et pour moi aussi. Je t'expliquerai peut-&ecirc;tre "
  "un jour, mais l&agrave; j'ai vraiment besoin que tu me "
  "fasses confiance.&nbsp;&raquo;")

p("Cette demande, formul&eacute;e avec un s&eacute;rieux inhabituel "
  "chez sa fille g&eacute;n&eacute;ralement enjou&eacute;e, finit par "
  "convaincre la m&egrave;re de Clara, qui accepte, non sans "
  "une derni&egrave;re pointe d'inqui&eacute;tude maternelle "
  "qu'elle garde n&eacute;anmoins pour elle, respectant "
  "l'intimit&eacute; grandissante de sa fille adolescente "
  "face &agrave; des probl&egrave;mes qu'elle ne peut, "
  "visiblement, pas encore lui confier enti&egrave;rement.")

p("Ils passent la derni&egrave;re soir&eacute;e avant l'&eacute;ch&eacute;ance chez "
  "Darius, tous les quatre r&eacute;unis, r&eacute;visant une derni&egrave;re "
  "fois chaque d&eacute;tail connu de leur histoire, chaque "
  "objet de la bo&icirc;te en bois align&eacute; sur la table, comme "
  "des soldats se pr&eacute;parant &agrave; une bataille dont ils ignorent "
  "encore compl&egrave;tement la forme qu'elle prendra.")

p("Le seize f&eacute;vrier se l&egrave;ve sur Luynes comme n'importe "
  "quel autre matin d'hiver, un ciel bas et blanc, un froid "
  "sec qui mord les joues, et rien, absolument rien dans "
  "l'atmosph&egrave;re ordinaire du village, ne laisse pr&eacute;sager "
  "l'&eacute;ch&eacute;ance que Darius et ses proches redoutent depuis "
  "des semaines.")

p("Ils se retrouvent tous les quatre d&egrave;s huit heures chez "
  "Darius, la journ&eacute;e enti&egrave;re devant eux, et d&eacute;cident, "
  "apr&egrave;s discussion, de la passer normalement, "
  "refusant de laisser l'angoisse dicter enti&egrave;rement leur "
  "emploi du temps &mdash; un petit-d&eacute;jeuner prolong&eacute;, une "
  "promenade au bord de la Loire malgr&eacute; le froid, des "
  "jeux de soci&eacute;t&eacute; l'apr&egrave;s-midi pour s'occuper l'esprit.")

p("La promenade au bord de la Loire, entam&eacute;e vers dix "
  "heures sous un ciel toujours aussi bas, les m&egrave;ne "
  "jusqu'&agrave; l'ancien embarcad&egrave;re o&ugrave; Darius, Clara et "
  "Alex avaient l'habitude, enfants, de jeter des cailloux "
  "plats en comptant les ricochets, et cette activit&eacute; "
  "toute simple, r&eacute;p&eacute;t&eacute;e machinalement ce matin-l&agrave;, "
  "leur offre une bulle de normalit&eacute; presque douloureuse "
  "&agrave; savourer, tant elle contraste avec la gravit&eacute; de "
  "ce qu'ils redoutent.")

name("ALEX")
p("&laquo;&nbsp;Cinq ricochets, regardez &ccedil;a ! J'ai plus fait &ccedil;a "
  "depuis genre trois ans. On devrait faire &ccedil;a plus "
  "souvent, franchement, m&ecirc;me sans compte &agrave; rebours "
  "flippant en fond sonore.&nbsp;&raquo;")

p("Franck, les observant depuis un banc proche, sourit "
  "malgr&eacute; la tension qui ne le quitte pas vraiment, "
  "touch&eacute; de voir ces trois adolescents capables encore "
  "de rire ensemble malgr&eacute; l'ampleur de ce qu'ils "
  "portent, et se surprend &agrave; esp&eacute;rer, contre toute "
  "raison, que cette journ&eacute;e se terminera finalement "
  "sans le moindre incident.")

p("L'apr&egrave;s-midi se poursuit autour d'un jeu de soci&eacute;t&eacute; "
  "sorti du placard de la chambre de Darius, une "
  "vieille bo&icirc;te de Monopoly aux coins us&eacute;s h&eacute;rit&eacute;e de "
  "son grand-p&egrave;re, et la partie, ponctu&eacute;e de rires et "
  "de contestations amicales sur les r&egrave;gles exactes, "
  "occupe suffisamment leurs esprits pour leur faire, "
  "presque, oublier l'heure qui tourne inexorablement.")

name("CLARA")
p("&laquo;&nbsp;Darius, tu peux pas poser un h&ocirc;tel sur la rue "
  "de la Paix, t'as m&ecirc;me pas les quatre maisons "
  "d'abord, c'est dans les r&egrave;gles &ccedil;a, m&ecirc;me si &ccedil;a "
  "t'arrange pas.&nbsp;&raquo;")

p("Cette dispute enfantine, aussi d&eacute;risoire para&icirc;t-elle "
  "au regard de tout ce qu'ils affrontent par ailleurs, "
  "leur fait un bien immense, chacun s'accrochant, "
  "sans se l'avouer clairement, &agrave; ces petits moments "
  "d'insouciance comme &agrave; des bou&eacute;es de sauvetage "
  "&eacute;motionnelles avant l'&eacute;ch&eacute;ance redout&eacute;e du soir.")

p("Le carnet de Clara reste d&eacute;sesp&eacute;r&eacute;ment silencieux toute "
  "la journ&eacute;e, la cicatrice d'Alex ne se manifeste "
  "d'aucune mani&egrave;re, et &agrave; mesure que les heures passent "
  "sans incident, une forme d'espoir prudent commence &agrave; "
  "na&icirc;tre chez chacun d'eux, l'id&eacute;e que peut-&ecirc;tre, cette "
  "fois, le compte &agrave; rebours n'annon&ccedil;ait rien de "
  "catastrophique apr&egrave;s tout.")

name("ALEX")
p("&laquo;&nbsp;Il est d&eacute;j&agrave; dix-huit heures, et il s'est rien pass&eacute; "
  "du tout. Peut-&ecirc;tre que Kayden se trompait, ou que &ccedil;a "
  "concernait un truc plus symbolique que r&eacute;el, "
  "finalement. &Ccedil;a me rassurerait presque trop d'y "
  "croire.&nbsp;&raquo;")

p("Franck insiste malgr&eacute; tout pour rester jusqu'au bout de "
  "la soir&eacute;e, refusant de baisser sa garde trop t&ocirc;t, et "
  "c'est ensemble, tous les quatre, qu'ils partagent un "
  "d&icirc;ner simple dans la cuisine, presque joyeux malgr&eacute; la "
  "tension r&eacute;siduelle, comme si cette journ&eacute;e finissait "
  "par ressembler, contre toute attente, &agrave; une victoire "
  "tranquille.")

p("Pendant le d&icirc;ner, Franck raconte, avec un enthousiasme "
  "inhabituel, une anecdote de son propre travail au "
  "garage, une r&eacute;paration particuli&egrave;rement complexe "
  "r&eacute;solue plus t&ocirc;t dans la semaine, et Darius l'&eacute;coute "
  "avec un plaisir sinc&egrave;re, savourant cette normalit&eacute; "
  "retrouv&eacute;e entre eux, cette capacit&eacute; nouvelle de son "
  "p&egrave;re &agrave; partager simplement sa journ&eacute;e sans "
  "arri&egrave;re-pens&eacute;e ni gravit&eacute; excessive.")

name("FRANCK")
p("&laquo;&nbsp;Le client &eacute;tait convaincu que c'&eacute;tait la "
  "batterie, mais en fait c'&eacute;tait juste un fusible grill&eacute; "
  "tout b&ecirc;te. &Ccedil;a m'a pris cinq minutes &agrave; trouver, une "
  "fois que j'ai su o&ugrave; chercher. Des fois, les probl&egrave;mes "
  "qui font le plus peur sont les plus simples &agrave; "
  "r&eacute;soudre, en fin de compte.&nbsp;&raquo;")

p("Clara sourit &agrave; cette remarque, presque involontairement "
  "philosophique venant d'un simple r&eacute;cit de m&eacute;canique "
  "automobile, et &eacute;change avec Alex un regard entendu, "
  "tous deux pensant &agrave; quel point cette phrase pourrait "
  "s'appliquer, d'une certaine mani&egrave;re, &agrave; leur propre "
  "situation face &agrave; cette journ&eacute;e redout&eacute;e qui touche "
  "&agrave; sa fin sans le moindre incident.")

p("C'est apr&egrave;s le d&icirc;ner, alors que Franck s'appr&ecirc;te &agrave; "
  "partir et que Clara et Alex enfilent d&eacute;j&agrave; leurs "
  "manteaux, que Darius demande, presque timidement, &agrave; "
  "pouvoir terminer seul, cette derni&egrave;re heure de la "
  "journ&eacute;e, le tout dernier d&eacute;tail de son jeu &mdash; une "
  "simple texture &agrave; ajuster derri&egrave;re la porte close, "
  "quelque chose qu'il veut absolument finir avant de "
  "consid&eacute;rer, officiellement, que le projet est achev&eacute;.")

name("DARIUS")
p("&laquo;&nbsp;Vingt minutes, promis. Juste le temps de finir ce "
  "dernier truc. Vu que rien s'est pass&eacute; de toute la "
  "journ&eacute;e, je pense vraiment qu'on peut se d&eacute;tendre, "
  "maintenant.&nbsp;&raquo;")

p("Franck h&eacute;site, une inqui&eacute;tude diffuse persistant malgr&eacute; "
  "le calme apparent de la journ&eacute;e, mais finit par c&eacute;der, "
  "rassur&eacute; par l'absence totale d'incident depuis le matin, "
  "et quitte l'appartement en promettant de rappeler dans "
  "une demi-heure pour prendre des nouvelles, laissant "
  "Clara et Alex partir chacun de leur c&ocirc;t&eacute;, confiants eux "
  "aussi que cette journ&eacute;e redout&eacute;e touche enfin, "
  "paisiblement, &agrave; sa fin.")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 8 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 9 -- LA DERNI&Egrave;RE PORTE
# ======================================================================
chap(9, "LA DERNI&Egrave;RE PORTE")

p("Darius s'installe &agrave; son bureau, seul dans sa chambre "
  "pour la premi&egrave;re fois depuis des semaines, et ressent, "
  "en enfilant le casque, une paix &eacute;trange, presque parfaite "
  "&mdash; celle d'un travail enfin sur le point de s'achever, "
  "d'une longue ann&eacute;e de peur qui semble, ce soir, "
  "vraiment toucher &agrave; sa fin.")

p("Il retrouve son monde familier, ce couloir qu'il conna&icirc;t "
  "d&eacute;sormais par c&oelig;ur, cette lumi&egrave;re bleue qui clignote "
  "doucement au-dessus de la porte close, et s'attarde un "
  "instant devant le personnage a&icirc;n&eacute; inspir&eacute; de Templier, "
  "qu'il a plac&eacute; l&agrave; comme un gardien silencieux, avant de "
  "s'atteler &agrave; ce dernier d&eacute;tail de texture qu'il voulait "
  "tant peaufiner.")

p("Le compte &agrave; rebours, toujours affich&eacute; dans son coin "
  "habituel, indique d&eacute;sormais z&eacute;ro jour, z&eacute;ro heure, "
  "quelques minutes seulement, et Darius, absorb&eacute; par son "
  "travail, le remarque &agrave; peine, presque soulag&eacute; que "
  "cette journ&eacute;e entière se soit &eacute;coul&eacute;e sans le moindre "
  "incident.")

p("C'est en ajustant une derni&egrave;re fois la lumi&egrave;re au-dessus "
  "de la porte, cherchant &agrave; capter exactement la teinte de "
  "bleu qu'il avait imagin&eacute;e des mois plus t&ocirc;t, que la "
  "porte, pour la premi&egrave;re fois depuis qu'il l'a cr&eacute;&eacute;e, "
  "s'entrouvre d'elle-m&ecirc;me, sans qu'aucune commande, "
  "aucun clic, aucune action de sa part ne l'ait "
  "d&eacute;clench&eacute;e.")

p("Une lumi&egrave;re bien plus intense que celle qu'il a "
  "program&eacute;e filtre par l'entrebâillement, blanche, "
  "&eacute;blouissante, et Darius sent, dans son propre corps, "
  "physiquement, une chaleur inhabituelle irradier depuis "
  "le casque pos&eacute; sur ses yeux, comme si l'objet "
  "lui-m&ecirc;me venait, d'un coup, de prendre vie d'une "
  "mani&egrave;re qu'aucune notice technique n'aurait jamais pu "
  "pr&eacute;voir.")

p("Il entend, dans cette derni&egrave;re seconde de pleine "
  "conscience, une voix qui n'est pas tout &agrave; fait &eacute;trang&egrave;re "
  "&mdash; ni tout &agrave; fait la sienne, ni tout &agrave; fait celle de "
  "Kayden, mais un m&eacute;lange indistinct des deux, prononçant "
  "cette phrase, une derni&egrave;re fois, avec une tendresse "
  "presque insupportable : &laquo;&nbsp;je voulais juste que &ccedil;a "
  "compte.&nbsp;&raquo;")

p("Dans la chambre, seule dans le silence de la nuit "
  "naissante, la petite console de Darius &eacute;met un "
  "grésillement bref, &agrave; peine audible, avant qu'un &eacute;clair "
  "soudain, aveuglant, ne jaillisse du casque encore viss&eacute; "
  "sur son visage &mdash; un bruit sourd, une odeur de plastique "
  "brûl&eacute; envahissant instantan&eacute;ment la pi&egrave;ce, et puis, "
  "plus rien.")

p("Le silence qui suit cet instant est d'une nature "
  "compl&egrave;tement diff&eacute;rente de tous ceux que cette histoire "
  "avait connus jusque-l&agrave; &mdash; non pas un silence "
  "d'attente, ni de tension, mais un silence d&eacute;finitif, "
  "absolu, celui d'une pi&egrave;ce qui vient, sans que personne "
  "au monde n'en soit encore t&eacute;moin, de perdre son seul "
  "occupant.")

p("Franck rappelle, comme promis, une demi-heure apr&egrave;s "
  "&ecirc;tre parti, laissant sonner longuement sans obtenir de "
  "r&eacute;ponse, d'abord agac&eacute;, puis progressivement gagn&eacute; par "
  "une inqui&eacute;tude qu'il tente de rationaliser &mdash; Darius a "
  "d&ucirc; s'endormir, ou n'entend simplement pas son "
  "t&eacute;l&eacute;phone avec le casque sur les oreilles.")

p("Il rappelle une seconde fois, puis une troisi&egrave;me, avant "
  "de renoncer &agrave; la raison et de reprendre sa voiture, "
  "roulant plus vite que n&eacute;cessaire jusqu'&agrave; l'appartement "
  "de son ex-femme, gravissant les escaliers quatre &agrave; "
  "quatre avec cette certitude glaciale, form&eacute;e par des "
  "mois de peur accumul&eacute;e, que quelque chose vient "
  "d'aller irr&eacute;m&eacute;diablement de travers.")

p("La m&egrave;re de Darius, alert&eacute;e par ses coups frapp&eacute;s "
  "avec insistance &agrave; la porte, le laisse entrer, aussi "
  "inqui&egrave;te que lui d&eacute;sormais, et c'est ensemble qu'ils "
  "d&eacute;couvrent, en poussant la porte de la chambre, la "
  "sc&egrave;ne que ni l'un ni l'autre n'oubliera jamais compl&egrave;tement "
  "&mdash; Darius immobile, effondr&eacute; sur son bureau, le "
  "casque encore fum&acirc;nt l&eacute;g&egrave;rement, fondu par endroits, "
  "une odeur &acirc;cre encore suspendue dans l'air de la pi&egrave;ce.")

p("Les secours, appel&eacute;s imm&eacute;diatement, ne peuvent que "
  "constater, malgr&eacute; toutes les tentatives de r&eacute;animation, "
  "l'irr&eacute;versible &mdash; une d&eacute;charge &eacute;lectrique massive, "
  "expliquera-t-on plus tard, provoqu&eacute;e par un composant "
  "d&eacute;fectueux dans la batterie du casque, un incident "
  "extr&ecirc;mement rare mais document&eacute;, capable, dans de "
  "tr&egrave;s rares cas, de se r&eacute;v&eacute;ler fatal.")

p("Franck reste prostr&eacute; pendant de longues heures dans le "
  "couloir de l'h&ocirc;pital o&ugrave; l'on a transport&eacute; le corps de "
  "son fils, incapable de formuler une seule pens&eacute;e "
  "coh&eacute;rente, hant&eacute; par cette derni&egrave;re image de Darius, "
  "souriant, promettant vingt minutes de plus avant de le "
  "laisser partir tranquillement ce soir-l&agrave;.")

p("Il ne remarque pas, sur le moment, submerg&eacute; par le "
  "chagrin, un d&eacute;tail que seul un t&eacute;moin plus attentif "
  "aurait pu relever &mdash; que l'&eacute;cran de son propre "
  "t&eacute;l&eacute;phone, pos&eacute; sur ses genoux pendant toute cette "
  "attente immobile, affiche, l'espace d'une fraction de "
  "seconde &agrave; peine, un motif de lignes verticales "
  "parfaitement identique &agrave; celui qui accompagnait, "
  "autrefois, chaque manifestation du Non-lieu.")

p("La nouvelle atteint Clara et Alex s&eacute;par&eacute;ment, ce m&ecirc;me "
  "soir, chacun recevant l'appel bris&eacute; de Franck avec une "
  "incr&eacute;dulit&eacute; d'abord totale, puis un effondrement qui ne "
  "ressemble &agrave; rien de ce qu'ils avaient jamais travers&eacute; "
  "auparavant, m&ecirc;me au c&oelig;ur des pires moments du "
  "Non-lieu.")

p("Ce qui frappe Clara, d&egrave;s les premi&egrave;res heures, c'est "
  "l'&eacute;trange pr&eacute;cision avec laquelle elle se souvient de "
  "chaque d&eacute;tail de leur histoire commune &mdash; l'entrep&ocirc;t, "
  "la grotte, Templier, Amboise, le compte &agrave; rebours &mdash; "
  "sans qu'aucun flou, aucune brume caract&eacute;ristique des "
  "oublis provoqu&eacute;s par la Marge ne vienne att&eacute;nuer sa "
  "peine, comme si, cette fois, aucune page n'avait &eacute;t&eacute; "
  "effac&eacute;e nulle part.")

name("CLARA")
p("&laquo;&nbsp;Alex, dis-moi que tu te souviens de tout, toi "
  "aussi. Dis-moi que c'est pas encore un truc que le "
  "monde va nous reprendre, en plus de l'avoir perdu "
  "lui.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;Je me souviens de tout, Clara. De chaque seconde. "
  "&Ccedil;a fait un mal de chien, mais au moins &ccedil;a, personne "
  "peut nous l'enlever.&nbsp;&raquo;")

p("Ils comprennent, en comparant leurs souvenirs "
  "respectifs dans les jours suivants, une chose qu'aucun "
  "des deux n'aurait pu anticiper &mdash; que jamais, &agrave; aucun "
  "moment, ils n'avaient &eacute;t&eacute; physiquement connect&eacute;s au "
  "casque de Darius ni &agrave; la session qu'il menait ce "
  "soir-l&agrave;, ayant quitt&eacute; l'appartement bien avant qu'il ne "
  "l'enfile pour la derni&egrave;re fois.")

name("CLARA")
p("&laquo;&nbsp;On &eacute;tait pas dedans, Alex. On &eacute;tait pas branch&eacute;s, "
  "on &eacute;tait m&ecirc;me plus dans l'appartement. Alors si "
  "jamais quelqu'un se demande un jour si tout &ccedil;a s'est "
  "vraiment pass&eacute;, si c'&eacute;tait pas juste un jeu, juste "
  "l'imagination de Darius depuis le d&eacute;but &mdash; nous, on "
  "sait que non. On &eacute;tait l&agrave;. Pour de vrai. En dehors de "
  "tout &ccedil;a.&nbsp;&raquo;")

p("Cette certitude, fragile mais in&eacute;branlable, devient, "
  "dans les jours de deuil qui suivent, la seule chose &agrave; "
  "laquelle Clara et Alex parviennent &agrave; se raccrocher "
  "solidement &mdash; la preuve vivante, port&eacute;e &agrave; deux, que "
  "l'histoire enti&egrave;re de Darius, aussi impossible qu'elle "
  "puisse para&icirc;tre racont&eacute;e &agrave; un &eacute;tranger, n'&eacute;tait pas "
  "qu'une simulation referm&eacute;e sur elle-m&ecirc;me le soir de sa "
  "mort, mais quelque chose qui leur &eacute;tait vraiment, "
  "r&eacute;ellement, arriv&eacute; &agrave; tous les trois.")

p("Franck, de son c&ocirc;t&eacute;, retrouve les deux amis quelques "
  "jours plus tard, ravag&eacute; par un chagrin qu'il n'aurait "
  "jamais imagin&eacute; pouvoir un jour ressentir avec une telle "
  "intensit&eacute;, et leur confie, la voix bris&eacute;e, qu'il a lui "
  "aussi gard&eacute; intacte chaque parcelle de m&eacute;moire "
  "partag&eacute;e avec son fils, comme si le monde ext&eacute;rieur, "
  "cette fois, avait renonc&eacute; &agrave; leur voler quoi que ce soit "
  "de plus.")

p("Le reste de Luynes, lui, ne conna&icirc;t de cette histoire que "
  "sa version la plus simple, la plus supportable &mdash; un "
  "accident domestique tragique, un adolescent brillant "
  "emport&eacute; par un mat&eacute;riel &eacute;lectronique d&eacute;fectueux, une "
  "nouvelle qui &eacute;meut le village entier sans qu'aucun "
  "habitant, except&eacute; trois d'entre eux et un p&egrave;re "
  "endeuill&eacute;, ne soup&ccedil;onne la moindre trace de Marge, de "
  "Non-lieu, ou de programme M.13.")

p("Le principal du coll&egrave;ge organise une minute de silence "
  "en salle de permanence, les professeurs &eacute;voquent, la "
  "gorge nou&eacute;e, un &eacute;l&egrave;ve discret mais attachant, et "
  "personne, dans cette version officielle et rassurante des "
  "&eacute;v&eacute;nements, ne mentionne jamais le jeu que Darius "
  "avait pass&eacute; des mois &agrave; construire seul dans sa "
  "chambre, ni ce qu'il pouvait bien repr&eacute;senter pour lui.")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a me rend dingue, d'entendre tout le monde "
  "parler de lui comme d'un gamin qui a eu un accident "
  "b&ecirc;te avec un casque. Ils savent rien de tout ce qu'il a "
  "vraiment fait, de tout ce qu'il a vraiment travers&eacute;. Pour "
  "eux, c'est juste... un fait divers triste.&nbsp;&raquo;")

p("Alex, plus pragmatique face &agrave; cette injustice, lui "
  "rappelle que c'est peut-&ecirc;tre mieux ainsi, que Darius "
  "lui-m&ecirc;me n'aurait probablement pas voulu voir son "
  "histoire enti&egrave;re expos&eacute;e publiquement, transform&eacute;e en "
  "spectacle m&eacute;diatique ou en objet de curiosit&eacute; morbide "
  "pour des inconnus incapables de vraiment comprendre.")

name("ALEX")
p("&laquo;&nbsp;On sait, nous. Franck sait. &Ccedil;a suffit peut-&ecirc;tre. Tout "
  "le monde n'a pas besoin de tout savoir pour que &ccedil;a ait "
  "vraiment compt&eacute;.&nbsp;&raquo;")

p("Cette phrase, prononc&eacute;e presque par hasard, r&eacute;sonne "
  "&eacute;trangement dans l'esprit de Clara, lui rappelant "
  "malgr&eacute; elle la formule si souvent r&eacute;p&eacute;t&eacute;e par "
  "Kayden depuis son enfance, cette qu&ecirc;te obstin&eacute;e d'un "
  "sens, d'une reconnaissance, que Darius, lui, semble "
  "avoir finalement trouv&eacute;e d'une mani&egrave;re bien plus "
  "discr&egrave;te et bien plus sinc&egrave;re que son ancien "
  "adversaire.")

p("Ils d&eacute;cident, tous les deux, de garder pour eux "
  "l'essentiel de cette histoire, se contentant, face aux "
  "questions bienveillantes des autres &eacute;l&egrave;ves, de r&eacute;ponses "
  "&eacute;vasives sur leur amiti&eacute; avec Darius, prot&eacute;geant "
  "jalousement, comme un dernier cadeau qu'ils pourraient "
  "encore lui offrir, la v&eacute;rit&eacute; enti&egrave;re de qui il &eacute;tait "
  "vraiment.")

p("Franck se retrouve, dans les jours qui suivent, &agrave; g&eacute;rer "
  "seul l'essentiel des d&eacute;marches li&eacute;es aux obs&egrave;ques, la "
  "m&egrave;re de Darius trop effondr&eacute;e pour s'occuper des "
  "d&eacute;tails pratiques, et il d&eacute;couvre, dans cette t&acirc;che "
  "douloureuse, une forme &eacute;trange de r&eacute;confort &mdash; celle de "
  "pouvoir enfin faire quelque chose de concret pour son "
  "fils, m&ecirc;me si ce quelque chose consiste &agrave; choisir un "
  "cercueil et une date d'enterrement.")

p("Il d&eacute;cide, apr&egrave;s r&eacute;flexion, d'organiser la c&eacute;r&eacute;monie "
  "dans la petite &eacute;glise de Luynes, celle-l&agrave; m&ecirc;me dont "
  "l'ancien presbyt&egrave;re abrite la biblioth&egrave;que o&ugrave; Darius "
  "avait pass&eacute; tant d'heures &agrave; fouiller les archives "
  "anciennes, sentant que ce choix, symboliquement, "
  "aurait plu &agrave; son fils, m&ecirc;me si personne d'autre ne "
  "saisirait jamais cette r&eacute;sonance particuli&egrave;re.")

p("Clara propose, timidement, d'apporter son carnet lors "
  "de la c&eacute;r&eacute;monie, sans trop savoir pourquoi elle ressent "
  "ce besoin, seulement guid&eacute;e par l'intuition que cet "
  "objet, t&eacute;moin silencieux de tant d'&eacute;v&eacute;nements "
  "extraordinaires, m&eacute;rite d'&ecirc;tre pr&eacute;sent &agrave; ce dernier "
  "moment, comme un ultime lien entre l'ordinaire et "
  "l'extraordinaire qu'ils ont partag&eacute; tous ensemble.")

name("FRANCK")
p("&laquo;&nbsp;Apporte-le. Je pense que Darius aurait aim&eacute; &ccedil;a. "
  "Vous avez tous les deux &eacute;t&eacute; tellement plus qu'un "
  "simple soutien pour lui, tout au long de cette histoire. "
  "&Ccedil;a me semble juste que vous soyez pr&eacute;sents avec ce "
  "qu'il vous a laiss&eacute;.&nbsp;&raquo;")

p("Alex, de son c&ocirc;t&eacute;, d&eacute;cide de porter, sous sa manche, "
  "la cicatrice bien visible pour la premi&egrave;re fois depuis "
  "des mois, refusant de la cacher plus longtemps, comme "
  "une mani&egrave;re silencieuse d'honorer tout ce que lui et "
  "Darius avaient travers&eacute; ensemble, m&ecirc;me si personne "
  "d'autre, dans l'assistance, ne pourrait jamais en "
  "comprendre la signification exacte.")

p("La bo&icirc;te en bois, contenant le pon&ccedil;on grav&eacute; d'un "
  "&laquo;&nbsp;K.&nbsp;&raquo;, celui de Templier grav&eacute; d'un &laquo;&nbsp;T.&nbsp;&raquo;, le b&acirc;ton "
  "us&eacute; et le carnet de Clara, est plac&eacute;e, &agrave; la demande "
  "expresse de Franck, dans le cercueil aux c&ocirc;t&eacute;s de son "
  "fils &mdash; non pas le carnet lui-m&ecirc;me, que Clara garde "
  "pr&eacute;cieusement, mais une copie manuscrite qu'elle a "
  "r&eacute;alis&eacute;e des passages les plus importants, une "
  "derni&egrave;re trace tangible de tout ce que Darius a "
  "accompli.")

p("Le jour de l'enterrement se l&egrave;ve, comme un &eacute;cho cruel "
  "de tant d'autres matins d&eacute;cisifs de cette histoire, sous "
  "un ciel d&eacute;gag&eacute;, d'un bleu presque insultant tant il "
  "contraste avec la gravit&eacute; de la journ&eacute;e, et la petite "
  "&eacute;glise de Luynes se remplit, bien plus que Franck ne "
  "l'aurait imagin&eacute;, d'une foule compos&eacute;e de professeurs, "
  "de voisins, d'&eacute;l&egrave;ves du coll&egrave;ge et de simples "
  "habitants touch&eacute;s par la nouvelle.")

p("Clara et Alex arrivent tôt, s'installant au premier rang "
  "aux c&ocirc;t&eacute;s de Franck et de la m&egrave;re de Darius, le "
  "carnet serr&eacute; contre la poitrine de Clara comme un "
  "talisman, la cicatrice d'Alex visible sous sa manche "
  "retrouss&eacute;e, tous deux port&eacute;s par cette certitude "
  "commune qui les distingue de chaque autre personne "
  "pr&eacute;sente dans l'assistance : ils savent, eux, exactement "
  "qui &eacute;tait vraiment Darius, et ce qu'il a v&eacute;cu.")

p("Le pr&ecirc;tre, ne connaissant de Darius que ce que Franck "
  "a bien voulu lui confier, prononce une homélie sobre "
  "&eacute;voquant un adolescent curieux, passionn&eacute; "
  "d'informatique, aim&eacute; de ses proches, sans jamais "
  "soup&ccedil;onner &agrave; quel point ces mots, bien que sinc&egrave;res, "
  "ne repr&eacute;sentent qu'une fraction infime de la v&eacute;rit&eacute; "
  "enti&egrave;re.")

p("Mme Ferrand, la biblioth&eacute;caire, assiste elle aussi &agrave; la "
  "c&eacute;r&eacute;monie, discr&egrave;te au fond de l'&eacute;glise, ayant fini "
  "par comprendre, sans jamais tout savoir, que ces trois "
  "adolescents poursuivaient depuis des mois une "
  "recherche bien plus s&eacute;rieuse qu'un simple expos&eacute; "
  "scolaire, et pleure discr&egrave;tement pendant toute la "
  "c&eacute;r&eacute;monie sans trop savoir elle-m&ecirc;me pourquoi ce "
  "chagrin la frappe avec une telle intensit&eacute;.")

p("Franck, appel&eacute; &agrave; prendre la parole, parvient, malgr&eacute; "
  "les larmes, &agrave; prononcer quelques mots simples, sinc&egrave;res, "
  "&eacute;voquant sans d&eacute;tail un fils qu'il regrette de ne pas "
  "avoir mieux compris plus t&ocirc;t, mais qu'il a appris, dans "
  "sa derni&egrave;re ann&eacute;e de vie, &agrave; conna&icirc;tre et &agrave; admirer "
  "plus profond&eacute;ment qu'il n'aurait jamais cru possible.")

name("FRANCK")
p("&laquo;&nbsp;Mon fils portait des choses bien plus lourdes que "
  "ce que la plupart d'entre vous imaginent. Il les a "
  "port&eacute;es avec un courage que je n'ai jamais eu, moi, &agrave; "
  "son &acirc;ge, ni m&ecirc;me plus tard. Je suis fier de lui. Je "
  "serai toujours fier de lui.&nbsp;&raquo;")

p("La c&eacute;r&eacute;monie se poursuit dans un recueillement digne, "
  "et c'est en sortant de l'&eacute;glise, le cercueil port&eacute; par "
  "quatre proches de la famille, que Clara remarque, sans "
  "trop savoir si elle doit y attacher de l'importance, un "
  "l&eacute;ger scintillement bleu&acirc;tre traverser, l'espace d'une "
  "fraction de seconde, l'&eacute;cran d'un t&eacute;l&eacute;phone abandonn&eacute; "
  "sur un banc, sans que son propri&eacute;taire, absorb&eacute; par son "
  "chagrin, ne remarque quoi que ce soit.")

p("Alex, marchant en silence aux c&ocirc;t&eacute;s de Clara sur le "
  "parvis de l'&eacute;glise, sent sa cicatrice le picoter "
  "l&eacute;g&egrave;rement, une sensation famili&egrave;re qu'il a appris, au "
  "fil des mois, &agrave; ne plus redouter compl&egrave;tement, "
  "presque un dernier salut discret de tout ce que "
  "Darius a travers&eacute; avec lui, une derni&egrave;re trace "
  "physique d'une amiti&eacute; que la mort ne parvient pas &agrave; "
  "effacer enti&egrave;rement.")

p("Un groupe d'anciens camarades de classe, "
  "reconnaissables &agrave; leur &acirc;ge et &agrave; leur g&ecirc;ne palpable "
  "face &agrave; un deuil qu'ils ne savent pas vraiment "
  "comment traverser, s'attarde pr&egrave;s de l'entr&eacute;e de "
  "l'&eacute;glise, &eacute;changeant des souvenirs simples et "
  "touchants &mdash; une blague de Darius en cours de "
  "sciences, sa mani&egrave;re particuli&egrave;re d'incliner "
  "l&eacute;g&egrave;rement la t&ecirc;te vers la gauche quand il "
  "r&eacute;fl&eacute;chissait &mdash; sans jamais soup&ccedil;onner &agrave; quel "
  "point ce d&eacute;tail physique, h&eacute;rit&eacute; directement de "
  "Templier et de toute une lign&eacute;e avant lui, portait une "
  "signification qui d&eacute;passait de tr&egrave;s loin la simple "
  "habitude adolescente.")

name("PROFESSEUR PRINCIPAL")
p("&laquo;&nbsp;C'&eacute;tait un &eacute;l&egrave;ve discret, mais quand il "
  "parlait, on sentait toujours qu'il avait r&eacute;fl&eacute;chi "
  "avant. Je me souviens d'une r&eacute;daction qu'il avait "
  "&eacute;crite sur l'histoire locale, avec un s&eacute;rieux "
  "impressionnant pour son &acirc;ge. Je pensais jamais avoir "
  "&agrave; prononcer ces mots &agrave; son propos, un jour comme "
  "aujourd'hui.&nbsp;&raquo;")

p("Franck, entendant ces derniers mots par-dessus "
  "l'&eacute;paule d'un proche venu lui pr&eacute;senter ses "
  "condol&eacute;ances, sent une bouff&eacute;e de fiert&eacute; se m&ecirc;ler "
  "&agrave; son chagrin, cette r&eacute;daction mentionn&eacute;e n'&eacute;tant "
  "autre, il le sait, que le fruit direct des recherches "
  "men&eacute;es par son fils sur la l&eacute;gende de la Marge, "
  "d&eacute;guis&eacute;e habilement en simple devoir scolaire pour "
  "ne jamais r&eacute;v&eacute;ler sa v&eacute;ritable port&eacute;e.")

p("Le cort&egrave;ge funéraire se forme lentement sur le "
  "parvis, les quatre porteurs du cercueil &mdash; un oncle "
  "&eacute;loign&eacute; de Franck, deux voisins et le p&egrave;re d'Alex, "
  "tous mobilis&eacute;s dans l'urgence des derniers jours "
  "&mdash; avan&ccedil;ant avec cette lenteur solennelle propre &agrave; "
  "ce genre de proc&eacute;dure, tandis que la petite foule "
  "commence &agrave; s'&eacute;grener en direction du cimeti&egrave;re, &agrave; "
  "quelques centaines de m&egrave;tres seulement de l'&eacute;glise.")

p("Mme Ferrand, marchant discr&egrave;tement en retrait du "
  "cort&egrave;ge principal, rejoint un instant Clara pour lui "
  "glisser, &agrave; voix basse, quelques mots qu'elle a "
  "visiblement pr&eacute;par&eacute;s avec soin, consciente sans "
  "jamais tout &agrave; fait le formuler explicitement, que "
  "cette perte repr&eacute;sente bien plus qu'un simple deuil "
  "adolescent ordinaire.")

name("MME FERRAND")
p("&laquo;&nbsp;Je sais pas exactement tout ce que vous avez "
  "travers&eacute;, tous les trois, avec vos recherches &agrave; la "
  "biblioth&egrave;que. Mais je sais que c'&eacute;tait important, "
  "et que Darius portait &ccedil;a avec un s&eacute;rieux qui "
  "d&eacute;passait largement son &acirc;ge. Si vous avez besoin "
  "d'aide un jour, pour continuer quoi que ce soit, "
  "sachez que ma porte vous reste ouverte.&nbsp;&raquo;")

p("Cette offre discr&egrave;te, formul&eacute;e par une femme qui "
  "n'a jamais totalement compris l'ampleur r&eacute;elle de "
  "ce qu'ils traversaient mais qui a toujours "
  "respect&eacute; leur qu&ecirc;te sans jamais la questionner "
  "excessivement, touche profond&eacute;ment Clara, qui la "
  "remercie sinc&egrave;rement, sachant qu'elle "
  "sollicitera probablement, un jour, cette aide "
  "propos&eacute;e avec tant de discr&eacute;tion et de "
  "bienveillance.")

p("Le petit cimeti&egrave;re de Luynes, install&eacute; en surplomb du "
  "village depuis des si&egrave;cles, offre en cette fin de matin "
  "d'hiver une vue d&eacute;gag&eacute;e sur la Loire, ce m&ecirc;me fleuve "
  "gris&acirc;tre que Darius avait appris, gr&acirc;ce &agrave; Templier, &agrave; "
  "regarder diff&eacute;remment, comme le t&eacute;moin silencieux "
  "d'une histoire bien plus vieille que n'importe lequel de "
  "ses habitants actuels.")

p("La foule, plus restreinte qu'&agrave; l'&eacute;glise, se resserre "
  "autour de la tombe fra&icirc;chement creus&eacute;e, Franck en "
  "premi&egrave;re ligne, le visage ravag&eacute; mais digne, Clara et "
  "Alex juste derri&egrave;re lui, leurs mains jointes sans qu'ils "
  "aient besoin de se le proposer explicitement, cherchant "
  "dans ce simple contact un peu de la force n&eacute;cessaire "
  "pour tenir debout jusqu'au bout.")

p("Alors que le cercueil descend lentement dans la terre "
  "gel&eacute;e, un lampadaire situ&eacute; en bordure du cimeti&egrave;re, "
  "&eacute;teint depuis le matin comme tous les autres &agrave; cette "
  "heure de la journ&eacute;e, clignote soudain une fois, d'une "
  "lumi&egrave;re bleu&acirc;tre inhabituelle pour ce type "
  "d'&eacute;clairage public, avant de s'&eacute;teindre &agrave; nouveau "
  "d&eacute;finitivement, sans que personne, except&eacute; Clara, ne "
  "semble le remarquer.")

p("Elle serre la main d'Alex plus fort, sans un mot, et il "
  "hoche imperceptiblement la t&ecirc;te, ayant vu, lui aussi, ce "
  "m&ecirc;me &eacute;clat fugace, tous deux reconnaissant, sans "
  "besoin de se l'expliquer &agrave; voix haute, cette teinte "
  "particuli&egrave;re de bleu qu'aucun r&eacute;verb&egrave;re ordinaire ne "
  "produit jamais &mdash; exactement celle que Darius avait "
  "choisie, avec un tel soin, pour &eacute;clairer la porte close "
  "de son jeu.")

p("Le pr&ecirc;tre prononce les derni&egrave;res paroles rituelles, "
  "la terre commence &agrave; recouvrir le cercueil, et Clara, "
  "incapable de retenir plus longtemps une pens&eacute;e qui la "
  "hante depuis l'instant m&ecirc;me de l'annonce, murmure, "
  "assez bas pour qu'Alex seul puisse l'entendre, une "
  "question qui restera, pour eux deux, &agrave; jamais sans "
  "r&eacute;ponse d&eacute;finitive.")

name("CLARA")
p("&laquo;&nbsp;Tu crois que c'est lui, l&agrave;, dans cette lumi&egrave;re ? "
  "Kayden, je veux dire. Tu crois qu'il est venu, d'une "
  "mani&egrave;re ou d'une autre, pour &ecirc;tre l&agrave; aussi, "
  "aujourd'hui ?&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;J'en sais rien, Clara. Mais si c'est &ccedil;a, j'esp&egrave;re "
  "vraiment qu'il a fini par trouver sa paix, lui aussi, "
  "quelque part, m&ecirc;me &eacute;parpill&eacute;. &Ccedil;a serait juste, apr&egrave;s "
  "tout ce qui s'est pass&eacute;.&nbsp;&raquo;")

p("Ils restent tous deux immobiles, longtemps apr&egrave;s que "
  "les autres visiteurs ont commenc&eacute; &agrave; se disperser, "
  "fixant cette terre fra&icirc;chement retourn&eacute;e, incapables de "
  "se r&eacute;soudre &agrave; quitter cet endroit tant qu'une derni&egrave;re "
  "part d'eux esp&egrave;re, absurdement, voir Darius se relever "
  "et leur sourire, comme si tout cela n'&eacute;tait, "
  "finalement, qu'une nouvelle &eacute;preuve de plus &agrave; surmonter "
  "ensemble.")

p("Les semaines qui suivent l'enterrement s'&eacute;coulent pour "
  "Clara et Alex dans une sorte de brouillard &eacute;pais, "
  "chaque geste du quotidien &mdash; se rendre en cours, "
  "manger, dormir &mdash; accompli m&eacute;caniquement, comme si "
  "une partie essentielle de leur propre &eacute;nergie vitale "
  "&eacute;tait rest&eacute;e enterr&eacute;e avec leur ami dans ce petit "
  "cimeti&egrave;re surplombant la Loire.")

p("Ils continuent, presque religieusement, &agrave; se retrouver "
  "chaque apr&egrave;s-midi, incapables de supporter l'id&eacute;e de "
  "se s&eacute;parer davantage apr&egrave;s avoir d&eacute;j&agrave; perdu le "
  "troisi&egrave;me membre indispensable de leur trio, et "
  "trouvent, dans cette pr&eacute;sence mutuelle constante, la "
  "seule chose capable d'att&eacute;nuer, un tout petit peu, la "
  "violence du manque.")

name("CLARA")
p("&laquo;&nbsp;J'arr&ecirc;te pas de vouloir lui &eacute;crire un truc, dans "
  "le carnet, comme avant, comme s'il allait me r&eacute;pondre. "
  "C'est idiot, je sais. Mais j'ai l'impression que si "
  "j'arr&ecirc;te d'esp&eacute;rer un signe, alors l&agrave;, vraiment, il "
  "sera parti pour de bon.&nbsp;&raquo;")

p("Le carnet, pourtant, reste d&eacute;sesp&eacute;r&eacute;ment muet, aucune "
  "&eacute;criture &eacute;trang&egrave;re ne venant plus jamais s'y ajouter "
  "d'elle-m&ecirc;me, comme si la disparition de Darius avait, "
  "d'une certaine mani&egrave;re, referm&eacute; d&eacute;finitivement ce canal "
  "particulier qui les avait reli&eacute;s, autrefois, &agrave; Kayden et "
  "&agrave; tout ce myst&eacute;rieux univers parall&egrave;le.")

p("Franck, de son c&ocirc;t&eacute;, traverse ce deuil avec une "
  "dignit&eacute; silencieuse qui &eacute;tonne son entourage, refusant "
  "de sombrer compl&egrave;tement malgr&eacute; l'ampleur &eacute;vidente de "
  "sa douleur, port&eacute; par cette d&eacute;termination nouvelle, "
  "acquise durant la derni&egrave;re ann&eacute;e de vie de son fils, de "
  "ne plus jamais fuir ce qui fait mal.")

name("FRANCK")
p("&laquo;&nbsp;Je vais pas pr&eacute;tendre que &ccedil;a va, parce que &ccedil;a "
  "va pas du tout, et &ccedil;a ira probablement plus jamais "
  "vraiment. Mais je vais pas non plus faire comme si de "
  "rien n'&eacute;tait, comme j'aurais fait avant. Darius m'a "
  "appris &ccedil;a, au moins, dans le peu de temps qu'on a eu "
  "ensemble.&nbsp;&raquo;")

p("Il d&eacute;cide, quelques semaines plus tard, de conserver "
  "intacte la chambre de son fils chez son ex-femme, "
  "refusant pour l'instant d'y toucher, et passe, certains "
  "soirs, de longues heures assis simplement sur le lit, "
  "entour&eacute; des objets familiers, cherchant dans ce silence "
  "particulier une forme de proximit&eacute; que les mots seuls "
  "ne parviennent jamais tout &agrave; fait &agrave; offrir.")

p("La question de la petite maison troglodytique h&eacute;rit&eacute;e "
  "par Darius quelques mois plus t&ocirc;t se pose &agrave; nouveau, "
  "cruellement, apr&egrave;s sa mort &mdash; le notaire, perplexe, "
  "informant Franck que le testament de Templier ne "
  "pr&eacute;voyait aucune clause de succession en cas de "
  "d&eacute;c&egrave;s pr&eacute;matur&eacute; du b&eacute;n&eacute;ficiaire, laissant la "
  "propri&eacute;t&eacute; dans un flou juridique inattendu.")

p("Franck, apr&egrave;s r&eacute;flexion, d&eacute;cide de reprendre &agrave; son "
  "nom la petite propri&eacute;t&eacute; du coteau, incapable de "
  "supporter l'id&eacute;e de la voir vendue &agrave; des inconnus ou "
  "laiss&eacute;e &agrave; l'abandon, et invite Clara et Alex &agrave; "
  "l'accompagner, un dimanche de printemps, pour "
  "d&eacute;couvrir ensemble ce lieu que Darius avait tant aim&eacute; "
  "durant sa derni&egrave;re ann&eacute;e de vie.")

p("Ils trouvent la vigne un peu envahie par les mauvaises "
  "herbes, faute d'entretien depuis plusieurs mois, mais "
  "encore vivante, robuste, prometteuse malgr&eacute; l'absence "
  "prolong&eacute;e de soins, et Clara, en observant les jeunes "
  "pousses perçant d&eacute;j&agrave; entre les ceps, ne peut "
  "s'emp&ecirc;cher d'y voir une forme de m&eacute;taphore un peu "
  "na&iuml;ve mais r&eacute;confortante sur la persistance de la vie "
  "malgr&eacute; le deuil.")

name("ALEX")
p("&laquo;&nbsp;On devrait s'en occuper, non ? De la vigne, je "
  "veux dire. &Ccedil;a serait b&ecirc;te de la laisser mourir "
  "compl&egrave;tement, apr&egrave;s tout ce que Templier et Darius "
  "ont travers&eacute; pour la garder en vie tous les deux.&nbsp;&raquo;")

p("Franck accueille cette id&eacute;e avec un enthousiasme "
  "sinc&egrave;re, et c'est ainsi que na&icirc;t, dans les mois suivants, "
  "une petite habitude nouvelle &mdash; des visites r&eacute;guli&egrave;res "
  "au coteau, tous les trois, parfois accompagn&eacute;s de la "
  "m&egrave;re de Darius, entretenant p&eacute;niblement mais avec "
  "une constance touchante ce petit lopin de vigne devenu, "
  "sans qu'ils l'aient vraiment planifi&eacute;, un m&eacute;morial "
  "vivant plus significatif qu'aucune pierre tombale.")

p("Ils d&eacute;couvrent, en rangeant la maison, quelques "
  "affaires personnelles de Templier jamais r&eacute;cup&eacute;r&eacute;es, "
  "dont un vieux cahier de vigneron d&eacute;taillant, ann&eacute;e "
  "apr&egrave;s ann&eacute;e, les r&eacute;coltes successives, et Clara "
  "d&eacute;cide de continuer cette tradition, tenant d&eacute;sormais "
  "elle-m&ecirc;me le registre de la vigne aux c&ocirc;t&eacute;s de son "
  "propre carnet de recherches, comme deux formes "
  "parall&egrave;les de m&eacute;moire qu'elle refuse de laisser "
  "s'&eacute;teindre.")

p("Un an s'&eacute;coule, marqu&eacute; par cette lente reconstruction "
  "douloureuse mais r&eacute;elle, Clara et Alex terminant leur "
  "ann&eacute;e de troisi&egrave;me puis entamant le lyc&eacute;e, chacun "
  "portant, discr&egrave;tement, une part de l'h&eacute;ritage laiss&eacute; "
  "par Darius &mdash; Clara approfondissant sans rel&acirc;che ses "
  "recherches sur l'histoire de Luynes et de la l&eacute;gende de "
  "la Marge, Alex gardant sa cicatrice visible, presque "
  "fi&egrave;rement d&eacute;sormais, comme la preuve tangible d'une "
  "amiti&eacute; qui a tout travers&eacute;.")

p("Aucune manifestation majeure de la Marge ne vient "
  "troubler cette ann&eacute;e de deuil et de reconstruction, "
  "comme si l'entit&eacute;, quelle qu'elle soit devenue apr&egrave;s la "
  "mort de son dernier porteur connu, avait choisi "
  "d'observer un silence respectueux, ou peut-&ecirc;tre, plus "
  "inqui&eacute;tant encore, de simplement attendre patiemment "
  "l'&eacute;mergence d'un nouveau porteur pour reprendre son "
  "cours l&agrave; o&ugrave; il s'&eacute;tait interrompu.")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a m'inqui&egrave;te, ce silence. Templier disait que &ccedil;a "
  "sautait jamais compl&egrave;tement une g&eacute;n&eacute;ration bien "
  "longtemps. Si Darius &eacute;tait le dernier maillon connu, et "
  "qu'il est plus l&agrave;... j'ose &agrave; peine imaginer qui va devoir "
  "porter &ccedil;a &agrave; sa place, un jour.&nbsp;&raquo;")

p("Ni Clara ni Alex ne parviennent &agrave; se r&eacute;soudre &agrave; "
  "abandonner totalement leurs recherches, continuant, "
  "chacun &agrave; sa mani&egrave;re, &agrave; surveiller le moindre signe "
  "suppl&eacute;mentaire, la moindre lumi&egrave;re clignotante "
  "suspecte, la moindre mention retrouv&eacute;e par hasard "
  "&eacute;voquant Vasseur, la Marge, ou le r&eacute;seau des sept "
  "sites &mdash; fid&egrave;les, malgr&eacute; leur jeune &acirc;ge, &agrave; la "
  "promesse implicite de ne jamais laisser cette histoire "
  "sombrer compl&egrave;tement dans l'oubli.")

p("Ils re&ccedil;oivent, un soir d'automne, un &eacute;trange colis "
  "anonyme d&eacute;pos&eacute; devant la porte de Clara, contenant "
  "une simple feuille manuscrite, d'une &eacute;criture qu'aucun "
  "des deux ne reconna&icirc;t, portant une seule phrase, glaciale "
  "dans sa neutralit&eacute; administrative : &laquo;&nbsp;dossier "
  "Templier-Lenoir class&eacute; &mdash; recherche de successeur en "
  "cours &mdash; ne pas intervenir.&nbsp;&raquo;")

p("Cette d&eacute;couverte confirme, avec une froideur "
  "terrifiante, ce que Franck redoutait depuis la r&eacute;v&eacute;lation "
  "de sa propre fiche &agrave; Amboise &mdash; que l'organisation "
  "responsable de tout ce r&eacute;seau, quelle qu'elle soit "
  "exactement, continue, encore aujourd'hui, bien "
  "au-del&agrave; de la mort de Darius, &agrave; surveiller "
  "activement cette lign&eacute;e ancienne, patiente, m&eacute;thodique, "
  "attendant simplement son heure.")

p("Franck, consult&eacute; imm&eacute;diatement apr&egrave;s cette "
  "d&eacute;couverte troublante, examine longuement la "
  "feuille myst&eacute;rieuse, la retournant plusieurs fois "
  "entre ses doigts comme si le simple geste pouvait "
  "r&eacute;v&eacute;ler un d&eacute;tail suppl&eacute;mentaire sur son origine, "
  "avant de la reposer sur la table avec une gravit&eacute; "
  "renouvel&eacute;e.")

name("FRANCK")
p("&laquo;&nbsp;'Recherche de successeur en cours.' &Ccedil;a veut "
  "dire qu'ils cherchent d&eacute;j&agrave; qui va devoir porter &ccedil;a "
  "apr&egrave;s Darius. &Ccedil;a me rend malade, cette id&eacute;e qu'un "
  "autre gamin, quelque part &agrave; Luynes ou ailleurs, va "
  "devoir vivre ce que mon fils a v&eacute;cu, sans que "
  "personne puisse rien y faire.&nbsp;&raquo;")

p("Clara propose, avec cette d&eacute;termination qui la "
  "caract&eacute;rise depuis toujours face &agrave; l'adversit&eacute;, "
  "d'intensifier leurs propres recherches pr&eacute;ventives, "
  "esp&eacute;rant identifier eux-m&ecirc;mes ce potentiel "
  "successeur avant l'organisation, dans l'espoir "
  "fragile de pouvoir le pr&eacute;parer, ou peut-&ecirc;tre m&ecirc;me le "
  "prot&eacute;ger, avant que le pire ne se reproduise.")

name("CLARA")
p("&laquo;&nbsp;Si on peut trouver qui c'est en premier, "
  "peut-&ecirc;tre qu'on peut faire les choses diff&eacute;remment "
  "cette fois. Pr&eacute;venir plut&ocirc;t que subir. On a d&eacute;j&agrave; "
  "toutes les connaissances que Darius a mis des mois "
  "&agrave; rassembler. &Ccedil;a serait b&ecirc;te de pas s'en servir "
  "pour aider quelqu'un d'autre.&nbsp;&raquo;")

p("Cette r&eacute;solution commune, prise dans le salon de "
  "Franck ce soir d'automne, marquera le d&eacute;but d'une "
  "nouvelle phase de leur veille collective, moins "
  "purement r&eacute;active que par le pass&eacute;, davantage "
  "tourn&eacute;e vers l'anticipation et la protection "
  "&eacute;ventuelle d'un successeur encore inconnu, fid&egrave;les "
  "en cela &agrave; l'esprit m&ecirc;me de ce que Darius avait "
  "toujours d&eacute;fendu &mdash; ne jamais laisser quelqu'un "
  "d'autre affronter seul ce qu'ils avaient eux-m&ecirc;mes "
  "d&ucirc; traverser.")

p("Ils &eacute;tablissent, dans les semaines qui suivent, une "
  "sorte de protocole informel de surveillance &mdash; Clara "
  "se chargeant de suivre les naissances et "
  "d&eacute;m&eacute;nagements r&eacute;cents dans la commune via les "
  "avis municipaux publics, Alex se concentrant sur "
  "les &eacute;coles primaires locales &agrave; la recherche d'enfants "
  "manifestant des signes &eacute;tranges similaires &agrave; ceux "
  "que Darius avait lui-m&ecirc;me pr&eacute;sent&eacute;s enfant, et "
  "Franck maintenant le contact r&eacute;gulier avec Mme "
  "Ferrand &agrave; la biblioth&egrave;que pour toute nouvelle "
  "d&eacute;couverte archivistique pertinente.")

name("FRANCK")
p("&laquo;&nbsp;On n'a pas de garantie que &ccedil;a marche, cette "
  "surveillance. Mais au moins on essaie activement, "
  "plut&ocirc;t que d'attendre passivement que le pire "
  "arrive &agrave; quelqu'un d'autre comme &ccedil;a nous est "
  "arriv&eacute;, &agrave; nous, sans qu'on voie rien venir.&nbsp;&raquo;")

p("Ce syst&egrave;me de veille, mod&eacute;r&eacute;ment efficace mais "
  "surtout r&eacute;confortant psychologiquement pour ceux qui "
  "le maintiennent, leur permet de traverser les mois "
  "suivants avec un sentiment renouvel&eacute; d'utilit&eacute; et de "
  "sens, transformant leur deuil en une forme d'action "
  "concr&egrave;te plut&ocirc;t qu'en simple attente passive et "
  "douloureuse.")

p("Clara, en particulier, s'investit avec une "
  "&eacute;nergie presque f&eacute;brile dans cette veille "
  "collective, passant des heures enti&egrave;res, certains "
  "week-ends, &agrave; &eacute;plucher les registres municipaux &agrave; "
  "la recherche du moindre indice concernant une "
  "naissance ou une installation r&eacute;cente correspondant "
  "aux crit&egrave;res qu'ils ont eux-m&ecirc;mes &eacute;tablis, une "
  "activit&eacute; presque obsessionnelle que son entourage "
  "attribue, sans en conna&icirc;tre la v&eacute;ritable raison, &agrave; "
  "un deuil particuli&egrave;rement tenace.")

name("ALEX")
p("&laquo;&nbsp;Clara, faut que tu penses aussi &agrave; toi, "
  "hein. Je sais que &ccedil;a nous aide, cette mission, mais "
  "faut pas non plus que &ccedil;a devienne la seule chose "
  "qui compte dans ta vie. Darius voudrait pas &ccedil;a "
  "pour toi, j'en suis certain.&nbsp;&raquo;")

p("Cette mise en garde bienveillante, formul&eacute;e par "
  "Alex un soir o&ugrave; Clara avait annul&eacute; une sortie entre "
  "amis pour poursuivre ses recherches, touche "
  "profond&eacute;ment la jeune fille, qui reconna&icirc;t, non sans "
  "une pointe de honte, &agrave; quel point cette mission "
  "auto-impos&eacute;e &eacute;tait devenue, ces derniers mois, une "
  "mani&egrave;re commode d'&eacute;viter d'affronter pleinement "
  "son propre chagrin.")

name("CLARA")
p("&laquo;&nbsp;T'as raison, je crois. Je me suis un peu "
  "perdue l&agrave;-dedans, ces derniers temps. Merci de me "
  "le dire, franchement. J'ai besoin d'entendre &ccedil;a, "
  "m&ecirc;me si &ccedil;a fait un peu mal &agrave; l'ego.&nbsp;&raquo;")

p("Ils d&eacute;cident, ensemble, d'&eacute;tablir des limites plus "
  "saines &agrave; leur veille collective, se r&eacute;servant "
  "d&eacute;sormais des soir&eacute;es enti&egrave;res consacr&eacute;es "
  "uniquement &agrave; leur amiti&eacute;, sans jamais &eacute;voquer la "
  "Marge, Vasseur, ou la recherche d'un successeur "
  "&eacute;ventuel, retrouvant ainsi, peu &agrave; peu, un &eacute;quilibre "
  "de vie plus sain, m&ecirc;me au c&oelig;ur du deuil qui ne les "
  "quitte jamais compl&egrave;tement.")

p("Ces soir&eacute;es r&eacute;serv&eacute;es &agrave; leur seule amiti&eacute; "
  "deviennent rapidement un rituel pr&eacute;cieux, souvent "
  "organis&eacute;es autour d'un film ou d'un repas simple "
  "pr&eacute;par&eacute; ensemble, durant lesquelles ils "
  "s'autorisent, enfin, &agrave; rire aux &eacute;clats sans la "
  "moindre culpabilit&eacute;, &agrave; &eacute;voquer des souvenirs "
  "d'enfance plus l&eacute;gers, ou simplement &agrave; profiter de "
  "la pr&eacute;sence rassurante l'un de l'autre sans autre "
  "objectif que celui d'exister pleinement ensemble.")

name("ALEX")
p("&laquo;&nbsp;Vous vous souvenez de la fois o&ugrave; Darius "
  "avait essay&eacute; d'impressionner cette fille en cours "
  "de sport, et qu'il s'&eacute;tait pris les pieds dans le "
  "tapis de course devant toute la classe ? J'ai "
  "jamais autant ri de ma vie, franchement.&nbsp;&raquo;")

p("Ces anecdotes partag&eacute;es, dr&ocirc;les et tendres &agrave; la "
  "fois, permettent &agrave; Clara et Alex de garder vivant "
  "le souvenir de leur ami sans toujours passer par "
  "le prisme douloureux de la Marge et de ses "
  "myst&egrave;res, red&eacute;couvrant, &agrave; travers ces moments de "
  "rire partag&eacute;, une facette plus l&eacute;g&egrave;re et plus "
  "humaine de Darius que leur qu&ecirc;te obsessionnelle "
  "avait, ces derniers temps, quelque peu occult&eacute;e.")

p("Clara commence &eacute;galement, lors de ces soir&eacute;es "
  "plus l&eacute;g&egrave;res, &agrave; esquisser les premi&egrave;res id&eacute;es "
  "de ce qui deviendra, des ann&eacute;es plus tard, son "
  "premier roman, griffonnant discr&egrave;tement dans un "
  "carnet s&eacute;par&eacute; de celui consacr&eacute; &agrave; leurs "
  "recherches des fragments de sc&egrave;nes, des "
  "dialogues imagin&eacute;s, une mani&egrave;re personnelle de "
  "commencer &agrave; transformer leur chagrin en quelque "
  "chose de cr&eacute;atif et de durable.")

name("ALEX")
p("&laquo;&nbsp;T'&eacute;cris quoi, l&agrave; ? &Ccedil;a fait un moment que "
  "je te vois griffonner des trucs sans nous dire "
  "quoi exactement.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;J'sais pas encore trop. Peut-&ecirc;tre une "
  "histoire, un jour. Une mani&egrave;re de raconter tout "
  "&ccedil;a sans vraiment le raconter, tu vois ? Pour que "
  "Darius continue d'exister quelque part, m&ecirc;me "
  "sous une autre forme.&nbsp;&raquo;")

p("Cette confidence, la premi&egrave;re allusion concr&egrave;te &agrave; "
  "ce qui deviendra son projet litt&eacute;raire, touche "
  "profond&eacute;ment Alex, qui encourage imm&eacute;diatement "
  "son amie &agrave; poursuivre cette id&eacute;e, sentant "
  "intuitivement qu'elle tient l&agrave; une mani&egrave;re "
  "authentique et personnelle de faire son deuil, "
  "diff&eacute;rente de la sienne mais tout aussi valable.")

p("Il propose, ce m&ecirc;me soir, de commencer &agrave; "
  "consigner lui aussi, &agrave; sa mani&egrave;re, une sorte de "
  "journal technique parall&egrave;le, r&eacute;pertoriant "
  "m&eacute;thodiquement tous les aspects m&eacute;caniques et "
  "&eacute;lectroniques &eacute;tranges qu'il a pu observer au fil "
  "de leur aventure, esp&eacute;rant qu'une approche plus "
  "scientifique de leur histoire pourrait, un jour, "
  "compl&eacute;menter utilement le travail plus litt&eacute;raire "
  "et intuitif de Clara.")

name("ALEX")
p("&laquo;&nbsp;Toi t'&eacute;cris l'&acirc;me de l'histoire, moi "
  "j'&eacute;cris sa m&eacute;canique. &Ccedil;a se compl&egrave;te bien, "
  "je trouve. Un jour, peut-&ecirc;tre, quelqu'un aura "
  "besoin des deux versions pour vraiment tout "
  "comprendre.&nbsp;&raquo;")

p("Cette r&eacute;partition naturelle de leurs t&acirc;ches "
  "respectives, refl&eacute;tant fid&egrave;lement leurs "
  "personnalit&eacute;s si diff&eacute;rentes mais si "
  "compl&eacute;mentaires, renforce encore davantage le lien "
  "qui unit Clara et Alex depuis la disparition de "
  "Darius, chacun trouvant dans le travail de "
  "l'autre une validation pr&eacute;cieuse de sa propre "
  "mani&egrave;re, unique, de traverser ce deuil "
  "extraordinaire.")

p("Franck, mis au courant de ces deux projets "
  "parall&egrave;les lors d'un d&icirc;ner dominical quelques "
  "semaines plus tard, propose spontan&eacute;ment de "
  "financer, dans la mesure de ses moyens modestes, "
  "l'impression future du roman de Clara si celle-ci "
  "venait un jour &agrave; aboutir, touchant profond&eacute;ment "
  "la jeune fille par cette confiance anticip&eacute;e en "
  "un projet qu'elle-m&ecirc;me consid&eacute;rait encore comme "
  "un simple exercice personnel sans avenir "
  "certain.")

name("FRANCK")
p("&laquo;&nbsp;Si un jour tu finis ce livre, Clara, je "
  "serai le premier &agrave; en acheter dix exemplaires, "
  "promis. Pour l'offrir &agrave; tout le monde autour de "
  "moi. Darius m&eacute;rite que son histoire soit racont&eacute;e, "
  "d'une mani&egrave;re ou d'une autre.&nbsp;&raquo;")

p("Cette promesse, tenue scrupuleusement des ann&eacute;es "
  "plus tard lorsque le roman verra effectivement le "
  "jour, restera l'un des souvenirs les plus "
  "pr&eacute;cieux de Clara concernant cette p&eacute;riode "
  "difficile mais riche en soutien mutuel qui a "
  "suivi la disparition de son meilleur ami.")

p("Alex, de son c&ocirc;t&eacute;, obtient &eacute;galement, quelques "
  "ann&eacute;es plus tard, la reconnaissance discr&egrave;te "
  "mais sinc&egrave;re de ses propres comp&eacute;tences "
  "techniques lorsqu'il d&eacute;croche son premier stage "
  "d'&eacute;t&eacute; dans une petite entreprise de "
  "cybers&eacute;curit&eacute; tourangelle, un accomplissement "
  "professionnel qu'il attribue directement, sans "
  "jamais totalement l'exprimer &agrave; voix haute, &agrave; "
  "cette curiosit&eacute; technique aiguis&eacute;e par les "
  "myst&egrave;res entourant l'accident de son meilleur "
  "ami.")

name("ALEX")
p("&laquo;&nbsp;C'est fou de penser que tout ce qu'on a "
  "v&eacute;cu avec Darius a fini par orienter toute ma "
  "vie professionnelle future. J'aurais jamais "
  "choisi cette voie sans tout &ccedil;a, je pense.&nbsp;&raquo;")

p("Clara, encourag&eacute;e par ce constat partag&eacute;, "
  "r&eacute;alise &agrave; son tour &agrave; quel point leur amiti&eacute; "
  "avec Darius, m&ecirc;me &eacute;court&eacute;e tragiquement, "
  "continue de fa&ccedil;onner positivement leurs "
  "trajectoires respectives, une forme de "
  "l&eacute;gs invisible mais bien r&eacute;el que leur ami "
  "disparu leur a laiss&eacute;, sans jamais l'avoir "
  "pr&eacute;m&eacute;dit&eacute;.")

name("CLARA")
p("&laquo;&nbsp;On porte tous les deux un peu de lui dans "
  "ce qu'on est devenus, tu sais. C'est peut-&ecirc;tre &ccedil;a, "
  "au fond, la vraie mani&egrave;re de ne jamais vraiment "
  "perdre quelqu'un &mdash; continuer &agrave; grandir gr&acirc;ce &agrave; "
  "ce qu'il nous a appris, m&ecirc;me apr&egrave;s son "
  "d&eacute;part.&nbsp;&raquo;")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 9 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 10 -- CE QUI CONTINUE DE GUETTER
# ======================================================================
chap(10, "CE QUI CONTINUE DE GUETTER")

p("Les premi&egrave;res semaines qui suivent l'enterrement de "
  "Darius voient Clara et Alex retomber, tant bien que "
  "mal, dans une routine scolaire qu'ils traversent "
  "comme des automates, chaque cours, chaque "
  "r&eacute;cr&eacute;ation, chaque trajet familier prenant d&eacute;sormais "
  "une texture &eacute;trange, comme si le monde ordinaire "
  "avait perdu, d'un coup, une partie de sa cons&eacute;quence "
  "r&eacute;elle.")

p("Le principal du coll&egrave;ge, sensible &agrave; la situation, leur "
  "accorde &agrave; tous deux quelques am&eacute;nagements discrets "
  "&mdash; la possibilit&eacute; de sortir de cours en cas de besoin, "
  "un rendez-vous hebdomadaire avec la psychologue "
  "scolaire que Clara accepte par politesse plus que "
  "par conviction, incapable d'expliquer &agrave; une inconnue "
  "bienveillante l'ampleur r&eacute;elle de ce qui pèse sur ses "
  "&eacute;paules.")

name("PSYCHOLOGUE SCOLAIRE")
p("&laquo;&nbsp;C'est normal de ressentir de la col&egrave;re, Clara, "
  "m&ecirc;me envers Darius lui-m&ecirc;me, pour vous avoir "
  "laiss&eacute;s derri&egrave;re. Le deuil, &ccedil;a passe rarement par "
  "une seule &eacute;motion propre et bien range&eacute;e.&nbsp;&raquo;")

p("Clara hoche la t&ecirc;te poliment, sachant pertinemment "
  "que sa col&egrave;re, si elle existe, ne vise ni Darius ni le "
  "hasard d'un accident domestique, mais une "
  "organisation bien r&eacute;elle et bien vivante dont elle ne "
  "peut, &eacute;videmment, souffler mot &agrave; cette femme "
  "bienveillante mais totalement &eacute;trang&egrave;re &agrave; la v&eacute;ritable "
  "nature de leur histoire.")

p("Alex, de son c&ocirc;t&eacute;, retrouve le terrain de foot avec "
  "un soulagement mitig&eacute;, cet espace physique et "
  "&eacute;puisant lui offrant, au moins pendant la dur&eacute;e d'un "
  "entra&icirc;nement, une tr&ecirc;ve bienvenue face &agrave; l'avalanche "
  "de pens&eacute;es qui l'assaillent d&egrave;s qu'il se retrouve "
  "seul, la nuit, incapable de trouver le sommeil.")

name("ENTRAINEUR")
p("&laquo;&nbsp;Prends ton temps, Alex, personne t'en voudra "
  "si t'as besoin de souffler quelques semaines. On "
  "comprend tous ce que tu traverses, avec ton pote.&nbsp;&raquo;")

p("Ce que l'entra&icirc;neur ne peut pas savoir, c'est &agrave; quel "
  "point cette phrase, si banale en apparence, "
  "sous-estime &eacute;norm&eacute;ment ce que repr&eacute;sentait "
  "vraiment Darius pour Alex &mdash; non pas un simple "
  "camarade de classe emport&eacute; par un accident "
  "tragique, mais un fr&egrave;re d'armes ayant travers&eacute;, &agrave; ses "
  "c&ocirc;t&eacute;s, des &eacute;preuves qu'aucun adulte de son entourage "
  "ne pourrait jamais imaginer possibles.")

p("Clara continue, m&ecirc;me dans ces semaines les plus "
  "sombres, &agrave; tenir son carnet avec la m&ecirc;me rigueur "
  "qu'auparavant, consignant d&eacute;sormais non plus les "
  "&eacute;critures myst&eacute;rieuses d'un fragment de Kayden, "
  "mais ses propres observations sur le monde qui "
  "continue, cruellement, &agrave; tourner normalement autour "
  "d'elle malgr&eacute; l'ampleur de sa perte.")

S.append(rule())
S.append(PageBreak())

p("La feuille anonyme rec&ccedil;ue par Clara devient, dans les "
  "semaines qui suivent, l'objet d'une obsession discr&egrave;te "
  "partag&eacute;e avec Alex, tous deux reprenant, avec une "
  "&eacute;nergie renouvel&eacute;e par la col&egrave;re autant que par la "
  "peur, l'ensemble des recherches entam&eacute;es des mois plus "
  "t&ocirc;t avec Darius, esp&eacute;rant identifier, cette fois, "
  "l'organisation pr&eacute;cise qui continue de surveiller leur "
  "petite communaut&eacute;.")

name("ALEX")
p("&laquo;&nbsp;'Ne pas intervenir.' &Ccedil;a veut dire quoi, concr&egrave;tement, "
  "pour eux ? Qu'ils vont juste attendre qu'un autre gamin "
  "de Luynes naisse avec le mauvais nom, ou la mauvaise "
  "adresse, et recommencer tout le cirque depuis le "
  "d&eacute;but ?&nbsp;&raquo;")

p("Franck, mis au courant de cette nouvelle d&eacute;couverte, "
  "d&eacute;cide, pour la premi&egrave;re fois depuis des mois, de "
  "reprendre lui-m&ecirc;me contact avec cette voix administrative "
  "anonyme entendue au t&eacute;l&eacute;phone une ann&eacute;e plus t&ocirc;t, "
  "convaincu qu'un adulte, p&egrave;re endeuill&eacute; d'un ancien "
  "porteur, aurait peut-&ecirc;tre plus de poids qu'un adolescent "
  "isol&eacute; face &agrave; une organisation aussi opaque.")

p("La ligne, cette fois, ne r&eacute;pond plus du tout, remplac&eacute;e "
  "par un simple message enregistr&eacute; indiquant que le "
  "num&eacute;ro n'est plus attribu&eacute;, comme si l'organisation "
  "avait, entre-temps, chang&eacute; discr&egrave;tement tous ses "
  "canaux de contact, laissant Franck, Clara et Alex "
  "totalement d&eacute;munis face &agrave; un adversaire capable de "
  "s'effacer aussi facilement qu'il appara&icirc;t.")

name("FRANCK")
p("&laquo;&nbsp;On dirait qu'ils savent exactement quand se rendre "
  "invisibles, d&egrave;s qu'on s'approche un peu trop pr&egrave;s. &Ccedil;a "
  "fait des d&eacute;cennies qu'ils font &ccedil;a, apparemment, et ils "
  "sont visiblement tr&egrave;s bons &agrave; ce jeu-l&agrave;.&nbsp;&raquo;")

p("Clara consacre, cette ann&eacute;e-l&agrave;, un chapitre entier de "
  "son carnet de recherches personnelles &agrave; cette question "
  "sans r&eacute;ponse, esquissant, par d&eacute;duction et par "
  "intuition, l'hypoth&egrave;se d'une organisation h&eacute;rit&eacute;e du "
  "docteur Vasseur, poursuivie apr&egrave;s sa mort par des "
  "successeurs anonymes convaincus, comme lui, de "
  "l'importance capitale de ma&icirc;triser ce que la l&eacute;gende "
  "appelle la Marge &mdash; peut-&ecirc;tre m&ecirc;me au-del&agrave; des "
  "fronti&egrave;res de la r&eacute;gion, &agrave; une &eacute;chelle qu'aucun d'eux "
  "n'ose encore vraiment imaginer.")

p("Deux ann&eacute;es passent, transformant peu &agrave; peu Clara et "
  "Alex, d&eacute;sormais lyc&eacute;ens, en jeunes adultes port&eacute;s par "
  "une maturit&eacute; pr&eacute;coce forg&eacute;e par tout ce qu'ils ont "
  "travers&eacute; ensemble, sans jamais oublier, une seule "
  "ann&eacute;e, de fleurir la tombe de Darius chaque seize "
  "f&eacute;vrier, cette date d&eacute;sormais associ&eacute;e, pour eux, "
  "autant au deuil qu'&agrave; une forme de veille collective.")

p("Franck refait sa vie, doucement, sans jamais oublier "
  "son fils, retrouvant m&ecirc;me, quelques ann&eacute;es plus tard, "
  "une compagne compr&eacute;hensive &agrave; qui il finit par confier, "
  "avec une honn&ecirc;tet&eacute; totale, l'int&eacute;gralit&eacute; de cette "
  "histoire extraordinaire, trouvant en elle une &eacute;coute "
  "sinc&egrave;re qui ne cherche jamais &agrave; minimiser ni &agrave; "
  "rationaliser ce qu'il a v&eacute;cu &agrave; travers son fils.")

p("Clara publie, sous pseudonyme, un roman largement "
  "inspir&eacute; de leur histoire commune, transform&eacute; en fiction "
  "pour &ecirc;tre publiable sans trahir aucun d&eacute;tail v&eacute;ridique "
  "trop pr&eacute;cis, esp&eacute;rant, confus&eacute;ment, que cette "
  "transposition litt&eacute;raire permettrait &agrave; l'histoire de "
  "Darius de survivre d'une mani&egrave;re ou d'une autre, m&ecirc;me "
  "d&eacute;guis&eacute;e, m&ecirc;me incomprise du grand public.")

name("CLARA")
p("&laquo;&nbsp;Personne saura jamais que c'est vraiment nous, "
  "dans ce livre. Mais nous, on saura. Et peut-&ecirc;tre que "
  "&ccedil;a suffit, comme Alex disait &agrave; l'&eacute;poque &mdash; tout le "
  "monde n'a pas besoin de tout savoir pour que &ccedil;a ait "
  "vraiment compt&eacute;.&nbsp;&raquo;")

p("Alex, de son c&ocirc;t&eacute;, s'oriente vers des &eacute;tudes "
  "d'ing&eacute;nierie informatique, fascin&eacute; malgr&eacute; lui par tout "
  "ce que le casque de Darius avait pu repr&eacute;senter, "
  "esp&eacute;rant, un jour, comprendre suffisamment bien la "
  "technologie pour percer, peut-&ecirc;tre, le myst&egrave;re exact de "
  "ce qui avait r&eacute;ellement caus&eacute; cette d&eacute;faillance fatale, "
  "sans jamais totalement se r&eacute;soudre &agrave; croire &agrave; la "
  "version purement accidentelle des faits.")

p("Ils continuent, tous les deux, &agrave; entretenir la vigne de "
  "Templier chaque &eacute;t&eacute;, cette petite parcelle devenue, au "
  "fil des ann&eacute;es, un v&eacute;ritable sanctuaire priv&eacute; o&ugrave; ils se "
  "retrouvent r&eacute;guli&egrave;rement, loin du regard des autres, "
  "pour se souvenir ensemble, &agrave; voix haute, de tout ce "
  "qu'ils ont v&eacute;cu avec Darius, refusant, ann&eacute;e apr&egrave;s "
  "ann&eacute;e, de laisser le temps &eacute;roder la pr&eacute;cision de "
  "leurs souvenirs communs.")

p("C'est un d&eacute;tail anodin, presque dr&ocirc;le au d&eacute;part, qui "
  "ravive brutalement toutes leurs inqui&eacute;tudes, trois ans "
  "apr&egrave;s la mort de Darius &mdash; la petite s&oelig;ur d'Alex, "
  "&Eacute;milie, &acirc;g&eacute;e d&eacute;sormais de huit ans, se met &agrave; "
  "dessiner, r&eacute;p&eacute;titivement, sans que personne ne le lui "
  "ait jamais sugg&eacute;r&eacute;, un motif de couloirs bord&eacute;s de "
  "portes identiques, toujours accompagn&eacute; d'un simple "
  "num&eacute;ro griffonn&eacute; dans un coin de la feuille : 404.")

name("ALEX")
p("&laquo;&nbsp;Elle a jamais vu le jeu de Darius, Clara. Elle avait "
  "cinq ans quand il est mort, elle s'en souvient m&ecirc;me "
  "pas vraiment. Comment elle peut dessiner exactement "
  "&ccedil;a, ce m&ecirc;me chiffre, ces m&ecirc;mes couloirs ?&nbsp;&raquo;")

p("Ils observent la petite fille avec une attention "
  "renouvel&eacute;e, sans jamais rien lui r&eacute;v&eacute;ler directement de "
  "leur histoire, cherchant simplement &agrave; comprendre si "
  "cette co&iuml;ncidence troublante rel&egrave;ve du pur hasard "
  "enfantin ou d'un signe bien plus inqui&eacute;tant, celui d'une "
  "transmission qui aurait, contre toute attente, saut&eacute; "
  "directement vers la famille d'Alex plut&ocirc;t que vers un "
  "&eacute;tranger comme le voulait la tradition &eacute;tablie par "
  "Templier.")

name("CLARA")
p("&laquo;&nbsp;Templier disait que &ccedil;a passait par le lieu, pas par "
  "le sang. &Eacute;milie a grandi ici, &agrave; Luynes, exactement "
  "comme Darius, comme Templier avant lui. &Ccedil;a pourrait "
  "coller, m&ecirc;me si &ccedil;a me fait horriblement peur d'y "
  "penser.&nbsp;&raquo;")

p("Ils d&eacute;cident, apr&egrave;s une longue discussion angoiss&eacute;e, "
  "de ne surtout rien pr&eacute;cipiter, se souvenant des "
  "avertissements r&eacute;p&eacute;t&eacute;s de Templier sur la n&eacute;cessit&eacute; "
  "de laisser chaque porteur d&eacute;couvrir son r&ocirc;le &agrave; son "
  "propre rythme plut&ocirc;t que de le lui imposer "
  "pr&eacute;matur&eacute;ment, et se contentent, pour l'instant, de "
  "surveiller discr&egrave;tement la petite &Eacute;milie, esp&eacute;rant de "
  "tout leur c&oelig;ur qu'elle ne sera, en fin de compte, qu'une "
  "enfant ordinaire ayant simplement r&eacute;v&eacute; d'un motif "
  "&eacute;trange sans signification particuli&egrave;re.")

p("Alex range, ce soir-l&agrave;, les dessins de sa petite s&oelig;ur "
  "dans une bo&icirc;te sp&eacute;ciale, sans lui expliquer pourquoi, "
  "avec la m&ecirc;me pr&eacute;caution presque religieuse que Darius "
  "avait autrefois consacr&eacute;e &agrave; sa propre bo&icirc;te en bois, "
  "comprenant, avec un vertige nouveau, que cette histoire "
  "n'a peut-&ecirc;tre jamais vraiment cess&eacute;, simplement chang&eacute; "
  "de porteur silencieusement, sous leurs propres yeux, "
  "sans qu'aucun d'eux ne l'ait choisi.")

p("Ni Clara ni Alex ne parviendront jamais &agrave; percer "
  "totalement le myst&egrave;re de l'organisation qui continue, "
  "dans l'ombre, de surveiller Luynes et ses environs, ni "
  "&agrave; d&eacute;terminer avec certitude si la petite &Eacute;milie "
  "deviendra un jour, r&eacute;ellement, la nouvelle porteuse "
  "d'une l&eacute;gende vieille de plusieurs si&egrave;cles, ni m&ecirc;me &agrave; "
  "conna&icirc;tre, un jour, le sort exact de ce qui reste de "
  "Kayden, quelque part, &eacute;parpill&eacute; dans les serveurs "
  "oubli&eacute;s d'un programme officiellement ferm&eacute; depuis "
  "des d&eacute;cennies.")

p("Ce qu'ils savent, en revanche, avec une certitude qui "
  "ne les quittera jamais, c'est ce que Darius a v&eacute;cu, ce "
  "qu'il &eacute;tait vraiment, la fa&ccedil;on exacte dont il riait, "
  "dont il fronçait les sourcils en r&eacute;fl&eacute;chissant, dont il "
  "portait, avec une gr&acirc;ce discr&egrave;te qui ne cessait de les "
  "&eacute;merveiller, un fardeau qu'aucun adolescent de "
  "quatorze ans n'aurait jamais d&ucirc; avoir &agrave; porter seul.")

p("Ils gardent, pr&eacute;cieusement, tous les objets qui leur "
  "restent de lui &mdash; le carnet de Clara, d&eacute;sormais rempli "
  "de ses propres recherches plut&ocirc;t que de messages "
  "myst&eacute;rieux, la cicatrice d'Alex, toujours visible, "
  "toujours silencieuse depuis trois ans, et cette copie du "
  "jeu de Darius que Franck a fini par leur confier, "
  "sauvegard&eacute;e sur un disque dur externe conserv&eacute; comme "
  "une relique.")

name("CLARA")
p("&laquo;&nbsp;On devrait peut-&ecirc;tre y rejouer, un jour. Pas pour "
  "chercher un truc en particulier, juste pour... le "
  "retrouver un peu, tu vois. Pour se souvenir de comment "
  "il voyait le monde, &agrave; travers ce qu'il a construit "
  "l&agrave;-dedans.&nbsp;&raquo;")

p("Ils n'osent pourtant jamais vraiment enfiler eux-m&ecirc;mes "
  "le casque r&eacute;cup&eacute;r&eacute; apr&egrave;s l'accident, remplac&eacute; depuis "
  "par un mod&egrave;le neuf sur lequel la copie du jeu a &eacute;t&eacute; "
  "install&eacute;e, une peur diffuse mais t&eacute;nace les retenant "
  "chaque fois qu'ils s'en approchent, comme si une part "
  "d'eux redoutait, sans se l'avouer clairement, de "
  "d&eacute;couvrir, derri&egrave;re la fameuse porte close, quelque "
  "chose qu'ils ne seraient pas pr&ecirc;ts &agrave; affronter.")

p("Ils finissent par franchir le pas un soir d'hiver, quatre "
  "ans presque jour pour jour apr&egrave;s la mort de Darius, "
  "install&eacute;s tous les deux dans le salon de Franck, le "
  "nouveau casque pos&eacute; entre eux sur la table basse comme "
  "un objet presque sacr&eacute;, et c'est Clara, finalement, qui "
  "trouve le courage de l'enfiler la premi&egrave;re.")

p("Elle retrouve, avec une &eacute;motion immense, ce couloir "
  "familier tant de fois d&eacute;crit par Darius, cette lumi&egrave;re "
  "bleue clignotant doucement au-dessus de la porte close, "
  "et ce personnage a&icirc;n&eacute; inspir&eacute; de Templier, immobile, "
  "attendant patiemment depuis des ann&eacute;es qu'un joueur "
  "vienne enfin franchir cette derni&egrave;re porte que Darius "
  "n'avait jamais eu le temps d'ouvrir lui-m&ecirc;me.")

p("Elle avance, la main tremblante malgr&eacute; l'aspect virtuel "
  "de la manette, et pousse doucement la porte, "
  "d&eacute;couvrant, de l'autre c&ocirc;t&eacute;, non pas un niveau de jeu "
  "&agrave; proprement parler, mais une simple pi&egrave;ce paisible, "
  "baign&eacute;e de lumi&egrave;re douce, o&ugrave; sont repr&eacute;sent&eacute;s, "
  "cote &agrave; c&ocirc;te, tous ceux que cette histoire a touch&eacute;s : "
  "Templier jeune, Kayden enfant souriant, Miel courant "
  "dans un jardin, et, assis simplement sur un banc, un "
  "avatar de Darius lui-m&ecirc;me, immobile, comme en "
  "attente.")

p("Un texte appara&icirc;t, doucement, &agrave; l'&eacute;cran, r&eacute;dig&eacute; par "
  "Darius lui-m&ecirc;me des mois avant sa mort, dans une "
  "s&eacute;quence qu'il avait programm&eacute;e pour se d&eacute;clencher "
  "uniquement lorsque quelqu'un, enfin, at teindrait cette "
  "derni&egrave;re pi&egrave;ce : &laquo;&nbsp;Si vous lisez &ccedil;a, c'est que vous "
  "avez trouv&eacute; la derni&egrave;re porte. Merci d'&ecirc;tre venus "
  "jusqu'ici. &Ccedil;a veut dire que vous vous souvenez encore "
  "de moi, et &ccedil;a, pour moi, &ccedil;a compte plus que tout le "
  "reste.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;Alex... il savait. Il savait qu'un jour on viendrait "
  "jusqu'ici. Il nous a laiss&eacute; un message, exactement l&agrave; "
  "o&ugrave; il fallait, en esp&eacute;rant qu'on le trouverait un "
  "jour.&nbsp;&raquo;")

p("Elle retire le casque, les larmes coulant librement, "
  "et le tend &agrave; Alex qui, &agrave; son tour, d&eacute;couvre cette "
  "m&ecirc;me pi&egrave;ce paisible, ce m&ecirc;me message, ressentant "
  "une paix inattendue se substituer, l'espace de "
  "quelques minutes pr&eacute;cieuses, &agrave; l'angoisse constante "
  "qui accompagne leur vigilance depuis quatre ans.")

p("Les ann&eacute;es suivantes voient Clara et Alex grandir, "
  "quitter progressivement Luynes pour leurs &eacute;tudes "
  "sup&eacute;rieures tout en continuant, avec une fid&eacute;lit&eacute; "
  "in&eacute;branlable, &agrave; revenir chaque seize f&eacute;vrier fleurir la "
  "tombe de Darius et entretenir la vigne de Templier, "
  "cette double veille devenue, au fil du temps, une "
  "part indissociable de leur identit&eacute; d'adultes.")

p("&Eacute;milie, la petite s&oelig;ur d'Alex, grandit elle aussi, "
  "sans jamais montrer d'autre signe particulier apr&egrave;s "
  "cette s&eacute;rie de dessins &eacute;tranges de son enfance, et "
  "Alex, sans jamais totalement se rassurer, finit par "
  "esp&eacute;rer, avec le temps, qu'il s'agissait bel et bien "
  "d'une simple co&iuml;ncidence enfantine plut&ocirc;t que d'un "
  "signe annonciateur.")

p("Franck vieillit doucement, gardant pr&eacute;cieusement la "
  "petite maison du coteau, y recevant r&eacute;guli&egrave;rement "
  "Clara et Alex devenus, avec le temps, une sorte de "
  "famille &eacute;largie qu'il ch&eacute;rit autant que le souvenir de "
  "son fils, et continuant, chaque ann&eacute;e, &agrave; leur raconter "
  "de nouveaux fragments retrouv&eacute;s de sa propre "
  "enfance effac&eacute;e, comme si sa m&eacute;moire, lentement, "
  "continuait de se reconstituer avec les d&eacute;cennies.")

p("Aucune trace suppl&eacute;mentaire de l'organisation "
  "mystérieuse ne refait surface durant toutes ces "
  "ann&eacute;es, le silence retombant, patient et opaque, sur "
  "cette question rest&eacute;e sans r&eacute;ponse d&eacute;finitive, et Clara "
  "finit par consigner, dans les derni&egrave;res pages de son "
  "carnet personnel, une conclusion provisoire qu'elle "
  "sait, au fond d'elle-m&ecirc;me, incompl&egrave;te.")

name("CLARA")
p("&laquo;&nbsp;On saura peut-&ecirc;tre jamais qui ils sont vraiment, ni "
  "ce qu'ils veulent exactement, ni si &Eacute;milie ou quelqu'un "
  "d'autre devra un jour porter &ccedil;a &agrave; la place de Darius. "
  "Mais on sait ce qu'on a v&eacute;cu, nous. &Ccedil;a, personne "
  "pourra jamais nous l'enlever, ni l'effacer, ni le "
  "rendre moins vrai.&nbsp;&raquo;")

p("Elle referme le carnet ce soir-l&agrave;, consciente que "
  "cette histoire, la leur, continuera probablement bien "
  "au-del&agrave; d'eux-m&ecirc;mes, sous une forme ou une autre, "
  "port&eacute;e par d'autres, ailleurs, sans qu'ils en soient "
  "n&eacute;cessairement t&eacute;moins &mdash; et c'est avec cette pens&eacute;e, "
  "&agrave; la fois apaisante et vertigineuse, qu'elle &eacute;teint la "
  "lumi&egrave;re, ce seize f&eacute;vrier-l&agrave;, exactement dix ans "
  "apr&egrave;s la mort de son meilleur ami.")

p("Dix ann&eacute;es, exactement, se sont &eacute;coul&eacute;es depuis cette "
  "soir&eacute;e de f&eacute;vrier o&ugrave; Franck avait rappel&eacute; sans "
  "obtenir de r&eacute;ponse, et Clara, d&eacute;sormais &eacute;crivaine "
  "publi&eacute;e sous son v&eacute;ritable nom depuis quelques ann&eacute;es, "
  "revient chaque fois &agrave; Luynes pour cette date "
  "anniversaire avec la m&ecirc;me fid&eacute;lit&eacute; qu'&agrave; quinze ans, "
  "quand elle rentrait &agrave; pied du coll&egrave;ge en se demandant "
  "encore si tout &ccedil;a avait vraiment exist&eacute;.")

p("Alex, ing&eacute;nieur d&eacute;sormais install&eacute; &agrave; Tours, la "
  "rejoint chaque ann&eacute;e sans faute, sa cicatrice toujours "
  "visible sur son avant-bras, d&eacute;sormais un peu plus "
  "pale avec les ann&eacute;es mais toujours parfaitement "
  "dessin&eacute;e, et sa petite s&oelig;ur &Eacute;milie, devenue une "
  "adolescente parfaitement ordinaire, n'ayant plus "
  "jamais dessin&eacute; le moindre couloir num&eacute;rot&eacute; depuis "
  "cette br&egrave;ve p&eacute;riode de son enfance.")

p("Franck, plus &acirc;g&eacute; d&eacute;sormais, les accueille comme "
  "chaque ann&eacute;e dans la petite maison du coteau, "
  "pr&eacute;parant lui-m&ecirc;me un repas simple avant qu'ils ne "
  "descendent tous ensemble au cimeti&egrave;re, cette petite "
  "proc&eacute;dure devenue, avec le temps, un rituel presque "
  "sacr&eacute; qu'aucun d'eux n'envisagerait de rompre, quoi "
  "qu'il arrive dans leurs vies respectives.")

name("FRANCK")
p("&laquo;&nbsp;Dix ans. &Ccedil;a para&icirc;t &agrave; la fois &eacute;norme et "
  "minuscule, comme temps. Certains jours j'ai "
  "l'impression que c'&eacute;tait hier. D'autres jours, "
  "j'arrive presque plus &agrave; me souvenir du son exact de "
  "sa voix, et &ccedil;a me terrifie plus que tout le reste "
  "r&eacute;uni.&nbsp;&raquo;")

p("Clara le rassure, comme chaque ann&eacute;e, lui r&eacute;p&eacute;tant "
  "des anecdotes pr&eacute;cises, des d&eacute;tails du quotidien de "
  "Darius qu'elle n'a jamais laiss&eacute; s'estomper, refusant "
  "farouchement de le laisser devenir, m&ecirc;me pour son "
  "propre p&egrave;re, une simple silhouette floue effac&eacute;e par "
  "le temps.")

p("Ils marchent ensemble jusqu'au petit cimeti&egrave;re "
  "surplombant la Loire en cette fin d'apr&egrave;s-midi de "
  "f&eacute;vrier, le ciel prenant d&eacute;j&agrave; cette teinte particuli&egrave;re, "
  "entre gris et orange, qui annonce le cr&eacute;puscule "
  "hivernal, et s'arr&ecirc;tent, comme chaque ann&eacute;e, devant la "
  "pierre tombale simple, sobre, portant seulement un "
  "nom, deux dates, et une phrase choisie par Franck lui-m&ecirc;me "
  "quelques semaines apr&egrave;s l'enterrement : &laquo;&nbsp;il a "
  "port&eacute; plus que sa part, et il l'a fait avec courage.&nbsp;&raquo;")

p("Alex d&eacute;pose, comme chaque ann&eacute;e, une petite fleur "
  "s&eacute;ch&eacute;e provenant directement de la vigne de "
  "Templier, tandis que Clara, silencieuse, relit "
  "mentalement, comme un mantra devenu familier, les "
  "grandes lignes de tout ce qu'ils ont v&eacute;cu ensemble &mdash; "
  "la vitrine sous la pluie, l'entrep&ocirc;t, la grotte, le "
  "Non-lieu, Templier, Amboise, le compte &agrave; rebours, la "
  "derni&egrave;re porte &mdash; toute une vie condens&eacute;e en une "
  "poign&eacute;e d'ann&eacute;es d'adolescence extraordinaire.")

p("La nuit tombe doucement sur Luynes pendant qu'ils "
  "s'attardent encore un peu, comme chaque ann&eacute;e, "
  "incapables de vraiment se r&eacute;soudre &agrave; quitter cet "
  "endroit tant que la derni&egrave;re lueur du jour n'a pas "
  "compl&egrave;tement disparu derri&egrave;re les coteaux, et c'est &agrave; "
  "cet instant pr&eacute;cis, dans cette lumi&egrave;re d&eacute;clinante "
  "particuli&egrave;re, que Clara croit percevoir, tr&egrave;s loin, "
  "presque &agrave; la limite de son champ de vision, deux "
  "silhouettes immobiles observant la sc&egrave;ne depuis la "
  "lisi&egrave;re du petit bois qui borde le cimeti&egrave;re.")

p("Elle ne dit rien sur le moment, incertaine d'avoir "
  "vraiment vu quelque chose, se disant que la fatigue et "
  "l'&eacute;motion de cette date anniversaire lui jouent "
  "peut-&ecirc;tre un tour, et il ne lui faut qu'un battement de "
  "cils pour que les deux silhouettes, si elles ont "
  "vraiment exist&eacute;, disparaissent enti&egrave;rement derri&egrave;re "
  "les arbres, absorb&eacute;es par l'obscurit&eacute; grandissante.")

p("Alex, remarquant son trouble, suit son regard sans "
  "poser de question imm&eacute;diate, et tous deux restent "
  "silencieux un long moment, cette vieille vigilance "
  "jamais totalement &eacute;teinte se r&eacute;veillant d'un coup, "
  "identique &agrave; celle qui les habitait &agrave; quatorze ans "
  "devant l'entrep&ocirc;t de Luynes.")

name("ALEX")
p("&laquo;&nbsp;T'as vu quelque chose, l&agrave; ? Ton visage vient de "
  "changer compl&egrave;tement.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;Je sais pas. Peut-&ecirc;tre rien. Peut-&ecirc;tre juste mon "
  "imagination qui me joue des tours, &agrave; force de "
  "toujours guetter quelque chose qui viendrait jamais.&nbsp;&raquo;")

p("Franck, un peu plus loin, appelle doucement qu'il est "
  "temps de rentrer avant que le froid ne devienne "
  "vraiment mordant, et ils quittent, tous les trois, le "
  "petit cimeti&egrave;re dans la p&eacute;nombre naissante, sans que "
  "Clara ne parvienne compl&egrave;tement &agrave; se d&eacute;faire de cette "
  "sensation t&eacute;nace d'avoir &eacute;t&eacute;, l'espace d'un instant, "
  "observ&eacute;e par quelqu'un &mdash; ou quelque chose &mdash; qui les "
  "aurait suivis discr&egrave;tement depuis bien plus longtemps "
  "qu'elle ne voudrait l'admettre.")

p("Ce soir-l&agrave;, une fois rentr&eacute;e chez elle &agrave; Tours, elle "
  "sort une derni&egrave;re fois son vieux carnet de recherches, "
  "d&eacute;sormais rempli aux trois quarts, et y ajoute une "
  "ligne suppl&eacute;mentaire, la premi&egrave;re depuis des mois, "
  "d'une &eacute;criture qui, cette fois, est bien la sienne, "
  "pleinement consciente, sans le moindre myst&egrave;re "
  "surnaturel pour l'accompagner.")

p("&laquo;&nbsp;Dix ans aujourd'hui. J'ai cru voir quelque chose au "
  "cimeti&egrave;re, ce soir. Je saurai peut-&ecirc;tre jamais si "
  "c'&eacute;tait r&eacute;el. Mais si quelqu'un lit ce carnet un jour, "
  "apr&egrave;s moi &mdash; sachez que Darius Lenoir a exist&eacute;, qu'il "
  "a &eacute;t&eacute; extraordinairement courageux, et que ce qu'on a "
  "v&eacute;cu ensemble &eacute;tait vrai. Enti&egrave;rement vrai. Quoi "
  "qu'il en co&ucirc;te de le croire.&nbsp;&raquo;")

p("Alex, troubl&eacute; lui aussi par l'attitude de Clara ce "
  "soir-l&agrave;, sans se l'avouer enti&egrave;rement sur le moment, "
  "d&eacute;cide, quelques jours plus tard, de ressortir "
  "l'ancien fichier de configuration r&eacute;seau r&eacute;cup&eacute;r&eacute; chez "
  "les Vasseur des ann&eacute;es plus t&ocirc;t, celui listant les sept "
  "sites r&eacute;gionaux, et le compare, gr&acirc;ce &agrave; ses "
  "comp&eacute;tences d&eacute;sormais professionnelles d'ing&eacute;nieur, "
  "&agrave; des bases de donn&eacute;es cadastrales r&eacute;centes "
  "accessibles publiquement.")

p("Il d&eacute;couvre, avec un frisson r&eacute;trospectif, qu'au moins "
  "trois des sept propri&eacute;t&eacute;s ont chang&eacute; de propri&eacute;taire "
  "au cours de la derni&egrave;re d&eacute;cennie, rachet&eacute;es "
  "successivement par une m&ecirc;me soci&eacute;t&eacute; civile "
  "immobili&egrave;re dont le si&egrave;ge social, curieusement, "
  "n'appara&icirc;t sous aucune adresse physique v&eacute;rifiable, "
  "seulement une bo&icirc;te postale &agrave; Paris.")

name("ALEX")
p("&laquo;&nbsp;Clara, regarde &ccedil;a. Quelqu'un rach&egrave;te "
  "discr&egrave;tement tous les anciens sites, un par un, depuis "
  "des ann&eacute;es. Amboise, Chinon, Loches. &Ccedil;a peut pas "
  "&ecirc;tre un hasard immobilier ordinaire.&nbsp;&raquo;")

p("Ils passent plusieurs soir&eacute;es &agrave; tenter de remonter "
  "jusqu'aux v&eacute;ritables propri&eacute;taires derri&egrave;re cette soci&eacute;t&eacute; "
  "&eacute;cran, sans jamais parvenir &agrave; percer totalement "
  "l'anonymat soigneusement entretenu de la structure, "
  "mais d&eacute;couvrent, presque par accident, un unique nom "
  "associ&eacute; &agrave; l'un des documents administratifs les plus "
  "anciens de la soci&eacute;t&eacute; : un certain &laquo;&nbsp;A. Vasseur, "
  "repr&eacute;sentant l&eacute;gal&nbsp;&raquo;, dat&eacute; de quelques ann&eacute;es "
  "seulement apr&egrave;s la mort de Darius.")

name("CLARA")
p("&laquo;&nbsp;'A. Vasseur.' &Ccedil;a peut &ecirc;tre n'importe qui portant "
  "ce nom de famille, mais &ccedil;a peut aussi &ecirc;tre... j'sais pas, "
  "un autre enfant du docteur, un cousin, quelqu'un qu'on "
  "n'a jamais rencontr&eacute;. Cette famille a peut-&ecirc;tre &eacute;t&eacute; "
  "bien plus &eacute;tendue que ce qu'on a jamais imagin&eacute;.&nbsp;&raquo;")

p("Cette d&eacute;couverte, loin d'apaiser leurs inqui&eacute;tudes, "
  "confirme au contraire ce que la lettre anonyme "
  "recçue par Clara des ann&eacute;es plus t&ocirc;t laissait d&eacute;j&agrave; "
  "entrevoir : que l'h&eacute;ritage du docteur Vasseur, loin de "
  "s'&eacute;teindre avec sa propre mort ou m&ecirc;me celle de "
  "Kayden, continue d'&ecirc;tre administr&eacute;, discr&egrave;tement mais "
  "activement, par des descendants ou des affili&eacute;s dont ils "
  "ignorent tout, patiemment occup&eacute;s &agrave; reconstituer, "
  "pi&egrave;ce par pi&egrave;ce, l'int&eacute;gralit&eacute; du r&eacute;seau originel.")

p("Ils d&eacute;cident, une fois de plus, de tout partager avec "
  "Franck, d&eacute;sormais &acirc;g&eacute; de pr&egrave;s de soixante ans, "
  "retrouv&eacute; dans la m&ecirc;me petite maison du coteau qu'il "
  "n'a jamais voulu quitter, entour&eacute; par la vigne "
  "d&eacute;sormais bien plus fournie qu'&agrave; l'&eacute;poque de "
  "Templier, entretenue avec un soin constant depuis "
  "plus d'une d&eacute;cennie.")

p("Franck &eacute;coute leur r&eacute;cit avec cette gravit&eacute; "
  "particuli&egrave;re qu'il a appris, avec l'&acirc;ge, &agrave; accueillir "
  "sans paniquer, ayant fini, au fil des ann&eacute;es, par faire "
  "une sorte de paix relative avec l'id&eacute;e que cette "
  "histoire, commenc&eacute;e bien avant sa propre naissance, "
  "ne conna&icirc;trait probablement jamais de conclusion "
  "d&eacute;finitive de son vivant.")

name("FRANCK")
p("&laquo;&nbsp;J'ai plus la force de me battre contre &ccedil;a comme "
  "avant, je vous avoue. Mais j'ai une confiance "
  "absolue en vous deux. Si un jour &ccedil;a doit vraiment "
  "recommencer, avec &Eacute;milie ou quelqu'un d'autre, je "
  "sais que vous serez l&agrave;, exactement comme vous "
  "l'avez &eacute;t&eacute; pour Darius. &Ccedil;a me suffit, comme "
  "certitude, pour dormir tranquille.&nbsp;&raquo;")

p("Il leur montre, ce jour-l&agrave;, un dernier objet qu'il "
  "n'avait jamais eu le courage de leur r&eacute;v&eacute;ler "
  "auparavant &mdash; une photographie r&eacute;cente, prise "
  "quelques mois plus t&ocirc;t &agrave; son insu semble-t-il, "
  "retrouv&eacute;e glissée sous sa porte sans un mot "
  "d'explication, le montrant lui-m&ecirc;me, de dos, dans "
  "son propre jardin, avec au verso, tap&eacute;e &agrave; la "
  "machine, une phrase unique : &laquo;&nbsp;toujours l&agrave;, "
  "toujours surveill&eacute;, toujours patients.&nbsp;&raquo;")

p("Ce dernier avertissement, glacial dans sa sobri&eacute;t&eacute;, "
  "confirme d&eacute;finitivement ce qu'ils redoutaient tous "
  "trois depuis des ann&eacute;es sans jamais oser vraiment se "
  "l'avouer &mdash; que l'organisation h&eacute;riti&egrave;re du "
  "programme M.13, quelle que soit sa forme exacte "
  "aujourd'hui, n'a jamais cess&eacute; de les observer, "
  "patiemment, silencieusement, attendant son heure "
  "avec une constance que ni le deuil, ni le temps, ni "
  "l'oubli n'ont jamais r&eacute;ussi &agrave; entamer.")

p("Clara, rentr&eacute;e chez elle apr&egrave;s cette visite bouleversante "
  "&agrave; Franck, passe plusieurs nuits sans trouver le "
  "sommeil, retournant dans tous les sens cette question "
  "qui la hante depuis le d&eacute;but &mdash; doit-elle continuer &agrave; "
  "chercher, encore et encore, une v&eacute;rit&eacute; que l'organisation "
  "semble d&eacute;termin&eacute;e &agrave; ne jamais leur livrer "
  "compl&egrave;tement, ou accepter, enfin, de vivre avec cette "
  "part d'ombre irr&eacute;ductible qui semble accompagner, "
  "depuis toujours, l'histoire de la Marge ?")

name("CLARA")
p("&laquo;&nbsp;Alex, j'ai r&eacute;fl&eacute;chi. Je crois qu'on devrait arr&ecirc;ter "
  "de chercher &agrave; tout comprendre. Templier disait de "
  "faire attention &agrave; ce qu'on donne. Peut-&ecirc;tre que fouiller "
  "sans arr&ecirc;t, c'est une forme de nourriture qu'on leur "
  "donne, &agrave; eux, sans m&ecirc;me s'en rendre compte.&nbsp;&raquo;")

p("Alex, apr&egrave;s r&eacute;flexion, finit par abonder dans son "
  "sens, reconnaissant que leur qu&ecirc;te incessante de "
  "r&eacute;ponses d&eacute;finitives n'a jamais r&eacute;ussi, en dix ans, qu'&agrave; "
  "les maintenir dans un &eacute;tat de vigilance &eacute;puisante sans "
  "jamais leur offrir la moindre v&eacute;ritable r&eacute;solution, et "
  "propose, &agrave; son tour, une forme de tr&ecirc;ve personnelle "
  "avec cette histoire trop vaste pour eux.")

name("ALEX")
p("&laquo;&nbsp;On continue &agrave; veiller sur &Eacute;milie, sur Franck, sur "
  "la vigne. On oublie pas Darius, jamais. Mais on arr&ecirc;te "
  "d'essayer de gagner une guerre qu'on comprend m&ecirc;me "
  "pas enti&egrave;rement. Peut-&ecirc;tre que c'est &ccedil;a, la vraie "
  "victoire, en fait &mdash; continuer &agrave; vivre, malgr&eacute; tout, "
  "sans se laisser d&eacute;vorer par &ccedil;a.&nbsp;&raquo;")

p("Ils prennent, ce soir-l&agrave;, la d&eacute;cision commune de "
  "ranger d&eacute;finitivement le fichier de configuration "
  "r&eacute;seau, le dossier des porteurs r&eacute;cup&eacute;r&eacute; &agrave; Amboise, "
  "et toutes leurs notes accumul&eacute;es, dans un unique "
  "coffre scell&eacute;, conserv&eacute; chez Franck, accompagn&eacute; "
  "d'une lettre destin&eacute;e &agrave; quiconque, un jour, aurait "
  "besoin d'y acc&eacute;der &agrave; nouveau &mdash; un futur porteur, "
  "peut-&ecirc;tre, ou simplement quelqu'un dispos&eacute; &agrave; "
  "continuer leur veille apr&egrave;s eux.")

p("La lettre que Clara r&eacute;dige, ce soir-l&agrave;, destin&eacute;e &agrave; un "
  "destinataire encore inconnu, r&eacute;sume avec une "
  "sobri&eacute;t&eacute; presque clinique l'essentiel de tout ce "
  "qu'elle et Alex ont appris depuis la vitrine sous la "
  "pluie &mdash; la Marge, les sept sites, la lign&eacute;e des "
  "Darius, le docteur Vasseur et ses descendants "
  "toujours actifs, et l'avertissement final de Templier, "
  "recopiu&eacute; presque mot pour mot : ne jamais rien "
  "donner de trop gros, quoi qu'on vous promette en "
  "&eacute;change.")

p("Elle ach&egrave;ve la lettre par une phrase personnelle, "
  "adress&eacute;e directement &agrave; celui ou celle qui la lira un "
  "jour, peut-&ecirc;tre des ann&eacute;es ou des d&eacute;cennies plus "
  "tard : &laquo;&nbsp;Vous n'&ecirc;tes pas seul, m&ecirc;me si &ccedil;a en a "
  "l'air. On l'a &eacute;t&eacute;, nous, tous les trois, jusqu'au bout. "
  "Faites pareil, si vous le pouvez. &Ccedil;a rend tout un peu "
  "plus supportable.&nbsp;&raquo;")

p("Le coffre, ferm&eacute; &agrave; cl&eacute;, est plac&eacute; dans un recoin "
  "discret de la petite maison du coteau, sous une "
  "latte de plancher que Franck lui-m&ecirc;me a am&eacute;nag&eacute;e "
  "pour l'occasion, exactement comme Templier avait "
  "jadis cach&eacute; son propre pon&ccedil;on dans un tissu us&eacute;, "
  "perp&eacute;tuant ainsi, sans le savoir consciemment, une "
  "tradition de transmission discr&egrave;te vieille de plusieurs "
  "g&eacute;n&eacute;rations.")

name("FRANCK")
p("&laquo;&nbsp;&Ccedil;a me rassure de savoir que c'est cach&eacute; ici, "
  "chez moi. Comme &ccedil;a, tant que je suis vivant, je "
  "pourrai veiller dessus, moi aussi, &agrave; ma mani&egrave;re. On "
  "n'est jamais vraiment seuls dans cette histoire, "
  "finalement, m&ecirc;me quand on a l'impression de "
  "l'&ecirc;tre.&nbsp;&raquo;")

p("Ils referment ensemble, ce soir-l&agrave;, ce chapitre actif "
  "de leur qu&ecirc;te, sans jamais totalement abandonner "
  "leur vigilance quotidienne, mais choisissant "
  "d&eacute;sormais de la porter avec plus de l&eacute;g&egrave;ret&eacute;, moins "
  "d'urgence, comme une part int&eacute;grante mais non "
  "&eacute;crasante de leur existence d&eacute;sormais adulte.")

p("L'ann&eacute;e suivante s'&eacute;coule avec une tranquillit&eacute; "
  "relative que Clara et Alex n'osent presque plus "
  "esp&eacute;rer, chacun avan&ccedil;ant dans sa propre vie "
  "d'adulte &mdash; Clara publiant un second roman, toujours "
  "inspir&eacute; en filigrane de leur histoire commune, Alex "
  "obtenant une promotion m&eacute;rit&eacute;e dans son entreprise "
  "d'ing&eacute;nierie &mdash; sans que ni l'un ni l'autre ne rel&acirc;che "
  "totalement, malgr&eacute; leur d&eacute;cision de l'ann&eacute;e "
  "pr&eacute;c&eacute;dente, cette vigilance devenue une seconde "
  "nature.")

p("Le seize f&eacute;vrier suivant les retrouve, comme "
  "toujours, r&eacute;unis chez Franck avant de descendre "
  "ensemble au cimeti&egrave;re, cette ann&eacute;e marqu&eacute;e par une "
  "atmosph&egrave;re un peu diff&eacute;rente, plus l&eacute;g&egrave;re "
  "peut-&ecirc;tre, comme si leur d&eacute;cision de ne plus se "
  "laisser d&eacute;vorer par la qu&ecirc;te de r&eacute;ponses avait "
  "vraiment port&eacute; ses fruits sur leur &eacute;quilibre &eacute;motionnel "
  "collectif.")

name("FRANCK")
p("&laquo;&nbsp;J'ai l'impression que cette ann&eacute;e, on est "
  "vraiment venus pour se souvenir de lui, pas pour "
  "guetter un signe ou une menace. &Ccedil;a fait du bien, "
  "cette diff&eacute;rence. &Ccedil;a fait longtemps que je l'avais "
  "pas ressentie aussi clairement.&nbsp;&raquo;")

p("Ils passent un long moment devant la tombe, "
  "&eacute;changeant des souvenirs plus l&eacute;gers cette fois, des "
  "anecdotes dr&ocirc;les plut&ocirc;t que des r&eacute;v&eacute;lations "
  "angoissantes, riant m&ecirc;me franchement en &eacute;voquant une "
  "bêtise commise par Darius lors d'un cours de "
  "math&eacute;matiques des ann&eacute;es plus t&ocirc;t, cette capacit&eacute; &agrave; "
  "rire malgr&eacute; le deuil devenue, avec le temps, une "
  "forme d'hommage tout aussi sinc&egrave;re que les larmes des "
  "premi&egrave;res ann&eacute;es.")

p("Aucune silhouette myst&eacute;rieuse ne vient troubler cette "
  "visite paisible, et Clara elle-m&ecirc;me finit par se "
  "convaincre, avec le temps, que la vision de l'ann&eacute;e "
  "pr&eacute;c&eacute;dente n'&eacute;tait probablement qu'un tour jou&eacute; par "
  "son propre &eacute;puisement &eacute;motionnel, une derni&egrave;re "
  "r&eacute;sistance de son esprit avant d'accepter, enfin, de "
  "vivre avec cette histoire sans en faire une source "
  "permanente d'angoisse.")

p("C'est Franck, quelques mois plus tard, un &eacute;t&eacute; "
  "particuli&egrave;rement chaud, qui re&ccedil;oit, sans le moindre "
  "signe avant-coureur, une enveloppe d&eacute;pos&eacute;e directement "
  "dans sa bo&icirc;te aux lettres, sans timbre ni cachet "
  "postal, contenant une simple invitation manuscrite, "
  "d'une &eacute;criture soign&eacute;e et formelle qu'aucun d'eux ne "
  "reconna&icirc;t.")

p("&laquo;&nbsp;Monsieur Lenoir. Nous souhaitons vous rencontrer, "
  "vous et les proches de votre fils, pour discuter de "
  "l'avenir du domaine familial Vasseur et des questions "
  "en suspens concernant votre h&eacute;ritage commun. "
  "Rendez-vous le seize f&eacute;vrier prochain, midi, &agrave; "
  "l'ancienne propri&eacute;t&eacute; de Fondettes. Venez seuls, ou "
  "ne venez pas du tout.&nbsp;&raquo;")

p("Franck appelle imm&eacute;diatement Clara et Alex, la voix "
  "tremblante, incapable de d&eacute;cider si cette invitation "
  "repr&eacute;sente enfin l'occasion tant attendue d'obtenir des "
  "r&eacute;ponses d&eacute;finitives, ou un pi&egrave;ge dangereux tendu "
  "par une organisation dont ils ignorent toujours "
  "l'&eacute;tendue r&eacute;elle.")

name("CLARA")
p("&laquo;&nbsp;Onze ans qu'on essaie de comprendre qui ils sont "
  "vraiment, et l&agrave; ils nous invitent directement, le jour "
  "anniversaire de la mort de Darius en plus. &Ccedil;a peut "
  "pas &ecirc;tre un hasard, ce choix de date. Ils savent "
  "exactement ce qu'ils font.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;On avait dit qu'on arr&ecirc;tait de chercher activement. "
  "Mais l&agrave;, c'est eux qui viennent &agrave; nous. C'est peut-&ecirc;tre "
  "diff&eacute;rent. Peut-&ecirc;tre qu'ignorer &ccedil;a serait pire que "
  "d'y aller, cette fois.&nbsp;&raquo;")

p("Ils d&eacute;battent pendant des jours de la conduite &agrave; "
  "tenir, partag&eacute;s entre la prudence enseign&eacute;e par "
  "Templier et cette curiosit&eacute; jamais totalement &eacute;teinte "
  "qui les a toujours pouss&eacute;s, depuis l'adolescence, &agrave; "
  "vouloir comprendre plut&ocirc;t que fuir, et finissent, "
  "apr&egrave;s une longue discussion, par accepter l'invitation "
  "&mdash; tous les trois ensemble, cette fois, refusant "
  "cat&eacute;goriquement l'id&eacute;e de s'y rendre s&eacute;par&eacute;ment ou "
  "de laisser Franck y aller seul.")

p("Le seize f&eacute;vrier suivant marquera ainsi, "
  "onze ans exactement apr&egrave;s la mort de Darius, un "
  "nouveau rendez-vous avec cette histoire qu'ils "
  "avaient sinc&egrave;rement esp&eacute;r&eacute; pouvoir enfin laisser "
  "reposer, une derni&egrave;re confrontation dont aucun d'eux "
  "ne pourrait, ce jour-l&agrave;, mesurer encore l'ampleur "
  "r&eacute;elle.")

p("Dans les jours pr&eacute;c&eacute;dant ce rendez-vous, chacun "
  "des trois se pr&eacute;pare &agrave; sa mani&egrave;re &mdash; Clara relit "
  "int&eacute;gralement son carnet de recherches, soulignant "
  "les passages qui pourraient s'av&eacute;rer utiles &agrave; "
  "invoquer face &agrave; Ambroise Vasseur ; Alex v&eacute;rifie et "
  "recharge un vieux t&eacute;l&eacute;phone jetable achet&eacute; "
  "sp&eacute;cialement pour l'occasion, au cas o&ugrave; ils "
  "auraient besoin de communiquer discr&egrave;tement sans "
  "risquer d'&ecirc;tre trac&eacute;s ; et Franck, la veille au soir, "
  "passe de longues heures assis dans le jardin de "
  "vigne, cherchant dans ce lieu impr&eacute;gn&eacute; de la "
  "pr&eacute;sence de Templier et de Darius une force "
  "tranquille pour affronter ce qui les attend.")

name("FRANCK")
p("&laquo;&nbsp;Si vous m'entendez, tous les deux, j'esp&egrave;re "
  "que vous approuvez cette d&eacute;cision d'y aller. J'ai "
  "l'impression de pas avoir vraiment le choix, de "
  "toute fa&ccedil;on. Cette histoire nous rattrape toujours, "
  "d'une mani&egrave;re ou d'une autre.&nbsp;&raquo;")

p("Clara passe &eacute;galement cette derni&egrave;re soir&eacute;e &agrave; "
  "relire, une fois de plus, la lettre laiss&eacute;e par "
  "Templier dans le testament, s'attardant longuement "
  "sur cette phrase qui r&eacute;sonne d&eacute;sormais avec une "
  "urgence nouvelle : ne jamais rien donner de trop "
  "gros, quoi qu'on leur promette en &eacute;change.")

p("Elle repense, en refermant la lettre, &agrave; tout le "
  "chemin parcouru depuis cette premi&egrave;re rencontre "
  "adolescente avec le vieil homme du coteau &mdash; la "
  "publication de son premier roman inspir&eacute; de leur "
  "histoire commune, accueilli avec une tendresse "
  "critique inattendue par quelques lecteurs "
  "perspicaces qui n'avaient jamais soup&ccedil;onn&eacute; &agrave; quel "
  "point la fiction puisait dans une v&eacute;rit&eacute; enti&egrave;re.")

p("Le succ&egrave;s modeste mais r&eacute;el de ce premier livre "
  "lui avait permis, l'ann&eacute;e suivante, de publier un "
  "second roman, davantage centr&eacute; sur le personnage "
  "de Templier lui-m&ecirc;me, transform&eacute; en fiction sous "
  "un nom d'emprunt, et elle se souvient encore de "
  "l'&eacute;motion particuli&egrave;re ressentie en recevant, "
  "quelques semaines apr&egrave;s la publication, un message "
  "d'une lectrice se pr&eacute;sentant simplement comme "
  "&laquo;&nbsp;une descendante &eacute;loign&eacute;e d'une famille "
  "vigneronne&nbsp;&raquo;, la remerciant d'avoir su capturer, "
  "sans jamais l'avoir rencontr&eacute;, l'essence exacte "
  "d'un certain type d'homme discret et courageux.")

p("Alex, de son c&ocirc;t&eacute;, avait achev&eacute; ses &eacute;tudes "
  "d'ing&eacute;nierie avec une mention tr&egrave;s bien, sp&eacute;cialis&eacute; "
  "finalement dans la s&eacute;curit&eacute; informatique plut&ocirc;t que "
  "dans le d&eacute;veloppement pur, une orientation qu'il "
  "attribuait volontiers, dans les conversations "
  "privées avec Clara, &agrave; ce d&eacute;sir jamais &eacute;teint de "
  "comprendre exactement ce qui avait pu causer la "
  "d&eacute;faillance fatale du casque de Darius, sans jamais "
  "totalement r&eacute;ussir &agrave; classer cette question dans la "
  "case des myst&egrave;res r&eacute;solus.")

p("Il avait &eacute;galement, au fil des ann&eacute;es, d&eacute;velopp&eacute; une "
  "expertise discr&egrave;te mais r&eacute;elle en cybers&eacute;curit&eacute; "
  "appliqu&eacute;e aux syst&egrave;mes anciens, une comp&eacute;tence "
  "qui lui avait permis, &agrave; deux reprises d&eacute;j&agrave;, "
  "d'analyser des fichiers de configuration r&eacute;seau "
  "similaires &agrave; celui trouv&eacute; jadis chez les Vasseur, "
  "sans jamais parvenir cependant &agrave; localiser "
  "pr&eacute;cis&eacute;ment le si&egrave;ge central de l'organisation "
  "qu'ils soup&ccedil;onnaient d&eacute;sormais s'&eacute;tendre bien "
  "au-del&agrave; des fronti&egrave;res fran&ccedil;aises.")

p("&Eacute;milie, la petite s&oelig;ur d'Alex, avait grandi sans "
  "jamais manifester de signe suppl&eacute;mentaire "
  "d'appartenance &agrave; la lign&eacute;e des porteurs, se "
  "d&eacute;veloppant en une adolescente parfaitement "
  "ordinaire, passionn&eacute;e de danse contemporaine "
  "plut&ocirc;t que de myst&egrave;res anciens, ce qui rassurait "
  "Alex plus qu'il ne l'aurait jamais admis "
  "ouvertement, m&ecirc;me si une part de lui restait, "
  "&eacute;ternellement, vigilante au moindre signe "
  "&eacute;ventuel.")

p("Franck, quant &agrave; lui, avait fini par accepter, "
  "apr&egrave;s de longues ann&eacute;es de r&eacute;sistance int&eacute;rieure, "
  "l'invitation r&eacute;p&eacute;t&eacute;e de sa compagne &agrave; l'&eacute;pouser, "
  "une petite c&eacute;r&eacute;monie intime organis&eacute;e dans le "
  "jardin de la maison du coteau, entour&eacute; uniquement "
  "de Clara, d'Alex et de quelques proches, sans jamais "
  "oublier, dans son discours de mari&eacute;, de mentionner "
  "son fils disparu comme la personne qui lui avait "
  "appris, le premier, &agrave; oser encore esp&eacute;rer.")

name("FRANCK")
p("&laquo;&nbsp;Darius m'a appris, dans le peu de temps qu'on "
  "a eu ensemble, que continuer &agrave; vivre pleinement "
  "n'est pas une trahison envers ceux qu'on a perdus. "
  "C'est peut-&ecirc;tre, au contraire, la meilleure fa&ccedil;on de "
  "leur rendre hommage.&nbsp;&raquo;")

p("Ces ann&eacute;es de reconstruction progressive, "
  "ponctu&eacute;es de petites victoires personnelles et de "
  "chagrins toujours pr&eacute;sents en filigrane, avaient "
  "forg&eacute; chez les trois survivants une r&eacute;silience "
  "particuli&egrave;re, une capacit&eacute; &agrave; porter simultan&eacute;ment "
  "le poids du pass&eacute; et l'&eacute;lan n&eacute;cessaire vers l'avenir, "
  "qui allait s'av&eacute;rer, cette veille du seize f&eacute;vrier, "
  "plus pr&eacute;cieuse encore qu'ils ne pouvaient "
  "l'imaginer.")

p("La compagne de Franck, une institutrice &agrave; la "
  "retraite pr&eacute;nomm&eacute;e Sylvie, rencontr&eacute;e par hasard "
  "lors d'un vide-grenier organis&eacute; sur la place de "
  "Luynes quelques ann&eacute;es plus t&ocirc;t, s'&eacute;tait "
  "int&eacute;gr&eacute;e progressivement &agrave; cette petite famille "
  "recompos&eacute;e avec une d&eacute;licatesse remarquable, "
  "prenant soin, d&egrave;s les premiers mois de leur "
  "relation, de ne jamais chercher &agrave; remplacer une "
  "quelconque figure maternelle aupr&egrave;s de Clara ou "
  "d'Alex, mais plut&ocirc;t &agrave; occuper, humblement, une "
  "place qui lui &eacute;tait propre.")

name("SYLVIE")
p("&laquo;&nbsp;Franck m'a tout racont&eacute;, vous savez, depuis "
  "longtemps d&eacute;j&agrave;. Toute l'histoire, m&ecirc;me les "
  "parties les plus incroyables. Je sais pas si "
  "j'aurais cru &ccedil;a venant de n'importe qui d'autre, "
  "mais avec tout ce que j'ai vu de sa transformation "
  "depuis qu'il a commenc&eacute; &agrave; vraiment vous "
  "&eacute;couter, vous et Darius, j'ai plus aucun doute "
  "sur la v&eacute;racit&eacute; de tout &ccedil;a.&nbsp;&raquo;")

p("Cette acceptation totale et sans r&eacute;serve de la part "
  "de Sylvie avait repr&eacute;sent&eacute;, pour Clara comme pour "
  "Alex, un soulagement consid&eacute;rable, leur permettant "
  "d'int&eacute;grer cette nouvelle pr&eacute;sence dans leur "
  "cercle familial &eacute;largi sans avoir &agrave; ma&icirc;triser "
  "constamment leurs propos ou &agrave; dissimuler une part "
  "essentielle de leur v&eacute;cu commun, un luxe rare "
  "qu'ils appr&eacute;cient chaque jour un peu plus.")

p("Le coffre contenant l'ensemble des preuves "
  "accumul&eacute;es au fil des ann&eacute;es avait &eacute;t&eacute;, &agrave; la "
  "demande expresse de Franck, pr&eacute;sent&eacute; ouvertement "
  "&agrave; Sylvie peu apr&egrave;s leur mariage, cette derni&egrave;re "
  "acceptant, sans la moindre h&eacute;sitation visible, de "
  "participer d&eacute;sormais &agrave; sa mani&egrave;re &agrave; cette veille "
  "collective, ajoutant m&ecirc;me, gr&acirc;ce &agrave; ses "
  "comp&eacute;tences p&eacute;dagogiques, une m&eacute;thode "
  "d'organisation plus rigoureuse encore &agrave; "
  "l'ensemble des documents rassembl&eacute;s.")

p("Sylvie, forte de son exp&eacute;rience d'enseignante, "
  "propose m&ecirc;me, quelques mois apr&egrave;s son mariage, "
  "de cr&eacute;er un syst&egrave;me de classement num&eacute;rot&eacute; pour "
  "l'ensemble des documents du coffre, chaque pi&egrave;ce "
  "recevant d&eacute;sormais une cote pr&eacute;cise permettant de "
  "la retrouver instantan&eacute;ment parmi les centaines de "
  "pages accumul&eacute;es depuis le d&eacute;but de cette longue "
  "enqu&ecirc;te familiale.")

name("SYLVIE")
p("&laquo;&nbsp;J'ai toujours &eacute;t&eacute; organis&eacute;e comme &ccedil;a, m&ecirc;me "
  "avec mes copies d'&eacute;l&egrave;ves. &Ccedil;a me rassure de "
  "savoir que si un jour quelqu'un a besoin de "
  "retrouver un document pr&eacute;cis rapidement, il pourra "
  "le faire sans avoir &agrave; tout retourner. C'est ma "
  "petite contribution &agrave; cette histoire qui me "
  "d&eacute;passe un peu, je dois l'avouer.&nbsp;&raquo;")

p("Clara, touch&eacute;e par cette implication sinc&egrave;re "
  "d'une personne qui n'a pourtant vécu aucun des "
  "&eacute;v&eacute;nements extraordinaires racont&eacute;s dans ces "
  "documents, remercie chaleureusement Sylvie pour "
  "cette contribution pr&eacute;cieuse, mesurant, une fois de "
  "plus, &agrave; quel point leur petit cercle de confiance "
  "s'est &eacute;largi, avec le temps, bien au-del&agrave; du trio "
  "original form&eacute; avec Darius des ann&eacute;es plus t&ocirc;t.")

p("&Eacute;milie, invit&eacute;e elle aussi &agrave; d&eacute;couvrir "
  "progressivement, au fil de son adolescence, "
  "l'existence de ce coffre familial sans pour autant "
  "en conna&icirc;tre tous les d&eacute;tails les plus troublants, "
  "d&eacute;veloppe &agrave; son tour un attachement discret &agrave; "
  "cette histoire qui pr&eacute;c&egrave;de sa propre naissance, "
  "posant parfois des questions candides que Franck "
  "et Alex g&egrave;rent avec une prudence bienveillante, "
  "toujours soucieux de ne pas lui r&eacute;v&eacute;ler davantage "
  "que ce qu'elle est pr&ecirc;te &agrave; entendre.")

name("&Eacute;MILIE")
p("&laquo;&nbsp;C'est vrai qu'il y avait un gar&ccedil;on avant moi "
  "qui s'appelait Darius et qui &eacute;tait super courageux ? "
  "Papa m'en parle jamais vraiment, mais j'ai "
  "l'impression que c'est important pour toute la "
  "famille.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;Oui, c'est vrai. C'&eacute;tait mon meilleur ami, et "
  "il &eacute;tait effectivement tr&egrave;s courageux. Un jour, "
  "quand tu seras plus grande, je te raconterai tout, "
  "promis. Pour l'instant, retiens juste &ccedil;a &mdash; il "
  "&eacute;tait quelqu'un de bien, et il nous manque "
  "&eacute;norm&eacute;ment.&nbsp;&raquo;")

p("Cette promesse, faite avec tendresse &agrave; sa petite "
  "s&oelig;ur encore trop jeune pour tout comprendre, "
  "pèse sur Alex comme une responsabilit&eacute; "
  "suppl&eacute;mentaire qu'il accepte n&eacute;anmoins "
  "volontiers, conscient qu'un jour, peut-&ecirc;tre plus "
  "t&ocirc;t qu'il ne le souhaiterait, il devra effectivement "
  "tout r&eacute;v&eacute;ler &agrave; &Eacute;milie, quelles qu'en soient les "
  "cons&eacute;quences pour elle.")

p("Clara, t&eacute;moin de cet &eacute;change tendre entre le "
  "fr&egrave;re et la s&oelig;ur, ressent une pointe de "
  "m&eacute;lancolie en pensant &agrave; sa propre situation "
  "familiale, fille unique depuis toujours, priv&eacute;e de "
  "cette dynamique fraternelle qu'elle observe avec "
  "une tendresse non d&eacute;pourvue d'envie chez son "
  "meilleur ami et sa petite s&oelig;ur.")

name("CLARA")
p("&laquo;&nbsp;J'ai toujours un peu envi&eacute; &ccedil;a, cette "
  "relation entre vous deux. J'aurais bien aim&eacute; "
  "avoir un fr&egrave;re ou une s&oelig;ur, moi aussi, quelqu'un "
  "avec qui partager tout &ccedil;a de l'int&eacute;rieur d'une "
  "m&ecirc;me famille.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;T'as Darius et moi, Clara. On est peut-&ecirc;tre "
  "pas du m&ecirc;me sang, mais franchement, apr&egrave;s tout "
  "ce qu'on a travers&eacute; ensemble, je vois pas trop "
  "quelle diff&eacute;rence &ccedil;a ferait avec une vraie "
  "fratrie.&nbsp;&raquo;")

p("Cette affirmation sinc&egrave;re, touchant profond&eacute;ment "
  "Clara, r&eacute;sume &agrave; elle seule la nature exacte du "
  "lien exceptionnel qui unit ces trois amis depuis "
  "l'enfance, une fraternit&eacute; choisie plut&ocirc;t "
  "qu'impos&eacute;e par le sang, mais tout aussi solide et "
  "durable, capable de traverser m&ecirc;me l'&eacute;preuve la "
  "plus terrible qu'ils aient jamais eu &agrave; affronter "
  "ensemble.")

p("&Eacute;milie, quelques ann&eacute;es plus tard, en grandissant "
  "davantage, finit par recevoir de la part d'Alex "
  "et de Clara un r&eacute;cit complet de l'histoire de "
  "Darius, jug&eacute;e enfin assez m&ucirc;re pour entendre la "
  "v&eacute;rit&eacute; enti&egrave;re, et accueille cette r&eacute;v&eacute;lation "
  "avec une gravit&eacute; et une compr&eacute;hension qui "
  "surprennent agr&eacute;ablement son grand fr&egrave;re, "
  "habitu&eacute; &agrave; la voir encore comme une enfant "
  "malgr&eacute; ses seize ans d&eacute;sormais r&eacute;volus.")

name("&Eacute;MILIE")
p("&laquo;&nbsp;Merci de me faire confiance avec &ccedil;a, "
  "Alex. Je comprends pourquoi vous avez attendu "
  "aussi longtemps pour me le dire. C'est &eacute;norme, "
  "comme histoire. Je suis fi&egrave;re de faire partie "
  "d'une famille qui a v&eacute;cu quelque chose d'aussi "
  "important, m&ecirc;me si &ccedil;a fait mal d'entendre tout "
  "&ccedil;a.&nbsp;&raquo;")

p("Elle demande, apr&egrave;s un long silence de "
  "digestion, &agrave; voir de ses propres yeux les "
  "preuves conserv&eacute;es dans le coffre familial, et "
  "Alex, apr&egrave;s une h&eacute;sitation compr&eacute;hensible, "
  "accepte de lui montrer le pon&ccedil;on grav&eacute; d'un "
  "&laquo;&nbsp;K.&nbsp;&raquo;, le laissant le tenir dans ses mains "
  "avec le m&ecirc;me respect presque religieux que "
  "lui-m&ecirc;me avait appris &agrave; lui accorder des ann&eacute;es "
  "plus t&ocirc;t.")

p("&Eacute;milie, tenant cet objet charg&eacute; d'histoire entre "
  "ses doigts, ressent un frisson qu'elle ne saurait "
  "expliquer rationnellement, une sensation fugace "
  "mais r&eacute;elle de connexion avec cette histoire "
  "familiale qui la pr&eacute;c&egrave;de, et repose finalement "
  "l'objet avec une gravit&eacute; nouvelle, comprenant "
  "d&eacute;sormais, dans sa chair autant que dans son "
  "esprit, l'ampleur r&eacute;elle de ce que sa famille a "
  "travers&eacute; bien avant sa propre naissance.")

p("Elle promet, ce jour-l&agrave;, de garder pr&eacute;cieusement "
  "ce secret familial aussi longtemps que "
  "n&eacute;cessaire, rejoignant ainsi, sans le savoir "
  "encore pleinement, le cercle restreint de ceux "
  "qui portent, chacun &agrave; sa mani&egrave;re, la m&eacute;moire "
  "vivante de Darius et de tout ce qu'il a "
  "accompli durant sa br&egrave;ve mais extraordinaire "
  "existence.")

p("Alex, observant sa petite s&oelig;ur refermer "
  "d&eacute;licatement le coffre familial ce jour-l&agrave;, "
  "ressent une fiert&eacute; immense &agrave; la voir accueillir "
  "cette v&eacute;rit&eacute; complexe avec autant de maturit&eacute; "
  "et de gr&acirc;ce, et se dit que Darius, o&ugrave; qu'il se "
  "trouve d&eacute;sormais, aurait probablement approuv&eacute; "
  "cette d&eacute;cision de faire enfin confiance &agrave; la "
  "nouvelle g&eacute;n&eacute;ration avec l'histoire compl&egrave;te de "
  "leur famille &eacute;largie.")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 10 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 11 -- LE DOMAINE VASSEUR
# ======================================================================
chap(11, "LE DOMAINE VASSEUR")

p("Le seize f&eacute;vrier suivant, Clara, Alex et Franck se "
  "retrouvent devant la m&ecirc;me grille rouill&eacute;e de la propri&eacute;t&eacute; "
  "Vasseur &agrave; Fondettes, plus de dix ans apr&egrave;s leur premi&egrave;re "
  "visite adolescente, constatant avec surprise que la haie "
  "immense a &eacute;t&eacute; r&eacute;cemment taill&eacute;e, la grille huil&eacute;e, "
  "l'all&eacute;e d&eacute;sherb&eacute;e, comme si quelqu'un, r&eacute;cemment, "
  "avait discr&egrave;tement entrepris de redonner vie &agrave; ce lieu "
  "longtemps laiss&eacute; &agrave; l'abandon.")

name("FRANCK")
p("&laquo;&nbsp;C'est plus du tout comme la derni&egrave;re fois. On "
  "dirait presque que quelqu'un les attendait, cette "
  "visite. &Ccedil;a me pla&icirc;t pas du tout, cette pr&eacute;paration "
  "aussi soign&eacute;e.&nbsp;&raquo;")

p("Ils avancent prudemment dans l'all&eacute;e, remarquant "
  "d'autres voitures gar&eacute;es plus loin, discr&egrave;tement r&eacute;parties "
  "le long du chemin, sugg&eacute;rant que d'autres visiteurs, "
  "invisibles pour l'instant, ont d&eacute;j&agrave; r&eacute;pondu, eux aussi, &agrave; "
  "une invitation similaire &agrave; celle re&ccedil;ue par Franck.")

p("La porte d'entr&eacute;e, autrefois branlante, s'ouvre "
  "d&eacute;sormais sans effort sur un int&eacute;rieur enti&egrave;rement "
  "r&eacute;nov&eacute;, les meubles jadis recouverts de draps blancs "
  "d&eacute;sormais expos&eacute;s, restaur&eacute;s, comme si la maison "
  "enti&egrave;re avait &eacute;t&eacute; ramen&eacute;e &agrave; la vie apr&egrave;s des "
  "d&eacute;cennies de sommeil, et un homme d'&acirc;ge m&ucirc;r, "
  "&eacute;l&eacute;gant, les accueille dans le hall avec un calme "
  "parfaitement professionnel qui glace instantan&eacute;ment "
  "Clara.")

name("A. VASSEUR")
p("&laquo;&nbsp;Monsieur Lenoir. Mademoiselle. Monsieur. Merci "
  "d'&ecirc;tre venus. Je m'appelle Ambroise Vasseur. Je suis, "
  "je suppose, ce qu'on pourrait appeler le dernier "
  "administrateur en titre de l'h&eacute;ritage de mon "
  "grand-p&egrave;re. Suivez-moi, je vous prie, les autres "
  "vous attendent d&eacute;j&agrave; dans le jardin d'hiver.&nbsp;&raquo;")

p("Le mot &laquo;&nbsp;les autres&nbsp;&raquo; r&eacute;sonne d&eacute;sagr&eacute;ablement dans "
  "l'esprit de Clara, qui &eacute;change un regard inquiet avec "
  "Alex, tous deux se demandant silencieusement combien "
  "de personnes, exactement, cette invitation a bien pu "
  "convier, et dans quel but pr&eacute;cis un homme se pr&eacute;sentant "
  "comme le petit-fils du docteur Vasseur a-t-il choisi de "
  "les faire venir pr&eacute;cis&eacute;ment ce jour anniversaire "
  "particulier.")

p("Ils traversent un couloir richement r&eacute;am&eacute;nag&eacute;, dont "
  "les murs, autrefois nus, affichent d&eacute;sormais une "
  "collection impressionnante de photographies encadr&eacute;es "
  "&mdash; des dizaines de visages, certains anciens, en noir et "
  "blanc, d'autres beaucoup plus r&eacute;cents, tous accompagn&eacute;s "
  "d'une simple &eacute;tiquette manuscrite portant un pr&eacute;nom et "
  "une plage d'ann&eacute;es, et Darius s'arr&ecirc;te net en "
  "reconnaissant, vers la fin de cette galerie, le propre "
  "visage de son fils, souriant sur une photographie de "
  "classe qu'il n'avait jamais vue circuler ailleurs.")

name("FRANCK")
p("&laquo;&nbsp;C'est Darius. Comment vous avez eu &ccedil;a. Comment "
  "vous avez seulement pu avoir une photo de mon "
  "fils.&nbsp;&raquo;")

name("A. VASSEUR")
p("&laquo;&nbsp;Nous documentons chaque porteur, Monsieur "
  "Lenoir, depuis toujours. C'est notre rôle, depuis des "
  "g&eacute;n&eacute;rations. Pas pour leur nuire. Pour t&eacute;moigner. "
  "Venez, je vous en prie, tout s'expliquera bient&ocirc;t. Ne "
  "craignez rien.&nbsp;&raquo;")

p("Le jardin d'hiver, une vaste v&eacute;randa vitr&eacute;e adoss&eacute;e &agrave; "
  "l'arri&egrave;re de la propri&eacute;t&eacute;, accueille effectivement une "
  "assembl&eacute;e bien plus nombreuse que ce qu'aucun des "
  "trois n'avait anticip&eacute; &mdash; une vingtaine de personnes "
  "environ, d'&acirc;ges tr&egrave;s divers, certaines &acirc;g&eacute;es, d'autres "
  "&agrave; peine plus vieilles que Clara et Alex, toutes "
  "silencieuses, install&eacute;es en cercle autour d'une simple "
  "table sur laquelle repose, seul objet visible, un unique "
  "pon&ccedil;on grav&eacute; d'une lettre qu'aucun d'eux ne reconna&icirc;t "
  "imm&eacute;diatement.")

name("A. VASSEUR")
p("&laquo;&nbsp;Chacune des personnes ici pr&eacute;sentes a, &agrave; un "
  "moment de son existence, port&eacute; ce que vous appelez "
  "la Marge, ou en a &eacute;t&eacute; le t&eacute;moin le plus proche &mdash; "
  "un fr&egrave;re, une s&oelig;ur, un parent, un ami. Nous les "
  "retrouvons, patiemment, depuis des d&eacute;cennies. Pas "
  "pour les exploiter. Pour les r&eacute;unir, enfin, et "
  "documenter ensemble ce qui n'a jamais &eacute;t&eacute; racont&eacute; "
  "correctement.&nbsp;&raquo;")

p("Clara reconna&icirc;t, parmi l'assembl&eacute;e, une femme &acirc;g&eacute;e "
  "dont les traits lui rappellent &eacute;trangement ceux de "
  "Templier, et comprend, avec un choc silencieux, qu'il "
  "doit s'agir de la petite s&oelig;ur disparue en 1979, "
  "retrouv&eacute;e depuis, d'une mani&egrave;re ou d'une autre, "
  "peut-&ecirc;tre jamais totalement perdue apr&egrave;s tout.")

name("FEMME &Acirc;G&Eacute;E")
p("&laquo;&nbsp;Je m'appelle Odile. J'ai &eacute;t&eacute; la Marge de mon "
  "fr&egrave;re, pendant quarante ans, avant de finir par "
  "trouver, moi aussi, un chemin de retour, partiel, "
  "incomplet, mais r&eacute;el. &Ccedil;a arrive plus souvent que vous "
  "ne croyez. La dissolution n'est jamais tout &agrave; fait "
  "d&eacute;finitive, pour personne.&nbsp;&raquo;")

p("Cette r&eacute;v&eacute;lation frappe Clara et Alex de plein fouet, "
  "tous deux pensant imm&eacute;diatement &agrave; Kayden, &agrave; sa "
  "dissolution jamais confirm&eacute;e, &agrave; cette voix entendue "
  "encore parfois dans le carnet ou dans le vent, et &agrave; "
  "l'espoir fou, jamais totalement &eacute;teint, qu'une part de "
  "lui subsiste encore, quelque part, capable un jour, "
  "peut-&ecirc;tre, de retrouver elle aussi un semblant de "
  "chemin.")

name("A. VASSEUR")
p("&laquo;&nbsp;Nous ne cherchons pas &agrave; provoquer un nouveau "
  "sacrifice, Monsieur Lenoir. Nous cherchons, au "
  "contraire, &agrave; comprendre suffisamment cette force pour "
  "qu'elle cesse, un jour, d'exiger quoi que ce soit de "
  "qui que ce soit. C'est le travail de toute une vie, "
  "voire de plusieurs vies. Votre fils y a &eacute;norm&eacute;ment "
  "contribu&eacute;, sans le savoir, par son courage. Nous "
  "voulions simplement vous en remercier, en personne, "
  "et vous inviter, si vous le souhaitez, &agrave; rejoindre "
  "notre travail plut&ocirc;t que de continuer &agrave; le craindre "
  "dans l'ombre.&nbsp;&raquo;")

p("Franck, boulevers&eacute; par cette d&eacute;claration inattendue, "
  "reste longtemps silencieux, incapable de d&eacute;cider si "
  "cette main tendue repr&eacute;sente enfin une v&eacute;ritable "
  "r&eacute;conciliation avec l'histoire familiale qui l'a "
  "poursuivi toute sa vie, ou une manipulation plus "
  "raffin&eacute;e encore que tout ce qu'ils avaient connu "
  "jusqu'alors.")

p("Clara, tout en &eacute;coutant attentivement les explications "
  "d'Ambroise Vasseur, remarque un d&eacute;tail qui la trouble "
  "profond&eacute;ment sans qu'elle parvienne, sur le moment, &agrave; "
  "en identifier pr&eacute;cis&eacute;ment la cause &mdash; chacun des "
  "membres de l'assembl&eacute;e, en l'&eacute;coutant parler, hoche la "
  "t&ecirc;te avec un ensemble parfait, un synchronisme "
  "presque m&eacute;canique qui ne ressemble &agrave; aucune "
  "attention humaine ordinaire.")

p("Elle observe plus attentivement Odile, cette femme "
  "&acirc;g&eacute;e se pr&eacute;sentant comme la s&oelig;ur retrouv&eacute;e de "
  "Templier, et remarque, avec un frisson glac&eacute;, que ses "
  "yeux, dans certaines conditions de lumi&egrave;re, semblent "
  "capter un &eacute;clat l&eacute;g&egrave;rement bleu&acirc;tre, exactement "
  "identique &agrave; celui aper&ccedil;u l'ann&eacute;e pr&eacute;c&eacute;dente au "
  "cimeti&egrave;re, exactement identique &agrave; celui d&eacute;crit par "
  "Darius &agrave; propos du Non-lieu.")

name("CLARA")
p("&laquo;&nbsp;Alex. Regarde leurs yeux, discr&egrave;tement. Tous, "
  "pas juste elle. Je crois pas qu'on est vraiment face &agrave; "
  "des gens ordinaires qui ont juste crois&eacute; cette histoire "
  "un jour. Je crois qu'on est face &agrave; des gens qui "
  "portent, tous, un petit bout de la m&ecirc;me chose que "
  "Kayden portait.&nbsp;&raquo;")

p("Alex, en observant &agrave; son tour, sent sa propre "
  "cicatrice se r&eacute;veiller brutalement, une br&ucirc;lure intense "
  "remontant tout le long de son avant-bras, plus forte "
  "que jamais auparavant, comme si la simple proximit&eacute; "
  "de cette assembl&eacute;e r&eacute;activait, d'un coup, un lien "
  "qu'il croyait pourtant &eacute;teint depuis des ann&eacute;es.")

name("A. VASSEUR")
p("&laquo;&nbsp;Vous avez l'&oelig;il fin, Mademoiselle. Oui, nous "
  "portons tous, &agrave; des degr&eacute;s divers, une part de ce que "
  "vous appelez Kayden, ou la Marge, ou le Non-lieu. "
  "Nous ne le combattons pas. Nous avons appris, avec "
  "le temps, &agrave; cohabiter avec, &agrave; le canaliser, &agrave; "
  "l'accueillir plut&ocirc;t qu'&agrave; le repousser. C'est peut-&ecirc;tre "
  "la seule vraie diff&eacute;rence entre nous et le docteur "
  "Vasseur, en fin de compte.&nbsp;&raquo;")

p("Cette explication, prononc&eacute;e avec un calme "
  "parfaitement rassurant, ne fait qu'accro&icirc;tre l'inqui&eacute;tude "
  "de Franck, qui sent, pour la premi&egrave;re fois depuis leur "
  "arriv&eacute;e, un profond malaise physique l'envahir, comme "
  "si son propre corps, marqu&eacute; enfant par le m&ecirc;me "
  "programme, reconnaissait instinctivement un danger "
  "que son esprit rationnel peinait encore &agrave; nommer "
  "clairement.")

p("Ambroise Vasseur, sentant visiblement leur "
  "appr&eacute;hension grandissante, l&egrave;ve une main apaisante et "
  "reprend la parole avec cette m&ecirc;me douceur "
  "professionnelle qui n'a jamais tout &agrave; fait quitt&eacute; sa "
  "voix depuis leur arriv&eacute;e, comme s'il avait r&eacute;p&eacute;t&eacute; ce "
  "discours des centaines de fois &agrave; des visiteurs "
  "diff&eacute;rents au fil des ann&eacute;es.")

name("A. VASSEUR")
p("&laquo;&nbsp;Nous ne vous demandons rien aujourd'hui, "
  "rassurez-vous. Simplement de savoir que cette porte "
  "vous reste ouverte, si un jour vous souhaitez "
  "comprendre davantage, ou si &Eacute;milie, un jour, en "
  "venait &agrave; avoir besoin de r&eacute;ponses que personne "
  "d'autre ne pourra lui offrir. Nous serons l&agrave;. Nous "
  "sommes toujours l&agrave;, en r&eacute;alit&eacute;, depuis tr&egrave;s "
  "longtemps.&nbsp;&raquo;")

p("Il leur remet, avant de les raccompagner vers la "
  "sortie, une simple carte grav&eacute;e d'un unique num&eacute;ro de "
  "t&eacute;l&eacute;phone, sans nom associ&eacute;, leur assurant qu'elle "
  "restera fonctionnelle ind&eacute;finiment, quoi qu'il arrive, "
  "pour quiconque de leur petit groupe souhaiterait un "
  "jour reprendre contact, et Clara la glisse dans sa "
  "poche avec une r&eacute;pulsion contenue, incapable de "
  "d&eacute;cider si ce geste repr&eacute;sente une v&eacute;ritable main "
  "tendue ou simplement une laisse suppl&eacute;mentaire "
  "discr&egrave;tement pass&eacute;e autour de leurs vies.")

p("Ils quittent la propri&eacute;t&eacute; en fin d'apr&egrave;s-midi, le soleil "
  "d&eacute;j&agrave; bas sur l'horizon, sans qu'aucun d'eux ne "
  "parvienne &agrave; formuler clairement, sur le trajet du "
  "retour, s'ils viennent de vivre une v&eacute;ritable "
  "r&eacute;conciliation avec cette histoire ou simplement une "
  "nouvelle &eacute;tape, plus sophistiqu&eacute;e, d'une surveillance "
  "qui ne s'est jamais vraiment interrompue.")

name("ALEX")
p("&laquo;&nbsp;J'sais pas quoi penser de tout &ccedil;a, honn&ecirc;tement. "
  "Ils avaient l'air sinc&egrave;res. Mais Templier disait "
  "toujours de jamais faire confiance trop vite &agrave; ce "
  "genre de promesse. J'ai l'impression qu'on vient "
  "juste d'ouvrir une porte qu'on pourra plus jamais "
  "refermer compl&egrave;tement.&nbsp;&raquo;")

p("Franck, silencieux durant tout le trajet, se contente "
  "de garder les yeux fix&eacute;s sur la route, la carte "
  "t&eacute;l&eacute;phonique donn&eacute;e par Ambroise Vasseur pos&eacute;e sur "
  "le tableau de bord, incapable de d&eacute;cider, lui non "
  "plus, si cette rencontre marque la fin d'un chapitre "
  "ou l'ouverture d'un autre, plus vaste et plus "
  "incertain encore que tout ce qu'ils avaient travers&eacute; "
  "jusqu'ici.")

p("Avant de les laisser repartir, Franck, rassemblant un "
  "courage qu'il ne se connaissait pas encore ce matin-l&agrave;, "
  "retient Ambroise Vasseur par la manche, refusant de "
  "quitter cette maison sans avoir pos&eacute; la question qui le "
  "hante depuis le d&eacute;but de la visite, depuis bien plus "
  "longtemps en r&eacute;alit&eacute;, depuis cette enfance effac&eacute;e "
  "qu'il n'a jamais totalement retrouv&eacute;e.")

name("FRANCK")
p("&laquo;&nbsp;Vous savez ce qui est arriv&eacute; &agrave; mon fr&egrave;re. &Agrave; "
  "Kayden. Vous devez le savoir, vous documentez tout, "
  "vous l'avez dit vous-m&ecirc;me. Alors dites-moi, "
  "franchement, une bonne fois pour toutes &mdash; est-ce "
  "qu'il existe encore, quelque part ? Est-ce que mon "
  "fr&egrave;re est vraiment mort, ce jour-l&agrave;, dans le "
  "Non-lieu, ou est-ce qu'il continue, d'une mani&egrave;re ou "
  "d'une autre, &agrave; exister encore ?&nbsp;&raquo;")

p("Ambroise Vasseur marque une longue pause avant de "
  "r&eacute;pondre, choisissant visiblement ses mots avec un "
  "soin particulier, conscient du poids que cette r&eacute;ponse "
  "repr&eacute;sente pour l'homme qui lui fait face, fils "
  "d'un p&egrave;re qu'il n'a jamais totalement connu et fr&egrave;re "
  "d'un fant&ocirc;me qu'il n'a jamais pu pleurer correctement.")

name("A. VASSEUR")
p("&laquo;&nbsp;La v&eacute;rit&eacute; honn&ecirc;te, Monsieur Lenoir, c'est que "
  "personne ne sait vraiment. Il y a des fragments, "
  "encore, dispers&eacute;s dans ce que le programme a laiss&eacute; "
  "derri&egrave;re lui. Odile, l&agrave;, a retrouv&eacute; un chemin "
  "presque complet vers elle-m&ecirc;me apr&egrave;s quarante "
  "ans. D'autres n'y arrivent jamais. Votre fr&egrave;re &eacute;tait "
  "particuli&egrave;rement... dilu&eacute;, si je puis dire, apr&egrave;s ce "
  "que votre fils a accompli dans le Non-lieu. Mais "
  "dilu&eacute; n'est pas la m&ecirc;me chose qu'&eacute;teint.&nbsp;&raquo;")

p("Cette r&eacute;ponse, &agrave; la fois honn&ecirc;te et douloureusement "
  "incompl&egrave;te, arrache &agrave; Franck des larmes qu'il ne "
  "cherche m&ecirc;me plus &agrave; retenir, un m&eacute;lange de chagrin "
  "et d'un espoir t&eacute;nu, presque insupportable &agrave; porter "
  "apr&egrave;s tant d'ann&eacute;es &agrave; croire son fr&egrave;re "
  "d&eacute;finitivement perdu.")

name("FRANCK")
p("&laquo;&nbsp;S'il reste quelque chose de lui, quelque part... "
  "dites-lui, si jamais vous trouvez un moyen de "
  "communiquer avec &ccedil;a un jour... dites-lui que je lui "
  "en veux plus. Que j'ai jamais vraiment pu, en fait, "
  "malgr&eacute; tout ce qu'il a fait. C'&eacute;tait mon grand fr&egrave;re. "
  "&Ccedil;a s'efface pas, &ccedil;a, m&ecirc;me apr&egrave;s tout &ccedil;a.&nbsp;&raquo;")

p("Ambroise Vasseur hoche lentement la t&ecirc;te, promettant, "
  "sans grande conviction apparente, de transmettre ce "
  "message si jamais l'occasion s'en pr&eacute;sentait, et "
  "raccompagne enfin ses visiteurs vers la sortie, "
  "laissant derri&egrave;re lui, dans le jardin d'hiver, une "
  "assembl&eacute;e silencieuse dont Clara et Alex ignorent "
  "encore, en quittant les lieux, qu'elle ne se dispersera "
  "pas comme eux ce soir-l&agrave;.")

p("Clara, en attendant que Franck termine sa conversation "
  "priv&eacute;e avec Ambroise Vasseur, profite de ce moment "
  "d'attente pour observer plus attentivement l'assembl&eacute;e "
  "encore r&eacute;unie dans le jardin d'hiver, cherchant, sans "
  "trop savoir quoi exactement, une confirmation ou une "
  "infirmation de ce malaise diffus qui ne l'a plus "
  "quitt&eacute;e depuis qu'elle a remarqu&eacute; cet &eacute;clat bleu&acirc;tre "
  "dans les yeux d'Odile.")

p("Elle s'approche discr&egrave;tement d'un homme plus jeune, "
  "install&eacute; en retrait du groupe principal, qui n'a "
  "pratiquement pas prononc&eacute; un mot depuis leur arriv&eacute;e, "
  "et engage, &agrave; voix basse, une conversation qu'elle "
  "esp&egrave;re plus sinc&egrave;re que le discours poli d'Ambroise "
  "Vasseur.")

name("CLARA")
p("&laquo;&nbsp;Vous &ecirc;tes ici depuis longtemps ? Dans ce groupe, "
  "je veux dire. Vous avez l'air different des autres, "
  "un peu &agrave; l'&eacute;cart.&nbsp;&raquo;")

name("HOMME DISCRET")
p("&laquo;&nbsp;Cinq ans. Ma m&egrave;re &eacute;tait porteuse, avant moi, "
  "dans une autre r&eacute;gion. Je suis venu ici parce qu'ils "
  "m'ont promis des r&eacute;ponses qu'elle avait jamais eues, "
  "elle. Je vous conseille pas de trop leur faire "
  "confiance trop vite, remarquez. Ils promettent "
  "beaucoup. Ils expliquent moins qu'on voudrait.&nbsp;&raquo;")

p("Cette confidence, glissée rapidement avant que "
  "l'homme ne se referme et rejoigne le reste du "
  "groupe, sans autre explication, ne fait que renforcer "
  "l'inqui&eacute;tude sourde de Clara, qui comprend, &agrave; cet "
  "instant, que ce cercle rassembl&eacute; par Ambroise "
  "Vasseur ne repr&eacute;sente probablement, pour beaucoup "
  "de ses membres, ni une communaut&eacute; de soutien "
  "sinc&egrave;re ni un pi&egrave;ge &eacute;vident, mais quelque chose de "
  "plus trouble encore, entre les deux, dont ni elle ni "
  "personne d'autre ne semble ma&icirc;triser enti&egrave;rement "
  "les contours r&eacute;els.")

p("Profitant d'un instant o&ugrave; Ambroise Vasseur "
  "s'&eacute;loigne pour accueillir de nouveaux arrivants, "
  "Alex entra&icirc;ne discr&egrave;tement Clara vers un couloir "
  "adjacent au jardin d'hiver, curieux de d&eacute;couvrir ce "
  "que cache le reste de cette demeure enti&egrave;rement "
  "r&eacute;nov&eacute;e, si diff&eacute;rente de la maison poussi&eacute;reuse et "
  "abandonn&eacute;e qu'ils avaient visit&eacute;e onze ans plus t&ocirc;t.")

p("Ils d&eacute;couvrent, au bout du couloir, une biblioth&egrave;que "
  "priv&eacute;e enti&egrave;re consacr&eacute;e, de toute &eacute;vidence, &agrave; "
  "l'&eacute;tude de la Marge sous toutes ses formes historiques "
  "&mdash; des ouvrages de folklore r&eacute;gional c&ocirc;toyant des "
  "rapports m&eacute;dicaux confidentiels, des cartes anciennes "
  "de la vall&eacute;e annot&eacute;es de symboles qu'aucun des deux "
  "ne reconna&icirc;t, et, trônant sur un pupitre central, un "
  "exemplaire richement reli&eacute; qui ressemble, &agrave; s'y "
  "m&eacute;prendre, au grimoire de 1962 qu'ils avaient "
  "eux-m&ecirc;mes consult&eacute; &agrave; la biblioth&egrave;que de Luynes.")

name("ALEX")
p("&laquo;&nbsp;Clara, regarde &ccedil;a. C'est exactement le m&ecirc;me "
  "genre d'&eacute;criture que le grimoire qu'on avait trouv&eacute;. "
  "Ils ont d&ucirc; en faire une copie, ou peut-&ecirc;tre m&ecirc;me "
  "que c'est l'original et que celui de la biblioth&egrave;que "
  "&eacute;tait juste une copie destin&eacute;e &agrave; &ecirc;tre trouv&eacute;e.&nbsp;&raquo;")

p("Clara feuillette prudemment l'ouvrage, d&eacute;couvrant "
  "des pages enti&egrave;res consacr&eacute;es &agrave; des porteurs dont "
  "elle n'a jamais entendu parler, chacun r&eacute;sum&eacute; en "
  "quelques lignes denses accompagn&eacute;es d'illustrations "
  "&agrave; la plume repr&eacute;sentant des sc&egrave;nes de sacrifice "
  "vieilles de plusieurs si&egrave;cles, jusqu'&agrave; tomber, vers "
  "la fin de l'ouvrage, sur une page consacr&eacute;e "
  "explicitement &agrave; Darius lui-m&ecirc;me, sa photographie "
  "de classe coll&eacute;e directement sur le papier jauni.")

p("La l&eacute;gende accompagnant cette photographie, r&eacute;dig&eacute;e "
  "d'une main soigneuse et r&eacute;cente, r&eacute;sume en quelques "
  "phrases l'int&eacute;gralit&eacute; du combat men&eacute; par Darius dans "
  "le Non-lieu, avec une pr&eacute;cision troublante qu'aucune "
  "source publique n'aurait jamais pu fournir, "
  "concluant sur une phrase qui glace instantan&eacute;ment "
  "Clara : &laquo;&nbsp;porteur le plus efficace recens&eacute; depuis "
  "le dix-neuvi&egrave;me si&egrave;cle &mdash; a failli, par inadvertance, "
  "compromettre d&eacute;finitivement nos plans.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;'Compromettre nos plans.' Alex, ils "
  "consid&eacute;raient Darius comme un obstacle, pas comme "
  "quelqu'un &agrave; sauver ou &agrave; comprendre. Tout ce discours "
  "d'Ambroise sur la documentation et le t&eacute;moignage, "
  "c'est que des conneries. Ils avaient d&eacute;j&agrave; un plan "
  "bien avant qu'on arrive ici aujourd'hui.&nbsp;&raquo;")

p("Ils entendent, &agrave; cet instant, des pas approcher dans "
  "le couloir, et referment pr&eacute;cipitamment le grimoire "
  "avant de s'&eacute;loigner du pupitre, juste &agrave; temps pour "
  "&eacute;viter d'&ecirc;tre surpris par un membre de l'assembl&eacute;e "
  "venu chercher, dans cette m&ecirc;me biblioth&egrave;que, un "
  "document quelconque n&eacute;cessaire &agrave; la c&eacute;r&eacute;monie qui "
  "se pr&eacute;pare.")

p("Elle retrouve Alex un peu plus loin, occup&eacute; &agrave; "
  "examiner discr&egrave;tement, sans y toucher, une carte "
  "encadr&eacute;e accroch&eacute;e au mur repr&eacute;sentant, avec une "
  "pr&eacute;cision troublante, un r&eacute;seau bien plus vaste que "
  "les sept sites r&eacute;gionaux qu'ils avaient identifi&eacute;s des "
  "ann&eacute;es plus t&ocirc;t &mdash; des dizaines de points lumineux "
  "r&eacute;partis sur l'ensemble du territoire fran&ccedil;ais, et "
  "m&ecirc;me, plus troublant encore, quelques points isol&eacute;s "
  "au-del&agrave; des fronti&egrave;res nationales.")

name("ALEX")
p("&laquo;&nbsp;Clara. Regarde &ccedil;a. C'est pas juste sept sites. "
  "C'est... c'est &eacute;norme. &Ccedil;a veut dire que ce qu'on a "
  "v&eacute;cu &agrave; Luynes, c'&eacute;tait peut-&ecirc;tre juste un tout petit "
  "morceau d'un truc largement plus grand que "
  "n'importe quoi qu'on aurait pu imaginer.&nbsp;&raquo;")

p("Ils n'ont pas le temps d'approfondir cette d&eacute;couverte "
  "vertigineuse avant que Franck, les yeux encore "
  "rougis par l'&eacute;motion de sa conversation avec Ambroise "
  "Vasseur, ne les rejoigne, signalant qu'il est temps, "
  "d&eacute;sormais, de rentrer, et tous trois quittent la "
  "propri&eacute;t&eacute; avec cette carte immense encore grav&eacute;e "
  "dans leur esprit, sans savoir encore &agrave; quel point elle "
  "annonce quelque chose de bien plus vaste que ce que "
  "cette seule soir&eacute;e leur permettra jamais de "
  "comprendre.")

p("Le retour vers Luynes se fait dans un silence presque "
  "total, chacun des trois passagers de la voiture "
  "digérant &agrave; sa mani&egrave;re l'ampleur nouvelle de ce qu'ils "
  "viennent d'entrevoir sur ce mur du jardin d'hiver &mdash; "
  "cette carte immense, ces dizaines de points lumineux "
  "r&eacute;partis bien au-del&agrave; de la seule vall&eacute;e de la Loire, "
  "cette id&eacute;e vertigineuse que leur propre histoire, si "
  "intense et si personnelle depuis l'enfance, ne "
  "repr&eacute;sentait peut-&ecirc;tre qu'une gouttelette dans un oc&eacute;an "
  "bien plus vaste.")

name("ALEX")
p("&laquo;&nbsp;J'arrive m&ecirc;me pas &agrave; imaginer combien de "
  "'Darius' il peut y avoir, en ce moment m&ecirc;me, &agrave; "
  "travers le pays, ou m&ecirc;me plus loin. Combien de "
  "Clara, combien d'Alex, combien de Franck, tous en "
  "train de vivre exactement le m&ecirc;me genre "
  "d'histoire sans jamais se douter qu'on existe, nous "
  "aussi, quelque part.&nbsp;&raquo;")

p("Clara, plong&eacute;e dans ses pens&eacute;es, ressort discr&egrave;tement "
  "son t&eacute;l&eacute;phone et prend quelques notes rapides, "
  "fid&egrave;le &agrave; son habitude de tout consigner m&ecirc;me dans "
  "les moments les plus &eacute;prouvants, esp&eacute;rant fixer, "
  "avant que le souvenir ne s'estompe, chaque d&eacute;tail "
  "pr&eacute;cis de cette carte entraper&ccedil;ue &mdash; la disposition "
  "des points, leur densit&eacute; plus forte autour de certaines "
  "r&eacute;gions, cette impression &eacute;trange que le r&eacute;seau, loin "
  "d'&ecirc;tre statique, semblait au contraire en pleine "
  "expansion r&eacute;cente.")

name("CLARA")
p("&laquo;&nbsp;Y'avait des points qui clignotaient diff&eacute;remment "
  "des autres, vous avez remarqu&eacute; ? Plus vifs, presque "
  "rouges par endroits. Je crois pas que c'&eacute;tait juste "
  "d&eacute;coratif. Je crois que &ccedil;a repr&eacute;sentait un truc "
  "pr&eacute;cis, genre un statut, une &eacute;tape, j'sais pas "
  "trop.&nbsp;&raquo;")

p("Franck, conduisant en silence depuis un moment, "
  "finit par exprimer &agrave; voix haute la question qui les "
  "taraude tous depuis leur d&eacute;part de la propri&eacute;t&eacute; "
  "Vasseur, celle qu'aucun d'eux n'avait encore os&eacute; "
  "formuler clairement malgr&eacute; son &eacute;vidence."
  " ")

name("FRANCK")
p("&laquo;&nbsp;Vous croyez qu'ils pr&eacute;parent quelque chose ? "
  "Genre, activement, maintenant, pas juste "
  "'documenter' comme il dit ? Parce que toute cette "
  "mise en sc&egrave;ne, cette invitation pile le jour "
  "anniversaire, cette assembl&eacute;e immense... &ccedil;a "
  "ressemble pas &agrave; un simple club de soutien entre "
  "anciens porteurs, tout &ccedil;a.&nbsp;&raquo;")

p("Aucun d'eux ne trouve de r&eacute;ponse rassurante &agrave; "
  "apporter &agrave; cette question, et le reste du trajet "
  "s'ach&egrave;ve dans un silence pesant, chacun repassant "
  "mentalement chaque d&eacute;tail de cette journ&eacute;e "
  "extraordinaire, cherchant, sans grand succ&egrave;s, &agrave; "
  "d&eacute;m&ecirc;ler ce qui rel&egrave;ve d'une v&eacute;ritable bienveillance "
  "de ce qui pourrait n'&ecirc;tre, en r&eacute;alit&eacute;, qu'un "
  "pr&eacute;lude &eacute;labor&eacute; &agrave; quelque chose de bien plus "
  "sombre.")

p("Ce que ni Clara, ni Alex, ni Franck ne peuvent savoir, "
  "en roulant vers Luynes ce soir-l&agrave;, c'est que la "
  "propri&eacute;t&eacute; qu'ils viennent de quitter n'est en r&eacute;alit&eacute; "
  "qu'un des multiples si&egrave;ges secondaires d'une "
  "organisation dont l'ampleur v&eacute;ritable d&eacute;passe de tr&egrave;s "
  "loin tout ce qu'Ambroise Vasseur a bien voulu leur "
  "laisser entrevoir &mdash; une organisation patiente, "
  "methodique, dont les racines plongent bien plus "
  "profond&eacute;ment dans l'histoire que le seul programme "
  "de 1991, jusqu'&agrave; cette l&eacute;gende ancienne de la Marge "
  "que Templier lui-m&ecirc;me n'avait jamais compl&egrave;tement "
  "perce.")

p("Dans les mois qui pr&eacute;c&eacute;daient cette rencontre, des "
  "r&eacute;unions similaires &agrave; celle de Fondettes s'&eacute;taient "
  "tenues, avec la m&ecirc;me discr&eacute;tion mesur&eacute;e, dans "
  "plusieurs autres propri&eacute;t&eacute;s &agrave; travers le pays, "
  "chacune rassemblant son propre groupe de porteurs, "
  "d'anciens t&eacute;moins et de familles endeuill&eacute;es, chacune "
  "recevant, &agrave; sa mani&egrave;re, la m&ecirc;me promesse rassurante "
  "de compr&eacute;hension mutuelle et de documentation "
  "partag&eacute;e.")

p("Et dans chacune de ces r&eacute;unions, &agrave; l'instant pr&eacute;cis "
  "o&ugrave; les derniers visiteurs invit&eacute;s quittaient les lieux, "
  "convaincus d'avoir simplement particip&eacute; &agrave; une &eacute;trange "
  "mais inoffensive c&eacute;r&eacute;monie de m&eacute;moire, une m&ecirc;me "
  "question &eacute;tait pos&eacute;e, depuis l'obscurit&eacute; d'un couloir "
  "voisin, par une voix impossible &agrave; identifier "
  "clairement, r&eacute;p&eacute;t&eacute;e presque mot pour mot d'un site &agrave; "
  "l'autre, comme un signal envoy&eacute; simultan&eacute;ment &agrave; "
  "travers tout le r&eacute;seau.")

p("Personne, parmi les habitants de Luynes, de Fondettes, "
  "ni m&ecirc;me parmi les autorit&eacute;s r&eacute;gionales cens&eacute;es "
  "surveiller ce genre d'activit&eacute;, ne remarquera, cette "
  "nuit-l&agrave;, la coordination parfaite de ces multiples "
  "rassemblements &eacute;parpill&eacute;s sur le territoire, ni "
  "l'&eacute;trange synchronisation des lumi&egrave;res &eacute;lectriques "
  "clignotant, une seule fois, exactement au m&ecirc;me "
  "instant, dans des dizaines de b&acirc;timents distincts, "
  "chacun autrefois li&eacute; au m&ecirc;me programme d&eacute;funt.")

p("Ce m&ecirc;me soir, &agrave; Tours, dans la petite chambre "
  "d'&Eacute;milie d&eacute;sormais âg&eacute;e de dix-huit ans, &eacute;tudiante "
  "en premi&egrave;re ann&eacute;e loin du regard vigilant de son "
  "grand fr&egrave;re, un r&ecirc;ve &eacute;trange vient troubler son "
  "sommeil pour la premi&egrave;re fois depuis cette br&egrave;ve "
  "p&eacute;riode de son enfance o&ugrave; elle dessinait, "
  "obstin&eacute;ment, des couloirs num&eacute;rot&eacute;s sans en "
  "comprendre elle-m&ecirc;me la signification.")

p("Elle se r&eacute;veille en sursaut, le c&oelig;ur battant, "
  "incapable de se souvenir enti&egrave;rement du contenu de "
  "ce r&ecirc;ve, seulement de cette impression tenace d'avoir "
  "travers&eacute; un long couloir bord&eacute; de portes identiques, "
  "et d'avoir entendu, tr&egrave;s distinctement, une voix "
  "d'homme lui demander si &laquo;&nbsp;tout le monde &eacute;tait bien "
  "l&agrave;&nbsp;&raquo;, sans qu'elle sache r&eacute;pondre ni &agrave; qui "
  "exactement cette question s'adressait.")

p("Elle n'en parle &agrave; personne le lendemain matin, se "
  "convainquant qu'il ne s'agit que d'un r&ecirc;ve anodin "
  "provoqu&eacute; par le stress des examens qui approchent, "
  "sans savoir que cette m&ecirc;me nuit, &agrave; quelques "
  "kilom&egrave;tres de l&agrave;, son propre fr&egrave;re venait tout "
  "juste de quitter une propri&eacute;t&eacute; o&ugrave; cette question "
  "exacte avait &eacute;t&eacute; pos&eacute;e &agrave; voix haute, dans la "
  "p&eacute;nombre d'un jardin d'hiver, par une voix qu'aucun "
  "des t&eacute;moins pr&eacute;sents n'avait su identifier.")

p("Elle range, ce matin-l&agrave;, sans trop savoir pourquoi, "
  "une vieille bo&icirc;te &agrave; chaussures conserv&eacute;e depuis "
  "l'enfance tout au fond de son armoire, contenant "
  "encore quelques-uns de ces dessins &eacute;tranges "
  "r&eacute;cup&eacute;r&eacute;s autrefois par Alex, et les regarde "
  "longuement, cette fois avec une attention nouvelle, "
  "presque inqui&egrave;te, remarquant pour la premi&egrave;re fois &agrave; "
  "quel point le num&eacute;ro griffonn&eacute; dans le coin de chaque "
  "feuille, 404, ressemble &eacute;trangement &agrave; une adresse, "
  "ou &agrave; un code, plut&ocirc;t qu'&agrave; un simple chiffre "
  "d&eacute;coratif choisi au hasard par une enfant de huit "
  "ans.")

p("Le monde ext&eacute;rieur, pendant ce temps, continue de "
  "tourner exactement comme il l'a toujours fait, "
  "ignorant tout de cette architecture patiente et "
  "invisible qui s'&eacute;tend, discr&egrave;tement, bien au-del&agrave; de "
  "la petite vall&eacute;e de la Loire &mdash; les journaux "
  "r&eacute;gionaux continuent de rapporter des faits divers "
  "ordinaires, les &eacute;coles poursuivent leurs programmes "
  "habituels, et personne, absolument personne except&eacute; "
  "une poign&eacute;e de t&eacute;moins &eacute;parpill&eacute;s &agrave; travers le "
  "pays, ne soup&ccedil;onne l'existence d'un r&eacute;seau aussi "
  "vaste que patient.")

p("Franck, dans les jours qui suivent leur visite &agrave; "
  "Fondettes, tente &agrave; plusieurs reprises de recontacter "
  "Ambroise Vasseur via le num&eacute;ro grav&eacute; sur la petite "
  "carte remise &agrave; leur d&eacute;part, sans jamais obtenir de "
  "r&eacute;ponse, la ligne sonnant ind&eacute;finiment dans le vide, "
  "comme si l'organisation enti&egrave;re s'&eacute;tait, une fois de "
  "plus, retir&eacute;e derri&egrave;re un silence parfaitement "
  "ma&icirc;tris&eacute;.")

name("FRANCK")
p("&laquo;&nbsp;&Ccedil;a r&eacute;pond plus du tout. Exactement comme le "
  "num&eacute;ro d'Amboise, &agrave; l'&eacute;poque. On dirait qu'ils "
  "savent toujours pr&eacute;cis&eacute;ment quand se rendre "
  "injoignables, une fois qu'ils ont obtenu ce qu'ils "
  "voulaient de nous.&nbsp;&raquo;")

p("Clara, de son c&ocirc;t&eacute;, consacre plusieurs semaines &agrave; "
  "consigner minutieusement, dans un nouveau carnet "
  "d&eacute;di&eacute; enti&egrave;rement &agrave; cette derni&egrave;re d&eacute;couverte, "
  "chaque d&eacute;tail dont elle se souvient de la carte "
  "aper&ccedil;ue dans le jardin d'hiver, esp&eacute;rant, malgr&eacute; "
  "l'impr&eacute;cision in&eacute;vitable de sa m&eacute;moire, laisser une "
  "trace suffisamment fid&egrave;le pour qu'un jour, "
  "peut-&ecirc;tre, quelqu'un d'autre puisse reprendre le fil "
  "l&agrave; o&ugrave; elle et Alex auront d&ucirc;, in&eacute;vitablement, "
  "s'arr&ecirc;ter.")

p("Ni elle ni Alex ne parviennent &agrave; se d&eacute;faire, dans "
  "les semaines suivantes, de cette sensation diffuse "
  "mais tenace que quelque chose, quelque part, vient "
  "de basculer d&eacute;finitivement &mdash; non pas de mani&egrave;re "
  "spectaculaire ou imm&eacute;diate, mais avec cette lenteur "
  "patiente propre &agrave; toute chose v&eacute;ritablement "
  "ancienne, comme une mar&eacute;e qui commence &agrave; monter "
  "bien avant que quiconque, sur le rivage, ne "
  "remarque le niveau de l'eau changer.")

p("Alex, hant&eacute; depuis des ann&eacute;es par cette question "
  "jamais totalement r&eacute;solue de la cause exacte de "
  "l'accident ayant co&ucirc;t&eacute; la vie &agrave; Darius, profite de "
  "ses nouvelles comp&eacute;tences d'ing&eacute;nieur pour se "
  "procurer, aupr&egrave;s du fabricant, les rapports techniques "
  "d&eacute;taill&eacute;s concernant le mod&egrave;le exact de casque "
  "impliqu&eacute;, esp&eacute;rant enfin trouver une explication "
  "purement m&eacute;canique &agrave; ce qui s'&eacute;tait produit ce "
  "soir-l&agrave;.")

p("Le rapport officiel, tel qu'il l'obtient apr&egrave;s plusieurs "
  "mois de d&eacute;marches administratives fastidieuses, "
  "confirme bien une d&eacute;faillance de la batterie, comme "
  "annonc&eacute; &agrave; l'&eacute;poque, mais une note technique "
  "annexe, presque perdue au milieu de dizaines de "
  "pages de jargon industriel, mentionne un d&eacute;tail qui "
  "glace imm&eacute;diatement Alex &mdash; une surtension "
  "&eacute;lectrique dont l'origine exacte n'a jamais pu &ecirc;tre "
  "expliqu&eacute;e par la seule d&eacute;faillance mat&eacute;rielle "
  "identifi&eacute;e, comme si un second facteur, ext&eacute;rieur, "
  "&eacute;tait venu s'ajouter au probl&egrave;me purement "
  "technique.")

name("ALEX")
p("&laquo;&nbsp;Clara, j'ai le rapport complet, enfin. Ils disent "
  "que la batterie a claqu&eacute;, &ccedil;a c'est confirm&eacute;. Mais "
  "y'a une note, tout &agrave; la fin, qui parle d'un pic "
  "&eacute;lectrique dont ils comprennent pas l'origine. Ils "
  "l'ont mis sur le compte d'une anomalie du secteur "
  "&eacute;lectrique du quartier, ce soir-l&agrave;, mais &ccedil;a explique "
  "pas tout, apparemment.&nbsp;&raquo;")

p("Il repense, en lisant et relisant ce rapport, &agrave; cette "
  "derni&egrave;re phrase entendue par Darius avant l'accident, "
  "rapport&eacute;e des ann&eacute;es plus tard par Franck comme un "
  "souvenir confus, presque un r&ecirc;ve &eacute;veill&eacute; ressenti par "
  "un p&egrave;re en deuil &mdash; &laquo;&nbsp;je voulais juste que &ccedil;a "
  "compte&nbsp;&raquo; &mdash; et se demande, une fois de plus, sans "
  "jamais parvenir &agrave; trancher d&eacute;finitivement, si Kayden, "
  "d'une mani&egrave;re ou d'une autre, avait vraiment &eacute;t&eacute; "
  "pr&eacute;sent ce soir-l&agrave;, au moment pr&eacute;cis de la mort de "
  "son ami, ou si toute cette histoire n'&eacute;tait, "
  "finalement, qu'une superposition douloureuse de "
  "co&iuml;ncidences que le chagrin transformait, avec le "
  "temps, en signes.")

name("CLARA")
p("&laquo;&nbsp;On saura jamais avec certitude, Alex. C'est "
  "peut-&ecirc;tre &ccedil;a, le plus dur, dans toute cette histoire "
  "&mdash; accepter qu'il y aura toujours une part de "
  "myst&egrave;re, m&ecirc;me pour nous qui avons tout v&eacute;cu de "
  "pr&egrave;s. Darius aurait peut-&ecirc;tre dit que &ccedil;a fait partie "
  "de porter le r&ocirc;le correctement, justement, cette "
  "incertitude-l&agrave;.&nbsp;&raquo;")

p("Alex range, ce soir-l&agrave;, le rapport technique dans le "
  "m&ecirc;me coffre scell&eacute; conserv&eacute; chez Franck, aux c&ocirc;t&eacute;s "
  "de toutes les autres preuves accumul&eacute;es au fil des "
  "ann&eacute;es, conscient qu'un jour, peut-&ecirc;tre, un "
  "successeur inconnu saura tirer de tous ces documents "
  "des conclusions qu'eux-m&ecirc;mes ne parviendront "
  "jamais &agrave; formuler enti&egrave;rement de leur vivant.")

p("Clara, poursuivant seule ses recherches historiques "
  "durant les ann&eacute;es qui suivent la rencontre de "
  "Fondettes, finit par retrouver, dans les archives "
  "nationales num&eacute;ris&eacute;es, des mentions &eacute;parses d'un "
  "motif similaire &agrave; celui de la l&eacute;gende locale de la "
  "Marge dans d'autres r&eacute;gions de France, sous des "
  "noms diff&eacute;rents mais une structure narrative "
  "&eacute;trangement identique &mdash; un &eacute;change, un porteur "
  "humain, une dette contract&eacute;e envers une force "
  "ancienne et patiente.")

p("Elle d&eacute;couvre, en Bretagne, la trace d'une l&eacute;gende "
  "appel&eacute;e &laquo;&nbsp;l'Interstice&nbsp;&raquo;, en Provence celle d'un "
  "&laquo;&nbsp;Passeur des Cendres&nbsp;&raquo;, et jusque dans le "
  "nord de l'Italie, une r&eacute;f&eacute;rence &agrave; peine traduisible "
  "&eacute;voquant une &laquo;&nbsp;porte qui compte les ann&eacute;es&nbsp;&raquo;, "
  "chacune de ces l&eacute;gendes r&eacute;gionales semblant "
  "d&eacute;crire, avec des mots diff&eacute;rents, la m&ecirc;me "
  "m&eacute;canique fondamentale que celle v&eacute;cue "
  "personnellement par Darius, par Templier, et par "
  "combien d'autres avant eux, &agrave; travers l'Europe "
  "enti&egrave;re peut-&ecirc;tre.")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a expliquerait la carte, Alex. Tous ces points, "
  "pas seulement en France. Cette chose-l&agrave;, quelle "
  "qu'elle soit exactement, elle a jamais &eacute;t&eacute; propre &agrave; "
  "Luynes, ni m&ecirc;me &agrave; la France. C'est peut-&ecirc;tre "
  "quelque chose de bien plus ancien et bien plus "
  "universel que &ccedil;a, tapi partout o&ugrave; des humains "
  "vivent depuis assez longtemps au m&ecirc;me endroit.&nbsp;&raquo;")

p("Cette d&eacute;couverte, aussi fascinante qu'effrayante, "
  "occupe Clara pendant des mois entiers, la poussant &agrave; "
  "correspondre discr&egrave;tement avec quelques rares "
  "chercheurs ind&eacute;pendants ayant, eux aussi, "
  "effleur&eacute; ce genre de motif dans leurs propres "
  "travaux acad&eacute;miques, sans jamais oser publier "
  "ouvertement leurs conclusions les plus troublantes, "
  "par crainte, disent-ils, de perdre toute cr&eacute;dibilit&eacute; "
  "professionnelle.")

p("Elle comprend, peu &agrave; peu, que le silence "
  "entourant cette question &agrave; l'&eacute;chelle mondiale "
  "n'est probablement pas le fruit du hasard ou de "
  "l'ignorance collective, mais bien celui d'une "
  "organisation, ou de plusieurs organisations "
  "apparent&eacute;es, activement engag&eacute;es depuis des "
  "g&eacute;n&eacute;rations &agrave; maintenir cette v&eacute;rit&eacute; hors de la "
  "conscience publique, pour des raisons qu'elle ne "
  "parvient toujours pas, malgr&eacute; toutes ses recherches, &agrave; "
  "cerner enti&egrave;rement.")

p("Franck, sentant l'&acirc;ge peser un peu plus chaque ann&eacute;e "
  "sur son corps sans jamais renoncer pour autant &agrave; "
  "cette vigilance devenue seconde nature, d&eacute;cide, "
  "quelques mois apr&egrave;s la visite &agrave; Fondettes, de "
  "rassembler par &eacute;crit tout ce qu'il souhaite voir "
  "transmis un jour, si n&eacute;cessaire, &agrave; quiconque leur "
  "succ&eacute;derait dans cette veille silencieuse &mdash; non pas "
  "par pressentiment funeste, mais par cette prudence "
  "m&eacute;thodique que Templier leur avait, &agrave; tous, "
  "enseign&eacute;e.")

p("Il r&eacute;dige, avec une application touchante pour un "
  "homme qui s'est longtemps d&eacute;fini par sa difficult&eacute; &agrave; "
  "mettre des mots sur ce qui compte vraiment, un long "
  "texte destin&eacute; &agrave; accompagner le coffre cach&eacute; sous le "
  "plancher de sa maison, r&eacute;sumant, dans ses propres "
  "termes, tout ce que son fils lui avait appris durant "
  "cette derni&egrave;re ann&eacute;e de vie partag&eacute;e, et tout ce "
  "qu'Ambroise Vasseur leur avait r&eacute;v&eacute;l&eacute; ce jour-l&agrave; &agrave; "
  "Fondettes.")

name("FRANCK")
p("&laquo;&nbsp;&Agrave; qui lira ceci un jour, si le besoin s'en fait "
  "sentir. J'ai &eacute;t&eacute; le fr&egrave;re d'un gar&ccedil;on devenu quelque "
  "chose d'&eacute;trange et de tragique, et le p&egrave;re d'un "
  "gar&ccedil;on devenu, plus tard, incroyablement courageux. "
  "J'ai men&eacute;, longtemps, une vie fond&eacute;e sur la fuite et "
  "le silence, croyant prot&eacute;ger ceux que j'aimais en leur "
  "cachant ce qui faisait mal. Mon fils m'a appris "
  "l'inverse. Que la v&eacute;rit&eacute;, dite &agrave; temps, prot&egrave;ge "
  "toujours mieux que le mensonge, m&ecirc;me quand elle "
  "fait mal.&nbsp;&raquo;")

p("Clara et Alex, mis dans la confidence de cette "
  "d&eacute;marche, l'aident &agrave; compl&eacute;ter le document de leurs "
  "propres observations, chacun ajoutant, &agrave; sa mani&egrave;re, "
  "sa part de v&eacute;rit&eacute; accumul&eacute;e au fil des ann&eacute;es, "
  "convaincus tous les trois qu'un jour, quelqu'un, "
  "peut-&ecirc;tre tr&egrave;s longtemps apr&egrave;s eux, aurait besoin de "
  "cette transmission pour affronter, &agrave; son tour, ce que "
  "Darius avait affront&eacute; le premier.")

name("FRANCK")
p("&laquo;&nbsp;Si vous &ecirc;tes en train de lire ceci un jour, sachez "
  "que vous n'&ecirc;tes pas seul, m&ecirc;me longtemps apr&egrave;s que "
  "nous aurons tous disparu &agrave; notre tour. Il y a "
  "toujours eu quelqu'un avant vous. Il y aura "
  "probablement toujours quelqu'un apr&egrave;s.&nbsp;&raquo;")

p("Le texte scell&eacute; est plac&eacute;, avec un soin presque "
  "c&eacute;r&eacute;monial, au sommet du coffre d&eacute;j&agrave; rempli de tant "
  "d'ann&eacute;es de preuves et de souvenirs, et Franck, ce "
  "soir-l&agrave;, ressent, malgr&eacute; l'&acirc;ge et la fatigue "
  "accumul&eacute;e, une paix nouvelle &agrave; l'id&eacute;e d'avoir enfin "
  "mis de l'ordre dans un h&eacute;ritage trop longtemps port&eacute; "
  "dans le seul silence.")

p("Aucun d'eux trois, ce jour du seize f&eacute;vrier o&ugrave; "
  "Ambroise Vasseur les re&ccedil;oit &agrave; Fondettes, ne peut "
  "encore savoir &agrave; quel point cette rencontre marquera, "
  "r&eacute;trospectivement, un tournant d&eacute;cisif dans une "
  "histoire commenc&eacute;e bien avant leur propre naissance "
  "&mdash; ni Franck, encore vigoureux malgr&eacute; ses soixante "
  "ans pass&eacute;s, ni Clara, ni Alex, absorb&eacute;s tous trois par "
  "l'&eacute;motion de cette journ&eacute;e extraordinaire, ne "
  "soup&ccedil;onnent que cette invitation, en apparence "
  "isol&eacute;e, r&eacute;pond en r&eacute;alit&eacute; &agrave; un calendrier bien plus "
  "vaste, orchestr&eacute; simultan&eacute;ment &agrave; travers des "
  "dizaines d'autres sites &agrave; travers le pays.")

p("Ils rentrent ce soir-l&agrave; vers Luynes, la nuit d&eacute;j&agrave; "
  "tomb&eacute;e sur la vall&eacute;e, sans imaginer un seul instant "
  "que la propri&eacute;t&eacute; qu'ils viennent de quitter continue, "
  "derri&egrave;re eux, d'accueillir une assembl&eacute;e qui ne "
  "s'est jamais vraiment dispers&eacute;e, et que cette m&ecirc;me "
  "soir&eacute;e, dans l'obscurit&eacute; grandissante, quelque chose "
  "de bien plus vaste que leur propre histoire "
  "personnelle s'appr&ecirc;te &agrave; franchir un seuil que ni "
  "Templier, ni m&ecirc;me Darius, n'avaient jamais "
  "compl&egrave;tement anticip&eacute;.")

p("Ce qu'Ambroise Vasseur n'a r&eacute;v&eacute;l&eacute; &agrave; aucun moment "
  "durant sa longue explication du jardin d'hiver, "
  "c'est que sa propre position &agrave; la t&ecirc;te de cette "
  "organisation h&eacute;rit&eacute;e de son grand-p&egrave;re n'a jamais "
  "&eacute;t&eacute; celle d'un simple gardien passif, comme il "
  "voulait le laisser croire &agrave; Franck, Clara et Alex, mais "
  "bien celle d'un homme convaincu, avec une "
  "d&eacute;termination presque religieuse, que l'humanit&eacute; "
  "enti&egrave;re gagnerait &agrave; comprendre enfin, publiquement, "
  "ce que la Marge repr&eacute;sente vraiment.")

p("Il a pass&eacute; sa vie enti&egrave;re, depuis la mort de son "
  "propre p&egrave;re, &agrave; rassembler patiemment les t&eacute;moins "
  "&eacute;pars de ce ph&eacute;nom&egrave;ne millénaire, convaincu qu'une "
  "r&eacute;v&eacute;lation coordonn&eacute;e, men&eacute;e simultan&eacute;ment depuis "
  "tous les sites du r&eacute;seau, offrirait enfin &agrave; l'humanit&eacute; "
  "l'occasion de n&eacute;gocier collectivement avec cette "
  "force ancienne plut&ocirc;t que de continuer &agrave; la "
  "combattre isol&eacute;ment, porteur apr&egrave;s porteur, "
  "g&eacute;n&eacute;ration apr&egrave;s g&eacute;n&eacute;ration, dans une souffrance "
  "qu'il juge d&eacute;sormais totalement &eacute;vitable.")

p("Cette conviction, nourrie par des d&eacute;cennies "
  "d'&eacute;tude solitaire et par la perte, jeune homme, d'une "
  "s&oelig;ur elle-m&ecirc;me emport&eacute;e par la Marge dans des "
  "circonstances qu'il n'a jamais compl&egrave;tement "
  "&eacute;lucid&eacute;es, l'a progressivement conduit &agrave; consid&eacute;rer "
  "cette c&eacute;r&eacute;monie du seize f&eacute;vrier non plus comme un "
  "simple rassemblement comm&eacute;moratif, mais comme le "
  "premier acte concret d'un plan bien plus ambitieux, "
  "muri depuis des ann&eacute;es dans le plus grand secret, "
  "m&ecirc;me vis-&agrave;-vis de la plupart des membres de sa "
  "propre organisation.")

p("Les quelques initi&eacute;s les plus proches de lui, "
  "convoqu&eacute;s discr&egrave;tement apr&egrave;s le d&eacute;part des "
  "visiteurs ext&eacute;rieurs, savent seuls que cette soir&eacute;e "
  "marque le d&eacute;but d'une tentative sans pr&eacute;c&eacute;dent &mdash; "
  "synchroniser, pour la premi&egrave;re fois de l'histoire "
  "connue de la Marge, l'ensemble des sites actifs du "
  "r&eacute;seau mondial, dans l'espoir de forcer, d'un seul "
  "geste collectif, une confrontation d&eacute;finitive avec la "
  "source elle-m&ecirc;me de cette force ancestrale.")

p("Ce qu'Ambroise Vasseur lui-m&ecirc;me n'a jamais "
  "compl&egrave;tement anticip&eacute;, malgr&eacute; des ann&eacute;es de "
  "pr&eacute;paration m&eacute;ticuleuse, c'est la nature exacte de ce "
  "que repr&eacute;sente r&eacute;ellement cette force que son "
  "grand-p&egrave;re, puis lui-m&ecirc;me, ont pass&eacute; leurs vies "
  "enti&egrave;res &agrave; &eacute;tudier sans jamais parvenir &agrave; en "
  "percevoir plus qu'une infime fraction &mdash; une "
  "sous-estimation qui rappelle, avec une ironie glac&eacute;e, "
  "celle commise par le docteur Vasseur lui-m&ecirc;me en "
  "1991, convaincu de pouvoir dompter par la science ce "
  "qu'aucune g&eacute;n&eacute;ration humaine, avant la sienne, "
  "n'avait jamais r&eacute;ussi &agrave; ma&icirc;triser enti&egrave;rement.")

p("Templier l'avait pourtant avert i, des ann&eacute;es plus "
  "t&ocirc;t, dans son jardin de vigne face &agrave; trois "
  "adolescents encore incapables de mesurer pleinement "
  "la port&eacute;e de ses paroles : ne jamais rien donner de "
  "trop gros &agrave; la Marge, quoi qu'elle promette en "
  "&eacute;change, car ce qu'elle rend rarement, elle finit "
  "toujours, tot ou tard, par le reprendre avec int&eacute;r&ecirc;t.")

p("Et c'est pr&eacute;cis&eacute;ment cela, cette promesse "
  "d&eacute;mesur&eacute;e formul&eacute;e par Ambroise Vasseur &agrave; "
  "l'ensemble de son r&eacute;seau &mdash; l'offre d'une "
  "confrontation d&eacute;finitive, d'une r&eacute;solution totale, "
  "d'une lib&eacute;ration compl&egrave;te pour tous les porteurs "
  "pr&eacute;sents et futurs &mdash; que la Marge, patiente depuis "
  "des si&egrave;cles, semble avoir attendu tout du long, "
  "comme si cette g&eacute;n&eacute;rosit&eacute; apparente n'&eacute;tait, en "
  "r&eacute;alit&eacute;, que l'app&acirc;t final d'un pi&egrave;ge tendu depuis "
  "bien plus longtemps que n'importe quel &ecirc;tre humain "
  "n'aurait jamais pu l'imaginer.")

p("Odile, cette femme &acirc;g&eacute;e retrouv&eacute;e par Clara au "
  "milieu de l'assembl&eacute;e du jardin d'hiver, poss&egrave;de, "
  "sans qu'aucun des visiteurs de l'apr&egrave;s-midi ne l'ait "
  "jamais soup&ccedil;onn&eacute;, une histoire personnelle bien plus "
  "&eacute;troitement li&eacute;e &agrave; Ambroise Vasseur que ne le "
  "laissait para&icirc;tre sa br&egrave;ve intervention devant Clara "
  "et Alex &mdash; elle fut, quarante ans plus t&ocirc;t, la toute "
  "premi&egrave;re personne qu'il retrouva, jeune homme &agrave; "
  "peine sorti de l'universit&eacute;, lors de ses recherches "
  "initiales sur les t&eacute;moins survivants du programme de "
  "son grand-p&egrave;re.")

p("C'est elle qui, la premi&egrave;re, lui avait racont&eacute; sa "
  "propre exp&eacute;rience de dissolution partielle apr&egrave;s la "
  "disparition de son fr&egrave;re Templier, et c'est cette "
  "histoire, plus que toute autre, qui avait convaincu "
  "le jeune Ambroise que la Marge n'&eacute;tait pas une force "
  "n&eacute;cessairement hostile &agrave; combattre, mais une "
  "&eacute;quation complexe qu'il suffirait, peut-&ecirc;tre, de "
  "r&eacute;soudre correctement pour en lib&eacute;rer d&eacute;finitivement "
  "l'humanit&eacute; enti&egrave;re.")

p("Elle seule, ce soir de f&eacute;vrier, conna&icirc;t avec certitude "
  "l'ampleur exacte du plan que son jeune protégé "
  "s'appr&ecirc;te &agrave; d&eacute;clencher, et elle seule, dans les "
  "instants qui pr&eacute;c&egrave;dent l'arriv&eacute;e de la voix "
  "myst&eacute;rieuse depuis le couloir obscur, ressent une "
  "h&eacute;sitation tardive, un doute profond quant &agrave; la "
  "sagesse r&eacute;elle de cette entreprise port&eacute;e depuis si "
  "longtemps avec tant de conviction.")

name("ODILE")
p("&laquo;&nbsp;Ambroise. Tu es s&ucirc;r de vouloir vraiment faire "
  "&ccedil;a ce soir ? On pourrait attendre encore. Rassembler "
  "plus de preuves, convaincre davantage de monde "
  "avant d'agir. Rien ne presse, apr&egrave;s toutes ces "
  "d&eacute;cennies d'attente.&nbsp;&raquo;")

name("AMBROISE VASSEUR")
p("&laquo;&nbsp;Tout presse, au contraire, Odile. Chaque ann&eacute;e "
  "suppl&eacute;mentaire, c'est un nouveau porteur qui souffre "
  "quelque part, un nouveau Darius qui risque de tout "
  "perdre comme lui. J'ai attendu toute ma vie ce "
  "moment pr&eacute;cis. Je compte pas reculer maintenant, "
  "m&ecirc;me si &ccedil;a me co&ucirc;te cher, personnellement.&nbsp;&raquo;")

p("Odile, malgr&eacute; ses r&eacute;serves grandissantes, ne "
  "s'oppose pas davantage &agrave; la volont&eacute; d'Ambroise, "
  "consciente qu'apr&egrave;s tant d'ann&eacute;es pass&eacute;es &agrave; "
  "construire ensemble ce projet, il est d&eacute;sormais bien "
  "trop tard pour esp&eacute;rer l'en d&eacute;tourner enti&egrave;rement, "
  "et se contente de rester &agrave; ses c&ocirc;t&eacute;s, silencieuse, "
  "pr&ecirc;te &agrave; affronter, avec lui, quoi qu'il advienne "
  "d&eacute;sormais de cette d&eacute;cision irr&eacute;versible.")

p("&Agrave; l'instant pr&eacute;cis o&ugrave; la voiture de Franck "
  "s'&eacute;loigne d&eacute;finitivement de la propri&eacute;t&eacute; de "
  "Fondettes, ses phares disparaissant au d&eacute;tour du "
  "chemin bord&eacute; de vignes, Ambroise Vasseur donne, "
  "d'un simple signe de t&ecirc;te &eacute;chang&eacute; avec un technicien "
  "install&eacute; discr&egrave;tement dans une pi&egrave;ce voisine, le "
  "signal d'activation d'un dispositif pr&eacute;par&eacute; depuis "
  "des mois, reliant simultan&eacute;ment, par un r&eacute;seau de "
  "communication crypt&eacute; qu'aucune autorit&eacute; officielle "
  "n'a jamais r&eacute;ussi &agrave; d&eacute;tecter, l'ensemble des sites "
  "encore actifs du programme &agrave; travers le pays et "
  "au-del&agrave; des fronti&egrave;res.")

p("Dans chacun de ces lieux, simultan&eacute;ment, une "
  "assembl&eacute;e similaire &agrave; celle de Fondettes attend, "
  "silencieuse, la m&ecirc;me confirmation, et c'est ce r&eacute;seau "
  "enti&egrave;rement synchronis&eacute;, tendu comme une corde "
  "unique reliant des dizaines de points du globe, qui "
  "recueille, dans le m&ecirc;me instant pr&eacute;cis, la question "
  "pos&eacute;e depuis l'obscurit&eacute; du couloir de Fondettes, "
  "relay&eacute;e imm&eacute;diatement &agrave; chacun des autres sites "
  "par ce dispositif invisible.")

p("&Agrave; Loches, dans une ancienne caserne d&eacute;saffect&eacute;e "
  "reconvertie en centre culturel municipal, une "
  "poign&eacute;e de personnes se tient immobile dans une "
  "salle des archives ferm&eacute;e au public depuis des "
  "ann&eacute;es, attendant, elles aussi, le m&ecirc;me signal que "
  "celui transmis depuis Fondettes, sans qu'aucun "
  "employ&eacute; municipal, occup&eacute; &agrave; fermer le b&acirc;timent "
  "pour la nuit &agrave; l'&eacute;tage sup&eacute;rieur, ne soup&ccedil;onne leur "
  "pr&eacute;sence.")

p("&Agrave; Blois, dans les caves vo&ucirc;t&eacute;es d'une propri&eacute;t&eacute; "
  "viticole appartenant depuis des g&eacute;n&eacute;rations &agrave; une "
  "famille alli&eacute;e aux Vasseur, une assembl&eacute;e similaire "
  "patiente autour d'une table identique, un pon&ccedil;on "
  "grav&eacute; en son centre, dans un silence aussi &eacute;pais que "
  "celui du jardin d'hiver de Fondettes.")

p("Plus loin encore, dans une petite ville du nord de "
  "l'Italie dont le nom n'appara&icirc;tra jamais dans aucun "
  "document officiel consult&eacute; par Clara durant ses "
  "recherches, une autre assembl&eacute;e, plus r&eacute;duite mais "
  "tout aussi d&eacute;termin&eacute;e, re&ccedil;oit &agrave; son tour, via ce "
  "m&ecirc;me r&eacute;seau invisible, l'&eacute;cho de la question pos&eacute;e "
  "depuis la France, chacun de ses membres portant, "
  "lui aussi, une part infime de cette m&ecirc;me force "
  "ancienne qui a travers&eacute; l'existence de Darius, de "
  "Templier, de Kayden, et de tant d'autres avant eux.")

p("Ce r&eacute;seau, in visible aux yeux du monde ordinaire, "
  "coordonn&eacute; avec une patience b&acirc;tie sur des "
  "d&eacute;cennies de pr&eacute;paration silencieuse, ne repr&eacute;sente "
  "somme toute qu'une fraction de l'ampleur r&eacute;elle de "
  "ce ph&eacute;nom&egrave;ne millénaire &mdash; une fraction suffisante, "
  "n&eacute;anmoins, aux yeux d'Ambroise Vasseur, pour "
  "tenter, ce soir-l&agrave;, ce qu'aucun porteur individuel, "
  "aussi courageux soit-il, n'aurait jamais pu accomplir "
  "seul.")

p("Dans la derni&egrave;re heure pr&eacute;c&eacute;dant l'activation "
  "d&eacute;finitive du dispositif, Ambroise Vasseur se retire "
  "un instant, seul, dans le petit bureau attenant au "
  "jardin d'hiver, ce m&ecirc;me bureau o&ugrave; Darius, onze ans "
  "plus t&ocirc;t, avait tap&eacute; le num&eacute;ro 404 sur un vieil "
  "ordinateur poussi&eacute;reux, et contemple longuement une "
  "photographie encadr&eacute;e de son grand-p&egrave;re, le docteur "
  "Vasseur, pos&eacute;e sur l'&eacute;tag&egrave;re depuis toujours.")

name("AMBROISE VASSEUR")
p("&laquo;&nbsp;J'esp&egrave;re que tu aurais &eacute;t&eacute; fier de moi, "
  "grand-p&egrave;re. J'ach&egrave;ve, ce soir, ce que tu avais "
  "commenc&eacute; sans jamais pouvoir le terminer. J'esp&egrave;re "
  "surtout que j'ai raison de croire que &ccedil;a valait la "
  "peine, tout &ccedil;a, apr&egrave;s tant d'ann&eacute;es et tant de "
  "sacrifices consentis par tant de gens qui n'avaient "
  "rien demand&eacute;.&nbsp;&raquo;")

p("Il repense, l'espace d'un instant, au visage de "
  "Darius entraper&ccedil;u sur cette photographie de classe "
  "accroch&eacute;e dans le couloir, &agrave; ce p&egrave;re boulevers&eacute; "
  "demandant si son fr&egrave;re existait encore quelque part, "
  "&agrave; cette jeune femme, Clara, dont le regard per&ccedil;ant "
  "avait failli percer &agrave; jour, quelques heures plus t&ocirc;t "
  "seulement, l'ensemble de son dispositif soigneusement "
  "orchestr&eacute;.")

p("Il &eacute;teint la lumi&egrave;re du bureau et rejoint l'assembl&eacute;e "
  "r&eacute;unie dans le jardin d'hiver, o&ugrave; chaque visage "
  "tourn&eacute; vers lui attend, dans un silence absolu, le "
  "signal final qu'il s'appr&ecirc;te, apr&egrave;s tant d'ann&eacute;es de "
  "pr&eacute;paration, &agrave; donner enfin.")

p("Clara, install&eacute;e &agrave; l'arri&egrave;re de la voiture de Franck "
  "pendant tout le trajet de retour vers Luynes, garde "
  "les yeux fix&eacute;s sur le paysage nocturne qui d&eacute;file, "
  "incapable de chasser totalement de son esprit "
  "l'image de cette immense carte entraper&ccedil;ue sur le mur "
  "du jardin d'hiver, ni celle, plus troublante encore, de "
  "ces regards teint&eacute;s de bleu qu'elle avait crus "
  "reconna&icirc;tre chez plusieurs membres de l'assembl&eacute;e.")

p("Elle repense &agrave; tout ce que Templier leur avait "
  "enseign&eacute;, des ann&eacute;es plus t&ocirc;t, dans son jardin de "
  "vigne, sur la prudence n&eacute;cessaire face &agrave; toute "
  "promesse trop belle formul&eacute;e par quiconque pr&eacute;tend "
  "vouloir n&eacute;gocier avec la Marge, et se demande, avec "
  "une inqui&eacute;tude grandissante qu'elle ne parvient pas &agrave; "
  "totalement justifier, si Ambroise Vasseur, malgr&eacute; "
  "toute l'apparente sinc&eacute;rit&eacute; de son discours, ne "
  "s'appr&ecirc;te pas, en r&eacute;alit&eacute;, &agrave; commettre exactement "
  "l'erreur que le vieil homme leur avait tant "
  "recommand&eacute; d'&eacute;viter.")

name("CLARA")
p("&laquo;&nbsp;Alex, &ccedil;a te dirait pas, &agrave; toi, ce qu'il a dit ? Cette "
  "promesse de tout r&eacute;soudre d&eacute;finitivement, de "
  "lib&eacute;rer tous les porteurs pour de bon ? &Ccedil;a ressemble "
  "&eacute;norm&eacute;ment &agrave; ce genre de truc trop beau pour &ecirc;tre "
  "vrai dont Templier nous parlait toujours.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;J'y ai pens&eacute; aussi, tout du long. Mais qu'est-ce "
  "qu'on pouvait faire, l&agrave;, sur place ? On conna&icirc;t "
  "m&ecirc;me pas l'ampleur exacte de ce qu'ils pr&eacute;parent. "
  "On a que des soup&ccedil;ons, pas de preuves. Difficile de "
  "s'opposer &agrave; quelque chose qu'on comprend "
  "qu'&agrave; moiti&eacute;.&nbsp;&raquo;")

p("Cette conversation, men&eacute;e &agrave; voix basse pour ne pas "
  "inqui&eacute;ter davantage Franck d&eacute;j&agrave; visiblement &eacute;puis&eacute; "
  "&eacute;motionnellement par sa propre conversation avec "
  "Ambroise Vasseur, se poursuit sur plusieurs kilom&egrave;tres, "
  "Clara et Alex tentant, sans grand succ&egrave;s, de "
  "d&eacute;terminer une conduite &agrave; tenir face &agrave; une menace "
  "dont ils ne ma&icirc;trisent, en fin de compte, qu'une "
  "fraction infime.")

p("Clara sort, &agrave; un moment, son t&eacute;l&eacute;phone pour "
  "photographier discr&egrave;tement, de m&eacute;moire, un croquis "
  "rapide de la carte aper&ccedil;ue &agrave; Fondettes, esp&eacute;rant "
  "fixer, avant qu'il ne s'estompe compl&egrave;tement, le "
  "souvenir pr&eacute;cieux de cette disposition &eacute;trange de "
  "points lumineux qui pourrait, un jour, s'av&eacute;rer "
  "essentielle pour comprendre l'ampleur r&eacute;elle de ce &agrave; "
  "quoi ils viennent d'&ecirc;tre m&ecirc;l&eacute;s.")

p("Franck, conduisant en silence depuis le d&eacute;part de "
  "Fondettes, n'a pas prononc&eacute; un mot depuis plusieurs "
  "kilom&egrave;tres, absorb&eacute; enti&egrave;rement par cette derni&egrave;re "
  "conversation avec Ambroise Vasseur au sujet de son "
  "fr&egrave;re, cette promesse fragile qu'une part de Kayden "
  "subsisterait peut-&ecirc;tre encore quelque part, dilu&eacute;e mais "
  "pas &eacute;teinte, et cette demande, formul&eacute;e presque "
  "malgr&eacute; lui, qu'on lui transmette un jour, s'il existait "
  "un moyen, ce pardon jamais totalement exprim&eacute; "
  "durant toutes ces ann&eacute;es de silence.")

p("Il ressent, en conduisant, une fatigue immense, "
  "diff&eacute;rente de la simple lassitude physique de l'&acirc;ge "
  "&mdash; celle d'un homme ayant pass&eacute; toute une vie &agrave; "
  "porter, tant bien que mal, l'h&eacute;ritage d'une famille "
  "bris&eacute;e par des d&eacute;cisions prises bien avant sa propre "
  "naissance, et qui sent, ce soir, que cette charge "
  "vient peut-&ecirc;tre, enfin, d'atteindre son point culminant.")

name("FRANCK")
p("&laquo;&nbsp;Vous savez, je crois que Darius aurait su quoi "
  "penser de tout &ccedil;a, lui. Il avait toujours cette "
  "capacit&eacute; &agrave; voir clair dans les situations "
  "compliqu&eacute;es, m&ecirc;me tout jeune. Moi, j'avoue que je "
  "suis compl&egrave;tement perdu, ce soir. J'sais m&ecirc;me plus si "
  "j'ai bien fait de vous emmener l&agrave;-bas.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;Vous avez bien fait, Franck. On pr&eacute;f&egrave;re "
  "toujours savoir, m&ecirc;me quand &ccedil;a fait peur. Darius "
  "aurait dit pareil, j'en suis certaine. C'est ce qu'il "
  "nous a appris, &agrave; tous, depuis le d&eacute;but.&nbsp;&raquo;")

p("Ils arrivent enfin en vue des premi&egrave;res lumi&egrave;res de "
  "Luynes, ce village qu'ils connaissent tous par c&oelig;ur "
  "depuis l'enfance, et dont l'aspect paisible, ce "
  "soir-l&agrave;, contraste violemment avec tout ce qu'ils "
  "viennent d'apprendre sur l'ampleur r&eacute;elle du monde "
  "qui l'entoure, invisible mais bien pr&eacute;sent, tapi "
  "derri&egrave;re la fa&ccedil;ade tranquille de leur petite ville "
  "natale.")

p("Alex, install&eacute; &agrave; l'avant de la voiture aux c&ocirc;t&eacute;s de "
  "Franck, observe en silence le visage &eacute;puis&eacute; de cet "
  "homme qu'il consid&egrave;re, depuis des ann&eacute;es d&eacute;sormais, "
  "presque comme un second p&egrave;re, et se fait, int&eacute;rieurement, "
  "une promesse silencieuse qu'il ne formulera pas &agrave; "
  "voix haute ce soir-l&agrave;, mais qui gravera profond&eacute;ment "
  "sa conduite dans les ann&eacute;es &agrave; venir.")

p("Il se jure de ne jamais laisser cette histoire, aussi "
  "vaste et effrayante soit-elle devenue, &eacute;craser "
  "compl&egrave;tement sa propre existence ni celle de Clara, "
  "refusant de r&eacute;p&eacute;ter, &agrave; sa mani&egrave;re, l'erreur commise "
  "autrefois par Franck lui-m&ecirc;me lorsqu'il avait laiss&eacute; "
  "la peur et le silence dicter toute une vie enti&egrave;re "
  "plut&ocirc;t que d'affronter, avec courage, ce qui m&eacute;ritait "
  "d'&ecirc;tre affront&eacute;.")

p("Il pense &agrave; sa petite s&oelig;ur &Eacute;milie, endormie "
  "paisiblement &agrave; cette heure dans son appartement "
  "&eacute;tudiant &agrave; Tours, ignorante encore de tout ce que "
  "cette soir&eacute;e vient de r&eacute;v&eacute;ler sur l'ampleur r&eacute;elle du "
  "monde qui pourrait, un jour, exiger d'elle &eacute;galement "
  "un r&ocirc;le qu'elle n'aura jamais choisi, et se promet de "
  "veiller sur elle avec encore plus d'attention que "
  "jamais, quoi qu'il advienne d&eacute;sormais.")

name("ALEX")
p("&laquo;&nbsp;Franck, quoi qu'il se passe &agrave; partir de "
  "maintenant, avec Vasseur, avec le r&eacute;seau, avec tout "
  "&ccedil;a &mdash; on l&acirc;chera pas l'affaire. Mais on se laissera "
  "pas non plus bouffer enti&egrave;rement par &ccedil;a, comme &ccedil;a a "
  "failli vous arriver, &agrave; vous et &agrave; Darius, chacun &agrave; "
  "votre mani&egrave;re. On trouvera un &eacute;quilibre. Promis.&nbsp;&raquo;")

p("Franck hoche la t&ecirc;te sans r&eacute;pondre imm&eacute;diatement, "
  "touch&eacute; par cette d&eacute;termination tranquille qu'Alex a "
  "d&eacute;velopp&eacute;e au fil des ann&eacute;es, cette capacit&eacute; &agrave; "
  "regarder le danger en face sans jamais se laisser "
  "totalement submerger par lui, une qualit&eacute; qu'il "
  "reconna&icirc;t, avec une fiert&eacute; presque paternelle, comme "
  "un h&eacute;ritage direct de tout ce que Darius leur avait, &agrave; "
  "tous, transmis avant de dispara&icirc;tre.")

p("La voiture franchit enfin le panneau d'entr&eacute;e du "
  "village, cette simple plaque annon&ccedil;ant &laquo;&nbsp;Luynes&nbsp;&raquo; "
  "que Darius avait d&ucirc; croiser des milliers de fois "
  "durant sa br&egrave;ve existence sans jamais imaginer &agrave; "
  "quel point ce petit coin tranquille de la vall&eacute;e de la "
  "Loire &eacute;tait, en r&eacute;alit&eacute;, li&eacute; &agrave; un r&eacute;seau bien plus "
  "vaste que n'importe quel de ses habitants n'aurait pu "
  "l'imaginer.")

p("Les rues sont d&eacute;sertes &agrave; cette heure tardive de "
  "f&eacute;vrier, les fen&ecirc;tres &eacute;clair&eacute;es des maisons "
  "t&eacute;moignant discr&egrave;tement de vies ordinaires se "
  "poursuivant sans le moindre soup&ccedil;on de ce qui vient "
  "de se jouer, quelques kilom&egrave;tres plus loin, dans le "
  "jardin d'hiver d'une propri&eacute;t&eacute; discr&egrave;te de Fondettes.")

name("CLARA")
p("&laquo;&nbsp;Merci de nous avoir emmen&eacute;s, aujourd'hui, "
  "Franck. Quoi qu'il se passe ensuite, je suis contente "
  "qu'on ait fait &ccedil;a ensemble, tous les trois. Darius "
  "aurait &eacute;t&eacute; fier de nous, je crois, de voir qu'on "
  "continue &agrave; avancer ensemble, m&ecirc;me face &agrave; un truc "
  "aussi &eacute;norme.&nbsp;&raquo;")

p("Franck lui sourit faiblement, &eacute;puis&eacute; mais sinc&egrave;rement "
  "touch&eacute; par ces mots, ralentissant l&eacute;g&egrave;rement la "
  "voiture &agrave; l'approche du centre du village, cette petite "
  "b&acirc;tisse troglodytique du coteau qui a vu passer, au fil "
  "des ann&eacute;es, Templier, Darius, et d&eacute;sormais lui-m&ecirc;me, "
  "chacun &agrave; son tour porteur d'une part de cette "
  "histoire qui semble d&eacute;sormais, plus que jamais, loin "
  "d'&ecirc;tre achev&eacute;e.")

p("Franck, en approchant du centre du village avec "
  "Clara encore assise &agrave; l'arri&egrave;re de la voiture, sent "
  "remonter en lui, sans crier gare, une avalanche de "
  "souvenirs pr&eacute;cis li&eacute;s &agrave; Darius &mdash; le trajet inverse, "
  "onze ans plus t&ocirc;t, quand il ramenait son fils chez sa "
  "m&egrave;re apr&egrave;s un week-end pass&eacute; ensemble, cette "
  "impression, d&eacute;j&agrave; &agrave; l'&eacute;poque, de ne jamais avoir "
  "assez de temps pour tout se dire.")

p("Il repense &agrave; cette derni&egrave;re soir&eacute;e, onze ans "
  "auparavant, quand Darius lui avait demand&eacute; vingt "
  "minutes suppl&eacute;mentaires pour terminer son jeu, et &agrave; "
  "quel point cette simple demande, si anodine sur le "
  "moment, r&eacute;sonne encore aujourd'hui dans sa m&eacute;moire "
  "avec le poids &eacute;crasant de tout ce qui a suivi.")

name("FRANCK")
p("&laquo;&nbsp;Vous savez, Clara, des fois j'me dis que si "
  "j'&eacute;tais rest&eacute; ce soir-l&agrave;, juste un peu plus longtemps, "
  "peut-&ecirc;tre que rien de tout &ccedil;a serait arriv&eacute;. Je sais "
  "que &ccedil;a sert &agrave; rien de penser &ccedil;a, mais &ccedil;a me "
  "quitte jamais vraiment, cette id&eacute;e.&nbsp;&raquo;")

name("CLARA")
p("&laquo;&nbsp;Vous auriez pu rien changer, Franck. Vous le "
  "savez, au fond. Darius portait quelque chose de "
  "beaucoup plus grand que nous tous, depuis toujours. "
  "&Ccedil;a devait peut-&ecirc;tre arriver, d'une mani&egrave;re ou d'une "
  "autre. C'est pas votre faute. &Ccedil;a l'a jamais &eacute;t&eacute;.&nbsp;&raquo;")

p("Ces mots, r&eacute;p&eacute;t&eacute;s presque chaque ann&eacute;e &agrave; peu de "
  "choses pr&egrave;s depuis onze ans, n'ont jamais totalement "
  "r&eacute;ussi &agrave; effacer la culpabilit&eacute; sourde que Franck "
  "porte depuis cette soir&eacute;e de f&eacute;vrier, mais ils "
  "apportent, chaque fois, un all&eacute;gement mom entan&eacute; "
  "suffisant pour continuer &agrave; avancer, une ann&eacute;e apr&egrave;s "
  "l'autre, sans jamais totalement sombrer sous le "
  "poids du regret.")

p("C'est &agrave; cet instant pr&eacute;cis, la voiture ralentissant "
  "encore &agrave; l'approche de la place centrale de Luynes, "
  "que Clara, incapable de laisser cette journ&eacute;e si dense "
  "se refermer sans un dernier geste envers son ami "
  "disparu, se penche l&eacute;g&egrave;rement vers l'avant du "
  "v&eacute;hicule pour formuler la demande qui la travaille "
  "depuis leur d&eacute;part de Fondettes.")

p("Elle pense &agrave; tout ce qu'ils viennent d'apprendre, &agrave; "
  "cette carte immense, &agrave; ces regards teint&eacute;s de bleu, "
  "&agrave; cette promesse ambigu&euml; d'Ambroise Vasseur, et "
  "ressent, plus que jamais, le besoin imp&eacute;rieux de "
  "retrouver, ne serait-ce que quelques minutes, la "
  "simplicit&eacute; d'un chagrin pur, sans myst&egrave;re "
  "suppl&eacute;mentaire &agrave; d&eacute;chiffrer, sans organisation "
  "secr&egrave;te &agrave; craindre &mdash; juste elle, Alex, Franck, et la "
  "m&eacute;moire intacte de Darius.")

p("Alex, silencieux depuis un moment sur la banquette "
  "arri&egrave;re &agrave; c&ocirc;t&eacute; de Clara, hoche imm&eacute;diatement la "
  "t&ecirc;te en entendant sa proposition, sachant, comme "
  "toujours, exactement &agrave; quel point ce d&eacute;tour compte "
  "pour elle autant que pour lui-m&ecirc;me, apr&egrave;s une "
  "journ&eacute;e aussi charg&eacute;e en r&eacute;v&eacute;lations et en incertitudes "
  "nouvelles.")

p("Franck repense, tout en conduisant, &agrave; cette derni&egrave;re "
  "image d'Ambroise Vasseur sur le pas de la porte de "
  "la propri&eacute;t&eacute;, les saluant d'un signe de t&ecirc;te presque "
  "chaleureux, comme s'il s'agissait d'une simple visite "
  "de courtoisie entre voisins plut&ocirc;t que d'une rencontre "
  "capable de bouleverser d&eacute;finitivement leur "
  "compr&eacute;hension de tout ce qu'ils croyaient savoir sur "
  "la Marge et son fonctionnement.")

name("FRANCK")
p("&laquo;&nbsp;Vous avez remarqu&eacute; comme il &eacute;tait calme, "
  "Ambroise Vasseur, pendant tout l'entretien ? Genre, "
  "anormalement calme, pour quelqu'un qui vient de "
  "nous r&eacute;v&eacute;ler l'existence d'un r&eacute;seau mondial secret. "
  "&Ccedil;a m'a paru presque plus inqui&eacute;tant que s'il avait "
  "&eacute;t&eacute; nerveux, en fait.&nbsp;&raquo;")

p("Clara acquiesce, ayant remarqu&eacute; elle aussi cette "
  "s&eacute;r&eacute;nit&eacute; presque d&eacute;rangeante chez leur h&ocirc;te, cette "
  "assurance tranquille d'un homme convaincu, "
  "profond&eacute;ment et depuis longtemps, du bien-fond&eacute; de "
  "sa d&eacute;marche, quelle qu'en soit la nature exacte "
  "encore &agrave; d&eacute;couvrir.")

name("CLARA")
p("&laquo;&nbsp;C'est le calme des gens qui ont d&eacute;j&agrave; tout "
  "d&eacute;cid&eacute; depuis longtemps, je crois. Pas celui des "
  "gens qui h&eacute;sitent encore. &Ccedil;a me fait froid dans le "
  "dos d'y penser, en fait, maintenant que je le "
  "formule &agrave; voix haute.&nbsp;&raquo;")

p("Ils roulent en silence quelques minutes "
  "suppl&eacute;mentaires, chacun ruminant &agrave; sa mani&egrave;re cette "
  "impression partag&eacute;e d'avoir affront&eacute;, sans le savoir "
  "pleinement sur le moment, quelque chose de bien "
  "plus d&eacute;cid&eacute; et abouti que ce que la simple "
  "pr&eacute;sentation d'Ambroise Vasseur avait bien voulu "
  "leur laisser deviner.")

name("ALEX")
p("&laquo;&nbsp;Vous avez vu la fa&ccedil;on dont Odile le regardait, "
  "&agrave; un moment donn&eacute; ? J'ai eu l'impression qu'elle "
  "&eacute;tait pas totalement d'accord avec lui, mais qu'elle "
  "le suivait quand m&ecirc;me, genre par loyaut&eacute; plus que "
  "par conviction. &Ccedil;a m'a paru bizarre, ce d&eacute;calage "
  "entre eux deux.&nbsp;&raquo;")

p("Clara confirme avoir remarqu&eacute; ce m&ecirc;me d&eacute;tail, "
  "cette h&eacute;sitation fugace mais r&eacute;elle chez la femme "
  "&acirc;g&eacute;e, et se demande, &agrave; voix haute, si cette faille "
  "apparente dans l'unit&eacute; de l'organisation pourrait, un "
  "jour, repr&eacute;senter une voie d'acc&egrave;s suppl&eacute;mentaire "
  "pour mieux comprendre, ou peut-&ecirc;tre m&ecirc;me "
  "contrecarrer, les intentions exactes d'Ambroise "
  "Vasseur.")

name("CLARA")
p("&laquo;&nbsp;Si jamais on doit un jour agir contre eux, "
  "plut&ocirc;t qu'avec eux, Odile pourrait &ecirc;tre notre seul "
  "point d'entr&eacute;e. Faudra s'en souvenir, si jamais &ccedil;a "
  "tourne mal.&nbsp;&raquo;")

p("Franck, silencieux depuis un moment, hoche "
  "lentement la t&ecirc;te, absorbant cette observation "
  "suppl&eacute;mentaire avec la m&ecirc;me gravit&eacute; qu'il applique "
  "d&eacute;sormais &agrave; chaque d&eacute;tail de cette rencontre "
  "&eacute;trange, conscient qu'ils viennent probablement "
  "d'identifier, sans le chercher activement, une "
  "faiblesse potentielle dans ce qui semblait, de "
  "prime abord, une organisation parfaitement "
  "unifi&eacute;e et d&eacute;termin&eacute;e.")

p("Ils repensent, chacun en silence, &agrave; la longue "
  "explication qu'Ambroise Vasseur leur avait offerte "
  "quelques heures plus t&ocirc;t, avant m&ecirc;me qu'ils ne "
  "d&eacute;couvrent la biblioth&egrave;que priv&eacute;e et ce grimoire "
  "compromettant, un discours pr&eacute;par&eacute; de longue date, "
  "visiblement, tant il coulait avec la fluidit&eacute; d'un "
  "argumentaire mille fois r&eacute;p&eacute;t&eacute; devant d'autres "
  "visiteurs avant eux.")

name("A. VASSEUR")
p("&laquo;&nbsp;Mon grand-p&egrave;re croyait pouvoir dompter la "
  "Marge par la science seule &mdash; des protocoles, des "
  "mesures, des grilles d'&eacute;valuation. Il n'avait pas tort "
  "de vouloir comprendre, seulement tort sur la "
  "m&eacute;thode. On ne dompte pas une rivi&egrave;re en "
  "l'&eacute;tudiant depuis la berge. Il faut y entrer, "
  "accepter d'en porter une part en soi, pour "
  "esp&eacute;rer un jour la comprendre assez pour la "
  "n&eacute;gocier &agrave; l'&eacute;chelle qu'elle m&eacute;rite.&nbsp;&raquo;")

p("Il leur avait expliqu&eacute;, avec une patience "
  "p&eacute;dagogique presque professorale, comment il avait "
  "pass&eacute; sa jeunesse enti&egrave;re &agrave; retrouver, un &agrave; un, "
  "les t&eacute;moins survivants du programme de son "
  "grand-p&egrave;re, convainquant patiemment chacun "
  "d'entre eux de rejoindre une organisation "
  "naissante, b&acirc;tie sur la conviction que seule une "
  "action coordonn&eacute;e &agrave; grande &eacute;chelle pourrait, un "
  "jour, mettre fin d&eacute;finitivement au cycle de "
  "souffrance impos&eacute; par la Marge &agrave; chaque nouvelle "
  "g&eacute;n&eacute;ration de porteurs.")

name("A. VASSEUR")
p("&laquo;&nbsp;Vous devez comprendre que je ne suis pas "
  "mon grand-p&egrave;re. Il voyait les patients comme des "
  "sujets d'&eacute;tude. Moi je les vois comme des "
  "coll&egrave;gues, des partenaires dans une entreprise qui "
  "nous d&eacute;passe tous individuellement. C'est pour "
  "&ccedil;a que je documente chaque histoire avec autant "
  "de soin &mdash; parce que chacune compte, chacune "
  "nourrit notre compr&eacute;hension collective d'un "
  "ph&eacute;nom&egrave;ne qu'aucun individu isol&eacute; ne pourra "
  "jamais appr&eacute;hender enti&egrave;rement seul.&nbsp;&raquo;")

p("Franck, &agrave; l'&eacute;poque, avait &eacute;cout&eacute; ce discours avec "
  "un m&eacute;lange de scepticisme et de fascination "
  "malgr&eacute; lui, reconnaissant dans la voix d'Ambroise "
  "Vasseur cette m&ecirc;me conviction inébranlable qu'il "
  "avait autrefois per&ccedil;ue, br&iuml;&egrave;vement, dans les yeux "
  "de son propre fr&egrave;re enfant, cette certitude "
  "absolue de participer &agrave; quelque chose de plus "
  "grand que soi.")

name("FRANCK")
p("&laquo;&nbsp;Et concr&egrave;tement, cette 'action coordonn&eacute;e &agrave; "
  "grande &eacute;chelle', &ccedil;a consiste en quoi ? Vous parlez "
  "toujours en g&eacute;n&eacute;ralit&eacute;s nobles, mais j'aimerais "
  "des d&eacute;tails pr&eacute;cis sur ce que vous comptez "
  "vraiment faire, et quand.&nbsp;&raquo;")

p("Ambroise Vasseur avait souri, cette fois, d'un "
  "sourire &eacute;nigmatique qui n'avait rien r&eacute;v&eacute;l&eacute; de "
  "concret, se contentant de r&eacute;pondre que &laquo;&nbsp;le moment "
  "venu, tout deviendrait parfaitement clair pour "
  "tous&nbsp;&raquo;, une formule dont Clara, Alex et Franck "
  "comprennent d&eacute;sormais, avec le recul de cette "
  "d&eacute;couverte troublante dans la biblioth&egrave;que priv&eacute;e, "
  "&agrave; quel point elle dissimulait une v&eacute;ritable intention "
  "d'action imminente plut&ocirc;t qu'une simple philosophie "
  "abstraite.")

p("Le trajet de retour se poursuit ainsi, ponctu&eacute; de "
  "ces reconstitutions partag&eacute;es de la conversation, "
  "chacun apportant un d&eacute;tail suppl&eacute;mentaire remarqu&eacute; "
  "&agrave; sa mani&egrave;re, jusqu'&agrave; ce qu'ils parviennent, "
  "collectivement, &agrave; reconstituer une image beaucoup "
  "plus compl&egrave;te et beaucoup plus inqui&eacute;tante de la "
  "v&eacute;ritable nature de leur h&ocirc;te que ce que chacun "
  "d'entre eux avait pu percevoir isol&eacute;ment sur le "
  "moment.")

p("Clara ressort &eacute;galement, de sa m&eacute;moire, un dernier "
  "&eacute;change avec Ambroise Vasseur survenu juste avant "
  "leur d&eacute;part, une question qu'elle lui avait pos&eacute;e "
  "presque par politesse et dont la r&eacute;ponse, sur le "
  "moment anodine, prend d&eacute;sormais une r&eacute;sonance "
  "beaucoup plus inqui&eacute;tante.")

name("CLARA")
p("&laquo;&nbsp;Je lui avais demand&eacute; ce qu'il ferait si un "
  "porteur, ou un t&eacute;moin proche, refusait de "
  "collaborer avec son organisation. Il m'a r&eacute;pondu "
  "qu'il esp&eacute;rait sinc&egrave;rement ne jamais avoir &agrave; "
  "affronter cette situation, mais que 'l'histoire, "
  "parfois, ne laisse pas vraiment le choix &agrave; "
  "personne.' Sur le moment j'ai trouv&eacute; &ccedil;a "
  "philosophique. Maintenant &ccedil;a me para&icirc;t carr&eacute;ment "
  "menaçant.&nbsp;&raquo;")

p("Alex, entendant cette reformulation, sent sa "
  "propre inqui&eacute;tude grimper d'un cran "
  "suppl&eacute;mentaire, comprenant que cette phrase "
  "pourrait tr&egrave;s bien s'appliquer directement &agrave; "
  "eux-m&ecirc;mes, s'ils venaient un jour &agrave; repr&eacute;senter un "
  "obstacle aux plans encore myst&eacute;rieux d'Ambroise "
  "Vasseur et de son r&eacute;seau &eacute;tendu.")

name("ALEX")
p("&laquo;&nbsp;J'esp&egrave;re vraiment qu'on n'aura jamais &agrave; "
  "d&eacute;couvrir ce que &ccedil;a signifie concr&egrave;tement, cette "
  "phrase. Parce que si Darius a &eacute;t&eacute; consid&eacute;r&eacute; comme "
  "un obstacle un jour, j'ai pas tr&egrave;s envie de savoir ce "
  "qui arrive aux obstacles selon eux.&nbsp;&raquo;")

p("Franck, arrivant enfin en vue de sa propre maison "
  "sur le coteau, ralentit la voiture et coupe le "
  "moteur, mais aucun d'entre eux ne fait mine de "
  "descendre imm&eacute;diatement, chacun pr&eacute;f&eacute;rant "
  "prolonger encore quelques minutes cette "
  "conversation collective qui, d'une mani&egrave;re "
  "&eacute;trange, les rassure malgr&eacute; la gravit&eacute; de son "
  "contenu, simplement parce qu'elle est partag&eacute;e "
  "plut&ocirc;t que ressassée en silence.")

name("FRANCK")
p("&laquo;&nbsp;Quoi qu'il arrive maintenant, on l'affrontera "
  "ensemble, comme on l'a toujours fait. Darius nous "
  "a appris &ccedil;a, et je compte bien continuer &agrave; "
  "l'honorer de cette mani&egrave;re, quoi qu'Ambroise "
  "Vasseur et son organisation nous r&eacute;servent "
  "d&eacute;sormais.&nbsp;&raquo;")

p("Clara acquiesce silencieusement, resserrant "
  "instinctivement son &eacute;charpe autour de son cou "
  "contre le froid qui commence &agrave; s'infiltrer dans "
  "l'habitacle d&eacute;sormais que le moteur est coup&eacute;, et "
  "tous trois restent encore un moment silencieux, "
  "chacun rassemblant le courage n&eacute;cessaire pour "
  "affronter la suite de cette soir&eacute;e d&eacute;j&agrave; si dense en "
  "&eacute;motions et en r&eacute;v&eacute;lations.")

p("Alex finit par rompre ce silence, proposant, "
  "avec cette pragmatisme qui le caract&eacute;rise "
  "toujours face &agrave; l'adversit&eacute;, d'&eacute;tablir d&egrave;s ce soir "
  "un plan d'action concret pour les jours suivants, "
  "refusant de laisser cette d&eacute;couverte troublante "
  "les paralyser sans r&eacute;action pratique.")

name("ALEX")
p("&laquo;&nbsp;Demain, on rassemble tout ce qu'on a "
  "not&eacute; aujourd'hui, on compare nos souvenirs "
  "pendant qu'ils sont encore frais, et on d&eacute;cide "
  "ensemble de la suite. Pas question de laisser &ccedil;a "
  "nous ronger sans rien faire de concret avec.&nbsp;&raquo;")

p("Cette proposition, accueillie avec soulagement "
  "par Clara et Franck, tous deux appr&eacute;ciant cette "
  "capacit&eacute; d'Alex &agrave; transformer l'angoisse en action "
  "structur&eacute;e, scelle leur d&eacute;cision commune de se "
  "retrouver d&egrave;s le lendemain matin pour entamer "
  "s&eacute;rieusement l'analyse de tout ce qu'ils viennent "
  "d'apprendre sur Ambroise Vasseur et son "
  "organisation &eacute;tendue.")

p("Avant de descendre enfin de la voiture, Franck "
  "se retourne vers Clara et Alex, install&eacute;s &agrave; "
  "l'arri&egrave;re, et leur adresse un dernier regard "
  "empreint d'une gravit&eacute; toute particuli&egrave;re, "
  "conscient que cette soir&eacute;e marque, d'une mani&egrave;re "
  "ou d'une autre, un tournant d&eacute;cisif dans leur "
  "histoire commune.")

name("FRANCK")
p("&laquo;&nbsp;Merci d'&ecirc;tre l&agrave;, tous les deux. Sans vous, "
  "j'aurais jamais eu le courage d'affronter tout &ccedil;a. "
  "Darius avait vraiment de la chance de vous avoir "
  "comme amis, et moi j'ai de la chance de vous "
  "avoir comme famille, maintenant.&nbsp;&raquo;")

p("Cette d&eacute;claration simple mais sinc&egrave;re clôture "
  "cette longue soir&eacute;e sur une note d'unit&eacute; et de "
  "d&eacute;termination partag&eacute;e, chacun des trois "
  "descendant finalement de la voiture avec la "
  "certitude renouvel&eacute;e qu'ils affronteront, quoi "
  "qu'il advienne d&eacute;sormais, cette menace grandissante "
  "exactement comme ils ont toujours affront&eacute; "
  "l'adversit&eacute; depuis le d&eacute;but de cette histoire &mdash; "
  "ensemble, sans exception.")

p("Clara et Alex marchent ensemble jusqu'&agrave; l'arr&ecirc;t "
  "de bus le plus proche, silencieux dans "
  "l'obscurit&eacute; grandissante, chacun perdu dans ses "
  "propres pens&eacute;es concernant tout ce que cette "
  "journ&eacute;e extraordinaire vient de r&eacute;v&eacute;ler sur "
  "l'ampleur r&eacute;elle de l'histoire &agrave; laquelle ils sont "
  "m&ecirc;l&eacute;s depuis tant d'ann&eacute;es d&eacute;sormais.")

name("ALEX")
p("&laquo;&nbsp;Onze ans, Clara. &Ccedil;a fait onze ans qu'on "
  "porte &ccedil;a. J'aurais jamais cru, quand on &eacute;tait "
  "gamins devant cette vitrine, qu'on serait encore "
  "l&agrave;-dedans plus d'une d&eacute;cennie plus tard.&nbsp;&raquo;")

p("Clara acquiesce silencieusement, songeant, elle "
  "aussi, &agrave; tout le chemin parcouru depuis cette "
  "premi&egrave;re nuit de f&eacute;vrier o&ugrave; Darius leur avait "
  "montr&eacute; cette photographie floue d'un collier "
  "suspendu dans le vide, incapable, &agrave; l'&eacute;poque, "
  "d'imaginer &agrave; quel point cette d&eacute;couverte "
  "changerait d&eacute;finitivement le cours de leurs trois "
  "existences enti&egrave;res.")

name("CLARA")
p("&laquo;&nbsp;Tu crois qu'on aurait fait pareil, si on "
  "avait su &agrave; l'&eacute;poque tout ce que &ccedil;a nous "
  "co&ucirc;terait ? Si on avait su pour Darius, pour tout "
  "&ccedil;a ?&nbsp;&raquo;")

p("Alex r&eacute;fl&eacute;chit longuement &agrave; cette question "
  "avant de r&eacute;pondre, pesant honn&ecirc;tement chaque mot "
  "avant de les prononcer, conscient de "
  "l'importance de cette r&eacute;flexion partag&eacute;e sur le "
  "sens profond de leur engagement mutuel depuis "
  "toutes ces ann&eacute;es.")

name("ALEX")
p("&laquo;&nbsp;Ouais. J'crois que oui, malgr&eacute; tout. Darius "
  "&eacute;tait notre ami, et on l'aurait jamais laiss&eacute; "
  "affronter &ccedil;a tout seul, m&ecirc;me en sachant le prix &agrave; "
  "payer. C'est &ccedil;a, l'amiti&eacute; v&eacute;ritable, je crois "
  "&mdash; continuer &agrave; choisir la m&ecirc;me chose, m&ecirc;me "
  "quand on conna&icirc;t d&eacute;j&agrave; le co&ucirc;t.&nbsp;&raquo;")

p("Clara serre la main d'Alex un bref instant, "
  "scellant silencieusement cet &eacute;change intime avant "
  "que chacun ne rentre finalement chez soi, "
  "port&eacute; par cette certitude renouvel&eacute;e que leur "
  "engagement mutuel, forg&eacute; par onze ann&eacute;es "
  "d'&eacute;preuves partag&eacute;es, ne fl&eacute;chira jamais, quoi "
  "que l'avenir puisse encore leur r&eacute;server.")

p("Cette nuit-l&agrave;, chacun de leur c&ocirc;t&eacute;, Clara et Alex "
  "s'endorment avec la m&ecirc;me pens&eacute;e confuse "
  "flottant dans leur esprit fatigu&eacute; &mdash; celle d'avoir "
  "franchi, ce jour-l&agrave;, un seuil important dans leur "
  "compr&eacute;hension de l'ampleur r&eacute;elle de l'histoire "
  "&agrave; laquelle ils appartiennent depuis l'enfance, "
  "sans encore savoir &agrave; quel point cette journ&eacute;e "
  "allait, r&eacute;trospectivement, marquer un tournant "
  "d&eacute;cisif dans le cours de leur existence enti&egrave;re.")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 11 &mdash;", chapter_label))
S.append(PageBreak())

# ======================================================================
# CHAPITRE 12 -- LA FIN DU MONDE
# ======================================================================
chap(12, "LA FIN DU MONDE")

p("Le retour vers Luynes prend, ce soir-l&agrave;, une allure "
  "diff&eacute;rente de tous les autres trajets similaires "
  "effectu&eacute;s au fil des ann&eacute;es, la petite Renault de "
  "Franck traversant des hameaux endormis dont les "
  "lumi&egrave;res, une &agrave; une, s'&eacute;teignent &agrave; mesure que la "
  "soir&eacute;e avance, comme si la vall&eacute;e enti&egrave;re se "
  "pr&eacute;parait, sans le savoir, &agrave; une nuit diff&eacute;rente de "
  "toutes les pr&eacute;c&eacute;dentes.")

p("Alex, regardant par la vitre les silhouettes sombres "
  "des vignobles d&eacute;filer dans l'obscurit&eacute;, repense &agrave; "
  "cette carte aper&ccedil;ue dans la biblioth&egrave;que priv&eacute;e "
  "d'Ambroise Vasseur, &agrave; cette mention glaciale "
  "concernant Darius consid&eacute;r&eacute; comme un obstacle "
  "plut&ocirc;t qu'une victime, et sent grandir en lui une "
  "col&egrave;re froide qu'il ne s'&eacute;tait pas autoris&eacute;e jusque-l&agrave;, "
  "trop occup&eacute; &agrave; digérer le choc des r&eacute;v&eacute;lations pour "
  "vraiment la ressentir pleinement.")

p("Clara, silencieuse &agrave; c&ocirc;t&eacute; de lui sur la banquette "
  "arri&egrave;re, ressent cette m&ecirc;me col&egrave;re contenue "
  "monter en elle par vagues successives, chaque "
  "kilom&egrave;tre parcouru lui laissant le temps "
  "suppl&eacute;mentaire de mesurer, un peu plus, l'ampleur "
  "de la trahison implicite contenue dans cette "
  "mention retrouv&eacute;e dans le grimoire d'Ambroise "
  "Vasseur.")

name("CLARA")
p("&laquo;&nbsp;Toutes ces ann&eacute;es &agrave; se dire que c'&eacute;tait "
  "une organisation bienveillante, qui voulait "
  "juste comprendre et documenter. Et en fait, ils "
  "voyaient Darius comme un simple probl&egrave;me &agrave; "
  "&eacute;liminer de leur &eacute;quation. &Ccedil;a change tout, "
  "cette d&eacute;couverte. Absolument tout.&nbsp;&raquo;")

name("ALEX")
p("&laquo;&nbsp;Je peux pas m'emp&ecirc;cher de penser &agrave; ce "
  "grimoire, l&agrave;-bas. 'Compromettre nos plans.' Ils "
  "voyaient Darius comme un probl&egrave;me &agrave; g&eacute;rer, "
  "Franck, pas comme quelqu'un qui m&eacute;ritait d'&ecirc;tre "
  "sauv&eacute;. &Ccedil;a me rend malade d'y penser, l&agrave;, "
  "maintenant.&nbsp;&raquo;")

p("Franck, les mains crisp&eacute;es sur le volant, ne r&eacute;pond "
  "pas imm&eacute;diatement, absorbant cette information "
  "suppl&eacute;mentaire avec la m&ecirc;me lenteur douloureuse "
  "qu'il applique d&eacute;sormais &agrave; chaque nouvelle r&eacute;v&eacute;lation "
  "concernant cette histoire familiale trop vaste pour "
  "&ecirc;tre enti&egrave;rement digérée d'un seul coup, m&ecirc;me apr&egrave;s "
  "onze ann&eacute;es de pratique.")

name("FRANCK")
p("&laquo;&nbsp;Je sais pas ce qui me terrifie le plus, "
  "franchement &mdash; qu'ils aient vu mon fils comme un "
  "obstacle, ou qu'ils continuent, ce soir m&ecirc;me, &agrave; "
  "poursuivre un plan qui nous consid&eacute;rait tous, depuis "
  "le d&eacute;but, comme de simples variables &agrave; g&eacute;rer plut&ocirc;t "
  "que comme des &ecirc;tres humains.&nbsp;&raquo;")

p("Clara, silencieuse depuis un moment, sort "
  "discr&egrave;tement son t&eacute;l&eacute;phone pour noter, avant que le "
  "souvenir ne s'estompe, la phrase exacte lue dans le "
  "grimoire, consciente qu'un jour, peut-&ecirc;tre, cette "
  "preuve suppl&eacute;mentaire pourrait s'av&eacute;rer d&eacute;cisive "
  "pour comprendre enfin la nature exacte des intentions "
  "d'Ambroise Vasseur et de son organisation.")

p("Ils traversent, en silence, le petit pont enjambant "
  "un affluent de la Loire, ce m&ecirc;me pont que Darius "
  "avait travers&eacute; des centaines de fois &agrave; v&eacute;lo durant "
  "son enfance, sans jamais imaginer &agrave; quel point sa "
  "propre existence serait, un jour, r&eacute;duite &agrave; une simple "
  "ligne dans un registre tenu par des inconnus "
  "convaincus d'agir pour le bien commun.")

S.append(rule())
S.append(PageBreak())

p("Franck engage la voiture sur la petite route sinueuse "
  "menant au cimeti&egrave;re, ralentissant encore &agrave; l'approche "
  "du dernier virage, celui-l&agrave; m&ecirc;me qu'il avait pris, onze "
  "ans plus t&ocirc;t, en pleine panique, roulant bien trop vite "
  "vers l'appartement de son ex-femme apr&egrave;s des appels "
  "rest&eacute;s sans r&eacute;ponse, et ce souvenir pr&eacute;cis, resurgi "
  "sans pr&eacute;venir, lui serre la gorge d'une mani&egrave;re qu'il "
  "n'aurait pas anticip&eacute;e ce soir.")

p("Clara, per&ccedil;evant ce changement subtil dans "
  "l'attitude de Franck, tend une main r&eacute;confortante "
  "vers son &eacute;paule, un geste simple qu'elle a appris, au "
  "fil des ann&eacute;es, &agrave; accomplir naturellement chaque fois "
  "que le chagrin de cet homme menace de le "
  "submerger sans qu'il n'ose jamais vraiment l'exprimer "
  "&agrave; voix haute.")

p("Alex, sur la banquette arri&egrave;re aux c&ocirc;t&eacute;s de "
  "Clara, observe en silence la nuque tendue de "
  "Franck, reconnaissant lui aussi ce m&ecirc;me chemin "
  "parcouru chaque ann&eacute;e avec la m&ecirc;me appr&eacute;hension "
  "muette, et se demande, une fois de plus, si "
  "cette douleur particuli&egrave;re finira, un jour, par "
  "s'att&eacute;nuer v&eacute;ritablement, ou si elle restera, "
  "&agrave; jamais, aussi vive qu'au premier jour.")

name("CLARA")
p("&laquo;&nbsp;&Ccedil;a va, Franck ? On peut faire une pause si "
  "vous voulez, avant d'y arriver. Y'a pas d'urgence, "
  "cette fois. On a tout le temps qu'il faut, "
  "d&eacute;sormais.&nbsp;&raquo;")

name("FRANCK")
p("&laquo;&nbsp;&Ccedil;a va aller, Clara. Merci. C'est juste que ce "
  "chemin-l&agrave;, je le prends toujours avec la m&ecirc;me "
  "boule au ventre, m&ecirc;me apr&egrave;s onze ans. Je crois que "
  "&ccedil;a partira jamais totalement, en fait. Et c'est "
  "peut-&ecirc;tre bien comme &ccedil;a, remarquez. &Ccedil;a veut dire "
  "que &ccedil;a compte encore, autant qu'au premier "
  "jour.&nbsp;&raquo;")

p("Alex, silencieux &agrave; l'arri&egrave;re, observe par la vitre le "
  "paysage nocturne d&eacute;filer, les vignes endormies sous "
  "le ciel &eacute;toil&eacute; de f&eacute;vrier, et se surprend &agrave; penser, "
  "une fois de plus, &agrave; quel point cette petite r&eacute;gion "
  "tranquille, si familiere depuis l'enfance, continue de "
  "receler, sous son apparente banalit&eacute;, des secrets d'une "
  "ampleur que peu d'endroits au monde pourraient "
  "&eacute;galer.")

p("Il repense &agrave; la carte entraper&ccedil;ue &agrave; Fondettes, &agrave; "
  "ces dizaines de points lumineux dispers&eacute;s &agrave; travers "
  "le pays et au-del&agrave;, et &agrave; cette phrase de l'homme "
  "discret rencontr&eacute; dans le jardin d'hiver, &laquo;&nbsp;ils "
  "promettent beaucoup, ils expliquent moins qu'on "
  "voudrait&nbsp;&raquo;, qui r&eacute;sonne encore en lui avec une "
  "insistance particuli&egrave;re, comme un avertissement qu'il "
  "ne parvient pas &agrave; totalement &eacute;carter de son esprit.")

p("La voiture franchit enfin le dernier virage, les "
  "premi&egrave;res pierres tombales apparaissant dans la "
  "p&eacute;nombre &agrave; la lueur des phares, et Franck coupe le "
  "moteur, ce silence soudain remplac&eacute; presque "
  "aussit&ocirc;t par le bruissement discret du vent dans les "
  "arbres du cimeti&egrave;re, ce m&ecirc;me vent qui, onze ans plus "
  "t&ocirc;t, avait port&eacute; jusqu'&agrave; eux, &agrave; Amboise, une phrase "
  "glaciale dont ils n'avaient jamais totalement per&ccedil;u "
  "l'ampleur exacte de la menace.")

p("Ils descendent tous les trois de la voiture en silence, "
  "le froid de f&eacute;vrier les saisissant imm&eacute;diatement, et "
  "marchent ensemble entre les rang&eacute;es de pierres "
  "tombales jusqu'&agrave; cette petite parcelle famili&egrave;re o&ugrave; "
  "reposent d&eacute;sormais, c&ocirc;te &agrave; c&ocirc;te, Darius et, un peu "
  "plus loin, dans une partie plus ancienne du cimeti&egrave;re, "
  "les grands-parents de Franck qu'aucun d'eux n'a "
  "jamais connus.")

p("Le gravier crisse sous leurs pas dans le silence "
  "presque absolu du cimeti&egrave;re nocturne, seulement "
  "troubl&eacute; par le bruissement lointain des arbres agit&eacute;s "
  "par une brise l&eacute;g&egrave;re, et chacun ralentit "
  "instinctivement en approchant de la tombe famili&egrave;re, "
  "comme si une force invisible imposait, &agrave; cet "
  "endroit pr&eacute;cis, un respect qu'aucun mot n'aurait "
  "besoin d'exprimer.")

p("Clara s'arr&ecirc;te un instant devant une troisi&egrave;me "
  "pierre, plus modeste, install&eacute;e quelques ann&eacute;es "
  "plus t&ocirc;t &agrave; la demande expresse de Templier "
  "lui-m&ecirc;me avant sa mort &mdash; un simple m&eacute;morial "
  "symbolique d&eacute;di&eacute; &agrave; sa petite s&oelig;ur disparue en 1979, "
  "dont le corps n'avait jamais &eacute;t&eacute; retrouv&eacute;, mais dont "
  "il avait tenu &agrave; marquer, malgr&eacute; tout, le souvenir "
  "quelque part de tangible.")

name("CLARA")
p("&laquo;&nbsp;Vous savez, je crois vraiment que c'&eacute;tait elle, "
  "&agrave; Fondettes. Odile. Templier serait tellement "
  "soulag&eacute; de savoir qu'elle a fini par retrouver un "
  "chemin, m&ecirc;me partiel, m&ecirc;me des d&eacute;cennies plus "
  "tard. &Ccedil;a me donne un peu d'espoir, en fait, malgr&eacute; "
  "tout le reste.&nbsp;&raquo;")

p("Franck acquiesce silencieusement, touch&eacute; par cette "
  "id&eacute;e qu'une dissolution, aussi compl&egrave;te para&icirc;t-elle "
  "sur le moment, ne signifie peut-&ecirc;tre pas toujours une "
  "fin d&eacute;finitive, et pense, une fois de plus, &agrave; son propre "
  "fr&egrave;re, quelque part, dilu&eacute; mais pas &eacute;teint, esp&eacute;rant "
  "de tout son c&oelig;ur qu'un jour, lui aussi, trouvera "
  "peut-&ecirc;tre un semblant de chemin vers lui-m&ecirc;me.")

p("Alex, s'&eacute;loignant l&eacute;g&egrave;rement du groupe pour laisser "
  "&agrave; Clara et Franck un moment plus intime devant la "
  "tombe de Darius, s'arr&ecirc;te pr&egrave;s de la lisi&egrave;re du petit "
  "bois bordant le cimeti&egrave;re, l&agrave; m&ecirc;me o&ugrave; Clara avait "
  "cru apercevoir, l'ann&eacute;e pr&eacute;c&eacute;dente, deux silhouettes "
  "immobiles les observant depuis la p&eacute;nombre.")

p("Il ne voit rien, cette fois, seulement les arbres nus "
  "se balan&ccedil;ant doucement sous la brise nocturne, et "
  "&eacute;prouve, malgr&eacute; cette absence rassurante de tout signe "
  "suspect, une sensation diffuse et t&eacute;nace d'&ecirc;tre, "
  "malgr&eacute; tout, observ&eacute; depuis quelque part qu'il ne "
  "saurait localiser pr&eacute;cis&eacute;ment.")

p("Franck s'agenouille, avec la lenteur pr&eacute;caution neuse "
  "d'un homme dont les articulations rappellent d&eacute;sormais "
  "chaque ann&eacute;e suppl&eacute;mentaire, devant la pierre "
  "tombale de son fils, et pose sa main &agrave; plat sur la "
  "surface froide de la pierre, exactement comme il le "
  "fait chaque ann&eacute;e depuis onze ans, cherchant dans ce "
  "contact simple une forme de communication qui "
  "d&eacute;passe largement tout ce que les mots pourraient "
  "exprimer.")

name("FRANCK")
p("&laquo;&nbsp;On a appris des trucs, aujourd'hui, fiston. Des "
  "trucs &eacute;normes, en fait. Je sais pas encore quoi en "
  "penser. Mais je voulais que tu saches, avant tout le "
  "reste, que je suis toujours aussi fier de toi qu'au "
  "premier jour. &Ccedil;a, &ccedil;a change jamais, quoi qu'on "
  "d&eacute;couvre par ailleurs.&nbsp;&raquo;")

p("Clara, &agrave; genoux elle aussi de l'autre c&ocirc;t&eacute; de la "
  "tombe, ferme les yeux un instant, laissant remonter "
  "en elle, comme chaque ann&eacute;e, cette pri&egrave;re "
  "personnelle qu'elle n'a jamais partag&eacute;e enti&egrave;rement "
  "avec personne, pas m&ecirc;me avec Alex, un dialogue "
  "silencieux qu'elle entretient avec son ami disparu "
  "depuis maintenant plus d'une d&eacute;cennie.")

p("Elle pense &agrave; tout ce chemin parcouru depuis la "
  "vitrine sous la pluie, &agrave; Miel, &agrave; l'entrep&ocirc;t, &agrave; la "
  "grotte, au Non-lieu, &agrave; Templier, &agrave; Amboise, &agrave; "
  "chaque &eacute;tape de cette histoire extraordinaire qu'elle a "
  "eu le privil&egrave;ge, malgr&eacute; toute la douleur qu'elle a "
  "engendr&eacute;e, de vivre aux c&ocirc;t&eacute;s de Darius, et ressent, "
  "une fois de plus, cette gratitude &eacute;trange qui "
  "accompagne toujours son chagrin, sans jamais "
  "vraiment le remplacer.")

p("Alex, revenu se joindre &agrave; eux devant la tombe, "
  "d&eacute;pose sa fleur habituelle issue de la vigne de "
  "Templier, et reste debout, silencieux, les mains dans "
  "les poches, laissant Franck et Clara terminer leurs "
  "propres dialogues int&eacute;rieurs avant de prendre, &agrave; son "
  "tour, un moment pour lui-m&ecirc;me devant cette pierre "
  "devenue, au fil des ann&eacute;es, presque un membre "
  "&agrave; part enti&egrave;re de leur petit groupe.")

name("ALEX")
p("&laquo;&nbsp;On va continuer &agrave; se battre pour comprendre "
  "tout &ccedil;a, Darius. Sans jamais oublier ce que tu nous "
  "as appris. Promis.&nbsp;&raquo;")

p("Ils restent encore un moment, tous les trois, debout "
  "c&ocirc;te &agrave; c&ocirc;te devant la tombe, contemplant en silence "
  "le ciel d&eacute;sormais compl&egrave;tement noir au-dessus de "
  "Luynes, cribl&eacute; d'&eacute;toiles que la faible pollution "
  "lumineuse de cette petite commune laisse "
  "g&eacute;n&eacute;reusement appara&icirc;tre, contrairement aux villes "
  "plus grandes o&ugrave; Clara et Alex passent d&eacute;sormais "
  "l'essentiel de leur temps.")

p("Franck l&egrave;ve les yeux vers ce ciel &eacute;toil&eacute;, pensant, "
  "comme chaque ann&eacute;e &agrave; ce m&ecirc;me endroit, &agrave; quel "
  "point l'univers para&icirc;t &agrave; la fois immense et "
  "incroyablement intime, capable de contenir, dans le "
  "m&ecirc;me espace infini, &agrave; la fois la petite existence "
  "tragique et magnifique de son fils, et cette "
  "organisation vaste et myst&eacute;rieuse qu'ils viennent tout "
  "juste de d&eacute;couvrir &agrave; Fondettes.")

name("FRANCK")
p("&laquo;&nbsp;Vous savez, malgr&eacute; tout ce qu'on a appris "
  "aujourd'hui, malgr&eacute; toutes ces inqui&eacute;tudes "
  "nouvelles, j'arrive quand m&ecirc;me &agrave; ressentir un peu de "
  "paix, l&agrave;, maintenant, avec vous deux, devant cette "
  "tombe. C'est peut-&ecirc;tre &ccedil;a, le vrai secret, en fait &mdash; "
  "pas de tout comprendre, juste de continuer &agrave; &ecirc;tre "
  "l&agrave; les uns pour les autres.&nbsp;&raquo;")

p("Clara acquiesce silencieusement, glissant sa main "
  "dans celle d'Alex sans y penser vraiment, ce geste "
  "devenu, au fil des ann&eacute;es de deuil partag&eacute;, aussi "
  "naturel qu'un simple r&eacute;flexe, et tous trois demeurent "
  "ainsi encore de longues minutes, immobiles sous les "
  "&eacute;toiles, sans qu'aucun mot suppl&eacute;mentaire ne semble "
  "n&eacute;cessaire pour combler ce silence pourtant si "
  "charg&eacute; de sens.")

p("Ils finissent par regagner la voiture, un peu apr&egrave;s "
  "vingt-deux heures, le froid ayant fini par les gagner "
  "malgr&eacute; leurs manteaux d'hiver, et Franck d&eacute;marre "
  "doucement le moteur, jetant un dernier regard dans "
  "le r&eacute;troviseur vers la petite parcelle qu'ils "
  "s'appr&ecirc;tent &agrave; quitter, avant de reprendre la route "
  "sinueuse menant hors du cimeti&egrave;re.")

p("Le trajet qui les ram&egrave;ne, dans l'obscurit&eacute; compl&egrave;te, "
  "vers le centre de Luynes se fait dans un silence "
  "apais&eacute;, tr&egrave;s diff&eacute;rent de la tension palpable qui "
  "avait accompagn&eacute; leur d&eacute;part de Fondettes quelques "
  "heures plus t&ocirc;t &mdash; comme si cette derni&egrave;re visite au "
  "cimeti&egrave;re avait permis, sinon de r&eacute;soudre les "
  "inqui&eacute;tudes accumul&eacute;es durant la journ&eacute;e, du moins "
  "de leur redonner &agrave; tous trois la force n&eacute;cessaire pour "
  "les affronter.")

p("Clara, regardant par la vitre les rues d&eacute;sertes de "
  "Luynes d&eacute;filer lentement, pense &agrave; cette carte du "
  "monde entraper&ccedil;ue &agrave; Fondettes, &agrave; Odile et &agrave; son "
  "chemin de retour partiel, &agrave; Ambroise Vasseur et &agrave; sa "
  "promesse ambigu&euml;, et se dit, avec une certaine "
  "sérénité malgr&eacute; tout, que quoi qu'il advienne "
  "d&eacute;sormais, elle affrontera cela exactement comme "
  "Darius le lui a appris &mdash; avec Alex &agrave; ses c&ocirc;t&eacute;s, sans "
  "jamais rien affronter seule.")

p("Franck d&eacute;pose finalement Alex devant son "
  "appartement, les deux hommes &eacute;changeant une derni&egrave;re "
  "accolade chaleureuse avant que le jeune homme ne "
  "disparaisse dans son immeuble, puis reconduit Clara "
  "jusque chez elle, promettant, avant qu'elle ne "
  "descende &agrave; son tour de la voiture, de les tenir "
  "inform&eacute;s au moindre nouveau d&eacute;veloppement concernant "
  "Ambroise Vasseur ou son myst&eacute;rieux r&eacute;seau.")

name("FRANCK")
p("&laquo;&nbsp;Merci pour cette journ&eacute;e, Clara. Malgr&eacute; tout ce "
  "qu'on vient d'apprendre, je suis content qu'on l'ait "
  "v&eacute;cue ensemble, tous les trois. &Ccedil;a rend les choses "
  "plus supportables, d'une certaine mani&egrave;re, m&ecirc;me "
  "quand elles sont effrayantes.&nbsp;&raquo;")

p("Clara l'embrasse affectueusement sur la joue avant "
  "de descendre, le regardant repartir seul vers sa "
  "petite maison du coteau, cette b&acirc;tisse troglodytique "
  "qui a vu passer, au fil des d&eacute;cennies, Templier, "
  "Darius, et d&eacute;sormais lui-m&ecirc;me, chacun &agrave; son tour "
  "gardien silencieux d'une histoire qui semble, plus "
  "que jamais ce soir, loin d'&ecirc;tre achev&eacute;e.")

p("Franck rentre seul, cette nuit-l&agrave;, jusqu'&agrave; sa petite "
  "maison troglodytique du coteau, gar&eacute;e la voiture "
  "devant la vigne endormie sous le givre l&eacute;ger de cette "
  "mi-f&eacute;vrier, et reste un long moment assis dans "
  "l'habitacle avant de trouver la force de rentrer, "
  "l'esprit encore travers&eacute; par cette avalanche de "
  "r&eacute;v&eacute;lations accumul&eacute;es depuis le matin.")

p("Il p&eacute;n&egrave;tre enfin dans la maison silencieuse, "
  "allumant machinalement les lumi&egrave;res une &agrave; une, et "
  "s'arr&ecirc;te devant la petite &eacute;tag&egrave;re du salon o&ugrave; "
  "trônent, c&ocirc;te &agrave; c&ocirc;te, une photographie de Darius "
  "souriant et une autre, plus ancienne, de Templier "
  "dans sa vigne, ces deux hommes ayant, chacun &agrave; leur "
  "mani&egrave;re, marqu&eacute; sa propre existence d'une empreinte "
  "indélébile.")

name("FRANCK")
p("&laquo;&nbsp;Qu'est-ce que je devrais faire, vous deux ? "
  "J'aimerais tellement savoir ce que vous auriez pens&eacute; "
  "de tout &ccedil;a, d'Ambroise Vasseur, de cette promesse "
  "de tout r&eacute;soudre. Je me sens tellement seul &agrave; devoir "
  "d&eacute;cider, sans vous deux pour me guider.&nbsp;&raquo;")

p("Il se sert un verre d'eau, s'installe dans son "
  "fauteuil pr&eacute;f&eacute;r&eacute; face &agrave; la fen&ecirc;tre donnant sur la "
  "vigne plong&eacute;e dans l'obscurit&eacute;, et repense, une "
  "derni&egrave;re fois avant de sombrer dans un sommeil "
  "agit&eacute;, &agrave; cette carte immense aper&ccedil;ue &agrave; Fondettes, "
  "&agrave; ce nombre vertigineux de sites r&eacute;partis &agrave; travers "
  "le monde, et &agrave; l'ampleur r&eacute;elle, encore largement "
  "insoup&ccedil;onn&eacute;e, de ce &agrave; quoi sa propre famille se "
  "trouve m&ecirc;l&eacute;e depuis des g&eacute;n&eacute;rations.")

p("Il finit par s'endormir, tard dans la nuit, sans "
  "savoir que la r&eacute;ponse &agrave; ses interrogations est d&eacute;j&agrave; "
  "en train de se jouer, &agrave; cet instant m&ecirc;me, dans un "
  "jardin d'hiver situ&eacute; &agrave; peine quelques kilom&egrave;tres de "
  "l&agrave; o&ugrave; il dort, sans qu'aucune force au monde ne "
  "puisse d&eacute;sormais rien y changer.")

p("Clara, rentr&eacute;e chez elle, ne parvient pas &agrave; trouver "
  "le sommeil malgr&eacute; l'&eacute;puisement de cette journ&eacute;e "
  "extraordinaire, et finit par se relever, un peu apr&egrave;s "
  "minuit, pour ouvrir une derni&egrave;re fois son carnet de "
  "recherches personnelles, celui qu'elle tient depuis "
  "des ann&eacute;es d&eacute;sormais avec la m&ecirc;me rigueur "
  "m&eacute;thodique que Templier leur avait, jadis, enseign&eacute;e.")

p("Elle y consigne, de sa propre &eacute;criture, sans le moindre "
  "myst&egrave;re surnaturel pour l'accompagner cette fois, "
  "chaque d&eacute;tail dont elle se souvient de cette journ&eacute;e "
  "&agrave; Fondettes &mdash; la propri&eacute;t&eacute; r&eacute;nov&eacute;e, Ambroise "
  "Vasseur, Odile et son regard teint&eacute; de bleu, la carte "
  "immense sur le mur du jardin d'hiver, cet homme "
  "discret l'ayant mise en garde &agrave; voix basse.")

name("CLARA")
p("&laquo;&nbsp;Je sais pas ce qu'ils pr&eacute;parent vraiment, ce "
  "soir. Mais j'ai un mauvais pressentiment, un "
  "vraiment mauvais. Si jamais il m'arrive quelque "
  "chose, si jamais on n'a plus l'occasion d'en reparler, "
  "sachez que j'ai fait de mon mieux pour comprendre, "
  "pour prot&eacute;ger ce qui devait l'&ecirc;tre, et pour ne "
  "jamais oublier ce que Darius nous a appris.&nbsp;&raquo;")

p("Elle referme le carnet, &eacute;puis&eacute;e mais un peu plus "
  "apais&eacute;e apr&egrave;s avoir couch&eacute; ces mots sur le papier, "
  "et se recouche enfin, sombrant rapidement dans un "
  "sommeil sans r&ecirc;ve, totalement ignorante, comme "
  "Franck avant elle, de ce qui se joue &agrave; cet instant "
  "pr&eacute;cis dans le jardin d'hiver de la propri&eacute;t&eacute; "
  "Vasseur.")

p("Alex, de son c&ocirc;t&eacute;, ne parvient pas davantage &agrave; "
  "trouver le sommeil cette nuit-l&agrave;, allong&eacute; dans le noir "
  "de sa chambre, sa cicatrice le d&eacute;mangeant "
  "l&eacute;g&egrave;rement, comme chaque fois qu'un &eacute;v&eacute;nement "
  "important li&eacute; &agrave; la Marge vient tout juste de se "
  "produire, sans qu'il puisse jamais pr&eacute;dire &agrave; l'avance "
  "l'intensit&eacute; exacte ni la dur&eacute;e de ces r&eacute;veils "
  "physiques.")

p("Il repense &agrave; sa petite s&oelig;ur &Eacute;milie, endormie "
  "paisiblement dans son propre appartement &eacute;tudiant, "
  "ignorante de tout ce qui vient de se passer &agrave; "
  "Fondettes, et se promet, une fois de plus, de "
  "continuer &agrave; veiller sur elle avec une vigilance "
  "renouvel&eacute;e, sans jamais lui faire porter, s'il peut "
  "l'&eacute;viter, le poids &eacute;crasant de cette histoire tant "
  "qu'elle n'y sera pas elle-m&ecirc;me contrainte.")

p("Il finit par se relever, incapable de rester allong&eacute; "
  "plus longtemps, et s'installe devant son ordinateur "
  "pour relire, une derni&egrave;re fois cette nuit-l&agrave;, le rapport "
  "technique concernant l'accident de Darius, cherchant, "
  "sans grand espoir, un d&eacute;tail suppl&eacute;mentaire qui "
  "pourrait &eacute;clairer d'une lumi&egrave;re nouvelle tout ce "
  "qu'ils viennent d'apprendre sur Ambroise Vasseur et "
  "son r&eacute;seau.")

p("Il ne trouve rien de plus que ce qu'il conna&icirc;t d&eacute;j&agrave; "
  "par c&oelig;ur, mais &eacute;prouve, en refermant finalement son "
  "ordinateur tard dans la nuit, la certitude "
  "grandissante que cette soir&eacute;e &agrave; Fondettes vient "
  "d'ouvrir un chapitre nouveau et probablement "
  "d&eacute;cisif dans une histoire qu'il croyait, il y a "
  "seulement quelques mois, avoir appris &agrave; porter avec "
  "un &eacute;quilibre enfin acquis.")

p("Cette nuit du seize f&eacute;vrier, dans les trois maisons "
  "distinctes o&ugrave; Franck, Clara et Alex tentent chacun, "
  "&agrave; leur mani&egrave;re, de trouver un sommeil qui se refuse "
  "obstin&eacute;ment &agrave; eux, s'&eacute;coule avec une lenteur "
  "particuli&egrave;re, comme si le temps lui-m&ecirc;me avait "
  "conscience de l'importance de ce qui se joue, cette "
  "m&ecirc;me nuit, dans le jardin d'hiver d'une propri&eacute;t&eacute; "
  "discr&egrave;te de Fondettes.")

p("Aucun des trois ne se doute encore &agrave; quel point cette "
  "soir&eacute;e restera, dans leur m&eacute;moire commune, comme "
  "un point de bascule d&eacute;finitif &mdash; le moment pr&eacute;cis o&ugrave; "
  "une histoire personnelle, intime, commenc&eacute;e sous la "
  "pluie devant une vitrine de Luynes quatorze ans plus "
  "t&ocirc;t, a fini par r&eacute;v&eacute;ler sa v&eacute;ritable dimension, "
  "in fin iment plus vaste et plus ancienne que ce "
  "qu'aucun d'eux, m&ecirc;me Templier en son temps, n'avait "
  "jamais os&eacute; imaginer compl&egrave;tement.")

p("Dehors, sur le coteau comme dans les rues "
  "silencieuses de Luynes, la nuit de f&eacute;vrier poursuit son "
  "cours ordinaire, indiff&eacute;rente en apparence &agrave; "
  "l'ampleur de ce qui se pr&eacute;pare &agrave; quelques kilom&egrave;tres "
  "de l&agrave;, et il faudra encore attendre de longues heures "
  "avant que le jour ne se l&egrave;ve enfin sur cette petite "
  "vall&eacute;e de la Loire, sans savoir encore ce qu'il r&eacute;v&eacute;lera "
  "de nouveau au monde.")

p("La vigne de Templier, sur le coteau surplombant "
  "Fondettes, dort profond&eacute;ment sous le givre l&eacute;ger de "
  "cette nuit de f&eacute;vrier, ses ceps taill&eacute;s avec soin "
  "durant l'automne pr&eacute;c&eacute;dent par Franck, Clara et "
  "Alex ensemble, attendant patiemment le retour du "
  "printemps pour bourgeonner &agrave; nouveau, indiff&eacute;rente "
  "&agrave; l'agitation souterraine qui travaille, cette m&ecirc;me "
  "nuit, l'ensemble d'un r&eacute;seau invisible dispers&eacute; &agrave; "
  "travers le monde.")

p("Cette petite parcelle de terre, h&eacute;rit&eacute;e de Templier "
  "puis entretenue avec amour par ceux qu'il avait "
  "choisi de prot&eacute;ger avant de dispara&icirc;tre, repr&eacute;sente, "
  "pour Clara et Alex comme pour Franck, un symbole "
  "pr&eacute;cieux de tout ce que leur histoire commune a "
  "r&eacute;ussi &agrave; pr&eacute;server malgr&eacute; les &eacute;preuves &mdash; la "
  "capacit&eacute; obstin&eacute;e de la vie &agrave; continuer, patiemment, "
  "quoi qu'il puisse se tramer ailleurs dans l'ombre.")

p("Les ceps endormis, align&eacute;s avec r&eacute;gularit&eacute; sur le "
  "coteau silencieux, semblent monter une garde "
  "discr&egrave;te sur ce lieu charg&eacute; d'histoire, t&eacute;moins "
  "immobiles de toutes les g&eacute;n&eacute;rations de porteurs "
  "qui ont, chacune &agrave; leur mani&egrave;re, tent&eacute; de "
  "n&eacute;gocier avec cette force ancienne tapie sous la "
  "vall&eacute;e enti&egrave;re.")

p("Demain, comme chaque lendemain de seize f&eacute;vrier "
  "depuis onze ans, ils se retrouveront probablement "
  "tous les trois pour discuter calmement de ce qu'il "
  "convient de faire d&eacute;sormais face &agrave; cette nouvelle "
  "donn&eacute;e, sans savoir encore &agrave; quel point le monde "
  "aura, cette nuit-l&agrave; m&ecirc;me, d&eacute;j&agrave; commenc&eacute; &agrave; "
  "basculer vers quelque chose qu'aucun d'eux n'aurait "
  "jamais pu anticiper, m&ecirc;me dans leurs pires "
  "sc&eacute;narios envisag&eacute;s ensemble au fil des ann&eacute;es.")

p("Le fleuve, en contrebas du coteau, poursuit son "
  "cours silencieux dans l'obscurit&eacute; de cette nuit de "
  "f&eacute;vrier, indiff&eacute;rent depuis toujours &agrave; tout ce qu'il a "
  "vu se jouer sur ses rives &mdash; des enfances enti&egrave;res, "
  "des l&eacute;gendes vieilles de plusieurs si&egrave;cles, un "
  "programme scientifique n&eacute; puis mort en quatre "
  "ann&eacute;es &agrave; peine, et d&eacute;sormais cette organisation "
  "patiente qui s'appr&ecirc;te, cette nuit m&ecirc;me, &agrave; franchir "
  "un seuil que personne, avant elle, n'avait jamais os&eacute; "
  "atteindre.")

p("Darius avait appris, gr&acirc;ce &agrave; Templier, &agrave; &eacute;couter "
  "cette Loire diff&eacute;remment, &agrave; y percevoir non plus "
  "seulement de l'eau qui coule, mais une sorte de "
  "t&eacute;moin immense et muet de tout ce que sa propre "
  "lign&eacute;e avait travers&eacute; depuis des g&eacute;n&eacute;rations, et "
  "Clara, Alex et Franck, chacun &agrave; leur mani&egrave;re, ont "
  "fini par h&eacute;riter, eux aussi, de cette &eacute;coute "
  "particuli&egrave;re.")

p("Cette nuit-l&agrave;, pourtant, le fleuve ne murmure rien de "
  "particulier, coulant simplement, comme il l'a "
  "toujours fait, ind&eacute;pendamment des drames humains "
  "se jouant sur ses berges, laissant &agrave; Fondettes, un peu "
  "plus loin, le soin de d&eacute;cider seule de ce que l'avenir "
  "leur r&eacute;serve d&eacute;sormais &agrave; tous.")

p("Minuit sonne au clocher de l'&eacute;glise de Luynes, ce "
  "m&ecirc;me clocher sous lequel Darius avait &eacute;t&eacute; enterr&eacute; "
  "onze ans plus t&ocirc;t, un son grave et familier port&eacute; par "
  "le vent froid jusqu'aux maisons endormies, marquant "
  "ainsi, sans que personne ne le remarque "
  "particuli&egrave;rement, le passage officiel d'un seize "
  "f&eacute;vrier &agrave; un dix-sept f&eacute;vrier ordinaire.")

p("Mais &agrave; Fondettes, dans le jardin d'hiver de la "
  "propri&eacute;t&eacute; Vasseur, cette limite calendaire ne "
  "signifie plus rien depuis longtemps d&eacute;j&agrave;, "
  "l'assembl&eacute;e r&eacute;unie autour d'Ambroise Vasseur ayant "
  "d&eacute;pass&eacute;, depuis l'instant m&ecirc;me o&ugrave; la voix "
  "myst&eacute;rieuse a pos&eacute; sa question depuis l'obscurit&eacute; du "
  "couloir, toute notion ordinaire de temps qui passe.")

p("Le matin du dix-sept f&eacute;vrier se l&egrave;vera, dans quelques "
  "heures &agrave; peine, sur une vall&eacute;e de la Loire en "
  "apparence totalement inchang&eacute;e &mdash; les boulangeries "
  "ouvriront &agrave; l'heure habituelle, les premiers "
  "coll&eacute;giens attendront le bus scolaire &agrave; l'arr&ecirc;t "
  "accoutum&eacute;, et rien, absolument rien dans le d&eacute;cor "
  "familier de Luynes, ne laissera deviner &agrave; ses "
  "habitants ordinaires qu'un seuil important vient "
  "d'&ecirc;tre franchi cette nuit-l&agrave;, quelque part du c&ocirc;t&eacute; de "
  "Fondettes.")

p("Franck, Clara et Alex se r&eacute;veilleront chacun, "
  "quelques heures plus tard, avec cette m&ecirc;me sensation "
  "diffuse de lendemain incertain, sans savoir encore si "
  "cette journ&eacute;e &agrave; venir leur apportera des r&eacute;ponses "
  "suppl&eacute;mentaires ou, au contraire, un silence encore "
  "plus &eacute;pais que celui qui a toujours entour&eacute; "
  "l'organisation d'Ambroise Vasseur.")

p("Ils se retrouveront, comme ils en ont pris l'habitude "
  "chaque lendemain de seize f&eacute;vrier, pour faire le point "
  "ensemble sur tout ce qu'ils ont appris, pr&ecirc;ts, une "
  "fois de plus, &agrave; affronter ensemble ce que l'avenir "
  "leur r&eacute;serve &mdash; fid&egrave;les, en cela, &agrave; tout ce que "
  "Darius, disparu depuis onze ans mais jamais "
  "vraiment oubli&eacute;, leur a appris sur la force "
  "tranquille de na jamais rien affronter seul.")

p("&Eacute;milie, endormie profond&eacute;ment &agrave; cette heure "
  "avanc&eacute;e de la nuit dans son petit appartement "
  "&eacute;tudiant de Tours, ignore encore tout de la "
  "d&eacute;cision qui vient d'&ecirc;tre prise &agrave; quelques kilom&egrave;tres "
  "de l&agrave;, dans ce jardin d'hiver o&ugrave; son propre avenir, "
  "sans qu'elle le sache, pourrait bien avoir &eacute;t&eacute; "
  "d&eacute;j&agrave; scell&eacute; par des inconnus convaincus d'agir "
  "pour le bien de tous.")

p("Franck, une fois rentr&eacute; chez lui et enfin "
  "endormi, fait un r&ecirc;ve &eacute;trange cette nuit-l&agrave; &mdash; "
  "celui de Darius, adolescent, souriant dans la "
  "lumi&egrave;re dor&eacute;e d'un &eacute;t&eacute; qui n'a jamais existé, "
  "lui disant simplement, avant de s'&eacute;vanouir dans "
  "la brume onirique : &laquo;&nbsp;&ccedil;a va aller, papa. Vous "
  "&ecirc;tes pr&ecirc;ts, m&ecirc;me si vous le savez pas encore "
  "compl&egrave;tement.&nbsp;&raquo; Un r&ecirc;ve dont il ne se "
  "souviendra, au r&eacute;veil, que d'une sensation "
  "diffuse de r&eacute;confort, sans jamais pouvoir en "
  "reconstituer les mots exacts.")

p("Il y a, dans cette longue histoire commenc&eacute;e sous "
  "une pluie battante devant la vitrine d'un magasin de "
  "Luynes, une v&eacute;rit&eacute; simple que Darius avait fini par "
  "comprendre bien avant tous les autres, et que Clara "
  "et Alex, chacun &agrave; leur mani&egrave;re, avaient fini par "
  "int&eacute;grer profond&eacute;ment au fil des ann&eacute;es &mdash; que "
  "quelle que soit l'ampleur r&eacute;elle de la Marge, du "
  "r&eacute;seau, ou de cette organisation men&eacute;e par Ambroise "
  "Vasseur, rien de tout cela ne pourrait jamais "
  "effacer compl&egrave;tement ce qui s'&eacute;tait v&eacute;ritablement "
  "pass&eacute; entre eux trois.")

p("Ni la solitude du porteur, ni le poids d'une lign&eacute;e "
  "ancienne, ni m&ecirc;me la perspective glaçante d'une "
  "organisation patiente pr&ecirc;te &agrave; tout risquer pour "
  "atteindre ses fins, n'avaient jamais r&eacute;ussi &agrave; briser "
  "cette chose simple et in&eacute;branlable qui les liait tous "
  "les trois depuis l'enfance &mdash; une amiti&eacute; capable de "
  "traverser l'impossible sans jamais totalement se "
  "dissoudre, contrairement &agrave; tout le reste.")

p("C'est peut-&ecirc;tre cela, en d&eacute;finitive, la seule chose que "
  "ni Ambroise Vasseur, ni le docteur Vasseur avant "
  "lui, ni m&ecirc;me la Marge elle-m&ecirc;me dans toute son "
  "&eacute;tendue ancienne et myst&eacute;rieuse, n'avaient jamais "
  "totalement r&eacute;ussi &agrave; comprendre ou &agrave; ma&icirc;triser &mdash; "
  "cette capacit&eacute; obstin&eacute;e de quelques &ecirc;tres humains &agrave; "
  "continuer de s'aimer et de se soutenir, envers et "
  "contre tout, m&ecirc;me au c&oelig;ur des t&eacute;n&egrave;bres les plus "
  "&eacute;paisses.")

p("Darius, o&ugrave; qu'il se trouve d&eacute;sormais &mdash; dissous "
  "dans la m&eacute;moire de ceux qui l'ont aim&eacute;, ou "
  "peut-&ecirc;tre, comme Kayden avant lui, dilu&eacute; quelque "
  "part sans &ecirc;tre totalement &eacute;teint &mdash; continue "
  "d'exister &agrave; travers chaque geste de courage que "
  "Clara et Alex accomplissent en son nom, &agrave; "
  "travers chaque preuve pr&eacute;cieusement conserv&eacute;e "
  "dans ce coffre qui attend, patiemment, qu'un "
  "successeur inconnu vienne un jour le r&eacute;clamer, "
  "&agrave; travers cette vigne qui continue, ann&eacute;e apr&egrave;s "
  "ann&eacute;e, de porter ses fruits sur le coteau silencieux "
  "de Fondettes.")

p("Pendant que la voiture de Franck s'&eacute;loigne, ses phares "
  "trouant doucement l'obscurit&eacute; naissante sur la route "
  "longeant la Loire, la propri&eacute;t&eacute; de Fondettes, elle, ne "
  "s'est pas vid&eacute;e comme Clara, Alex et Franck l'avaient "
  "suppos&eacute; en la quittant quelques heures plus t&ocirc;t &mdash; "
  "au contraire, l'assembl&eacute;e r&eacute;unie dans le jardin d'hiver "
  "s'est &eacute;toff&eacute;e, discr&egrave;tement, &agrave; mesure que la nuit "
  "tombait, de nouveaux arrivants entrant un &agrave; un par "
  "une porte lat&eacute;rale que les trois visiteurs n'avaient "
  "jamais remarqu&eacute;e.")

p("Ambroise Vasseur, d&eacute;barrass&eacute; d&eacute;sormais de la "
  "courtoisie professionnelle affich&eacute;e tout l'apr&egrave;s-midi, "
  "se tient pr&egrave;s de la grande baie vitr&eacute;e donnant sur le "
  "jardin plong&eacute; dans l'obscurit&eacute;, observant les phares "
  "de la voiture dispara&icirc;tre au loin sur la route, avant de "
  "se retourner vers la pi&egrave;ce d&eacute;sormais compl&egrave;te, "
  "chaque chaise occup&eacute;e, chaque regard tourn&eacute; vers "
  "lui dans un silence absolu.")

p("Ambroise Vasseur laisse son regard parcourir une "
  "derni&egrave;re fois l'assembl&eacute;e enti&egrave;re, reconnaissant, "
  "dans chaque visage tourn&eacute; vers lui, une part de "
  "cette longue qu&ecirc;te men&eacute;e depuis des d&eacute;cennies &mdash; "
  "Odile, silencieuse pr&egrave;s de la fen&ecirc;tre, son propre "
  "doute encore visible malgr&eacute; sa loyaut&eacute; in&eacute;branlable ; "
  "l'homme discret ayant averti Clara quelques heures "
  "plus t&ocirc;t, d&eacute;sormais parfaitement immobile lui aussi ; "
  "et tant d'autres, venus de sites &eacute;parpill&eacute;s &agrave; travers "
  "le pays et au-del&agrave;, tous r&eacute;unis ce soir pour "
  "assister, ou participer, &agrave; ce qu'il consid&egrave;re depuis "
  "toujours comme l'aboutissement logique et n&eacute;cessaire "
  "de la vie enti&egrave;re de son grand-p&egrave;re.")

p("Il pense, une derni&egrave;re fois, &agrave; ce jeune gar&ccedil;on nomm&eacute; "
  "Darius, disparu onze ans plus t&ocirc;t dans des "
  "circonstances qu'aucun rapport officiel n'a jamais "
  "su expliquer enti&egrave;rement, et &agrave; ce p&egrave;re boulevers&eacute;, "
  "Franck, venu quelques heures plus t&ocirc;t lui demander "
  "pardon pour un fr&egrave;re qu'il n'avait jamais vraiment pu "
  "pleurer correctement &mdash; deux existences parmi tant "
  "d'autres, broy&eacute;es par une force que son propre "
  "grand-p&egrave;re avait cru, na&iuml;vement, pouvoir un jour "
  "totalement ma&icirc;triser.")

p("Ce soir marquera, il en est profond&eacute;ment convaincu, "
  "la fin de toutes ces souffrances individuelles "
  "accumul&eacute;es depuis des si&egrave;cles, port&eacute;es isol&eacute;ment "
  "par des g&eacute;n&eacute;rations enti&egrave;res de porteurs solitaires "
  "&mdash; Templier, la petite s&oelig;ur perdue en 1979, Kayden "
  "lui-m&ecirc;me, dilu&eacute; mais jamais compl&egrave;tement &eacute;teint, et "
  "tant d'autres noms consign&eacute;s dans les dossiers "
  "poussi&eacute;reux des sept sites originels &mdash; toutes ces vies "
  "sacrifi&eacute;es, une &agrave; une, sans jamais qu'aucune "
  "g&eacute;n&eacute;ration ne parvienne &agrave; r&eacute;unir suffisamment de "
  "force pour affronter collectivement la source m&ecirc;me "
  "du probl&egrave;me.")

p("Il consulte une derni&egrave;re fois sa montre, un vieux "
  "mod&egrave;le &agrave; remontage manuel h&eacute;rit&eacute; directement de "
  "son grand-p&egrave;re, et constate que l'heure convenue "
  "depuis des mois avec l'ensemble des sites du r&eacute;seau "
  "vient tout juste de sonner, partout &agrave; la fois, sur "
  "plusieurs fuseaux horaires diff&eacute;rents, gr&acirc;ce &agrave; ce "
  "syst&egrave;me de synchronisation qu'il a mis des ann&eacute;es &agrave; "
  "perfectionner dans le plus grand secret.")

p("Une derni&egrave;re fois, avant de donner le signal "
  "d&eacute;finitif, il repense &agrave; ce que lui avait confi&eacute; "
  "Odile, dans la voiture les ramenant tous deux de "
  "l'a&eacute;roport quelques semaines plus t&ocirc;t, cette "
  "h&eacute;sitation ultime qu'elle n'avait jamais totalement "
  "dissip&eacute;e malgr&eacute; des ann&eacute;es de pr&eacute;paration commune "
  "&mdash; et choisit, comme toujours depuis le d&eacute;but de "
  "cette aventure, de faire taire ce doute au profit de "
  "sa conviction plus ancienne encore, celle d'une vie "
  "enti&egrave;re consacr&eacute;e &agrave; vouloir enfin r&eacute;soudre, "
  "d&eacute;finitivement, ce que son grand-p&egrave;re avait &eacute;chou&eacute; &agrave; "
  "seulement effleurer.")

p("Une lumi&egrave;re &eacute;lectrique, quelque part dans le couloir "
  "derri&egrave;re lui, cligno te une fois, deux fois, d'un bleu "
  "l&eacute;g&egrave;rement trop intense pour une simple ampoule "
  "domestique, avant de se stabiliser, comme si "
  "quelque chose, dans les murs m&ecirc;mes de cette maison "
  "restaur&eacute;e, respirait doucement au rythme de "
  "l'assembl&eacute;e r&eacute;unie.")

name("VOIX INCONNUE")
p("&laquo;&nbsp;C'est bon, ils sont tous l&agrave; ?&nbsp;&raquo;")

p("La question, pos&eacute;e depuis le fond obscur du couloir "
  "par une voix qu'aucun narrateur ne saurait d&eacute;crire "
  "avec certitude, homme ou femme, jeune ou vieille, "
  "flotte un instant dans l'air immobile du jardin "
  "d'hiver, chaque membre de l'assembl&eacute;e restant "
  "parfaitement silencieux, parfaitement immobile, "
  "comme suspendu dans l'attente d'une r&eacute;ponse qu'ils "
  "connaissent tous d&eacute;j&agrave;.")

name("AMBROISE VASSEUR")
p("&laquo;&nbsp;Oui, ils sont tous l&agrave;.&nbsp;&raquo;")

p("Quelque part, tr&egrave;s loin de ce jardin d'hiver, dans une "
  "petite chambre plong&eacute;e dans le noir &agrave; Tours, &Eacute;milie "
  "se retourne dans son sommeil, travers&eacute;e une "
  "nouvelle fois par ce m&ecirc;me r&ecirc;ve de couloirs identiques "
  "et de portes num&eacute;rot&eacute;es, sans jamais se r&eacute;veiller "
  "tout &agrave; fait, comme si quelque chose, quelque part, "
  "venait de tourner une page qu'elle ne saurait pas "
  "encore nommer.")

p("Et dans le petit cimeti&egrave;re de Luynes, sur la pierre "
  "tombale de Darius que Clara, Alex et Franck viennent "
  "tout juste de quitter, une fine pellicule de givre "
  "se forme, en quelques secondes &agrave; peine, en un motif "
  "qu'aucun m&eacute;t&eacute;orologue ne saurait expliquer par le "
  "seul froid de la nuit &mdash; des lignes verticales, "
  "parfaitement r&eacute;guli&egrave;res, comme un &eacute;cho silencieux "
  "r&eacute;pondant, &agrave; des kilom&egrave;tres de distance, &agrave; ce qui "
  "vient de se dire &agrave; Fondettes.")

p("Le silence qui suit cette confirmation s'&eacute;tire, "
  "&eacute;pais, absolu, seulement troubl&eacute; par le l&eacute;ger "
  "grésillement &eacute;lectrique de cette m&ecirc;me lumi&egrave;re "
  "clignotante dans le couloir, dont l'&eacute;clat bleu&acirc;tre, "
  "l'espace d'une fraction de seconde, se fige en un "
  "motif tr&egrave;s pr&eacute;cis de lignes verticales parfaitement "
  "r&eacute;guli&egrave;res &mdash; ce m&ecirc;me motif, exactement, qui "
  "annon&ccedil;ait autrefois, dans une autre vie, l'approche du "
  "Non-lieu.")

p("Ambroise Vasseur balaie une derni&egrave;re fois la "
  "pi&egrave;ce du regard, cette assembl&eacute;e enti&egrave;re suspendue "
  "&agrave; ses l&egrave;vres, port&eacute;e par des d&eacute;cennies "
  "d'attente patiente et de pr&eacute;paration minutieuse, "
  "et sent, au fond de lui, malgr&eacute; toute sa "
  "d&eacute;termination affich&eacute;e, une derni&egrave;re trace de "
  "vertige face &agrave; l'ampleur irr&eacute;versible de ce qu'il "
  "s'appr&ecirc;te &agrave; d&eacute;clencher, ce m&ecirc;me vertige, "
  "peut-&ecirc;tre, qu'avait ressenti son propre "
  "grand-p&egrave;re, des d&eacute;cennies plus t&ocirc;t, au moment de "
  "signer les premiers documents fondateurs du "
  "programme M.13.")

p("Personne, dans cette pi&egrave;ce, n'ose plus respirer trop "
  "fort, chacun sentant confus&eacute;ment que ce qui "
  "s'appr&ecirc;te &agrave; &ecirc;tre prononc&eacute; d&eacute;passe d&eacute;sormais, et de "
  "tr&egrave;s loin, la simple port&eacute;e d'une r&eacute;union priv&eacute;e "
  "tenue dans un jardin d'hiver de la vall&eacute;e de la "
  "Loire &mdash; comme si les murs eux-m&ecirc;mes de cette "
  "maison restaur&eacute;e retenaient leur souffle, dans "
  "l'attente de la phrase qui suivra.")

p("Ambroise Vasseur ferme les yeux un bref instant, "
  "cherchant, une derni&egrave;re fois avant de tout basculer "
  "d&eacute;finitivement, une trace de doute susceptible de "
  "l'arr&ecirc;ter encore &mdash; et n'en trouve aucune, seulement "
  "cette d&eacute;termination froide, forg&eacute;e par une vie "
  "enti&egrave;re de pr&eacute;paration, qui ne conna&icirc;t plus, d&eacute;sormais, "
  "d'autre chemin possible que celui qu'il s'appr&ecirc;te &agrave; "
  "emprunter.")

p("Quelque part dans cette assembl&eacute;e silencieuse, "
  "l'homme discret ayant chuchot&eacute; sa mise en garde &agrave; "
  "Clara quelques heures plus t&ocirc;t &eacute;change un regard "
  "furtif avec un autre membre du groupe, un &eacute;change "
  "muet charg&eacute; d'une inqui&eacute;tude qu'aucun des deux "
  "n'ose exprimer &agrave; voix haute, conscients tous deux "
  "qu'il est d&eacute;sormais bien trop tard pour esp&eacute;rer "
  "infl&eacute;chir le cours d&eacute;j&agrave; scell&eacute; de cette soir&eacute;e "
  "historique.")

p("Odile, pr&egrave;s de la fen&ecirc;tre, rouvre les yeux &agrave; cet "
  "instant pr&eacute;cis, et son regard, cette fois, semble "
  "capter une derni&egrave;re fois cette teinte bleu&acirc;tre "
  "particuli&egrave;re que Clara avait cru surprendre quelques "
  "heures plus t&ocirc;t, avant de se refermer &agrave; nouveau, "
  "lentement, comme si elle acceptait, malgr&eacute; tout, de "
  "laisser Ambroise mener seul jusqu'au bout ce qu'elle "
  "n'a plus la force, ce soir, d'emp&ecirc;cher.")

p("Autour de la table, chacun des membres de "
  "l'assembl&eacute;e semble retenir, &agrave; son tour, ce m&ecirc;me "
  "souffle suspendu, conscient que les prochaines "
  "secondes vont d&eacute;finitivement d&eacute;partager deux "
  "chemins possibles &mdash; celui, prudent, d'une retraite "
  "encore envisageable, et celui, d&eacute;sormais choisi "
  "d&eacute;finitivement par leur guide, d'un basculement "
  "irr&eacute;versible vers l'inconnu total.")

p("Dehors, dans l'obscurit&eacute; totale du parc entourant "
  "la propri&eacute;t&eacute;, le vent se l&egrave;ve doucement, agitant "
  "les branches nues des arbres centenaires plant&eacute;s "
  "par le docteur Vasseur lui-m&ecirc;me des d&eacute;cennies "
  "plus t&ocirc;t, comme si la nature environnante "
  "elle-m&ecirc;me pressentait, sans pouvoir l'exprimer "
  "autrement que par ce fr&eacute;missement inqui&eacute;tant, "
  "l'ampleur de ce qui s'appr&ecirc;te &agrave; se produire entre "
  "ces murs charg&eacute;s d'histoire.")

p("Plus loin encore, invisibles depuis le jardin "
  "d'hiver, les lumi&egrave;res de Luynes scintillent "
  "faiblement &agrave; l'horizon, ce petit village endormi "
  "n'ayant aucune id&eacute;e de ce qui se trame &agrave; quelques "
  "kilom&egrave;tres seulement de ses maisons paisibles, "
  "aucune id&eacute;e non plus que l'un de ses propres "
  "enfants, disparu onze ans plus t&ocirc;t un soir de "
  "f&eacute;vrier similaire &agrave; celui-ci, avait autrefois "
  "consacr&eacute; les derniers instants de sa vie &agrave; "
  "tenter de comprendre, mieux que quiconque avant "
  "lui, la nature exacte de cette force ancienne que "
  "l'assembl&eacute;e r&eacute;unie ce soir s'appr&ecirc;te, "
  "d&eacute;sormais, &agrave; r&eacute;veiller enti&egrave;rement.")

p("Le vieil homme discret, celui-l&agrave; m&ecirc;me qui avait "
  "chuchot&eacute; sa mise en garde &agrave; Clara quelques heures "
  "plus t&ocirc;t, baisse les yeux vers ses propres mains "
  "jointes sur ses genoux, incapable de dissimuler tout "
  "&agrave; fait le tremblement l&eacute;ger qui les agite, comme si "
  "une part de lui, m&ecirc;me &agrave; cet instant ultime, gardait "
  "encore l'espoir fragile qu'un dernier revirement "
  "demeurait, malgr&eacute; tout, possible.")

p("Puis la voix reprend, depuis l'obscurit&eacute;, avec un "
  "calme terrible, d&eacute;pourvu de toute urgence, comme "
  "quelqu'un qui n'a plus besoin de se presser d&eacute;sormais "
  "que le plus dur &mdash; attendre, rassembler, patienter des "
  "d&eacute;cennies durant &mdash; est enfin, apr&egrave;s tant d'ann&eacute;es, "
  "derri&egrave;re elle.")

name("VOIX INCONNUE")
p("&laquo;&nbsp;Commen&ccedil;ons la fin du monde.&nbsp;&raquo;")

S.append(rule())
S.append(Paragraph("&mdash; fin du chapitre 12 &mdash;", chapter_label))
S.append(Paragraph("&mdash; fin des douze chapitres &mdash;", chapter_label))

doc.build(S)
print("OK ->", OUT)
