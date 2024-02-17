from typing import List, Dict, Tuple, Set
import sys
import regex as re
from abc import ABC, abstractmethod

#Define Pulse type: False is a low pulse, True is a high pulse. 
Pulse = bool
Label = str

class Module(ABC):
    def __init__(self):
        self.destinations = {}
    
    @abstractmethod
    def send_pulse(self, module_in:Label, pulse:Pulse) -> Pulse:
        pass
        
    @abstractmethod
    def add_input(self, module_in:Label)->None:
        pass

class FlipFlopModule(Module):
    def __init__(self):
        self.destinations = set()
        self.on = False
        
    def add_input(self, module_in:Label)->None:
        pass
        
    def send_pulse(self, module_in:Label, pulse:Pulse) -> Pulse:
        if not pulse:
            self.on = not self.on
            return self.on
    
class ConjunctionModule(Module):
    def __init__(self):
        self.destinations = set()
        self.inputs = {}
        
    def add_input(self, module_in:Label)-> None:
        self.inputs[module_in] = False
        
    def send_pulse(self, module_in:Label, pulse:Pulse) -> Pulse:
        self.inputs[module_in] = pulse
        return not all(self.inputs.values())
        
class BroadcastModule(Module):
    def __init__(self):
        self.destinations = set()
        
    def add_input(self, module_in:Label)->None:
        pass
        
    def send_pulse(self, module_in:Label, pulse:Pulse) -> Pulse:
        return pulse
        
class Circuit():
    def __init__(self):
        self.modules = {}
        self.connections = set()
        self.queue = []
        
    def add_module(self, label:Label, module:Module):
        self.modules[label] = module
        for module_in in (module_in for (module_in, module_out) in self.connections if module_out == label):
            self.modules[label].add_input(module_in)
        
    def add_connection(self, module_in:Label, module_out:Label):
        self.connections.add((module_in, module_out))
        if module_out in self.modules:
            self.modules[module_out].add_input(module_in)
        self.modules[module_in].destinations.add(module_out)
            
    def update(self) -> Pulse:
        module_in, module_out, pulse_in = self.queue.pop(0)
        if module_out in self.modules:
            pulse_out = self.modules[module_out].send_pulse(module_in, pulse_in)
            if pulse_out != None:
                self.queue.extend([(module_out, dest, pulse_out) for dest in self.modules[module_out].destinations])
        return pulse_in
        
    def push_button(self):
        self.queue.insert(0, ("button", "broadcaster", False))
        
def main():
    name = "input"
    
    circuit = Circuit()
    
    line_pattern = re.compile("([%&]?)([a-zA-Z]+)\s->\s((?:[a-zA-Z]+,\s)*[a-zA-Z]+)$")
    for line in open("inputs/day20/{}.txt".format(name)):
        symbol, label, destinations = line_pattern.match(line).groups()
        if symbol == "%":
            circuit.add_module(label, FlipFlopModule())
        elif symbol == "&":
            circuit.add_module(label, ConjunctionModule())
        elif (symbol == "" and label == 'broadcaster'):
            circuit.add_module(label, BroadcastModule())
        else:
            print("Invalid module type or name.")
            return
        
        for module_out in destinations.split(","):
            circuit.add_connection(label, module_out.strip())
            
    low_count = 0
    high_count = 0
    for i in range(1000):
        circuit.push_button()
        while len(circuit.queue)>0:
            pulse = circuit.update()
            if pulse != None:
                low_count += not pulse
                high_count += pulse
        if all([not module.on for module in circuit.modules.values() if type(module) == FlipFlopModule]): break
    
    period = i+1
    low_count *= 1000//period
    high_count *= 1000//period
    
    for i in range(1000%period):
        circuit.push_button()
        while len(circuit.queue)>0:
            pulse = circuit.update()
            if pulse != None:
                low_count += not pulse
                high_count += pulse
                
    print("Product of high and low pulse counts(task 1):", high_count*low_count)

if __name__ == "__main__":
    sys.exit(main())
