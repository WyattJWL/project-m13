--!nonstrict
-- Effets visuels : glitchs (barres colorées, tremblement, teinte) et effets des pouvoirs.

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")
local TweenService = game:GetService("TweenService")
local Lighting = game:GetService("Lighting")
local Workspace = game:GetService("Workspace")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Remotes = require(Shared:WaitForChild("Remotes"))
local UI = require(script.Parent:WaitForChild("UI"))

local player = Players.LocalPlayer
local make = UI.make
local gui = UI.screenGui("M13Glitch", 20)

local bars = {}
for i = 1, 8 do
	bars[i] = make("Frame", {
		Size = UDim2.new(1, 0, 0, 10),
		BackgroundColor3 = Color3.fromRGB(110, 190, 255),
		BackgroundTransparency = 1,
		BorderSizePixel = 0,
	}, gui)
end

local glitchLabel = make("TextLabel", {
	Size = UDim2.fromScale(1, 0.2),
	Position = UDim2.fromScale(0, 0.4),
	BackgroundTransparency = 1,
	Text = "GL1TCH",
	Font = Enum.Font.Code,
	TextSize = 72,
	TextColor3 = Color3.fromRGB(255, 80, 120),
	TextTransparency = 1,
}, gui)

local glitchUntil = 0
local glitchPower = 0

local function humanoid()
	local character = player.Character
	return character and character:FindFirstChildOfClass("Humanoid")
end

Remotes.get("Game_Glitch").OnClientEvent:Connect(function(payload)
	glitchUntil = os.clock() + (payload.duration or 1)
	glitchPower = (payload.kind == "major") and 1 or 0.4
	glitchLabel.TextTransparency = (payload.kind == "major") and 0.2 or 1
	if payload.kind == "major" then
		task.delay(payload.duration or 1, function()
			glitchLabel.TextTransparency = 1
		end)
	end
end)

local random = Random.new()
RunService.RenderStepped:Connect(function()
	local active = os.clock() < glitchUntil
	for _, bar in bars do
		if active and random:NextNumber() < 0.5 * glitchPower + 0.1 then
			bar.Position = UDim2.fromScale(0, random:NextNumber())
			bar.Size = UDim2.new(1, 0, 0, random:NextInteger(4, 40))
			bar.BackgroundColor3 = Color3.fromHSV(random:NextNumber(), 0.7, 1)
			bar.BackgroundTransparency = 0.6 + random:NextNumber() * 0.3
		else
			bar.BackgroundTransparency = 1
		end
	end
	local h = humanoid()
	if h then
		if active then
			local amount = 0.25 * glitchPower
			h.CameraOffset = Vector3.new(random:NextNumber(-amount, amount), random:NextNumber(-amount, amount), 0)
		elseif h.CameraOffset ~= Vector3.zero then
			h.CameraOffset = Vector3.zero
		end
	end
end)

---------------------------------------------------------------------------
-- Effets des pouvoirs (côté client, purement visuels)
---------------------------------------------------------------------------
local function flash(position, size, color, duration, shape)
	local p = Instance.new("Part")
	p.Anchored = true
	p.CanCollide = false
	p.CanTouch = false
	p.CanQuery = false
	p.Material = Enum.Material.Neon
	p.Color = color
	p.Transparency = 0.4
	p.Shape = shape or Enum.PartType.Ball
	p.Size = Vector3.new(size, size, size)
	p.Position = position
	p.Parent = Workspace
	TweenService:Create(p, TweenInfo.new(duration), {
		Size = Vector3.new(size * 5, size * 5, size * 5),
		Transparency = 1,
	}):Play()
	task.delay(duration + 0.1, function()
		p:Destroy()
	end)
end

Remotes.get("Game_Fx").OnClientEvent:Connect(function(payload)
	local color = UI.rgb(payload.color or { 255, 255, 255 })
	local position = payload.position
	if payload.kind == "ring" then
		flash(position, 2, color, 0.7)
	elseif payload.kind == "burst" then
		flash(position, 3, color, 0.9)
	elseif payload.kind == "shield" then
		flash(position, 6, color, 1.2)
	elseif payload.kind == "slash" then
		flash(position, 1.2, color, 0.25)
	end
end)
