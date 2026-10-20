extends RefCounted
# Fabrique des objets tenables (modèles procéduraux).

const World := preload("res://scripts/world.gd")
const Item := preload("res://scripts/item.gd")

static func _part(parent: Node, pos: Vector3, size: Vector3, color: Color, shiny := 0.0) -> MeshInstance3D:
	var mi := MeshInstance3D.new()
	var bm := BoxMesh.new()
	bm.size = size
	mi.mesh = bm
	mi.position = pos
	mi.material_override = World.mat(color, 0.0, 0.35 if shiny > 0.0 else 0.8)
	parent.add_child(mi)
	return mi

static func _shape(it: Item, pos: Vector3, size: Vector3) -> void:
	var cs := CollisionShape3D.new()
	var bs := BoxShape3D.new()
	bs.size = size
	cs.shape = bs
	cs.position = pos
	it.add_child(cs)

static func knife() -> Item:
	var it := Item.new()
	it.kind = "knife"
	it.size_class = "small"
	it.tip = Vector3(0, 0, -0.2)
	it.damage = 1.0
	_part(it, Vector3(0, 0, 0.0), Vector3(0.022, 0.026, 0.1), Color(0.12, 0.08, 0.06))
	_part(it, Vector3(0, 0, -0.055), Vector3(0.05, 0.012, 0.012), Color(0.3, 0.3, 0.32), 1.0)
	_part(it, Vector3(0, 0, -0.14), Vector3(0.024, 0.006, 0.15), Color(0.78, 0.8, 0.85), 1.0)
	_shape(it, Vector3(0, 0, -0.06), Vector3(0.05, 0.03, 0.3))
	return it

static func bat() -> Item:
	var it := Item.new()
	it.kind = "bat"
	it.size_class = "large"
	it.tip = Vector3(0, 0, -0.75)
	it.damage = 2.0
	var mi := MeshInstance3D.new()
	var cm := CylinderMesh.new()
	cm.top_radius = 0.045
	cm.bottom_radius = 0.022
	cm.height = 0.85
	cm.radial_segments = 10
	mi.mesh = cm
	mi.rotation_degrees.x = 90
	mi.position = Vector3(0, 0, -0.33)
	mi.material_override = World.mat(Color(0.55, 0.38, 0.22), 0.0, 0.7)
	it.add_child(mi)
	_part(it, Vector3(0, 0, 0.0), Vector3(0.05, 0.05, 0.12), Color(0.1, 0.1, 0.12))
	_shape(it, Vector3(0, 0, -0.33), Vector3(0.1, 0.1, 0.85))
	return it

static func hatchet() -> Item:
	var it := Item.new()
	it.kind = "hatchet"
	it.size_class = "large"
	it.tip = Vector3(0, 0, -0.38)
	it.damage = 3.0
	_part(it, Vector3(0, 0, -0.15), Vector3(0.03, 0.03, 0.5), Color(0.5, 0.34, 0.2))
	_part(it, Vector3(0, 0.0, -0.36), Vector3(0.02, 0.04, 0.1), Color(0.2, 0.2, 0.22), 1.0)
	_part(it, Vector3(0, 0.0, -0.4), Vector3(0.012, 0.16, 0.09), Color(0.7, 0.72, 0.78), 1.0)
	_shape(it, Vector3(0, 0, -0.2), Vector3(0.1, 0.18, 0.55))
	return it

static func key() -> Item:
	var it := Item.new()
	it.kind = "key"
	it.size_class = "small"
	it.tip = Vector3(0, 0, -0.1)
	it.damage = 0.0
	var ring := MeshInstance3D.new()
	var tm := TorusMesh.new()
	tm.inner_radius = 0.012
	tm.outer_radius = 0.024
	ring.mesh = tm
	ring.rotation_degrees.x = 90
	ring.position = Vector3(0, 0, 0.045)
	ring.material_override = World.mat(Color(0.85, 0.65, 0.25), 0.3, 0.3)
	it.add_child(ring)
	_part(it, Vector3(0, 0, -0.02), Vector3(0.008, 0.008, 0.12), Color(0.85, 0.65, 0.25), 1.0)
	_part(it, Vector3(0.012, 0, -0.07), Vector3(0.022, 0.008, 0.012), Color(0.85, 0.65, 0.25), 1.0)
	_part(it, Vector3(0.012, 0, -0.095), Vector3(0.022, 0.008, 0.012), Color(0.85, 0.65, 0.25), 1.0)
	_shape(it, Vector3(0, 0, -0.02), Vector3(0.05, 0.05, 0.16))
	return it

# Document à lire : on l'attrape (GRIP), on le rapproche du visage pour le lire.
static func doc(title: String, text: String) -> Item:
	var d := Item.new()
	d.kind = "doc"
	d.size_class = "small"
	d.tip = Vector3(0, 0, -0.1)
	d.damage = 0.0
	d.set_meta("title", title)
	d.set_meta("text", text)
	_part(d, Vector3(0, 0, 0), Vector3(0.17, 0.006, 0.23), Color(0.93, 0.9, 0.8), 0.0)
	for i in 5:
		_part(d, Vector3(0, 0.004, -0.07 + i * 0.035), Vector3(0.12, 0.002, 0.008), Color(0.25, 0.22, 0.2))
	_shape(d, Vector3.ZERO, Vector3(0.17, 0.03, 0.23))
	d.grip_offset = Transform3D(Basis(Vector3.RIGHT, deg_to_rad(-75)), Vector3(0, 0.03, -0.08))
	return d

static func poincon(letter := "K") -> Item:
	var p := Item.new()
	p.kind = "poincon"
	p.size_class = "small"
	p.tip = Vector3(0, 0, -0.08)
	p.damage = 0.0
	_part(p, Vector3(0, 0, 0.02), Vector3(0.03, 0.03, 0.07), Color(0.18, 0.18, 0.22), 1.0)
	_part(p, Vector3(0, 0, -0.04), Vector3(0.012, 0.012, 0.06), Color(0.7, 0.7, 0.75), 1.0)
	_part(p, Vector3(0, 0, -0.075), Vector3(0.03, 0.03, 0.01), Color(0.3, 0.65, 1.0), 1.0)
	_shape(p, Vector3.ZERO, Vector3(0.05, 0.05, 0.15))
	return p
