import os
import re


def retrieve_document():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(here + '\..\document.txt') as file:
        return file.read().splitlines()


def string_to_calibration_value(string: str):
    match = re.findall(r'\d+', string)

    return match[0][0] + match[-1][-1]


if __name__ == '__main__':
    values = retrieve_document()
    result = 0
    for value in values:
        result += int(string_to_calibration_value(value))

    print(result)


