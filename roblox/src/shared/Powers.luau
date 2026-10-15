--!strict
-- Les trois pouvoirs de PROJECT-M13 et leur logique pure (sans API Roblox, donc testable).
--   Retenir   : encaisser et stocker, puis relâcher.
--   Rendre    : répartir la douleur entre tous.
--   Repousser : se protéger... mais le coup retombe sur quelqu'un d'autre.

export type PowerDef = {
	id: string,
	name: string,
	cooldown: number,
	summary: string,
	color: { number },
}

export type Member = { id: number, health: number, maxHealth: number }
export type Candidate = { id: number, health: number, maxHealth: number, distance: number }

local Powers = {}

Powers.Order = { "retenir", "rendre", "repousser" }

Powers.Definitions = {
	retenir = {
		id = "retenir",
		name = "Retenir",
		cooldown = 6,
		summary = "Encaisse les coups et les garde en toi. Réutilise le pouvoir pour tout relâcher.",
		color = { 80, 140, 255 },
	},
	rendre = {
		id = "rendre",
		name = "Rendre",
		cooldown = 8,
		summary = "Répartit la douleur entre tous les alliés proches. Ça te coûte un peu.",
		color = { 255, 200, 90 },
	},
	repousser = {
		id = "repousser",
		name = "Repousser",
		cooldown = 7,
		summary = "Repousse les ennemis et dévie les coups... qui retombent sur un allié. Et le monde glitche.",
		color = { 230, 90, 90 },
	},
} :: { [string]: PowerDef }

function Powers.isValid(id: any): boolean
	return typeof(id) == "string" and Powers.Definitions[id] ~= nil
end

-- Retenir : le bouclier absorbe jusqu'à `shieldRemaining` points et les stocke.
-- Renvoie (dégâts restants, bouclier restant, total stocké).
function Powers.absorb(shieldRemaining: number, stored: number, damage: number): (number, number, number)
	local absorbed = math.min(damage, shieldRemaining)
	return damage - absorbed, shieldRemaining - absorbed, stored + absorbed
end

-- Retenir : relâcher le poids stocké (borné pour éviter les abus).
function Powers.releaseDamage(stored: number): number
	return math.clamp(stored * 1.5, 0, 120)
end

-- Rendre : chaque membre se rapproche du ratio de santé moyen. Personne ne meurt de ça.
-- Renvoie la nouvelle santé par identifiant.
function Powers.share(members: { Member }, pull: number?): { [number]: number }
	local result: { [number]: number } = {}
	if #members == 0 then
		return result
	end
	local sum = 0
	for _, m in members do
		sum += m.health / m.maxHealth
	end
	local average = sum / #members
	local factor = pull or 0.6
	for _, m in members do
		local ratio = m.health / m.maxHealth
		local newRatio = ratio + (average - ratio) * factor
		result[m.id] = math.clamp(newRatio * m.maxHealth, 1, m.maxHealth)
	end
	return result
end

-- Repousser : le coup retombe sur l'allié en meilleure santé (en ratio) qui peut l'encaisser.
-- Renvoie nil s'il n'y a personne à portée (en solo, c'est le monde qui paie).
function Powers.pickDeflectTarget(candidates: { Candidate }, damage: number, maxDistance: number): number?
	local best: Candidate? = nil
	for _, c in candidates do
		if c.distance <= maxDistance and c.health > damage then
			if best == nil or c.health / c.maxHealth > best.health / best.maxHealth then
				best = c
			end
		end
	end
	if best then
		return best.id
	end
	return nil
end

return Powers
