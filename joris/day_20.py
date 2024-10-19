class Pulse: LOW = False; HIGH = True
class State: OFF = False; ON = True

class FlipFlop():
	def __init__(self, name, targets):
		self.name = name
		self.targets = targets
		self.state = State.OFF

	def process(self, src, pulse):
		if pulse == Pulse.LOW:
			self.state = not self.state
			if self.state == State.ON:
				return [(self.name, Pulse.HIGH, t) for t in self.targets]
			else:
				return [(self.name, Pulse.LOW, t) for t in self.targets]
		else:
			return []

class Conjunction():
	def __init__(self, name, targets):
		self.name = name
		self.targets = targets
		self.memory = {}

	def process(self, src, pulse):
		self.memory[src] = pulse
		if all([v == Pulse.HIGH for v in self.memory.values()]):
			return [(self.name, Pulse.LOW, t) for t in self.targets]
		else:
			return [(self.name, Pulse.HIGH, t) for t in self.targets]

class Broadcaster():
	def __init__(self, targets):
		self.targets = targets

	def process(self, src, pulse):
		return [('broadcaster', Pulse.LOW, t) for t in self.targets]

def init_modules(cfg):
	cfg.sort(reverse=True) # Broadcaster -> Conjunction -> FlipFlop
	modules = {}
	for line in cfg:
		src, targets = line.split(' -> ')
		targets = targets.split(', ')
		if src == 'broadcaster':
			modules[src] = Broadcaster(targets)
		else:
			src_type, src_name = src[0], src[1:]
			if src_type == '&':
				modules[src_name] = Conjunction(src_name, targets)
			elif src_type == '%':
				modules[src_name] = FlipFlop(src_name, targets)
				for t in targets:
					if t in modules and isinstance(modules[t], Conjunction):
						modules[t].memory[src_name] = Pulse.LOW
	return modules

def push_button(modules, n_pulses):
	to_send = [('button', Pulse.LOW, 'broadcaster')]
	while to_send:
		signal = to_send.pop(0)
		src, pulse, target = signal
		# print(signal)
		if target in modules:
			to_send += modules[target].process(src, pulse)
		n_pulses[pulse] += 1
	return n_pulses

def run():
	cfg = open('inputs/day_20.txt').read().split('\n')
	modules = init_modules(cfg)

	n_pulses = {Pulse.LOW: 0, Pulse.HIGH: 0}
	for i in range(1000):
		# print('\nIteration', i)
		push_button(modules, n_pulses)

	answer = n_pulses[Pulse.LOW] * n_pulses[Pulse.HIGH]
	print(f'The answer to part 1 is: {answer}.')

if __name__ == '__main__':
	run()