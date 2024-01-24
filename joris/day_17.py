from typing import NamedTuple

class State(NamedTuple):
	y: int
	x: int
	d: tuple[int]
	n: int

def get_directions(s: State, min_n: int, max_n: int) -> list[tuple[int]]:
	directions = []
	if s.d == (0, 0):
		directions = [(0, 1), (1, 0)]
	else:
		if s.n < max_n:
			directions += [s.d]
		if s.n >= min_n:
			if s.d[0] == 0:
				directions += [(-1, 0), (1, 0)]
			else:
				directions += [(0, -1), (0, 1)]
	return directions

def run(city: list[str], *, min_n: int, max_n: int) -> int:
	goal = (len(city) - 1, len(city[0]) - 1)
	states = {State(0, 0, (0, 0), 0)}
	losses = {State(0, 0, (0, 0), 0): 0}
	while states:
		print(f'States: {len(states): <6}', end='\r')
		new_states = set()
		for s in states:
			for d_new in get_directions(s, min_n, max_n):
				turn = (d_new != s.d) or (s.n == 0)
				steps = min_n if turn else 1
				y_new = s.y + d_new[0] * steps
				x_new = s.x + d_new[1] * steps
				if 0 <= y_new <= goal[0] and 0 <= x_new <= goal[1]:
					n_new = min_n if turn else s.n + 1
					s_new = State(y_new, x_new, d_new, n_new)
					l_new = losses[s] + city[y_new][x_new]
					for i in range(steps - 1):
						y_new -= d_new[0]
						x_new -= d_new[1]
						l_new += city[y_new][x_new]
					if s_new not in losses or l_new < losses[s_new]:
						losses[s_new] = l_new
						new_states.add(s_new)
		states = new_states
	goal_losses = [v for k, v in losses.items() if (k.y, k.x) == goal]
	return min(goal_losses)

if __name__ == '__main__':
	city = [
		[int(x) for x in line]
		for line in open('inputs/day_17.txt').read().split('\n')
	]
	print(f'The answer to part 1 is: {run(city, min_n=1, max_n=3)}.')
	print(f'The answer to part 2 is: {run(city, min_n=4, max_n=10)}.')