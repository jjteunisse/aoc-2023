import numpy as np
import sys

def read_numbers(line):
    header, content = line.split(":")
    numbers = [int(num) for num in content.split()]
    return numbers

def read_combined_number(line):
    header, content = line.split(":")
    number = int("".join(content.split()))
    return number

def find_intersections(duration, distance):
    #unit time = ms
    #unit distance = mm

    #Define coefficients for polynomial equation ax^2 + bx + c = 0
    a = -1 #distance/time^2
    b = duration #distance/time
    c = -distance #distance

    #Find roots analytically (using numpy in this case)
    roots = np.roots([a, b, c])

    #Convert roots (floats) to integers
    intersection_right = np.floor(roots[0])
    intersection_left = np.ceil(roots[1])
    
    return (intersection_left, intersection_right)

def main():
    name = "input"

    with open("inputs/day6/{}.txt".format(name)) as file:
        race_durations_line = next(file)
        race_durations = read_numbers(race_durations_line)
        race_duration_combined = read_combined_number(race_durations_line)

        record_distances_line = next(file)
        record_distances = read_numbers(record_distances_line)
        record_distance_combined = read_combined_number(record_distances_line)

    num_races = len(race_durations)

    intersections = np.zeros((num_races, 2))

    for i, (duration, distance) in enumerate(zip(race_durations, record_distances)):
        intersections[i] = find_intersections(duration, distance)

    widths = intersections[:, 1] - intersections[:, 0] + 1
    print("Product of margins:", np.product(widths))

    intersection_combined = find_intersections(race_duration_combined, record_distance_combined)
    print("Margin for combined numbers:", intersection_combined[1] - intersection_combined[0] + 1)

if __name__ == "__main__":
    sys.exit(main())