import numpy as np
from typing import List, Tuple

Mapping = List[Tuple[int, int, int]]

def read_seeds(seed_line:str):
    header, content = seed_line.split(":")
    seed_numbers = np.array([int(number) for number in content.split()])
    return seed_numbers

def read_map(lines:List[str])-> Mapping:
    return [tuple(int(number) for number in line.rstrip().split()) for line in lines]
    
def map_source_to_destination(source_numbers:Tuple[int, ...], mapping:Mapping) -> Tuple[int, ...]:
    destination_numbers = source_numbers.copy()
    for i, number in enumerate(source_numbers):
        for (destination_range_start, source_range_start, range_length) in mapping:
            if (number >= source_range_start and number < source_range_start + range_length):
                destination_numbers[i] = destination_range_start + number - source_range_start
                break

    return destination_numbers

name = "input"

with open("inputs/day5/{}.txt".format(name)) as file:
    seed_line = next(file)
    seed_numbers = read_seeds(seed_line)
    numbers = seed_numbers
    next(file)
    
    check=True
    while check:
        header = next(file)
        lines = []
        line = next(file)
        while any(line.rstrip()):
            lines += [line]
            try:
               line = next(file)
            except StopIteration:
               check = False
               break
        mapping = read_map(lines)
            
        #Map source to destination; assumes that previous output is current input
        numbers = map_source_to_destination(numbers, mapping)
            
    location_numbers = numbers
    print("Lowest location number:", min(location_numbers))