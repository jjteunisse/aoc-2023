import os
import re


def retrieve_engine_lines():
    engine_lines = []
    # here = os.path.dirname(os.path.abspath(__file__))
    # for line in open(here + '\data\day_3_test.txt'):
    #     engine_lines.append(line)
    #
    # return engine_lines
    for line in open("./data/day_3_test.txt").readlines():
        engine_lines.append(line)

    return engine_lines


def check_neighbours_for_special_character(list):
    for element in list:
        if re.search(r'[\d.]+', element):
            continue
        else:
            return True

    return False


def get_engine_line_value(previous_line, current_line, next_line):
    line_score = 0
    found_number_string = ""

    for index, character in enumerate(current_line):
        if re.search(r'\d+', character):
            found_number_string += character
        else:
            if found_number_string != "":
                first_index = index - len(found_number_string)
                last_index = index - 1

                pivot = first_index
                neighbours = []

                while pivot <= last_index:

                    if pivot == first_index and pivot > 0:
                        neighbours.append(current_line[index - 1])
                        if previous_line:
                            neighbours.append(previous_line[index - 1])
                            neighbours.append(previous_line[index])
                        if next_line:
                            neighbours.append(next_line[index - 1])
                            neighbours.append(next_line[index])
                    elif pivot == last_index and pivot < (len(current_line) - 1):
                        neighbours.append(current_line[index + 1])
                        if previous_line:
                            neighbours.append(previous_line[index + 1])
                            neighbours.append(previous_line[index])
                        if next_line:
                            neighbours.append(next_line[index + 1])
                            neighbours.append(next_line[index])
                    else:
                        if previous_line:
                            neighbours.append(previous_line[index])
                        if next_line:
                            neighbours.append(next_line[index])

                    pivot += 1

                if check_neighbours_for_special_character(neighbours):
                    line_score += int(found_number_string)

                found_number_string = ""

    return line_score


if __name__ == '__main__':
    engine_lines = retrieve_engine_lines()
    score = 0

    for index, current_line in enumerate(engine_lines):
        previous_line = None
        next_line = None

        if index != 0:
            previous_line = engine_lines[index - 1]

        if index != (len(engine_lines) - 1):
            next_line = engine_lines[index + 1]

        score += get_engine_line_value(previous_line, current_line, next_line)

        print(previous_line)
        print(current_line)
        print(next_line)

    print(score)
