def transposed(universe):
	return [''.join(x) for x in zip(*universe)]

def locate_galaxies(universe):
	galaxies = []
	for y, row in enumerate(universe):
		for x, space in enumerate(row):
			if universe[y][x] == '#': galaxies.append((y, x))
	return galaxies

def run(universe, expansion_factor):
	empty_rows, empty_cols = [], []
	for i, row in enumerate(universe):
		if '#' not in row: empty_rows.append(i)

	universe = transposed(universe)
	for i, row in enumerate(universe):
		if '#' not in row: empty_cols.append(i)
	universe = transposed(universe)

	galaxies = locate_galaxies(universe)

	total_distance = 0
	for i, g1 in enumerate(galaxies):
		for j, g2 in enumerate(galaxies):
			if j > i:
				dupe_rows = [
					x for x in empty_rows
					if min(g1[0], g2[0]) < x < max(g1[0], g2[0])
				]
				dupe_cols = [
					y for y in empty_cols
					if min(g1[1], g2[1]) < y < max(g1[1], g2[1])
				]
				total_distance += (
					abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) +
					len(dupe_rows + dupe_cols) * (expansion_factor - 1)
				)

	return total_distance

if __name__ == '__main__':
	universe = open('inputs/day_11.txt').read().split('\n')
	print(f'The answer to part 1 is: {run(universe, 2)}.')
	print(f'The answer to part 2 is: {run(universe, 1000000)}.')