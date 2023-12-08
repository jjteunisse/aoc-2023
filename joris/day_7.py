def get_card_rank(card: str, *, part: int):
	if part == 2 and card == 'J': return 0
	else:
		ranks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
		return ranks[card] if card in ranks.keys() else int(card)

def run(in_file: str, *, part: int):
	hands = []
	for line in open(in_file).readlines():
		cards, bid = line.rstrip('\n').split(' ')
		key = lambda x: (
			(x != 'J') if part == 2 else tuple(),
			cards.count(x),
			get_card_rank(x, part=part)
		)
		cards_sorted = ''.join(sorted(cards, key=key, reverse=True))

		if part == 2:
			if cards_sorted == 'J' * 5: cards_sorted = 'A' * 5
			else:
				for i in range(cards.count('J')):
					cards_sorted = (cards_sorted[0] + cards_sorted)[:-1]

		hands.append({'initial': cards, 'sorted': cards_sorted, 'bid': bid})

	hands.sort(
		key=lambda x: (
			x['sorted'].count(x['sorted'][0]),
			x['sorted'].count(x['sorted'][3]),
			*[get_card_rank(x['initial'][y], part=part) for y in range(5)]
		),
		reverse=True
	)

	total_winnings = sum([
		int(hand['bid']) * (len(hands) - i) for i, hand in enumerate(hands)
	])

	print(f'The answer to part {part} is: {total_winnings}.')

if __name__ == '__main__':
	in_file = 'inputs/day_7.txt'
	run(in_file, part=1)
	run(in_file, part=2)