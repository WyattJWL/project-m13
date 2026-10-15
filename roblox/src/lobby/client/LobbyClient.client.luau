--!nonstrict
-- Interface du lobby : solo, créer un groupe, rejoindre un groupe + créateur de personnage.

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Powers = require(Shared:WaitForChild("Powers"))
local Characters = require(Shared:WaitForChild("Characters"))
local Config = require(Shared:WaitForChild("Config"))
local Remotes = require(Shared:WaitForChild("Remotes"))

local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")

local startSolo = Remotes.get("Lobby_StartSolo")
local createParty = Remotes.get("Lobby_CreateParty")
local joinParty = Remotes.get("Lobby_JoinParty")
local notifyRemote = Remotes.get("Lobby_Notify")

local function make(className, props, parent)
	local inst = Instance.new(className)
	for key, value in props do
		inst[key] = value
	end
	inst.Parent = parent
	return inst
end

local function rgb(t)
	return Color3.fromRGB(t[1], t[2], t[3])
end

local function style(button)
	make("UICorner", { CornerRadius = UDim.new(0, 8) }, button)
	return button
end

local gui = make("ScreenGui", { Name = "M13Lobby", ResetOnSpawn = false, IgnoreGuiInset = true }, playerGui)

local title = make("TextLabel", {
	Size = UDim2.fromScale(1, 0.14),
	Position = UDim2.fromScale(0, 0.04),
	BackgroundTransparency = 1,
	Text = Config.GameName .. " — TOME 1",
	TextScaled = true,
	Font = Enum.Font.GothamBold,
	TextColor3 = Color3.fromRGB(110, 170, 255),
}, gui)
make("UITextSizeConstraint", { MaxTextSize = 54 }, title)

local status = make("TextLabel", {
	Size = UDim2.fromScale(0.8, 0.06),
	Position = UDim2.fromScale(0.1, 0.9),
	BackgroundTransparency = 1,
	Text = "",
	TextScaled = true,
	Font = Enum.Font.Gotham,
	TextColor3 = Color3.fromRGB(255, 200, 120),
}, gui)
make("UITextSizeConstraint", { MaxTextSize = 24 }, status)

local function setStatus(text)
	status.Text = text or ""
end

---------------------------------------------------------------------------
-- Menu principal
---------------------------------------------------------------------------
local menu = make("Frame", {
	Size = UDim2.fromScale(0.34, 0.4),
	Position = UDim2.fromScale(0.33, 0.3),
	BackgroundTransparency = 1,
}, gui)
make("UIListLayout", { Padding = UDim.new(0, 12), HorizontalAlignment = Enum.HorizontalAlignment.Center }, menu)

local function menuButton(text, order)
	local b = make("TextButton", {
		Size = UDim2.new(1, 0, 0, 56),
		BackgroundColor3 = Color3.fromRGB(30, 36, 60),
		TextColor3 = Color3.fromRGB(235, 240, 255),
		Font = Enum.Font.GothamMedium,
		TextSize = 22,
		Text = text,
		LayoutOrder = order,
		AutoButtonColor = true,
	}, menu)
	return style(b)
end

local soloButton = menuButton("Jouer en solo (Darius)", 1)
local createButton = menuButton("Créer un groupe", 2)
local joinButton = menuButton("Rejoindre un groupe", 3)

---------------------------------------------------------------------------
-- Créateur de personnage (groupe)
---------------------------------------------------------------------------
local panel = make("Frame", {
	Size = UDim2.fromScale(0.5, 0.7),
	Position = UDim2.fromScale(0.25, 0.18),
	BackgroundColor3 = Color3.fromRGB(16, 20, 38),
	Visible = false,
}, gui)
style(panel)
make("UIListLayout", { Padding = UDim.new(0, 8), HorizontalAlignment = Enum.HorizontalAlignment.Center }, panel)
make(
	"UIPadding",
	{ PaddingTop = UDim.new(0, 12), PaddingLeft = UDim.new(0, 12), PaddingRight = UDim.new(0, 12) },
	panel
)

local panelTitle = make("TextLabel", {
	Size = UDim2.new(1, 0, 0, 30),
	BackgroundTransparency = 1,
	Text = "Ton personnage",
	Font = Enum.Font.GothamBold,
	TextSize = 24,
	TextColor3 = Color3.fromRGB(235, 240, 255),
	LayoutOrder = 1,
}, panel)

local nameBox = make("TextBox", {
	Size = UDim2.new(1, 0, 0, 40),
	BackgroundColor3 = Color3.fromRGB(30, 36, 60),
	TextColor3 = Color3.fromRGB(255, 255, 255),
	PlaceholderText = "Nom (2 à 16 caractères, pas un nom de l'histoire)",
	Text = "",
	Font = Enum.Font.Gotham,
	TextSize = 18,
	ClearTextOnFocus = false,
	LayoutOrder = 2,
}, panel)
style(nameBox)

local codeBox = make("TextBox", {
	Size = UDim2.new(1, 0, 0, 40),
	BackgroundColor3 = Color3.fromRGB(30, 36, 60),
	TextColor3 = Color3.fromRGB(255, 255, 255),
	PlaceholderText = "Code du groupe (4 caractères)",
	Text = "",
	Font = Enum.Font.GothamBold,
	TextSize = 20,
	ClearTextOnFocus = false,
	LayoutOrder = 3,
	Visible = false,
}, panel)
style(codeBox)

local powerRow = make("Frame", { Size = UDim2.new(1, 0, 0, 44), BackgroundTransparency = 1, LayoutOrder = 4 }, panel)
make("UIListLayout", {
	FillDirection = Enum.FillDirection.Horizontal,
	Padding = UDim.new(0, 8),
	HorizontalAlignment = Enum.HorizontalAlignment.Center,
}, powerRow)

local powerSummary = make("TextLabel", {
	Size = UDim2.new(1, 0, 0, 56),
	BackgroundTransparency = 1,
	TextWrapped = true,
	Font = Enum.Font.Gotham,
	TextSize = 16,
	TextColor3 = Color3.fromRGB(200, 210, 235),
	Text = "",
	LayoutOrder = 5,
}, panel)

local selectedPower = "retenir"
local selectedColor = 1
local powerButtons = {}

local function refreshPower()
	for id, button in powerButtons do
		button.BackgroundColor3 = (id == selectedPower) and rgb(Powers.Definitions[id].color)
			or Color3.fromRGB(40, 46, 72)
		button.TextColor3 = (id == selectedPower) and Color3.fromRGB(10, 10, 16) or Color3.fromRGB(235, 240, 255)
	end
	local def = Powers.Definitions[selectedPower]
	powerSummary.Text = def.name .. " — " .. def.summary
end

for _, id in Powers.Order do
	local def = Powers.Definitions[id]
	local button = make("TextButton", {
		Size = UDim2.new(0.31, 0, 1, 0),
		Text = def.name,
		Font = Enum.Font.GothamBold,
		TextSize = 18,
	}, powerRow)
	style(button)
	powerButtons[id] = button
	button.Activated:Connect(function()
		selectedPower = id
		refreshPower()
	end)
end

local colorRow = make("Frame", { Size = UDim2.new(1, 0, 0, 40), BackgroundTransparency = 1, LayoutOrder = 6 }, panel)
make("UIListLayout", {
	FillDirection = Enum.FillDirection.Horizontal,
	Padding = UDim.new(0, 8),
	HorizontalAlignment = Enum.HorizontalAlignment.Center,
}, colorRow)

local colorButtons = {}
local function refreshColors()
	for index, button in colorButtons do
		button.Text = (index == selectedColor) and "●" or ""
	end
end
for index, color in Characters.Palette do
	local button = make("TextButton", {
		Size = UDim2.fromOffset(40, 40),
		BackgroundColor3 = rgb(color),
		TextColor3 = Color3.fromRGB(10, 10, 16),
		TextSize = 22,
		Text = "",
	}, colorRow)
	style(button)
	colorButtons[index] = button
	button.Activated:Connect(function()
		selectedColor = index
		refreshColors()
	end)
end

local confirmButton = make("TextButton", {
	Size = UDim2.new(1, 0, 0, 48),
	BackgroundColor3 = Color3.fromRGB(60, 120, 230),
	TextColor3 = Color3.fromRGB(255, 255, 255),
	Font = Enum.Font.GothamBold,
	TextSize = 20,
	Text = "Valider",
	LayoutOrder = 7,
}, panel)
style(confirmButton)

local backButton = make("TextButton", {
	Size = UDim2.new(1, 0, 0, 36),
	BackgroundColor3 = Color3.fromRGB(40, 46, 72),
	TextColor3 = Color3.fromRGB(220, 226, 245),
	Font = Enum.Font.Gotham,
	TextSize = 16,
	Text = "Retour",
	LayoutOrder = 8,
}, panel)
style(backButton)

---------------------------------------------------------------------------
-- Logique
---------------------------------------------------------------------------
local mode = nil -- "create" | "join"
local busy = false

local function showPanel(newMode)
	mode = newMode
	menu.Visible = false
	panel.Visible = true
	codeBox.Visible = (mode == "join")
	panelTitle.Text = (mode == "join") and "Rejoindre un groupe" or "Créer un groupe"
	setStatus("")
	refreshPower()
	refreshColors()
end

local function showMenu()
	mode = nil
	panel.Visible = false
	menu.Visible = true
	setStatus("")
end

local function currentCharacter()
	return { name = nameBox.Text, power = selectedPower, colorIndex = selectedColor }
end

local function run(label, fn)
	if busy then
		return
	end
	busy = true
	setStatus(label)
	local ok, result = pcall(fn)
	busy = false
	if not ok then
		setStatus("Erreur de connexion. Réessaie.")
		return
	end
	if result and result.ok then
		if result.code then
			setStatus("Groupe créé. Code : " .. result.code .. " — téléportation...")
		else
			setStatus("Téléportation...")
		end
	else
		setStatus((result and result.message) or "Échec.")
	end
end

soloButton.Activated:Connect(function()
	run("Préparation du serveur privé...", function()
		return startSolo:InvokeServer()
	end)
end)
createButton.Activated:Connect(function()
	showPanel("create")
end)
joinButton.Activated:Connect(function()
	showPanel("join")
end)
backButton.Activated:Connect(showMenu)

confirmButton.Activated:Connect(function()
	if mode == "create" then
		run("Création du groupe...", function()
			return createParty:InvokeServer(currentCharacter())
		end)
	elseif mode == "join" then
		run("Connexion au groupe...", function()
			return joinParty:InvokeServer(codeBox.Text, currentCharacter())
		end)
	end
end)

notifyRemote.OnClientEvent:Connect(function(message)
	setStatus(tostring(message))
end)
