from math import prod
import re

def part_1(parsed_flows: list[str], parts: list[str]):
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

def part_2(parsed_flows: list[str]):
	branches = [('in', {cat: [1, 4000] for cat in ['x', 'm', 'a', 's']})]
	accepted = []
	while len(branches) > 0:
		flow_name, ratings_stay = branches.pop(0)
		for rule in parsed_flows[flow_name]:
			ratings_switch = {k: v.copy() for k, v in ratings_stay.items()}
			if rule['cond'] != 'True':
				match = re.match(r'([xmas])([><])(\d+)', rule['cond'])
				cat, op, val = match.groups()
				val = int(val)

				if op == '>':
					ratings_switch[cat][0] = val + 1
					ratings_stay[cat][1] = val
				elif op == '<':
					ratings_switch[cat][1] = val - 1
					ratings_stay[cat][0] = val

			if rule['dest'] == 'A':
				accepted.append(ratings_switch)
			elif rule['dest'] != 'R':
				branches.append((rule['dest'], ratings_switch))

	n_combs = 0
	for ratings in accepted:
		n_combs += prod([v[1] - v[0] + 1 for v in ratings.values()])
	print(f'The answer to part 2 is: {n_combs}.')

if __name__ == '__main__':
	data = open('inputs/day_19.txt').read().split('\n')
	split = data.index('')
	flows, parts = data[:split], data[split + 1:]

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

	part_1(parsed_flows, parts)
	part_2(parsed_flows)