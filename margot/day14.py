import numpy as np
from typing import Tuple
import sys

def tilt(platform, direction:Tuple[int, int]) -> None:
    shifted = True
    while shifted:
        shifted = False
        for (i, j) in zip(*np.where(platform == "O")):
            if all([i+direction[0] >= 0, i+direction[0] < platform.shape[0], j+direction[1] >= 0, j+direction[1] < platform.shape[1]]):
                if platform[i+direction[0], j+direction[1]] == ".":
                    shifted = True
                    platform[i, j], platform[i+direction[0], j+direction[1]] = ".", "O"

def north_load(platform) -> int:
    return np.sum([platform.shape[0]-i for i in np.where(platform == "O")[0]])

def main():
    name = "input"

    platform = np.array([list(line.rstrip()) for line in open("inputs/day14/{}.txt".format(name))])

    history = [platform.copy()]

    tilt(platform, direction = (-1, 0))

    print("Load on north side of platform (task 1):", north_load(platform))

    #(Task 2) Tilt the platform cyclically until a limit cycle is reached, then determine transient and period.
    tilt(platform, direction = (0, -1))
    tilt(platform, direction = (1, 0))
    tilt(platform, direction = (0, 1))

    while not any([np.all(platform == platform_prev) for platform_prev in history]):
        history.append(platform.copy())
        print(len(history))
        tilt(platform, direction = (-1, 0))
        tilt(platform, direction = (0, -1))
        tilt(platform, direction = (1, 0))
        tilt(platform, direction = (0, 1))
    transient = np.where([np.all(platform == platform_prev) for platform_prev in history])[0][0]
    loop = history[transient:]
    period = len(loop)

    #Determine the state of the system after 1 billion cycles.
    platform = loop[int((1e9-transient)%period)]
    print("Load on north side of platform after 1 billion cycles (task 2):", north_load(platform))

if __name__ == "__main__":
    sys.exit(main())