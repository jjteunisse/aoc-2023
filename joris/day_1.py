import re, sys

def run(path, part):
	if 'test' in path:
		path = path.split('.txt')[0] + '_p' + str(part) + '.txt'
	digits = {
		'one':   1, 'two':   2, 'three': 3,
		'four':  4, 'five':  5, 'six':   6,
		'seven': 7, 'eight': 8, 'nine':  9
	}
	cali_sum = 0
	for line in open(path).readlines():
		first, last = '', ''
		for i, c in enumerate(line):
			if c >= '1' and c <= '9':
				if first == '': first = c
				last = c
				continue
			if part == 2:
				for k, v in digits.items():
					if c == k[0] and line[i : i + len(k)] == k:
						if first == '': first = v
						last = v
		cali_sum += int(f'{first}{last}')
	print(f'The answer to part {part} is: {cali_sum}')

if __name__ == '__main__':
	path = './inputs/day_1.txt'
	if len(sys.argv) > 1 and sys.argv[1] == 'test':
		path = './inputs/test_day_1.txt'
	run(path, 1)
	run(path, 2)