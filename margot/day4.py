import numpy as np

name = "input"

score = 0
with open("inputs/day4/{}.txt".format(name)) as file:
    card_counts = []
    card_wins = []

    for line in file:
        header, content = line.split(":")
        winning_numbers, numbers = content.split("|")
        winning_numbers = np.array(winning_numbers.split()).astype(int)
        numbers = np.array(numbers.split()).astype(int)
        
        numbers_match_to_winning = winning_numbers[np.newaxis] == numbers[:, np.newaxis]
        
        wins = np.sum(numbers_match_to_winning)
        
        card_counts += [1,]
        card_wins += [wins,]
        
        #Count points (task 1)
        if wins == 0:
            points = 0
        else:
            points = 2**(wins-1)
        
        score += points
        
    print("Score:", score)
        
    #Count number of cards (task 2)
    card_counts = np.array(card_counts)
    card_wins = np.array(card_wins)
    for i in range(len(card_counts)):
        card_counts[i+1:i+card_wins[i]+1] += card_counts[i]
        
    print("Total number of cards:", sum(card_counts))
        