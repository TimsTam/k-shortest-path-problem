from collections import defaultdict
import heapq
from timeit import default_timer as timer
import sys


class Graph:
    def __init__(self):
        self.vertices = []  # list to store vertices
        self.vertices_connections = defaultdict(set)  # dictionary to store edge connections between vertices
        self.removed_edges = []  # list to store deleted edges
        self.edge_weights = {}  # dictionary to store weights of edges

    # adds vertex to graph
    def add_vertex(self, v):
        self.vertices.append(v)

    # adds edge to graph
    def add_edge(self, v1, v2, weight):
        self.edge_weights[(v1, v2)] = weight
        self.vertices_connections[v1].add(v2)

    # adds all deleted edges back into graph
    def restore_edges(self):
        for e in self.removed_edges:
            self.edge_weights[(e[0], e[1])] = e[2]
            self.vertices_connections[e[0]].add(e[1])

    # get weight of edge between two vertices
    def get_weight(self, v1, v2):
        return self.edge_weights[(v1, v2)]

    # checks if a vertex is in graph
    def vertex_exists(self, v):
        return v in self.vertices

    # removes edge from graph
    def delete_edge(self, v1, v2):
        if v2 in self.vertices_connections[v1]:
            self.vertices_connections[v1].remove(v2)
            w = self.get_weight(v1, v2)
            self.removed_edges.append((v1, v2, w))
            del self.edge_weights[(v1, v2)]

    # calculates a cost of a path on the graph
    def calculate_path_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            v1 = path[i]
            v2 = path[i + 1]
            cost += self.get_weight(v1, v2)
        return cost


def dijkstra_algorithm(graph, source, destination):
    costs = {vertex: float('inf') for vertex in graph.vertices}  # initialize all vertex costs to infinity
    child_vertex = {vertex: None for vertex in graph.vertices}  # initialize all child_vertex vertex to None
    costs[source] = 0  # initialize cost of source vertex to 0
    queue = [(0, source)]  # initialize queue with source vertex and cost

    while queue:
        # pop the next vertex with the lowest cost out of the queue
        current_cost, current_vertex = heapq.heappop(queue)
        if current_vertex == destination:  # check if we have reached destination
            break

        if current_cost > costs[current_vertex]:
            # shortest path to vertex has already been found, so we can go to next iteration in while loop
            continue

        for neighbor in graph.vertices_connections[current_vertex]:
            alt = current_cost + graph.edge_weights[(current_vertex, neighbor)]
            if alt < costs[neighbor]:
                costs[neighbor] = alt
                child_vertex[neighbor] = current_vertex
                heapq.heappush(queue, (alt, neighbor))

    # no possible path from source to destination
    if child_vertex[destination] is None:
        return None, float('inf')

    # create path from source to destination using the child_vertex dictionary
    path = []
    node = destination
    while node != source:
        path.append(node)
        node = child_vertex[node]

    path.append(source)
    path.reverse()

    return path, costs[destination]


def yen_algorithm(graph, source, destination, K):
    shortest_path, shortest_cost = dijkstra_algorithm(graph, source, destination)  # find the shortest path

    # no path from source to destination
    if shortest_path is None:
        return []

    paths = [(shortest_path, shortest_cost)]  # add the shortest path to list
    possible_paths = []

    # Find k+1 shortest paths since the shortest path was found using Dijkstra’s algorithm
    for k in range(1, K):
        # Iterate through each vertex in the shortest path
        for i in range(len(paths[k - 1][0]) - 1):
            spur_vertex = paths[k - 1][0][i]  # creates spur vertex from current vertex in the shortest path
            root_path = paths[k - 1][0][:i + 1]  # creates root path (path of vertices up to spur vertex)

            # deletes all edges that are a part of the previous k-1 paths,
            # to ensure that no vertices are repeated in new paths.
            for path, _ in paths:
                if path[:i + 1] == root_path:
                    graph.delete_edge(path[i], path[i + 1])

            # calculate the shortest path from spur vertex to destination
            spur_path, spur_cost = dijkstra_algorithm(graph, spur_vertex, destination)

            if spur_path is not None:
                # combine root_path and spur_path to make new path.
                total_path = root_path + spur_path[1:]  # exclude first vertex of spur_path so there is no duplicates
                total_cost = graph.calculate_path_cost(total_path)  # calculate cost of new path.
                possible_paths.append((total_path, total_cost))  # add new path to list of possible paths

            # add back edges that were removed from graph
            graph.restore_edges()

        if not possible_paths:
            break

        possible_paths.sort(key=lambda x: x[1])  # sort list of tuples by second value in tuple

        paths.append(possible_paths[0])  # add the shortest path to paths
        possible_paths = []

    return paths


input_file = open(str(sys.argv[1]))  # open specified input file given from command line argument
graph = Graph()  # create graph structure
nodes, edges = input_file.readline().split()

# add all edges and vertices to graph structure
for edge in range(int(edges)):
    v1, v2, w = input_file.readline().split()
    if not graph.vertex_exists(v1):
        graph.add_vertex(v1)
    if not graph.vertex_exists(v2):
        graph.add_vertex(v2)
    graph.add_edge(v1, v2, float(w))

source, destination, kpaths = input_file.readline().split()

start_time = timer()  # start timer
shortestPaths = yen_algorithm(graph, source, destination, int(kpaths))  # get list of the shortest paths
end_time = timer()  # end timer
time_taken = (end_time - start_time) * 1000
print(f"{time_taken:.0f} milliseconds")

# print k path costs
for k, (path, cost) in enumerate(shortestPaths):
    print(f"Path {k+1} Cost: {cost:.3f}")
