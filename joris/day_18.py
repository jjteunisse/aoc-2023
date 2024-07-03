def convert_direction(direction: str) -> tuple[int]:
	if   direction == 'U': return -1,  0
	elif direction == 'R': return  0,  1
	elif direction == 'D': return  1,  0
	elif direction == 'L': return  0, -1
	else: raise Exception('Unknown direction!')

def run_v1(plan: list[str]):
	y_dim = x_dim = 800

	terrain = []
	for y in range(y_dim):
		char = '@' if y == 0 or y == y_dim - 1 else '.'
		terrain.append(['@'] + [char] * (x_dim - 2) + ['@'])

	pos_y, pos_x = y_dim // 2, x_dim // 2
	terrain[pos_y][pos_x] = '#'
	for line in plan:
		dir_y, dir_x = convert_direction(line.split(' ')[0])
		steps = int(line.split(' ')[1])

		for i in range(steps):
			pos_y += dir_y
			pos_x += dir_x
			terrain[pos_y][pos_x] = '#'

	to_check = [(1, 1)]
	while to_check:
		y, x = to_check.pop(0)
		for direction in ['U', 'R', 'D', 'L']:
			dir_y, dir_x = convert_direction(direction)
			next_y, next_x = y + dir_y, x + dir_x
			if terrain[next_y][next_x] == '.':
				terrain[next_y][next_x] = ' '
				to_check.append((next_y, next_x))

	with open('terrain.txt', 'w') as f:
		for row in terrain:
			print(''.join(row), file=f)

	terrain_str = ''.join([''.join(row) for row in terrain])
	lagoon_size = sum([terrain_str.count(char) for char in ['#', '.']])
	print(f'The answer to part 1 is: {lagoon_size}')

def run_v2(plan: list[str], dirs: list[str], steps: list[int], *, part: int):
	pos_y, pos_x = 0, 0
	h_walls, v_walls = {}, {}
	for i in range(len(plan)):
		if dirs[i] in ['L', 'R']:
			next_i = 0 if i == len(plan) - 1 else i + 1
			w_type = 'h_eq' if dirs[i - 1] != dirs[next_i] else 'h_neq'
			start_x = pos_x if dirs[i] == 'R' else pos_x - steps[i]
			end_x = pos_x if dirs[i] == 'L' else pos_x + steps[i]
			if (pos_y, pos_y) not in h_walls: h_walls[(pos_y, pos_y)] = []
			h_walls[(pos_y, pos_y)].append([w_type, start_x, end_x])
			pos_x = start_x if dirs[i] == 'L' else end_x
		elif dirs[i] in ['U', 'D']:
			start_y = pos_y if dirs[i] == 'D' else pos_y - steps[i]
			end_y = pos_y if dirs[i] == 'U' else pos_y + steps[i]
			if pos_x not in v_walls: v_walls[pos_x] = []
			v_walls[pos_x].append([start_y, end_y])
			pos_y = start_y if dirs[i] == 'U' else end_y

	h_walls = dict(sorted(h_walls.items()))
	prev_key = list(h_walls.keys())[0]
	for hk in list(h_walls.keys())[1:]:
		if hk[0] > prev_key[0] + 1:
			h_walls[(prev_key[0] + 1, hk[0] - 1)] = []
		prev_key = hk

	h_walls = dict(sorted(h_walls.items()))
	v_walls = dict(sorted(v_walls.items()))
	for vk, vv in v_walls.items():
		for y_pair in vv:
			start_y, end_y = y_pair
			for hk, hv in h_walls.items():
				if hk[1] <= start_y: continue
				elif hk[1] < end_y: h_walls[hk].append(['v', vk, vk])
				else: break

	h_walls = dict(sorted(h_walls.items()))
	for hk in h_walls.keys():
		h_walls[hk] = sorted(h_walls[hk], key=lambda x: x[1])

	space = {}
	for hk, hv in h_walls.items():
		space[hk] = 0
		inside = False
		start_x = None
		for wall in hv:
			if inside: space[hk] += wall[1] - start_x
			start_x = wall[2] + 1
			if wall[0] != 'h_eq': inside = not inside
		space[hk] *= hk[1] - hk[0] + 1

	print(f'The answer to part {part} is: {sum(steps) + sum(space.values())}.')

if __name__ == '__main__':
	plan = open('inputs/day_18.txt').read().split('\n')
	# run_v1(plan)

	dirs = [line.split(' ')[0] for line in plan]
	steps = [int(line.split(' ')[1]) for line in plan]
	run_v2(plan, dirs, steps, part=1)

	num_to_dir = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
	colors = [line.split(' ')[2][2:-1] for line in plan]
	dirs = [num_to_dir[int(c[-1])] for c in colors]
	steps = [int(c[:-1], 16) for c in colors]
	run_v2(plan, dirs, steps, part=2)