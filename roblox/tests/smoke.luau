--!nocheck
-- Test de fumée : exécute vraiment la génération des décors et des modèles d'ennemis
-- avec les vrais types Roblox (Instance, Vector3, CFrame...) fournis par Lune.
-- Lance avec : lune run tests/smoke

local fs = require("@lune/fs")
local process = require("@lune/process")

local PRELUDE = [[
local task = require("@lune/task")
local __env = require("../_env")
local game, Instance, Vector3, Vector2, CFrame, Color3, Enum = __env.game, __env.Instance, __env.Vector3, __env.Vector2, __env.CFrame, __env.Color3, __env.Enum
local UDim, UDim2, NumberRange, NumberSequence, ColorSequence, Random = __env.UDim, __env.UDim2, __env.NumberRange, __env.NumberSequence, __env.ColorSequence, __env.Random
]]

-- Copie un module du jeu dans tests/.gen avec l'environnement Roblox en en-tête.
local function generate(sourcePath, name)
	if not fs.isDir("tests/.gen") then
		fs.writeDir("tests/.gen")
	end
	fs.writeFile("tests/.gen/" .. name .. ".luau", PRELUDE .. fs.readFile(sourcePath))
end

generate("src/tome1/server/WorldBuilder.luau", "WorldBuilder")
generate("src/tome1/server/EnemyModels.luau", "EnemyModels")

local env = require("./_env")
local WorldBuilder = require("./.gen/WorldBuilder")
local EnemyModels = require("./.gen/EnemyModels")

local passed, failed = 0, 0
local function test(name, fn)
	local ok, err = pcall(fn)
	if ok then
		passed += 1
		print("  ok   " .. name)
	else
		failed += 1
		print("  FAIL " .. name .. "\n       " .. tostring(err))
	end
end

local workspace = env.game:GetService("Workspace")

local function countClass(root, className)
	local n = 0
	for _, descendant in root:GetDescendants() do
		if descendant.ClassName == className then
			n += 1
		end
	end
	return n
end

print("Décors")
test("Scène 1 (Miel) : 3 interactions et un spawn", function()
	local handles = WorldBuilder.buildMiel()
	assert(handles.machinePrompt and handles.claraPrompt and handles.alexPrompt, "prompts manquants")
	assert(workspace:FindFirstChild("M13Spawn"), "spawn manquant")
	local scene = workspace:FindFirstChild("M13Scene")
	assert(scene, "scène manquante")
	assert(countClass(scene, "ProximityPrompt") == 3, "3 ProximityPrompt attendus")
	assert(scene:FindFirstChild("Distributeur"), "distributeur manquant")
end)

test("Scène 2 (Non-lieu) : 12 portes dont la 41, 14 dalles", function()
	local handles = WorldBuilder.buildNonLieu()
	assert(#handles.doors == 12, "12 portes attendues")
	assert(#handles.tiles == 14, "14 dalles attendues")
	local found41, seen = 0, {}
	for _, door in handles.doors do
		if door.number == 41 then
			found41 += 1
		end
		assert(not seen[door.number], "numéro en double : " .. door.number)
		seen[door.number] = true
		assert(door.prompt and door.part, "porte incomplète")
	end
	assert(found41 == 1, "la porte 41 doit exister une fois")
	assert(#handles.enemySpawns >= 3, "points d'apparition manquants")
end)

test("Scène 3 (Kayden) : arène de 25 dalles et point d'apparition du boss", function()
	local handles = WorldBuilder.buildKayden()
	assert(#handles.tiles == 25, "25 dalles attendues")
	assert(handles.bossSpawn, "bossSpawn manquant")
end)

test("changer de scène supprime l'ancienne", function()
	WorldBuilder.buildMiel()
	WorldBuilder.buildKayden()
	local count = 0
	for _, child in workspace:GetChildren() do
		if child.Name == "M13Scene" then
			count += 1
		end
	end
	assert(count == 1, "une seule scène à la fois")
end)

print("Ennemis")
test("Silhouette : modèle complet", function()
	local folder = env.Instance.new("Folder")
	local model, body = EnemyModels.buildSilhouette(folder, env.Vector3.new(0, 3, 0))
	assert(model.PrimaryPart == body, "PrimaryPart")
	assert(model.Parent == folder, "parent")
	assert(model:FindFirstChild("Head") and model:FindFirstChild("Eyes"), "pièces manquantes")
end)

test("Kayden : modèle complet avec lumière", function()
	local folder = env.Instance.new("Folder")
	local model, body = EnemyModels.buildBoss(folder, env.Vector3.new(0, 6, -30))
	assert(model.PrimaryPart == body, "PrimaryPart")
	assert(countClass(model, "PointLight") == 1, "lumière du cœur")
end)

-- Nettoyage : détruit la scène (arrête aussi la boucle de la lampe bleue).
WorldBuilder.clear()
local scene = workspace:FindFirstChild("M13Scene")
if scene then
	scene:Destroy()
end

print("")
print(string.format("%d réussi(s), %d échec(s)", passed, failed))
process.exit(failed > 0 and 1 or 0)
