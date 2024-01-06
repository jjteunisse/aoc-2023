import numpy as np
from typing import Tuple
import time
import sys
        
def count_arrangements(springs:str, damaged_counts:Tuple[int, ...]):
    arrs_per_sequence = {length: {damaged_counts[:i]:0 for i in range(len(damaged_counts)+1)} for length in range(len(springs)+1)}
    
    arrs_per_sequence[0][tuple()] = 1
    for length in range(len(springs)):
        sequences = (seq for seq in arrs_per_sequence[length] if arrs_per_sequence[length][seq] > 0)
        for seq in sequences:
            if seq == damaged_counts:
                if not '#' in springs[length:]:
                    arrs_per_sequence[len(springs)][damaged_counts] += arrs_per_sequence[length][seq]
            else:
                remaining = len(springs[length:])-sum(damaged_counts[len(seq):])-(len(damaged_counts[len(seq):])-1)
                num_damaged = damaged_counts[len(seq)]
                for num_undamaged in range((len(seq)>0), min(springs[length:].find("#"), remaining)+1 if springs[length:].find("#") != -1 else remaining+1):
                    if (not '#' in springs[length:length+num_undamaged] and not '.' in springs[length+num_undamaged:length+num_undamaged+num_damaged]):
                        arrs_per_sequence[length+num_undamaged+num_damaged][seq + (num_damaged,)] += arrs_per_sequence[length][seq]
                        
    return arrs_per_sequence[len(springs)][damaged_counts]

def main():
    timer_start = time.time()
    
    name = "input"

    sum_arrangements = 0
    sum_arrangements_fivefold = 0
    
    with open("inputs/day12/{}.txt".format(name)) as file:
        for line in file:
            springs = line.split()[0]
            damaged_counts = tuple(int(count) for count in line.split()[1].split(","))
            
            #(Task 1) Add all arrangements to sum that match given springs
            sum_arrangements += count_arrangements(springs, damaged_counts)

            #(Task 2) Do the same for the unfolded sequence
            sum_arrangements_fivefold += count_arrangements("?".join([springs]*5), 5*damaged_counts)
            
    timer_end = time.time()
    print("Runtime:", timer_end-timer_start)
                
    print("Total number of arrangements (task 1):", sum_arrangements)
    print("Total number of arrangements (task 2):", sum_arrangements_fivefold)
    
if __name__ == "__main__":
    sys.exit(main())
