import numpy as np
import networkx as nx
import sys

def make_graph(data, max_steps:int, min_steps:int=1):
    #Make a (ridiculously large) graph that includes locations + number of steps taken in most recent direction
    graph = nx.DiGraph()

    directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
    for (i, j) in np.ndindex(*data.shape):
        if i > 0:
            for steps in range(1, max_steps):
                graph.add_edge(((i, j), (-1, 0), steps), ((i-1, j), (-1, 0), steps+1), loss=data[i-1, j])
            for direction in {(0, 1), (0, -1)}:
                for steps in range(min_steps, max_steps+1):
                    graph.add_edge(((i, j), direction, steps), ((i-1, j), (-1, 0), 1), loss=data[i-1, j])
        if i < data.shape[0]-1:
            for steps in range(1, max_steps):
                graph.add_edge(((i, j), (1, 0), steps), ((i+1, j), (1, 0), steps+1), loss=data[i+1, j])
            for direction in {(0, 1), (0, -1)}:
                for steps in range(min_steps, max_steps+1):
                    graph.add_edge(((i, j), direction, steps), ((i+1, j), (1, 0), 1), loss=data[i+1, j])
        if j > 0:
            for steps in range(1, max_steps):
                graph.add_edge(((i, j), (0, -1), steps), ((i, j-1), (0, -1), steps+1), loss=data[i, j-1])
            for direction in {(1, 0), (-1, 0)}:
                for steps in range(min_steps, max_steps+1):
                    graph.add_edge(((i, j), direction, steps), ((i, j-1), (0, -1), 1), loss=data[i, j-1])
        if j < data.shape[1]-1:
            for steps in range(1, max_steps):
                graph.add_edge(((i, j), (0, 1), steps), ((i, j+1), (0, 1), steps+1), loss=data[i, j+1])
            for direction in {(1, 0), (-1, 0)}:
                for steps in range(min_steps, max_steps+1):
                    graph.add_edge(((i, j), direction, steps), ((i, j+1), (0, 1), 1), loss=data[i, j+1])
        
    #Add source and target nodes that lead to all nodes in the top left resp. bottom right
    source=(0, 0)
    target=(data.shape[0]-1, data.shape[1]-1)

    graph.add_edges_from([((0, 0), ((0, 0), (0, 1), 1)), ((0, 0), ((0, 0), (1, 0), 1))], loss=0)
    graph.add_edges_from([((target, direction, steps), target)for direction in directions for steps in range(1, 4)], loss=0)
    
    return graph
    
def calculate_minimum_loss(graph, source, target):
    #Find the optimal path using Dijkstra's algorithm (thanks Lennard)
    heat_loss = 0
    shortest_path = nx.dijkstra_path(graph, source, target, weight='loss')
    for edge in zip(shortest_path[:-1], shortest_path[1:]):
        heat_loss += graph.edges[edge]['loss']
    return heat_loss

def main():
    name = "input"

    data = np.array([[int(char) for char in line.rstrip()] for line in open("inputs/day17/{}.txt".format(name))])
    
    source = (0, 0)
    target = (data.shape[0]-1, data.shape[1]-1)
    
    #Calculate heat loss for max. steps 3 (task 1)
    print("Minimum heat loss (task 1):", calculate_minimum_loss(make_graph(data, max_steps=3), source, target))
    
    #Calculate heat loss for min. steps 4, max. steps 10 (task 2)
    print("Minimum heat loss (task 2):", calculate_minimum_loss(make_graph(data, max_steps=10, min_steps=4), source, target))
    
if __name__ == "__main__":
    sys.exit(main())
