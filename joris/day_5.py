import re, time

DEBUG = False

def part_1():
	# Read all lines in the almanac.
	almanac = [
		line.rstrip('\n') for line
		in open('inputs/day_5.txt').readlines()
	]

	# Get the initial numbers, represented by the seeds.
	numbers = {
		'old': None,
		'new': [int(x) for x in re.findall(r'\d+', almanac[0])]
	}

	# Walk through the almanac.
	for line in almanac[1:]:
		# If the line is empty, we're entering a new map.
		# Replace the old numbers by the new ones.
		if line == '':
			numbers['old'] = numbers['new'].copy()
		# If it's a map, pass - this information is irrelevant.
		elif 'map' in line:
			pass
		else:
			# Otherwise, we need to get on with this converting business.
			dst, src, l = (int(x) for x in line.split(' '))
			for i, num in enumerate(numbers['old']):
				if num in range(src, src + l):
					numbers['new'][i] += dst - src

	print(f'The answer to part 1 is: {min(numbers["new"])}.')

def part_2():
	# Read all lines in the almanac.
	almanac = [
		line.rstrip('\n') for line
		in open('inputs/day_5.txt').readlines()
	]

	# Get the initial number ranges, represented by the seeds.
	pairs = re.findall(r'\d+ \d+', almanac[0])
	number_ranges = []
	for pair in pairs:
		start = int(pair.split(' ')[0])
		length = int(pair.split(' ')[1])
		number_ranges.append({'start': start, 'end': start + length})
	if DEBUG: print('Initial ranges: ' + str(number_ranges))

	# Modify the almanac, such that it only contains the number ranges
	# and the whitespace in between. Also add a blank line at the end.
	almanac = [x for x in almanac if 'map' not in x][2:]
	almanac.append('')

	# Go through the revised almanac.
	operations = []
	for i, line in enumerate(almanac):
		if line == '':
			# Base case: if the line is blank, this is the end of the map.
			# Apply all operations we retrieved from it and reset.
			# It is assumed that all operations target unique ranges.
			ranges_to_consider = number_ranges.copy()
			ranges_modded = []
			for op in operations:
				# For each operation, do the following:
				# * Try to apply the operation to each number range.
				# * If it can be applied, split the range between a modified
				#   part, and a part that still needs to be considered.
				ranges_todo = []
				if DEBUG: print('Next operation:', op)
				for rng in ranges_to_consider:
					if DEBUG: print('Apply to range:', rng)
					# Case 1: The operation and number range are disjoint.
					if rng['start'] >= op['end'] or rng['end'] <= op['start']:
						if DEBUG: print('Disjoint.')
						ranges_todo.append(rng.copy())
					# Case 2: The operation applies from start to end.
					elif rng['start'] >= op['start'] and rng['end'] <= op['end']:
						if DEBUG: print('Start to end.')
						ranges_modded.append({
							'start': rng['start'] + op['increment'],
							'end': rng['end'] + op['increment']
						})
					# Case 3: The operation applies from start to middle.
					elif rng['start'] >= op['start'] and rng['end'] > op['end']:
						if DEBUG: print('Start to middle.')
						ranges_modded.append({
							'start': rng['start'] + op['increment'],
							'end': op['end'] + op['increment']
						})
						ranges_todo.append({
							'start': op['end'], 'end': rng['end']
						})
					# Case 4: The operation applies from middle to end.
					elif rng['start'] < op['start'] and rng['end'] <= op['end']:
						if DEBUG: print('Middle to end.')
						ranges_todo.append({
							'start': rng['start'], 'end': op['start']
						})
						ranges_modded.append({
							'start': op['start'] + op['increment'],
							'end': rng['end'] + op['increment']
						})
					# Case 5: The operations applies from middle to middle.
					elif rng['start'] < op['start'] and rng['end'] > op['end']:
						if DEBUG: print('Middle to middle.')
						ranges_todo.append({
							'start': rng['start'], 'end': op['start']
						})
						ranges_modded.append({
							'start': op['start'] + op['increment'],
							'end': op['end'] + op['increment']
						})
						ranges_todo.append({
							'start': op['end'], 'end': rng['end']
						})
					else:
						raise Exception('Unknown range case occurred.')

				# After applying the operation to all ranges that needed,
				# to be considered, update that list for the next iteration.
				ranges_to_consider = ranges_todo.copy()

			# After applying all operations, update and sort the number ranges.
			# The ranges_to_consider list represents the unmodded ranges.
			# Also, reset the list of operations.
			number_ranges = ranges_to_consider + ranges_modded
			number_ranges.sort(key=lambda x: x['start'])
			operations = []

			if DEBUG: print(f'Resulting ranges:', number_ranges); print()
			if i == len(almanac) - 1:
				# Print the answer if we have reached the end of the almanac.
				print(f'The answer to part 2 is: {number_ranges[0]["start"]}.')

		else:
			# If the line is not blank, we've encountered an operation.
			# Append it to the list of operations we need to carry out.
			range_dst = int(line.split(' ')[0])
			range_src = int(line.split(' ')[1])
			range_len = int(line.split(' ')[2])
			operations.append({
				'start':     range_src,
				'end':       range_src + range_len,
				'increment': range_dst - range_src
			})

if __name__ == '__main__':
	start_time = time.time()
	part_1()
	part_2()
	print(f'The program took {time.time() - start_time:.4f} seconds.')