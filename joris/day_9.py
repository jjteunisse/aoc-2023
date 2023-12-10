if __name__ == '__main__':
	report = open('inputs/day_9.txt').readlines()

	ext_left, ext_right = [], []
	for line in report:
		history = [int(x) for x in line.split(' ')]

		left, right = [], []
		while sum(history) != 0:
			left.append(history[0]); right.append(history[-1])

			deltas = []
			for i in range(len(history) - 1):
				deltas.append(history[i + 1] - history[i])
			history = deltas

		val = 0
		for num in reversed(left): val = num - val
		ext_left.append(val)
		ext_right.append(sum(right))

	print(f'The answer to part 1 is: {sum(ext_right)}.')
	print(f'The answer to part 2 is: {sum(ext_left)}.')