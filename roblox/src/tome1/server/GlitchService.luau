--!nonstrict
-- Le « glitch » du Non-lieu : une jauge d'instabilité qui monte quand on repousse, qu'on se trompe
-- de porte ou qu'on tue. Au-dessus de 50 : petits glitchs. À 100 : glitch majeur (le sol disparaît).

local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Config = require(Shared.Config)
local Remotes = require(Shared.Remotes)
local Session = require(script.Parent.Session)

local GlitchService = {
	tiles = {},
	lastMinor = 0,
}

function GlitchService.setTiles(tiles)
	GlitchService.tiles = tiles or {}
end

local function vanishTile(tile)
	task.spawn(function()
		if not tile.Parent then
			return
		end
		local original = tile.Color
		for _ = 1, 3 do
			tile.Color = Color3.fromRGB(255, 60, 80)
			task.wait(0.25)
			if not tile.Parent then
				return
			end
			tile.Color = original
			task.wait(0.25)
		end
		if not tile.Parent then
			return
		end
		tile.CanCollide = false
		tile.Transparency = 1
		task.wait(3)
		if tile.Parent then
			tile.Transparency = 0
			tile.CanCollide = true
		end
	end)
end

function GlitchService.minor()
	Remotes.get("Game_Glitch"):FireAllClients({ kind = "minor", duration = 1.2 })
end

function GlitchService.major()
	Remotes.get("Game_Glitch"):FireAllClients({ kind = "major", duration = 3 })
	local tiles = GlitchService.tiles
	if #tiles > 0 then
		local pool = table.clone(tiles)
		local count = math.min(4, #pool)
		for _ = 1, count do
			local index = math.random(1, #pool)
			vanishTile(table.remove(pool, index))
		end
	end
end

function GlitchService.start()
	task.spawn(function()
		while true do
			task.wait(0.5)
			local cfg = Config.Instability
			Session.instability = math.max(0, Session.instability - cfg.DecayPerSecond * 0.5)

			local now = os.clock()
			if Session.instability >= cfg.Max then
				GlitchService.major()
				Session.instability = cfg.ResetAfterMajor
			elseif Session.instability >= cfg.MinorThreshold and now - GlitchService.lastMinor > 8 then
				GlitchService.lastMinor = now
				GlitchService.minor()
			end

			Session.sendState(nil, { instability = Session.instability, instabilityMax = cfg.Max })
		end
	end)
end

return GlitchService
