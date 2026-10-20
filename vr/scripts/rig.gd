extends XROrigin3D
# Le joueur en VR : tête, deux manettes avec laser, déplacement confortable (téléportation ou fluide),
# rotation par crans ou fluide, vignette de confort.
# Manettes : stick gauche = bouger, stick droit = tourner, gâchette = valider, grip = attraper,
# A (main droite) = pouvoir « Retenir ».

signal power_used
signal grabbed(controller: XRController3D)
signal released(controller: XRController3D)

var cam: XRCamera3D
var hands: Array[XRController3D] = []
var lasers: Dictionary = {}     # XRController3D -> RayCast3D
var beams: Dictionary = {}      # XRController3D -> MeshInstance3D
var hover: Dictionary = {}      # XRController3D -> Button3D survolé
var movement_enabled := false
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
	_build_vignette()
	position.y = 0.4 if Settings.seated else 0.0

func left() -> XRController3D:
	return hands[0]

func right() -> XRController3D:
	return hands[1]

func _build_hand(hand: XRController3D) -> void:
	var body := MeshInstance3D.new()
	var sm := SphereMesh.new()
	sm.radius = 0.035
	sm.height = 0.07
	body.mesh = sm
	var m := StandardMaterial3D.new()
	m.albedo_color = Color(0.08, 0.1, 0.18)
	m.emission_enabled = true
	m.emission = Color(0.2, 0.5, 1.0)
	m.emission_energy_multiplier = 0.8
	body.material_override = m
	hand.add_child(body)
	var ray := RayCast3D.new()
	ray.target_position = Vector3(0, 0, -8)
	ray.collide_with_areas = true
	ray.collide_with_bodies = true
	ray.collision_mask = 3
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
			var target = hover.get(hand)
			if ui_enabled and target and is_instance_valid(target):
				target.press()
		"grip_click":
			grabbed.emit(hand)
		"ax_button":
			if hand == right():
				use_power()

func _on_release(name: String, hand: XRController3D) -> void:
	if name == "grip_click":
		released.emit(hand)

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
	var r := right().get_vector2("primary")
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
	var l := left().get_vector2("primary")
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
