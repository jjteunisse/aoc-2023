Matrix = list[list[str]]

def find(matrix: Matrix) -> int:
	for i in range(len(matrix) // 2, 0, -1):
		mirror = mirrored(matrix, i)
		if mirror == matrix[:i * 2]: return i

def mirrored(matrix: Matrix, line: int) -> Matrix:
	return matrix[:line] + list(reversed(matrix[:line]))

def pprint(matrix: Matrix):
	for line in matrix: print(line)

def transposed(matrix: Matrix) -> Matrix:
	return [''.join(x) for x in zip(*matrix)]

def rev(matrix: Matrix) -> Matrix:
	return list(reversed(matrix))

patterns = [
	x.split('\n')
	for x in open('inputs/day_13.txt').read().split('\n\n')
]

summary = 0
for pattern in patterns:
	h_start = find(pattern)
	if h_start:
		summary += 100 * h_start
		continue

	h_end = find(rev(pattern))
	if h_end:
		v_len = len(pattern)
		summary += 100 * (v_len - h_end)
		continue

	v_start = find(transposed(pattern))
	if v_start:
		summary += v_start
		continue

	v_end = find(rev(transposed(pattern)))
	if v_end:
		h_len = len(pattern[0])
		summary += h_len - v_end
		continue

	raise Exception('No match found.')

print(f'The answer to part 1 is: {summary}.')