import numpy as np
import sys

def read_highest_qty(hands:str):
    highest_qty = {'red':0, 'blue':0, 'green':0}
    
    for hand in hands.split(";"):
        for colour_group in hand.split(','):
            qty, colour = colour_group.split()
            qty = int(qty)
            colour = colour.strip()
            if qty > highest_qty[colour]:
                highest_qty[colour] = qty
    
    return highest_qty

def __main__():
    name = "input"

    sum_identifiers = 0
    sum_powers = 0
    with open("inputs/day2/{}.txt".format(name)) as file:
        for line in file:
            header, hands = line.split(":")
            _, identifier = header.split()
            identifier = int(identifier)
            
            highest_qty = read_highest_qty(hands)
            
            max_qty = {'red':12, 'green':13, 'blue':14}
            if all(highest_qty[colour] <= max_qty[colour] for colour in max_qty):
                sum_identifiers += identifier
                
            sum_powers += np.product(list(highest_qty.values()))

    print("Sum of identifiers matching requirement:", sum_identifiers)
    print("Sum of powers:", sum_powers)
    
if __name__ == "__main__":
    sys.exit(__main__())