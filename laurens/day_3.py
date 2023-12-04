from laurens.util.file_reader import read_from_file
import re

TEST = False


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

            if check_neighbours_for_special_character(neighbours):
                line_score += int(found_number_string)

            found_number_string = ""

    return line_score


def return_numbers_on_indexes(list, string):
    found_number_string = ""
    found_numbers = []

    for index, character in enumerate(string):
        if re.search(r'\d+', character):
            found_number_string += character

        if (found_number_string != "" and index == (len(string) - 1)
                or found_number_string != "" and not re.search(r'\d+', string[index + 1])):
            first_index = index - len(found_number_string) + 1
            last_index = index

            pivot = first_index

            while pivot <= last_index:
                if pivot in list:
                    found_numbers.append(found_number_string)
                    break

                pivot += 1

            found_number_string = ""

    return found_numbers


def get_gear_score(previous_line, current_line, next_line):
    line_score = 0

    for index, character in enumerate(current_line):
        if character == "*":
            to_check_previous = []
            to_check_current = []
            to_check_next = []

            if index > 0:
                to_check_current.append(index - 1)
                if previous_line:
                    to_check_previous.append(index - 1)
                if next_line:
                    to_check_next.append(index - 1)

            to_check_current.append(index)
            if previous_line:
                to_check_previous.append(index)
            if next_line:
                to_check_next.append(index)

            if index < (len(current_line) - 1):
                to_check_current.append(index + 1)
                if previous_line:
                    to_check_previous.append(index + 1)
                if next_line:
                    to_check_next.append(index + 1)

            found_numbers = []

            found_numbers += return_numbers_on_indexes(to_check_current, current_line)

            if previous_line:
                found_numbers += return_numbers_on_indexes(to_check_previous, previous_line)

            if next_line:
                found_numbers += return_numbers_on_indexes(to_check_next, next_line)

            if len(found_numbers) == 2:
                line_score += int(found_numbers[0]) * int(found_numbers[1])

    return line_score


if __name__ == '__main__':
    engine_lines = []
    if TEST:
        engine_lines = read_from_file("./data/day_3_test.txt")
    else:
        engine_lines = read_from_file("./data/day_3.txt")

    schematic_score = 0
    gear_score = 0

    for index, current_line in enumerate(engine_lines):
        previous_line = None
        next_line = None

        if index != 0:
            previous_line = engine_lines[index - 1]

        if index != (len(engine_lines) - 1):
            next_line = engine_lines[index + 1]

        schematic_score += get_engine_line_value(previous_line, current_line, next_line)
        gear_score += get_gear_score(previous_line, current_line, next_line)

    print("Task 1: " + str(schematic_score))
    print("Task 2: " + str(gear_score))
