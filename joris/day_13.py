Matrix = list[list[str]]

def mirrored(matrix: Matrix, line: int) -> Matrix:
	return matrix[:line] + list(reversed(matrix[:line]))

def transposed(matrix: Matrix) -> Matrix:
	return [''.join(x) for x in zip(*matrix)]

def find(matrix: Matrix, n_diffs: int) -> int:
	for i in range(len(matrix) // 2, 0, -1):
		original = ''.join(matrix[:i * 2])
		mirror = ''.join(mirrored(matrix, i))
		if sum([int(x != y) for x, y in zip(original, mirror)]) == n_diffs:
			return i

def get_value(matrix: Matrix, n_diffs: int) -> int:
	h_len = len(matrix[0])
	v_len = len(matrix)

	h_start = find(matrix, n_diffs)
	if h_start: return 100 * h_start

	h_end = find(list(reversed(matrix)), n_diffs)
	if h_end: return 100 * (v_len - h_end)

	v_start = find(transposed(matrix), n_diffs)
	if v_start: return v_start

	v_end = find(list(reversed(transposed(matrix))), n_diffs)
	if v_end: return h_len - v_end

	raise Exception(f'No mirror image found with {n_diffs} differences.')

def run(patterns: Matrix, *, n_diffs: int) -> int:
	return sum([get_value(pattern, n_diffs) for pattern in patterns])

if __name__ == '__main__':
	patterns = [
		x.split('\n') for x in open('inputs/day_13.txt').read().split('\n\n')
	]
	print(f'The answer to part 1 is: {run(patterns, n_diffs=0)}.')
	print(f'The answer to part 2 is: {run(patterns, n_diffs=1)}.')