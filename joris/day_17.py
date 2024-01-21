from typing import NamedTuple

class State(NamedTuple):
	y: int
	x: int
	d: tuple[int]
	n: int

def get_turns(d: tuple[int]) -> list[tuple[int]]:
	return [(-1, 0), (1, 0)] if d[0] == 0 else [(0, -1), (0, 1)]

def run(city: list[str], *, min_n, max_n):
	dims = (len(city), len(city[0]))
	goal = (dims[0] - 1, dims[1] - 1)
	states = {State(0, 0, (0, 0), 0)}
	losses = {list(states)[0]: 0}
	while states:
		print(len(states), end='\r')
		new_states = set()
		for s in states:
			directions = (
				([s.d] if s.n < max_n else []) +
				(get_turns(s.d) if s.n >= min_n else [])
			)
			if s.d == (0, 0): directions = [(0, 1), (1, 0)]
			for d_new in directions:
				if s.n != 0 and d_new == s.d:
					y_new = s.y + d_new[0]
					x_new = s.x + d_new[1]
					if 0 <= y_new < dims[0] and 0 <= x_new < dims[1]:
						n_new = s.n + 1
						l_new = losses[s] + int(city[y_new][x_new])
						s_new = State(y_new, x_new, d_new, n_new)
						if s_new not in losses or l_new < losses[s_new]:
							losses[s_new] = l_new
							new_states.add(s_new)
				else:
					y_new = s.y + (d_new[0] * min_n)
					x_new = s.x + (d_new[1] * min_n)
					if 0 <= y_new < dims[0] and 0 <= x_new < dims[1]:
						n_new = min_n
						l_new = losses[s]
						for i in range(min_n):
							l_new += int(city[y_new - (d_new[0] * i)][x_new - (d_new[1] * i)])
						s_new = State(y_new, x_new, d_new, n_new)
						if s_new not in losses or l_new < losses[s_new]:
							losses[s_new] = l_new
							new_states.add(s_new)
		states = new_states
	goal_losses = [v for k, v in losses.items() if (k.y, k.x) == goal]
	return min(goal_losses)

if __name__ == '__main__':
	city = open('inputs/day_17.txt').read().split('\n')
	print(f'The answer to part 1 is: {run(city, min_n=1, max_n=3)}.')
	print(f'The answer to part 2 is: {run(city, min_n=4, max_n=10)}.')