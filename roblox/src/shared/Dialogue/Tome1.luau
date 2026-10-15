--!strict
-- Dialogues du Tome 1 (données pures). Adapté du chapitre 1 de PROJECT-M13.
-- Un noeud : { speaker?, text, next?, choices?, effect? }
-- Effets : "scene:<id>" (change de scène, réservé à l'hôte), "flag:<nom>".

export type Choice = { text: string, next: string?, effect: string? }
export type Node = {
	speaker: string?,
	text: string,
	next: string?,
	choices: { Choice }?,
	effect: string?,
}

local nodes: { [string]: Node } = {
	-- Scène 1 : Miel (Luynes, sous la pluie)
	narr_pluie = {
		text = "Il pleut sur Luynes comme il pleut toujours en novembre, de biais, sans conviction.",
		next = "narr_machine",
	},
	narr_machine = {
		text = "Entre le présentoir à journaux et le vieux flipper hors service, il y a une machine que personne n'a jamais vue. Personne, sauf toi.",
	},

	machine_label = {
		speaker = "Distributeur",
		text = "INSERTION REQUISE. POUR RÉCUPÉRER UNE PAGE, VOUS DEVEZ ABANDONNER UNE ANNÉE.",
		choices = {
			{ text = "Insérer une année", next = "machine_insert" },
			{ text = "Reculer", next = "machine_refuse" },
		},
	},
	machine_refuse = {
		text = "Tu recules d'un pas. Le collier de Miel est toujours là, dans son gel. Il attend.",
	},
	machine_insert = {
		speaker = "Distributeur",
		text = "ANNÉE ACCEPTÉE. LA PAGE 41 VOUS ATTEND.",
		effect = "scene:nonlieu",
	},

	clara_1 = {
		speaker = "Clara",
		text = "Elle est encore là ? Elle est apparue une première fois y'a deux ans. Le soir où mon père est parti.",
		choices = {
			{ text = "Qu'est-ce qu'il y avait dedans ?", next = "clara_montre" },
			{ text = "Pourquoi tu me crois ?", next = "clara_croit" },
			{ text = "Ça veut dire quoi, la page 41 ?", next = "clara_page" },
		},
	},
	clara_montre = {
		speaker = "Clara",
		text = "Sa montre. Sa vraie montre, celle qu'il enlève jamais, même sous la douche.",
		next = "clara_fin",
	},
	clara_croit = {
		speaker = "Clara",
		text = "Parce que j'ai tout noté. Les dates, les objets. Et chaque fois, la même question : « qu'est-ce qu'on m'a dit à la place ? »",
		next = "clara_fin",
	},
	clara_page = {
		speaker = "Clara",
		text = "Ça veut dire qu'il existe un livre quelque part où y'a écrit ce qui s'est vraiment passé. Et vu le numéro, c'est loin d'être la première page qu'elle remplit.",
		next = "clara_fin",
	},
	clara_fin = {
		speaker = "Clara",
		text = "Va lire l'étiquette. Moi, je note.",
	},

	alex_1 = {
		speaker = "Alex",
		text = "Moi j'y crois pas à fond, hein, je précise. Mais ça coûte rien de noter.",
		choices = {
			{ text = "Elle choisit ses victimes ?", next = "alex_choix" },
			{ text = "Tu as peur ?", next = "alex_peur" },
		},
	},
	alex_choix = {
		speaker = "Alex",
		text = "Elle choisit des familles où quelqu'un aime assez fort quelqu'un d'autre pour lui mentir. C'est presque pire que si c'était au hasard.",
	},
	alex_peur = {
		speaker = "Alex",
		text = "Moi ? Jamais. J'ai juste envie d'être très loin, très vite.",
	},

	-- Scène 2 : le Non-lieu
	nonlieu_intro = {
		text = "Tu ouvres les yeux dans un couloir qui n'existe pas. Le sol est blanc. Les portes sont toutes numérotées. L'une d'elles porte le numéro 41.",
		next = "nonlieu_conseil",
	},
	nonlieu_conseil = {
		text = "Chaque porte cache un souvenir. Mais quelque chose rôde dans le couloir, et le décor commence à glitcher.",
	},
	door_wrong = {
		text = "Derrière cette porte, il y a un souvenir. Pas le tien. Il se dissout dans tes mains, et le couloir tremble.",
	},
	door_41 = {
		text = "La porte 41 s'ouvre sur un silence immense.",
	},

	-- Scène 3 : Kayden
	kayden_intro = {
		speaker = "Kayden",
		text = "Vous êtes venus. Ravissant. J'aurai plus de choses à garder.",
	},
	kayden_mid = {
		speaker = "Kayden",
		text = "Tu portes tout ça tout seul ? Tu ne tiendras pas.",
	},
	kayden_defeat = {
		text = "Kayden s'effrite en pages blanches. Sur la dernière, un numéro : 41. Et le dessin d'un petit chien.",
		effect = "flag:finished",
	},
}

return {
	nodes = nodes,
	-- Noeuds d'entrée utilisés par l'histoire.
	entries = {
		"narr_pluie",
		"machine_label",
		"clara_1",
		"alex_1",
		"nonlieu_intro",
		"door_wrong",
		"door_41",
		"kayden_intro",
		"kayden_mid",
		"kayden_defeat",
	},
}
