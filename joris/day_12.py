Known = dict[dict[str: int]]

def get_valid_positions(string: str, group_size: int) -> list[int]:
	# Returns all (starting) positions where the group fits into the string.

	# Pad the string first, to deal with edge cases efficiently.
	string = '.' + string + '.'

	# Use a sliding window to check whether the string fits.
	n_possible_splits = len(string) - group_size - 1
	valid_splits = []
	for i in range(n_possible_splits):
		window = string[i : i + group_size + 2]
		if (
			window[0] != '#' and
			window[group_size + 1] != '#' and
			'.' not in window[1 : group_size + 1]
		):
			valid_splits.append(i)

	return valid_splits

def solve(
	string: str, groups: tuple[str], known: Known = {}, depth: int = 0
) -> int:
	# Recursive function that uses a divide & conquer strategy.
	# Returns the number of ways the groups fit into the string.

	# Strip the ends of the string for easier duplicate detection.
	string = string.strip('.')

	# Base cases: in which situations are we sure of the solution?
	# Tried smarter checks as well, but the time saved didn't outweigh the cost.
	if   groups == tuple() and string != '': return 0 if '#' in string else 1
	elif groups == tuple() and string == '': return 1
	elif groups != tuple() and string == '': return 0
	elif groups in known and string in known[groups]: return known[groups][string]
	elif sum(groups) < string.count('#'): return 0
	elif sum(groups) + len(groups) - 1 > len(string): return 0
	else:
		# Induction step: find the largest group and remove it from the string,
		# then solve the left and right remainders.
		max_size = max(groups)
		max_idx = groups.index(max_size)

		# Get all positions where the group fits into the string.
		valid_positions = get_valid_positions(string, max_size)
		if not valid_positions: return 0

		# List all possible split strings based on the valid positions.
		# Note: the extra slice accounts for the space around the group.
		split_strings = [
			[string[:i][:-1], string[i + max_size:][1:]]
			for i in valid_positions
		]

		# Divide the remaining groups, skipping the group itself.
		groups_left = groups[:max_idx]
		groups_right = groups[max_idx:][1:]

		# Solve both remaining sides, then multiply the results.
		n_arrangements = 0
		for string_pair in split_strings:
			n_left = solve(string_pair[0], groups_left, known, depth + 1)
			n_right = solve(string_pair[1], groups_right, known, depth + 1)
			n_arrangements += n_left * n_right

		# Add the configuration to the list of known results.
		if groups not in known:
			known[groups] = {}
		if string not in known[groups]:
			known[groups][string] = n_arrangements

		return n_arrangements

def run(record: list[str], *, part: int):
	total_arrangements = 0
	for line_nr, line in enumerate(record):
		print(f'Progress: {line_nr} / {len(record)}', end='\r')

		string, groups = line.split(' ')
		if part == 2:
			string = '?'.join([string] * 5)
			groups = ','.join([groups] * 5)
		groups = tuple([int(x) for x in groups.split(',')])

		total_arrangements += solve(string, groups)

	print(f'The answer to part {part} is: {total_arrangements}.')

if __name__ == '__main__':
	record = open('inputs/day_12.txt').read().split('\n')
	run(record, part=1)
	run(record, part=2)