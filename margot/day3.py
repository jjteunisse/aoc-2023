import numpy as np
import re
import sys

Environment = dict()

class Number():
    def __init__(self, value:int, row:int, start:int):
        self.value = value
        self.row = row
        self.start = start
        
    @property
    def length(self):
        return len(str(self.value))
        
    @property
    def end(self):
        return self.start + self.length

def environment(data, row:int, start:int, end:int) -> Environment:
    env = {}
    
    if start > 0:
        left = start-1
        env[(row, left)] = data[row, left]
    else:
        left = 0
    
    if end < data.shape[1]:
        right = end+1
        env[(row, right-1)] = data[row, right-1]
    else:
        right = data.shape[1]
        
    if row > 0:
        top = row-1
        for col in range(left, right):
            env[(top, col)] = data[top, col]
    
    if row < data.shape[0]-1:
        bot = row+1
        for col in range(left, right):
            env[(bot, col)] = data[bot, col]
    
    return env
    
def is_part(data, number:Number) -> bool:
    env = environment(data, number.row, number.start, number.end)
    return any(not (char.isalnum() or char == ".") for char in env.values())

def __main__():
    name = "input"

    data = np.array([list(line.strip("\n")) for line in open("inputs/day3/{}.txt".format(name))])

    sum_part_numbers = 0 

    pattern = re.compile("\d+")

    part_numbers = []
    for row in range(data.shape[0]):
        line = "".join(data[row]).strip("\n")
        for match in pattern.finditer(line):
            number = Number(int(match.group(0)), row, match.start(0))
            if is_part(data, number):
                part_numbers.append(number)

    print("Sum of part numbers:", sum(number.value for number in part_numbers))

    sum_gear_ratios = 0
    for gear in zip(*np.where(data == "*")):
        adjacent_parts = [number for number in part_numbers if gear in environment(data, number.row, number.start, number.end)]

        if len(adjacent_parts) == 2:
            gear_ratio = adjacent_parts[0].value*adjacent_parts[1].value
            sum_gear_ratios += gear_ratio
            
    print("Sum of gear ratios:", sum_gear_ratios)
    
if __name__ == "__main__":
    sys.exit(__main__())