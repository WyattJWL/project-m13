extends Node3D
# Point d'entrée : lance OpenXR, place le joueur et enchaîne menu / tutoriel / jeu.

const Rig := preload("res://scripts/rig.gd")
const MenuScript := preload("res://scripts/menu.gd")
const TutorialScript := preload("res://scripts/tutorial.gd")
const GameScript := preload("res://scripts/game.gd")
const World := preload("res://scripts/world.gd")
const Props := preload("res://scripts/props.gd")
const Button3D := preload("res://scripts/button3d.gd")
const Sfx := preload("res://scripts/sfx.gd")

var xr_interface: XRInterface
var rig
var scene: Node3D

func _ready() -> void:
	xr_interface = XRServer.find_interface("OpenXR")
	if xr_interface and xr_interface.is_initialized():
		get_viewport().use_xr = true
		get_viewport().vrs_mode = Viewport.VRS_XR
		DisplayServer.window_set_vsync_mode(DisplayServer.VSYNC_DISABLED)
		Engine.physics_ticks_per_second = 72
	else:
		push_warning("OpenXR non initialisé : lance ce projet sur un casque.")
	rig = Rig.new()
	add_child(rig)
	rig.quit_to_menu.connect(show_menu)
	show_menu()

func _swap(new_scene: Node3D) -> void:
	if scene:
		scene.queue_free()
	scene = new_scene
	add_child(scene)
	rig.recenter_to(scene.spawn_point(), 0.0)
	# Le suivi de la tête n'est pas toujours prêt à la première image : on recale juste après.
	var sc := scene
	await get_tree().create_timer(0.6).timeout
	if scene == sc:
		rig.recenter_to(sc.spawn_point(), 0.0)

func show_menu() -> void:
	rig.movement_enabled = false
	rig.ui_enabled = true
	rig.set_menu_available(false)
	rig.hint_controller("", "")
	var menu := MenuScript.new()
	menu.new_game.connect(func(slot: int, diff: String):
		Settings.new_game(slot, diff)
		show_tutorial())
	menu.load_game.connect(func(slot: int):
		Settings.load_game(slot)
		if Settings.tutorial_done():
			show_game()
		else:
			show_tutorial())
	menu.quit.connect(func(): get_tree().quit())
	_swap(menu)
	Sfx.ambience(menu)

func show_tutorial() -> void:
	var tuto := TutorialScript.new()
	tuto.finished.connect(show_game)
	_swap(tuto)
	rig.ui_enabled = true
	tuto.begin(rig)

func show_game() -> void:
	var game := GameScript.new()
	game.finished.connect(show_menu)
	_swap(game)
	rig.ui_enabled = true
	game.begin(rig)

func show_chapter_placeholder() -> void:
	# Le chapitre 1 arrive dans la prochaine version.
	var s := Node3D.new()
	Props.night_env(s)
	Props.ground(s)
	Props.forest(s, 21, 150, Rect2(-40, -45, 80, 65), [Rect2(-8, -8, 16, 14)])
	Props.lantern(s, Vector3(-2.5, 0, -1.0), Color(1.0, 0.72, 0.38))
	World.blue_lines(s, Vector3(0, 0, -5), 11.0, 12, 9.0)
	World.label(s, "CHAPITRE 1 : MIEL", Vector3(0, 2.5, -3.2), 0.005, Color(1, 1, 1), 80)
	World.label(s, "Jeudi de novembre. Il pleut sur Luynes.\n\nA suivre dans la prochaine version.", Vector3(0, 1.8, -3.2), 0.0028, Color(0.75, 0.82, 0.95), 56)
	var b := Button3D.new()
	b.text = "RETOUR"
	b.position = Vector3(0, 1.0, -3.0)
	s.add_child(b)
	b.pressed.connect(show_menu)
	rig.set_menu_available(true)
	rig.movement_enabled = true
	Sfx.ambience(s)
	_swap_plain(s)

func _swap_plain(s: Node3D) -> void:
	if scene:
		scene.queue_free()
	scene = s
	add_child(scene)
	rig.recenter_to(Vector3(0, 0, 1.2), 0.0)
