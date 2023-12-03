import os
import re


def retrieve_engine_lines():
    engine_lines = []
    for line in open("./data/day_3.txt").readlines():
        engine_lines.append(line.strip())

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

        if (found_number_string != "" and index == (len(current_line) - 1)
                or found_number_string != "" and not re.search(r'\d+', current_line[index + 1])):
            first_index = index - len(found_number_string) + 1
            last_index = index

            pivot = first_index
            neighbours = []

            while pivot <= last_index:

                if pivot == first_index and pivot > 0:
                    neighbours.append(current_line[pivot - 1])
                    if previous_line:
                        neighbours.append(previous_line[pivot - 1])
                        neighbours.append(previous_line[pivot])
                    if next_line:
                        neighbours.append(next_line[pivot - 1])
                        neighbours.append(next_line[pivot])

                if pivot == last_index and pivot < (len(current_line) - 1):
                    neighbours.append(current_line[pivot + 1])
                    if previous_line:
                        neighbours.append(previous_line[pivot + 1])
                        neighbours.append(previous_line[pivot])
                    if next_line:
                        neighbours.append(next_line[pivot + 1])
                        neighbours.append(next_line[pivot])
                else:
                    if previous_line:
                        neighbours.append(previous_line[pivot])
                    if next_line:
                        neighbours.append(next_line[pivot])

                pivot += 1

            if found_number_string == "8":
                print(neighbours)
                print(first_index)
                print(last_index)

            if check_neighbours_for_special_character(neighbours):
                if found_number_string == "8":
                    print("true")
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

    print(score)
