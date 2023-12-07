import re

if __name__ == '__main__':
	card_pile = open('inputs/day_4.txt').readlines()

	total_points = 0 
	n_copies = [1] * len(card_pile)
	card_rx = re.compile(r'Card [ \d]+: ([\d ]+) \| ([\d ]+)\n?')
	for i, card in enumerate(card_pile):
		# Determine the set of winning and held numbers.
		match = re.match(card_rx, card)
		winning_nums = re.findall(r'\d+', match[1])
		held_nums = re.findall(r'\d+', match[2])

		# Get the number of matching numbers.
		n_winning = [x for x in held_nums if x in winning_nums]

		# PART 1: Add the number of points to the total.
		if len(n_winning) > 0: total_points += 2 ** (len(n_winning) - 1)

		# PART 2: Add the number of current copies to the next cards.
		for j in range(len(n_winning)): n_copies[i + j + 1] += n_copies[i]

	print(f'The answer to part 1 is: {total_points}.')
	print(f'The answer to part 2 is: {sum(n_copies)}.')