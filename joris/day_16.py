Dims = tuple[int]
Grid = list[str]
Tile = tuple[int, int, str]

def get_entrances(dims: Dims) -> list[Tile]:
	return (
		[(y, 0, '>') for y in range(0, dims[0])] +
		[(y, dims[1] - 1, '<') for y in range(0, dims[0])] +
		[(0, x, 'v') for x in range(dims[1])] +
		[(dims[0] - 1, x, '^') for x in range(dims[1])]
	)

def init_done(dims: Dims) -> dict[Tile: bool]:
	return {
		(y, x, d): False
		for y in range(dims[0])
		for x in range(dims[1])
		for d in ['>', '<', 'v', '^']
	}

def step(tile: Tile) -> Tile:
	y, x, d = tile
	if   d == '>': return (y, x + 1, d)
	elif d == '<': return (y, x - 1, d)
	elif d == 'v': return (y + 1, x, d)
	elif d == '^': return (y - 1, x, d)
	else: raise Exception('Unknown direction.')

def turn_split(tile: Tile, grid: Grid) -> list[Tile]:
	y, x, d = tile
	match grid[y][x]:
		case '.': return [(y, x, d)]
		case '/':
			if   d == '>': return [(y, x, '^')]
			elif d == '<': return [(y, x, 'v')]
			elif d == 'v': return [(y, x, '<')]
			elif d == '^': return [(y, x, '>')]
			else: raise Exception('Unknown direction.')
		case '\\':
			if   d == '>': return [(y, x, 'v')]
			elif d == '<': return [(y, x, '^')]
			elif d == 'v': return [(y, x, '>')]
			elif d == '^': return [(y, x, '<')]
			else: raise Exception('Unknown direction.')
		case '|':
			if   d in ['>', '<']: return [(y, x, 'v'), (y, x, '^')]
			elif d in ['v', '^']: return [(y, x, d)]
			else: raise Exception('Unknown direction.')
		case '-':
			if   d in ['>', '<']: return [(y, x, d)]
			elif d in ['v', '^']: return [(y, x, '>'), (y, x, '<')]
			else: raise Exception('Unknown direction.')
		case _:
			raise Exception('Unknown character.')

def within_bounds(tile: Tile, dims: Dims) -> bool:
	return 0 <= tile[0] < dims[0] and 0 <= tile[1] < dims[1]

def run():
	grid = open('inputs/day_16.txt').read().split('\n')
	dims = (len(grid), len(grid[0]))
	done = init_done(dims)
	solutions = {}
	for entrance in get_entrances(dims):
		done, todo, unique = dict.fromkeys(done, False), [entrance], set()
		while todo != []:
			tile = todo.pop(0)
			done[tile] = True
			unique.add(tile[:2])
			for next_tile in turn_split(tile, grid):
				next_tile = step(next_tile)
				if within_bounds(next_tile, dims):
					if not done[next_tile]:
						todo.append(next_tile)
		solutions[entrance] = len(unique)
	print(f'The answer to part 1 is: {solutions[(0, 0, ">")]}.')
	print(f'The answer to part 2 is: {max(solutions.values())}.')

if __name__ == '__main__':
	run()