# Note: This program is tailored to the specific input of the challenge.
# It will not compute the right answer for all possible inputs in this format.

import math, re

if __name__ == '__main__':
	document = open('inputs/day_8.txt').read().splitlines()
	directions = document[0]

	nodes = {}
	for line in document[2:]:
		match = re.match(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line)
		nodes[match[1]] = {'L': match[2], 'R': match[3]}

	start_nodes = [node for node in nodes.keys() if node[2] == 'A']
	steps_to_finish = {}
	for i, node in enumerate(start_nodes):
		n_steps = 0
		while node[2] != 'Z':
			node = nodes[node][directions[n_steps % len(directions)]]
			n_steps += 1
		steps_to_finish[start_nodes[i]] = n_steps

	print(f'The answer to part 1 is: {steps_to_finish["AAA"]}.')
	print(f'The answer to part 2 is: {math.lcm(*steps_to_finish.values())}.')