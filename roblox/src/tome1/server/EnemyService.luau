--!nonstrict
-- Ennemis : les Silhouettes (mensonges qui rôdent) et Kayden (boss).
-- Les ennemis sont des modèles ancrés déplacés par le serveur (simple et fiable pour un prototype).

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")
local TweenService = game:GetService("TweenService")
local Workspace = game:GetService("Workspace")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Config = require(Shared.Config)
local Session = require(script.Parent.Session)
local Models = require(script.Parent.EnemyModels)

local EnemyService = {
	list = {},
	-- Branchés par PowerService / StoryService :
	attackHandler = nil, -- function(player, damage, sourceName)
	onKilled = nil, -- function(enemy, byPlayer)
	onBossHealth = nil, -- function(hp, maxHp)
	onBossPhase = nil, -- function(phase)
}

local nextId = 0

local function folder()
	local f = Workspace:FindFirstChild("M13Enemies")
	if not f then
		f = Instance.new("Folder")
		f.Name = "M13Enemies"
		f.Parent = Workspace
	end
	return f
end

---------------------------------------------------------------------------
-- API
---------------------------------------------------------------------------
function EnemyService.spawn(kind: string, position: Vector3)
	nextId += 1
	local enemy
	if kind == "boss" then
		local extra = math.max(0, Session.count() - 1)
		local maxHp = Config.Boss.BaseHealth + Config.Boss.PerExtraPlayer * extra
		local model, body = Models.buildBoss(folder(), position)
		enemy = {
			id = nextId,
			kind = "boss",
			model = model,
			body = body,
			pos = position,
			hp = maxHp,
			maxHp = maxHp,
			speed = Config.Boss.Speed,
			damage = 15,
			attackRange = 7,
			attackCooldown = 1.6,
			nextAttack = 0,
			nextSlam = os.clock() + 5,
			nextSummon = os.clock() + 10,
			slamCooldown = 7,
			phase = 1,
			hover = 6.5,
			pushVel = Vector3.zero,
			pushUntil = 0,
		}
	else
		local model, body = Models.buildSilhouette(folder(), position)
		local cfg = Config.Silhouette
		enemy = {
			id = nextId,
			kind = "silhouette",
			model = model,
			body = body,
			pos = position,
			hp = cfg.Health,
			maxHp = cfg.Health,
			speed = cfg.Speed,
			damage = cfg.Damage,
			attackRange = cfg.AttackRange,
			attackCooldown = cfg.AttackCooldown,
			nextAttack = os.clock() + 1,
			hover = 3.5,
			pushVel = Vector3.zero,
			pushUntil = 0,
		}
	end
	table.insert(EnemyService.list, enemy)
	if enemy.kind == "boss" and EnemyService.onBossHealth then
		EnemyService.onBossHealth(enemy.hp, enemy.maxHp)
	end
	return enemy
end

function EnemyService.inRadius(position: Vector3, radius: number)
	local found = {}
	for _, enemy in EnemyService.list do
		if not enemy.dead then
			local delta = enemy.pos - position
			if Vector3.new(delta.X, 0, delta.Z).Magnitude <= radius then
				table.insert(found, enemy)
			end
		end
	end
	return found
end

function EnemyService.push(enemy, direction: Vector3, distance: number)
	local flat = Vector3.new(direction.X, 0, direction.Z)
	if flat.Magnitude < 0.01 then
		return
	end
	-- Le boss est plus lourd.
	local factor = (enemy.kind == "boss") and 0.25 or 1
	enemy.pushVel = flat.Unit * (distance * factor / 0.25)
	enemy.pushUntil = os.clock() + 0.25
end

local function dissolve(enemy)
	local position = enemy.pos + Vector3.new(0, 4, 0)
	local pages = folder()
	for _ = 1, (enemy.kind == "boss") and 24 or 8 do
		local page = Models.block(
			pages,
			"Page",
			Vector3.new(0.8, 1.1, 0.1),
			position + Vector3.new(math.random(-20, 20) / 10, math.random(-20, 20) / 10, math.random(-20, 20) / 10),
			Color3.fromRGB(245, 245, 240)
		)
		local tween = TweenService:Create(page, TweenInfo.new(1.4), {
			Position = page.Position
				+ Vector3.new(math.random(-60, 60) / 10, math.random(40, 90) / 10, math.random(-60, 60) / 10),
			Transparency = 1,
		})
		tween:Play()
		task.delay(1.5, function()
			page:Destroy()
		end)
	end
	enemy.model:Destroy()
end

function EnemyService.damage(enemy, amount: number, byPlayer: Player?)
	if enemy.dead then
		return
	end
	enemy.hp -= amount
	if enemy.kind == "boss" then
		if EnemyService.onBossHealth then
			EnemyService.onBossHealth(math.max(enemy.hp, 0), enemy.maxHp)
		end
		if enemy.phase == 1 and enemy.hp <= enemy.maxHp / 2 and enemy.hp > 0 then
			enemy.phase = 2
			enemy.speed *= 1.25
			enemy.slamCooldown = 5
			if EnemyService.onBossPhase then
				EnemyService.onBossPhase(2)
			end
		end
	end
	if enemy.hp <= 0 then
		enemy.dead = true
		dissolve(enemy)
		if EnemyService.onKilled then
			EnemyService.onKilled(enemy, byPlayer)
		end
	end
end

function EnemyService.clear()
	for _, enemy in EnemyService.list do
		enemy.dead = true
	end
	EnemyService.list = {}
	local f = Workspace:FindFirstChild("M13Enemies")
	if f then
		f:ClearAllChildren()
	end
end

function EnemyService.livingCount(): number
	local n = 0
	for _, enemy in EnemyService.list do
		if not enemy.dead then
			n += 1
		end
	end
	return n
end

---------------------------------------------------------------------------
-- IA
---------------------------------------------------------------------------
local function nearestPlayer(position: Vector3)
	local best, bestDistance, bestRoot = nil, math.huge, nil
	for _, player in Session.alivePlayers() do
		local root = Session.root(player)
		local delta = root.Position - position
		local distance = Vector3.new(delta.X, 0, delta.Z).Magnitude
		if distance < bestDistance then
			best, bestDistance, bestRoot = player, distance, root
		end
	end
	return best, bestDistance, bestRoot
end

local function slam(enemy)
	local target = nearestPlayer(enemy.pos)
	if not target then
		return
	end
	local root = Session.root(target)
	if not root then
		return
	end
	local center = Vector3.new(root.Position.X, 0.2, root.Position.Z)
	local radius = Config.Boss.SlamRadius
	local marker = Instance.new("Part")
	marker.Name = "SlamWarning"
	marker.Shape = Enum.PartType.Cylinder
	marker.Size = Vector3.new(0.3, radius * 2, radius * 2)
	marker.CFrame = CFrame.new(center) * CFrame.Angles(0, 0, math.rad(90))
	marker.Color = Color3.fromRGB(255, 60, 80)
	marker.Material = Enum.Material.Neon
	marker.Transparency = 0.55
	marker.Anchored = true
	marker.CanCollide = false
	marker.CanTouch = false
	marker.Parent = folder()
	task.delay(1.5, function()
		marker:Destroy()
		if enemy.dead then
			return
		end
		for _, player in Session.alivePlayers() do
			local r = Session.root(player)
			if r then
				local delta = r.Position - center
				if Vector3.new(delta.X, 0, delta.Z).Magnitude <= radius and EnemyService.attackHandler then
					EnemyService.attackHandler(player, Config.Boss.SlamDamage, "Kayden")
				end
			end
		end
	end)
end

local function step(enemy, dt: number, now: number)
	local target, distance, root = nearestPlayer(enemy.pos)

	if enemy.kind == "boss" then
		if now >= enemy.nextSlam then
			enemy.nextSlam = now + enemy.slamCooldown
			slam(enemy)
		end
		if now >= enemy.nextSummon then
			enemy.nextSummon = now + 12
			for i = 1, 2 do
				EnemyService.spawn("silhouette", enemy.pos + Vector3.new(i * 6 - 9, -2.5, 4))
			end
		end
	end

	local newPos = enemy.pos
	if now < enemy.pushUntil then
		newPos += enemy.pushVel * dt
	elseif target and distance > enemy.attackRange - 1 then
		local direction = Vector3.new(root.Position.X - newPos.X, 0, root.Position.Z - newPos.Z)
		if direction.Magnitude > 0.01 then
			newPos += direction.Unit * enemy.speed * dt
		end
	end
	newPos = Vector3.new(newPos.X, enemy.hover, newPos.Z)
	enemy.pos = newPos

	if target then
		local look = Vector3.new(root.Position.X, newPos.Y, root.Position.Z)
		if (look - newPos).Magnitude > 0.1 then
			enemy.model:PivotTo(CFrame.lookAt(newPos, look))
		else
			enemy.model:PivotTo(CFrame.new(newPos))
		end
		if distance <= enemy.attackRange and now >= enemy.nextAttack then
			enemy.nextAttack = now + enemy.attackCooldown
			if EnemyService.attackHandler then
				EnemyService.attackHandler(target, enemy.damage, enemy.model.Name)
			end
		end
	else
		enemy.model:PivotTo(CFrame.new(newPos))
	end
end

function EnemyService.start()
	RunService.Heartbeat:Connect(function(dt)
		local now = os.clock()
		for i = #EnemyService.list, 1, -1 do
			local enemy = EnemyService.list[i]
			if enemy.dead or not enemy.model.Parent then
				table.remove(EnemyService.list, i)
			else
				step(enemy, dt, now)
			end
		end
	end)
end

return EnemyService
