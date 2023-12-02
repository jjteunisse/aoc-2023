import numpy as np

name = "input"

count = 0
with open("inputs/day1/{}.txt".format(name)) as file:
    for line in file:
        digit_strings = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
        lowest_index = len(line)
        highest_index = 0
        for key in digit_strings:
            try:
                index = line.index(key)
                if index <= lowest_index:
                    lowest_index = index
                    first_digit = digit_strings[key]
                index = line.rindex(key)
                if index >= highest_index:
                    highest_index = index
                    last_digit = digit_strings[key]
            except ValueError:
                pass
        
        for digit in np.arange(10).astype(str):
            try:
                index = line.index(digit)
                if index <= lowest_index:
                    lowest_index = index
                    first_digit = digit
                index = line.rindex(digit)
                if index >= highest_index:
                    highest_index = index
                    last_digit = digit
            except ValueError:
                pass

        print(line)
        print(first_digit, last_digit)
        count += int(first_digit + last_digit)

print(count)