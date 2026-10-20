extends XROrigin3D
# Le joueur en VR : tête, deux manettes avec laser, déplacement confortable (téléportation ou fluide),
# rotation par crans ou fluide, vignette de confort.
# Manettes : stick gauche = bouger, stick droit = tourner, gâchette = valider, grip = attraper,
# A (main droite) = pouvoir « Retenir ».

signal power_used
signal telekinesis_grab(body: RigidBody3D)
signal telekinesis_launch(body: RigidBody3D)
signal telekinesis_pulled(body: RigidBody3D)
signal grabbed(controller: XRController3D)
signal released(controller: XRController3D)

const Hands := preload("res://scripts/hands.gd")
var cam: XRCamera3D
var visuals: Dictionary = {}     # XRController3D -> { hand, ctrl, tag, part }
var power_ui: Node3D
var power_text: Label3D
var power_bar: MeshInstance3D
var _was_ready := true
var hands: Array[XRController3D] = []
var lasers: Dictionary = {}     # XRController3D -> RayCast3D
var beams: Dictionary = {}      # XRController3D -> MeshInstance3D
var hover: Dictionary = {}      # XRController3D -> Button3D survolé
var movement_enabled := false
var telekinesis_enabled := true
var held: Dictionary = {}       # XRController3D -> RigidBody3D tenu à distance
var hold_dist: Dictionary = {}
var in_hand: Dictionary = {}    # XRController3D -> true quand l'objet a été ramené dans la main
var hand_prev: Dictionary = {}
var hand_vel: Dictionary = {}
var ui_enabled := true
var power_cooldown := 0.0
var protected_until := 0.0
var _snap_ready := true
var _tele_marker: MeshInstance3D
var _tele_target := Vector3.ZERO
var _tele_valid := false
var _vignette: MeshInstance3D
var _vignette_mat: ShaderMaterial
var _moving_amount := 0.0

func _ready() -> void:
	cam = XRCamera3D.new()
	add_child(cam)
	for side in ["left_hand", "right_hand"]:
		var hand := XRController3D.new()
		hand.tracker = side
		hand.name = side
		add_child(hand)
		hands.append(hand)
		_build_hand(hand)
		hand.button_pressed.connect(_on_button.bind(hand))
		hand.button_released.connect(_on_release.bind(hand))
	_build_marker()
	_build_power_ui()
	_build_vignette()
	position.y = 0.4 if Settings.seated else 0.0

func left() -> XRController3D:
	return hands[0]

func right() -> XRController3D:
	return hands[1]

func _build_hand(hand: XRController3D) -> void:
	var side := "left" if hand.tracker == &"left_hand" else "right"
	var visual := Hands.hand(side)
	hand.add_child(visual)
	var ctrl := Hands.controller(side)
	ctrl.visible = false
	hand.add_child(ctrl)
	var tag := Label3D.new()
	tag.font_size = 40
	tag.pixel_size = 0.0012
	tag.modulate = Color(1.0, 0.85, 0.3)
	tag.outline_size = 8
	tag.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	tag.no_depth_test = true
	tag.position = Vector3(0, 0.12, -0.02)
	tag.visible = false
	hand.add_child(tag)
	visuals[hand] = {"hand": visual, "ctrl": ctrl, "tag": tag, "part": ""}
	var ray := RayCast3D.new()
	ray.target_position = Vector3(0, 0, -8)
	ray.collide_with_areas = true
	ray.collide_with_bodies = true
	ray.collision_mask = 7
	hand.add_child(ray)
	lasers[hand] = ray
	var beam := MeshInstance3D.new()
	var bm := BoxMesh.new()
	bm.size = Vector3(0.004, 0.004, 1.0)
	beam.mesh = bm
	var bmat := StandardMaterial3D.new()
	bmat.albedo_color = Color(0.4, 0.75, 1.0, 0.6)
	bmat.emission_enabled = true
	bmat.emission = Color(0.4, 0.75, 1.0)
	bmat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	bmat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	beam.material_override = bmat
	hand.add_child(beam)
	beams[hand] = beam

func _build_marker() -> void:
	_tele_marker = MeshInstance3D.new()
	var cm := CylinderMesh.new()
	cm.top_radius = 0.35
	cm.bottom_radius = 0.35
	cm.height = 0.02
	_tele_marker.mesh = cm
	var m := StandardMaterial3D.new()
	m.albedo_color = Color(0.3, 0.7, 1.0, 0.5)
	m.emission_enabled = true
	m.emission = Color(0.3, 0.7, 1.0)
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	_tele_marker.material_override = m
	_tele_marker.visible = false
	_tele_marker.top_level = true
	add_child(_tele_marker)

func _build_vignette() -> void:
	# Anneau sombre devant la caméra, visible seulement pendant les déplacements fluides.
	_vignette = MeshInstance3D.new()
	var qm := QuadMesh.new()
	qm.size = Vector2(2.0, 2.0)
	_vignette.mesh = qm
	var shader := Shader.new()
	shader.code = """
shader_type spatial;
render_mode unshaded, cull_disabled, depth_test_disabled;
uniform float amount : hint_range(0.0, 1.0) = 0.0;
void fragment() {
	float d = distance(UV, vec2(0.5));
	float v = smoothstep(0.55 - amount * 0.3, 0.75, d * 1.4);
	ALBEDO = vec3(0.0);
	ALPHA = v * amount;
}
"""
	_vignette_mat = ShaderMaterial.new()
	_vignette_mat.shader = shader
	_vignette.material_override = _vignette_mat
	_vignette.position = Vector3(0, 0, -0.3)
	_vignette.visible = false
	cam.add_child(_vignette)

func head_yaw() -> float:
	return cam.global_rotation.y

func _on_button(name: String, hand: XRController3D) -> void:
	match name:
		"trigger_click":
			if held.has(hand):
				_pull_to_hand(hand)
				return
			var target = hover.get(hand)
			if ui_enabled and target and is_instance_valid(target):
				target.press()
		"grip_click":
			if telekinesis_enabled and _try_telekinesis(hand):
				return
			grabbed.emit(hand)
		"ax_button":
			if hand == right():
				use_power()

func _on_release(name: String, hand: XRController3D) -> void:
	if name == "grip_click":
		if held.has(hand):
			_drop(hand, false)
		released.emit(hand)

# ---- Télékinésie : GRIP maintenu vers un objet = il est retenu de loin, à sa distance.
# ---- GÂCHETTE = il vient dans la main. Geste de la main + relâcher GRIP = lancer.
func _try_telekinesis(hand: XRController3D) -> bool:
	var ray: RayCast3D = lasers[hand]
	if not ray.is_colliding():
		return false
	var body = ray.get_collider()
	if not (body is RigidBody3D) or not body.is_in_group("grabbable"):
		return false
	for other in held:
		if held[other] == body:
			_drop(other, false)
			break
	held[hand] = body
	hold_dist[hand] = clampf(ray.global_position.distance_to(body.global_position), 0.6, 12.0)
	body.gravity_scale = 0.0
	body.linear_damp = 4.0
	body.angular_damp = 3.0
	body.sleeping = false
	_haptic(hand, 0.7)
	telekinesis_grab.emit(body)
	return true

func _drop(hand: XRController3D, _unused: bool) -> void:
	var body: RigidBody3D = held.get(hand)
	held.erase(hand)
	hold_dist.erase(hand)
	in_hand.erase(hand)
	if body == null or not is_instance_valid(body):
		return
	body.gravity_scale = 1.0
	body.linear_damp = 0.1
	body.angular_damp = 0.5
	# Lancer : on lâche GRIP en faisant un mouvement de la main, l'objet part avec sa vitesse.
	var v: Vector3 = (hand_vel.get(hand, Vector3.ZERO) as Vector3) * 2.0
	body.linear_velocity = v
	if v.length() > 2.0:
		body.angular_velocity = Vector3(randf_range(-4, 4), randf_range(-4, 4), randf_range(-4, 4))
		_haptic(hand, 0.8)
		telekinesis_launch.emit(body)

# GÂCHETTE pendant qu'on retient un objet à distance : il vient se coller dans la main.
func _pull_to_hand(hand: XRController3D) -> void:
	if in_hand.has(hand):
		return
	in_hand[hand] = true
	_haptic(hand, 0.5)
	telekinesis_pulled.emit(held[hand])

func _update_telekinesis(delta: float) -> void:
	for hand in hands:
		var pos := hand.global_position
		if hand_prev.has(hand):
			var v: Vector3 = (pos - hand_prev[hand]) / maxf(delta, 0.001)
			hand_vel[hand] = (hand_vel.get(hand, Vector3.ZERO) as Vector3).lerp(v, 0.35)
		hand_prev[hand] = pos
		if not held.has(hand):
			continue
		var body: RigidBody3D = held[hand]
		if not is_instance_valid(body):
			held.erase(hand)
			continue
		# Retenu de loin : l'objet garde sa distance. Après GÂCHETTE : il est dans la main.
		var dist: float = 0.14 if in_hand.has(hand) else float(hold_dist[hand])
		var target := pos + (-hand.global_basis.z) * dist
		var gain := 22.0 if in_hand.has(hand) else 12.0
		body.linear_velocity = ((target - body.global_position) * gain).limit_length(30.0)
		body.angular_velocity = body.angular_velocity.lerp(Vector3.ZERO, 0.1)
		(beams[hand].material_override as StandardMaterial3D).emission = Color(1.0, 0.45, 0.9)

# ---- Aide visuelle : la main est remplacée par la manette, bouton en surbrillance ----
# side : "left", "right", "both" ou "" (pour tout effacer). part : trigger, grip, stick, a, b.
func hint_controller(side: String, part: String) -> void:
	for h in hands:
		var v: Dictionary = visuals[h]
		var mine: bool = side == "both" or (side == "left" and h == left()) or (side == "right" and h == right())
		v["part"] = part if mine else ""
		(v["hand"] as Node3D).visible = not mine
		(v["ctrl"] as Node3D).visible = mine
		(v["tag"] as Label3D).visible = mine
		if mine:
			var names: Dictionary = (v["ctrl"] as Node3D).get_meta("names")
			(v["tag"] as Label3D).text = String(names.get(part, part))

func _update_hints() -> void:
	var t := Time.get_ticks_msec() / 1000.0
	for h in hands:
		var v: Dictionary = visuals[h]
		if v["part"] != "":
			Hands.set_highlight(v["ctrl"], v["part"], t)

# ---- Affichage du pouvoir au poignet gauche : protégé / recharge / prêt ----
func _build_power_ui() -> void:
	power_ui = Node3D.new()
	power_ui.position = Vector3(0, 0.07, 0.1)
	power_ui.rotation_degrees = Vector3(-70, 0, 0)
	left().add_child(power_ui)
	var back := MeshInstance3D.new()
	var qm := QuadMesh.new()
	qm.size = Vector2(0.2, 0.09)
	back.mesh = qm
	var m := StandardMaterial3D.new()
	m.albedo_color = Color(0.02, 0.03, 0.07, 0.8)
	m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	back.material_override = m
	power_ui.add_child(back)
	power_text = Label3D.new()
	power_text.font_size = 36
	power_text.pixel_size = 0.0007
	power_text.position = Vector3(0, 0.02, 0.002)
	power_text.outline_size = 6
	power_ui.add_child(power_text)
	power_bar = MeshInstance3D.new()
	var bm := BoxMesh.new()
	bm.size = Vector3(0.18, 0.015, 0.004)
	power_bar.mesh = bm
	power_bar.position = Vector3(0, -0.025, 0.003)
	var bmat := StandardMaterial3D.new()
	bmat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	power_bar.material_override = bmat
	power_ui.add_child(power_bar)

func power_status() -> Dictionary:
	var now := Time.get_ticks_msec() / 1000.0
	var prot := maxf(0.0, protected_until - now)
	if prot > 0.0:
		return {"state": "protege", "left": prot, "ratio": prot / 5.0}
	if power_cooldown > 0.0:
		return {"state": "recharge", "left": power_cooldown, "ratio": 1.0 - power_cooldown / 7.0}
	return {"state": "pret", "left": 0.0, "ratio": 1.0}

func power_label() -> String:
	var st := power_status()
	match st["state"]:
		"protege":
			return "RETENIR : PROTEGE  %.1f s" % st["left"]
		"recharge":
			return "RETENIR : RECHARGE  %.1f s" % st["left"]
	return "RETENIR : PRET  (A)"

func _update_power_ui() -> void:
	var st := power_status()
	var color: Color
	match st["state"]:
		"protege":
			color = Color(0.4, 0.75, 1.0)
		"recharge":
			color = Color(1.0, 0.6, 0.25)
		_:
			color = Color(0.4, 1.0, 0.55)
	power_text.text = power_label()
	power_text.modulate = color
	(power_bar.material_override as StandardMaterial3D).albedo_color = color
	var ratio := clampf(st["ratio"], 0.02, 1.0)
	power_bar.scale.x = ratio
	power_bar.position.x = -0.09 * (1.0 - ratio)
	var is_ready: bool = st["state"] == "pret"
	if is_ready and not _was_ready:
		_haptic(right(), 0.8)
		_haptic(left(), 0.8)
	_was_ready = is_ready

func use_power() -> void:
	if power_cooldown > 0.0:
		return
	power_cooldown = 12.0
	protected_until = Time.get_ticks_msec() / 1000.0 + 5.0
	power_used.emit()
	_haptic(right(), 0.6)

func is_protected() -> bool:
	return Time.get_ticks_msec() / 1000.0 < protected_until

func _haptic(hand: XRController3D, strength: float) -> void:
	hand.trigger_haptic_pulse("haptic", 0.0, strength, 0.15, 0.0)

func _physics_process(delta: float) -> void:
	power_cooldown = maxf(0.0, power_cooldown - delta)
	_update_lasers()
	_update_telekinesis(delta)
	_update_hints()
	_update_power_ui()
	for hand in hands:
		if not held.has(hand):
			(beams[hand].material_override as StandardMaterial3D).emission = Color(0.4, 0.75, 1.0)
	if movement_enabled:
		_locomotion(delta)
	else:
		_tele_marker.visible = false
	_vignette_mat.set_shader_parameter("amount", _moving_amount if Settings.vignette else 0.0)
	_vignette.visible = Settings.vignette and _moving_amount > 0.01
	_moving_amount = move_toward(_moving_amount, 0.0, delta * 2.0)

func _update_lasers() -> void:
	for hand in hands:
		var ray: RayCast3D = lasers[hand]
		var beam: MeshInstance3D = beams[hand]
		var length := 3.0
		var target = null
		if ray.is_colliding():
			length = ray.global_position.distance_to(ray.get_collision_point())
			target = ray.get_collider()
		var button = target if (target and target.has_method("press")) else null
		var old = hover.get(hand)
		if old != button:
			if old and is_instance_valid(old):
				old.set_hover(false)
			if button:
				button.set_hover(true)
				_haptic(hand, 0.25)
			hover[hand] = button
		beam.visible = true
		beam.scale = Vector3(1, 1, length)
		beam.position = Vector3(0, 0, -length / 2.0)

func _locomotion(delta: float) -> void:
	# Rotation (stick droit)
	var r := right().get_vector2("primary") if not held.has(right()) else Vector2.ZERO
	if Settings.turn_mode == "snap":
		if absf(r.x) > 0.7 and _snap_ready:
			_rotate_around_head(-signf(r.x) * deg_to_rad(Settings.snap_degrees))
			_snap_ready = false
		elif absf(r.x) < 0.3:
			_snap_ready = true
	elif absf(r.x) > 0.15:
		_rotate_around_head(-r.x * deg_to_rad(90.0) * delta)
		_moving_amount = maxf(_moving_amount, 0.4)
	# Déplacement (stick gauche)
	var l := left().get_vector2("primary") if not held.has(left()) else Vector2.ZERO
	if Settings.move_mode == "smooth":
		_tele_marker.visible = false
		if l.length() > 0.2:
			var basis_yaw := Basis(Vector3.UP, head_yaw())
			var dir := basis_yaw * Vector3(l.x, 0, -l.y)
			position += dir * 2.0 * delta
			_moving_amount = maxf(_moving_amount, 0.8)
	else:
		_teleport_aim(l)

func _teleport_aim(l: Vector2) -> void:
	var ray: RayCast3D = lasers[left()]
	if l.y > 0.6:
		if ray.is_colliding() and ray.get_collider() is StaticBody3D:
			var n := ray.get_collision_normal()
			_tele_valid = n.y > 0.7
			_tele_target = ray.get_collision_point()
		else:
			_tele_valid = false
		_tele_marker.visible = _tele_valid
		if _tele_valid:
			_tele_marker.global_position = _tele_target + Vector3(0, 0.02, 0)
	else:
		if _tele_marker.visible and _tele_valid:
			var offset := global_position - cam.global_position
			global_position = Vector3(_tele_target.x + offset.x, global_position.y, _tele_target.z + offset.z)
			_moving_amount = 0.0
		_tele_marker.visible = false

func _rotate_around_head(angle: float) -> void:
	var head := cam.global_position
	var t := Transform3D(Basis(Vector3.UP, angle), Vector3.ZERO)
	var pivot := Transform3D(Basis.IDENTITY, head)
	global_transform = pivot * t * pivot.affine_inverse() * global_transform

func recenter_to(spot: Vector3, yaw: float) -> void:
	# Place la tête du joueur sur `spot`, regardant dans la direction `yaw`.
	rotation = Vector3(0, yaw - (cam.rotation.y if cam.is_inside_tree() else 0.0), 0)
	var offset := global_position - cam.global_position
	global_position = Vector3(spot.x + offset.x, spot.y + (0.4 if Settings.seated else 0.0), spot.z + offset.z)
