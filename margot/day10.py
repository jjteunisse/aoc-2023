import numpy as np

name = "input"

mapping = {'.':set(), 'L':{(-1, 0), (0, 1)}, 'J':{(-1, 0), (0, -1)}, 'F':{(1, 0), (0, 1)}, 
           '7': {(1, 0), (0, -1)}, '-':{(0, -1), (0, 1)}, '|':{(-1, 0), (1, 0)}, 'S':set()}

schematic = np.array([list(line.rstrip()) for line in open("inputs/day10/{}.txt".format(name))])

starting_loc = tuple(coord[0] for coord in np.where(schematic == 'S'))

i, j = starting_loc

#(Task 2) Save vertices and 'walls' to help calculate the enclosed area
vertices = []
vertical_walls = np.zeros_like(schematic, dtype=bool)
horizontal_walls = np.zeros_like(schematic, dtype=bool)

#Determine what type of pipe is beneath S. 
for direction in {(1, 0), (-1, 0), (0, -1), (0, 1)}:
    if (-direction[0], -direction[1]) in mapping[schematic[i+direction[0], j+direction[1]]]:
        mapping['S'].add(direction)
        
for char in set(mapping.keys()) - {'.', 'S'}:
    if mapping['S'] == mapping[char]:
        schematic[i, j] = char
        if char in {'L', 'J', 'F', '7'}:
            vertices.append(starting_loc)
        break

#To start walking the loop, pick a random direction.
direction = next(iter(mapping['S']))
i, j = i+direction[0], j+direction[1]
if (1, 0) in mapping[schematic[i, j]] or (-1, 0) in mapping[schematic[i, j]]:
    vertical_walls[i, j] = True
if (0, 1) in mapping[schematic[i, j]] or (0, -1) in mapping[schematic[i, j]]:
    horizontal_walls[i, j] = True

#Walk the entire loop to find its period.
period = 1
while (i, j) != starting_loc:
    if schematic[i, j] in {'L', 'J', 'F', '7'}:
        vertices.append((i, j))
    #Pick the direction that doesn't lead you to go backwards.
    direction = next(iter(mapping[schematic[i, j]]-{(-direction[0], -direction[1])}))
    #Update position.
    i, j = i+direction[0], j+direction[1]
    if (1, 0) in mapping[schematic[i, j]] or (-1, 0) in mapping[schematic[i, j]]:
        vertical_walls[i, j] = True
    if (0, 1) in mapping[schematic[i, j]] or (0, -1) in mapping[schematic[i, j]]:
        horizontal_walls[i, j] = True
    period += 1

#(Task 1) Since S lies on a loop, the farthest point from S lies a half-period away.
print("Steps to farthest point (task 1):", period//2)

#(Task 2) Correct walls at the corners and calculate the enclosed area
for vertex1, vertex2 in zip(vertices, vertices[1:]+[vertices[0]]):
    if any([{schematic[vertex1], schematic[vertex2]} == check for check in ({'L', '7'}, {'J','F'})]):
        if vertex1[0] == vertex2[0]:
            vertical_walls[vertex2] = False
        if vertex1[1] == vertex2[1]:
            horizontal_walls[vertex2] = False

enclosed = (np.cumsum(vertical_walls, axis=1)%2 == 1)*(np.cumsum(horizontal_walls, axis=0)%2 == 1)*np.invert(horizontal_walls)*np.invert(vertical_walls)
print("Area enclosed by loop (task 2):", np.sum(enclosed))