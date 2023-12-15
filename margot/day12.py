import itertools

name = "input"

with open("inputs/day12/{}.txt".format(name)) as file:
    for line in file:
        springs = line.split()[0]
        damaged_counts = tuple(int(count) for count in line.split()[1].split(","))
        
        num_springs = len(springs)
        num_damaged = sum(damaged_counts)
        num_undamaged = num_springs - num_damaged