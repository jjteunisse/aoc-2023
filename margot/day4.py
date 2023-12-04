import numpy as np

name = "input"

score = 0
with open("inputs/day4/{}.txt".format(name)) as file:
    for line in file:
        header, content = line.split(":")
        winning_numbers, numbers = content.split("|")
        winning_numbers = np.array(winning_numbers.split()).astype(int)
        numbers = np.array(numbers.split()).astype(int)
        
        numbers_match_to_winning = winning_numbers[np.newaxis] == numbers[:, np.newaxis]
        
        wins = np.sum(numbers_match_to_winning)
        
        if wins == 0:
            points = 0
        else:
            points = 2**(wins-1)
        
        score += points
        
print(score)