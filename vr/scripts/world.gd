extends RefCounted
# Petits générateurs de décor réutilisés par le menu et le tutoriel.

static func mat(color: Color, emissive := 0.0, rough := 0.8) -> StandardMaterial3D:
	var m := StandardMaterial3D.new()
	m.albedo_color = color
	m.roughness = rough
	if emissive > 0.0:
		m.emission_enabled = true
		m.emission = color
		m.emission_energy_multiplier = emissive
	return m

static func box(parent: Node, pos: Vector3, size: Vector3, color: Color, emissive := 0.0, solid := false) -> Node3D:
	var node: Node3D
	var mesh := MeshInstance3D.new()
	var bm := BoxMesh.new()
	bm.size = size
	mesh.mesh = bm
	mesh.material_override = mat(color, emissive)
	if solid:
		var body := StaticBody3D.new()
		body.collision_layer = 1
		var cs := CollisionShape3D.new()
		var bs := BoxShape3D.new()
		bs.size = size
		cs.shape = bs
		body.add_child(cs)
		body.add_child(mesh)
		node = body
	else:
		node = mesh
	node.position = pos
	parent.add_child(node)
	return node

static func label(parent: Node, text: String, pos: Vector3, size := 0.004, color := Color.WHITE, font_size := 64) -> Label3D:
	var l := Label3D.new()
	l.text = text
	l.position = pos
	l.pixel_size = size
	l.font_size = font_size
	l.modulate = color
	l.outline_size = 8
	parent.add_child(l)
	return l

static func environment(parent: Node, fog_color: Color, ambient: Color, fog_density := 0.04) -> void:
	var env := Environment.new()
	env.background_mode = Environment.BG_COLOR
	env.background_color = fog_color
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.ambient_light_color = ambient
	env.ambient_light_energy = 1.0
	env.fog_enabled = true
	env.fog_light_color = fog_color
	env.fog_density = fog_density
	var we := WorldEnvironment.new()
	we.environment = env
	parent.add_child(we)

static func light(parent: Node, pos: Vector3, color: Color, energy := 1.5, reach := 8.0) -> OmniLight3D:
	var l := OmniLight3D.new()
	l.position = pos
	l.light_color = color
	l.light_energy = energy
	l.omni_range = reach
	parent.add_child(l)
	return l

# Les lignes verticales bleues du Non-lieu, en fond de décor.
static func blue_lines(parent: Node, center: Vector3, radius: float, count: int, height := 6.0) -> void:
	for i in count:
		var a := TAU * float(i) / float(count)
		var pos := center + Vector3(cos(a) * radius, height / 2.0, sin(a) * radius)
		box(parent, pos, Vector3(0.06, height, 0.06), Color(0.3, 0.65, 1.0), 2.5)
