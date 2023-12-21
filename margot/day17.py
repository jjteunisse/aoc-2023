import numpy as np
import networkx as nx

name = "input"

data = np.array([[int(char) for char in line.rstrip()] for line in open("inputs/day17/{}.txt".format(name))])

graph = nx.DiGraph()

#Make a (ridiculously large) graph that includes locations + number of steps taken in most recent direction
directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
for (i, j) in np.ndindex(*data.shape):
    if i > 0:
        graph.add_edge(((i, j), (-1, 0), 1), ((i-1, j), (-1, 0), 2), loss=data[i-1, j])
        graph.add_edge(((i, j), (-1, 0), 2), ((i-1, j), (-1, 0), 3), loss=data[i-1, j])
        for direction in {(0, 1), (0, -1)}:
            graph.add_edge(((i, j), direction, 1), ((i-1, j), (-1, 0), 1), loss=data[i-1, j])
            graph.add_edge(((i, j), direction, 2), ((i-1, j), (-1, 0), 1), loss=data[i-1, j])
            graph.add_edge(((i, j), direction, 3), ((i-1, j), (-1, 0), 1), loss=data[i-1, j])
    if i < data.shape[0]-1:
        graph.add_edge(((i, j), (1, 0), 1), ((i+1, j), (1, 0), 2), loss=data[i+1, j])
        graph.add_edge(((i, j), (1, 0), 2), ((i+1, j), (1, 0), 3), loss=data[i+1, j])
        for direction in {(0, 1), (0, -1)}:
            graph.add_edge(((i, j), direction, 1), ((i+1, j), (1, 0), 1), loss=data[i+1, j])
            graph.add_edge(((i, j), direction, 2), ((i+1, j), (1, 0), 1), loss=data[i+1, j])
            graph.add_edge(((i, j), direction, 3), ((i+1, j), (1, 0), 1), loss=data[i+1, j])
    if j > 0:
        graph.add_edge(((i, j), (0, -1), 1), ((i, j-1), (0, -1), 2), loss=data[i, j-1])
        graph.add_edge(((i, j), (0, -1), 2), ((i, j-1), (0, -1), 3), loss=data[i, j-1])
        for direction in {(1, 0), (-1, 0)}:
            graph.add_edge(((i, j), direction, 1), ((i, j-1), (0, -1), 1), loss=data[i, j-1])
            graph.add_edge(((i, j), direction, 2), ((i, j-1), (0, -1), 1), loss=data[i, j-1])
            graph.add_edge(((i, j), direction, 3), ((i, j-1), (0, -1), 1), loss=data[i, j-1])
    if j < data.shape[1]-1:
        graph.add_edge(((i, j), (0, 1), 1), ((i, j+1), (0, 1), 2), loss=data[i, j+1])
        graph.add_edge(((i, j), (0, 1), 2), ((i, j+1), (0, 1), 3), loss=data[i, j+1])
        for direction in {(1, 0), (-1, 0)}:
            graph.add_edge(((i, j), direction, 1), ((i, j+1), (0, 1), 1), loss=data[i, j+1])
            graph.add_edge(((i, j), direction, 2), ((i, j+1), (0, 1), 1), loss=data[i, j+1])
            graph.add_edge(((i, j), direction, 3), ((i, j+1), (0, 1), 1), loss=data[i, j+1])
        
#Add source and target nodes that lead to all nodes in the top left resp. bottom right
source=(0, 0)
target=(data.shape[0]-1, data.shape[1]-1)

graph.add_edges_from([((0, 0), ((0, 0), (0, 1), 1)), ((0, 0), ((0, 0), (1, 0), 1))], loss=0)
graph.add_edges_from([((target, direction, steps), target)for direction in directions for steps in range(1, 4)], loss=0)

#Find the optimal path using Dijkstra's algorithm (thanks Lennard)
heat_loss = 0
shortest_path = nx.dijkstra_path(graph, source, target, weight='loss')
for edge in zip(shortest_path[:-1], shortest_path[1:]):
    heat_loss += graph.edges[edge]['loss']
print("Minimum heat loss:", heat_loss)