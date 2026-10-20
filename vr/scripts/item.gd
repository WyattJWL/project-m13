extends RigidBody3D
# Objet que l'on peut tenir, ranger (épaules, poches, torse) et lâcher : couteau, batte, hachette, clé...

var kind := "item"
var size_class := "small"        # "large" : seulement aux épaules ; "small" : épaules, poches, torse
var tip := Vector3(0, 0, -0.2)   # extrémité (lame, bout de la clé), repère local
var grip_offset := Transform3D.IDENTITY
var damage := 1.0
var state := "free"              # free | held | stowed
var holder: XRController3D = null
var slot := ""

func _ready() -> void:
	add_to_group("item")
	collision_layer = 16
	collision_mask = 1
	mass = 1.0

func attach_mode(on: bool) -> void:
	# tenu ou rangé : pas de physique, pas de collisions
	freeze = on
	freeze_mode = RigidBody3D.FREEZE_MODE_KINEMATIC
	collision_layer = 0 if on else 16
	collision_mask = 0 if on else 1
