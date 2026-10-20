extends "res://scripts/tutorial.gd"
# Le Tome 1 en VR : enchaîne les 12 chapitres (scripts/ch/ch01.gd ... ch12.gd).
# Les chapitres appellent les fonctions de ce nœud : scene(), say(), npc(), doc(), give(), fight(), choice()...

const Locations := preload("res://scripts/locations.gd")
const Enemy := preload("res://scripts/enemy.gd")
const CHAPTERS := [
	preload("res://scripts/ch/ch01.gd"), preload("res://scripts/ch/ch02.gd"), preload("res://scripts/ch/ch03.gd"),
	preload("res://scripts/ch/ch04.gd"), preload("res://scripts/ch/ch05.gd"), preload("res://scripts/ch/ch06.gd"),
	preload("res://scripts/ch/ch07.gd"), preload("res://scripts/ch/ch08.gd"), preload("res://scripts/ch/ch09.gd"),
	preload("res://scripts/ch/ch10.gd"), preload("res://scripts/ch/ch11.gd"), preload("res://scripts/ch/ch12.gd"),
]

var stage: Node3D
var marks: Dictionary = {}
var spawn_pos := Vector3.ZERO
var enemies: Array = []
var lives := 3
var fade_mat: StandardMaterial3D
var read_panel: Node3D
var read_title: Label3D
var read_text: Label3D
var read_docs: Dictionary = {}       # id -> true
var chosen := -1
var door_done := false
var card: Label3D

func _ready() -> void:
	_build_hud()
	stage = Node3D.new()
	add_child(stage)

func spawn_point() -> Vector3:
	return Vector3.ZERO

func begin(player_rig) -> void:
	rig = player_rig
	rig.movement_enabled = true
	rig.set_menu_available(true)
	rig.telekinesis_enabled = true
	show_power = true
	_build_overlays()
	_run_story()

func _build_overlays() -> void:
	var fade := MeshInstance3D.new()
	var qm := QuadMesh.new()
	qm.size = Vector2(3, 3)
	fade.mesh = qm
	fade_mat = StandardMaterial3D.new()
	fade_mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	fade_mat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	fade_mat.albedo_color = Color(0, 0, 0, 0)
	fade_mat.no_depth_test = true
	fade_mat.render_priority = 100
	fade.material_override = fade_mat
	fade.position = Vector3(0, 0, -0.15)
	rig.cam.add_child(fade)
	card = Label3D.new()
	card.position = Vector3(0, 0.0, -1.4)
	card.font_size = 64
	card.pixel_size = 0.0016
	card.width = 1100
	card.outline_size = 10
	card.no_depth_test = true
	card.render_priority = 120
	card.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	card.modulate = Color(1, 1, 1, 0)
	rig.cam.add_child(card)
	# panneau de lecture (devant le visage quand on lit un document)
	read_panel = Node3D.new()
	read_panel.position = Vector3(0, -0.02, -0.6)
	read_panel.visible = false
	rig.cam.add_child(read_panel)
	var back := MeshInstance3D.new()
	var bq := QuadMesh.new()
	bq.size = Vector2(0.62, 0.56)
	back.mesh = bq
	var bm := StandardMaterial3D.new()
	bm.albedo_color = Color(0.9, 0.86, 0.74)
	bm.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	bm.no_depth_test = true
	bm.render_priority = 110
	back.material_override = bm
	read_panel.add_child(back)
	read_title = Label3D.new()
	read_title.position = Vector3(0, 0.23, 0.002)
	read_title.font_size = 38
	read_title.pixel_size = 0.0007
	read_title.width = 780
	read_title.modulate = Color(0.25, 0.1, 0.08)
	read_title.no_depth_test = true
	read_title.render_priority = 115
	read_title.outline_size = 0
	read_panel.add_child(read_title)
	read_text = Label3D.new()
	read_text.position = Vector3(-0.28, 0.17, 0.002)
	read_text.font_size = 34
	read_text.pixel_size = 0.0007
	read_text.width = 780
	read_text.modulate = Color(0.15, 0.1, 0.08)
	read_text.horizontal_alignment = HORIZONTAL_ALIGNMENT_LEFT
	read_text.vertical_alignment = VERTICAL_ALIGNMENT_TOP
	read_text.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	read_text.no_depth_test = true
	read_text.render_priority = 115
	read_text.outline_size = 0
	read_panel.add_child(read_text)

func _process(delta: float) -> void:
	super(delta)
	if power_label and rig:
		var dots := ""
		for i in 3:
			dots += "● " if i < lives else "○ "
		power_label.text = "SOUVENIRS  %s |  %s" % [dots, rig.power_label()]
	if rig and read_panel:
		_update_reading()

func _update_reading() -> void:
	var showing := false
	for hand in rig.hands:
		var it = rig.inventory.held_item(hand)
		if it != null and it.kind == "doc":
			var d: float = it.global_position.distance_to(rig.cam.global_position)
			if d < 0.5:
				read_title.text = String(it.get_meta("title"))
				read_text.text = String(it.get_meta("text"))
				read_panel.visible = true
				showing = true
				it.set_meta("reading", true)
				read_docs[it.get_meta("id", "")] = true
	if not showing:
		read_panel.visible = false

# ---------- Mise en scène ----------
func fade(to_black: bool, seconds := 0.7) -> void:
	var tw := create_tween()
	tw.tween_property(fade_mat, "albedo_color:a", 1.0 if to_black else 0.0, seconds)
	await tw.finished

func scene(id: String, extra := {}) -> void:
	await fade(true, 0.6)
	for e in enemies:
		if is_instance_valid(e):
			e.queue_free()
	enemies.clear()
	for n in get_tree().get_nodes_in_group("item"):
		if n.state == "free":
			n.queue_free()
	for c in stage.get_children():
		c.queue_free()
	await get_tree().process_frame
	var info: Dictionary
	if id == "nonlieu":
		info = Locations.nonlieu(stage, rig, extra.get("doors", [38, 39, 40, 41, 42, 43]))
	else:
		info = Locations.build(id, stage, rig)
	marks = info["marks"]
	spawn_pos = info["spawn"]
	rig.recenter_to(spawn_pos, info.get("yaw", 0.0))
	Sfx.ambience(stage)
	await fade(false, 0.7)

func card_text(title: String, text := "", seconds := 4.5) -> void:
	await fade(true, 0.8)
	card.text = title + ("\n\n" + text if text != "" else "")
	var tw := create_tween()
	tw.tween_property(card, "modulate:a", 1.0, 1.0)
	await get_tree().create_timer(seconds).timeout
	var tw2 := create_tween()
	tw2.tween_property(card, "modulate:a", 0.0, 0.8)
	await tw2.finished
	await fade(false, 0.8)

func say(who: String, text: String) -> void:
	await _say(who, text)

func obj(t: String) -> void:
	_set_objective(t)

func hint(t: String) -> void:
	_hint(t)

func controller_hint(side: String, part: String) -> void:
	rig.hint_controller(side, part)

# ---------- Personnages et objets ----------
func npc(who: String, at, color := Color(0.5, 0.5, 0.6)) -> Node3D:
	var pos: Vector3 = marks[at] if at is String else at
	var n := Node3D.new()
	n.position = Vector3(pos.x, 0, pos.z)
	stage.add_child(n)
	World.bx(n, Vector3(0, 0, 0), Vector3(0.42, 1.05, 0.26), color)
	World.bx(n, Vector3(-0.1, 0, 0), Vector3(0.16, 0.7, 0.18), color * 0.6)
	World.bx(n, Vector3(0.1, 0, 0), Vector3(0.16, 0.7, 0.18), color * 0.6)
	var head := MeshInstance3D.new()
	var sm := SphereMesh.new()
	sm.radius = 0.13
	sm.height = 0.26
	head.mesh = sm
	head.position = Vector3(0, 1.62, 0)
	head.material_override = World.mat(Color(0.85, 0.68, 0.55))
	n.add_child(head)
	World.label(n, who, Vector3(0, 1.95, 0), 0.0035, Color(1, 0.9, 0.7), 56).billboard = BaseMaterial3D.BILLBOARD_ENABLED
	return n

func doc(id: String, title: String, text: String, at) -> Node:
	var pos: Vector3 = marks[at] if at is String else at
	var d := Items.doc(title, text)
	d.set_meta("id", id)
	d.position = pos + Vector3(0, 0.05, 0)
	add_child(d)
	return d

func give(kind: String, at) -> Node:
	var pos: Vector3 = marks[at] if at is String else at
	var it: Node
	match kind:
		"knife":
			it = Items.knife()
		"bat":
			it = Items.bat()
		"hatchet":
			it = Items.hatchet()
		"key":
			it = Items.key()
		"poincon":
			it = Items.poincon()
		_:
			it = Items.knife()
	it.position = pos + Vector3(0, 0.05, 0)
	add_child(it)
	return it

func prop(kind: String, at) -> Node:
	var pos: Vector3 = marks[at] if at is String else at
	var b: RigidBody3D = Props.barrel() if kind == "barrel" else Props.crate()
	b.position = pos + Vector3(0, 0.3, 0)
	add_child(b)
	return b

# ---------- Attentes ----------
func wait_read(id: String) -> void:
	read_docs.erase(id)
	await _wait(func(): return read_docs.has(id))

func wait_held(kind: String) -> void:
	await _wait(func(): return _holding(kind))

func wait_near(at, radius := 1.6) -> void:
	var pos: Vector3 = marks[at] if at is String else at
	await _wait(func(): return _flat_dist(rig.cam.global_position, pos) < radius)

func wait_time(seconds: float) -> void:
	await get_tree().create_timer(seconds).timeout

# Poser la main (ou une manette) contre un point pendant N secondes.
func hold_at(at, seconds := 2.0, radius := 0.22) -> void:
	var pos: Vector3 = marks[at] if at is String else at
	var t := 0.0
	while _alive and t < seconds:
		var near := false
		for h in rig.hands:
			if h.global_position.distance_to(pos) < radius:
				near = true
		if near:
			t += get_process_delta_time()
			if fmod(t, 0.4) < get_process_delta_time():
				rig._haptic(rig.right(), 0.3)
				rig._haptic(rig.left(), 0.3)
		else:
			t = maxf(0.0, t - get_process_delta_time())
		await get_tree().process_frame

# Boutons de choix devant le joueur. Renvoie l'indice choisi.
func choice(prompt: String, options: Array) -> int:
	chosen = -1
	var root := Node3D.new()
	var yaw: float = rig.head_yaw()
	var f := Vector3(-sin(yaw), 0, -cos(yaw))
	root.position = rig.cam.global_position + f * 1.7
	root.rotation.y = yaw
	add_child(root)
	World.label(root, prompt, Vector3(0, 0.55, 0), 0.0028, Color(1, 0.9, 0.7), 56)
	var buttons: Array = []
	for i in options.size():
		var b := Button3D.new()
		b.size = Vector3(2.4, 0.3, 0.05)
		b.text = options[i]
		b.position = Vector3(0, 0.2 - i * 0.36, 0)
		root.add_child(b)
		var idx := i
		b.pressed.connect(func(): chosen = idx)
		buttons.append(b)
	await _wait(func(): return chosen >= 0)
	root.queue_free()
	return chosen

# ---------- Ennemis ----------
func spawn_enemy(kind := "silhouette", angle_deg := -1.0) -> Node:
	var e := Enemy.new()
	add_child(e)
	var yaw: float = rig.head_yaw() + deg_to_rad(angle_deg if angle_deg >= 0.0 else randf_range(120.0, 240.0))
	var c: Vector3 = rig.cam.global_position
	var at := Vector3(c.x - sin(yaw) * 11.0, 0, c.z - cos(yaw) * 11.0)
	if rig.bounds.size != Vector2.ZERO:
		at.x = clampf(at.x, rig.bounds.position.x, rig.bounds.end.x)
		at.z = clampf(at.z, rig.bounds.position.y, rig.bounds.end.y)
	e.setup(rig, kind, at, Settings.enemy_speed() / 1.2)
	e.touched.connect(_on_touched)
	enemies.append(e)
	Sfx.play(self, "whisper", at, -4.0)
	return e

func _on_touched(_e: Node) -> void:
	lives -= 1
	Sfx.play(self, "hurt", null, -2.0)
	rig._haptic(rig.right(), 1.0)
	rig._haptic(rig.left(), 1.0)
	_hint("Un souvenir t'a été arraché.")
	if lives <= 0:
		_faint()

func _faint() -> void:
	for e in enemies:
		if is_instance_valid(e):
			e.vanish()
	enemies.clear()
	await fade(true, 0.8)
	lives = 3
	rig.recenter_to(spawn_pos, 0.0)
	_hint("Tu perds connaissance... et tu te réveilles au début de la scène.")
	await fade(false, 0.8)

func alive_count() -> int:
	var n := 0
	for e in enemies:
		if is_instance_valid(e) and e.alive:
			n += 1
	return n

# Lance `count` ennemis (par vagues d'un coup) et attend qu'ils soient tous repoussés, ou la fin du délai.
func fight(count: int, timeout := 60.0, kind := "silhouette") -> void:
	for i in count:
		spawn_enemy(kind, 120.0 + 240.0 * float(i) / float(maxi(1, count)))
	var t := 0.0
	while _alive and alive_count() > 0 and t < timeout:
		await get_tree().process_frame
		t += get_process_delta_time()
	for e in enemies:
		if is_instance_valid(e) and e.alive:
			e.vanish()
	enemies.clear()

func boss(kind := "kayden", extra := 3, timeout := 120.0) -> void:
	var b := spawn_enemy(kind, 180.0)
	var t := 0.0
	var next_wave := 12.0
	while _alive and b.alive and t < timeout:
		await get_tree().process_frame
		t += get_process_delta_time()
		if t > next_wave and alive_count() < extra + 1:
			next_wave += 14.0
			spawn_enemy("silhouette")
	for e in enemies:
		if is_instance_valid(e) and e.alive:
			e.vanish()
	enemies.clear()

# Portes numérotées du Non-lieu : appuie sur la bonne. Une mauvaise réveille une Silhouette.
func door_puzzle(doors: Array, correct: int) -> void:
	door_done = false
	var door_marks: Dictionary = marks["doors"]
	for num in doors:
		var n: int = num
		var p: Vector3 = door_marks[n]
		var b := Button3D.new()
		b.size = Vector3(0.9, 0.34, 0.06)
		b.text = "OUVRIR %d" % n
		b.position = p + Vector3(0, -0.2, 0) + Vector3(-0.1 if p.x > 0 else 0.1, 0, 0)
		b.rotation_degrees.y = 90 if p.x > 0 else -90
		stage.add_child(b)
		b.pressed.connect(func():
			if n == correct:
				door_done = true
			else:
				spawn_enemy("silhouette")
				_hint("Pas celle-là. Quelque chose s'est réveillé."))
	await _wait(func(): return door_done)
	for e in enemies:
		if is_instance_valid(e):
			e.vanish()
	enemies.clear()

# ---------- Déroulement ----------
func _run_story() -> void:
	var n := Settings.chapter()
	while _alive and n <= CHAPTERS.size():
		lives = 3
		await CHAPTERS[n - 1].run(self)
		n += 1
		Settings.set_chapter(n)
	if _alive:
		await end_book()

func end_book() -> void:
	await card_text("FIN DU TOME 1", "« Commençons la fin du monde. »\n\nLa suite : Tome 2, Les Pages Retirées.", 9.0)
	Settings.set_chapter(1)
	finished.emit()
