function dijkstra_algorithm(graph, source, destination):
	for each vertex in graph.vertices:
		cost[vertex] = INFINITY
		child[vertex] = None
	cost[source] = 0
	add source to Q
	
	while Q is not empty:
		current_vertex = vertex in Q with min cost[vertex]
		remove current_vertex from Q
		
		for each neighbour of current_vertex:
            cost = cost[current_vertex] + graph.edge_weight[(current_vertex, neighbour)]
            if cost < cost[neighbour]:
                cost[neighbour] = cost
                child[neighbour] = current_vertex
                add neighbour to Q
                
    if child[destination] is None:
        return path=None, cost=INFINITY
       
    path = []
    vertex = destination
    while vertex is not source:
        add vertex to path
        vertex = child[vertex]
    
    add source to path
    reverse path
    
    return path, cost[destination]