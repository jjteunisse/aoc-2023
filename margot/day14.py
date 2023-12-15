import numpy as np
from typing import Tuple
import sys

def tilt(platform, direction:Tuple[int, int]):
    shifted = True
    while shifted:
        shifted = False
        for (i, j) in zip(*np.where(platform == "O")):
            if all([i+direction[0] >= 0, i+direction[0] < platform.shape[0], j+direction[1] >= 0, j+direction[1] < platform.shape[1]]):
                if platform[i+direction[0], j+direction[1]] == ".":
                    shifted = True
                    platform[i, j], platform[i+direction[0], j+direction[1]] = ".", "O"

def main():
    name = "input"

    platform = np.array([list(line.rstrip()) for line in open("inputs/day14/{}.txt".format(name))])

    tilt(platform, direction = (-1, 0))

    north_load = np.sum([platform.shape[0]-i for i in np.where(platform == "O")[0]])
    print("Load on north side of platform (task 1):", north_load)

if __name__ == "__main__":
    sys.exit(main())