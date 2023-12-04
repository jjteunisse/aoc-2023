from laurens.util.file_reader import read_from_file
import re

TEST = True

def text_to_num(text: str):
    num_dict = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0
    }
    return num_dict.get(text.lower(), None)

def find_first_number_in_list(list: list):
    for element in list:
        if element.isdigit():
            return int(element)
        elif text_to_num(element) is not None:
            return text_to_num(element)

def values_to_calibration_value_task_1(values: list):
    result = 0

    for value in values:
        match = re.findall(r'\d+', value)
        result += int(match[0][0] + match[-1][-1])

    return result

def values_to_calibration_value_task_2(values: list):
    number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = 0

    for string in values:
        split_string = []
        pivot = 0

        while pivot < len(string):
            if re.search(r'\d+', string[pivot]):
                split_string.append(string[pivot])
                pivot += 1
            else:
                built_string = ""
                index = pivot
                while (any(value.startswith(built_string) for value in number_words)
                       and built_string not in number_words):
                    built_string += string[index]
                    index += 1

                    if index >= len(string):
                        break

                if built_string in number_words:
                    split_string.append(built_string)

                pivot += 1

        first_number = find_first_number_in_list(split_string)
        last_number = find_first_number_in_list(reversed(split_string))

        if first_number is None or last_number is None:
            print(split_string)
            exit()

        result += (int(str(first_number) + str(last_number)))

    return result

if __name__ == '__main__':
    values = []
    if TEST:
        print("Task 1: " + str(values_to_calibration_value_task_1(read_from_file("./data/day_1_test_1.txt"))))
        print("Task 2: " + str(values_to_calibration_value_task_2(read_from_file("./data/day_1_test_2.txt"))))
    else:
        values = read_from_file("./data/day_1.txt")
        print("Task 1: " + str(values_to_calibration_value_task_1(values)))
        print("Task 2: " + str(values_to_calibration_value_task_2(values)))



