--!nonstrict
-- Modèles 3D des ennemis (blocs simples). Aucun lien avec le reste du jeu : testable seul.

local EnemyModels = {}

function EnemyModels.block(parent, name, size, position, color, material, shape)
	local p = Instance.new("Part")
	p.Name = name
	p.Size = size
	p.Position = position
	p.Color = color
	p.Material = material or Enum.Material.SmoothPlastic
	p.Anchored = true
	p.CanCollide = false
	p.CanTouch = false
	p.TopSurface = Enum.SurfaceType.Smooth
	p.BottomSurface = Enum.SurfaceType.Smooth
	if shape then
		p.Shape = shape
	end
	p.Parent = parent
	return p
end

local function nameplate(adornee, text, size)
	local billboard = Instance.new("BillboardGui")
	billboard.Size = UDim2.fromOffset(size or 120, 24)
	billboard.StudsOffset = Vector3.new(0, 2.5, 0)
	billboard.AlwaysOnTop = true
	billboard.Parent = adornee
	local label = Instance.new("TextLabel")
	label.Size = UDim2.fromScale(1, 1)
	label.BackgroundTransparency = 1
	label.Text = text
	label.Font = Enum.Font.GothamBold
	label.TextSize = 18
	label.TextColor3 = Color3.fromRGB(255, 255, 255)
	label.TextStrokeTransparency = 0.3
	label.Parent = billboard
end

function EnemyModels.buildSilhouette(parent, position)
	local model = Instance.new("Model")
	model.Name = "Silhouette"
	local body = EnemyModels.block(model, "Body", Vector3.new(2.2, 6.5, 1.2), position, Color3.fromRGB(12, 12, 16))
	body.Transparency = 0.15
	local head = EnemyModels.block(
		model,
		"Head",
		Vector3.new(1.9, 1.9, 1.9),
		position + Vector3.new(0, 4.2, 0),
		Color3.fromRGB(12, 12, 16),
		nil,
		Enum.PartType.Ball
	)
	EnemyModels.block(
		model,
		"Eyes",
		Vector3.new(1.2, 0.25, 0.1),
		position + Vector3.new(0, 4.3, -0.95),
		Color3.fromRGB(240, 245, 255),
		Enum.Material.Neon
	)
	nameplate(head, "Silhouette", 100)
	model.PrimaryPart = body
	model.Parent = parent
	return model, body
end

function EnemyModels.buildBoss(parent, position)
	local model = Instance.new("Model")
	model.Name = "Kayden"
	local body = EnemyModels.block(model, "Body", Vector3.new(5, 13, 3), position, Color3.fromRGB(10, 14, 40))
	body.Transparency = 0.1
	local head = EnemyModels.block(
		model,
		"Head",
		Vector3.new(4, 4, 4),
		position + Vector3.new(0, 8.5, 0),
		Color3.fromRGB(14, 18, 50),
		nil,
		Enum.PartType.Ball
	)
	local core = EnemyModels.block(
		model,
		"Core",
		Vector3.new(2.4, 2.4, 0.6),
		position + Vector3.new(0, 2, -1.7),
		Color3.fromRGB(110, 190, 255),
		Enum.Material.Neon
	)
	local light = Instance.new("PointLight")
	light.Color = Color3.fromRGB(110, 190, 255)
	light.Range = 30
	light.Brightness = 3
	light.Parent = core
	nameplate(head, "Kayden", 140)
	model.PrimaryPart = body
	model.Parent = parent
	return model, body
end

return EnemyModels
