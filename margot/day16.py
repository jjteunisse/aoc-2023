import numpy as np
from typing import Tuple
import sys

class LightContraption():
    def __init__(self, grid):
        self.grid = grid
        self.energized = np.zeros_like(grid, dtype=bool)
        self.beams = set()
        self.stale = set()
        self.direction_mapping = {}
        self.direction_mapping["."] = {}
        self.direction_mapping["\\"] = {(0, 1):((1, 0),), (1, 0):((0, 1),), (0, -1):((-1, 0),), (-1, 0):((0, -1),)}
        self.direction_mapping["/"] = {(0, 1):((-1, 0),), (-1, 0):((0, 1),), (0, -1):((1, 0),), (1, 0):((0, -1),)}
        self.direction_mapping["-"] = {(1, 0):((0, 1), (0, -1)), (-1, 0):((0, 1), (0, -1))}
        self.direction_mapping["|"] = {(0, 1):((1, 0), (-1, 0)), (0, -1):((1, 0), (-1, 0))}

    def update(self):
        self.stale.update(self.beams)
        beams_new = set()
        for (loc, direction) in self.beams:
            if not any([loc[0] + direction[0] < 0, loc[0] + direction[0] >= self.grid.shape[0], 
                    loc[1] + direction[1] < 0, loc[1] + direction[1] >= self.grid.shape[1]]):
                loc_new = (loc[0]+direction[0], loc[1]+direction[1])
                self.energized[loc_new[0], loc_new[1]] = True
                char = self.grid[loc_new[0], loc_new[1]]
                if direction in self.direction_mapping[char]:
                    for direction_new in self.direction_mapping[char][direction]:
                        beams_new.add((loc_new, direction_new))
                else:
                    beams_new.add((loc_new, direction))
        self.beams = beams_new - self.stale
            
    
def main():
    name = "input"

    grid = np.array([list(line.rstrip()) for line in open("inputs/day16/{}.txt".format(name))])
    
    #Task 1
    contrpt = LightContraption(grid)
    contrpt.beams.add(((0, -1), (0, 1)))
    
    while any(contrpt.beams):
        contrpt.update()
    
    print("Number of energized tiles (task 1):", np.sum(contrpt.energized))

if __name__ == "__main__":
    sys.exit(main())