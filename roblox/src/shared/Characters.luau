--!strict
-- Personnages : canon (Darius, Clara, Alex...) et personnages créés par les joueurs.
-- En solo, on joue Darius. En groupe, on crée un personnage qui N'EST PAS dans l'histoire.

export type Custom = { name: string, power: string, colorIndex: number }
export type Resolved = {
	mode: string,
	partyCode: string?,
	canon: string?,
	name: string,
	power: string,
	colorIndex: number,
}

local Characters = {}

-- Couleurs (R, G, B) proposées dans le créateur.
Characters.Palette = {
	{ 235, 235, 240 },
	{ 90, 140, 255 },
	{ 255, 190, 80 },
	{ 230, 90, 90 },
	{ 120, 200, 140 },
	{ 190, 130, 230 },
} :: { { number } }

Characters.Canon = {
	darius = { name = "Darius", power = "retenir", colorIndex = 1 },
	clara = { name = "Clara", colorIndex = 3 },
	alex = { name = "Alex", colorIndex = 2 },
} :: { [string]: { name: string, power: string?, colorIndex: number } }

-- Noms réservés : ils appartiennent à l'histoire.
local RESERVED = {
	"darius",
	"clara",
	"alex",
	"aubin",
	"kayden",
	"templier",
	"franck",
	"miel",
	"vasseur",
	"odile",
	"evie",
	"évie",
	"emilie",
	"émilie",
	"leopold",
	"léopold",
	"lecteur",
}

-- string.lower ne gère pas les majuscules accentuées : on les traite à la main.
local function lowerName(name: string): string
	local result = name
	for upper, lower in { ["É"] = "é", ["È"] = "è", ["Ê"] = "ê", ["Ë"] = "ë", ["À"] = "à", ["Ô"] = "ô" } do
		result = string.gsub(result, upper, lower)
	end
	return string.lower(result)
end

function Characters.isReservedName(name: string): boolean
	local lowered = lowerName(name)
	for _, reserved in RESERVED do
		if lowered == reserved then
			return true
		end
	end
	return false
end

-- Valide un personnage envoyé par un client. `powers` = le module Powers (injection pour les tests).
-- Renvoie (personnage nettoyé, nil) ou (nil, message d'erreur).
function Characters.sanitizeCustom(raw: any, powers: any): (Custom?, string?)
	if typeof(raw) ~= "table" then
		return nil, "Personnage invalide."
	end
	local name = raw.name
	if typeof(name) ~= "string" then
		return nil, "Choisis un nom."
	end
	name = string.gsub(name, "^%s+", "")
	name = string.gsub(name, "%s+$", "")
	local length = utf8.len(name)
	if length == nil or length < 2 or length > 16 then
		return nil, "Le nom doit faire entre 2 et 16 caractères."
	end
	if string.find(name, "%c") then
		return nil, "Le nom contient des caractères interdits."
	end
	if Characters.isReservedName(name) then
		return nil, "Ce nom appartient à l'histoire. Choisis-en un autre."
	end
	if not powers.isValid(raw.power) then
		return nil, "Choisis un pouvoir."
	end
	local colorIndex = raw.colorIndex
	if typeof(colorIndex) ~= "number" or colorIndex < 1 or colorIndex > #Characters.Palette then
		colorIndex = 1
	end
	return { name = name, power = raw.power, colorIndex = math.floor(colorIndex) }, nil
end

-- Lit les données de téléportation reçues par le serveur de jeu.
-- Sans données valides (ou en Studio), on retombe sur le solo avec Darius.
function Characters.resolve(teleportData: any, powers: any): Resolved
	local solo: Resolved = {
		mode = "solo",
		partyCode = nil,
		canon = "darius",
		name = Characters.Canon.darius.name,
		power = "retenir",
		colorIndex = Characters.Canon.darius.colorIndex,
	}
	if typeof(teleportData) ~= "table" then
		return solo
	end
	if teleportData.mode == "group" then
		local custom = Characters.sanitizeCustom(teleportData.character, powers)
		if custom == nil then
			return solo
		end
		local code = if typeof(teleportData.partyCode) == "string" then teleportData.partyCode else nil
		return {
			mode = "group",
			partyCode = code,
			canon = nil,
			name = custom.name,
			power = custom.power,
			colorIndex = custom.colorIndex,
		}
	end
	return solo
end

return Characters
