import re, sys

def part_1(data):
	game_id_sum = 0
	max_cubes = { 'red': 12, 'green': 13, 'blue': 14 }
	for line in open('./inputs/' + data + '.txt').readlines():
		match = re.match(r'Game (\d+): (.*)', line)
		game_id = int(match.group(1))
		sets = match.group(2).split('; ')
		valid_game = True
		for s in sets:
			for combo in s.split(', '):
				amount, color = combo.split(' ')
				if int(amount) > max_cubes[color]:
					valid_game = False
		if valid_game: game_id_sum += game_id

	print(f'Answer to part 1: {game_id_sum}')

def part_2(data):
	power_sum = 0
	for line in open('./inputs/' + data + '.txt').readlines():
		match = re.match(r'Game (\d+): (.*)', line)
		sets = match.group(2).split('; ')
		min_cubes = { 'red': 0, 'green': 0, 'blue': 0 }
		for s in sets:
			for combo in s.split(', '):
				amount, color = combo.split(' ')
				if int(amount) > min_cubes[color]:
					min_cubes[color] = int(amount)
		set_power = 1
		for amount in min_cubes.values(): set_power *= int(amount)
		power_sum += set_power

	print(f'Answer to part 2: {power_sum}')

if __name__ == '__main__':
	data = 'day_2'
	if len(sys.argv) > 1 and sys.argv[1] == '--test':
		data = 'test_' + data

	part_1(data)
	part_2(data)