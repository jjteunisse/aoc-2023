import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
import re

name = "input"

pattern = re.compile("\w\w\w")

network = {}
with open("inputs/day8/{}.txt".format(name)) as file:
    instructions = ""
    line = next(file).rstrip()
    while any(line):
        instructions += line
        line = next(file).rstrip()

    for line in file:
        node, left_node, right_node = pattern.findall(line)
        network[node] = (left_node, right_node)
        
#Task 1
if 'AAA' in network:
    current_node = 'AAA'
    arrived = False
    steps = 0
    while not arrived:
        for direction in instructions:
            current_node = network[current_node]["LR".index(direction)]
            steps += 1
            if current_node == 'ZZZ':
                arrived = True
                break

    print("Required steps(task 1):", steps)
    
#Task 2
#Check assumptions about input
starting_nodes = (node for node in network if node[2] == 'A')
periods = []
for node in starting_nodes:
    current_node = node
    arrived = False
    steps = 0
    while not arrived:
        for direction in instructions:
            current_node = network[current_node]["LR".index(direction)]
            steps += 1
            if current_node[2] == 'Z':
                arrived = True
                
                #Check that a 'Z' node is only reached at the end of a set of instructions
                assert steps%len(instructions) == 0
                
                #Check that the output of the 'Z' node is the same as that of the initial 'A' node
                assert network[current_node]["LR".index(instructions[-1])] == network[current_node]["LR".index(instructions[-1])]
                
                periods.append(steps//len(instructions))
                
                break
                
#If the periods are all prime numbers, then the first number divisible by all periods is their product.
#Could write a check for this, but don't really need to since I can check by eye.
print("Required steps (task 2):", np.product(periods, dtype=np.int64)*len(instructions))
