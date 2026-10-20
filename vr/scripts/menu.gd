extends Node3D
# Menu principal : NOUVELLE PARTIE (emplacement puis difficulté), CONTINUER (choix de la partie),
# RÉGLAGES, CRÉDITS, QUITTER. Décor : clairière de forêt de nuit.

signal new_game(slot: int, difficulty: String)
signal load_game(slot: int)
signal quit

const World := preload("res://scripts/world.gd")
const Props := preload("res://scripts/props.gd")
const Button3D := preload("res://scripts/button3d.gd")

var screens: Dictionary = {}
var _toggles: Dictionary = {}
var _pending_slot := 0

func _ready() -> void:
	Props.night_env(self, Color(0.04, 0.07, 0.13), 0.03)
	Props.ground(self)
	var clear: Array = [Rect2(-9, -9, 18, 16)]
	Props.forest(self, 3, 190, Rect2(-45, -50, 90, 70), clear)
	Props.grass(self, 9, 380, Rect2(-14, -12, 28, 24), [])
	Props.rocks(self, 4, 16, Rect2(-14, -14, 28, 24), [Rect2(-3, -5, 6, 8)])
	Props.lantern(self, Vector3(-3.2, 0, -1.2), Color(1.0, 0.72, 0.38))
	Props.lantern(self, Vector3(3.2, 0, -1.2), Color(1.0, 0.72, 0.38))
	Props.standing_stone(self, Vector3(-6.0, 0, -4.0), deg_to_rad(40))
	Props.standing_stone(self, Vector3(6.0, 0, -4.0), deg_to_rad(-40))
	World.blue_lines(self, Vector3(0, 0, -6), 12.0, 14, 9.0)
	_build_all()
	_show("main")

func spawn_point() -> Vector3:
	return Vector3(0, 0, 1.5)

func _screen(id: String) -> Node3D:
	var n := Node3D.new()
	add_child(n)
	screens[id] = n
	return n

func _button(parent: Node, text: String, pos: Vector3, callback: Callable, width := 2.1, enabled := true) -> Node:
	var b := Button3D.new()
	b.size = Vector3(width, 0.34, 0.06)
	b.text = text
	b.position = pos
	parent.add_child(b)
	if enabled:
		b.pressed.connect(callback)
	else:
		b.dim()
	return b

func _title(parent: Node, text: String, y: float, px := 0.0035) -> void:
	World.label(parent, text, Vector3(0, y, -3.2), px, Color(1, 1, 1), 80)

func _build_all() -> void:
	# --- Accueil ---
	var m := _screen("main")
	World.label(m, "PROJECT-M13", Vector3(0, 2.85, -3.2), 0.0045, Color(1, 1, 1), 96)
	World.label(m, "TOME 1 : LA PAGE 404", Vector3(0, 2.3, -3.2), 0.0028, Color(0.5, 0.75, 1.0), 80)
	var y := 1.75
	_button(m, "NOUVELLE PARTIE", Vector3(0, y, -3.0), func(): _show("slots_new"))
	_button(m, "CONTINUER", Vector3(0, y - 0.4, -3.0), func(): _show("slots_load"), 2.1, Settings.has_saves())
	_button(m, "REGLAGES", Vector3(0, y - 0.8, -3.0), func(): _show("settings"))
	_button(m, "CREDITS", Vector3(0, y - 1.2, -3.0), func(): _show("credits"))
	_button(m, "QUITTER", Vector3(0, y - 1.6, -3.0), func(): quit.emit())
	World.label(m, "Vise avec le laser, gachette pour valider", Vector3(0, 0.0, -2.9), 0.0026, Color(0.6, 0.65, 0.75), 56)
	# --- Choix de l'emplacement (nouvelle partie / continuer) ---
	for mode in ["new", "load"]:
		var s := _screen("slots_" + mode)
		_title(s, "NOUVELLE PARTIE" if mode == "new" else "CONTINUER", 2.6)
		for i in 3:
			var idx := i
			var used: bool = not (Settings.slots[i] as Dictionary).is_empty()
			var label: String = Settings.slot_label(i)
			if mode == "new":
				_button(s, label, Vector3(0, 1.9 - i * 0.42, -3.0), func(): _pick_new(idx), 4.2)
			else:
				_button(s, label, Vector3(0, 1.9 - i * 0.42, -3.0), func(): load_game.emit(idx), 4.2, used)
		_button(s, "RETOUR", Vector3(0, 0.5, -3.0), func(): _show("main"))
	# --- Difficulté ---
	var d := _screen("difficulty")
	_title(d, "DIFFICULTE", 2.6)
	var yy := 1.9
	for key in ["easy", "normal", "hard"]:
		var k: String = key
		var info: Dictionary = Settings.DIFFICULTIES[k]
		var sub: String = {"easy": "Ennemis lents, pouvoir rapide", "normal": "L'experience prevue", "hard": "Ennemis rapides, pouvoir lent"}[k]
		_button(d, "%s  -  %s" % [info["label"], sub], Vector3(0, yy, -3.0), func(): new_game.emit(_pending_slot, k), 4.6)
		yy -= 0.42
	_button(d, "RETOUR", Vector3(0, 0.5, -3.0), func(): _show("slots_new"))
	# --- Réglages ---
	var r := _screen("settings")
	_title(r, "REGLAGES DE CONFORT", 2.7)
	var ry := 2.1
	for id in ["move", "turn", "vig", "seat", "dom"]:
		_toggles[id] = _button(r, "", Vector3(0, ry, -3.0), Callable(self, "_toggle_" + id), 3.8)
		ry -= 0.4
	_button(r, "RETOUR", Vector3(0, ry - 0.1, -3.0), func(): _show("main"))
	_refresh_toggles()
	# --- Crédits ---
	var c := _screen("credits")
	World.label(c, "PROJECT-M13", Vector3(0, 2.6, -3.2), 0.0045, Color(1, 1, 1), 80)
	World.label(c, "Une histoire de Wyatt (Siroxtag)\nTome 1 : La Page 404\n\nVersion de test VR\nMeta Quest", Vector3(0, 1.85, -3.2), 0.0028, Color(0.75, 0.82, 0.95), 56)
	_button(c, "RETOUR", Vector3(0, 0.95, -3.0), func(): _show("main"))

func _pick_new(slot: int) -> void:
	_pending_slot = slot
	_show("difficulty")

func _refresh_toggles() -> void:
	_toggles["move"].text = "DEPLACEMENT : " + ("TELEPORTATION" if Settings.move_mode == "teleport" else "FLUIDE")
	_toggles["turn"].text = "ROTATION : " + ("PAR CRANS" if Settings.turn_mode == "snap" else "FLUIDE")
	_toggles["vig"].text = "VIGNETTE : " + ("OUI" if Settings.vignette else "NON")
	_toggles["seat"].text = "MODE ASSIS : " + ("OUI" if Settings.seated else "NON")
	_toggles["dom"].text = "MAIN DOMINANTE : " + ("DROITE" if Settings.dominant == "right" else "GAUCHE")

func _toggle_move() -> void:
	Settings.move_mode = "smooth" if Settings.move_mode == "teleport" else "teleport"
	_changed()

func _toggle_turn() -> void:
	Settings.turn_mode = "smooth" if Settings.turn_mode == "snap" else "snap"
	_changed()

func _toggle_vig() -> void:
	Settings.vignette = not Settings.vignette
	_changed()

func _toggle_seat() -> void:
	Settings.seated = not Settings.seated
	_changed()

func _toggle_dom() -> void:
	Settings.dominant = "left" if Settings.dominant == "right" else "right"
	_changed()

func _changed() -> void:
	Settings.save()
	_refresh_toggles()

func _show(id: String) -> void:
	for k in screens:
		var root: Node3D = screens[k]
		var on: bool = (k == id)
		root.visible = on
		for child in root.get_children():
			if child is Area3D:
				for c in child.get_children():
					if c is CollisionShape3D:
						c.set_deferred("disabled", not on)
