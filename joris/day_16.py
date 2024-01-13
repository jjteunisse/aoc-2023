Grid = list[str]
Tile = list[int, int, str]

def get_entrances(grid: Grid) -> list[Tile]:
	y_max, x_max = len(grid), len(grid[0])
	return (
		[[y, 0, '>'] for y in range(0, y_max)] +
		[[y, x_max - 1, '<'] for y in range(0, y_max)] +
		[[0, x, 'v'] for x in range(x_max)] +
		[[y_max - 1, x, '^'] for x in range(x_max)]
	)

def step(tile: Tile) -> Tile:
	y, x, d = tile
	if   d == '^': return [y - 1, x, d]
	elif d == 'v': return [y + 1, x, d]
	elif d == '>': return [y, x + 1, d]
	elif d == '<': return [y, x - 1, d]
	else: raise Exception('Unknown direction.')

def turn_split(tile: Tile, grid: Grid) -> list[Tile]:
	y, x, d = tile
	match grid[y][x]:
		case '.': return [[y, x, d]]
		case '/':
			if   d == '^': return [[y, x, '>']]
			elif d == 'v': return [[y, x, '<']]
			elif d == '>': return [[y, x, '^']]
			elif d == '<': return [[y, x, 'v']]
			else: raise Exception('Unknown direction.')
		case '\\':
			if   d == '^': return [[y, x, '<']]
			elif d == 'v': return [[y, x, '>']]
			elif d == '>': return [[y, x, 'v']]
			elif d == '<': return [[y, x, '^']]
			else: raise Exception('Unknown direction.')
		case '|':
			if   d in ['>', '<']: return [[y, x, 'v'], [y, x, '^']]
			elif d in ['^', 'v']: return [[y, x, d]]
			else: raise Exception('Unknown direction.')
		case '-':
			if   d in ['^', 'v']: return [[y, x, '>'], [y, x, '<']]
			elif d in ['>', '<']: return [[y, x, d]]
			else: raise Exception('Unknown direction.')
		case _:
			raise Exception('Unknown character.')

def within_bounds(tile: Tile, grid: Grid) -> bool:
	return 0 <= tile[0] < len(grid) and 0 <= tile[1] < len(grid[0])

def run():
	grid = open('inputs/day_16.txt').read().split('\n')
	solutions = []
	for entrance in get_entrances(grid):
		done, todo = [], [entrance]
		while todo != []:
			tile = todo.pop(0)
			done.append(tile)
			todo += [
				step(t) for t in turn_split(tile, grid)
				if within_bounds(step(t), grid) and step(t) not in done
			]
		unique_tiles = set(tuple(x[:2]) for x in done)
		solutions.append((entrance, len(unique_tiles)))
	print(f'The answer to part 1 is: {solutions[0][1]}.')
	print(f'The answer to part 2 is: {max(x[1] for x in solutions)}.')

if __name__ == '__main__':
	run()