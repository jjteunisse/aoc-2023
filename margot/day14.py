import numpy as np

name = "input"

platform = np.array([list(line.rstrip()) for line in open("inputs/day14/{}.txt".format(name))])

round_rocks = {identifier:(i, j) for identifier, (i, j) in enumerate(zip(*np.where(platform == "O")))}

shifted = True
direction = (-1, 0)
while shifted:
    shifted = False
    for identifier in round_rocks:
        i, j = round_rocks[identifier]
        if all([i+direction[0] >= 0, i+direction[0] < platform.shape[0], j+direction[1] >= 0, j+direction[1] < platform.shape[1]]):
            if platform[i+direction[0], j+direction[1]] == ".":
                shifted = True
                platform[i, j], platform[i+direction[0], j+direction[1]] = ".", "O"
                round_rocks[identifier] = (i+direction[0], j+direction[1])

north_load = np.sum([platform.shape[0]-round_rocks[identifier][0] for identifier in round_rocks])
print("Load on north side of platform (task 1):", north_load)