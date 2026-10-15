--!nonstrict
-- Petits outils pour construire l'interface en code (pas besoin de Studio pour l'éditer).

local UI = {}

function UI.make(className, props, parent)
	local inst = Instance.new(className)
	for key, value in props do
		inst[key] = value
	end
	inst.Parent = parent
	return inst
end

function UI.corner(inst, radius)
	UI.make("UICorner", { CornerRadius = UDim.new(0, radius or 8) }, inst)
	return inst
end

function UI.rgb(t)
	return Color3.fromRGB(t[1], t[2], t[3])
end

function UI.screenGui(name, order)
	local Players = game:GetService("Players")
	local playerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
	local existing = playerGui:FindFirstChild(name)
	if existing then
		existing:Destroy()
	end
	return UI.make("ScreenGui", {
		Name = name,
		ResetOnSpawn = false,
		IgnoreGuiInset = true,
		DisplayOrder = order or 1,
	}, playerGui)
end

return UI
