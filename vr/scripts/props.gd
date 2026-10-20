extends RefCounted
# Décors et objets procéduraux (pas d'assets externes) : forêt, rochers, caisses, tonneaux, lanternes,
# souches, pierres levées. Les arbres sont instanciés en MultiMesh pour rester fluides sur Quest.

const World := preload("res://scripts/world.gd")

static func night_env(parent: Node, fog := Color(0.05, 0.08, 0.14), density := 0.035) -> void:
	var sky_mat := ProceduralSkyMaterial.new()
	sky_mat.sky_top_color = Color(0.02, 0.04, 0.12)
	sky_mat.sky_horizon_color = Color(0.08, 0.14, 0.26)
	sky_mat.ground_bottom_color = Color(0.02, 0.03, 0.06)
	sky_mat.ground_horizon_color = Color(0.06, 0.1, 0.18)
	var sky := Sky.new()
	sky.sky_material = sky_mat
	var env := Environment.new()
	env.background_mode = Environment.BG_SKY
	env.sky = sky
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.ambient_light_color = Color(0.22, 0.3, 0.5)
	env.ambient_light_energy = 0.9
	env.fog_enabled = true
	env.fog_light_color = fog
	env.fog_density = density
	env.glow_enabled = true
	env.glow_intensity = 0.8
	env.glow_bloom = 0.1
	var we := WorldEnvironment.new()
	we.environment = env
	parent.add_child(we)
	var moon := DirectionalLight3D.new()
	moon.light_color = Color(0.55, 0.7, 1.0)
	moon.light_energy = 0.55
	moon.rotation_degrees = Vector3(-50, 30, 0)
	moon.shadow_enabled = false
	parent.add_child(moon)

static func ground(parent: Node, size := 220.0) -> StaticBody3D:
	var body := StaticBody3D.new()
	body.name = "Floor"
	body.collision_layer = 1
	var cs := CollisionShape3D.new()
	var bs := BoxShape3D.new()
	bs.size = Vector3(size, 0.4, size)
	cs.shape = bs
	cs.position.y = -0.2
	body.add_child(cs)
	var mesh := MeshInstance3D.new()
	var pm := PlaneMesh.new()
	pm.size = Vector2(size, size)
	mesh.mesh = pm
	mesh.material_override = World.mat(Color(0.06, 0.12, 0.09), 0.0, 1.0)
	body.add_child(mesh)
	parent.add_child(body)
	return body

# Chemin de terre : bande claire le long de -Z.
static func path(parent: Node, from_z: float, to_z: float, width := 3.0) -> void:
	var mesh := MeshInstance3D.new()
	var pm := PlaneMesh.new()
	pm.size = Vector2(width, absf(to_z - from_z))
	mesh.mesh = pm
	mesh.material_override = World.mat(Color(0.22, 0.17, 0.12), 0.0, 1.0)
	mesh.position = Vector3(0, 0.01, (from_z + to_z) / 2.0)
	parent.add_child(mesh)

static func _multi(parent: Node, mesh: Mesh, mat: Material, items: Array) -> void:
	var mm := MultiMesh.new()
	mm.transform_format = MultiMesh.TRANSFORM_3D
	mm.use_colors = true
	mm.mesh = mesh
	mm.instance_count = items.size()
	for i in items.size():
		mm.set_instance_transform(i, items[i][0])
		mm.set_instance_color(i, items[i][1])
	var inst := MultiMeshInstance3D.new()
	inst.multimesh = mm
	inst.material_override = mat
	parent.add_child(inst)

# Forêt dense. `clear` : liste de Rect2 (x, z) où l'on ne plante rien (chemin, clairières).
static func forest(parent: Node, seed_value: int, count: int, area: Rect2, clear: Array) -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = seed_value
	var trunks: Array = []
	var cones: Array = [[], [], []]
	var placed := 0
	var tries := 0
	while placed < count and tries < count * 6:
		tries += 1
		var p := Vector2(rng.randf_range(area.position.x, area.end.x), rng.randf_range(area.position.y, area.end.y))
		var blocked := false
		for r in clear:
			if (r as Rect2).has_point(p):
				blocked = true
				break
		if blocked:
			continue
		placed += 1
		var s := rng.randf_range(0.8, 1.7)
		var yaw := rng.randf() * TAU
		var tone := rng.randf_range(0.75, 1.15)
		var base := Transform3D(Basis(Vector3.UP, yaw).scaled(Vector3(s, s, s)), Vector3(p.x, 0, p.y))
		trunks.append([base.translated_local(Vector3(0, 3.0, 0)), Color(0.28, 0.2, 0.14) * tone])
		for layer in 3:
			var y := 4.2 + layer * 1.9
			cones[layer].append([base.translated_local(Vector3(0, y, 0)), Color(0.07, 0.2, 0.12) * tone])
	var tm := CylinderMesh.new()
	tm.top_radius = 0.16
	tm.bottom_radius = 0.32
	tm.height = 6.0
	tm.radial_segments = 6
	var bark := World.mat(Color.WHITE, 0.0, 1.0)
	bark.vertex_color_use_as_albedo = true
	_multi(parent, tm, bark, trunks)
	var radii := [2.4, 1.9, 1.3]
	for layer in 3:
		var cm := CylinderMesh.new()
		cm.top_radius = 0.0
		cm.bottom_radius = radii[layer]
		cm.height = 2.6
		cm.radial_segments = 7
		var leaf := World.mat(Color.WHITE, 0.0, 1.0)
		leaf.vertex_color_use_as_albedo = true
		_multi(parent, cm, leaf, cones[layer])

static func grass(parent: Node, seed_value: int, count: int, area: Rect2, clear: Array) -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = seed_value
	var items: Array = []
	var tries := 0
	while items.size() < count and tries < count * 4:
		tries += 1
		var p := Vector2(rng.randf_range(area.position.x, area.end.x), rng.randf_range(area.position.y, area.end.y))
		var skip := false
		for r in clear:
			if (r as Rect2).has_point(p):
				skip = true
				break
		if skip:
			continue
		var s := rng.randf_range(0.5, 1.3)
		var b := Basis(Vector3.UP, rng.randf() * TAU).scaled(Vector3(s, s, s))
		items.append([Transform3D(b, Vector3(p.x, 0.2 * s, p.y)), Color(0.1, 0.28, 0.14) * rng.randf_range(0.7, 1.2)])
	var m := CylinderMesh.new()
	m.top_radius = 0.0
	m.bottom_radius = 0.12
	m.height = 0.45
	m.radial_segments = 4
	var mat := World.mat(Color.WHITE, 0.0, 1.0)
	mat.vertex_color_use_as_albedo = true
	_multi(parent, m, mat, items)

static func rocks(parent: Node, seed_value: int, count: int, area: Rect2, clear: Array) -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = seed_value
	for i in count:
		var p := Vector2(rng.randf_range(area.position.x, area.end.x), rng.randf_range(area.position.y, area.end.y))
		var skip := false
		for r in clear:
			if (r as Rect2).has_point(p):
				skip = true
		if skip:
			continue
		rock(parent, Vector3(p.x, 0, p.y), rng.randf_range(0.5, 1.6), rng)

static func rock(parent: Node, pos: Vector3, size: float, rng: RandomNumberGenerator) -> void:
	var mesh := MeshInstance3D.new()
	var sm := SphereMesh.new()
	sm.radial_segments = 7
	sm.rings = 4
	sm.radius = 0.5
	sm.height = 0.8
	mesh.mesh = sm
	var g := rng.randf_range(0.25, 0.4)
	mesh.material_override = World.mat(Color(g, g * 1.02, g * 1.1), 0.0, 1.0)
	mesh.position = pos + Vector3(0, 0.15 * size, 0)
	mesh.scale = Vector3(size * rng.randf_range(0.9, 1.6), size * rng.randf_range(0.5, 0.9), size * rng.randf_range(0.9, 1.4))
	mesh.rotation.y = rng.randf() * TAU
	parent.add_child(mesh)

# ---- Objets attrapables : caisse en planches avec montants, tonneau cerclé ----
static func crate() -> RigidBody3D:
	var rb := _body(Vector3(0.5, 0.5, 0.5), 2.0)
	var wood := Color(0.5, 0.35, 0.2)
	for i in 3:
		_visual_box(rb, Vector3(0, -0.17 + i * 0.17, 0), Vector3(0.5, 0.155, 0.5), wood * (0.9 + 0.1 * float(i % 2)))
	for sx in [-1, 1]:
		for sz in [-1, 1]:
			_visual_box(rb, Vector3(0.235 * sx, 0, 0.235 * sz), Vector3(0.06, 0.52, 0.06), Color(0.3, 0.2, 0.12))
	_visual_box(rb, Vector3(0, 0.255, 0), Vector3(0.52, 0.03, 0.52), Color(0.34, 0.23, 0.13))
	return rb

static func barrel() -> RigidBody3D:
	var rb := RigidBody3D.new()
	rb.collision_layer = 4
	rb.collision_mask = 1 | 4
	rb.mass = 3.0
	rb.add_to_group("grabbable")
	var cs := CollisionShape3D.new()
	var shape := CylinderShape3D.new()
	shape.radius = 0.27
	shape.height = 0.7
	cs.shape = shape
	rb.add_child(cs)
	var mi := MeshInstance3D.new()
	var cm := CylinderMesh.new()
	cm.top_radius = 0.25
	cm.bottom_radius = 0.25
	cm.height = 0.7
	cm.radial_segments = 12
	mi.mesh = cm
	mi.material_override = World.mat(Color(0.45, 0.3, 0.18))
	rb.add_child(mi)
	for y in [-0.22, 0.0, 0.22]:
		var band := MeshInstance3D.new()
		var bm := CylinderMesh.new()
		bm.top_radius = 0.27 if y != 0.0 else 0.29
		bm.bottom_radius = bm.top_radius
		bm.height = 0.04
		bm.radial_segments = 12
		band.mesh = bm
		band.position.y = y
		band.material_override = World.mat(Color(0.12, 0.12, 0.14), 0.0, 0.4)
		rb.add_child(band)
	return rb

static func _body(size: Vector3, mass: float) -> RigidBody3D:
	var rb := RigidBody3D.new()
	rb.collision_layer = 4
	rb.collision_mask = 1 | 4
	rb.mass = mass
	rb.add_to_group("grabbable")
	var cs := CollisionShape3D.new()
	var bs := BoxShape3D.new()
	bs.size = size
	cs.shape = bs
	rb.add_child(cs)
	return rb

static func _visual_box(parent: Node, pos: Vector3, size: Vector3, color: Color) -> void:
	var mi := MeshInstance3D.new()
	var bm := BoxMesh.new()
	bm.size = size
	mi.mesh = bm
	mi.position = pos
	mi.material_override = World.mat(color, 0.0, 0.9)
	parent.add_child(mi)

# Lanterne posée au sol : base métal, verre lumineux, petite lumière.
static func lantern(parent: Node, pos: Vector3, color := Color(1.0, 0.75, 0.4), with_light := true) -> Node3D:
	var n := Node3D.new()
	n.position = pos
	parent.add_child(n)
	_visual_box(n, Vector3(0, 0.03, 0), Vector3(0.2, 0.06, 0.2), Color(0.1, 0.1, 0.12))
	_visual_box(n, Vector3(0, 0.2, 0), Vector3(0.14, 0.28, 0.14), color, )
	(n.get_child(1) as MeshInstance3D).material_override = World.mat(color, 3.0)
	_visual_box(n, Vector3(0, 0.38, 0), Vector3(0.22, 0.05, 0.22), Color(0.1, 0.1, 0.12))
	if with_light:
		World.light(n, Vector3(0, 0.3, 0), color, 1.2, 6.0)
	return n

static func stump(parent: Node, pos: Vector3, height := 0.7) -> void:
	var mi := MeshInstance3D.new()
	var cm := CylinderMesh.new()
	cm.top_radius = 0.42
	cm.bottom_radius = 0.55
	cm.height = height
	cm.radial_segments = 10
	mi.mesh = cm
	mi.material_override = World.mat(Color(0.3, 0.21, 0.14), 0.0, 1.0)
	mi.position = pos + Vector3(0, height / 2.0, 0)
	parent.add_child(mi)
	var body := StaticBody3D.new()
	body.collision_layer = 1
	var cs := CollisionShape3D.new()
	var sh := CylinderShape3D.new()
	sh.radius = 0.45
	sh.height = height
	cs.shape = sh
	body.add_child(cs)
	body.position = pos + Vector3(0, height / 2.0, 0)
	parent.add_child(body)

# Pierre levée avec motif lumineux bleu (le « marqueur » du Non-lieu).
static func standing_stone(parent: Node, pos: Vector3, yaw := 0.0) -> Node3D:
	var n := Node3D.new()
	n.position = pos
	n.rotation.y = yaw
	parent.add_child(n)
	_visual_box(n, Vector3(0, 1.1, 0), Vector3(0.9, 2.2, 0.35), Color(0.22, 0.24, 0.28))
	_visual_box(n, Vector3(0, 0.1, 0), Vector3(1.2, 0.2, 0.6), Color(0.18, 0.2, 0.24))
	for i in 3:
		var line := MeshInstance3D.new()
		var bm := BoxMesh.new()
		bm.size = Vector3(0.05, 1.4, 0.02)
		line.mesh = bm
		line.position = Vector3(-0.25 + i * 0.25, 1.2, 0.185)
		line.material_override = World.mat(Color(0.3, 0.7, 1.0), 4.0)
		n.add_child(line)
	World.light(n, Vector3(0, 1.4, 0.6), Color(0.3, 0.65, 1.0), 1.6, 6.0)
	return n

# Une page de papier qui flotte légèrement, avec quelques lignes de texte.
static func page(text := "") -> Node3D:
	var n := Node3D.new()
	var mi := MeshInstance3D.new()
	var bm := BoxMesh.new()
	bm.size = Vector3(0.18, 0.25, 0.004)
	mi.mesh = bm
	mi.material_override = World.mat(Color(0.93, 0.9, 0.8), 0.6, 0.9)
	n.add_child(mi)
	for i in 5:
		_visual_box(n, Vector3(0, 0.08 - i * 0.035, 0.003), Vector3(0.12, 0.006, 0.002), Color(0.25, 0.22, 0.2))
	World.light(n, Vector3.ZERO, Color(0.5, 0.75, 1.0), 0.6, 1.8)
	return n

# Petite cabane en bois : l'ouverture de la porte fait 1 m (x de -0.5 à 0.5), la porte est ajoutée à part.
static func hut(parent: Node, pos: Vector3) -> void:
	var n := Node3D.new()
	n.position = pos
	parent.add_child(n)
	var wood := Color(0.3, 0.2, 0.13)
	World.bx(n, Vector3(-1.25, 0, 0), Vector3(1.5, 2.6, 0.15), wood, 0.0, true)
	World.bx(n, Vector3(1.25, 0, 0), Vector3(1.5, 2.6, 0.15), wood, 0.0, true)
	World.bx(n, Vector3(0, 2.1, 0), Vector3(1.0, 0.5, 0.15), wood, 0.0, true)
	World.bx(n, Vector3(-1.95, 0, -1.5), Vector3(0.15, 2.6, 3.0), wood, 0.0, true)
	World.bx(n, Vector3(1.95, 0, -1.5), Vector3(0.15, 2.6, 3.0), wood, 0.0, true)
	World.bx(n, Vector3(0, 0, -3.0), Vector3(4.0, 2.6, 0.15), wood, 0.0, true)
	World.bx(n, Vector3(0, -0.02, -1.5), Vector3(4.0, 0.04, 3.0), Color(0.22, 0.15, 0.1), 0.0, true)
	for side in [-1, 1]:
		var roof := MeshInstance3D.new()
		var bm := BoxMesh.new()
		bm.size = Vector3(2.5, 0.12, 3.6)
		roof.mesh = bm
		roof.position = Vector3(1.05 * side, 3.1, -1.5)
		roof.rotation_degrees.z = -28.0 * side
		roof.material_override = World.mat(Color(0.2, 0.13, 0.1), 0.0, 0.9)
		n.add_child(roof)
	World.light(n, Vector3(0, 1.8, -1.5), Color(1.0, 0.75, 0.4), 1.6, 5.0)
	World.bx(n, Vector3(0, 0, -2.4), Vector3(1.4, 0.8, 0.7), Color(0.34, 0.23, 0.14), 0.0, true)
	lantern(n, Vector3(0.0, 0.8, -2.4), Color(1.0, 0.75, 0.4), false)
