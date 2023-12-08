import numpy as np
import re

tiers = {(5,):7, (1, 4):6, (2, 3):5, (1, 1, 3):4, (1, 2, 2):3, (1, 1, 1, 2):2, (1, 1, 1, 1, 1):1}

cards = [str(i) for i in range(2, 10)]+['T', 'J', 'Q', 'K', 'A']
card_strengths = {card:i+2 for (i, card) in enumerate(cards)}

card_strengths_with_jokers = {card: (card_strengths[card] if card != 'J' else 1) for card in card_strengths}

name = "input"

scores = []
scores_with_jokers = []
bids = []

with open("inputs/day7/{}.txt".format(name)) as file:
    for line in file:
        hand = line.split()[0]
        bid = int(line.split()[1])
        bids.append(bid)

        #Get unique cards and counts
        unique_cards, counts = np.unique(list(hand), return_counts=True)
        
        #Sort cards & corresponding cards to get rid of permutations
        unique_cards = unique_cards[np.argsort(counts)]
        counts = tuple(sorted(counts))
        
        #(Task 1) Convert a hand to a number score for sorting 
        score = sum([tiers[counts]*10**10] + [card_strengths[hand[i]]*10**(2*(4-i)) for i in range(5)])
        scores.append(score)
        
        #(Task 2) Convert jokers to the most prevalent non-joker card; this always gives the highest tier
        if (len(unique_cards) > 1 and unique_cards[-1] == "J"):
            sub = unique_cards[-2]
        else:
            sub = unique_cards[-1]
        
        hand_subbed = re.sub("J", sub, hand)
        counts_with_jokers = tuple(sorted((np.unique(list(hand_subbed), return_counts=True)[1])))

        score = sum([tiers[counts_with_jokers]*10**10] + [card_strengths_with_jokers[hand[i]]*10**(2*(4-i)) for i in range(5)])
        scores_with_jokers.append(score)
        
#Task 1
winnings = np.sum([(rank+1)*bid for rank, bid in enumerate(np.array(bids)[np.argsort(scores)])])
print(winnings)

#Task 2
winnings_with_jokers = np.sum([(rank+1)*bid for rank, bid in enumerate(np.array(bids)[np.argsort(scores_with_jokers)])])
print(winnings_with_jokers)

