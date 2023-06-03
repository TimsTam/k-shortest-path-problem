function yen_algorithm(graph, source, destination, K):
	shortest_path = dijkstra_algorithm(graph, source, destination)
	if shortest_path is None:
		return []
	paths = [dijkstra_algorithm(graph, source, destination)]
	possible_paths = []
	exclude_nodes = None
	
	for k from 1 to K
		for i from 0 to len(paths[k-1] - 1)
			spur_vertex = paths[k-1][i]
			root_path = paths[k-1].vertices(0 to i)
			
			for path in paths:
				if root_path = path.vertices(0 to i)
					remove path.edge(i, i+1) from graph
			
			spur_path = dijkstra_algorithm(graph, spur_vertex, destination, exclude_nodes)
			
			total_path = root_path + spur_path
			if total_path not in possible_paths:
				add total_path to possible_paths
			
			restore edges to graph
			
			if possible_paths is empty:
				break
			
			sort possible_paths
			
			add possible_paths[0] to paths
			possible_paths = []
			
		return paths
			