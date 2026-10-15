--!strict
-- Codes de groupe : 4 caractères lisibles (sans 0/O, 1/I/L pour éviter les confusions).

local PartyCode = {}

PartyCode.Alphabet = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"

function PartyCode.generate(length: number, randomInt: (number, number) -> number): string
	local chars = {}
	for i = 1, length do
		local index = randomInt(1, #PartyCode.Alphabet)
		chars[i] = string.sub(PartyCode.Alphabet, index, index)
	end
	return table.concat(chars)
end

-- Met en majuscules et retire les espaces. Renvoie nil si l'entrée n'est pas un texte.
function PartyCode.normalize(input: any): string?
	if typeof(input) ~= "string" then
		return nil
	end
	local cleaned = string.gsub(input, "%s+", "")
	return string.upper(cleaned)
end

function PartyCode.isValid(code: any, length: number): boolean
	if typeof(code) ~= "string" or #code ~= length then
		return false
	end
	for i = 1, #code do
		local ch = string.sub(code, i, i)
		if string.find(PartyCode.Alphabet, ch, 1, true) == nil then
			return false
		end
	end
	return true
end

return PartyCode
