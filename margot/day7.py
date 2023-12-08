import numpy as np

cards = [str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']
card_strengths = {card:i for i, card in enumerate(cards)}

name = 'input' 

with open("inputs/day7/{}.txt".format(name)) as file:
    for line in file:
        strings = line.split()
        hand = list(strings[0])
        bid = int(strings[1])
        
        counts = sorted(list(np.unique(hand, return_counts=True)[1]))
