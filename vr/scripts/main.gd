extends Node3D
# Point d'entrée : lance OpenXR, place le joueur et enchaîne menu / tutoriel / jeu.

const Rig := preload("res://scripts/rig.gd")
const MenuScript := preload("res://scripts/menu.gd")
const TutorialScript := preload("res://scripts/tutorial.gd")
const World := preload("res://scripts/world.gd")
const Button3D := preload("res://scripts/button3d.gd")

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
	show_menu()

func _swap(new_scene: Node3D) -> void:
	if scene:
		scene.queue_free()
	scene = new_scene
	add_child(scene)
	rig.recenter_to(scene.spawn_point(), 0.0)

func show_menu() -> void:
	rig.movement_enabled = false
	rig.ui_enabled = true
	var menu := MenuScript.new()
	menu.play.connect(_on_play)
	menu.tutorial.connect(show_tutorial)
	menu.quit.connect(func(): get_tree().quit())
	_swap(menu)

func _on_play() -> void:
	if not Settings.tutorial_done:
		show_tutorial()
	else:
		show_chapter_placeholder()

func show_tutorial() -> void:
	var tuto := TutorialScript.new()
	tuto.finished.connect(show_menu)
	_swap(tuto)
	rig.ui_enabled = true
	tuto.begin(rig)

func show_chapter_placeholder() -> void:
	# Le chapitre 1 arrive dans la prochaine version.
	var s := Node3D.new()
	World.environment(s, Color(0.02, 0.03, 0.07), Color(0.2, 0.25, 0.4), 0.05)
	var floor_body := World.box(s, Vector3(0, -0.05, 0), Vector3(30, 0.1, 30), Color(0.05, 0.06, 0.1), 0.0, true)
	floor_body.name = "Floor"
	World.blue_lines(s, Vector3.ZERO, 8.0, 24, 8.0)
	World.label(s, "CHAPITRE 1 : MIEL", Vector3(0, 2.4, -2.2), 0.01, Color(1, 1, 1), 80)
	World.label(s, "Jeudi de novembre. Il pleut sur Luynes.\n\nA suivre dans la prochaine version.", Vector3(0, 1.7, -2.2), 0.005, Color(0.75, 0.82, 0.95), 64)
	var b := Button3D.new()
	b.text = "RETOUR"
	b.position = Vector3(0, 1.0, -2.0)
	s.add_child(b)
	b.pressed.connect(show_menu)
	_swap_plain(s)

func _swap_plain(s: Node3D) -> void:
	if scene:
		scene.queue_free()
	scene = s
	add_child(scene)
	rig.recenter_to(Vector3(0, 0, 1.2), 0.0)
