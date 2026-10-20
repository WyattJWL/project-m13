extends Node3D
# Tutoriel dans la forêt : on avance le long d'un chemin et Darius commente chaque étape.
# Les consignes s'affichent dans un bandeau qui suit doucement le regard (un seul message à la fois).

signal finished

const World := preload("res://scripts/world.gd")
const Props := preload("res://scripts/props.gd")
const Button3D := preload("res://scripts/button3d.gd")
const Sfx := preload("res://scripts/sfx.gd")
const Items := preload("res://scripts/items.gd")
const DoorScript := preload("res://scripts/door.gd")

var rig
var hud: Node3D
var obj_label: Label3D
var talk_label: Label3D
var hint_label: Label3D
var power_label: Label3D
var show_power := false
var speaker_label: Label3D
var held_page := false
var page: Node3D
var held_by: XRController3D = null
var crates: Array[RigidBody3D] = []
var target_area: Area3D
var target_hit := false
var tk_grabbed := false
var tk_pulled := false
var powered := false
var silhouette: Node3D
var survive_left := 0.0
var hits := 0
var light: OmniLight3D
var beacon: Array[Node3D] = []
var dummy: Node3D
var dummy_hits := 0
var door
var door_open := false
var hits_taken := 0
var stun_until := 0.0
var _alive := true

func _ready() -> void:
	Props.night_env(self)
	Props.ground(self)
	Props.path(self, 6.0, -48.0, 3.2)
	var clear: Array = [Rect2(-3.0, -48.0, 6.0, 56.0), Rect2(-9.0, -30.0, 18.0, 16.0)]
	Props.forest(self, 7, 170, Rect2(-45, -75, 90, 95), clear)
	Props.grass(self, 11, 500, Rect2(-14, -42, 28, 52), [Rect2(-1.4, -48.0, 2.8, 56.0)])
	Props.rocks(self, 5, 28, Rect2(-30, -60, 60, 70), [Rect2(-3.0, -48.0, 6.0, 56.0)])
	# lanternes le long du chemin
	for i in 6:
		Props.lantern(self, Vector3(1.9 if i % 2 == 0 else -1.9, 0, 2.0 - i * 7.0), Color(1.0, 0.72, 0.38), i % 2 == 0)
	# balise bleue (premier but)
	var beacon_light := World.light(self, Vector3(0, 2.0, -9.0), Color(0.3, 0.6, 1.0), 2.4, 9.0)
	var beacon_pillar := World.box(self, Vector3(0, 2.0, -9.0), Vector3(0.12, 4.0, 0.12), Color(0.35, 0.7, 1.0), 4.0)
	beacon = [beacon_light, beacon_pillar]
	light = World.light(self, Vector3(0, 1.5, -9.0), Color(0.3, 0.6, 1.0), 0.0, 6.0)
	Props.standing_stone(self, Vector3(7.0, 0, -9.5), deg_to_rad(-70))
	Props.stump(self, Vector3(-2.2, 0, -10.0))
	_build_hud()

func spawn_point() -> Vector3:
	return Vector3(0, 0, 2.5)

# ---------- Bandeau d'instructions (suit la tête avec un léger retard) ----------
func _build_hud() -> void:
	hud = Node3D.new()
	hud.top_level = true
	add_child(hud)
	var back := MeshInstance3D.new()
	var qm := QuadMesh.new()
	qm.size = Vector2(1.8, 0.78)
	back.mesh = qm
	var m := StandardMaterial3D.new()
	m.albedo_color = Color(0.02, 0.03, 0.07, 0.72)
	m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	back.material_override = m
	back.position = Vector3(0, -0.03, -0.01)
	hud.add_child(back)
	obj_label = _hud_label(Vector3(0, 0.29, 0), 34, Color(0.5, 0.78, 1.0), true)
	speaker_label = _hud_label(Vector3(-0.66, 0.19, 0), 32, Color(1.0, 0.8, 0.45), false)
	talk_label = _hud_label(Vector3(-0.66, 0.12, 0), 38, Color.WHITE, false)
	talk_label.vertical_alignment = VERTICAL_ALIGNMENT_TOP
	hint_label = _hud_label(Vector3(0, -0.2, 0), 32, Color(0.6, 0.95, 0.7), true)
	power_label = _hud_label(Vector3(0, -0.32, 0), 32, Color(0.4, 1.0, 0.55), true)

func _hud_label(pos: Vector3, size: int, color: Color, centered: bool) -> Label3D:
	var l := Label3D.new()
	l.position = pos
	l.font_size = size
	l.pixel_size = 0.0013
	l.modulate = color
	l.outline_size = 8
	l.width = 1000
	l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER if centered else HORIZONTAL_ALIGNMENT_LEFT
	l.vertical_alignment = VERTICAL_ALIGNMENT_TOP if not centered else VERTICAL_ALIGNMENT_CENTER
	hud.add_child(l)
	return l

func _process(delta: float) -> void:
	if rig == null or not is_instance_valid(hud):
		return
	var cam: XRCamera3D = rig.cam
	var yaw := cam.global_rotation.y
	var forward := Vector3(-sin(yaw), 0, -cos(yaw))
	if show_power:
		power_label.text = rig.power_label()
		var st: Dictionary = rig.power_status()
		power_label.modulate = Color(0.4, 0.75, 1.0) if st["state"] == "protege" else (Color(1.0, 0.6, 0.25) if st["state"] == "recharge" else Color(0.4, 1.0, 0.55))
	var goal := cam.global_position + forward * 1.7 + Vector3(0, -0.45, 0)
	hud.global_position = hud.global_position.lerp(goal, clampf(delta * 3.0, 0.0, 1.0))
	var cur := hud.global_rotation.y
	hud.global_rotation = Vector3(0, lerp_angle(cur, yaw, clampf(delta * 3.0, 0.0, 1.0)), 0)

func _set_objective(t: String) -> void:
	obj_label.text = "OBJECTIF : " + t if t != "" else ""

func _hint(t: String) -> void:
	hint_label.text = t

# Une réplique : le texte s'écrit, puis on attend un peu (durée selon la longueur).
func _say(who: String, text: String) -> void:
	speaker_label.text = who.to_upper()
	talk_label.text = text
	talk_label.visible_characters = 0
	for i in text.length():
		if not _alive:
			return
		talk_label.visible_characters = i + 1
		await get_tree().create_timer(0.025).timeout
	await get_tree().create_timer(1.4 + text.length() * 0.035).timeout

func _wait(cond: Callable, timeout := 600.0) -> void:
	var t := 0.0
	while _alive and not cond.call() and t < timeout:
		await get_tree().process_frame
		t += get_process_delta_time()

func _flat_dist(a: Vector3, b: Vector3) -> float:
	return Vector2(a.x - b.x, a.z - b.z).length()

# ---------- Déroulement ----------
func begin(player_rig) -> void:
	rig = player_rig
	rig.movement_enabled = true
	rig.set_menu_available(true)
	Sfx.ambience(self)
	rig.power_used.connect(func(): powered = true)
	rig.grabbed.connect(_on_grab)
	rig.released.connect(_on_release)
	rig.telekinesis_grab.connect(func(_b): tk_grabbed = true)
	rig.telekinesis_pulled.connect(func(_b): tk_pulled = true)
	_run()

func _run() -> void:
	# 1. Regarder
	_set_objective("regarde autour de toi")
	await _say("Darius", "... Où suis-je ? Cette forêt, je ne l'ai jamais vue.")
	_hint("Tourne la tête pour regarder autour de toi.")
	var yaw0: float = rig.head_yaw()
	await _wait(func(): return absf(angle_difference(yaw0, rig.head_yaw())) > deg_to_rad(60.0))
	# 2. Avancer
	_set_objective("avance jusqu'à la lumière bleue")
	await _say("Darius", "Une lueur bleue, plus loin sur le chemin. Je n'ai pas le choix : j'y vais.")
	_hint("Stick GAUCHE : avancer, reculer, aller sur le côté.")
	rig.hint_controller("left", "stick")
	await _wait(func(): return _flat_dist(rig.cam.global_position, Vector3(0, 0, -9.0)) < 2.5)
	for n in beacon:
		if is_instance_valid(n):
			n.queue_free()
	Sfx.play(self, "pickup", null, -6.0)
	# 3. Tourner
	_set_objective("tourne-toi vers la pierre levée")
	await _say("Darius", "Cette pierre, sur le côté... Elle brille de la même lumière.")
	_hint("Stick DROIT : tourner. Ou tourne simplement ton corps.")
	rig.hint_controller("right", "stick")
	await _wait(_facing_stone)
	rig.hint_controller("", "")
	# 4. Attraper la page
	page = Props.page()
	page.position = Vector3(-2.2, 1.0, -10.0)
	add_child(page)
	_set_objective("attrape la page sur la souche")
	await _say("Darius", "Une page de papier, posée sur cette souche. Elle flotte.")
	_hint("Approche la main de la page et maintiens GRIP pour l'attraper.")
	rig.hint_controller("both", "grip")
	await _wait(func(): return held_by != null)
	# 5. Lire
	rig.hint_controller("", "")
	_set_objective("amène la page près de ton visage")
	await _say("Darius", "Elle est tiède. Je devrais la lire.")
	_hint("Rapproche la page de tes yeux.")
	await _wait(func(): return page.global_position.distance_to(rig.cam.global_position) < 0.4)
	_hint("")
	await _say("La page", "« Page 41. Une année contre une vérité. Quelqu'un a arraché la suite. »")
	page.queue_free()
	held_by = null
	# 6. Télékinésie
	_spawn_crates()
	_set_objective("lance une caisse dans l'anneau bleu")
	await _say("Darius", "Des caisses, là-bas, dans la clairière. Trop loin pour les toucher... et pourtant, je les sens.")
	_hint("Vise une caisse avec le laser et MAINTIENS GRIP : elle flotte à distance.")
	rig.hint_controller("both", "grip")
	await _wait(func(): return tk_grabbed)
	_hint("GACHETTE : la caisse vient dans ta main.")
	rig.hint_controller("both", "trigger")
	await _wait(func(): return tk_pulled)
	_hint("Bouge la main d'un geste franc et LACHE GRIP pour lancer. Vise l'anneau !")
	rig.hint_controller("both", "grip")
	await _wait(func(): return target_hit)
	_clear_crates()
	rig.hint_controller("", "")
	await _say("Darius", "Je déplace les choses d'un regard... Je ne sais pas ce que je suis en train de devenir.")
	# 7. Pouvoir Retenir
	_set_objective("utilise le pouvoir Retenir")
	await _say("Darius", "Quelque chose m'observe, dans les arbres. Je dois pouvoir me protéger.")
	_hint("Bouton %s : RETENIR. 5 secondes de protection, recharge %d s." % [rig.power_button_name(), int(Settings.power_cooldown())])
	rig.hint_controller("dom", "a")
	show_power = true
	await _wait(func(): return powered)
	rig.hint_controller("", "")
	light.light_energy = 4.0
	await _say("Darius", "Le temps ralentit... C'est ça, « retenir ».")
	light.light_energy = 2.4
	# 8. Armes et rangements
	_spawn_weapons()
	_set_objective("prends le couteau sur la table")
	await _say("Darius", "Sur cette table : un couteau et une batte. Je ne peux pas me défendre à mains nues.")
	_hint("Main près de l'arme, maintiens GRIP pour la saisir.")
	rig.hint_controller("both", "grip")
	await _wait(func(): return _holding("knife"))
	_set_objective("frappe le mannequin 3 fois")
	await _say("Darius", "Un mannequin d'entraînement. Un geste franc suffit.")
	_hint("Balance un coup rapide dans le mannequin (%d/3)." % 0)
	dummy_hits = 0
	await _wait(func():
		_hint("Balance un coup rapide dans le mannequin (%d/3)." % dummy_hits)
		return dummy_hits >= 3)
	rig.hint_controller("", "")
	_set_objective("range le couteau : poche (hanche) ou torse")
	await _say("Darius", "Les petits objets se rangent aux poches, sur les hanches, ou sur le torse.")
	_hint("Relâche GRIP près d'un point doré. Le couteau est petit : hanche ou torse.")
	await _wait(func(): return rig.inventory.stored_kinds().has("knife"))
	_set_objective("range la batte sur une épaule")
	await _say("Darius", "Les armes longues vont dans le dos, par-dessus l'épaule.")
	_hint("Prends la batte, puis passe la main derrière l'épaule et relâche GRIP.")
	await _wait(func(): return rig.inventory.has_in("shoulder_r") or rig.inventory.has_in("shoulder_l"))
	_set_objective("dégaine une arme")
	_hint("GRIP à l'endroit du rangement (épaule, hanche, torse) pour la sortir.")
	await _wait(func(): return _holding("bat") or _holding("knife"))
	# 9. Fuir ou se battre
	_set_objective("repousse la Silhouette ou survis 20 secondes")
	_build_silhouette()
	await _say("Darius", "Une Silhouette ! Frappe-la, elle recule après 3 coups. Ou utilise Retenir.")
	_hint("Frappe-la, recule (stick gauche) ou utilise %s : Retenir." % rig.power_button_name())
	rig.hint_controller("dom", "a")
	survive_left = 20.0
	hits_taken = 0
	await _wait(func(): return survive_left <= 0.0)
	silhouette.visible = false
	rig.hint_controller("", "")
	show_power = false
	power_label.text = ""
	_hint("")
	await _say("Darius", "Elle est partie. Il y a une cabane au bout du chemin.")
	# 10. Clé et porte
	_spawn_hut()
	_set_objective("prends la clé sur la souche")
	await _say("Darius", "Une clé, sur cette souche. Elle doit ouvrir la porte de la cabane.")
	_hint("GRIP près de la clé. Si ta main est pleine, range ton arme d'abord.")
	rig.hint_controller("both", "grip")
	await _wait(func(): return _holding("key"))
	_set_objective("enfonce la clé dans la serrure")
	await _say("Darius", "Marche jusqu'à la porte. La serrure est sur le côté, près de la poignée.")
	_hint("Approche le bout de la clé du trou de la serrure.")
	rig.hint_controller("", "")
	await _wait(func(): return door.state != "locked")
	_set_objective("tourne la clé")
	_hint("Tourne ton poignet comme une vraie clé (environ un quart de tour).")
	await _wait(func(): return door.state == "unlocked")
	_set_objective("ouvre la porte par la poignée")
	await _say("Darius", "Clic. Maintenant, la poignée.")
	_hint("GRIP sur la poignée en laiton, puis tire vers toi.")
	rig.hint_controller("both", "grip")
	await _wait(func(): return door_open)
	rig.hint_controller("", "")
	_hint("")
	_set_objective("")
	await _say("Darius", "Elle s'ouvre. Je sais me défendre, me protéger, déplacer les choses et ouvrir les portes. Le Non-lieu m'attend.")
	Settings.mark_tutorial_done()
	var btn := Button3D.new()
	btn.text = "RETOUR AU MENU"
	var yaw: float = rig.head_yaw()
	var f := Vector3(-sin(yaw), 0, -cos(yaw))
	btn.position = rig.cam.global_position + f * 1.8
	btn.position.y = 1.2
	btn.rotation.y = yaw
	add_child(btn)
	btn.pressed.connect(func(): finished.emit())
	rig.hint_controller("dom", "trigger")
	_say("", "Tutoriel terminé. Bravo !")

func _holding(kind: String) -> bool:
	for h in rig.hands:
		var it = rig.inventory.held_item(h)
		if it != null and it.kind == kind:
			return true
	return false

# ---------- Armes, mannequin, cabane ----------
func _spawn_weapons() -> void:
	var table := Node3D.new()
	table.position = Vector3(-3.2, 0, -13.0)
	add_child(table)
	World.box(table, Vector3(0, 0.0, 0), Vector3(1.3, 0.78, 0.7), Color(0.34, 0.23, 0.14), 0.0, true)
	World.box(table, Vector3(0, 0.78, 0), Vector3(1.4, 0.05, 0.8), Color(0.45, 0.31, 0.19))
	var k := Items.knife()
	k.position = Vector3(-3.55, 0.9, -13.0)
	k.rotation_degrees.y = 20
	add_child(k)
	var b := Items.bat()
	b.position = Vector3(-2.7, 0.9, -12.8)
	b.rotation_degrees.y = 90
	add_child(b)
	# mannequin d'entraînement (poteau, sac, tête, bras)
	var d := Node3D.new()
	d.position = Vector3(2.8, 0, -13.5)
	add_child(d)
	dummy = d
	World.box(d, Vector3(0, 0, 0), Vector3(0.12, 1.9, 0.12), Color(0.35, 0.24, 0.15), 0.0, true)
	World.box(d, Vector3(0, 1.25, 0), Vector3(0.5, 0.55, 0.3), Color(0.55, 0.45, 0.3))
	World.box(d, Vector3(0, 1.45, 0), Vector3(1.0, 0.1, 0.1), Color(0.35, 0.24, 0.15))
	var head := MeshInstance3D.new()
	var sm := SphereMesh.new()
	sm.radius = 0.15
	sm.height = 0.3
	head.mesh = sm
	head.position = Vector3(0, 1.85, 0)
	head.material_override = World.mat(Color(0.6, 0.5, 0.35))
	d.add_child(head)
	d.add_to_group("hittable")
	d.set_meta("center", Vector3(0, 1.3, 0))
	d.set_meta("radius", 0.6)
	d.set_meta("on_hit", Callable(self, "_dummy_hit"))

func _dummy_hit(dir: Vector3, power: float) -> void:
	dummy_hits += 1
	Sfx.play(self, "thud", dummy.global_position, -2.0)
	var tw := create_tween()
	tw.tween_property(dummy, "rotation:z", clampf(-dir.x * 0.25, -0.3, 0.3), 0.06)
	tw.tween_property(dummy, "rotation:z", 0.0, 0.35).set_trans(Tween.TRANS_ELASTIC)

func _spawn_hut() -> void:
	Props.stump(self, Vector3(-2.6, 0, -33.0))
	var k := Items.key()
	k.position = Vector3(-2.6, 0.82, -33.0)
	k.rotation_degrees.y = 35
	add_child(k)
	Props.hut(self, Vector3(0, 0, -38.0))
	door = DoorScript.new()
	door.position = Vector3(-0.5, 0, -38.0)
	add_child(door)
	door.setup(rig, rig.inventory)
	door.opened.connect(func(): door_open = true)
	Sfx.play(self, "pickup", null, -10.0)

func _facing_stone() -> bool:
	var to: Vector3 = Vector3(7.0, 0, -9.5) - rig.cam.global_position
	var want := atan2(-to.x, -to.z)
	return absf(angle_difference(want, rig.head_yaw())) < deg_to_rad(20.0)

func _on_grab(hand: XRController3D) -> void:
	if page and is_instance_valid(page) and held_by == null and hand.global_position.distance_to(page.global_position) < 0.4:
		held_by = hand
		Sfx.play(self, "page", null, -4.0)

func _on_release(hand: XRController3D) -> void:
	pass

func _physics_process(delta: float) -> void:
	if held_by and page and is_instance_valid(page):
		page.global_transform = Transform3D(held_by.global_basis, held_by.global_position + held_by.global_basis * Vector3(0, 0.06, -0.12))
	if silhouette and silhouette.visible and rig:
		_update_silhouette(delta)

# ---------- Caisses, tonneaux et cible ----------
func _spawn_crates() -> void:
	target_hit = false
	target_area = Area3D.new()
	target_area.collision_layer = 0
	target_area.collision_mask = 4
	target_area.position = Vector3(0, 1.7, -23.0)
	var cs := CollisionShape3D.new()
	var sph := SphereShape3D.new()
	sph.radius = 1.3
	cs.shape = sph
	target_area.add_child(cs)
	var ring := MeshInstance3D.new()
	var tm := TorusMesh.new()
	tm.inner_radius = 1.15
	tm.outer_radius = 1.3
	ring.mesh = tm
	ring.rotation.x = PI / 2.0
	ring.material_override = World.mat(Color(0.3, 0.7, 1.0), 3.5)
	target_area.add_child(ring)
	add_child(target_area)
	target_area.body_entered.connect(func(b): if b is RigidBody3D and b.is_in_group("grabbable"): target_hit = true)
	World.light(self, Vector3(0, 1.7, -22.0), Color(0.3, 0.65, 1.0), 1.5, 7.0)
	for i in 5:
		var rb: RigidBody3D = Props.barrel() if i % 2 == 1 else Props.crate()
		rb.position = Vector3(-3.0 + i * 1.5, 0.4, -14.5 - (i % 2) * 0.9)
		rb.rotation.y = randf() * TAU
		add_child(rb)
		crates.append(rb)

func _clear_crates() -> void:
	for rb in crates:
		if is_instance_valid(rb):
			rb.queue_free()
	crates.clear()
	if target_area:
		target_area.queue_free()

# ---------- Silhouette ----------
func _build_silhouette() -> void:
	silhouette = Node3D.new()
	add_child(silhouette)
	var body := MeshInstance3D.new()
	var cap := CapsuleMesh.new()
	cap.radius = 0.26
	cap.height = 1.8
	body.mesh = cap
	body.material_override = World.mat(Color(0.01, 0.01, 0.02))
	body.position.y = 0.95
	silhouette.add_child(body)
	var cloak := MeshInstance3D.new()
	var cm := CylinderMesh.new()
	cm.top_radius = 0.28
	cm.bottom_radius = 0.6
	cm.height = 1.2
	cm.radial_segments = 8
	cloak.mesh = cm
	cloak.material_override = World.mat(Color(0.015, 0.015, 0.03))
	cloak.position.y = 0.6
	silhouette.add_child(cloak)
	for ex in [-0.09, 0.09]:
		World.box(silhouette, Vector3(ex, 1.55, -0.24), Vector3(0.07, 0.03, 0.02), Color(0.7, 0.9, 1.0), 5.0)
	silhouette.add_to_group("hittable")
	silhouette.set_meta("center", Vector3(0, 1.0, 0))
	silhouette.set_meta("radius", 0.6)
	silhouette.set_meta("on_hit", Callable(self, "_silhouette_hit"))
	Sfx.play(self, "whisper", null, -6.0)
	var cam_pos: Vector3 = rig.cam.global_position
	silhouette.global_position = Vector3(cam_pos.x + 4.0, 0, cam_pos.z - 13.0)

func _silhouette_hit(dir: Vector3, power: float) -> void:
	hits_taken += 1
	stun_until = Time.get_ticks_msec() / 1000.0 + 1.0
	silhouette.global_position += Vector3(dir.x, 0, dir.z).normalized() * 1.6
	Sfx.play(self, "hurt", silhouette.global_position, -4.0)
	if hits_taken >= 3:
		survive_left = 0.0

func _update_silhouette(delta: float) -> void:
	if Time.get_ticks_msec() / 1000.0 < stun_until:
		survive_left -= delta
		return
	var target: Vector3 = rig.cam.global_position
	target.y = 0.0
	var pos: Vector3 = silhouette.global_position
	var dir: Vector3 = target - pos
	var dist: float = dir.length()
	if dist > 0.1:
		silhouette.look_at(Vector3(target.x, pos.y, target.z), Vector3.UP)
		silhouette.rotate_y(PI)
		silhouette.global_position += dir.normalized() * 1.2 * Settings.enemy_speed() * delta
	if dist < 1.0:
		if rig.is_protected():
			silhouette.global_position -= dir.normalized() * 3.5 * delta
		else:
			hits += 1
			_hint("Elle t'a pris un souvenir (%d). Recule, utilise %s !" % [hits, rig.power_button_name()])
			var c: Vector3 = rig.cam.global_position
			silhouette.global_position = Vector3(c.x + 4.0, 0, c.z - 13.0)
			Sfx.play(self, "hurt", null, -2.0)
			rig._haptic(rig.right(), 1.0)
			rig._haptic(rig.left(), 1.0)
	survive_left -= delta

func _exit_tree() -> void:
	_alive = false
