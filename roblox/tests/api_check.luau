--!nocheck
-- Vérifie le code contre la VRAIE base de données de l'API Roblox (fournie par Lune) :
--   * les classes passées à Instance.new / make("Classe", {...}) existent et sont créables ;
--   * les propriétés assignées existent sur la classe (ou ses parents) ;
--   * les énumérations Enum.X.Y existent.
-- Lance avec : lune run tests/api_check

local fs = require("@lune/fs")
local process = require("@lune/process")
local roblox = require("@lune/roblox")

local db = roblox.getReflectionDatabase()

local errors = {}
local function fail(file, line, message)
	table.insert(errors, string.format("%s:%d : %s", file, line, message))
end

local classCache = {}
local function classInfo(name)
	if classCache[name] == nil then
		classCache[name] = db:GetClass(name) or false
	end
	return classCache[name]
end

local function hasProperty(className, prop)
	local class = classInfo(className)
	while class do
		if class.Properties[prop] ~= nil then
			return true
		end
		class = class.Superclass and classInfo(class.Superclass) or nil
	end
	return false
end

local function isCreatable(className)
	local class = classInfo(className)
	if not class then
		return false
	end
	for _, tag in class.Tags or {} do
		if tag == "NotCreatable" or tag == "Service" then
			return false
		end
	end
	return true
end

-- Propriétés qui ne sont pas lisibles dans la base mais valides (ou gérées par notre code).
local ALLOWED = { Parent = true, Name = true }

local function lineOf(src, index)
	local _, count = string.gsub(string.sub(src, 1, index), "\n", "")
	return count + 1
end

-- Texte de premier niveau d'un tableau { ... } (sans contenu imbriqué ni chaînes).
local function topLevelOfTable(src, openIndex)
	local depth, i, out = 0, openIndex, {}
	local n = #src
	while i <= n do
		local ch = string.sub(src, i, i)
		if ch == '"' or ch == "'" then
			local quote = ch
			i += 1
			while i <= n and string.sub(src, i, i) ~= quote do
				if string.sub(src, i, i) == "\\" then
					i += 1
				end
				i += 1
			end
		elseif ch == "{" then
			depth += 1
			if depth == 1 then
				table.insert(out, "{")
			end
		elseif ch == "}" then
			depth -= 1
			if depth == 0 then
				table.insert(out, "}")
				return table.concat(out), i
			end
		elseif depth == 1 then
			table.insert(out, ch)
		end
		i += 1
	end
	return table.concat(out), n
end

local function checkFile(path)
	local src = fs.readFile(path)

	-- 1) Enums
	for index, enumName, itemName in string.gmatch(src, "()Enum%.(%w+)%.(%w+)") do
		local enum = db:GetEnum(enumName)
		if not enum then
			fail(path, lineOf(src, index), "Enum inconnu : Enum." .. enumName)
		elseif enum.Items[itemName] == nil then
			fail(path, lineOf(src, index), "Valeur d'enum inconnue : Enum." .. enumName .. "." .. itemName)
		end
	end

	-- 2) Instance.new("Classe")
	for index, className in string.gmatch(src, '()Instance%.new%("(%w+)"%)') do
		if not isCreatable(className) then
			fail(path, lineOf(src, index), "Classe inexistante ou non créable : " .. className)
		end
	end

	-- 3) make("Classe", { Propriété = ..., })
	local pos = 1
	while true do
		local s, e, className = string.find(src, 'make%("(%w+)",%s*{', pos)
		if not s then
			break
		end
		if not isCreatable(className) then
			fail(path, lineOf(src, s), "Classe inexistante ou non créable : " .. className)
		else
			local top, closeIndex = topLevelOfTable(src, e)
			for key in string.gmatch(top, "[{,]%s*([%a_][%w_]*)%s*=[^=]") do
				if not ALLOWED[key] and not hasProperty(className, key) then
					fail(path, lineOf(src, s), className .. " n'a pas de propriété « " .. key .. " »")
				end
			end
			pos = closeIndex
		end
		pos = math.max(pos, e + 1)
	end

	-- Propriétés assignées à une variable, dans sa portée (jusqu'au « end » de la fonction ou à la redéclaration).
	local function checkAssignments(declIndex, varName, className)
		local scopeEnd = #src
		local functionEnd = string.find(src, "\nend\n", declIndex, true)
		if functionEnd and functionEnd < scopeEnd then
			scopeEnd = functionEnd
		end
		local redeclared = string.find(src, "local " .. varName .. " =", declIndex + 1, true)
		if redeclared and redeclared < scopeEnd then
			scopeEnd = redeclared
		end
		local scope = string.sub(src, declIndex, scopeEnd)
		for offset, prop in string.gmatch(scope, "()%f[%w_]" .. varName .. "%.([%a_][%w_]*)%s*=[^=]") do
			if not ALLOWED[prop] and not hasProperty(className, prop) then
				fail(
					path,
					lineOf(src, declIndex + offset - 1),
					className .. " n'a pas de propriété « " .. prop .. " »"
				)
			end
		end
	end

	-- 4) variable = Instance.new("Classe") puis variable.Prop = ...
	for declIndex, varName, className in string.gmatch(src, '()local ([%w_]+) = Instance%.new%("(%w+)"%)') do
		if classInfo(className) then
			checkAssignments(declIndex, varName, className)
		end
	end

	-- Propriétés assignées sur les services (Lighting.ClockTime = ..., Players.RespawnTime = ...)
	for _, service in { "Lighting", "Players", "Workspace" } do
		for index, prop in string.gmatch(src, "()%f[%w_]" .. service .. "%.([%a_][%w_]*)%s*=[^=]") do
			if not hasProperty(service, prop) then
				fail(path, lineOf(src, index), service .. " n'a pas de propriété « " .. prop .. " »")
			end
		end
	end

	-- 5) variables renvoyées par nos petites fonctions utilitaires
	local helperClass = { part = "Part", block = "Part", pointLight = "PointLight", prompt = "ProximityPrompt" }
	for declIndex, varName, helper in string.gmatch(src, "()local ([%w_]+) = (%w+)%(") do
		local className = helperClass[helper]
		if className then
			checkAssignments(declIndex, varName, className)
		end
	end
end

local function walk(dir)
	for _, name in fs.readDir(dir) do
		local path = dir .. "/" .. name
		if fs.isDir(path) then
			walk(path)
		elseif string.match(name, "%.luau$") then
			checkFile(path)
		end
	end
end

walk("src")

if #errors > 0 then
	print("Problèmes d'API trouvés :")
	for _, message in errors do
		print("  - " .. message)
	end
	process.exit(1)
end
print("API Roblox : aucun problème trouvé.")
