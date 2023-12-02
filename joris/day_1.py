import re, sys

def run(data, part):
	if 'test' in data: data += f'_p{part}'

	digits = {
		'one':   1, 'two':   2, 'three': 3,
		'four':  4, 'five':  5, 'six':   6,
		'seven': 7, 'eight': 8, 'nine':  9
	}
	cali_sum = 0
	for line in open('./inputs/' + data + '.txt').readlines():
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

	print(f'Answer to part {part}: {cali_sum}')

if __name__ == '__main__':
	data = 'day_1'
	if len(sys.argv) > 1 and sys.argv[1] == '--test':
		data = 'test_' + data

	run(data, 1)
	run(data, 2)