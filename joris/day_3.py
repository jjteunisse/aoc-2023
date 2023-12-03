DEBUG = False

def run(schematic: list[str]):
	# Figure out relevant data for each number.
	number_data = []
	symbol_data = []
	for y, row in enumerate(schematic):
		current_number = ''
		for x, char in enumerate(row):
			if char.isdigit(): current_number += char
			else:
				if char not in ['.', '\n']:
					symbol_data.append({
						'symbol': char,
						'y': y,
						'x': x,
					})
				if current_number != '':
					number_data.append({
						'number': int(current_number),
						'y': y,
						'x_start': x - len(current_number),
						'x_end': x - 1,
					})
					current_number = ''

	# Print the retrieved data.
	if DEBUG:
		for num_dict in number_data: print(num_dict)
		print()
		for sym_dict in symbol_data: print(sym_dict)
		print()

	# For each symbol, check adjacent numbers and add them to the sum.
	# Processed numbers are flagged to prevent duplicate additions.
	# For part 2, duplicates are fine: figure out all adjacent numbers.
	part_sum = 0
	for num_dict in number_data: num_dict['processed'] = False
	for sym_dict in symbol_data:
		sym_dict['adjacent'] = []
		for num_dict in number_data:
			if   num_dict['y'] < sym_dict['y'] - 1: continue
			elif num_dict['y'] > sym_dict['y'] + 1: break
			elif (
					num_dict['x_start'] - 1 <=
					sym_dict['x'] <=
					num_dict['x_end'] + 1
				):
					sym_dict['adjacent'].append(num_dict['number'])
					if not num_dict['processed']:
						part_sum += num_dict['number']
						num_dict['processed'] = True
	print(f'The answer to part 1 is: {part_sum}.')

	# Figure out the gear ratio for part 2.
	gear_ratio = 0
	for sym_dict in [x for x in symbol_data if x['symbol'] == '*']:
		if len(sym_dict['adjacent']) == 2:
			gear_ratio += sym_dict['adjacent'][0] * sym_dict['adjacent'][1]
	print(f'The answer to part 2 is: {gear_ratio}.')


if __name__ == '__main__':
	# Read and print the schematic.
	schematic = open('./inputs/day_3.txt').readlines()
	if DEBUG:
		for line in schematic: print(line, end='')
		print('\n')

	run(schematic)