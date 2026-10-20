extends Node3D
# Menu principal : un hall sombre, le titre, des boutons 3D à viser au laser.

signal play
signal tutorial
signal quit

const World := preload("res://scripts/world.gd")
const Button3D := preload("res://scripts/button3d.gd")

var main_root: Node3D
var settings_root: Node3D
var credits_root: Node3D
var _toggles: Dictionary = {}

func _ready() -> void:
	World.environment(self, Color(0.02, 0.03, 0.07), Color(0.18, 0.22, 0.4), 0.05)
	var floor_body := World.box(self, Vector3(0, -0.05, 0), Vector3(30, 0.1, 30), Color(0.05, 0.06, 0.1), 0.0, true)
	floor_body.name = "Floor"
	World.blue_lines(self, Vector3(0, 0, 0), 9.0, 28, 8.0)
	World.light(self, Vector3(0, 3.5, -1.5), Color(0.5, 0.7, 1.0), 2.0, 9.0)
	_build_main()
	_build_settings()
	_build_credits()
	_show(main_root)

func spawn_point() -> Vector3:
	return Vector3(0, 0, 1.2)

func _button(parent: Node, text: String, pos: Vector3, callback: Callable) -> Node:
	var b := Button3D.new()
	b.text = text
	b.position = pos
	parent.add_child(b)
	b.pressed.connect(callback)
	return b

func _build_main() -> void:
	main_root = Node3D.new()
	add_child(main_root)
	World.label(main_root, "PROJECT-M13", Vector3(0, 2.55, -2.2), 0.012, Color(1, 1, 1), 96)
	World.label(main_root, "TOME 1 : LA PAGE 404", Vector3(0, 2.15, -2.2), 0.006, Color(0.5, 0.75, 1.0), 80)
	var y := 1.6
	_button(main_root, "JOUER", Vector3(0, y, -2.0), func(): play.emit())
	_button(main_root, "TUTORIEL", Vector3(0, y - 0.32, -2.0), func(): tutorial.emit())
	_button(main_root, "REGLAGES", Vector3(0, y - 0.64, -2.0), func(): _show(settings_root))
	_button(main_root, "CREDITS", Vector3(0, y - 0.96, -2.0), func(): _show(credits_root))
	_button(main_root, "QUITTER", Vector3(0, y - 1.28, -2.0), func(): quit.emit())
	World.label(main_root, "Vise avec le laser, gachette pour valider", Vector3(0, 0.12, -1.9), 0.0035, Color(0.6, 0.65, 0.75), 56)

func _build_settings() -> void:
	settings_root = Node3D.new()
	add_child(settings_root)
	World.label(settings_root, "REGLAGES DE CONFORT", Vector3(0, 2.4, -2.2), 0.008, Color(1, 1, 1), 80)
	var y := 1.9
	_toggles["move"] = _button(settings_root, "", Vector3(0, y, -2.0), _toggle_move)
	_toggles["turn"] = _button(settings_root, "", Vector3(0, y - 0.32, -2.0), _toggle_turn)
	_toggles["vig"] = _button(settings_root, "", Vector3(0, y - 0.64, -2.0), _toggle_vignette)
	_toggles["seat"] = _button(settings_root, "", Vector3(0, y - 0.96, -2.0), _toggle_seated)
	_button(settings_root, "RETOUR", Vector3(0, y - 1.5, -2.0), func(): _show(main_root))
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
	World.label(credits_root, "PROJECT-M13", Vector3(0, 2.4, -2.2), 0.01, Color(1, 1, 1), 80)
	World.label(credits_root, "Une histoire de JWL Marketing\nTome 1 : La Page 404\n\nVersion de test VR\nMeta Quest", Vector3(0, 1.7, -2.2), 0.005, Color(0.75, 0.82, 0.95), 64)
	_button(credits_root, "RETOUR", Vector3(0, 0.95, -2.0), func(): _show(main_root))

func _show(root: Node3D) -> void:
	for r in [main_root, settings_root, credits_root]:
		r.visible = (r == root)
		for child in r.get_children():
			if child is Area3D:
				child.monitorable = (r == root)
				for c in child.get_children():
					if c is CollisionShape3D:
						c.disabled = (r != root)
