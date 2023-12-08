import re

def run(times, distances):
	ways = 1
	for i, time in enumerate(times):
		for j in range(1, time):
			if (time - j) * j > distances[i]:
				ways *= (time + 1) - (j * 2)
				break
	return ways

if __name__ == '__main__':
	document = open('inputs/day_6.txt').readlines()

	times = [int(x) for x in re.findall(r'\d+', document[0])]
	distances = [int(x) for x in re.findall(r'\d+', document[1])]
	print(f'The answer to part 1 is: {run(times, distances)}.')

	times = [int(''.join(re.findall(r'\d+', document[0])))]
	distances = [int(''.join(re.findall(r'\d+', document[1])))]
	print(f'The answer to part 2 is: {run(times, distances)}.')