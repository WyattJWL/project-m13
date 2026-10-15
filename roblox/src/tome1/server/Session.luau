--!nonstrict
-- État de la partie (un serveur privé = une partie) : joueurs, hôte, instabilité.

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Config = require(Shared.Config)
local Powers = require(Shared.Powers)
local Characters = require(Shared.Characters)
local Remotes = require(Shared.Remotes)

local Session = {
	players = {}, -- [Player] = données
	mode = "solo",
	partyCode = nil,
	host = nil,
	instability = 0,
	sceneId = nil,
	flags = {},
}

local function newStates()
	return {
		shieldUntil = 0,
		shieldRemaining = 0,
		stored = 0,
		storedUntil = 0,
		deflectUntil = 0,
		lastPower = -100,
		lastAttack = 0,
	}
end

function Session.register(player: Player)
	local join = player:GetJoinData()
	local resolved = Characters.resolve(join and join.TeleportData, Powers)
	local data = {
		player = player,
		character = resolved,
		displayName = resolved.name,
		power = resolved.power,
		states = newStates(),
	}
	Session.players[player] = data
	if Session.host == nil then
		Session.host = player
		Session.mode = resolved.mode
		Session.partyCode = resolved.partyCode
	end
	return data
end

function Session.remove(player: Player)
	Session.players[player] = nil
	if Session.host == player then
		Session.host = nil
		for other in Session.players do
			Session.host = other
			break
		end
	end
end

function Session.get(player: Player)
	return Session.players[player]
end

function Session.isHost(player: Player): boolean
	return Session.host == player
end

function Session.resetStates(player: Player)
	local data = Session.players[player]
	if data then
		data.states = newStates()
	end
end

function Session.humanoid(player: Player)
	local character = player.Character
	return character and character:FindFirstChildOfClass("Humanoid")
end

function Session.root(player: Player)
	local character = player.Character
	return character and character:FindFirstChild("HumanoidRootPart")
end

-- Joueurs vivants (avec personnage, santé > 0).
function Session.alivePlayers()
	local list = {}
	for player in Session.players do
		local humanoid = Session.humanoid(player)
		local root = Session.root(player)
		if humanoid and root and humanoid.Health > 0 then
			table.insert(list, player)
		end
	end
	return list
end

function Session.count(): number
	local n = 0
	for _ in Session.players do
		n += 1
	end
	return n
end

function Session.addInstability(amount: number)
	Session.instability = math.clamp(Session.instability + amount, 0, Config.Instability.Max)
end

function Session.sendState(target: Player?, payload)
	local remote = Remotes.get("Game_State")
	if target then
		remote:FireClient(target, payload)
	else
		remote:FireAllClients(payload)
	end
end

function Session.notify(player: Player, text: string)
	Remotes.get("Game_Notify"):FireClient(player, text)
end

function Session.notifyAll(text: string)
	Remotes.get("Game_Notify"):FireAllClients(text)
end

Players.PlayerRemoving:Connect(function(player)
	Session.remove(player)
end)

return Session
