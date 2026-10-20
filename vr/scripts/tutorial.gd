extends Node3D
# Tutoriel : apprendre à regarder, bouger, tourner, attraper, lire, utiliser le pouvoir « Retenir »,
# puis échapper à une Silhouette. Chaque étape se valide toute seule.

signal finished

const World := preload("res://scripts/world.gd")
const Button3D := preload("res://scripts/button3d.gd")

var rig
var panel_title: Label3D
var panel_text: Label3D
var panel_step: Label3D
var step := -1
var step_time := 0.0
var start_yaw := 0.0
var start_pos := Vector3.ZERO
var start_rig_yaw := 0.0
var page: Node3D
var held_by: XRController3D = null
var page_read := false
var silhouette: Node3D
var hit_count := 0
var survive := 0.0
var done_button: Node
var _powered := false
var _reading := false
var _flash: OmniLight3D

const STEPS := [
	{"title": "REGARDER", "text": "Tourne la tete pour regarder autour de toi.\nDeux lignes bleues t'attendent derriere."},
	{"title": "SE DEPLACER", "text": ""},
	{"title": "TOURNER", "text": ""},
	{"title": "ATTRAPER", "text": "Approche une main de la page lumineuse\net maintiens le bouton GRIP pour l'attraper."},
	{"title": "LIRE", "text": "Amene la page pres de ton visage\npour la lire."},
	{"title": "LE POUVOIR : RETENIR", "text": "Appuie sur A (main droite).\nPendant 5 secondes, tu es protege.\nRecharge : 12 secondes."},
	{"title": "FUIR", "text": "Une Silhouette arrive. Elle t'arrache un souvenir\nsi elle te touche. Utilise RETENIR (A) ou recule.\nTiens 20 secondes."},
	{"title": "TUTORIEL TERMINE", "text": "Tu es pret. Le Non-lieu t'attend."}
]

func _ready() -> void:
	World.environment(self, Color(0.82, 0.86, 0.96), Color(0.75, 0.8, 0.95), 0.015)
	var floor_body := World.box(self, Vector3(0, -0.05, 0), Vector3(40, 0.1, 40), Color(0.86, 0.88, 0.95), 0.0, true)
	floor_body.name = "Floor"
	for x in range(-20, 21, 4):
		World.box(self, Vector3(x, 0.001, 0), Vector3(0.03, 0.01, 40), Color(0.6, 0.65, 0.8))
		World.box(self, Vector3(0, 0.001, x), Vector3(40, 0.01, 0.03), Color(0.6, 0.65, 0.8))
	World.blue_lines(self, Vector3.ZERO, 14.0, 36, 9.0)
	World.light(self, Vector3(0, 4.0, 0), Color(0.9, 0.95, 1.0), 2.2, 18.0)
	_flash = World.light(self, Vector3(0, 1.5, 0), Color(0.3, 0.6, 1.0), 0.0, 6.0)
	# Panneau d'instructions, devant le joueur
	var panel := Node3D.new()
	panel.position = Vector3(0, 1.7, -2.4)
	add_child(panel)
	World.box(panel, Vector3(0, 0, -0.03), Vector3(2.4, 1.25, 0.04), Color(0.04, 0.05, 0.1), 0.0)
	panel_step = World.label(panel, "", Vector3(0, 0.5, 0), 0.004, Color(0.5, 0.75, 1.0), 56)
	panel_title = World.label(panel, "", Vector3(0, 0.3, 0), 0.007, Color(1, 1, 1), 80)
	panel_text = World.label(panel, "", Vector3(0, -0.15, 0), 0.0042, Color(0.85, 0.9, 1.0), 56)
	# La page (objet à attraper)
	page = Node3D.new()
	page.position = Vector3(0.7, 1.15, -1.3)
	page.visible = false
	add_child(page)
	World.box(page, Vector3.ZERO, Vector3(0.16, 0.22, 0.008), Color(0.9, 0.95, 1.0), 2.0)
	World.light(page, Vector3.ZERO, Color(0.5, 0.75, 1.0), 0.8, 2.0)
	World.box(self, Vector3(0.7, 0.55, -1.3), Vector3(0.25, 1.1, 0.25), Color(0.2, 0.22, 0.32))
	# La Silhouette
	silhouette = Node3D.new()
	silhouette.visible = false
	add_child(silhouette)
	var body := MeshInstance3D.new()
	var cap := CapsuleMesh.new()
	cap.radius = 0.28
	cap.height = 1.9
	body.mesh = cap
	body.material_override = World.mat(Color(0.01, 0.01, 0.02))
	body.position.y = 0.95
	silhouette.add_child(body)
	for ex in [-0.1, 0.1]:
		World.box(silhouette, Vector3(ex, 1.55, -0.26), Vector3(0.07, 0.03, 0.02), Color(0.7, 0.9, 1.0), 4.0)

func begin(player_rig) -> void:
	rig = player_rig
	rig.movement_enabled = true
	rig.power_used.connect(_on_power)
	rig.grabbed.connect(_on_grab)
	rig.released.connect(_on_release)
	_next()

func spawn_point() -> Vector3:
	return Vector3(0, 0, 1.0)

func _next() -> void:
	step += 1
	step_time = 0.0
	var data: Dictionary = STEPS[step]
	panel_step.text = "ETAPE %d / %d" % [step + 1, STEPS.size()]
	panel_title.text = data["title"]
	panel_text.text = data["text"]
	start_yaw = rig.head_yaw()
	start_pos = rig.cam.global_position
	start_rig_yaw = rig.rotation.y
	match step:
		1:
			var how := "Pousse le stick gauche vers l'avant, vise le sol,\nrelache pour te teleporter." if Settings.move_mode == "teleport" else "Pousse le stick gauche pour avancer."
			panel_text.text = how + "\nDeplace-toi de deux metres."
		2:
			panel_text.text = "Pousse le stick droit a gauche ou a droite\npour tourner" + (" par crans." if Settings.turn_mode == "snap" else ".")
		3:
			page.visible = true
		5:
			_powered = false
		6:
			silhouette.visible = true
			silhouette.global_position = Vector3(0, 0, -9)
			survive = 0.0
			hit_count = 0
		7:
			Settings.tutorial_done = true
			Settings.save()
			rig.movement_enabled = false
			done_button = Button3D.new()
			done_button.text = "RETOUR AU MENU"
			done_button.position = Vector3(0, 0.9, -2.2)
			add_child(done_button)
			done_button.pressed.connect(func(): finished.emit())

func _process(delta: float) -> void:
	if rig == null or step < 0 or step >= STEPS.size():
		return
	step_time += delta
	match step:
		0:
			if absf(angle_difference(start_yaw, rig.head_yaw())) > deg_to_rad(60.0):
				_next()
		1:
			if rig.cam.global_position.distance_to(start_pos) > 2.0:
				_next()
		2:
			if absf(angle_difference(start_rig_yaw, rig.rotation.y)) > deg_to_rad(25.0):
				_next()
		3:
			if held_by:
				_next()
		4:
			if held_by:
				page.global_transform = Transform3D(held_by.global_basis, held_by.global_position + held_by.global_basis * Vector3(0, 0.08, -0.1))
			if not _reading and page.global_position.distance_to(rig.cam.global_position) < 0.4 and step_time > 0.5:
				_reading = true
				panel_text.text = "« Page 41 : ta vie est un livre.\nQuelqu'un en arrache les pages. »"
				_flash.light_energy = 3.0
				await get_tree().create_timer(2.5).timeout
				_flash.light_energy = 0.0
				if step == 4:
					page.visible = false
					_next()
		5:
			if _powered and step_time > 1.0:
				_next()
		6:
			_update_silhouette(delta)

func _update_silhouette(delta: float) -> void:
	var target := rig.cam.global_position
	target.y = 0.0
	var pos := silhouette.global_position
	var dir := (target - pos)
	var dist := dir.length()
	if dist > 0.1:
		silhouette.look_at(Vector3(target.x, pos.y, target.z), Vector3.UP)
		silhouette.rotate_y(PI)
	if dist > 0.01:
		silhouette.global_position += dir.normalized() * 1.1 * delta
	if dist < 1.0:
		if rig.is_protected():
			silhouette.global_position -= dir.normalized() * 3.0 * delta
		else:
			hit_count += 1
			panel_text.text = "Elle t'a pris un souvenir. Recule !\nTiens 20 secondes. (%d)" % hit_count
			silhouette.global_position = Vector3(0, 0, -9)
			rig._haptic(rig.right(), 1.0)
			rig._haptic(rig.left(), 1.0)
	survive += delta
	if survive >= 20.0:
		silhouette.visible = false
		_next()

func _on_power() -> void:
	_powered = true
	_flash.light_energy = 2.5
	await get_tree().create_timer(0.6).timeout
	_flash.light_energy = 0.0

func _on_grab(hand: XRController3D) -> void:
	if step == 3 and page.visible and hand.global_position.distance_to(page.global_position) < 0.35:
		held_by = hand

func _on_release(hand: XRController3D) -> void:
	if hand == held_by and step != 4:
		held_by = null
