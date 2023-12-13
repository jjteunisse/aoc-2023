import numpy as np

name = "input"

sum_arrangements = 0
with open("inputs/day12/{}.txt".format(name)) as file:
    for line in file:
        springs = line.split()[0]
        damaged_counts = tuple(int(count) for count in line.split()[1].split(","))
        
        num_springs = len(springs)
        num_damaged = sum(damaged_counts)
        num_undamaged = num_springs - num_damaged
        
        #Determine the number of 'free' springs: these are the undamaged springs, excluding those that must be placed after each sequence
        num_free = num_undamaged - (len(damaged_counts)-1)

        #Construct all possible arrangements for given numbers of damaged springs
        free_counts = np.zeros((num_free+1, len(damaged_counts)), dtype=int)
        free_counts[:, 0] = np.arange(num_free+1)
        for i in range(1, len(damaged_counts)):
            remaining = num_free - np.sum(free_counts[:, :i], axis=1)
            free_counts = np.repeat(free_counts, remaining+1, axis=0)
            free_counts[:, i] = [count for max_count in remaining for count in range(max_count+1)]
        remaining = num_free - np.sum(free_counts, axis=1)

        arrangements = ("".join(["."*free_count + "#"*damaged_count + "."  for (damaged_count, free_count) in zip(damaged_counts[:-1], free_counts[i, :-1])])
                                 + "."*free_counts[i, -1] + "#"*damaged_counts[-1] + "."*remaining[i] 
                                   for i in range(free_counts.shape[0]))
                                   
        #Add all arrangements to sum that match given springs
        for arr in arrangements:
            sum_arrangements += all([val == check if val != '?' else True for (val, check) in zip(springs, arr)])
        
print("Total number of arrangements:", sum_arrangements)