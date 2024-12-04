from typing import List, Dict, Tuple, Set
import sys
import regex as re
from abc import ABC, abstractmethod
import networkx as nx
from matplotlib import pyplot as plt

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
        return (module_in, pulse_in)
        
    def push_button(self):
        self.queue.insert(0, ("button", "broadcaster", False))
        
def main():
    name = "input"
    
    #Construct circuit
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
        
    #(Task 1) Count number of low and high pulses sent after 1000 button presses
    low_count = 0
    high_count = 0
    for i in range(1):
        circuit.push_button()
        while len(circuit.queue)>0:
            pulse = circuit.update()[1]
            if pulse != None:
                low_count += not pulse
                high_count += pulse
    
    print("Product of high and low pulse counts(task 1):", high_count*low_count)
    
    #(Task 2) Reaching rx will be difficult without knowing where it is and how the flip-flop/conjunction modules interact.
    #Instead of trying to solve this generically, try to see what the circuit looks like first.
    circuit_graph = nx.DiGraph()
    circuit_graph.add_edges_from(circuit.connections)
    
    colour_map = ['green' if label == 'rx' else 'red' if type(circuit.modules[label]) == FlipFlopModule else 'blue' if type(circuit.modules[label]) == ConjunctionModule 
                  else 'gray' for label in circuit_graph.nodes]
    nx.draw_networkx(circuit_graph, node_color = colour_map, with_labels=True)
    plt.axis('off')
    plt.show()
    
    #The broadcaster leads to four subcircuits, all of which have a conjunction module that need to give a 'low' pulse. 
    #We can reformulate the problem to state that the conjunction module in each module must give a low pulse. 
    num_iterations = 1
    for label_init in circuit.modules['broadcaster'].destinations:
        subcircuit = Circuit()
        queue = circuit.modules[label_init].destinations
        nodes = nx.descendants(circuit_graph, label_init)
        nodes.add(label_init)
        subgraph = circuit_graph.subgraph(nodes)
        subcircuit.add_module('broadcaster', BroadcastModule())
        for label in subgraph:
            if not label == "rx":
                subcircuit.add_module(label, type(circuit.modules[label])())
        subcircuit.add_connection('broadcaster', label_init)
        for edge in subgraph.edges:
            subcircuit.add_connection(*edge)
        
        visited_states = []
        flipflops = {label for label in subcircuit.modules if type(subcircuit.modules[label]) == FlipFlopModule}
        conjunction_label = {label for label in subcircuit.modules if type(subcircuit.modules[label]) == ConjunctionModule if len(subcircuit.modules[label].inputs)>1}.pop()
        
        i = 0
        while True:
            state = {label:subcircuit.modules[label].on for label in flipflops}
            if state in visited_states:
                break
            else:
                visited_states.append(state)
            subcircuit.push_button()
            while len(subcircuit.queue)>0:
                label, pulse = subcircuit.update()
            i += 1
        period = i-visited_states.index(state)
        #The subcircuit loops back to the start - there is no transient. 
        #It seems like the subcircuit immediately loops back after sending a high pulse; this should be verifiable from the circuit structure.
        #The numbers also all happen to be primes, so we can simply multiply them. 
        num_iterations *= period
    print("Number of iterations required to reach rx:", num_iterations)
    return

if __name__ == "__main__":
    sys.exit(main())
