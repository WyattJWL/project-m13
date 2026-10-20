extends RefCounted
# Décors du Tome 1 (procéduraux). Locations.build(id, stage, rig) -> { spawn, yaw, marks }
# marks : points utiles pour l'histoire (nom -> Vector3). Les pièces sont fermées (rig.bounds limite la zone).

const World := preload("res://scripts/world.gd")
const Props := preload("res://scripts/props.gd")

const LOOKS := {
	"rain": {"sky": Color(0.03, 0.05, 0.1), "hor": Color(0.1, 0.13, 0.2), "fog": Color(0.1, 0.13, 0.19), "den": 0.04, "amb": Color(0.25, 0.3, 0.45), "moon": 0.35},
	"night": {"sky": Color(0.02, 0.04, 0.12), "hor": Color(0.08, 0.14, 0.26), "fog": Color(0.05, 0.08, 0.14), "den": 0.03, "amb": Color(0.22, 0.3, 0.5), "moon": 0.55},
	"day": {"sky": Color(0.35, 0.5, 0.75), "hor": Color(0.7, 0.78, 0.9), "fog": Color(0.7, 0.78, 0.88), "den": 0.012, "amb": Color(0.7, 0.72, 0.8), "moon": 1.0},
	"winter": {"sky": Color(0.55, 0.62, 0.72), "hor": Color(0.82, 0.86, 0.92), "fog": Color(0.8, 0.84, 0.9), "den": 0.02, "amb": Color(0.7, 0.74, 0.82), "moon": 0.7},
	"warm": {"sky": Color(0.1, 0.08, 0.1), "hor": Color(0.2, 0.15, 0.12), "fog": Color(0.16, 0.11, 0.08), "den": 0.01, "amb": Color(0.55, 0.42, 0.32), "moon": 0.0},
	"cold": {"sky": Color(0.05, 0.07, 0.12), "hor": Color(0.1, 0.13, 0.2), "fog": Color(0.08, 0.1, 0.16), "den": 0.015, "amb": Color(0.32, 0.38, 0.5), "moon": 0.0},
	"perfect": {"sky": Color(1.0, 0.95, 0.8), "hor": Color(1.0, 0.97, 0.85), "fog": Color(1.0, 0.95, 0.8), "den": 0.02, "amb": Color(1.0, 0.92, 0.75), "moon": 0.0},
	"void": {"sky": Color(0.8, 0.85, 0.95), "hor": Color(0.9, 0.93, 1.0), "fog": Color(0.88, 0.92, 1.0), "den": 0.04, "amb": Color(0.8, 0.84, 0.98), "moon": 0.0},
	"fire": {"sky": Color(0.02, 0.05, 0.2), "hor": Color(0.05, 0.15, 0.4), "fog": Color(0.05, 0.12, 0.35), "den": 0.04, "amb": Color(0.2, 0.35, 0.8), "moon": 0.3},
	"cave": {"sky": Color(0.04, 0.03, 0.03), "hor": Color(0.06, 0.05, 0.04), "fog": Color(0.07, 0.06, 0.05), "den": 0.05, "amb": Color(0.3, 0.25, 0.2), "moon": 0.0},
	"lab": {"sky": Color(0.03, 0.06, 0.1), "hor": Color(0.05, 0.1, 0.18), "fog": Color(0.05, 0.09, 0.16), "den": 0.02, "amb": Color(0.3, 0.45, 0.65), "moon": 0.0},
	"vr": {"sky": Color(0.02, 0.04, 0.2), "hor": Color(0.05, 0.1, 0.4), "fog": Color(0.03, 0.06, 0.25), "den": 0.03, "amb": Color(0.3, 0.45, 0.9), "moon": 0.0},
}

static func look(stage: Node, name: String) -> void:
	var L: Dictionary = LOOKS[name]
	var sky_mat := ProceduralSkyMaterial.new()
	sky_mat.sky_top_color = L["sky"]
	sky_mat.sky_horizon_color = L["hor"]
	sky_mat.ground_horizon_color = L["hor"]
	sky_mat.ground_bottom_color = (L["sky"] as Color) * 0.5
	var sky := Sky.new()
	sky.sky_material = sky_mat
	var env := Environment.new()
	env.background_mode = Environment.BG_SKY
	env.sky = sky
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.ambient_light_color = L["amb"]
	env.ambient_light_energy = 0.9
	env.fog_enabled = true
	env.fog_light_color = L["fog"]
	env.fog_density = L["den"]
	env.glow_enabled = true
	env.glow_intensity = 0.8
	var we := WorldEnvironment.new()
	we.environment = env
	stage.add_child(we)
	if (L["moon"] as float) > 0.0:
		var moon := DirectionalLight3D.new()
		moon.light_color = Color(0.6, 0.72, 1.0) if name != "day" and name != "winter" else Color(1, 0.97, 0.9)
		moon.light_energy = L["moon"]
		moon.rotation_degrees = Vector3(-50, 30, 0)
		stage.add_child(moon)

# ---------- meubles (au sol, centrés sur x, z) ----------
static func _node(stage: Node, x: float, z: float, yaw: float) -> Node3D:
	var n := Node3D.new()
	n.position = Vector3(x, 0, z)
	n.rotation_degrees.y = yaw
	stage.add_child(n)
	return n

static func furniture(stage: Node, kind: String, x: float, z: float, yaw := 0.0) -> Node3D:
	var n := _node(stage, x, z, yaw)
	var wood := Color(0.36, 0.24, 0.15)
	match kind:
		"table":
			World.bx(n, Vector3(0, 0.72, 0), Vector3(1.6, 0.06, 0.9), wood, 0.0, true)
			for sx in [-0.7, 0.7]:
				for sz in [-0.35, 0.35]:
					World.bx(n, Vector3(sx, 0, sz), Vector3(0.07, 0.72, 0.07), wood * 0.8)
		"chair":
			World.bx(n, Vector3(0, 0.42, 0), Vector3(0.42, 0.05, 0.42), wood)
			World.bx(n, Vector3(0, 0.45, 0.19), Vector3(0.42, 0.5, 0.05), wood)
			for sx in [-0.18, 0.18]:
				for sz in [-0.18, 0.18]:
					World.bx(n, Vector3(sx, 0, sz), Vector3(0.04, 0.42, 0.04), wood * 0.8)
		"bed":
			World.bx(n, Vector3(0, 0.0, 0), Vector3(1.1, 0.4, 2.0), wood * 0.9, 0.0, true)
			World.bx(n, Vector3(0, 0.4, 0.1), Vector3(1.0, 0.18, 1.8), Color(0.55, 0.6, 0.8))
			World.bx(n, Vector3(0, 0.55, -0.75), Vector3(0.7, 0.14, 0.35), Color(0.9, 0.9, 0.95))
		"sofa":
			World.bx(n, Vector3(0, 0, 0), Vector3(2.0, 0.45, 0.9), Color(0.4, 0.3, 0.32), 0.0, true)
			World.bx(n, Vector3(0, 0.45, 0.35), Vector3(2.0, 0.5, 0.2), Color(0.35, 0.26, 0.28))
			for sx in [-1.0, 1.0]:
				World.bx(n, Vector3(sx, 0.45, 0), Vector3(0.18, 0.3, 0.9), Color(0.35, 0.26, 0.28))
		"shelf":
			World.bx(n, Vector3(0, 0, 0), Vector3(1.6, 2.2, 0.35), wood * 0.85, 0.0, true)
			for i in 4:
				for j in 7:
					var c := Color.from_hsv(randf() * 0.15 + 0.02 * float(j % 3), 0.5, 0.45 + 0.2 * randf())
					World.bx(n, Vector3(-0.65 + j * 0.2, 0.2 + i * 0.5, -0.19), Vector3(0.15, 0.36, 0.2), c)
		"desk":
			World.bx(n, Vector3(0, 0.74, 0), Vector3(1.4, 0.05, 0.7), wood, 0.0, true)
			World.bx(n, Vector3(-0.6, 0, 0), Vector3(0.06, 0.74, 0.6), wood * 0.8)
			World.bx(n, Vector3(0.6, 0, 0), Vector3(0.06, 0.74, 0.6), wood * 0.8)
		"pc":
			World.bx(n, Vector3(0, 0.74, 0), Vector3(1.4, 0.05, 0.7), wood, 0.0, true)
			World.bx(n, Vector3(-0.6, 0, 0), Vector3(0.06, 0.74, 0.6), wood * 0.8)
			World.bx(n, Vector3(0.6, 0, 0), Vector3(0.06, 0.74, 0.6), wood * 0.8)
			World.bx(n, Vector3(0, 0.8, -0.1), Vector3(0.6, 0.38, 0.05), Color(0.1, 0.1, 0.12))
			World.bx(n, Vector3(0, 0.83, -0.075), Vector3(0.54, 0.31, 0.01), Color(0.3, 0.65, 1.0), 2.0)
		"cabinet":
			World.bx(n, Vector3(0, 0, 0), Vector3(1.2, 1.1, 0.5), wood * 0.9, 0.0, true)
			World.bx(n, Vector3(0, 1.1, 0), Vector3(1.3, 0.05, 0.55), wood)
		"counter":
			World.bx(n, Vector3(0, 0, 0), Vector3(3.0, 1.0, 0.7), wood * 0.8, 0.0, true)
			World.bx(n, Vector3(0, 1.0, 0), Vector3(3.1, 0.05, 0.8), Color(0.6, 0.5, 0.4))
		"bench":
			World.bx(n, Vector3(0, 0.42, 0), Vector3(1.6, 0.06, 0.4), wood)
			World.bx(n, Vector3(-0.7, 0, 0), Vector3(0.06, 0.42, 0.35), wood * 0.8)
			World.bx(n, Vector3(0.7, 0, 0), Vector3(0.06, 0.42, 0.35), wood * 0.8)
		"pew":
			World.bx(n, Vector3(0, 0.42, 0), Vector3(2.4, 0.06, 0.45), wood)
			World.bx(n, Vector3(0, 0.45, 0.22), Vector3(2.4, 0.55, 0.05), wood * 0.9)
			World.bx(n, Vector3(-1.15, 0, 0), Vector3(0.06, 0.42, 0.4), wood * 0.8)
			World.bx(n, Vector3(1.15, 0, 0), Vector3(0.06, 0.42, 0.4), wood * 0.8)
		"rug":
			World.bx(n, Vector3(0, 0.0, 0), Vector3(2.4, 0.02, 1.6), Color(0.45, 0.18, 0.2))
		"crate":
			World.bx(n, Vector3(0, 0, 0), Vector3(0.9, 0.9, 0.9), Color(0.5, 0.36, 0.2), 0.0, true)
		"boxes":
			for i in 4:
				World.bx(n, Vector3((i % 2) * 0.7 - 0.35, (i / 2) * 0.5, 0), Vector3(0.6, 0.5, 0.6), Color(0.6, 0.5, 0.35), 0.0, true)
		"lamp":
			World.bx(n, Vector3(0, 0, 0), Vector3(0.08, 1.5, 0.08), Color(0.2, 0.2, 0.22))
			World.bx(n, Vector3(0, 1.5, 0), Vector3(0.3, 0.25, 0.3), Color(1.0, 0.85, 0.55), 2.0)
			World.light(n, Vector3(0, 1.4, 0), Color(1.0, 0.8, 0.5), 1.4, 7.0)
		"tv":
			World.bx(n, Vector3(0, 0, 0), Vector3(1.2, 0.5, 0.4), wood * 0.8, 0.0, true)
			World.bx(n, Vector3(0, 0.5, 0), Vector3(1.1, 0.65, 0.08), Color(0.05, 0.05, 0.07))
		"fireplace":
			World.bx(n, Vector3(0, 0, 0), Vector3(2.0, 1.5, 0.6), Color(0.4, 0.38, 0.35), 0.0, true)
			World.bx(n, Vector3(0, 0.1, 0.1), Vector3(1.2, 0.9, 0.3), Color(0.05, 0.03, 0.02))
			World.bx(n, Vector3(0, 0.2, 0.15), Vector3(0.6, 0.3, 0.1), Color(1.0, 0.5, 0.15), 3.0)
			World.light(n, Vector3(0, 0.6, 0.6), Color(1.0, 0.55, 0.25), 2.0, 8.0)
		"plant":
			World.bx(n, Vector3(0, 0, 0), Vector3(0.35, 0.4, 0.35), Color(0.5, 0.3, 0.2))
			World.bx(n, Vector3(0, 0.4, 0), Vector3(0.5, 0.7, 0.5), Color(0.15, 0.4, 0.2))
		"barrel":
			var b := Props.barrel()
			b.freeze = true
			n.add_child(b)
		"coffin":
			World.bx(n, Vector3(0, 0.6, 0), Vector3(0.8, 0.5, 2.0), Color(0.3, 0.2, 0.12), 0.0, true)
			World.bx(n, Vector3(0, 1.1, 0), Vector3(0.7, 0.12, 1.9), Color(0.9, 0.9, 0.92))
		"altar":
			World.bx(n, Vector3(0, 0, 0), Vector3(2.0, 1.0, 0.8), Color(0.75, 0.72, 0.68), 0.0, true)
			World.bx(n, Vector3(0, 1.0, 0), Vector3(2.2, 0.06, 0.9), Color(0.85, 0.83, 0.8))
		"locker":
			for i in 5:
				World.bx(n, Vector3(-1.0 + i * 0.5, 0, 0), Vector3(0.45, 1.9, 0.45), Color(0.3, 0.38, 0.5), 0.0, true)
		"seat":
			World.bx(n, Vector3(0, 0.0, 0), Vector3(0.9, 0.45, 0.5), Color(0.2, 0.3, 0.5))
			World.bx(n, Vector3(0, 0.45, 0.22), Vector3(0.9, 0.7, 0.1), Color(0.18, 0.27, 0.45))
		"server":
			World.bx(n, Vector3(0, 0, 0), Vector3(0.7, 2.0, 0.7), Color(0.12, 0.13, 0.16), 0.0, true)
			for i in 6:
				World.bx(n, Vector3(0.0, 0.2 + i * 0.3, 0.36), Vector3(0.5, 0.04, 0.01), Color(0.3, 1.0, 0.5), 2.0)
		"frame":
			World.bx(n, Vector3(0, 1.2, 0), Vector3(0.5, 0.65, 0.04), Color(0.25, 0.18, 0.1))
			World.bx(n, Vector3(0, 1.2, 0.025), Vector3(0.42, 0.57, 0.01), Color(0.7, 0.68, 0.62))
		"basket":
			World.bx(n, Vector3(0, 0, 0), Vector3(0.8, 0.22, 0.6), Color(0.6, 0.45, 0.25))
			World.bx(n, Vector3(0, 0.18, 0), Vector3(0.6, 0.1, 0.4), Color(0.8, 0.25, 0.25))
		"window":
			World.bx(n, Vector3(0, 1.0, 0), Vector3(1.2, 1.2, 0.08), Color(0.35, 0.5, 0.8), 0.8)
	return n

# ---------- pièce fermée ----------
static func room(stage: Node, w: float, d: float, h: float, wall: Color, floor_c: Color, ceiling := true) -> void:
	var t := 0.2
	World.bx(stage, Vector3(0, -0.1, 0), Vector3(w + 2.0, 0.2, d + 2.0), floor_c, 0.0, true)
	World.bx(stage, Vector3(0, 0, -d / 2.0 - t / 2.0), Vector3(w + t * 2.0, h, t), wall, 0.0, true)
	World.bx(stage, Vector3(0, 0, d / 2.0 + t / 2.0), Vector3(w + t * 2.0, h, t), wall, 0.0, true)
	World.bx(stage, Vector3(-w / 2.0 - t / 2.0, 0, 0), Vector3(t, h, d), wall, 0.0, true)
	World.bx(stage, Vector3(w / 2.0 + t / 2.0, 0, 0), Vector3(t, h, d), wall, 0.0, true)
	if ceiling:
		World.bx(stage, Vector3(0, h, 0), Vector3(w + 2.0, 0.2, d + 2.0), wall * 0.9)

static func marks_from(spec: Dictionary) -> Dictionary:
	var out := {}
	for k in spec:
		var v: Array = spec[k]
		out[k] = Vector3(v[0], v[1] if v.size() > 2 else 0.0, v[v.size() - 1])
	return out

# Décors intérieurs définis par des données : taille, couleurs, éclairage, meubles, points utiles.
const INTERIORS := {
	"clara_room": {"size": [5.5, 4.5, 2.7], "wall": [0.55, 0.42, 0.5], "floor": [0.38, 0.27, 0.2], "look": "warm", "light": [1.0, 0.78, 0.5],
		"furn": [["bed", -1.8, -1.6, 0], ["desk", 1.6, -1.8, 0], ["chair", 1.6, -1.0, 180], ["shelf", 2.5, 0.5, -90], ["rug", 0, 0.2, 0], ["window", 0, -2.2, 0], ["lamp", -2.4, 1.6, 0], ["plant", 2.4, 1.8, 0]],
		"marks": {"desk": [1.6, 0.8, -1.8], "clara": [0.6, 0.0, -0.4], "alex": [-0.8, 0.0, 0.3], "window": [0, 1.2, -2.0]}, "spawn": [0, 0, 1.6]},
	"lenoir": {"size": [8.0, 6.0, 2.8], "wall": [0.6, 0.55, 0.48], "floor": [0.35, 0.25, 0.18], "look": "cold", "light": [1.0, 0.85, 0.6],
		"furn": [["sofa", -2.0, 1.4, 180], ["tv", -2.0, 2.6, 180], ["rug", -2.0, 0.3, 0], ["cabinet", 3.0, -2.8, 0], ["table", 0.6, -1.5, 0], ["chair", 0.6, -0.7, 180], ["pc", 3.1, 1.5, -90], ["chair", 2.3, 1.5, -90], ["bed", -3.2, -2.3, 90], ["lamp", -3.6, 2.4, 0], ["window", 0, -3.0, 0]],
		"marks": {"franck": [-0.5, 0.0, 0.9], "buffet": [3.0, 1.15, -2.8], "desk": [3.1, 0.85, 1.5], "computer": [3.1, 1.2, 1.5], "headset": [3.1, 0.85, 1.2], "sofa": [-2.0, 0.0, 0.2]}, "spawn": [0, 0, 2.2]},
	"perfect": {"size": [8.0, 6.0, 3.0], "wall": [1.0, 0.95, 0.8], "floor": [0.85, 0.7, 0.5], "look": "perfect", "light": [1.0, 0.92, 0.7],
		"furn": [["sofa", -2.0, 1.4, 180], ["rug", -2.0, 0.3, 0], ["table", 0.8, -1.5, 0], ["plant", -3.5, -2.5, 0], ["plant", 3.5, -2.5, 0], ["basket", 2.0, 0.5, 0], ["frame", 1.0, -2.95, 0], ["window", -2.0, -2.95, 0], ["window", 3.0, -2.95, 0]],
		"marks": {"franck": [0.8, 0.0, 0.2], "miel": [2.0, 0.3, 0.5], "photo": [1.0, 1.2, -2.8]}, "spawn": [0, 0, 2.3]},
	"library": {"size": [9.0, 7.0, 3.4], "wall": [0.45, 0.35, 0.26], "floor": [0.3, 0.2, 0.13], "look": "warm", "light": [1.0, 0.8, 0.5],
		"furn": [["shelf", -3.5, -3.1, 0], ["shelf", -1.8, -3.1, 0], ["shelf", 1.8, -3.1, 0], ["shelf", 3.5, -3.1, 0], ["shelf", -4.3, -0.5, 90], ["shelf", 4.3, -0.5, -90], ["table", -1.5, 0.5, 0], ["table", 1.5, 0.5, 0], ["chair", -1.5, 1.3, 180], ["chair", 1.5, 1.3, 180], ["counter", 0, 2.6, 0], ["lamp", -1.5, 0.5, 0], ["lamp", 1.5, 0.5, 0]],
		"marks": {"librarian": [0, 0.0, 3.2], "manuscript": [-1.5, 0.8, 0.5], "grimoire": [1.5, 0.8, 0.5], "shelf": [0, 0.0, -2.4], "registry": [0, 1.0, -2.8], "clipping": [3.5, 1.0, -2.6]}, "spawn": [0, 0, 1.8]},
	"college": {"size": [10.0, 7.0, 3.2], "wall": [0.75, 0.75, 0.7], "floor": [0.5, 0.52, 0.5], "look": "day", "light": [1.0, 0.98, 0.9],
		"furn": [["table", -2.5, -0.5, 0], ["table", 0.0, -0.5, 0], ["table", 2.5, -0.5, 0], ["table", -2.5, 1.5, 0], ["table", 0.0, 1.5, 0], ["table", 2.5, 1.5, 0], ["desk", 0.0, -2.8, 0], ["locker", -4.2, 0, 90], ["window", 3.0, -3.45, 0]],
		"marks": {"screen": [0, 1.5, -3.3], "alex": [-1.2, 0.0, 2.8], "clara": [1.2, 0.0, 2.8], "desk": [0, 0.8, -2.8]}, "spawn": [0, 0, 3.0]},
	"mairie": {"size": [8.0, 6.0, 3.2], "wall": [0.8, 0.78, 0.7], "floor": [0.55, 0.5, 0.45], "look": "winter", "light": [1.0, 0.98, 0.92],
		"furn": [["counter", 0, -1.8, 0], ["bench", -2.5, 1.5, 0], ["bench", 2.5, 1.5, 0], ["shelf", 3.4, -2.8, 0], ["shelf", -3.4, -2.8, 0], ["plant", 3.6, 2.4, 0]],
		"marks": {"clerk": [0, 0.0, -2.4], "registry": [3.4, 1.0, -2.6], "map": [0, 1.6, -2.95], "bench": [-2.5, 0.5, 1.5]}, "spawn": [0, 0, 2.4]},
	"templier": {"size": [7.0, 6.0, 2.8], "wall": [0.72, 0.66, 0.52], "floor": [0.45, 0.38, 0.3], "look": "warm", "light": [1.0, 0.7, 0.4],
		"furn": [["fireplace", 0, -2.65, 0], ["table", 0.0, 0.6, 0], ["chair", -1.0, 0.6, 90], ["chair", 1.0, 0.6, -90], ["shelf", -3.2, -0.5, 90], ["crate", 2.8, -2.0, 0], ["bed", 2.8, 1.8, 0], ["lamp", -2.6, 2.4, 0]],
		"marks": {"templier": [0, 0.0, -0.9], "table": [0, 0.8, 0.6], "chest": [2.8, 0.9, -2.0], "fireplace": [0, 0.5, -2.2], "map": [-3.0, 1.4, -0.5], "window": [0, 1.2, 2.9]}, "spawn": [0, 0, 2.3]},
	"vasseur": {"size": [8.0, 6.0, 2.8], "wall": [0.5, 0.48, 0.42], "floor": [0.28, 0.22, 0.17], "look": "cold", "light": [0.8, 0.85, 1.0],
		"furn": [["pc", 2.8, -2.2, 0], ["chair", 2.8, -1.4, 180], ["cabinet", -3.2, -2.5, 0], ["cabinet", -1.8, -2.5, 0], ["shelf", 0.0, -2.8, 0], ["sofa", -2.5, 1.5, 180], ["table", 0.5, 0.8, 0], ["frame", -3.9, -0.5, 90], ["frame", -3.9, 0.8, 90], ["frame", -3.9, 2.1, 90]],
		"marks": {"photos": [-3.7, 1.2, 0.8], "files": [-3.0, 1.2, -2.2], "computer": [2.8, 1.1, -2.2], "desk": [2.8, 0.85, -2.2], "cabinet": [-1.8, 1.15, -2.5], "franck": [0, 0.0, 1.8]}, "spawn": [0, 0, 2.5]},
	"church": {"size": [9.0, 16.0, 6.0], "wall": [0.7, 0.68, 0.64], "floor": [0.5, 0.45, 0.4], "look": "winter", "light": [1.0, 0.95, 0.85],
		"furn": [["pew", -2.5, -2.0, 0], ["pew", 2.5, -2.0, 0], ["pew", -2.5, 0.4, 0], ["pew", 2.5, 0.4, 0], ["pew", -2.5, 2.8, 0], ["pew", 2.5, 2.8, 0], ["altar", 0, -7.2, 0], ["coffin", 0, -5.6, 0], ["window", -4.4, -3.0, 90], ["window", 4.4, -3.0, -90]],
		"marks": {"coffin": [0, 1.2, -5.6], "altar": [0, 1.0, -7.2], "pew": [-2.5, 0.5, 2.8], "clara": [-2.5, 0.0, 1.6], "alex": [2.5, 0.0, 1.6], "franck": [-1.2, 0.0, -4.2]}, "spawn": [0, 0, 7.0]},
	"restaurant": {"size": [10.0, 7.0, 3.2], "wall": [0.55, 0.3, 0.25], "floor": [0.4, 0.28, 0.2], "look": "warm", "light": [1.0, 0.8, 0.55],
		"furn": [["table", -2.5, 0.0, 0], ["table", 2.5, 0.0, 0], ["table", -2.5, 2.2, 0], ["chair", -2.5, 0.9, 180], ["chair", -2.5, -0.9, 0], ["chair", -1.5, 0, 90], ["chair", -3.5, 0, -90], ["counter", 0, -3.0, 0], ["lamp", 4.3, -2.8, 0], ["window", 0, 3.45, 180]],
		"marks": {"table": [-2.5, 0.8, 0.0], "franck": [-1.6, 0.0, 0.0], "clara": [-3.4, 0.0, 0.0], "alex": [-2.5, 0.0, -0.9], "window": [0, 1.2, 3.3]}, "spawn": [0, 0, 2.6]},
	"amboise": {"size": [9.0, 8.0, 3.0], "wall": [0.5, 0.52, 0.5], "floor": [0.3, 0.32, 0.3], "look": "lab", "light": [0.6, 0.8, 1.0],
		"furn": [["cabinet", -3.5, -3.6, 0], ["cabinet", -2.0, -3.6, 0], ["cabinet", 2.0, -3.6, 0], ["server", 3.6, -3.4, 0], ["pc", 0.0, -3.4, 0], ["desk", -3.4, 1.0, 90], ["boxes", 3.0, 2.8, 0], ["crate", -3.8, 3.0, 0]],
		"marks": {"file": [-2.0, 1.15, -3.6], "phone_log": [-3.4, 0.85, 1.0], "terminal": [0, 1.1, -3.4], "room": [0, 0.0, -2.0]}, "spawn": [0, 0, 3.2]},
	"emilie": {"size": [4.5, 4.0, 2.6], "wall": [0.55, 0.5, 0.7], "floor": [0.4, 0.3, 0.3], "look": "cold", "light": [0.5, 0.6, 1.0],
		"furn": [["bed", -1.5, -1.3, 0], ["desk", 1.4, -1.6, 0], ["chair", 1.4, -0.9, 180], ["rug", 0, 0.4, 0], ["plant", 1.8, 1.4, 0]],
		"marks": {"emilie": [0.2, 0.0, 0.2], "alex": [-0.6, 0.0, 0.9], "drawings": [1.4, 1.1, -1.95], "bed": [-1.5, 0.6, -1.3], "desk": [1.4, 0.85, -1.6]}, "spawn": [0, 0, 1.5]},
	"train": {"size": [3.2, 14.0, 2.6], "wall": [0.65, 0.65, 0.7], "floor": [0.25, 0.27, 0.32], "look": "winter", "light": [1.0, 1.0, 0.95],
		"furn": [["seat", -0.9, -4.0, 90], ["seat", 0.9, -4.0, -90], ["seat", -0.9, -2.0, 90], ["seat", 0.9, -2.0, -90], ["seat", -0.9, 0.0, 90], ["seat", 0.9, 0.0, -90], ["seat", -0.9, 2.0, 90], ["seat", 0.9, 2.0, -90]],
		"marks": {"clara": [0.9, 0.0, -2.0], "alex": [0.9, 0.0, -1.0], "seat": [-0.9, 0.5, 0.0], "window": [-1.55, 1.3, -1.0]}, "spawn": [0, 0, 5.5]},
}

static func _interior(stage: Node, id: String, rig) -> Dictionary:
	var I: Dictionary = INTERIORS[id]
	var s: Array = I["size"]
	var w: float = s[0]
	var d: float = s[1]
	var h: float = s[2]
	var wc: Array = I["wall"]
	var fc: Array = I["floor"]
	room(stage, w, d, h, Color(wc[0], wc[1], wc[2]), Color(fc[0], fc[1], fc[2]))
	look(stage, I["look"])
	var lc: Array = I["light"]
	var col := Color(lc[0], lc[1], lc[2])
	World.light(stage, Vector3(0, h - 0.4, 0), col, 1.6, maxf(w, d) * 0.9)
	if d > 10.0:
		World.light(stage, Vector3(0, h - 0.4, -d / 4.0), col, 1.6, d * 0.6)
		World.light(stage, Vector3(0, h - 0.4, d / 4.0), col, 1.6, d * 0.6)
	for f in I["furn"]:
		furniture(stage, f[0], f[1], f[2], f[3] if f.size() > 3 else 0.0)
	rig.bounds = Rect2(-w / 2.0 + 0.4, -d / 2.0 + 0.4, w - 0.8, d - 0.8)
	var sp: Array = I["spawn"]
	return {"spawn": Vector3(sp[0], 0, sp[2]), "yaw": 0.0, "marks": marks_from(I["marks"])}

# ---------- extérieurs et lieux spéciaux ----------
static func _houses(stage: Node, ring: float, count: int, seed_value: int, night := true) -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = seed_value
	for i in count:
		var a := TAU * float(i) / float(count)
		var w := rng.randf_range(7.0, 11.0)
		var h := rng.randf_range(6.0, 10.0)
		var p := Vector3(cos(a) * ring, 0, sin(a) * ring)
		var n := Node3D.new()
		n.position = p
		n.rotation.y = -a + PI / 2.0
		stage.add_child(n)
		var wall := Color(rng.randf_range(0.55, 0.8), rng.randf_range(0.5, 0.72), rng.randf_range(0.4, 0.6))
		World.bx(n, Vector3(0, 0, 0), Vector3(w, h, 7.0), wall, 0.0, true)
		var roof := MeshInstance3D.new()
		var rm := CylinderMesh.new()
		rm.top_radius = 0.0
		rm.bottom_radius = w * 0.75
		rm.height = 3.0
		rm.radial_segments = 4
		roof.mesh = rm
		roof.rotation.y = PI / 4.0
		roof.position.y = h + 1.5
		roof.material_override = World.mat(Color(0.3, 0.17, 0.14))
		n.add_child(roof)
		for r in int(h / 3.0):
			for c in 3:
				var lit := night and rng.randf() < 0.45
				World.bx(n, Vector3(-w / 3.0 + c * w / 3.0, 1.4 + r * 2.8, 3.55), Vector3(1.1, 1.4, 0.08), Color(1.0, 0.8, 0.45) if lit else Color(0.1, 0.13, 0.18), 1.5 if lit else 0.0)

static func _place(stage: Node, rig, with_machine := true) -> Dictionary:
	look(stage, "rain")
	Props.ground(stage)
	World.bx(stage, Vector3(0, 0.01, 0), Vector3(36, 0.04, 30), Color(0.2, 0.2, 0.22))
	_houses(stage, 26.0, 14, 5)
	Props.forest(stage, 31, 90, Rect2(-70, -70, 140, 140), [Rect2(-34, -34, 68, 68)])
	# bar-tabac
	var bar := Node3D.new()
	bar.position = Vector3(0, 0, -13)
	stage.add_child(bar)
	World.bx(bar, Vector3(0, 0, 0), Vector3(14, 5.5, 5), Color(0.6, 0.5, 0.38), 0.0, true)
	World.bx(bar, Vector3(0, 2.0, 2.55), Vector3(10, 1.6, 0.1), Color(1.0, 0.75, 0.4), 1.5)
	World.bx(bar, Vector3(0, 4.6, 2.6), Vector3(7, 0.9, 0.15), Color(0.6, 0.12, 0.12), 1.2)
	World.label(bar, "BAR  TABAC", Vector3(0, 4.6, 2.72), 0.012, Color(1, 0.9, 0.7), 80)
	World.light(bar, Vector3(0, 3.0, 4.0), Color(1.0, 0.75, 0.45), 2.0, 12.0)
	# terrasse : journaux, machine, flipper
	furniture(stage, "crate", -6.0, -9.5, 0)
	World.label(stage, "JOURNAUX", Vector3(-6.0, 1.3, -9.0), 0.004, Color(0.9, 0.9, 0.8), 56)
	World.bx(stage, Vector3(5.5, 0, -10.0), Vector3(1.0, 1.5, 0.6), Color(0.5, 0.1, 0.35), 0.0, true)
	World.label(stage, "HORS SERVICE", Vector3(5.5, 1.7, -9.65), 0.004, Color(1, 0.4, 0.4), 48)
	var mp := Vector3(-3.5, 0, -10.0)
	if with_machine:
		World.bx(stage, mp, Vector3(1.6, 3.0, 1.0), Color(0.12, 0.18, 0.32), 0.0, true)
		World.bx(stage, mp + Vector3(0, 0.9, 0.52), Vector3(1.3, 1.9, 0.05), Color(0.45, 0.75, 1.0), 2.5)
		World.light(stage, mp + Vector3(0, 1.6, 1.4), Color(0.4, 0.7, 1.0), 2.5, 8.0)
		World.label(stage, "INSERTION REQUISE", mp + Vector3(0, 2.75, 0.6), 0.003, Color(0.7, 0.9, 1.0), 56)
	# lampadaires, halle, bancs
	for p in [Vector2(-10, 4), Vector2(10, 4), Vector2(-10, -4), Vector2(10, -4)]:
		World.bx(stage, Vector3(p.x, 0, p.y), Vector3(0.14, 5.0, 0.14), Color(0.12, 0.12, 0.14))
		World.bx(stage, Vector3(p.x, 5.0, p.y), Vector3(0.5, 0.3, 0.5), Color(1.0, 0.85, 0.55), 2.5)
		World.light(stage, Vector3(p.x, 4.6, p.y), Color(1.0, 0.8, 0.5), 2.0, 12.0)
	for i in 3:
		furniture(stage, "bench", -4.0 + i * 4.0, 7.0, 0)
	rig.bounds = Rect2(-16, -9, 32, 24)
	return {"spawn": Vector3(0, 0, 9.5), "yaw": 0.0, "marks": {"machine": mp + Vector3(0, 1.4, 1.2), "bar": Vector3(0, 0, -8.5), "clara": Vector3(3.5, 0, -6.5), "alex": Vector3(5.0, 0, -5.8)}}

static func _forest(stage: Node, rig, id := "forest") -> Dictionary:
	look(stage, "night")
	Props.ground(stage)
	Props.path(stage, 10.0, -50.0, 3.2)
	var clear: Array = [Rect2(-3.0, -50.0, 6.0, 60.0), Rect2(-8.0, -26.0, 16.0, 16.0)]
	Props.forest(stage, 17, 170, Rect2(-45, -75, 90, 95), clear)
	Props.grass(stage, 11, 400, Rect2(-14, -42, 28, 52), [Rect2(-1.4, -50.0, 2.8, 60.0)])
	Props.rocks(stage, 5, 24, Rect2(-30, -60, 60, 70), [Rect2(-3.0, -50.0, 6.0, 60.0)])
	for i in 6:
		Props.lantern(stage, Vector3(1.9 if i % 2 == 0 else -1.9, 0, 4.0 - i * 8.0), Color(1.0, 0.72, 0.38), i % 2 == 0)
	var tree_pos := Vector3(0, 0, -30.0)
	if id == "forest_dream":
		Props.standing_stone(stage, tree_pos + Vector3(3.0, 0, 0), 0.4)
	Props.stump(stage, Vector3(-2.0, 0, -12.0))
	Props.stump(stage, Vector3(-2.0, 0, -32.0))
	rig.bounds = Rect2(-9, -46, 18, 60)
	return {"spawn": Vector3(0, 0, 8.0), "yaw": 0.0, "marks": {"stump": Vector3(-2.0, 0.8, -12.0), "stump2": Vector3(-2.0, 0.8, -32.0), "clearing": Vector3(0, 0, -18.0), "end": Vector3(0, 0, -44.0), "stone": tree_pos + Vector3(3.0, 1.0, 0)}}

static func _cemetery(stage: Node, rig) -> Dictionary:
	look(stage, "rain")
	Props.ground(stage)
	Props.forest(stage, 41, 60, Rect2(-60, -60, 120, 120), [Rect2(-20, -20, 40, 40)])
	Props.path(stage, 14.0, -16.0, 2.4)
	var rng := RandomNumberGenerator.new()
	rng.seed = 8
	for i in 40:
		var gx := rng.randf_range(-15, 15)
		var gz := rng.randf_range(-15, 12)
		if absf(gx) < 2.0:
			continue
		World.bx(stage, Vector3(gx, 0, gz), Vector3(0.7, rng.randf_range(0.8, 1.4), 0.15), Color(0.4, 0.4, 0.43), 0.0, true)
	# tombe de Darius + lampadaire
	World.bx(stage, Vector3(4.0, 0, -8.0), Vector3(1.2, 0.3, 2.2), Color(0.45, 0.45, 0.48), 0.0, true)
	World.bx(stage, Vector3(4.0, 0, -9.3), Vector3(0.9, 1.1, 0.2), Color(0.5, 0.5, 0.53), 0.0, true)
	World.bx(stage, Vector3(4.0, 0.3, -7.6), Vector3(0.8, 0.12, 0.8), Color(0.8, 0.3, 0.4))
	World.bx(stage, Vector3(-3.0, 0, -6.0), Vector3(0.12, 4.5, 0.12), Color(0.12, 0.12, 0.14))
	World.bx(stage, Vector3(-3.0, 4.5, -6.0), Vector3(0.45, 0.28, 0.45), Color(0.4, 0.7, 1.0), 3.0)
	World.light(stage, Vector3(-3.0, 4.0, -6.0), Color(0.4, 0.7, 1.0), 2.5, 10.0)
	rig.bounds = Rect2(-14, -14, 28, 30)
	return {"spawn": Vector3(0, 0, 11.0), "yaw": 0.0, "marks": {"grave": Vector3(4.0, 0.6, -7.0), "lamp": Vector3(-3.0, 2.0, -6.0), "gate": Vector3(0, 0, 13.0), "clara": Vector3(2.0, 0, -5.5), "alex": Vector3(3.2, 0, -5.0), "franck": Vector3(5.5, 0, -7.0)}}

static func _nonlieu(stage: Node, rig, doors: Array) -> Dictionary:
	look(stage, "void")
	World.bx(stage, Vector3(0, -0.1, -15), Vector3(14, 0.2, 60), Color(0.88, 0.9, 0.97), 0.3, true)
	World.bx(stage, Vector3(-7.2, 0, -15), Vector3(0.3, 4.0, 60), Color(0.85, 0.88, 0.95), 0.2, true)
	World.bx(stage, Vector3(7.2, 0, -15), Vector3(0.3, 4.0, 60), Color(0.85, 0.88, 0.95), 0.2, true)
	for i in 14:
		World.bx(stage, Vector3(-2.0 + (i % 2) * 4.0, 3.99, 12.0 - i * 4.2), Vector3(0.1, 0.02, 3.0), Color(0.9, 0.95, 1.0), 3.0)
		World.bx(stage, Vector3(0, 0.0, 12.0 - i * 4.2), Vector3(0.05, 4.0, 0.05), Color(0.3, 0.65, 1.0), 2.5)
	World.light(stage, Vector3(0, 3.5, 0), Color(0.8, 0.9, 1.0), 2.0, 14.0)
	World.light(stage, Vector3(0, 3.5, -22), Color(0.8, 0.9, 1.0), 2.0, 14.0)
	var door_marks := {}
	for i in doors.size():
		var side: int = -1 if i % 2 == 0 else 1
		var z := -2.0 - (i / 2) * 5.0
		var p := Vector3(side * 7.0, 1.1, z)
		World.bx(stage, Vector3(side * 7.0, 0, z), Vector3(0.2, 2.2, 1.3), Color(0.92, 0.94, 1.0), 0.6)
		World.label(stage, str(doors[i]), Vector3(side * 6.85, 1.6, z), 0.008, Color(0.1, 0.12, 0.3), 96).rotation_degrees.y = -90.0 * side
		door_marks[doors[i]] = p
	rig.bounds = Rect2(-6.4, -26, 12.8, 36)
	return {"spawn": Vector3(0, 0, 8.0), "yaw": 0.0, "marks": {"doors": door_marks, "end": Vector3(0, 1.0, -24.0), "center": Vector3(0, 0, -8.0)}}

static func _fire(stage: Node, rig) -> Dictionary:
	look(stage, "fire")
	World.bx(stage, Vector3(0, -0.1, 0), Vector3(36, 0.2, 36), Color(0.05, 0.08, 0.2), 0.4, true)
	_houses(stage, 22.0, 9, 3, false)
	for i in 30:
		var a := TAU * float(i) / 30.0
		World.bx(stage, Vector3(cos(a) * 17.0, 0.0, sin(a) * 17.0), Vector3(0.5, 2.0 + 3.0 * fmod(float(i) * 0.37, 1.0), 0.5), Color(0.2, 0.5, 1.0), 4.0)
		if i % 6 == 0:
			World.light(stage, Vector3(cos(a) * 16.0, 1.0, sin(a) * 16.0), Color(0.2, 0.5, 1.0), 1.0, 5.0)
	World.bx(stage, Vector3(0, 0, 0), Vector3(1.0, 0.1, 1.0), Color(0.5, 0.8, 1.0), 3.0)
	rig.bounds = Rect2(-14, -14, 28, 28)
	return {"spawn": Vector3(0, 0, 10.0), "yaw": 0.0, "marks": {"center": Vector3(0, 0, 0), "kayden": Vector3(0, 0, -11.0), "clara": Vector3(-3, 0, 8.0), "alex": Vector3(3, 0, 8.0)}}

static func _warehouse(stage: Node, rig, room_open := false) -> Dictionary:
	look(stage, "lab")
	room(stage, 20.0, 24.0, 5.0, Color(0.35, 0.37, 0.4), Color(0.22, 0.23, 0.26))
	World.light(stage, Vector3(-5, 4.5, 0), Color(0.6, 0.8, 1.0), 1.8, 14.0)
	World.light(stage, Vector3(5, 4.5, 0), Color(0.6, 0.8, 1.0), 1.8, 14.0)
	for i in 5:
		furniture(stage, "shelf", -7.0, -9.0 + i * 3.2, 90)
		furniture(stage, "shelf", 7.0, -9.0 + i * 3.2, -90)
	for i in 8:
		furniture(stage, "boxes", -3.0 + (i % 4) * 2.0, -5.0 + (i / 4) * 5.0, 0)
	# salle M.13 au fond
	World.bx(stage, Vector3(0, 0, -9.0), Vector3(20, 5, 0.3), Color(0.3, 0.32, 0.36), 0.0, true)
	World.label(stage, "PROGRAMME M.13", Vector3(0, 3.6, -8.8), 0.008, Color(0.5, 0.85, 1.0), 80)
	World.bx(stage, Vector3(0, 0, -8.8), Vector3(1.4, 2.4, 0.2), Color(0.18, 0.2, 0.24), 0.0, not room_open)
	World.bx(stage, Vector3(1.1, 1.4, -8.65), Vector3(0.3, 0.4, 0.05), Color(0.1, 0.1, 0.12), 0.0)
	World.label(stage, "404", Vector3(1.1, 1.4, -8.6), 0.006, Color(0.4, 1.0, 0.5), 64)
	var m13 := Node3D.new()
	stage.add_child(m13)
	room(m13, 14.0, 6.0, 3.5, Color(0.28, 0.3, 0.34), Color(0.18, 0.19, 0.22))
	m13.position = Vector3(0, 0, -13.0)
	World.light(m13, Vector3(0, 3.0, 0), Color(0.6, 0.85, 1.0), 2.0, 9.0)
	furniture(m13, "server", -5.5, -2.0, 0)
	furniture(m13, "server", -4.3, -2.0, 0)
	furniture(m13, "pc", 0.0, -2.2, 0)
	furniture(m13, "cabinet", 4.5, -2.2, 0)
	furniture(m13, "cabinet", 5.8, -2.2, 0)
	rig.bounds = Rect2(-9.4, -15.0, 18.8, 26.0) if room_open else Rect2(-9.4, -8.0, 18.8, 19.0)
	var mk := {"carton": Vector3(-3.0, 1.0, -2.0), "punch": Vector3(-2.2, 1.0, -2.0), "door": Vector3(1.1, 1.4, -8.4), "terminal": Vector3(0, 1.1, -15.2), "cabinet": Vector3(4.5, 1.2, -15.2), "letter": Vector3(5.8, 1.2, -15.2), "screen": Vector3(0, 1.8, -15.9), "room": Vector3(0, 0, -11.0)}
	return {"spawn": Vector3(0, 0, 9.5), "yaw": 0.0, "marks": mk}

static func _caves(stage: Node, rig) -> Dictionary:
	look(stage, "cave")
	World.bx(stage, Vector3(0, -0.1, -10), Vector3(14, 0.2, 40), Color(0.35, 0.3, 0.25), 0.0, true)
	World.bx(stage, Vector3(0, 4.0, -10), Vector3(14, 0.4, 40), Color(0.3, 0.26, 0.22))
	World.bx(stage, Vector3(-7.2, 0, -10), Vector3(0.6, 4.0, 40), Color(0.5, 0.45, 0.38), 0.0, true)
	World.bx(stage, Vector3(7.2, 0, -10), Vector3(0.6, 4.0, 40), Color(0.5, 0.45, 0.38), 0.0, true)
	World.bx(stage, Vector3(0, 0, -30.4), Vector3(14, 4.0, 0.6), Color(0.5, 0.45, 0.38), 0.0, true)
	for i in 8:
		var z := 6.0 - i * 5.0
		World.bx(stage, Vector3(-4.5, 0, z), Vector3(0.7, 4.0, 0.7), Color(0.55, 0.5, 0.42))
		World.bx(stage, Vector3(4.5, 0, z), Vector3(0.7, 4.0, 0.7), Color(0.55, 0.5, 0.42))
		World.light(stage, Vector3(0, 3.2, z), Color(1.0, 0.75, 0.45), 1.6, 8.0)
	for i in 6:
		furniture(stage, "barrel", -6.2, 2.0 - i * 4.5, 0)
	for i in 6:
		World.label(stage, ["JEAN L.", "AMÉLIE R.", "PAUL D.", "SERGE M.", "LOUIS V.", "ROSE T."][i], Vector3(6.85, 1.8, 2.0 - i * 4.5), 0.004, Color(0.85, 0.8, 0.7), 56).rotation_degrees.y = -90.0
	rig.bounds = Rect2(-6.4, -29.5, 12.8, 36)
	return {"spawn": Vector3(0, 0, 4.0), "yaw": 0.0, "marks": {"engraving": Vector3(6.6, 1.5, -3.0), "chamber": Vector3(0, 0, -22.0), "notebook": Vector3(0, 1.0, -26.0), "exit": Vector3(0, 0, -28.5)}}

static func _estate(stage: Node, rig) -> Dictionary:
	look(stage, "warm")
	room(stage, 14.0, 22.0, 4.5, Color(0.42, 0.34, 0.28), Color(0.25, 0.17, 0.12))
	World.light(stage, Vector3(0, 4.0, 6), Color(1.0, 0.8, 0.55), 2.0, 12.0)
	World.light(stage, Vector3(0, 4.0, -2), Color(1.0, 0.8, 0.55), 2.0, 12.0)
	World.light(stage, Vector3(0, 4.0, -9), Color(1.0, 0.8, 0.55), 2.0, 12.0)
	# couloir de photos (mur ouest) : 8 cadres
	for i in 8:
		furniture(stage, "frame", -6.85, 8.0 - i * 2.0, 90)
	# salon : table + poinçon au fond
	furniture(stage, "table", 0.0, -8.0, 0)
	for i in 14:
		var a := TAU * float(i) / 14.0
		var p := Vector3(cos(a) * 2.6, 0, -8.0 + sin(a) * 2.6)
		var n := Node3D.new()
		n.position = p
		stage.add_child(n)
		var c := Color.from_hsv(randf(), 0.25, 0.45)
		World.bx(n, Vector3(0, 0, 0), Vector3(0.5, 1.5, 0.3), c)
		var hd := World.bx(n, Vector3(0, 1.5, 0), Vector3(0.25, 0.28, 0.25), Color(0.7, 0.6, 0.5))
		World.bx(n, Vector3(-0.07, 1.62, -0.13), Vector3(0.04, 0.03, 0.02), Color(0.4, 0.7, 1.0), 4.0)
		World.bx(n, Vector3(0.07, 1.62, -0.13), Vector3(0.04, 0.03, 0.02), Color(0.4, 0.7, 1.0), 4.0)
	furniture(stage, "shelf", 6.4, 2.0, -90)
	World.bx(stage, Vector3(6.85, 1.4, 4.5), Vector3(0.05, 1.6, 3.0), Color(0.7, 0.75, 0.8), 0.4)
	World.label(stage, "CARTE DU RESEAU", Vector3(6.8, 2.4, 4.5), 0.003, Color(0.2, 0.3, 0.5), 56).rotation_degrees.y = -90.0
	rig.bounds = Rect2(-6.5, -10.5, 13.0, 21.0)
	return {"spawn": Vector3(0, 0, 9.5), "yaw": 0.0, "marks": {"gallery": Vector3(-6.0, 1.3, 2.0), "ambroise": Vector3(1.5, 0.0, 3.0), "odile": Vector3(-1.5, 0.0, -2.0), "hall": Vector3(0, 0, 8.0), "map": Vector3(6.4, 1.4, 4.5), "punch_table": Vector3(0, 0.8, -8.0), "stranger": Vector3(4.5, 0.0, -3.5), "library": Vector3(5.0, 0.0, 2.0)}}

static func _vr(stage: Node, rig) -> Dictionary:
	look(stage, "vr")
	World.bx(stage, Vector3(0, -0.1, -8), Vector3(26, 0.2, 40), Color(0.04, 0.06, 0.2), 0.8, true)
	for i in range(-12, 13, 2):
		World.bx(stage, Vector3(i, 0.01, -8), Vector3(0.04, 0.02, 40), Color(0.3, 0.6, 1.0), 2.0)
	for i in range(-28, 12, 2):
		World.bx(stage, Vector3(0, 0.01, i), Vector3(26, 0.02, 0.04), Color(0.3, 0.6, 1.0), 2.0)
	for i in 8:
		var s := 1.5 + fmod(float(i) * 0.7, 1.5)
		World.bx(stage, Vector3(-6 if i % 2 == 0 else 6, 0, -2 - i * 3.0), Vector3(2.0, s * 2.0, 2.0), Color.from_hsv(0.58 + 0.03 * float(i), 0.7, 0.8), 0.8, true)
	# la porte close éclairée de bleu
	World.bx(stage, Vector3(0, 0, -26), Vector3(3.0, 4.0, 0.4), Color(0.1, 0.12, 0.3), 0.5, true)
	World.bx(stage, Vector3(0, 0.0, -25.75), Vector3(1.6, 3.0, 0.1), Color(0.3, 0.6, 1.0), 3.0)
	World.light(stage, Vector3(0, 2.0, -24.5), Color(0.3, 0.6, 1.0), 3.0, 9.0)
	rig.bounds = Rect2(-10, -24, 20, 34)
	return {"spawn": Vector3(0, 0, 6.0), "yaw": 0.0, "marks": {"door": Vector3(0, 1.4, -24.5)}}

static func build(id: String, stage: Node, rig) -> Dictionary:
	rig.bounds = Rect2()
	match id:
		"place":
			return _place(stage, rig)
		"place_empty":
			return _place(stage, rig, false)
		"forest", "forest_dream":
			return _forest(stage, rig, id)
		"cemetery":
			return _cemetery(stage, rig)
		"fire":
			return _fire(stage, rig)
		"warehouse":
			return _warehouse(stage, rig, false)
		"warehouse_open":
			return _warehouse(stage, rig, true)
		"caves":
			return _caves(stage, rig)
		"estate":
			return _estate(stage, rig)
		"vr":
			return _vr(stage, rig)
	if INTERIORS.has(id):
		return _interior(stage, id, rig)
	push_warning("Décor inconnu : " + id)
	return _interior(stage, "clara_room", rig)

static func nonlieu(stage: Node, rig, doors: Array) -> Dictionary:
	rig.bounds = Rect2()
	return _nonlieu(stage, rig, doors)
