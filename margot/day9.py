import numpy as np

name = "input"

sum_extrap = 0
with open("inputs/day9/{}.txt".format(name)) as file:
    for line in file:
        numbers = np.array([int(num) for num in line.split()])
        starting_values = [numbers[0]]
        while not np.all(numbers == 0):
            numbers = np.diff(numbers)
            starting_values.insert(0, numbers[0])
        
        for val in starting_values:
            numbers = np.cumsum([val]+list(numbers))
            
        sum_extrap += numbers[-1]
        
print(sum_extrap)