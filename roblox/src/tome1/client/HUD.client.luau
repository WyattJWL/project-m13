--!nonstrict
-- Interface de jeu : santé, instabilité, objectif, pouvoir, boss, messages, fondu et écran de fin.

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")
local TweenService = game:GetService("TweenService")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Remotes = require(Shared:WaitForChild("Remotes"))
local UI = require(script.Parent:WaitForChild("UI"))

local player = Players.LocalPlayer
local make = UI.make

local gui = UI.screenGui("M13HUD", 5)

---------------------------------------------------------------------------
-- Éléments
---------------------------------------------------------------------------
local modeLabel = make("TextLabel", {
	Size = UDim2.fromOffset(300, 48),
	Position = UDim2.fromOffset(12, 12),
	BackgroundTransparency = 1,
	TextXAlignment = Enum.TextXAlignment.Left,
	TextYAlignment = Enum.TextYAlignment.Top,
	Font = Enum.Font.GothamMedium,
	TextSize = 18,
	TextColor3 = Color3.fromRGB(230, 235, 255),
	TextStrokeTransparency = 0.5,
	Text = "",
}, gui)

local objective = make("TextLabel", {
	Size = UDim2.fromOffset(320, 90),
	Position = UDim2.new(1, -332, 0, 12),
	BackgroundColor3 = Color3.fromRGB(12, 14, 26),
	BackgroundTransparency = 0.35,
	TextWrapped = true,
	TextXAlignment = Enum.TextXAlignment.Left,
	TextYAlignment = Enum.TextYAlignment.Top,
	Font = Enum.Font.Gotham,
	TextSize = 17,
	TextColor3 = Color3.fromRGB(240, 240, 255),
	Text = "",
	Visible = false,
}, gui)
UI.corner(objective)
make(
	"UIPadding",
	{ PaddingTop = UDim.new(0, 8), PaddingLeft = UDim.new(0, 10), PaddingRight = UDim.new(0, 10) },
	objective
)

-- Barre d'instabilité (le glitch)
local instabilityBack = make("Frame", {
	Size = UDim2.fromOffset(320, 18),
	Position = UDim2.new(0.5, -160, 0, 14),
	BackgroundColor3 = Color3.fromRGB(16, 18, 32),
	BorderSizePixel = 0,
}, gui)
UI.corner(instabilityBack, 9)
local instabilityFill = make("Frame", {
	Size = UDim2.fromScale(0, 1),
	BackgroundColor3 = Color3.fromRGB(230, 90, 120),
	BorderSizePixel = 0,
}, instabilityBack)
UI.corner(instabilityFill, 9)
make("TextLabel", {
	Size = UDim2.new(1, 0, 0, 16),
	Position = UDim2.fromOffset(0, 20),
	BackgroundTransparency = 1,
	Text = "INSTABILITÉ",
	Font = Enum.Font.GothamBold,
	TextSize = 12,
	TextColor3 = Color3.fromRGB(230, 130, 150),
}, instabilityBack)

-- Barre du boss
local bossBack = make("Frame", {
	Size = UDim2.fromOffset(460, 20),
	Position = UDim2.new(0.5, -230, 0, 64),
	BackgroundColor3 = Color3.fromRGB(16, 18, 32),
	BorderSizePixel = 0,
	Visible = false,
}, gui)
UI.corner(bossBack, 10)
local bossFill = make("Frame", {
	Size = UDim2.fromScale(1, 1),
	BackgroundColor3 = Color3.fromRGB(110, 190, 255),
	BorderSizePixel = 0,
}, bossBack)
UI.corner(bossFill, 10)
make("TextLabel", {
	Size = UDim2.fromScale(1, 1),
	BackgroundTransparency = 1,
	Text = "KAYDEN",
	Font = Enum.Font.GothamBold,
	TextSize = 14,
	TextColor3 = Color3.fromRGB(255, 255, 255),
}, bossBack)

-- Santé
local healthBack = make("Frame", {
	Size = UDim2.fromOffset(280, 22),
	Position = UDim2.new(0, 16, 1, -44),
	BackgroundColor3 = Color3.fromRGB(16, 18, 32),
	BorderSizePixel = 0,
}, gui)
UI.corner(healthBack, 11)
local healthFill = make("Frame", {
	Size = UDim2.fromScale(1, 1),
	BackgroundColor3 = Color3.fromRGB(110, 210, 140),
	BorderSizePixel = 0,
}, healthBack)
UI.corner(healthFill, 11)

-- Bouton de pouvoir (aussi utilisable au toucher)
local powerButton = make("TextButton", {
	Name = "PowerButton",
	Size = UDim2.fromOffset(220, 56),
	Position = UDim2.new(0.5, -110, 1, -76),
	BackgroundColor3 = Color3.fromRGB(30, 36, 60),
	TextColor3 = Color3.fromRGB(240, 244, 255),
	Font = Enum.Font.GothamBold,
	TextSize = 18,
	Text = "[Q] Pouvoir",
	AutoButtonColor = true,
}, gui)
UI.corner(powerButton)
local cooldownCover = make("Frame", {
	Size = UDim2.fromScale(0, 1),
	BackgroundColor3 = Color3.fromRGB(0, 0, 0),
	BackgroundTransparency = 0.55,
	BorderSizePixel = 0,
	ZIndex = 2,
}, powerButton)
UI.corner(cooldownCover)

local attackButton = make("TextButton", {
	Name = "AttackButton",
	Size = UDim2.fromOffset(110, 56),
	Position = UDim2.new(0.5, 120, 1, -76),
	BackgroundColor3 = Color3.fromRGB(60, 40, 40),
	TextColor3 = Color3.fromRGB(255, 240, 240),
	Font = Enum.Font.GothamBold,
	TextSize = 18,
	Text = "Attaque",
}, gui)
UI.corner(attackButton)

local toast = make("TextLabel", {
	Size = UDim2.fromOffset(520, 40),
	Position = UDim2.new(0.5, -260, 1, -130),
	BackgroundTransparency = 1,
	Font = Enum.Font.GothamMedium,
	TextSize = 20,
	TextColor3 = Color3.fromRGB(255, 220, 140),
	TextStrokeTransparency = 0.4,
	Text = "",
}, gui)

local fadeFrame = make("Frame", {
	Size = UDim2.fromScale(1, 1),
	BackgroundColor3 = Color3.new(0, 0, 0),
	BackgroundTransparency = 1,
	BorderSizePixel = 0,
	ZIndex = 50,
	Active = false,
}, gui)

local finishFrame = make("Frame", {
	Size = UDim2.fromScale(1, 1),
	BackgroundColor3 = Color3.fromRGB(8, 10, 20),
	BackgroundTransparency = 0.1,
	Visible = false,
	ZIndex = 60,
}, gui)
local finishLabel = make("TextLabel", {
	Size = UDim2.fromScale(0.8, 0.3),
	Position = UDim2.fromScale(0.1, 0.35),
	BackgroundTransparency = 1,
	TextWrapped = true,
	Font = Enum.Font.GothamBold,
	TextSize = 36,
	TextColor3 = Color3.fromRGB(235, 240, 255),
	Text = "",
	ZIndex = 61,
}, finishFrame)

---------------------------------------------------------------------------
-- Logique
---------------------------------------------------------------------------
local cooldownEnd = 0
local cooldownTotal = 1

local function setObjective(text)
	objective.Visible = text ~= nil and text ~= ""
	objective.Text = text and ("Objectif\n" .. text) or ""
end

local toastToken = 0
local function showToast(text)
	toastToken += 1
	local token = toastToken
	toast.Text = text
	toast.TextTransparency = 0
	task.delay(4, function()
		if token == toastToken then
			TweenService:Create(toast, TweenInfo.new(0.6), { TextTransparency = 1 }):Play()
		end
	end)
end

Remotes.get("Game_Notify").OnClientEvent:Connect(showToast)

Remotes.get("Game_State").OnClientEvent:Connect(function(state)
	if state.mode ~= nil or state.partyCode ~= nil or state.name ~= nil then
		local lines = {}
		if state.name then
			table.insert(lines, state.name)
		end
		if state.partyCode then
			table.insert(lines, "Code du groupe : " .. state.partyCode)
		elseif state.mode == "solo" then
			table.insert(lines, "Mode solo")
		end
		modeLabel.Text = table.concat(lines, "\n")
	end
	if state.power then
		cooldownTotal = state.power.cooldown
		powerButton.Text = "[Q] " .. state.power.name
		powerButton.BackgroundColor3 = UI.rgb(state.power.color):Lerp(Color3.fromRGB(20, 22, 36), 0.55)
	end
	if state.objective ~= nil then
		setObjective(state.objective)
	end
	if state.instability then
		local maxValue = state.instabilityMax or 100
		TweenService:Create(
			instabilityFill,
			TweenInfo.new(0.4),
			{ Size = UDim2.fromScale(math.clamp(state.instability / maxValue, 0, 1), 1) }
		):Play()
	end
	if state.cooldown then
		cooldownEnd = os.clock() + state.cooldown
	end
	if state.boss ~= nil then
		if state.boss == false then
			bossBack.Visible = false
		else
			bossBack.Visible = true
			bossFill.Size = UDim2.fromScale(math.clamp(state.boss.hp / state.boss.max, 0, 1), 1)
		end
	end
	if state.fade ~= nil then
		TweenService:Create(fadeFrame, TweenInfo.new(0.8), { BackgroundTransparency = state.fade and 0 or 1 }):Play()
	end
	if state.finished then
		finishFrame.Visible = true
		finishLabel.Text = (state.summary or "Fin du Tome 1.") .. "\n\nRetour au lobby..."
	end
end)

powerButton.Activated:Connect(function()
	Remotes.get("Game_UsePower"):FireServer()
end)
attackButton.Activated:Connect(function()
	Remotes.get("Game_BasicAttack"):FireServer()
end)

RunService.RenderStepped:Connect(function()
	local remaining = cooldownEnd - os.clock()
	cooldownCover.Size = UDim2.fromScale(remaining > 0 and math.clamp(remaining / cooldownTotal, 0, 1) or 0, 1)

	local character = player.Character
	local humanoid = character and character:FindFirstChildOfClass("Humanoid")
	if humanoid then
		healthFill.Size = UDim2.fromScale(math.clamp(humanoid.Health / humanoid.MaxHealth, 0, 1), 1)
	end
end)
