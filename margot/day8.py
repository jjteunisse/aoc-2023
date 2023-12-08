import re

name = "input"

pattern = re.compile("\w\w\w")

network = {}
steps = 0
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
while not arrived:
    for direction in instructions:
        current_node = network[current_node]["LR".index(direction)]
        steps += 1
        if current_node == 'ZZZ':
            arrived = True

print(steps)