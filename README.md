# Shortest Path Problem (Graph Algorithms)
## 2801ICT – COMPUTING ALGORITHMS (A1: TASK 2)

### 2.1	PROBLEM OVERVIEW

Melanie’s father wants to travel from Southport to Brisbane CBD and wants Melanie to recommend the exactly K-shortest loopless paths. Melanie’s father insists that the first recommended path must be the shortest path between Southport and Brisbane CBD. While the rest of the K – 1 paths are approximated shortest paths which Melanie’s father will use as backup paths.
This is an application of the shortest path problem, in where the goal is to find the shortest path between two vertices in a graph. BFS cannot be used to solve this problem as the weights of the graph can be any value. Two of the most popular algorithms, Dijkstra’s and Bellman Ford’s, are unable to solve this problem so another algorithm must be used.

### 2.2	INPUT SPECIFICATIONS

The input must be given in a file named “finalInput.txt”. The first line of input will contain 2 integers (N, M). Where N is the number of vertices and M is the number of edges. The following lines of input will contain 3 variables ai, bi, wi where ai and bi is the edge between vertices ai and bi while wi is the weight of that edge.

### 2.3	OUTPUT SPECIFICATIONS

The output must print out the length of the K-shortest loopless paths separated by commas. These paths must include the shortest possible path from the Southport to Brisbane CDB followed by the rest of the k-1 shortest paths.

