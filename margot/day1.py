import numpy as np

def __main__():
    name = "input"

    count_without_strings = 0
    count_with_strings = 0
    with open("inputs/day1/{}.txt".format(name)) as file:
        for line in file:
            lowest_index = len(line)
            highest_index = 0

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
                
            count_without_strings += int(first_digit + last_digit)
                
            digit_strings = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
                
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

            count_with_strings += int(first_digit + last_digit)

    print("Count without strings:", count_without_strings)
    print("Count with strings:", count_with_strings)
    
if __name__ == "__main__":
    sys.exit(main())