import numpy as np
from typing import List, Tuple

Mapping = List[Tuple[int, int, int]]
Range = Tuple[int, int]

def read_seeds(seed_line:str):
    header, content = seed_line.split(":")
    seed_numbers = np.array([int(number) for number in content.split()])
    return seed_numbers
    
def read_seeds_ranges(seed_line:str) -> List[Range]:
    header, content = seed_line.split(":")
    numbers = [int(number) for number in content.split()]

    seed_ranges = [(start, length) for (start, length) in zip(numbers[::2], numbers[1::2])]
    return seed_ranges

def read_map(lines:List[str])-> Mapping:
    return [tuple(int(number) for number in line.rstrip().split()) for line in lines]
    
def overlap(range1:Range, range2:Range) -> Range:
    start1, length1 = range1
    start2, length2 = range2 
    
    overlap_start = max(start1, start2)
    overlap_end = min(start1+length1, start2+length2)
    overlap_length = overlap_end - overlap_start
    overlap = (overlap_start, overlap_length)
    
    return overlap

def map_source_to_destination(source_numbers:Tuple[int, ...], mapping:Mapping) -> Tuple[int, ...]:
    destination_numbers = source_numbers.copy()
    for i, number in enumerate(source_numbers):
        for (destination_range_start, source_range_start, range_length) in mapping:
            if (number >= source_range_start and number < source_range_start + range_length):
                destination_numbers[i] = destination_range_start + number - source_range_start
                break

    return destination_numbers
    
def map_source_to_destination_ranges(source_ranges:List[Range], mapping:Mapping) -> List[Range]:
    destination_ranges = []
    for (destination_range_start, source_range_start, range_length) in mapping:
        residuals = []
        for source_range in source_ranges:
            overlap_start, overlap_length = overlap(source_range, (source_range_start, range_length))
            if overlap_length > 0:
                destination_ranges += [(destination_range_start + overlap_start - source_range_start, overlap_length)]
                cutting_left = (source_range[0], overlap_start - source_range[0])
                if cutting_left[1] > 0:
                    residuals += [cutting_left]
                cutting_right = (overlap_start + overlap_length, source_range[0]-overlap_start + source_range[1]-overlap_length)
                if cutting_right[1] > 0:
                    residuals += [cutting_right]
            else:
                residuals += [source_range]
        source_ranges = residuals
        
    destination_ranges += residuals
                
    return destination_ranges

name = "input"

with open("inputs/day5/{}.txt".format(name)) as file:
    seed_line = next(file)
    seed_numbers = read_seeds(seed_line)
    seed_ranges = read_seeds_ranges(seed_line)
    numbers = seed_numbers
    ranges = seed_ranges
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
        ranges = map_source_to_destination_ranges(ranges, mapping)
            
    location_numbers = numbers
    print("Lowest location number (task 1):", min(location_numbers))
    
    location_ranges = ranges
    print("Lowest location number (task 2):", min([start for (start, length) in location_ranges]))