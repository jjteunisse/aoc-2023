from typing import NamedTuple

class State(NamedTuple):
	y: int
	x: int
	d: tuple[int]
	n: int

def get_turns(d: tuple[int]) -> list[tuple[int]]:
	return [(-1, 0), (1, 0)] if d[0] == 0 else [(0, -1), (0, 1)]

def run(city: list[str], *, max_n):
	dims = (len(city), len(city[0]))
	goal = (dims[0] - 1, dims[1] - 1)
	states = {State(0, 0, (0, 1), 0)}
	losses = {list(states)[0]: 0}
	while states:
		new_states = set()
		for s in states:
			directions = ([s.d] if s.n < max_n else []) + get_turns(s.d)
			for d_new in directions:
				y_new = s.y + d_new[0]
				x_new = s.x + d_new[1]
				if 0 <= y_new < dims[0] and 0 <= x_new < dims[1]:
					n_new = 1 if d_new != s.d else s.n + 1
					l_new = losses[s] + int(city[y_new][x_new])
					s_new = State(y_new, x_new, d_new, n_new)
					if s_new not in losses or l_new < losses[s_new]:
						losses[s_new] = l_new
						new_states.add(s_new)
		states = new_states
	goal_losses = [v for k, v in losses.items() if (k.y, k.x) == goal]
	return min(goal_losses)

if __name__ == '__main__':
	city = open('inputs/day_17.txt').read().split('\n')
	print(f'The answer to part 1 is: {run(city, max_n=3)}.')