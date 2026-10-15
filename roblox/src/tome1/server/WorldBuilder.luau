--!nonstrict
-- Décors générés par le code (blocs simples). Tu pourras les remplacer par de vrais décors
-- dans Roblox Studio : il suffit de garder les mêmes noms et les mêmes ProximityPrompt.
-- Chaque scène renvoie un tableau de « poignées » utilisées par StoryService.

local Lighting = game:GetService("Lighting")
local Workspace = game:GetService("Workspace")

local WorldBuilder = {}

local SCENE_NAME = "M13Scene"
local SPAWN_NAME = "M13Spawn"

local function part(parent, name, size, cframe, color, material, extra)
	local p = Instance.new("Part")
	p.Name = name
	p.Size = size
	p.CFrame = cframe
	p.Color = color
	p.Material = material or Enum.Material.SmoothPlastic
	p.Anchored = true
	p.TopSurface = Enum.SurfaceType.Smooth
	p.BottomSurface = Enum.SurfaceType.Smooth
	if extra then
		for key, value in extra do
			p[key] = value
		end
	end
	p.Parent = parent
	return p
end

local function surfaceText(target, text, face, color, font)
	local gui = Instance.new("SurfaceGui")
	gui.Face = face or Enum.NormalId.Front
	gui.SizingMode = Enum.SurfaceGuiSizingMode.PixelsPerStud
	gui.PixelsPerStud = 40
	gui.Parent = target
	local label = Instance.new("TextLabel")
	label.Size = UDim2.fromScale(1, 1)
	label.BackgroundTransparency = 1
	label.Text = text
	label.TextScaled = true
	label.Font = font or Enum.Font.GothamBold
	label.TextColor3 = color or Color3.fromRGB(255, 255, 255)
	label.Parent = gui
	return label
end

local function pointLight(parent, color, range, brightness)
	local light = Instance.new("PointLight")
	light.Color = color
	light.Range = range
	light.Brightness = brightness
	light.Parent = parent
	return light
end

local function prompt(parent, action, object, distance, hold)
	local p = Instance.new("ProximityPrompt")
	p.ActionText = action
	p.ObjectText = object
	p.MaxActivationDistance = distance or 10
	p.HoldDuration = hold or 0
	p.RequiresLineOfSight = false
	p.Parent = parent
	return p
end

---------------------------------------------------------------------------
-- Scène, spawn, lumières
---------------------------------------------------------------------------
function WorldBuilder.clear()
	local old = Workspace:FindFirstChild(SCENE_NAME)
	if old then
		old:Destroy()
	end
	local folder = Instance.new("Folder")
	folder.Name = SCENE_NAME
	folder.Parent = Workspace
	return folder
end

function WorldBuilder.setSpawn(cframe: CFrame)
	local spawnPad = Workspace:FindFirstChild(SPAWN_NAME)
	if not spawnPad then
		spawnPad = Instance.new("SpawnLocation")
		spawnPad.Name = SPAWN_NAME
		spawnPad.Anchored = true
		spawnPad.Size = Vector3.new(10, 1, 10)
		spawnPad.Neutral = true
		spawnPad.Duration = 0
		spawnPad.Transparency = 1
		spawnPad.CanCollide = false
		local decal = spawnPad:FindFirstChildOfClass("Decal")
		if decal then
			decal:Destroy()
		end
		spawnPad.Parent = Workspace
	end
	spawnPad.CFrame = cframe
end

local function effect(className)
	local fx = Lighting:FindFirstChildOfClass(className)
	if not fx then
		fx = Instance.new(className)
		fx.Parent = Lighting
	end
	return fx
end

local function applyLighting(preset)
	Lighting.ClockTime = preset.clock
	Lighting.Brightness = preset.brightness
	Lighting.Ambient = preset.ambient
	Lighting.OutdoorAmbient = preset.ambient
	Lighting.FogColor = preset.fog
	Lighting.FogEnd = preset.fogEnd
	local atmosphere = effect("Atmosphere")
	atmosphere.Density = preset.density
	atmosphere.Color = preset.fog
	local correction = effect("ColorCorrectionEffect")
	correction.Name = "M13Color"
	correction.TintColor = preset.tint
	correction.Saturation = preset.saturation
	correction.Contrast = 0.1
	local bloom = effect("BloomEffect")
	bloom.Intensity = 0.6
	bloom.Threshold = 1.2
end

local function rain(parent, size)
	local emitterPart = part(
		parent,
		"Rain",
		Vector3.new(size, 1, size),
		CFrame.new(0, 60, 0),
		Color3.new(1, 1, 1),
		Enum.Material.SmoothPlastic,
		{ Transparency = 1, CanCollide = false }
	)
	local emitter = Instance.new("ParticleEmitter")
	emitter.Rate = 700
	emitter.Lifetime = NumberRange.new(2, 2.4)
	emitter.Speed = NumberRange.new(50, 60)
	emitter.EmissionDirection = Enum.NormalId.Bottom
	emitter.SpreadAngle = Vector2.new(3, 3)
	emitter.Size = NumberSequence.new(0.15)
	emitter.Color = ColorSequence.new(Color3.fromRGB(170, 190, 220))
	emitter.Transparency = NumberSequence.new(0.5)
	emitter.LightEmission = 0.2
	emitter.Parent = emitterPart
end

local function npc(parent, name, position, color, action)
	local model = Instance.new("Model")
	model.Name = name
	local torso = part(model, "Torso", Vector3.new(2, 3, 1.2), CFrame.new(position + Vector3.new(0, 3.5, 0)), color)
	local head = part(
		model,
		"Head",
		Vector3.new(1.8, 1.8, 1.8),
		CFrame.new(position + Vector3.new(0, 5.8, 0)),
		Color3.fromRGB(235, 200, 170),
		Enum.Material.SmoothPlastic,
		{ Shape = Enum.PartType.Ball }
	)
	part(model, "Legs", Vector3.new(2, 3, 1), CFrame.new(position + Vector3.new(0, 1.5, 0)), Color3.fromRGB(40, 44, 60))
	model.PrimaryPart = torso

	local billboard = Instance.new("BillboardGui")
	billboard.Size = UDim2.fromOffset(120, 28)
	billboard.StudsOffset = Vector3.new(0, 2.2, 0)
	billboard.AlwaysOnTop = true
	billboard.Parent = head
	local label = Instance.new("TextLabel")
	label.Size = UDim2.fromScale(1, 1)
	label.BackgroundTransparency = 1
	label.Text = name
	label.Font = Enum.Font.GothamBold
	label.TextSize = 20
	label.TextColor3 = Color3.fromRGB(255, 255, 255)
	label.TextStrokeTransparency = 0.4
	label.Parent = billboard

	local p = prompt(torso, action, name, 10, 0)
	model.Parent = parent
	return p
end

---------------------------------------------------------------------------
-- Scène 1 : Luynes, sous la pluie
---------------------------------------------------------------------------
function WorldBuilder.buildMiel()
	local scene = WorldBuilder.clear()
	applyLighting({
		clock = 21,
		brightness = 1,
		ambient = Color3.fromRGB(55, 60, 85),
		fog = Color3.fromRGB(70, 78, 100),
		fogEnd = 420,
		density = 0.35,
		tint = Color3.fromRGB(215, 225, 245),
		saturation = -0.15,
	})

	part(
		scene,
		"Ground",
		Vector3.new(260, 2, 260),
		CFrame.new(0, -1, 0),
		Color3.fromRGB(58, 60, 66),
		Enum.Material.Cobblestone
	)
	part(
		scene,
		"Road",
		Vector3.new(260, 0.2, 18),
		CFrame.new(0, 0.05, 28),
		Color3.fromRGB(30, 31, 36),
		Enum.Material.Asphalt
	)

	-- Bar-tabac
	local bar = part(scene, "BarTabac", Vector3.new(34, 18, 22), CFrame.new(0, 9, -48), Color3.fromRGB(150, 118, 88))
	local sign = part(scene, "BarSign", Vector3.new(16, 3, 0.5), CFrame.new(0, 14, -36.8), Color3.fromRGB(20, 20, 24))
	surfaceText(sign, "BAR-TABAC", Enum.NormalId.Front, Color3.fromRGB(255, 120, 90))
	sign.CFrame = CFrame.lookAt(Vector3.new(0, 14, -36.8), Vector3.new(0, 14, -26.8))
	pointLight(bar, Color3.fromRGB(255, 170, 110), 30, 1.2)

	-- Immeubles de la place
	for index, x in { -60, -40, 40, 60 } do
		part(
			scene,
			"Immeuble" .. index,
			Vector3.new(18, 22 + index * 2, 18),
			CFrame.new(x, 11 + index, -20),
			Color3.fromRGB(110 + index * 8, 100, 92)
		)
	end

	-- Réverbères
	for index, x in { -28, -10, 10, 28 } do
		local pole = part(
			scene,
			"LampPole" .. index,
			Vector3.new(0.6, 12, 0.6),
			CFrame.new(x, 6, 10),
			Color3.fromRGB(25, 25, 30)
		)
		local lamp = part(
			scene,
			"Lamp" .. index,
			Vector3.new(1.6, 1.2, 1.6),
			CFrame.new(x, 12.4, 10),
			Color3.fromRGB(255, 220, 150),
			Enum.Material.Neon
		)
		pointLight(lamp, Color3.fromRGB(255, 200, 130), 36, 1.6)
		pole.Name = "LampPole" .. index
	end

	-- Le distributeur
	local machine = Instance.new("Model")
	machine.Name = "Distributeur"
	local body = part(
		machine,
		"Body",
		Vector3.new(6, 10, 3),
		CFrame.new(0, 5, -34),
		Color3.fromRGB(150, 200, 230),
		Enum.Material.Glass,
		{ Transparency = 0.35 }
	)
	pointLight(body, Color3.fromRGB(110, 170, 255), 26, 3)
	local screen = part(
		machine,
		"Screen",
		Vector3.new(4.4, 1.8, 0.3),
		CFrame.new(0, 8.4, -32.4),
		Color3.fromRGB(10, 20, 40),
		Enum.Material.Neon
	)
	surfaceText(screen, "INSERTION REQUISE", Enum.NormalId.Front, Color3.fromRGB(150, 220, 255), Enum.Font.Code)
	screen.CFrame = CFrame.lookAt(Vector3.new(0, 8.4, -32.4), Vector3.new(0, 8.4, -22.4))
	-- Objets en suspension : collier, dent de lait, montre
	part(
		machine,
		"Collier",
		Vector3.new(1.4, 0.3, 1.4),
		CFrame.new(1.4, 1.6, -34),
		Color3.fromRGB(110, 70, 40),
		Enum.Material.Leather,
		{
			Shape = Enum.PartType.Cylinder,
			CanCollide = false,
		}
	)
	part(
		machine,
		"DentDeLait",
		Vector3.new(0.6, 0.6, 0.6),
		CFrame.new(-1.3, 4.2, -34),
		Color3.fromRGB(240, 240, 235),
		Enum.Material.SmoothPlastic,
		{
			Shape = Enum.PartType.Ball,
			CanCollide = false,
		}
	)
	part(
		machine,
		"Montre",
		Vector3.new(0.4, 1.2, 1.2),
		CFrame.new(0.2, 3, -34),
		Color3.fromRGB(190, 190, 200),
		Enum.Material.Metal,
		{
			Shape = Enum.PartType.Cylinder,
			CanCollide = false,
		}
	)
	machine.PrimaryPart = body
	machine.Parent = scene
	local machinePrompt = prompt(body, "Lire l'étiquette", "Distributeur", 12, 0.4)

	local claraPrompt = npc(scene, "Clara", Vector3.new(-12, 0, -8), Color3.fromRGB(255, 190, 80), "Parler")
	local alexPrompt = npc(scene, "Alex", Vector3.new(12, 0, -8), Color3.fromRGB(90, 140, 255), "Parler")

	rain(scene, 260)

	local spawn = CFrame.new(0, 1.5, 24)
	WorldBuilder.setSpawn(spawn)
	return {
		spawn = spawn,
		machinePrompt = machinePrompt,
		claraPrompt = claraPrompt,
		alexPrompt = alexPrompt,
		tiles = {},
	}
end

---------------------------------------------------------------------------
-- Scène 2 : le Non-lieu (couloir blanc aux portes numérotées)
---------------------------------------------------------------------------
local DOOR_NUMBERS = { 7, 12, 19, 23, 28, 33, 41, 46, 52, 58, 63, 77 }

function WorldBuilder.buildNonLieu()
	local scene = WorldBuilder.clear()
	applyLighting({
		clock = 0,
		brightness = 0.6,
		ambient = Color3.fromRGB(190, 200, 235),
		fog = Color3.fromRGB(220, 228, 255),
		fogEnd = 260,
		density = 0.45,
		tint = Color3.fromRGB(225, 235, 255),
		saturation = -0.4,
	})

	local TILE = 14
	local COUNT = 14
	local length = TILE * COUNT
	local tiles = {}
	for index = 1, COUNT do
		local tile = part(
			scene,
			"Tile" .. index,
			Vector3.new(TILE, 1, TILE),
			CFrame.new(0, -0.5, -(index - 1) * TILE),
			Color3.fromRGB(235, 238, 245)
		)
		table.insert(tiles, tile)
	end

	local midZ = -((COUNT - 1) * TILE) / 2
	part(scene, "WallLeft", Vector3.new(1, 14, length), CFrame.new(-7.5, 7, midZ), Color3.fromRGB(205, 210, 222))
	part(scene, "WallRight", Vector3.new(1, 14, length), CFrame.new(7.5, 7, midZ), Color3.fromRGB(205, 210, 222))
	part(scene, "Ceiling", Vector3.new(16, 1, length), CFrame.new(0, 14.5, midZ), Color3.fromRGB(215, 220, 232))
	part(
		scene,
		"WallEnd",
		Vector3.new(16, 14, 1),
		CFrame.new(0, 7, -(length - TILE / 2) - 0.5),
		Color3.fromRGB(205, 210, 222)
	)
	part(scene, "WallStart", Vector3.new(16, 14, 1), CFrame.new(0, 7, TILE / 2 + 0.5), Color3.fromRGB(205, 210, 222))

	-- Lampe bleue qui clignote à l'autre bout (3 s allumée, 1 s éteinte)
	local lamp = part(
		scene,
		"BlueLamp",
		Vector3.new(2, 2, 2),
		CFrame.new(0, 12, -(length - TILE)),
		Color3.fromRGB(110, 170, 255),
		Enum.Material.Neon
	)
	local light = pointLight(lamp, Color3.fromRGB(110, 170, 255), 40, 3)
	task.spawn(function()
		while lamp.Parent do
			light.Enabled = true
			task.wait(3)
			light.Enabled = false
			task.wait(1)
		end
	end)

	-- Portes numérotées, mélangées
	local rng = Random.new()
	local numbers = table.clone(DOOR_NUMBERS)
	for i = #numbers, 2, -1 do
		local j = rng:NextInteger(1, i)
		numbers[i], numbers[j] = numbers[j], numbers[i]
	end

	local doors = {}
	for slot, number in numbers do
		local side = (slot % 2 == 0) and -1 or 1
		local z = -(16 + math.floor((slot - 1) / 2) * 28)
		local position = Vector3.new(side * 7, 5, z)
		local door = part(
			scene,
			"Door" .. number,
			Vector3.new(0.6, 9, 6),
			CFrame.lookAt(position, Vector3.new(0, 5, z)),
			Color3.fromRGB(90, 96, 120)
		)
		surfaceText(door, tostring(number), Enum.NormalId.Front, Color3.fromRGB(255, 255, 255))
		local p = prompt(door, "Ouvrir", "Porte " .. number, 9, 0.3)
		table.insert(doors, { number = number, part = door, prompt = p })
	end

	local spawn = CFrame.new(0, 2, 4)
	WorldBuilder.setSpawn(spawn)
	return {
		spawn = spawn,
		doors = doors,
		tiles = tiles,
		enemySpawns = {
			Vector3.new(0, 3.5, -60),
			Vector3.new(0, 3.5, -100),
			Vector3.new(0, 3.5, -140),
			Vector3.new(0, 3.5, -170),
		},
	}
end

---------------------------------------------------------------------------
-- Scène 3 : l'arène de Kayden
---------------------------------------------------------------------------
function WorldBuilder.buildKayden()
	local scene = WorldBuilder.clear()
	applyLighting({
		clock = 0,
		brightness = 0.4,
		ambient = Color3.fromRGB(35, 30, 70),
		fog = Color3.fromRGB(20, 18, 50),
		fogEnd = 300,
		density = 0.5,
		tint = Color3.fromRGB(200, 190, 255),
		saturation = -0.2,
	})

	local tiles = {}
	for ix = -2, 2 do
		for iz = -2, 2 do
			local tile = part(
				scene,
				"ArenaTile",
				Vector3.new(24, 2, 24),
				CFrame.new(ix * 24, -1, iz * 24),
				Color3.fromRGB(32 + ((ix + iz) % 2) * 8, 34, 58),
				Enum.Material.SmoothPlastic
			)
			table.insert(tiles, tile)
		end
	end

	for index, corner in
		{ Vector3.new(-60, 0, -60), Vector3.new(60, 0, -60), Vector3.new(-60, 0, 60), Vector3.new(60, 0, 60) }
	do
		local pillar = part(
			scene,
			"Pillar" .. index,
			Vector3.new(4, 26, 4),
			CFrame.new(corner + Vector3.new(0, 13, 0)),
			Color3.fromRGB(20, 22, 40),
			Enum.Material.Neon
		)
		pointLight(pillar, Color3.fromRGB(230, 90, 120), 50, 2)
	end

	local spawn = CFrame.new(0, 2, 44)
	WorldBuilder.setSpawn(spawn)
	return {
		spawn = spawn,
		tiles = tiles,
		bossSpawn = Vector3.new(0, 6, -30),
	}
end

return WorldBuilder
