import numpy as np
import numpy.typing as npt
from typing import Tuple, List
import pandas as pd
import sys

def calculate_lagoon_volume(directions:List[Tuple[int, int]], steps:List[int])->int:
    vertices = np.cumsum([(number*direction[0], number*direction[1]) for number, direction in zip(steps, directions)], axis=0)

    #Use the Shoelace formula to get area of polygon - basically, divide the shape up into squares and add their areas
    volume = abs(np.sum((np.roll(vertices[:, 0], 1) + vertices[:, 0])/2*(vertices[:, 1]-np.roll(vertices[:, 1], 1))))
    
    #Correct 1/2 for each edge point; the extra +1 accounts for corners, as there are 4 corners which all contribute 1/4.
    #Note the correction is always only for the 4 corners of a square, as further corner contributions cancel each other out. 
    return volume + sum(steps)/2 + 1
    
def main():
    name = "input"

    #Read input data as pandas dataframe
    dframe = pd.read_csv("inputs/day18/{}.txt".format(name), sep=" ", header=None)

    #Task 1
    mapping = {"L":(0, -1), "R":(0, 1), "D":(1, 0), "U":(-1, 0)}

    directions = [mapping[char] for char in dframe[0]]
    steps = [int(number) for number in dframe[1]]

    print("Volume of lagoon (task 1): {} m^3".format(calculate_lagoon_volume(directions, steps)))

    #Task 2
    mapping = {'2':(0, -1), '0':(0, 1), '1':(1, 0), '3':(-1, 0)}

    directions = [mapping[string[-2]] for string in dframe[2]]
    steps = [int(string[2:-2], 16) for string in dframe[2]]

    print("Volume of lagoon (task 2): {} m^3".format(calculate_lagoon_volume(directions, steps)))