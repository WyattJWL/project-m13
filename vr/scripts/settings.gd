extends Node
# Réglages du joueur (confort VR), sauvegardés dans user://settings.cfg.

const PATH := "user://settings.cfg"

var move_mode := "teleport"   # "teleport" (confortable) ou "smooth"
var turn_mode := "snap"       # "snap" (par crans) ou "smooth"
var snap_degrees := 30.0
var vignette := true          # assombrit les bords pendant les déplacements
var seated := false           # mode assis : monte la vue de 40 cm
var tutorial_done := false

func _ready() -> void:
	var cfg := ConfigFile.new()
	if cfg.load(PATH) != OK:
		return
	move_mode = cfg.get_value("comfort", "move_mode", move_mode)
	turn_mode = cfg.get_value("comfort", "turn_mode", turn_mode)
	snap_degrees = cfg.get_value("comfort", "snap_degrees", snap_degrees)
	vignette = cfg.get_value("comfort", "vignette", vignette)
	seated = cfg.get_value("comfort", "seated", seated)
	tutorial_done = cfg.get_value("progress", "tutorial_done", tutorial_done)

func save() -> void:
	var cfg := ConfigFile.new()
	cfg.set_value("comfort", "move_mode", move_mode)
	cfg.set_value("comfort", "turn_mode", turn_mode)
	cfg.set_value("comfort", "snap_degrees", snap_degrees)
	cfg.set_value("comfort", "vignette", vignette)
	cfg.set_value("comfort", "seated", seated)
	cfg.set_value("progress", "tutorial_done", tutorial_done)
	cfg.save(PATH)
