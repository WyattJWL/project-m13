--!nonstrict
-- Création et accès aux RemoteEvent / RemoteFunction.
-- Le serveur crée tout au démarrage (Remotes.init) ; le client attend ce qu'il utilise.

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")

local FOLDER_NAME = "M13Remotes"

local Remotes = {}

-- Nom -> classe
Remotes.All = {
	-- Lobby
	Lobby_StartSolo = "RemoteFunction",
	Lobby_CreateParty = "RemoteFunction",
	Lobby_JoinParty = "RemoteFunction",
	Lobby_Notify = "RemoteEvent",
	-- Jeu (Tome 1)
	Game_UsePower = "RemoteEvent",
	Game_BasicAttack = "RemoteEvent",
	Game_State = "RemoteEvent",
	Game_Fx = "RemoteEvent",
	Game_Glitch = "RemoteEvent",
	Game_Dialogue = "RemoteEvent",
	Game_DialogueAdvance = "RemoteEvent",
	Game_DialogueChoice = "RemoteEvent",
	Game_DialogueClose = "RemoteEvent",
	Game_Notify = "RemoteEvent",
}

function Remotes.init(names: { string }?)
	assert(RunService:IsServer(), "Remotes.init est réservé au serveur")
	local folder = ReplicatedStorage:FindFirstChild(FOLDER_NAME)
	if not folder then
		folder = Instance.new("Folder")
		folder.Name = FOLDER_NAME
		folder.Parent = ReplicatedStorage
	end
	for name, className in Remotes.All do
		local wanted = (names == nil) or table.find(names, name) ~= nil
		if wanted and not folder:FindFirstChild(name) then
			local remote = Instance.new(className)
			remote.Name = name
			remote.Parent = folder
		end
	end
end

function Remotes.get(name: string)
	local folder
	if RunService:IsServer() then
		folder = ReplicatedStorage:FindFirstChild(FOLDER_NAME)
		assert(folder, "Remotes.init doit être appelé avant Remotes.get")
		return folder:FindFirstChild(name) or error("Remote introuvable : " .. name)
	end
	folder = ReplicatedStorage:WaitForChild(FOLDER_NAME)
	return folder:WaitForChild(name)
end

return Remotes
