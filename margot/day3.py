import numpy as np
import re

def environment(data, row:int, start:int, end:int):
    env = []
    
    if start > 0:
        left = start-1
        env += [data[row, left],]
    else:
        left = 0
    
    if end < data.shape[1]:
        right = end+1
        env += [data[row, right-1]]
    else:
        right = data.shape[1]
        
    if row > 0:
        top = row-1
        env += list(data[top, left:right])
    
    if row < data.shape[0]-1:
        bot = row+1
        env += list(data[bot, left:right])
    
    return env

name = "input"

data = np.array([list(line.strip("\n")) for line in open("inputs/day3/{}.txt".format(name))])

sum_part_numbers = 0 

pattern = re.compile("\d+")

for row in range(data.shape[0]):
    line = "".join(data[row]).strip("\n")
    for match in pattern.finditer(line):
        if any(not (char.isalnum() or char == ".") for char in environment(data, row, match.start(0), match.end(0))):
            part_number = int(match.group(0))
            sum_part_numbers += part_number
            
print("Sum of part numbers:", sum_part_numbers)