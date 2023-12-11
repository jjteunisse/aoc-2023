import numpy as np
import sys

def calculate_sum_distances(skydat, expansion_factor):
    horizontal_expansion = expansion_factor**np.all(skydat == '.', axis=0)
    vertical_expansion = expansion_factor**np.all(skydat == '.', axis=1)

    #Assign numbers to all galaxies
    mask = (skydat == "#")
    locs = {identifier: (i, j) for identifier, (i, j) in enumerate(zip(*np.where(mask)))}

    #Calculate all distances between galaxies
    sum_distances = 0
    pairs = np.triu_indices(len(locs), k=1)
    for (id1, id2) in zip(*pairs):
        loc1, loc2 = locs[id1], locs[id2]
        sum_distances += np.sum(vertical_expansion[min(loc1[0], loc2[0]):max(loc1[0], loc2[0])])
        sum_distances += np.sum(horizontal_expansion[min(loc1[1], loc2[1]):max(loc1[1], loc2[1])])
        
    return sum_distances

def main():
    name = "input"

    skydat = np.array([list(line.rstrip()) for line in open("inputs/day11/{}.txt".format(name))])

    print("Sum of distances for expansion factor 2 (task 1):", calculate_sum_distances(skydat, 2))
    print("Sum of distances for expansion factor 1 million (task 2):", calculate_sum_distances(skydat, 1e6))
    
if __name__ == '__main__':
    sys.exit(main())

