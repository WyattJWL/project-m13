--!nocheck
-- Tests de la logique pure (sans Roblox) : lance avec `lune run tests/run`.

local process = require("@lune/process")

local Powers = require("../src/shared/Powers")
local PartyCode = require("../src/shared/PartyCode")
local Characters = require("../src/shared/Characters")
local DialogueGraph = require("../src/shared/DialogueGraph")
local Tome1 = require("../src/shared/Dialogue/Tome1")
local Config = require("../src/shared/Config")

local passed, failed = 0, 0

local function test(name, fn)
	local ok, err = pcall(fn)
	if ok then
		passed += 1
		print("  ok   " .. name)
	else
		failed += 1
		print("  FAIL " .. name .. "\n       " .. tostring(err))
	end
end

local function eq(actual, expected, label)
	if actual ~= expected then
		error((label or "valeur") .. " : attendu " .. tostring(expected) .. ", obtenu " .. tostring(actual), 2)
	end
end

local function near(actual, expected, label)
	if math.abs(actual - expected) > 1e-6 then
		error((label or "valeur") .. " : attendu " .. tostring(expected) .. ", obtenu " .. tostring(actual), 2)
	end
end

print("Powers")
test("les trois pouvoirs existent", function()
	eq(#Powers.Order, 3)
	for _, id in Powers.Order do
		assert(Powers.isValid(id), id)
		assert(Powers.Definitions[id].cooldown > 0, id)
	end
	eq(Powers.isValid("feu"), false)
	eq(Powers.isValid(nil), false)
	eq(Powers.isValid(12), false)
end)

test("Retenir : le bouclier absorbe puis déborde", function()
	local left, remaining, stored = Powers.absorb(40, 0, 25)
	eq(left, 0)
	eq(remaining, 15)
	eq(stored, 25)
	left, remaining, stored = Powers.absorb(15, 25, 60)
	eq(left, 45)
	eq(remaining, 0)
	eq(stored, 40)
end)

test("Retenir : l'explosion est bornée", function()
	eq(Powers.releaseDamage(40), 60)
	eq(Powers.releaseDamage(0), 0)
	eq(Powers.releaseDamage(10000), 120)
end)

test("Rendre : rapproche tout le monde de la moyenne sans rien perdre", function()
	local members = {
		{ id = 1, health = 100, maxHealth = 100 },
		{ id = 2, health = 20, maxHealth = 100 },
		{ id = 3, health = 60, maxHealth = 100 },
	}
	local result = Powers.share(members)
	near(result[1] + result[2] + result[3], 180, "somme des santés conservée")
	assert(result[1] < 100 and result[2] > 20, "doit se rapprocher")
	assert(result[2] < result[3] and result[3] < result[1], "l'ordre doit rester le même")
end)

test("Rendre : ne tue jamais et gère le vide", function()
	local result =
		Powers.share({ { id = 1, health = 1, maxHealth = 100 }, { id = 2, health = 100, maxHealth = 100 } }, 1)
	assert(result[1] >= 1 and result[2] <= 100)
	eq(next(Powers.share({})), nil)
end)

test("Repousser : le coup retombe sur l'allié le plus en forme", function()
	local candidates = {
		{ id = 10, health = 50, maxHealth = 100, distance = 100 }, -- trop loin
		{ id = 11, health = 90, maxHealth = 100, distance = 20 },
		{ id = 12, health = 30, maxHealth = 100, distance = 5 },
		{ id = 13, health = 4, maxHealth = 100, distance = 3 }, -- ne survivrait pas
	}
	eq(Powers.pickDeflectTarget(candidates, 6, 60), 11)
end)

test("Repousser : personne à portée = le monde paie", function()
	eq(Powers.pickDeflectTarget({}, 6, 60), nil)
	eq(Powers.pickDeflectTarget({ { id = 1, health = 5, maxHealth = 100, distance = 1 } }, 6, 60), nil)
end)

print("PartyCode")
test("génération : longueur et alphabet", function()
	local seed = 7
	local function rnd(a, b)
		seed = (seed * 1103515245 + 12345) % 2147483648
		return a + seed % (b - a + 1)
	end
	for _ = 1, 200 do
		local code = PartyCode.generate(Config.PartyCodeLength, rnd)
		eq(#code, Config.PartyCodeLength)
		assert(PartyCode.isValid(code, Config.PartyCodeLength), code)
		assert(not string.find(code, "[01OIL]"), "caractère ambigu : " .. code)
	end
end)

test("normalisation et validation", function()
	eq(PartyCode.normalize(" ab c2 "), "ABC2")
	eq(PartyCode.normalize(42), nil)
	eq(PartyCode.isValid("ABC2", 4), true)
	eq(PartyCode.isValid("ABC", 4), false)
	eq(PartyCode.isValid("AB0C", 4), false)
	eq(PartyCode.isValid(nil, 4), false)
end)

print("Characters")
test("personnage valide", function()
	local clean, err = Characters.sanitizeCustom({ name = "  Zoé ", power = "rendre", colorIndex = 3 }, Powers)
	assert(clean, err)
	eq(clean.name, "Zoé")
	eq(clean.power, "rendre")
	eq(clean.colorIndex, 3)
end)

test("noms interdits ou invalides", function()
	local function bad(raw)
		local clean, err = Characters.sanitizeCustom(raw, Powers)
		eq(clean, nil)
		assert(err and #err > 0)
	end
	bad(nil)
	bad({ name = "A", power = "rendre" })
	bad({ name = string.rep("x", 17), power = "rendre" })
	bad({ name = "Darius", power = "rendre" })
	bad({ name = "Émilie", power = "rendre" })
	bad({ name = "ÉVIE", power = "rendre" })
	bad({ name = "Léopold", power = "rendre" })
	bad({ name = "Zoé", power = "feu" })
	bad({ name = 12, power = "rendre" })
end)

test("couleur hors limites ramenée à 1", function()
	local clean = Characters.sanitizeCustom({ name = "Noa", power = "retenir", colorIndex = 99 }, Powers)
	eq(clean.colorIndex, 1)
end)

test("sans données : solo avec Darius", function()
	local r = Characters.resolve(nil, Powers)
	eq(r.mode, "solo")
	eq(r.canon, "darius")
	eq(r.power, "retenir")
end)

test("groupe valide et groupe invalide", function()
	local ok = Characters.resolve({
		mode = "group",
		partyCode = "ABC2",
		character = { name = "Noa", power = "repousser", colorIndex = 2 },
	}, Powers)
	eq(ok.mode, "group")
	eq(ok.partyCode, "ABC2")
	eq(ok.name, "Noa")
	eq(ok.canon, nil)
	local bad = Characters.resolve({ mode = "group", character = { name = "Alex", power = "rendre" } }, Powers)
	eq(bad.mode, "solo")
end)

print("Dialogues")
test("le graphe du Tome 1 est cohérent", function()
	local errors = DialogueGraph.validate(Tome1)
	eq(#errors, 0, table.concat(errors, " | "))
end)

test("le validateur détecte les erreurs", function()
	local errors = DialogueGraph.validate({
		nodes = {
			a = { text = "ok", next = "inconnu" },
			b = { text = "", choices = { { text = "x", next = "a" } } },
			c = { text = "orphelin" },
		},
		entries = { "a", "b", "zzz" },
	})
	assert(#errors >= 4, "erreurs trouvées : " .. #errors)
end)

print("")
print(string.format("%d réussi(s), %d échec(s)", passed, failed))
if failed > 0 then
	process.exit(1)
end
