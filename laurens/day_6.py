import math
import time

from laurens.util.file_reader import read_from_file

TEST = False


def find_x_values(y, a, y_vertex, game_index):
    h, k = y_vertex

    square_root_part = ((y - k) / a) ** 0.5

    if square_root_part < 0:
        print("Game with index: " + str(game_index) + " is not winnable.")
        exit()

    if square_root_part == 0:
        return [h + square_root_part]

    return [h - square_root_part, h + square_root_part]


def run(times: list, records: list):
    score = 0

    for index, time in enumerate(times):
        x_vertex = time / 2
        y_vertex = x_vertex * x_vertex
        x_values_for_y = (find_x_values(records[index], -1, [x_vertex, y_vertex], index))
        if len(x_values_for_y) == 1:
            possible_games = 1
        else:
            possible_games = math.ceil(x_values_for_y[1]) - math.floor(x_values_for_y[0]) - 1

        if score == 0:
            score = possible_games
        else:
            score = score * possible_games

    return score


if __name__ == '__main__':
    start_time = time.time()
    values = []
    if TEST:
        values = read_from_file("./data/day_6_test.txt")
    else:
        values = read_from_file("./data/day_6_txt")

    times = [int(item) for item in values[0].split(":")[1].strip().split(" ") if item]
    records = [int(item) for item in values[1].split(":")[1].strip().split(" ") if item]
    print("Task 1: " + str(run(times, records)))
    times = [int("".join([str(item) for item in values[0].split(":")[1].strip().split(" ") if item]))]
    records = [int("".join([str(item) for item in values[1].split(":")[1].strip().split(" ") if item]))]
    print("Task 2: " + str(run(times, records)))

    print("In seconds this took: ")
    print(time.time() - start_time)