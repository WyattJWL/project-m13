extends Area3D
# Bouton 3D visé au laser : survol = éclairé, gâchette = appui.

signal pressed

var text := "BOUTON":
	set(value):
		text = value
		if _label:
			_label.text = value
			_fit()
var size := Vector3(2.1, 0.34, 0.06)
var _label: Label3D
var _mesh: MeshInstance3D
var _mat := StandardMaterial3D.new()
var _hover := false

func _ready() -> void:
	collision_layer = 2
	collision_mask = 0
	var shape := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = size
	shape.shape = box
	add_child(shape)
	_mesh = MeshInstance3D.new()
	var bm := BoxMesh.new()
	bm.size = size
	_mesh.mesh = bm
	_mat.albedo_color = Color(0.05, 0.07, 0.13)
	_mat.emission_enabled = true
	_mat.emission = Color(0.1, 0.35, 0.8)
	_mat.emission_energy_multiplier = 0.4
	_mesh.material_override = _mat
	add_child(_mesh)
	_label = Label3D.new()
	_label.text = text
	_label.font_size = 64
	_label.pixel_size = 0.0042
	_label.position = Vector3(0, 0, size.z / 2 + 0.002)
	_label.modulate = Color(0.9, 0.95, 1)
	_label.outline_size = 6
	add_child(_label)
	_fit()

# Réduit le texte pour qu'il tienne toujours dans le bouton.
func _fit() -> void:
	var chars := maxf(1.0, float(text.length()))
	var wanted := (size.x * 0.88) / (chars * 0.58 * float(_label.font_size))
	_label.pixel_size = minf(0.0042, wanted)

func set_hover(on: bool) -> void:
	if on == _hover:
		return
	_hover = on
	_mat.emission_energy_multiplier = 1.6 if on else 0.4
	_label.modulate = Color(1, 1, 1) if on else Color(0.9, 0.95, 1)
	scale = Vector3.ONE * (1.04 if on else 1.0)

func press() -> void:
	pressed.emit()
