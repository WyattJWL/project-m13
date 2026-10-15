--!nocheck
-- Environnement Roblox minimal pour les tests de fumée sous Lune (vrais types Roblox via @lune/roblox).
local roblox = require("@lune/roblox")

local game = roblox.Instance.new("DataModel")

local Random = {}
function Random.new()
	return {
		NextInteger = function(_, a, b)
			return math.random(a, b)
		end,
		NextNumber = function(_, a, b)
			return a + math.random() * ((b or 1) - (a or 0))
		end,
	}
end

return {
	game = game,
	Instance = roblox.Instance,
	Vector3 = roblox.Vector3,
	Vector2 = roblox.Vector2,
	CFrame = roblox.CFrame,
	Color3 = roblox.Color3,
	Enum = roblox.Enum,
	UDim = roblox.UDim,
	UDim2 = roblox.UDim2,
	NumberRange = roblox.NumberRange,
	NumberSequence = roblox.NumberSequence,
	ColorSequence = roblox.ColorSequence,
	Random = Random,
}
