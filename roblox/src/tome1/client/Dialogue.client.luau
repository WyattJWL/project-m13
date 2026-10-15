--!nonstrict
-- Boîte de dialogue : texte qui s'écrit, bouton « Continuer » ou choix.

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local UserInputService = game:GetService("UserInputService")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Remotes = require(Shared:WaitForChild("Remotes"))
local UI = require(script.Parent:WaitForChild("UI"))

local make = UI.make
local gui = UI.screenGui("M13Dialogue", 10)

local box = make("Frame", {
	Size = UDim2.new(0.62, 0, 0, 220),
	Position = UDim2.new(0.19, 0, 1, -250),
	BackgroundColor3 = Color3.fromRGB(10, 12, 24),
	BackgroundTransparency = 0.12,
	Visible = false,
}, gui)
UI.corner(box, 12)
make("UIPadding", {
	PaddingTop = UDim.new(0, 12),
	PaddingLeft = UDim.new(0, 16),
	PaddingRight = UDim.new(0, 16),
	PaddingBottom = UDim.new(0, 12),
}, box)

local speaker = make("TextLabel", {
	Size = UDim2.new(1, 0, 0, 26),
	BackgroundTransparency = 1,
	TextXAlignment = Enum.TextXAlignment.Left,
	Font = Enum.Font.GothamBold,
	TextSize = 22,
	TextColor3 = Color3.fromRGB(255, 200, 120),
	Text = "",
}, box)

local body = make("TextLabel", {
	Size = UDim2.new(1, 0, 0, 100),
	Position = UDim2.fromOffset(0, 30),
	BackgroundTransparency = 1,
	TextWrapped = true,
	TextXAlignment = Enum.TextXAlignment.Left,
	TextYAlignment = Enum.TextYAlignment.Top,
	Font = Enum.Font.Gotham,
	TextSize = 20,
	TextColor3 = Color3.fromRGB(240, 242, 255),
	Text = "",
}, box)

local buttons = make("Frame", {
	Size = UDim2.new(1, 0, 0, 70),
	Position = UDim2.new(0, 0, 1, -70),
	BackgroundTransparency = 1,
}, box)
make("UIListLayout", {
	FillDirection = Enum.FillDirection.Horizontal,
	Padding = UDim.new(0, 10),
	HorizontalAlignment = Enum.HorizontalAlignment.Right,
	VerticalAlignment = Enum.VerticalAlignment.Bottom,
}, buttons)

local currentId = nil
local canContinue = false
local typeToken = 0

local function clearButtons()
	for _, child in buttons:GetChildren() do
		if child:IsA("TextButton") then
			child:Destroy()
		end
	end
end

local function addButton(text, callback)
	local button = make("TextButton", {
		Size = UDim2.fromOffset(math.clamp(#text * 11 + 40, 120, 340), 44),
		BackgroundColor3 = Color3.fromRGB(40, 56, 100),
		TextColor3 = Color3.fromRGB(240, 244, 255),
		Font = Enum.Font.GothamMedium,
		TextSize = 17,
		Text = text,
		TextWrapped = true,
	}, buttons)
	UI.corner(button)
	button.Activated:Connect(callback)
	return button
end

local function advance()
	if currentId and canContinue then
		Remotes.get("Game_DialogueAdvance"):FireServer(currentId)
	end
end

Remotes.get("Game_Dialogue").OnClientEvent:Connect(function(payload)
	currentId = payload.id
	canContinue = payload.canContinue and not payload.choices
	box.Visible = true
	speaker.Text = payload.speaker or ""
	clearButtons()

	-- Texte qui s'écrit
	typeToken += 1
	local token = typeToken
	local text = payload.text
	body.Text = text
	body.MaxVisibleGraphemes = 0
	task.spawn(function()
		local total = utf8.len(text) or #text
		for i = 1, total do
			if token ~= typeToken then
				return
			end
			body.MaxVisibleGraphemes = i
			task.wait(0.012)
		end
		body.MaxVisibleGraphemes = -1
	end)

	if payload.choices then
		for index, choice in payload.choices do
			local id = payload.id
			addButton(choice, function()
				Remotes.get("Game_DialogueChoice"):FireServer(id, index)
			end)
		end
	else
		addButton("Continuer", advance)
	end
end)

Remotes.get("Game_DialogueClose").OnClientEvent:Connect(function()
	currentId = nil
	canContinue = false
	typeToken += 1
	box.Visible = false
	clearButtons()
end)

UserInputService.InputBegan:Connect(function(input, processed)
	if processed or not box.Visible then
		return
	end
	if input.KeyCode == Enum.KeyCode.Return or input.KeyCode == Enum.KeyCode.Space then
		advance()
	end
end)
