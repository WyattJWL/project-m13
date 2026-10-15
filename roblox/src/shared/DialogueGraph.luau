--!strict
-- Vérifie qu'un graphe de dialogue est cohérent (utilisé par les tests et au démarrage en Studio).

local DialogueGraph = {}

-- Renvoie la liste des erreurs trouvées (liste vide = graphe valide).
function DialogueGraph.validate(graph: any): { string }
	local errors: { string } = {}
	local nodes = graph.nodes
	if typeof(nodes) ~= "table" then
		return { "graph.nodes manquant" }
	end

	local reachable: { [string]: boolean } = {}
	local function visit(id: string)
		if reachable[id] then
			return
		end
		reachable[id] = true
		local node = nodes[id]
		if node == nil then
			return
		end
		if node.next then
			visit(node.next)
		end
		if node.choices then
			for _, choice in node.choices do
				if choice.next then
					visit(choice.next)
				end
			end
		end
	end

	for _, entry in graph.entries or {} do
		if nodes[entry] == nil then
			table.insert(errors, "entrée inconnue : " .. tostring(entry))
		else
			visit(entry)
		end
	end

	for id, node in nodes do
		if typeof(node.text) ~= "string" or #node.text == 0 then
			table.insert(errors, id .. " : texte vide")
		end
		if node.next and nodes[node.next] == nil then
			table.insert(errors, id .. " : next inconnu (" .. tostring(node.next) .. ")")
		end
		if node.next and node.choices then
			table.insert(errors, id .. " : a à la fois next et choices")
		end
		if node.choices then
			if #node.choices == 0 then
				table.insert(errors, id .. " : choices vide")
			end
			for index, choice in node.choices do
				if typeof(choice.text) ~= "string" or #choice.text == 0 then
					table.insert(errors, id .. " : choix " .. index .. " sans texte")
				end
				if choice.next and nodes[choice.next] == nil then
					table.insert(errors, id .. " : choix " .. index .. " vers un noeud inconnu")
				end
			end
		end
		if not reachable[id] then
			table.insert(errors, id .. " : noeud inatteignable")
		end
	end

	return errors
end

return DialogueGraph
