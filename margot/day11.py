import numpy as np

name = "input"

skydat = np.array([list(line.rstrip()) for line in open("inputs/day11/{}.txt".format(name))])

#Apply expansion
expanded_skydat = np.repeat(skydat, repeats=2**np.all(skydat == '.', axis=1), axis=0)
expanded_skydat = np.repeat(expanded_skydat, repeats=2**np.all(skydat == '.', axis=0), axis=1)

#Assign numbers to all galaxies
mask = (expanded_skydat == "#")
locs = {identifier: (i, j) for identifier, (i, j) in enumerate(zip(*np.where(mask)))}

#Calculate all distances between galaxies
sum_distances = 0
pairs = np.triu_indices(len(locs), k=1)
for (id1, id2) in zip(*pairs):
    loc1, loc2 = locs[id1], locs[id2]
    sum_distances += abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])
    
print("Sum of distances between galaxies (task 1):", sum_distances)

