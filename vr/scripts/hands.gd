extends RefCounted
# Mains « fantômes » et manette Meta Quest 3 (Touch Plus) procédurales.
# Pendant le tutoriel, la main est remplacée par la manette, avec le bon bouton en surbrillance.

const World := preload("res://scripts/world.gd")

static func _box(parent: Node, pos: Vector3, size: Vector3, mat: Material) -> MeshInstance3D:
	var mi := MeshInstance3D.new()
	var bm := BoxMesh.new()
	bm.size = size
	mi.mesh = bm
	mi.position = pos
	mi.material_override = mat
	parent.add_child(mi)
	return mi

static func hand(side: String) -> Node3D:
	var root := Node3D.new()
	var skin := World.mat(Color(0.7, 0.8, 0.95), 0.5, 0.6)
	var s := 1.0 if side == "right" else -1.0
	_box(root, Vector3(0, 0, 0.02), Vector3(0.085, 0.03, 0.095), skin)
	var lens := [0.07, 0.082, 0.078, 0.062]
	for i in 4:
		var x := -0.03 + i * 0.02
		var l: float = lens[i]
		var f1 := _box(root, Vector3(x, -0.004, -0.03 - l / 2.0), Vector3(0.017, 0.02, l), skin)
		f1.rotation_degrees.x = -12
	var th := _box(root, Vector3(-0.058 * s, -0.004, 0.0), Vector3(0.02, 0.02, 0.065), skin)
	th.rotation_degrees.y = -30.0 * s
	root.rotation_degrees.x = -10
	return root

# Renvoie un Node3D dont meta "parts" = { nom : MeshInstance3D } (trigger, grip, stick, a, b, menu).
static func controller(side: String) -> Node3D:
	var root := Node3D.new()
	var body_mat := World.mat(Color(0.1, 0.1, 0.12), 0.0, 0.5)
	var plate_mat := World.mat(Color(0.16, 0.16, 0.19), 0.0, 0.4)
	var s := 1.0 if side == "right" else -1.0
	var parts := {}
	# poignée inclinée
	var handle := MeshInstance3D.new()
	var cm := CylinderMesh.new()
	cm.top_radius = 0.027
	cm.bottom_radius = 0.03
	cm.height = 0.13
	cm.radial_segments = 12
	handle.mesh = cm
	handle.material_override = body_mat
	handle.position = Vector3(0, -0.045, 0.03)
	handle.rotation_degrees.x = 20
	root.add_child(handle)
	# plaque supérieure (stick + boutons)
	var plate := _box(root, Vector3(0, 0.02, -0.02), Vector3(0.062, 0.02, 0.085), plate_mat)
	plate.rotation_degrees.x = -12
	var stick := MeshInstance3D.new()
	var sm := CylinderMesh.new()
	sm.top_radius = 0.011
	sm.bottom_radius = 0.009
	sm.height = 0.014
	stick.mesh = sm
	stick.material_override = World.mat(Color(0.3, 0.3, 0.34), 0.0, 0.4)
	stick.position = Vector3(-0.012 * s, 0.038, -0.03)
	root.add_child(stick)
	parts["stick"] = stick
	for i in 2:
		var b := MeshInstance3D.new()
		var bc := CylinderMesh.new()
		bc.top_radius = 0.0085
		bc.bottom_radius = 0.0085
		bc.height = 0.008
		b.mesh = bc
		b.material_override = World.mat(Color(0.3, 0.3, 0.34), 0.0, 0.4)
		b.position = Vector3(0.016 * s, 0.034, -0.05 + i * 0.03)
		root.add_child(b)
		parts["b" if i == 0 else "a"] = b   # droite : B devant, A derrière (X/Y à gauche)
	var trig := _box(root, Vector3(0, -0.004, -0.06), Vector3(0.016, 0.04, 0.018), World.mat(Color(0.2, 0.2, 0.24), 0.0, 0.4))
	trig.rotation_degrees.x = 20
	parts["trigger"] = trig
	var grip := _box(root, Vector3(-0.031 * s, -0.04, 0.03), Vector3(0.008, 0.07, 0.04), World.mat(Color(0.2, 0.2, 0.24), 0.0, 0.4))
	grip.rotation_degrees.x = 20
	parts["grip"] = grip
	root.set_meta("parts", parts)
	root.set_meta("names", {"a": "X" if side == "left" else "A", "b": "Y" if side == "left" else "B", "stick": "STICK", "trigger": "GACHETTE", "grip": "GRIP"})
	return root

static func set_highlight(ctrl: Node3D, part: String, t: float) -> void:
	var parts: Dictionary = ctrl.get_meta("parts")
	for k in parts:
		var mi: MeshInstance3D = parts[k]
		var m := mi.material_override as StandardMaterial3D
		if k == part:
			m.emission_enabled = true
			m.emission = Color(1.0, 0.85, 0.3)
			m.emission_energy_multiplier = 2.0 + sin(t * 8.0) * 1.6
			m.albedo_color = Color(1.0, 0.85, 0.3)
		else:
			m.emission_enabled = false
			m.albedo_color = Color(0.3, 0.3, 0.34)
