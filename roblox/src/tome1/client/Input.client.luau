--!nonstrict
-- Commandes : Q = pouvoir, clic = attaque. (Au toucher : les boutons du HUD.)

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local UserInputService = game:GetService("UserInputService")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Remotes = require(Shared:WaitForChild("Remotes"))

local usePower = Remotes.get("Game_UsePower")
local basicAttack = Remotes.get("Game_BasicAttack")

UserInputService.InputBegan:Connect(function(input, processed)
	if processed then
		return
	end
	if input.KeyCode == Enum.KeyCode.Q then
		usePower:FireServer()
	elseif input.UserInputType == Enum.UserInputType.MouseButton1 then
		basicAttack:FireServer()
	end
end)
