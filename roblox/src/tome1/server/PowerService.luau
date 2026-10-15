--!nonstrict
-- Pouvoirs, attaque de base et dégâts. Tout est calculé côté serveur (le client ne fait que demander).
--   Retenir   : bouclier qui stocke les coups, puis explosion.
--   Rendre    : répartit la santé entre les alliés proches.
--   Repousser : repousse les ennemis et dévie les coups sur un allié. Le monde glitche en échange.

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")

local Shared = ReplicatedStorage:WaitForChild("Shared")
local Config = require(Shared.Config)
local Powers = require(Shared.Powers)
local Remotes = require(Shared.Remotes)
local Session = require(script.Parent.Session)
local EnemyService = require(script.Parent.EnemyService)

local PowerService = {}

local BASE_WALK_SPEED = 16

local function fx(kind: string, position: Vector3, color: { number })
	Remotes.get("Game_Fx"):FireAllClients({ kind = kind, position = position, color = color })
end

local function distanceBetween(a: Player, b: Player): number
	local ra, rb = Session.root(a), Session.root(b)
	if not ra or not rb then
		return math.huge
	end
	return (ra.Position - rb.Position).Magnitude
end

---------------------------------------------------------------------------
-- Dégâts reçus par un joueur
---------------------------------------------------------------------------
function PowerService.applyDamage(player: Player, amount: number, source: string?, noTransfer: boolean?)
	local data = Session.get(player)
	local humanoid = Session.humanoid(player)
	if not data or not humanoid or humanoid.Health <= 0 then
		return
	end
	local now = os.clock()
	local states = data.states

	-- Repousser : le coup ne m'atteint pas... il retombe sur quelqu'un d'autre.
	if states.deflectUntil > now and not noTransfer then
		local candidates = {}
		for _, other in Session.alivePlayers() do
			if other ~= player then
				local otherHumanoid = Session.humanoid(other)
				table.insert(candidates, {
					id = other.UserId,
					health = otherHumanoid.Health,
					maxHealth = otherHumanoid.MaxHealth,
					distance = distanceBetween(player, other),
				})
			end
		end
		local targetId = Powers.pickDeflectTarget(candidates, amount, Config.Repousser.TransferRange)
		if targetId then
			for _, other in Session.alivePlayers() do
				if other.UserId == targetId then
					Session.notify(other, data.displayName .. " a repoussé un coup : il retombe sur toi.")
					Session.notify(player, "Le coup est retombé sur " .. Session.get(other).displayName .. ".")
					PowerService.applyDamage(other, amount, source, true)
					return
				end
			end
		else
			-- Personne à portée : c'est le monde qui paie.
			Session.addInstability(amount * 0.8)
			Session.notify(player, "Personne pour porter le coup : le monde glitche.")
			return
		end
	end

	-- Retenir : le bouclier encaisse et stocke.
	if states.shieldUntil > now and states.shieldRemaining > 0 then
		local left, remaining, stored = Powers.absorb(states.shieldRemaining, states.stored, amount)
		states.shieldRemaining = remaining
		states.stored = stored
		amount = left
	end

	if amount > 0 then
		humanoid:TakeDamage(amount)
	end
end

---------------------------------------------------------------------------
-- Utiliser son pouvoir
---------------------------------------------------------------------------
local function useRetenir(player: Player, data, humanoid, root, now: number)
	local cfg = Config.Retenir
	local states = data.states
	if states.stored > 0 and now < states.storedUntil then
		local damage = Powers.releaseDamage(states.stored)
		states.stored = 0
		states.lastPower = now
		for _, enemy in EnemyService.inRadius(root.Position, cfg.ReleaseRadius) do
			EnemyService.damage(enemy, damage, player)
		end
		fx("burst", root.Position, Powers.Definitions.retenir.color)
		return
	end
	if now - states.lastPower < Powers.Definitions.retenir.cooldown then
		return
	end
	states.lastPower = now
	states.shieldUntil = now + cfg.ShieldSeconds
	states.shieldRemaining = cfg.ShieldCapacity
	states.stored = 0
	states.storedUntil = now + cfg.ShieldSeconds + cfg.StoredSeconds
	fx("shield", root.Position, Powers.Definitions.retenir.color)
end

local function useRendre(player: Player, data, humanoid, root, now: number)
	local def = Powers.Definitions.rendre
	local states = data.states
	if now - states.lastPower < def.cooldown then
		return
	end
	local members, humanoids = {}, {}
	for _, other in Session.alivePlayers() do
		if distanceBetween(player, other) <= Config.Rendre.Radius then
			local otherHumanoid = Session.humanoid(other)
			table.insert(
				members,
				{ id = other.UserId, health = otherHumanoid.Health, maxHealth = otherHumanoid.MaxHealth }
			)
			humanoids[other.UserId] = otherHumanoid
		end
	end
	if #members <= 1 then
		Session.notify(player, "Personne à portée : il n'y a rien à rendre.")
		states.lastPower = now - def.cooldown + 2
		return
	end
	states.lastPower = now
	local result = Powers.share(members)
	for id, health in result do
		local target = humanoids[id]
		target.Health = math.min(health + Config.Rendre.Heal, target.MaxHealth)
	end
	-- Le coût : celui qui rend en garde un peu pour lui.
	humanoid.Health = math.max(1, humanoid.Health - Config.Rendre.SelfCost)
	fx("ring", root.Position, def.color)
end

local function useRepousser(player: Player, data, humanoid, root, now: number)
	local def = Powers.Definitions.repousser
	local cfg = Config.Repousser
	local states = data.states
	if now - states.lastPower < def.cooldown then
		return
	end
	states.lastPower = now
	states.deflectUntil = now + cfg.DeflectSeconds
	for _, enemy in EnemyService.inRadius(root.Position, cfg.Radius) do
		EnemyService.push(enemy, enemy.pos - root.Position, cfg.Push)
		EnemyService.damage(enemy, cfg.Damage, player)
	end
	Session.addInstability(cfg.InstabilityGain)
	fx("ring", root.Position, def.color)
end

function PowerService.use(player: Player)
	local data = Session.get(player)
	local humanoid = Session.humanoid(player)
	local root = Session.root(player)
	if not data or not humanoid or not root or humanoid.Health <= 0 then
		return
	end
	local now = os.clock()
	if data.power == "retenir" then
		useRetenir(player, data, humanoid, root, now)
	elseif data.power == "rendre" then
		useRendre(player, data, humanoid, root, now)
	elseif data.power == "repousser" then
		useRepousser(player, data, humanoid, root, now)
	end
	-- Informe le HUD du temps de recharge restant.
	local def = Powers.Definitions[data.power]
	local remaining = math.max(0, def.cooldown - (os.clock() - data.states.lastPower))
	Session.sendState(player, { cooldown = remaining })
end

---------------------------------------------------------------------------
-- Attaque de base (clic)
---------------------------------------------------------------------------
function PowerService.basicAttack(player: Player)
	local data = Session.get(player)
	local humanoid = Session.humanoid(player)
	local root = Session.root(player)
	if not data or not humanoid or not root or humanoid.Health <= 0 then
		return
	end
	local now = os.clock()
	if now - data.states.lastAttack < Config.BasicAttack.Cooldown then
		return
	end
	data.states.lastAttack = now
	local look = root.CFrame.LookVector
	for _, enemy in EnemyService.inRadius(root.Position, Config.BasicAttack.Range + 3) do
		local offset = enemy.pos - root.Position
		local flat = Vector3.new(offset.X, 0, offset.Z)
		if flat.Magnitude < 0.1 or flat.Unit:Dot(Vector3.new(look.X, 0, look.Z).Unit) > 0.2 then
			EnemyService.damage(enemy, Config.BasicAttack.Damage, player)
		end
	end
	fx("slash", root.Position + look * 3, { 255, 255, 255 })
end

---------------------------------------------------------------------------
-- Démarrage
---------------------------------------------------------------------------
function PowerService.start()
	EnemyService.attackHandler = function(player, damage, source)
		PowerService.applyDamage(player, damage, source, false)
	end

	Remotes.get("Game_UsePower").OnServerEvent:Connect(function(player)
		PowerService.use(player)
	end)
	Remotes.get("Game_BasicAttack").OnServerEvent:Connect(function(player)
		PowerService.basicAttack(player)
	end)

	-- Ralentissement tant qu'on porte du poids (Retenir) + péremption du poids stocké.
	task.spawn(function()
		while true do
			task.wait(0.25)
			local now = os.clock()
			for player, data in Session.players do
				local humanoid = Session.humanoid(player)
				if humanoid then
					local states = data.states
					if states.stored > 0 and now >= states.storedUntil then
						states.stored = 0
					end
					local carrying = states.stored > 0
					humanoid.WalkSpeed = carrying and BASE_WALK_SPEED * Config.Retenir.SlowFactor or BASE_WALK_SPEED
				end
			end
		end
	end)
end

return PowerService
