extends Node3D
# Silhouette (ennemi de base) ou Kayden (boss). Poursuit le joueur ; se repousse à l'arme ; ignore un joueur protégé.

signal died(enemy: Node)
signal touched(enemy: Node)

const World := preload("res://scripts/world.gd")
const Sfx := preload("res://scripts/sfx.gd")

var rig
var kind := "silhouette"
var hp := 3
var max_hp := 3
var speed := 1.2
var alive := true
var stun_until := 0.0
var cool_until := 0.0

func setup(player_rig, k: String, at: Vector3, speed_mult := 1.0) -> void:
	rig = player_rig
	kind = k
	global_position = at
	var big := k == "kayden"
	hp = 14 if big else 3
	max_hp = hp
	speed = (0.9 if big else 1.2) * speed_mult
	var s := 1.7 if big else 1.0
	var tint := Color(0.02, 0.03, 0.12) if big else Color(0.01, 0.01, 0.02)
	var glow := Color(0.35, 0.6, 1.0) if big else Color(0.7, 0.9, 1.0)
	var body := MeshInstance3D.new()
	var cap := CapsuleMesh.new()
	cap.radius = 0.26
	cap.height = 1.8
	body.mesh = cap
	body.material_override = World.mat(tint)
	body.position.y = 0.95
	add_child(body)
	var cloak := MeshInstance3D.new()
	var cm := CylinderMesh.new()
	cm.top_radius = 0.28
	cm.bottom_radius = 0.6
	cm.height = 1.2
	cm.radial_segments = 8
	cloak.mesh = cm
	cloak.material_override = World.mat(tint * 1.3)
	cloak.position.y = 0.6
	add_child(cloak)
	for ex in [-0.09, 0.09]:
		World.box(self, Vector3(ex, 1.55, -0.24), Vector3(0.07, 0.03, 0.02), glow, 5.0)
	if big:
		World.light(self, Vector3(0, 1.6, 0), glow, 1.6, 9.0)
		# couronne de lignes verticales bleues
		for i in 8:
			var a := TAU * float(i) / 8.0
			World.box(self, Vector3(cos(a) * 0.6, 1.2, sin(a) * 0.6), Vector3(0.04, 2.2, 0.04), glow, 4.0)
	scale = Vector3.ONE * s
	add_to_group("hittable")
	set_meta("center", Vector3(0, 1.0 * s, 0))
	set_meta("radius", 0.7 * s)
	set_meta("on_hit", Callable(self, "_on_hit"))

func _on_hit(dir: Vector3, power: float) -> void:
	if not alive:
		return
	hp -= 1
	stun_until = Time.get_ticks_msec() / 1000.0 + (0.5 if kind == "kayden" else 1.0)
	var push := 0.6 if kind == "kayden" else 1.6
	global_position += Vector3(dir.x, 0, dir.z).normalized() * push
	Sfx.play(self, "hurt", global_position, -4.0)
	if hp <= 0:
		alive = false
		remove_from_group("hittable")
		var tw := create_tween()
		tw.tween_property(self, "scale", Vector3.ZERO, 0.6)
		tw.tween_callback(queue_free)
		emit_signal("died", self)

func _physics_process(delta: float) -> void:
	if not alive or rig == null:
		return
	var now := Time.get_ticks_msec() / 1000.0
	if now < stun_until:
		return
	var target: Vector3 = rig.cam.global_position
	target.y = 0.0
	var pos := global_position
	var dir: Vector3 = target - pos
	var dist := dir.length()
	if dist > 0.1:
		look_at(Vector3(target.x, pos.y, target.z), Vector3.UP)
		rotate_y(PI)
		global_position += dir.normalized() * speed * delta
	if dist < 1.0 * scale.x:
		if rig.is_protected():
			global_position -= dir.normalized() * 3.5 * delta
		elif now > cool_until:
			cool_until = now + 2.0
			emit_signal("touched", self)
			global_position -= dir.normalized() * 3.0

func vanish() -> void:
	alive = false
	remove_from_group("hittable")
	queue_free()
