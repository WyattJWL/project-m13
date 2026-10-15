--!nonstrict
-- L'histoire du Tome 1 : trois scènes (Miel, le Non-lieu, Kayden), les dialogues et la fin de partie.
-- Les dialogues sont lus dans Shared/Dialogue/Tome1 (données pures, testées).

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")
local TeleportService = game:GetService("TeleportService")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Config = require(Shared.Config)
local PlaceIds = require(Shared.PlaceIds)
local Remotes = require(Shared.Remotes)
local Graph = require(Shared.Dialogue.Tome1)
local DialogueGraph = require(Shared.DialogueGraph)

local Session = require(script.Parent.Session)
local WorldBuilder = require(script.Parent.WorldBuilder)
local EnemyService = require(script.Parent.EnemyService)
local GlitchService = require(script.Parent.GlitchService)

local StoryService = {}

local current = {} -- [Player] = id du noeud de dialogue affiché
local sceneHandles = nil
local transitioning = false
local waveToken = 0
local bossMidSaid = false

local OBJECTIVES = {
	miel = "Parle à Clara et Alex, puis lis l'étiquette du distributeur.",
	nonlieu = "Trouve la porte 41. Les autres portes mentent, et des Silhouettes rôdent.",
	kayden = "Vaincs Kayden. Clic : attaque. Q : ton pouvoir.",
}

---------------------------------------------------------------------------
-- Dialogues
---------------------------------------------------------------------------
local function closeDialogue(player: Player)
	current[player] = nil
	Remotes.get("Game_DialogueClose"):FireClient(player)
end

local function applyEffect(player: Player, effect: string?)
	if not effect then
		return
	end
	local scene = string.match(effect, "^scene:(.+)$")
	if scene then
		if Session.isHost(player) then
			StoryService.goto(scene)
		else
			Session.notify(player, "Seul l'hôte du groupe peut insérer l'année.")
		end
		return
	end
	if effect == "flag:finished" then
		StoryService.finish()
	end
end

function StoryService.say(player: Player, nodeId: string)
	local node = Graph.nodes[nodeId]
	if not node then
		warn("[M13] Noeud de dialogue inconnu : " .. tostring(nodeId))
		return
	end
	current[player] = nodeId
	local choices = nil
	if node.choices then
		choices = {}
		for _, choice in node.choices do
			table.insert(choices, choice.text)
		end
	end
	Remotes.get("Game_Dialogue"):FireClient(player, {
		id = nodeId,
		speaker = node.speaker,
		text = node.text,
		choices = choices,
		canContinue = (node.next ~= nil) or (choices == nil),
	})
end

function StoryService.sayAll(nodeId: string)
	for player in Session.players do
		StoryService.say(player, nodeId)
	end
end

local function onAdvance(player: Player, nodeId)
	if current[player] ~= nodeId then
		return
	end
	local node = Graph.nodes[nodeId]
	if not node or node.choices then
		return
	end
	if node.next then
		StoryService.say(player, node.next)
	else
		closeDialogue(player)
		applyEffect(player, node.effect)
	end
end

local function onChoice(player: Player, nodeId, index)
	if current[player] ~= nodeId or typeof(index) ~= "number" then
		return
	end
	local node = Graph.nodes[nodeId]
	if not node or not node.choices then
		return
	end
	local choice = node.choices[math.floor(index)]
	if not choice then
		return
	end
	if choice.next then
		StoryService.say(player, choice.next)
	else
		closeDialogue(player)
	end
	applyEffect(player, choice.effect)
end

---------------------------------------------------------------------------
-- Scènes
---------------------------------------------------------------------------
local function teleportPlayersToSpawn(spawn: CFrame)
	local index = 0
	for _, player in Session.alivePlayers() do
		local character = player.Character
		if character then
			index += 1
			local offset = Vector3.new(((index - 1) % 4) * 4 - 6, 3, 0)
			character:PivotTo(spawn + offset)
		end
	end
end

local function startWaves(maxAlive: number, interval: number, spawns)
	waveToken += 1
	local token = waveToken
	task.spawn(function()
		while token == waveToken and Session.sceneId == "nonlieu" do
			if EnemyService.livingCount() < maxAlive and #Session.alivePlayers() > 0 then
				local point = spawns[math.random(1, #spawns)]
				EnemyService.spawn("silhouette", point)
			end
			task.wait(interval)
		end
	end)
end

local function setupMiel()
	local handles = WorldBuilder.buildMiel()
	handles.machinePrompt.Triggered:Connect(function(player)
		StoryService.say(player, "machine_label")
	end)
	handles.claraPrompt.Triggered:Connect(function(player)
		StoryService.say(player, "clara_1")
	end)
	handles.alexPrompt.Triggered:Connect(function(player)
		StoryService.say(player, "alex_1")
	end)
	GlitchService.setTiles({})
	return handles
end

local function setupNonLieu()
	local handles = WorldBuilder.buildNonLieu()
	GlitchService.setTiles(handles.tiles)
	local opened = false
	for _, door in handles.doors do
		door.prompt.Triggered:Connect(function(player)
			if opened or transitioning then
				return
			end
			if door.number == 41 then
				opened = true
				door.part.Transparency = 0.8
				door.part.CanCollide = false
				StoryService.sayAll("door_41")
				task.delay(4, function()
					if Session.sceneId == "nonlieu" then
						StoryService.goto("kayden")
					end
				end)
			else
				door.prompt.Enabled = false
				Session.addInstability(10)
				StoryService.say(player, "door_wrong")
				for _ = 1, 2 do
					local point = handles.enemySpawns[math.random(1, #handles.enemySpawns)]
					EnemyService.spawn("silhouette", point)
				end
			end
		end)
	end
	startWaves(5, 14, handles.enemySpawns)
	for _ = 1, 2 do
		EnemyService.spawn("silhouette", handles.enemySpawns[math.random(1, #handles.enemySpawns)])
	end
	return handles
end

local function setupKayden()
	local handles = WorldBuilder.buildKayden()
	GlitchService.setTiles(handles.tiles)
	bossMidSaid = false
	task.delay(2, function()
		if Session.sceneId == "kayden" then
			EnemyService.spawn("boss", handles.bossSpawn)
			StoryService.sayAll("kayden_intro")
		end
	end)
	return handles
end

local SCENES = {
	miel = setupMiel,
	nonlieu = setupNonLieu,
	kayden = setupKayden,
}

function StoryService.goto(sceneId: string)
	if transitioning or not SCENES[sceneId] or Session.sceneId == sceneId then
		return
	end
	transitioning = true
	Session.sendState(nil, { fade = true })
	task.wait(1.2)

	waveToken += 1
	EnemyService.clear()
	for player in Session.players do
		if current[player] then
			closeDialogue(player)
		end
	end

	Session.sceneId = sceneId
	sceneHandles = SCENES[sceneId]()
	teleportPlayersToSpawn(sceneHandles.spawn)
	Session.sendState(nil, { objective = OBJECTIVES[sceneId], scene = sceneId, boss = false })
	task.wait(0.4)
	Session.sendState(nil, { fade = false })
	transitioning = false

	if sceneId == "miel" then
		task.delay(1.5, function()
			StoryService.sayAll("narr_pluie")
		end)
	elseif sceneId == "nonlieu" then
		task.delay(1.0, function()
			StoryService.sayAll("nonlieu_intro")
		end)
	end
end

---------------------------------------------------------------------------
-- Fin de partie
---------------------------------------------------------------------------
function StoryService.finish()
	if Session.flags.finished then
		return
	end
	Session.flags.finished = true
	Session.sendState(nil, {
		finished = true,
		summary = "Page 41 récupérée. Fin du Tome 1.",
	})
	task.delay(15, function()
		if PlaceIds.Lobby ~= 0 and not RunService:IsStudio() then
			local players = Players:GetPlayers()
			if #players > 0 then
				pcall(function()
					TeleportService:TeleportAsync(PlaceIds.Lobby, players)
				end)
			end
		end
	end)
end

---------------------------------------------------------------------------
-- Démarrage et joueurs
---------------------------------------------------------------------------
function StoryService.onPlayerReady(player: Player)
	local data = Session.get(player)
	local def = require(Shared.Powers).Definitions[data.power]
	Session.sendState(player, {
		mode = Session.mode,
		partyCode = Session.partyCode,
		name = data.displayName,
		power = { id = def.id, name = def.name, cooldown = def.cooldown, color = def.color },
		objective = Session.sceneId and OBJECTIVES[Session.sceneId] or nil,
		instability = Session.instability,
		instabilityMax = Config.Instability.Max,
	})
	if Session.sceneId == nil then
		StoryService.goto("miel")
	elseif Session.sceneId == "miel" then
		task.delay(1.5, function()
			StoryService.say(player, "narr_pluie")
		end)
	end
end

function StoryService.start()
	local problems = DialogueGraph.validate(Graph)
	for _, problem in problems do
		warn("[M13] Dialogue : " .. problem)
	end

	-- Le décor existe dès le démarrage du serveur : personne ne tombe dans le vide à l'arrivée.
	task.spawn(function()
		StoryService.goto("miel")
	end)

	Remotes.get("Game_DialogueAdvance").OnServerEvent:Connect(onAdvance)
	Remotes.get("Game_DialogueChoice").OnServerEvent:Connect(onChoice)

	EnemyService.onKilled = function(enemy, byPlayer)
		Session.addInstability(2)
		if enemy.kind == "boss" then
			Session.sendState(nil, { boss = false })
			StoryService.sayAll("kayden_defeat")
			-- Si personne ne ferme le dialogue, la fin de partie démarre quand même.
			task.delay(12, function()
				StoryService.finish()
			end)
		end
	end
	EnemyService.onBossHealth = function(hp, maxHp)
		Session.sendState(nil, { boss = { hp = hp, max = maxHp } })
		if not bossMidSaid and hp > 0 and hp <= maxHp / 2 then
			bossMidSaid = true
			StoryService.sayAll("kayden_mid")
		end
	end
end

Players.PlayerRemoving:Connect(function(player)
	current[player] = nil
end)

return StoryService
