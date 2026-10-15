--!nonstrict
-- Lobby : choix du mode (solo ou groupe) puis téléportation vers un serveur PRIVÉ du Tome 1.
--  * Solo   : un serveur réservé pour le joueur seul (il joue Darius).
--  * Groupe : un serveur réservé + un code à 4 caractères, stocké dans MemoryStore.
--             Les amis tapent le code dans le lobby et rejoignent le même serveur privé.

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Lighting = game:GetService("Lighting")
local MemoryStoreService = game:GetService("MemoryStoreService")
local RunService = game:GetService("RunService")
local TeleportService = game:GetService("TeleportService")
local TextService = game:GetService("TextService")
local Workspace = game:GetService("Workspace")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Config = require(Shared.Config)
local PlaceIds = require(Shared.PlaceIds)
local Powers = require(Shared.Powers)
local PartyCode = require(Shared.PartyCode)
local Characters = require(Shared.Characters)
local Remotes = require(Shared.Remotes)

Remotes.init({ "Lobby_StartSolo", "Lobby_CreateParty", "Lobby_JoinParty", "Lobby_Notify" })

local startSolo = Remotes.get("Lobby_StartSolo")
local createParty = Remotes.get("Lobby_CreateParty")
local joinParty = Remotes.get("Lobby_JoinParty")
local notifyRemote = Remotes.get("Lobby_Notify")

local parties = MemoryStoreService:GetHashMap("M13Parties_v1")

---------------------------------------------------------------------------
-- Décor du lobby (simple, remplaçable par ton propre décor dans Studio)
---------------------------------------------------------------------------
local function buildLobby()
	Lighting.ClockTime = 0
	Lighting.Brightness = 1
	Lighting.Ambient = Color3.fromRGB(25, 28, 45)
	Lighting.OutdoorAmbient = Color3.fromRGB(25, 28, 45)

	local floor = Instance.new("Part")
	floor.Name = "LobbyFloor"
	floor.Anchored = true
	floor.Size = Vector3.new(80, 2, 80)
	floor.Position = Vector3.new(0, -1, 0)
	floor.Color = Color3.fromRGB(35, 36, 48)
	floor.Material = Enum.Material.SmoothPlastic
	floor.Parent = Workspace

	local spawnPad = Instance.new("SpawnLocation")
	spawnPad.Name = "LobbySpawn"
	spawnPad.Anchored = true
	spawnPad.Size = Vector3.new(8, 1, 8)
	spawnPad.Position = Vector3.new(0, 0.5, 15)
	spawnPad.Neutral = true
	spawnPad.Duration = 0
	spawnPad.Transparency = 1
	spawnPad.CanCollide = false
	local decal = spawnPad:FindFirstChildOfClass("Decal")
	if decal then
		decal:Destroy()
	end
	spawnPad.Parent = Workspace

	local sign = Instance.new("Part")
	sign.Name = "TitleSign"
	sign.Anchored = true
	sign.Size = Vector3.new(40, 10, 1)
	sign.Color = Color3.fromRGB(10, 12, 24)
	sign.Material = Enum.Material.SmoothPlastic
	sign.CFrame = CFrame.lookAt(Vector3.new(0, 8, -30), Vector3.new(0, 8, 15))
	sign.Parent = Workspace

	local gui = Instance.new("SurfaceGui")
	gui.Face = Enum.NormalId.Front
	gui.Parent = sign
	local label = Instance.new("TextLabel")
	label.Size = UDim2.fromScale(1, 1)
	label.BackgroundTransparency = 1
	label.Text = Config.GameName
	label.TextScaled = true
	label.Font = Enum.Font.GothamBold
	label.TextColor3 = Color3.fromRGB(110, 170, 255)
	label.Parent = gui

	local light = Instance.new("PointLight")
	light.Color = Color3.fromRGB(80, 140, 255)
	light.Range = 40
	light.Brightness = 2
	light.Parent = sign
end

buildLobby()

---------------------------------------------------------------------------
-- Outils
---------------------------------------------------------------------------
local lastCall: { [number]: { [string]: number } } = {}

local function tooSoon(player: Player, key: string, interval: number): boolean
	local entry = lastCall[player.UserId]
	if not entry then
		entry = {}
		lastCall[player.UserId] = entry
	end
	local now = os.clock()
	if entry[key] and now - entry[key] < interval then
		return true
	end
	entry[key] = now
	return false
end

Players.PlayerRemoving:Connect(function(player)
	lastCall[player.UserId] = nil
end)

local function notify(player: Player, message: string)
	notifyRemote:FireClient(player, message)
end

-- Filtrage obligatoire du texte saisi par les joueurs (règles Roblox).
local function filteredName(player: Player, raw: string): string?
	local ok, result = pcall(function()
		local filtered = TextService:FilterStringAsync(raw, player.UserId)
		return filtered:GetNonChatStringForBroadcastAsync()
	end)
	if not ok or typeof(result) ~= "string" or #result == 0 then
		return nil
	end
	if string.match(result, "^#+$") then
		return nil
	end
	return result
end

local function teleport(player: Player, accessCode: string?, data: any): (boolean, string?)
	if PlaceIds.Tome1 == 0 then
		return false, "Le Tome 1 n'est pas encore configuré (PlaceIds.Tome1)."
	end
	if RunService:IsStudio() then
		return false, "La téléportation ne marche pas dans Studio. Publie le jeu pour tester les groupes."
	end
	local options = Instance.new("TeleportOptions")
	if accessCode then
		options.ReservedServerAccessCode = accessCode
	else
		options.ShouldReserveServer = true
	end
	options:SetTeleportData(data)
	local ok, err = pcall(function()
		TeleportService:TeleportAsync(PlaceIds.Tome1, { player }, options)
	end)
	if not ok then
		warn("[M13] Téléportation échouée : " .. tostring(err))
		return false, "Téléportation impossible. Réessaie dans un instant."
	end
	return true, nil
end

local function prepareCharacter(player: Player, raw: any): (any?, string?)
	local clean, problem = Characters.sanitizeCustom(raw, Powers)
	if not clean then
		return nil, problem
	end
	local name = filteredName(player, clean.name)
	if not name then
		return nil, "Ce nom n'est pas accepté. Essaie-en un autre."
	end
	clean.name = name
	return clean, nil
end

---------------------------------------------------------------------------
-- Solo : on joue Darius sur un serveur privé tout neuf
---------------------------------------------------------------------------
startSolo.OnServerInvoke = function(player)
	if tooSoon(player, "solo", 3) then
		return { ok = false, message = "Doucement..." }
	end
	local ok, message = teleport(player, nil, { mode = "solo" })
	return { ok = ok, message = message }
end

---------------------------------------------------------------------------
-- Groupe : créer
---------------------------------------------------------------------------
createParty.OnServerInvoke = function(player, rawCharacter)
	if tooSoon(player, "create", 5) then
		return { ok = false, message = "Doucement..." }
	end
	local character, problem = prepareCharacter(player, rawCharacter)
	if not character then
		return { ok = false, message = problem }
	end
	if PlaceIds.Tome1 == 0 or RunService:IsStudio() then
		local _, message = teleport(player, nil, nil)
		return { ok = false, message = message }
	end

	local reserved, accessCode = pcall(function()
		return (TeleportService:ReserveServer(PlaceIds.Tome1))
	end)
	if not reserved then
		return { ok = false, message = "Impossible de réserver un serveur privé." }
	end

	local entry = { accessCode = accessCode, host = player.UserId, createdAt = os.time() }
	local code: string? = nil
	for _ = 1, 6 do
		local candidate = PartyCode.generate(Config.PartyCodeLength, math.random)
		local claimed = false
		local ok = pcall(function()
			parties:UpdateAsync(candidate, function(old)
				claimed = (old == nil)
				if old ~= nil then
					return nil
				end
				return entry
			end, Config.PartyTTLSeconds)
		end)
		if ok and claimed then
			code = candidate
			break
		end
	end
	if not code then
		return { ok = false, message = "Impossible de créer le code du groupe. Réessaie." }
	end

	local ok, message = teleport(player, accessCode, {
		mode = "group",
		partyCode = code,
		character = character,
	})
	return { ok = ok, message = message, code = code }
end

---------------------------------------------------------------------------
-- Groupe : rejoindre avec un code
---------------------------------------------------------------------------
joinParty.OnServerInvoke = function(player, rawCode, rawCharacter)
	if tooSoon(player, "join", 3) then
		return { ok = false, message = "Doucement..." }
	end
	local code = PartyCode.normalize(rawCode)
	if not code or not PartyCode.isValid(code, Config.PartyCodeLength) then
		return { ok = false, message = "Code invalide (" .. Config.PartyCodeLength .. " caractères)." }
	end
	local character, problem = prepareCharacter(player, rawCharacter)
	if not character then
		return { ok = false, message = problem }
	end

	local fetched, entry = pcall(function()
		return parties:GetAsync(code)
	end)
	if not fetched then
		return { ok = false, message = "Service indisponible. Réessaie." }
	end
	if entry == nil then
		return { ok = false, message = "Code inconnu ou expiré." }
	end

	local ok, message = teleport(player, entry.accessCode, {
		mode = "group",
		partyCode = code,
		character = character,
	})
	return { ok = ok, message = message }
end

TeleportService.TeleportInitFailed:Connect(function(player, _result, errorMessage)
	warn("[M13] TeleportInitFailed : " .. tostring(errorMessage))
	notify(player, "La téléportation a échoué (groupe complet ou serveur indisponible).")
end)
