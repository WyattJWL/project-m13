extends RefCounted
# Bruitages synthétisés au démarrage (aucun fichier audio) : clics, pas, vent, grillons, pouvoir, etc.
# Sfx.play(parent, "nom", position?, volume_db) joue un son et le supprime à la fin.

const RATE := 16000
static var cache: Dictionary = {}

static func _make(n: int, loop := false) -> PackedByteArray:
	var b := PackedByteArray()
	b.resize(n * 2)
	return b

static func _stream(data: PackedByteArray, loop: bool) -> AudioStreamWAV:
	var s := AudioStreamWAV.new()
	s.format = AudioStreamWAV.FORMAT_16_BITS
	s.mix_rate = RATE
	s.stereo = false
	s.data = data
	if loop:
		s.loop_mode = AudioStreamWAV.LOOP_FORWARD
		s.loop_begin = 0
		s.loop_end = data.size() / 2
	return s

static func _put(b: PackedByteArray, i: int, v: float) -> void:
	b.encode_s16(i * 2, int(clampf(v, -1.0, 1.0) * 32000.0))

# Génère un son à partir d'une fonction f(t, i, n) -> échantillon.
static func _gen(seconds: float, f: Callable, loop := false) -> AudioStreamWAV:
	var n := int(RATE * seconds)
	var b := _make(n)
	for i in n:
		_put(b, i, f.call(float(i) / RATE, i, n))
	return _stream(b, loop)

static func get_sound(name: String) -> AudioStreamWAV:
	if cache.has(name):
		return cache[name]
	var rng := RandomNumberGenerator.new()
	rng.seed = name.hash()
	var st := [0.0]    # état partagé par les fonctions (filtre passe-bas)
	var secs := 0.05
	var looped := false
	var f: Callable
	match name:
		"tick":
			secs = 0.03
			f = func(t, i, n): return sin(TAU * 2600.0 * t) * exp(-t * 140.0) * 0.4
		"click":
			secs = 0.07
			f = func(t, i, n): return (sin(TAU * 900.0 * t) + sin(TAU * 1400.0 * t) * 0.5) * exp(-t * 60.0) * 0.6
		"pickup":
			secs = 0.22
			f = func(t, i, n): return sin(TAU * (500.0 + 700.0 * t / 0.22) * t) * (1.0 - t / 0.22) * 0.5
		"page":
			secs = 0.35
			f = func(t, i, n):
				st[0] = st[0] * 0.6 + rng.randf_range(-1.0, 1.0) * 0.4
				return st[0] * sin(PI * t / 0.35) * 0.5
		"whoosh":
			secs = 0.3
			f = func(t, i, n):
				st[0] = st[0] * 0.85 + rng.randf_range(-1.0, 1.0) * 0.15
				return st[0] * sin(PI * t / 0.3) * 1.6
		"hit":
			secs = 0.22
			f = func(t, i, n):
				st[0] = st[0] * 0.7 + rng.randf_range(-1.0, 1.0) * 0.3
				return (sin(TAU * 85.0 * t) * 0.9 + st[0] * 0.5) * exp(-t * 22.0)
		"power":
			secs = 0.7
			f = func(t, i, n): return (sin(TAU * (260.0 + 900.0 * t) * t) + sin(TAU * (390.0 + 1350.0 * t) * t) * 0.4) * sin(PI * t / 0.7) * 0.5
		"shield":
			secs = 0.5
			f = func(t, i, n): return (sin(TAU * 140.0 * t) * 0.5 + sin(TAU * 210.0 * t) * 0.25) * sin(PI * t / 0.5)
		"ready":
			secs = 0.35
			f = func(t, i, n): return sin(TAU * (1500.0 if t < 0.15 else 2000.0) * t) * exp(-fmod(t, 0.17) * 18.0) * 0.45
		"hurt":
			secs = 0.5
			f = func(t, i, n): return (sin(TAU * (160.0 - 90.0 * t) * t) * 0.8 + rng.randf_range(-0.3, 0.3)) * exp(-t * 6.0)
		"step":
			secs = 0.14
			f = func(t, i, n):
				st[0] = st[0] * 0.8 + rng.randf_range(-1.0, 1.0) * 0.2
				return (st[0] * 1.2 + sin(TAU * 70.0 * t) * 0.6) * exp(-t * 30.0)
		"key_in":
			secs = 0.12
			f = func(t, i, n): return (sin(TAU * 3200.0 * t) * 0.4 + sin(TAU * 4700.0 * t) * 0.25) * exp(-t * 55.0)
		"key_turn":
			secs = 0.2
			f = func(t, i, n): return sin(TAU * 1800.0 * t) * exp(-fmod(t, 0.05) * 90.0) * 0.5
		"unlock":
			secs = 0.25
			f = func(t, i, n): return (sin(TAU * 600.0 * t) * 0.6 + sin(TAU * 1900.0 * t) * 0.4) * exp(-t * 30.0)
		"creak":
			secs = 0.7
			f = func(t, i, n):
				var fr := 130.0 + 40.0 * sin(t * 9.0)
				return (fmod(t * fr, 1.0) * 2.0 - 1.0) * 0.35 * sin(PI * t / 0.7) * (0.6 + 0.4 * sin(t * 40.0))
		"thud":
			secs = 0.4
			f = func(t, i, n):
				st[0] = st[0] * 0.8 + rng.randf_range(-1.0, 1.0) * 0.2
				return (sin(TAU * 60.0 * t) * 0.9 + st[0] * 0.4) * exp(-t * 11.0)
		"stow":
			secs = 0.12
			f = func(t, i, n): return sin(TAU * 700.0 * t) * exp(-t * 50.0) * 0.5
		"tk_grab":
			secs = 0.4
			f = func(t, i, n): return sin(TAU * (300.0 + sin(t * 40.0) * 60.0 + 400.0 * t) * t) * sin(PI * t / 0.4) * 0.45
		"whisper":
			secs = 1.2
			f = func(t, i, n):
				st[0] = st[0] * 0.9 + rng.randf_range(-1.0, 1.0) * 0.1
				return st[0] * sin(PI * t / 1.2) * 1.2 * (0.6 + 0.4 * sin(t * 25.0))
		"wind":
			secs = 4.0
			looped = true
			f = func(t, i, n):
				st[0] = st[0] * 0.97 + rng.randf_range(-1.0, 1.0) * 0.03
				var fade: float = minf(1.0, minf(float(i) / 800.0, float(n - i) / 800.0))
				return st[0] * 2.4 * (0.6 + 0.4 * sin(t * 1.6)) * fade
		"crickets":
			secs = 3.0
			looped = true
			f = func(t, i, n):
				var gate: float = maxf(0.0, sin(TAU * 7.0 * t)) * (0.5 + 0.5 * sin(TAU * 1.0 * t))
				return sin(TAU * 3900.0 * t) * gate * 0.12
		"drone":
			secs = 8.0
			looped = true
			f = func(t, i, n): return (sin(TAU * 55.0 * t) * 0.4 + sin(TAU * 55.5 * t) * 0.4 + sin(TAU * 82.5 * t) * 0.2) * 0.5
		_:
			f = func(t, i, n): return 0.0
	var s := _gen(secs, f, looped)
	cache[name] = s
	return s

static func play(parent: Node, name: String, pos = null, volume_db := 0.0) -> void:
	if parent == null or not parent.is_inside_tree():
		return
	var stream := get_sound(name)
	if pos != null:
		var p3 := AudioStreamPlayer3D.new()
		p3.stream = stream
		p3.volume_db = volume_db
		p3.unit_size = 4.0
		p3.max_distance = 40.0
		parent.add_child(p3)
		p3.global_position = pos
		p3.finished.connect(p3.queue_free)
		p3.play()
	else:
		var p2 := AudioStreamPlayer.new()
		p2.stream = stream
		p2.volume_db = volume_db
		parent.add_child(p2)
		p2.finished.connect(p2.queue_free)
		p2.play()

# Son en boucle (ambiance). Renvoie le lecteur pour pouvoir l'arrêter.
static func loop(parent: Node, name: String, volume_db := -12.0) -> AudioStreamPlayer:
	var p := AudioStreamPlayer.new()
	p.stream = get_sound(name)
	p.volume_db = volume_db
	parent.add_child(p)
	p.play()
	return p

static func ambience(parent: Node) -> void:
	loop(parent, "wind", -14.0)
	loop(parent, "crickets", -22.0)
	loop(parent, "drone", -20.0)
