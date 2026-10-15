--!nonstrict
-- Point d'entrée du serveur de jeu (Tome 1). Un serveur privé = une partie.
-- Les données du personnage arrivent par TeleportData depuis le lobby.
-- En Studio (pas de téléportation), on joue Darius en solo.

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Config = require(Shared.Config)
local Characters = require(Shared.Characters)
local Remotes = require(Shared.Remotes)

Remotes.init()

local Session = require(script.Parent.Session)
local EnemyService = require(script.Parent.EnemyService)
local PowerService = require(script.Parent.PowerService)
local GlitchService = require(script.Parent.GlitchService)
local StoryService = require(script.Parent.StoryService)

Players.RespawnTime = 5

EnemyService.start()
PowerService.start()
GlitchService.start()
StoryService.start()

local function applyAppearance(player: Player, character: Model)
	local data = Session.get(player)
	if not data then
		return
	end
	local humanoid = character:WaitForChild("Humanoid", 10)
	if not humanoid then
		return
	end
	humanoid.DisplayName = data.displayName
	humanoid.MaxHealth = Config.StartingHealth
	humanoid.Health = Config.StartingHealth
	humanoid.WalkSpeed = 16

	local rgb = Characters.Palette[data.character.colorIndex] or Characters.Palette[1]
	local color = Color3.fromRGB(rgb[1], rgb[2], rgb[3])
	local bodyColors = character:FindFirstChildOfClass("BodyColors")
	if not bodyColors then
		bodyColors = Instance.new("BodyColors")
		bodyColors.Parent = character
	end
	bodyColors.TorsoColor3 = color
	bodyColors.LeftArmColor3 = color
	bodyColors.RightArmColor3 = color
end

local function onCharacter(player: Player, character: Model)
	Session.resetStates(player)
	applyAppearance(player, character)
	-- L'apparence Roblox se charge un peu plus tard : on ré-applique la couleur.
	task.delay(2, function()
		if character.Parent then
			applyAppearance(player, character)
		end
	end)
end

local function onPlayer(player: Player)
	Session.register(player)
	player.CharacterAdded:Connect(function(character)
		onCharacter(player, character)
	end)
	if player.Character then
		onCharacter(player, player.Character)
	end
	-- Laisse le temps au client de charger ses scripts avant d'envoyer l'état.
	task.delay(3, function()
		if player.Parent then
			StoryService.onPlayerReady(player)
		end
	end)
end

Players.PlayerAdded:Connect(onPlayer)
for _, player in Players:GetPlayers() do
	task.spawn(onPlayer, player)
end

-- Chute dans le vide (glitch majeur) : le joueur réapparaît au spawn.
RunService.Heartbeat:Connect(function()
	for player in Session.players do
		local root = Session.root(player)
		local humanoid = Session.humanoid(player)
		if root and humanoid and humanoid.Health > 0 and root.Position.Y < -30 then
			humanoid.Health = 0
		end
	end
end)
