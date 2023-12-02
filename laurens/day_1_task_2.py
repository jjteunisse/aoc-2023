import os
import re


def retrieve_document():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(here + '\data\day1.txt') as file:
        return file.read().splitlines()


def starts_with_any(string, list):
    return any(value.startswith(string) for value in list)


def text_to_num(text):
    num_dict = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0
    }
    return num_dict.get(text.lower(), None)


def find_first_number_in_list(list):
    for element in list:
        if element.isdigit():
            return int(element)
        elif text_to_num(element) is not None:
            return text_to_num(element)


def string_to_calibration_value(string):
    number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    split_string = []
    pivot = 0

    while pivot < len(string):
        if re.search(r'\d+', string[pivot]):
            split_string.append(string[pivot])
            pivot += 1
        else:
            built_string = ""
            index = pivot
            while starts_with_any(built_string, number_words) and built_string not in number_words:
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

    return int(str(first_number) + str(last_number))

if __name__ == '__main__':
    values = retrieve_document()
    result = 0
    for value in values:
        result += string_to_calibration_value(value)

    print(result)
