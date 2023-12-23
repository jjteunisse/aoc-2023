record = open('inputs/day_12.txt').read().split('\n')

arrangements = 0
for line_nr, line in enumerate(record):
	print(line_nr, end='\r')
	string = line.split(' ')[0]
	groups = [int(x) for x in line.split(' ')[1].split(',')]

	unknown_indices = [i for i, x in enumerate(string) if x == '?']
	n_unknowns = len(unknown_indices)
	n_configs = 2 ** n_unknowns
	configs = [
		f'{i:b}'
		.zfill(n_unknowns)
		.replace('0', '.')
		.replace('1', '#')
		for i in range(n_configs)
	]

	for config in configs:
		arrangement_list = list(string)
		for i, j in enumerate(unknown_indices):
			arrangement_list[j] = config[i]
		arrangement_groups = [
			len(x)
			for x in ''.join(arrangement_list).split('.')
			if x
		]
		if arrangement_groups == groups: arrangements += 1

print(f'The answer to part 1 is: {arrangements}.')