extends Node
# Réglages du joueur (confort VR) et parties sauvegardées (3 emplacements), dans user://settings.cfg.

const PATH := "user://settings.cfg"
const DIFFICULTIES := {
	"easy": {"label": "FACILE", "speed": 0.8, "cooldown": 8.0},
	"normal": {"label": "NORMAL", "speed": 1.2, "cooldown": 12.0},
	"hard": {"label": "DIFFICILE", "speed": 1.7, "cooldown": 16.0},
}

var move_mode := "smooth"     # "smooth" (par défaut) ou "teleport"
var turn_mode := "snap"       # "snap" (par crans) ou "smooth"
var snap_degrees := 30.0
var vignette := true          # assombrit les bords pendant les déplacements
var seated := false           # mode assis : monte la vue de 40 cm
var dominant := "right"       # main dominante : "right" ou "left"
var slots: Array = [{}, {}, {}]   # { name, difficulty, tutorial_done, created }
var current_slot := -1

func _ready() -> void:
	var cfg := ConfigFile.new()
	if cfg.load(PATH) != OK:
		return
	move_mode = cfg.get_value("comfort", "move_mode", move_mode)
	turn_mode = cfg.get_value("comfort", "turn_mode", turn_mode)
	snap_degrees = cfg.get_value("comfort", "snap_degrees", snap_degrees)
	vignette = cfg.get_value("comfort", "vignette", vignette)
	seated = cfg.get_value("comfort", "seated", seated)
	dominant = cfg.get_value("comfort", "dominant", dominant)
	var saved = cfg.get_value("progress", "slots", slots)
	if saved is Array and saved.size() == 3:
		slots = saved

func save() -> void:
	var cfg := ConfigFile.new()
	cfg.set_value("comfort", "move_mode", move_mode)
	cfg.set_value("comfort", "turn_mode", turn_mode)
	cfg.set_value("comfort", "snap_degrees", snap_degrees)
	cfg.set_value("comfort", "vignette", vignette)
	cfg.set_value("comfort", "seated", seated)
	cfg.set_value("comfort", "dominant", dominant)
	cfg.set_value("progress", "slots", slots)
	cfg.save(PATH)

func has_saves() -> bool:
	for s in slots:
		if not (s as Dictionary).is_empty():
			return true
	return false

func slot_label(i: int) -> String:
	var s: Dictionary = slots[i]
	if s.is_empty():
		return "PARTIE %d  -  VIDE" % (i + 1)
	var d: Dictionary = DIFFICULTIES.get(s.get("difficulty", "normal"), DIFFICULTIES["normal"])
	var where := "TUTORIEL" if not s.get("tutorial_done", false) else "CHAPITRE 1"
	return "PARTIE %d  -  %s  -  %s" % [i + 1, d["label"], where]

func new_game(i: int, difficulty: String) -> void:
	slots[i] = {"name": "Partie %d" % (i + 1), "difficulty": difficulty, "tutorial_done": false, "created": Time.get_unix_time_from_system()}
	current_slot = i
	save()

func load_game(i: int) -> void:
	current_slot = i

func current() -> Dictionary:
	if current_slot >= 0 and current_slot < slots.size():
		return slots[current_slot]
	return {}

func tutorial_done() -> bool:
	return current().get("tutorial_done", false)

func mark_tutorial_done() -> void:
	if current_slot >= 0:
		slots[current_slot]["tutorial_done"] = true
		save()

func difficulty() -> Dictionary:
	return DIFFICULTIES.get(current().get("difficulty", "normal"), DIFFICULTIES["normal"])

func power_cooldown() -> float:
	return float(difficulty()["cooldown"])

func enemy_speed() -> float:
	return float(difficulty()["speed"])
