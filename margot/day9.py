import numpy as np

name = "input"

sum_extrap = 0
sum_extrap_backwards = 0
with open("inputs/day9/{}.txt".format(name)) as file:
    for line in file:
        numbers = np.array([int(num) for num in line.split()])
        starting_values = [numbers[0]]
        ending_values = [numbers[-1]]
        while not np.all(numbers == 0):
            numbers = np.diff(numbers)
            starting_values.insert(0, numbers[0])
            ending_values.insert(0, numbers[-1])
        
        numbers_forwards = numbers
        for val in starting_values:
            numbers_forwards = np.cumsum([val]+list(numbers_forwards))
            
        sum_extrap += numbers_forwards[-1]
        
        numbers_backwards = np.flip(numbers)
        for val in ending_values:
            numbers_backwards = np.cumsum([val]+list(-numbers_backwards))
            
        sum_extrap_backwards += numbers_backwards[-1]
        
print("Sum of forward-extrapolated values (task 1):", sum_extrap)
print("Sum of backward-extrapolated values (task 2):", sum_extrap_backwards)