extends Node3D
# Rangements sur le corps : épaule droite et gauche (armes longues), poches aux hanches, torse (petits objets).
# GRIP près d'un rangement : on sort l'objet. Relâcher GRIP près d'un rangement libre : on le range, sinon il tombe.
# Un coup assez rapide avec une arme sur une cible « hittable » la touche.

signal weapon_hit(target: Node)
signal stowed(item: Node, slot_name: String)
signal drawn(item: Node, slot_name: String)

const Sfx := preload("res://scripts/sfx.gd")

const SLOTS := {
	"shoulder_r": {"off": Vector3(0.2, -0.24, 0.1), "accept": ["large", "small"], "tilt": 80.0},
	"shoulder_l": {"off": Vector3(-0.2, -0.24, 0.1), "accept": ["large", "small"], "tilt": 80.0},
	"hip_r": {"off": Vector3(0.24, -0.78, 0.02), "accept": ["small"], "tilt": -85.0},
	"hip_l": {"off": Vector3(-0.24, -0.78, 0.02), "accept": ["small"], "tilt": -85.0},
	"chest": {"off": Vector3(0.0, -0.4, -0.14), "accept": ["small"], "tilt": 60.0},
}
const TAKE_RADIUS := 0.24

var rig
var body_yaw := 0.0
var held: Dictionary = {}       # XRController3D -> Item
var stored: Dictionary = {}     # nom du rangement -> Item
var indicators: Dictionary = {}
var _tip_prev: Dictionary = {}
var _hit_cool: Dictionary = {}
var _hand_prev: Dictionary = {}
var _hand_vel: Dictionary = {}

func _ready() -> void:
	for name in SLOTS:
		var mi := MeshInstance3D.new()
		var sm := SphereMesh.new()
		sm.radius = 0.07
		sm.height = 0.14
		sm.radial_segments = 8
		sm.rings = 4
		mi.mesh = sm
		var m := StandardMaterial3D.new()
		m.albedo_color = Color(1.0, 0.85, 0.3, 0.35)
		m.emission_enabled = true
		m.emission = Color(1.0, 0.85, 0.3)
		m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
		m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
		mi.material_override = m
		mi.visible = false
		mi.top_level = true
		add_child(mi)
		indicators[name] = mi

func slot_pos(name: String) -> Vector3:
	var cam: XRCamera3D = rig.cam
	return cam.global_position + Basis(Vector3.UP, body_yaw) * (SLOTS[name]["off"] as Vector3)

func held_item(hand: XRController3D):
	return held.get(hand)

func _accepts(name: String, it) -> bool:
	return it.size_class in (SLOTS[name]["accept"] as Array)

func on_grip(hand: XRController3D) -> bool:
	if held.has(hand):
		return true
	# 1. objet rangé
	var best := ""
	var best_d := TAKE_RADIUS
	for name in stored:
		var d := hand.global_position.distance_to(slot_pos(name))
		if d < best_d:
			best_d = d
			best = name
	if best != "":
		var it = stored[best]
		stored.erase(best)
		_take(hand, it)
		emit_signal("drawn", it, best)
		return true
	# 2. objet posé
	var near = null
	best_d = 0.28
	for node in get_tree().get_nodes_in_group("item"):
		if node.state == "free":
			var d: float = hand.global_position.distance_to(node.global_position)
			if d < best_d:
				best_d = d
				near = node
	if near != null:
		_take(hand, near)
		return true
	return false

func _take(hand: XRController3D, it) -> void:
	it.attach_mode(true)
	it.state = "held"
	it.holder = hand
	it.slot = ""
	held[hand] = it
	_tip_prev.erase(hand)
	Sfx.play(self, "pickup", null, -6.0)
	rig._haptic(hand, 0.4)

func on_release(hand: XRController3D) -> bool:
	if not held.has(hand):
		return false
	var it = held[hand]
	if it.has_meta("locked_in"):
		return true     # la clé reste dans la serrure
	held.erase(hand)
	var best := ""
	var best_d := TAKE_RADIUS
	for name in SLOTS:
		if stored.has(name) or not _accepts(name, it):
			continue
		var d := hand.global_position.distance_to(slot_pos(name))
		if d < best_d:
			best_d = d
			best = name
	if best != "":
		stored[best] = it
		it.state = "stowed"
		it.slot = best
		it.holder = null
		Sfx.play(self, "click", null, -2.0)
		rig._haptic(hand, 0.5)
		emit_signal("stowed", it, best)
	else:
		it.attach_mode(false)
		it.state = "free"
		it.holder = null
		it.linear_velocity = (_hand_vel.get(hand, Vector3.ZERO) as Vector3) * 1.6
	return true

func has_in(slot_name: String) -> bool:
	return stored.has(slot_name)

func stored_kinds() -> Array:
	var out: Array = []
	for name in stored:
		out.append(stored[name].kind)
	return out

func _physics_process(delta: float) -> void:
	if rig == null or rig.cam == null:
		return
	for k in stored.keys():
		if not is_instance_valid(stored[k]):
			stored.erase(k)
	for h in held.keys():
		if not is_instance_valid(held[h]):
			held.erase(h)
	body_yaw = lerp_angle(body_yaw, rig.cam.global_rotation.y, clampf(delta * 4.0, 0.0, 1.0))
	for hand in rig.hands:
		var p: Vector3 = hand.global_position
		if _hand_prev.has(hand):
			_hand_vel[hand] = (_hand_vel.get(hand, Vector3.ZERO) as Vector3).lerp((p - _hand_prev[hand]) / maxf(delta, 0.001), 0.4)
		_hand_prev[hand] = p
	# objets rangés
	for name in stored:
		var it = stored[name]
		var tilt: float = SLOTS[name]["tilt"]
		var b := Basis(Vector3.UP, body_yaw) * Basis(Vector3.RIGHT, deg_to_rad(tilt))
		it.global_transform = Transform3D(b, slot_pos(name))
	# objets en main + coups
	var any_held := false
	for hand in held:
		var it = held[hand]
		any_held = true
		if not it.has_meta("locked_in"):
			it.global_transform = hand.global_transform * it.grip_offset
		_check_hits(hand, it, delta)
	# repères de rangement visibles quand on tient quelque chose
	var t := Time.get_ticks_msec() / 1000.0
	for name in SLOTS:
		var mi: MeshInstance3D = indicators[name]
		var visible_slot := false
		for hand in held:
			if not stored.has(name) and _accepts(name, held[hand]):
				visible_slot = true
		mi.visible = visible_slot
		if visible_slot:
			mi.global_position = slot_pos(name)
			mi.scale = Vector3.ONE * (1.0 + 0.12 * sin(t * 6.0))

func _check_hits(hand: XRController3D, it, delta: float) -> void:
	if it.damage <= 0.0:
		return
	var tip: Vector3 = it.global_transform * it.tip
	if _tip_prev.has(hand):
		var v: Vector3 = (tip - _tip_prev[hand]) / maxf(delta, 0.001)
		var speed := v.length()
		if speed > 2.2:
			for node in get_tree().get_nodes_in_group("hittable"):
				if not is_instance_valid(node) or not node.visible:
					continue
				var key := str(node.get_instance_id())
				if _hit_cool.get(key, 0.0) > Time.get_ticks_msec() / 1000.0:
					continue
				var center: Vector3 = node.global_position + (node.get_meta("center", Vector3(0, 1.0, 0)) as Vector3)
				var radius: float = node.get_meta("radius", 0.55)
				if tip.distance_to(center) < radius:
					_hit_cool[key] = Time.get_ticks_msec() / 1000.0 + 0.45
					var cb: Callable = node.get_meta("on_hit")
					cb.call(v.normalized(), speed * it.damage)
					Sfx.play(self, "hit", tip, 0.0)
					rig._haptic(hand, clampf(speed / 6.0, 0.3, 1.0))
					emit_signal("weapon_hit", node)
		elif speed > 1.2 and randf() < 0.06:
			Sfx.play(self, "whoosh", tip, -14.0)
	_tip_prev[hand] = tip
