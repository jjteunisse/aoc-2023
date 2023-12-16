import colorama, math

Point = tuple[int, int]

class Sketch:
	def __init__(self, sketch: list[str]):
		self.tiles = {
			(y, x): value
			for y, line in enumerate(sketch)
			for x, value in enumerate(line)
		}
		self.max = {'y': len(sketch), 'x': len(sketch[0])}

	def get_valid_directions(self, pipe: str):
		if pipe == 'S':   return [(-1, 0), (0, 1), (1, 0), (0, -1)]
		elif pipe == '|': return [(-1, 0), (1, 0)]
		elif pipe == '-': return [(0, -1), (0, 1)]
		elif pipe == 'L': return [(-1, 0), (0, 1)]
		elif pipe == 'J': return [(-1, 0), (0, -1)]
		elif pipe == 'F': return [(0, 1), (1, 0)]
		elif pipe == '7': return [(0, -1), (1, 0)]
		else: raise Exception()

	def is_connected_pipe(
		self, pipe: str, new_pipe: str, direction: Point
	) -> bool:
		if direction == (-1, 0):
			return pipe in ['S', '|', 'L', 'J'] and new_pipe in ['|', '7', 'F']
		elif direction == (0, 1): 
			return pipe in ['S', '-', 'L', 'F'] and new_pipe in ['-', 'J', '7']
		elif direction == (1, 0): 
			return pipe in ['S', '|', '7', 'F'] and new_pipe in ['|', 'L', 'J']
		elif direction == (0, -1):
			return pipe in ['S', '-', 'J', '7'] and new_pipe in ['-', 'L', 'F']
		else:
			raise Exception()

	def print(self):
		for y in range(self.max['y']):
			for x in range(self.max['x']):
				if (y, x) in self.tiles:
					if self.tiles[(y, x)] == 'O':
						print(colorama.Fore.GREEN + self.tiles[(y, x)], end='')
					elif self.tiles[(y, x)] == 'I':
						print(colorama.Fore.RED + self.tiles[(y, x)], end='')
					else:
						print(colorama.Fore.WHITE + self.tiles[(y, x)], end='')
			print()
		print()

if __name__ == '__main__':
	colorama.init()

	sketch = open('inputs/day_10.txt').read().split('\n')
	S = Sketch(sketch)

	# Trace the pipeline and answer part 1.
	# TODO: Lots of redundancy, currently.
	tile = [key for key, value in S.tiles.items() if value == 'S'][0]
	history = []
	done = False
	while not done:
		history.append(tile)
		valid_directions = S.get_valid_directions(S.tiles[tile])
		for direction in valid_directions:
			new_tile = (tile[0] + direction[0], tile[1] + direction[1])
			if new_tile in S.tiles and S.tiles[new_tile] != '.':
				if len(history) != 2 and S.tiles[new_tile] == 'S':
					done = True
					break
				elif new_tile not in history:
					if S.is_connected_pipe(
						S.tiles[tile], S.tiles[new_tile], direction
					):
						tile = new_tile
						break

	print(f'The answer to part 1 is: {math.ceil(len(history) / 2)}.')

	# Note: This is the point I didn't feel like OOP anymore.

	# Clean up the sketch.
	S.tiles[history[0]] = '|' # TODO: Determine this automatically.
	for key in S.tiles.keys():
		if key not in history:
			S.tiles[key] = '.'
	S.print()

	# Create a map of tile intersections: the value represents whether
	# there exists a path to outside the loop.
	intersections = []
	for y in range(S.max['y'] + 1):
		row = []
		for x in range(S.max['x'] + 1):
			if y in [0, S.max['y']] or x in [0, S.max['x']]:
				row.append(True)
			else:
				row.append(False)
		intersections.append(row)

	# Loop through the intersections, check if they're out- or inside the loop.
	north_south_blocks = ['--', 'L7', 'FJ', 'F-', '-7', 'F7', 'L-', '-J', 'LJ']
	east_west_blocks   = ['||', '7L', 'FJ', '7|', '|J', '7J', 'F|', '|L', 'FL']
	n_changes = 1 # Not really, but we'll accept that for now :p
	while n_changes > 0:
		n_changes = 0
		iteration = 0
		while iteration < S.max['y'] / 2:
			for i, row in enumerate(intersections):
				for j, cross in enumerate(row):
					if not cross:
						# Check all directions for blockades.
						north = S.tiles[(i-1, j-1)] + S.tiles[(i-1, j)]
						east = S.tiles[(i-1, j)] + S.tiles[(i, j)]
						south = S.tiles[(i, j-1)] + S.tiles[(i, j)]
						west = S.tiles[(i-1, j-1)] + S.tiles[(i, j-1)]
						if (
							(north not in north_south_blocks and
							intersections[i-1][j])
							or
							(east not in east_west_blocks and
							intersections[i][j+1])
							or
							(south not in north_south_blocks and
							intersections[i+1][j])
							or
							(west not in east_west_blocks and
							intersections[i][j-1])
						):
							# No blockade, path to outside found.
							intersections[i][j] = True
							n_changes += 1
			iteration += 1

		# Print the intersection map every loop.
		for row in intersections:
			for cross in row:
				print(int(cross), end='')
			print()
		print(f'Number of changes this loop: {n_changes}.')
		print()

	# Replace the map of tiles with O/I for outside / inside.
	for y in range(S.max['y']):
		for x in range(S.max['x']):
			if S.tiles[(y, x)] == '.':
				if (intersections[y][x] == 1 or
					intersections[y][x+1] == 1 or
					intersections[y+1][x] == 1 or
					intersections[y+1][x+1] == 1
				):
					S.tiles[(y, x)] = 'O'
				else:
					S.tiles[(y, x)] = 'I'

	# Print the final version of the sketch.
	S.print()

	# Sum the number of I's for the answer to part 2.
	print(
		colorama.Fore.WHITE + f'The answer to part 2 is: ' +
		f'{sum([1 for val in S.tiles.values() if val == "I"])}.'
	)