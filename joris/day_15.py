def hash(code: str) -> str:
	current_value = 0
	for char in code:
		current_value += ord(char)
		current_value *= 17
		current_value %= 256
	return current_value

def part_1(codes: list[str]):
	code_values = []
	for code in codes: code_values.append(hash(code))
	print(f'The answer to part 1 is: {sum(code_values)}.')

def part_2(codes: list[str]):
	boxes = {i: [[], []] for i in range(256)}
	for code in codes:
		if '-' in code:
			label = code[:-1]
			box = boxes[hash(label)]
			if label in box[0]:
				slot = box[0].index(label)
				del box[0][slot]
				del box[1][slot]
		elif '=' in code:
			label, foc_len = code.split('=')
			box = boxes[hash(label)]
			if label in box[0]:
				slot = box[0].index(label)
				box[1][slot] = int(foc_len)
			else:
				box[0].append(label)
				box[1].append(int(foc_len))
		else:
			raise Exception('Invalid code format.')

	foc_power = 0
	for box_id, box in boxes.items():
		for slot, foc_len in enumerate(box[1]):
			foc_power += (box_id + 1) * (slot + 1) * foc_len

	print(f'The answer to part 2 is: {foc_power}.')

if __name__ == '__main__':
	sequence = open('inputs/day_15.txt').read()
	codes = sequence.split(',')
	part_1(codes)
	part_2(codes)