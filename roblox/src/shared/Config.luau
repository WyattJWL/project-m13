--!strict
-- Réglages communs au lobby et au Tome 1.

local Config = {
	GameName = "PROJECT-M13",

	-- Groupes (serveurs privés)
	MaxPartySize = 4,
	PartyCodeLength = 4,
	PartyTTLSeconds = 3600,

	-- Joueur
	StartingHealth = 100,
	BasicAttack = { Damage = 8, Range = 7, Cooldown = 0.45 },

	-- Pouvoirs
	Retenir = { ShieldCapacity = 40, ShieldSeconds = 4, StoredSeconds = 8, SlowFactor = 0.8, ReleaseRadius = 18 },
	Rendre = { Radius = 25, SelfCost = 8, Heal = 8 },
	Repousser = { DeflectSeconds = 3, Radius = 14, Push = 12, Damage = 5, InstabilityGain = 12, TransferRange = 60 },

	-- Instabilité (le « glitch » du Non-lieu)
	Instability = { Max = 100, DecayPerSecond = 1, MinorThreshold = 50, ResetAfterMajor = 40 },

	-- Ennemis
	Silhouette = { Health = 30, Speed = 11, Damage = 6, AttackRange = 4, AttackCooldown = 1.2 },
	Boss = { BaseHealth = 700, PerExtraPlayer = 300, Speed = 9, SlamDamage = 25, SlamRadius = 10 },

	-- Test dans Roblox Studio (pas de téléportation possible)
	StudioDefaultMode = "solo",
}

return Config
