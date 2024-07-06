import re

def part_1(flows: list[str], parts: list[str]):
	parsed_flows = {}
	for flow in flows:
		name = flow.split('{')[0]
		rules = re.search(r'\{(.*)\}', flow)[1].split(',')

		parsed_flows[name] = []
		for rule in rules:
			if ':' in rule:
				parsed_flows[name].append({
					'cond': rule.split(':')[0],
					'dest': rule.split(':')[1]
				})
			else:
				parsed_flows[name].append({'cond': 'True', 'dest': rule})

	total_rating = 0
	for part in parts:
		x, m, a, s = [int(d) for d in re.findall(r'\d+', part)]

		flow_name = 'in'
		while flow_name not in ['R', 'A']:
			flow = parsed_flows[flow_name]
			for rule in flow:
				if eval(rule['cond']):
					flow_name = rule['dest']
					break

		if flow_name == 'A':
			total_rating += sum([x, m, a, s])

	print(f'The answer to part 1 is: {total_rating}.')

if __name__ == '__main__':
	data = open('inputs/day_19.txt').read().split('\n')
	split = data.index('')
	flows, parts = data[:split], data[split + 1:]

	part_1(flows, parts)