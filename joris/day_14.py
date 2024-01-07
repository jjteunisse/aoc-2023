Matrix = list[str]

class Platform:
	def __init__(self, infile: str):
		self.mat = open(infile).read().split('\n')

	def _reverse(self):
		self.mat = list(reversed(self.mat))

	def _roll(self, *, transpose: bool, reverse: bool):
		if transpose: self._transpose()
		for i, row in enumerate(self.mat):
			self.mat[i] = '#'.join(
				[
					''.join(sorted(x, reverse=reverse))
					for x in row.split('#')
				]
			)
		if transpose: self._transpose()

	def _transpose(self):
		self.mat = [''.join(row) for row in zip(*self.mat)]

	def calc_load(self) -> int:
		load = 0
		for i, row in enumerate(self.mat):
			load += row.count('O') * (len(self.mat) - i)
		return load

	def cycle(self):
		self._roll(transpose = True, reverse = True)
		self._roll(transpose = False, reverse = True)
		self._roll(transpose = True, reverse = False)
		self._roll(transpose = False, reverse = False)

	def override(self, mat: Matrix):
		self.mat = mat

	def tilt_north(self):
		self._roll(transpose = True, reverse = True)

if __name__ == '__main__':
	P = Platform('inputs/day_14.txt')
	P.tilt_north()
	print(f'The answer to part 1 is: {P.calc_load()}.')

	configs = []
	n_cycles = int(1E9)
	cycle_start = 0
	for i in range(n_cycles):
		P.cycle()
		if P.mat not in configs:
			configs.append(P.mat)
		else:
			cycle_start = configs.index(P.mat)
			configs = configs[cycle_start:]
			break

	P.override(configs[(n_cycles - cycle_start - 1) % len(configs)])
	print(f'The answer to part 2 is: {P.calc_load()}.')