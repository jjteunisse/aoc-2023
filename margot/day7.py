import numpy as np

tiers = {(5,):7, (1, 4):6, (2, 3):5, (1, 1, 3):4, (1, 2, 2):3, (1, 1, 1, 2):2, (1, 1, 1, 1, 1):1}

cards = [str(i) for i in range(2, 10)]+['T', 'J', 'Q', 'K', 'A']
card_strengths = {card:i+2 for (i, card) in enumerate(cards)}

name = "input"

scores = []
bids = []

with open("inputs/day7/{}.txt".format(name)) as file:
    for line in file:
        hand = list(line.split()[0])
        bid = int(line.split()[1])

        #Get unique card counts; sort to get rid of permutations
        counts = tuple(sorted(np.unique(hand, return_counts=True)[1]))

        #Convert a hand to a number score for sorting 
        score = sum([tiers[counts]*10**10] + [card_strengths[hand[i]]*10**(2*(4-i)) for i in range(5)])
        
        scores.append(score)
        bids.append(bid)
        
#Task 1
winnings = 0
for rank, bid in enumerate(np.array(bids)[np.argsort(scores)]):
    winnings += (rank+1)*bid
print(winnings)

