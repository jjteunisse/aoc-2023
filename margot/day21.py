import sys
import numpy as np

def main():
    path = "inputs/day21/"
    name = "input"
    
    data = np.array([list(line.strip()) for line in open(path+name+".txt")])
    print(data.shape)
    
    positions = (data == "S")
    mask = (data != "#")
    
    kernel = np.array([True, False, True])
    
    #Task 1
    num_steps = 64
    for _ in range(num_steps):
        positions = mask*np.logical_or(np.array([np.convolve(row, kernel, 'same') for row in positions]),
                                       np.array([np.convolve(col, kernel, 'same') for col in positions.T]).T)
    
    print("Number of accessible positions after {} steps: {}".format(num_steps, np.sum(positions)))
    
if __name__ == "__main__":
    sys.exit(main())