import numpy as np

name = "input"

mapping = {'.':set(), 'L':{(-1, 0), (0, 1)}, 'J':{(-1, 0), (0, -1)}, 'F':{(1, 0), (0, 1)}, 
           '7': {(1, 0), (0, -1)}, '-':{(0, -1), (0, 1)}, '|':{(-1, 0), (1, 0)}, 'S':{(1, 0), (-1, 0), (0, -1), (0, 1)}}

schematic = np.array([list(line.rstrip()) for line in open("inputs/day10/{}.txt".format(name))])

starting_loc = tuple(coord[0] for coord in np.where(schematic == 'S'))

i, j = starting_loc
#To start walking the loop, find a direction that connects to a pipe.
for direction in mapping['S']:
    if (-direction[0], -direction[1]) in mapping[schematic[i+direction[0], j+direction[1]]]:
        i, j = i+direction[0], j+direction[1]
        break

#Walk the entire loop to find its period.
period = 1
while (i, j) != starting_loc:
    #Pick the direction that doesn't lead you to go backwards.
    direction = next(iter(mapping[schematic[i, j]]-{(-direction[0], -direction[1])}))
    #Update position.
    i, j = i+direction[0], j+direction[1]
    period += 1

#Since S lies on a loop, the farthest point from S lies a half-period away.
print("Steps to farthest point:", period//2)