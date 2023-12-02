import numpy as np

name = "input"

sum_identifiers = 0
sum_powers = 0
with open("inputs/day2/{}.txt".format(name)) as file:
    for line in file:
        key, value = line.split(":")
        _, identifier = key.split()
        highest_qty = {'red':0, 'blue':0, 'green':0}
        for hand in value.split(";"):
            for colour_group in hand.split(','):
                qty, colour = colour_group.split()
                qty = int(qty)
                colour = colour.strip()
                if qty > highest_qty[colour]:
                    highest_qty[colour] = qty
        sum_powers += np.product(list(highest_qty.values()))

        max_qty = {'red':12, 'green':13, 'blue':14}
        if all(highest_qty[colour] <= max_qty[colour] for colour in max_qty):
           sum_identifiers += int(identifier)

print(sum_identifiers)
print(sum_powers)