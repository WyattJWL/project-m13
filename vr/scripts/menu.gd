extends Node3D
# Menu principal : un hall sombre, le titre, des boutons 3D à viser au laser.

signal play
signal tutorial
signal quit

const World := preload("res://scripts/world.gd")
const Props := preload("res://scripts/props.gd")
const Button3D := preload("res://scripts/button3d.gd")

var main_root: Node3D
var settings_root: Node3D
var credits_root: Node3D
var _toggles: Dictionary = {}

func _ready() -> void:
	# Une clairière de forêt, la nuit, avec les lignes bleues du Non-lieu au loin.
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
	_build_main()
	_build_settings()
	_build_credits()
	_show(main_root)

func spawn_point() -> Vector3:
	return Vector3(0, 0, 1.5)

func _button(parent: Node, text: String, pos: Vector3, callback: Callable, width := 2.1) -> Node:
	var b := Button3D.new()
	b.size = Vector3(width, 0.34, 0.06)
	b.text = text
	b.position = pos
	parent.add_child(b)
	b.pressed.connect(callback)
	return b

func _build_main() -> void:
	main_root = Node3D.new()
	add_child(main_root)
	World.label(main_root, "PROJECT-M13", Vector3(0, 2.85, -3.2), 0.0045, Color(1, 1, 1), 96)
	World.label(main_root, "TOME 1 : LA PAGE 404", Vector3(0, 2.3, -3.2), 0.0028, Color(0.5, 0.75, 1.0), 80)
	var y := 1.75
	_button(main_root, "JOUER", Vector3(0, y, -3.0), func(): play.emit())
	_button(main_root, "TUTORIEL", Vector3(0, y - 0.4, -3.0), func(): tutorial.emit())
	_button(main_root, "REGLAGES", Vector3(0, y - 0.8, -3.0), func(): _show(settings_root))
	_button(main_root, "CREDITS", Vector3(0, y - 1.2, -3.0), func(): _show(credits_root))
	_button(main_root, "QUITTER", Vector3(0, y - 1.6, -3.0), func(): quit.emit())
	World.label(main_root, "Vise avec le laser, gachette pour valider", Vector3(0, 0.12, -2.9), 0.0026, Color(0.6, 0.65, 0.75), 56)

func _build_settings() -> void:
	settings_root = Node3D.new()
	add_child(settings_root)
	World.label(settings_root, "REGLAGES DE CONFORT", Vector3(0, 2.55, -3.2), 0.0035, Color(1, 1, 1), 80)
	var y := 1.9
	_toggles["move"] = _button(settings_root, "", Vector3(0, y, -3.0), _toggle_move, 3.4)
	_toggles["turn"] = _button(settings_root, "", Vector3(0, y - 0.4, -3.0), _toggle_turn, 3.4)
	_toggles["vig"] = _button(settings_root, "", Vector3(0, y - 0.8, -3.0), _toggle_vignette, 3.4)
	_toggles["seat"] = _button(settings_root, "", Vector3(0, y - 1.2, -3.0), _toggle_seated, 3.4)
	_button(settings_root, "RETOUR", Vector3(0, y - 1.5, -3.0), func(): _show(main_root))
	_refresh_toggles()

func _refresh_toggles() -> void:
	_toggles["move"].text = "DEPLACEMENT : " + ("TELEPORTATION" if Settings.move_mode == "teleport" else "FLUIDE")
	_toggles["turn"].text = "ROTATION : " + ("PAR CRANS" if Settings.turn_mode == "snap" else "FLUIDE")
	_toggles["vig"].text = "VIGNETTE : " + ("OUI" if Settings.vignette else "NON")
	_toggles["seat"].text = "MODE ASSIS : " + ("OUI" if Settings.seated else "NON")

func _toggle_move() -> void:
	Settings.move_mode = "smooth" if Settings.move_mode == "teleport" else "teleport"
	_changed()

func _toggle_turn() -> void:
	Settings.turn_mode = "smooth" if Settings.turn_mode == "snap" else "snap"
	_changed()

func _toggle_vignette() -> void:
	Settings.vignette = not Settings.vignette
	_changed()

func _toggle_seated() -> void:
	Settings.seated = not Settings.seated
	_changed()

func _changed() -> void:
	Settings.save()
	_refresh_toggles()

func _build_credits() -> void:
	credits_root = Node3D.new()
	add_child(credits_root)
	World.label(credits_root, "PROJECT-M13", Vector3(0, 2.6, -3.2), 0.0045, Color(1, 1, 1), 80)
	World.label(credits_root, "Une histoire de Wyatt (Siroxtag)\nTome 1 : La Page 404\n\nVersion de test VR\nMeta Quest", Vector3(0, 1.85, -3.2), 0.0028, Color(0.75, 0.82, 0.95), 56)
	_button(credits_root, "RETOUR", Vector3(0, 0.95, -3.0), func(): _show(main_root))

func _show(root: Node3D) -> void:
	for r in [main_root, settings_root, credits_root]:
		r.visible = (r == root)
		for child in r.get_children():
			if child is Area3D:
				child.monitorable = (r == root)
				for c in child.get_children():
					if c is CollisionShape3D:
						c.disabled = (r != root)
