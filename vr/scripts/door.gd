extends Node3D
# Porte verrouillée : on insère la clé dans la serrure, on la TOURNE (le poignet pivote d'environ 80°),
# puis on attrape la poignée (GRIP) et on tire pour ouvrir. La charnière est à l'origine de ce nœud.
# La porte fermée est le long de +X, elle s'ouvre vers +Z (vers le joueur).

signal unlocked
signal opened

const World := preload("res://scripts/world.gd")
const Sfx := preload("res://scripts/sfx.gd")

var rig
var inv
var leaf: Node3D
var keyhole: Node3D
var handle: Node3D
var state := "locked"       # locked | inserted | unlocked
var key_item = null
var key_hand: XRController3D = null
var ref_vec := Vector3.RIGHT
var roll := 0.0
var angle := 0.0            # <= 0 : ouverte vers +Z
var grab_hand: XRController3D = null
var was_open := false
var _creak_t := 0.0

func _ready() -> void:
	leaf = Node3D.new()
	add_child(leaf)
	var panel := MeshInstance3D.new()
	var bm := BoxMesh.new()
	bm.size = Vector3(1.0, 2.1, 0.07)
	panel.mesh = bm
	panel.position = Vector3(0.5, 1.05, 0)
	panel.material_override = World.mat(Color(0.32, 0.2, 0.12), 0.0, 0.8)
	leaf.add_child(panel)
	for y in [0.3, 1.0, 1.8]:
		var band := MeshInstance3D.new()
		var bb := BoxMesh.new()
		bb.size = Vector3(1.0, 0.08, 0.08)
		band.mesh = bb
		band.position = Vector3(0.5, y, 0.01)
		band.material_override = World.mat(Color(0.12, 0.1, 0.1), 0.0, 0.5)
		leaf.add_child(band)
	# plaque de serrure + trou
	keyhole = Node3D.new()
	keyhole.position = Vector3(0.82, 1.2, 0.04)
	leaf.add_child(keyhole)
	var plate := MeshInstance3D.new()
	var pb := BoxMesh.new()
	pb.size = Vector3(0.09, 0.14, 0.02)
	plate.mesh = pb
	plate.material_override = World.mat(Color(0.75, 0.6, 0.25), 0.4, 0.3)
	keyhole.add_child(plate)
	var hole := MeshInstance3D.new()
	var hb := BoxMesh.new()
	hb.size = Vector3(0.012, 0.03, 0.022)
	hole.mesh = hb
	hole.position.z = 0.002
	hole.material_override = World.mat(Color(0.0, 0.0, 0.0))
	keyhole.add_child(hole)
	# poignée
	handle = Node3D.new()
	handle.position = Vector3(0.82, 0.95, 0.09)
	leaf.add_child(handle)
	var bar := MeshInstance3D.new()
	var bb2 := BoxMesh.new()
	bb2.size = Vector3(0.03, 0.03, 0.14)
	bar.mesh = bb2
	bar.material_override = World.mat(Color(0.75, 0.6, 0.25), 0.2, 0.3)
	handle.add_child(bar)
	var knob := MeshInstance3D.new()
	var sm := SphereMesh.new()
	sm.radius = 0.035
	sm.height = 0.07
	knob.mesh = sm
	knob.position.z = 0.07
	knob.material_override = World.mat(Color(0.75, 0.6, 0.25), 0.2, 0.3)
	handle.add_child(knob)
	# collision pour ne pas traverser la porte fermée
	var body := StaticBody3D.new()
	body.collision_layer = 1
	var cs := CollisionShape3D.new()
	var bs := BoxShape3D.new()
	bs.size = Vector3(1.0, 2.1, 0.12)
	cs.shape = bs
	cs.position = Vector3(0.5, 1.05, 0)
	body.add_child(cs)
	leaf.add_child(body)

func setup(player_rig, inventory) -> void:
	rig = player_rig
	inv = inventory

func _physics_process(delta: float) -> void:
	if rig == null or inv == null:
		return
	match state:
		"locked":
			_try_insert()
		"inserted":
			_turn_key(delta)
		"unlocked":
			_pull_handle(delta)

func _try_insert() -> void:
	for hand in rig.hands:
		var it = inv.held_item(hand)
		if it != null and it.kind == "key":
			var tip: Vector3 = it.global_transform * it.tip
			if tip.distance_to(keyhole.global_position + Vector3(0, 0, 0.02)) < 0.08:
				state = "inserted"
				key_item = it
				key_hand = hand
				it.set_meta("locked_in", true)
				var x: Vector3 = hand.global_basis.x
				ref_vec = Vector3(x.x, x.y, 0.0).normalized()
				roll = 0.0
				Sfx.play(self, "key_in", keyhole.global_position, 0.0)
				rig._haptic(hand, 0.6)
				return

func _turn_key(delta: float) -> void:
	if key_item == null or not is_instance_valid(key_item) or not key_hand.is_button_pressed("grip_click"):
		# on lâche la clé avant d'avoir tourné : elle sort et tombe
		if key_item and is_instance_valid(key_item):
			key_item.remove_meta("locked_in")
			if inv.held.get(key_hand) == key_item:
				inv.held.erase(key_hand)
			key_item.attach_mode(false)
			key_item.state = "free"
		state = "locked"
		key_item = null
		return
	var x: Vector3 = key_hand.global_basis.x
	var cur := Vector3(x.x, x.y, 0.0).normalized()
	var new_roll := clampf(ref_vec.signed_angle_to(cur, Vector3(0, 0, 1)), -deg_to_rad(95.0), deg_to_rad(95.0))
	if absf(new_roll - roll) > 0.02:
		_creak_t -= delta
		if _creak_t <= 0.0:
			Sfx.play(self, "key_turn", keyhole.global_position, -6.0)
			rig._haptic(key_hand, 0.3)
			_creak_t = 0.25
	roll = new_roll
	var tip_local: Vector3 = key_item.tip
	var b := Basis(Vector3(0, 0, 1), roll)
	var pos: Vector3 = keyhole.global_position + Vector3(0, 0, 0.02)
	key_item.global_transform = Transform3D(b, pos - b * tip_local)
	if absf(roll) > deg_to_rad(80.0):
		state = "unlocked"
		Sfx.play(self, "unlock", keyhole.global_position, 0.0)
		rig._haptic(key_hand, 1.0)
		if inv.held.get(key_hand) == key_item:
			inv.held.erase(key_hand)
		key_item.state = "free"
		key_item.holder = null
		key_item.remove_meta("locked_in")
		key_item.attach_mode(true)           # la clé reste dans la serrure
		emit_signal("unlocked")

func _pull_handle(delta: float) -> void:
	if grab_hand == null:
		for hand in rig.hands:
			if hand.is_button_pressed("grip_click") and inv.held_item(hand) == null:
				if hand.global_position.distance_to(handle.global_position) < 0.18:
					grab_hand = hand
					rig._haptic(hand, 0.4)
					break
	else:
		if not grab_hand.is_button_pressed("grip_click"):
			grab_hand = null
			return
		var v: Vector3 = grab_hand.global_position - global_position
		var target := clampf(atan2(-v.z, v.x), -deg_to_rad(110.0), 0.0)
		if absf(target - angle) > 0.01:
			_creak_t -= delta
			if _creak_t <= 0.0:
				Sfx.play(self, "creak", global_position + Vector3(0.5, 1.0, 0), -4.0)
				rig._haptic(grab_hand, 0.25)
				_creak_t = 0.55
		angle = lerpf(angle, target, clampf(delta * 14.0, 0.0, 1.0))
		leaf.rotation.y = angle
		if angle < -1.2 and not was_open:
			was_open = true
			Sfx.play(self, "thud", global_position + Vector3(0.6, 1.0, 0.3), 0.0)
			rig._haptic(grab_hand, 0.8)
			emit_signal("opened")
