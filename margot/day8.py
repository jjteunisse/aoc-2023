import numpy as np
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

current_nodes = [node for node in network if node[2] == 'A']

arrived = False
steps = 0
while not arrived:
    for direction in instructions:
        current_nodes = [network[node]["LR".index(direction)] for node in current_nodes]
        steps += 1
        if all([node[2] == 'Z' for node in current_nodes]):
            arrived = True
            break

print("Required steps(task 2):", steps)