# advent of code 2023
# by: hielke
from pathlib import Path
import re

path = Path(__file__).parent / "input.txt"
str_dump = []
test_str_dump = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']

for str_in in open(path, "rt"):
    try:
        str_dump.append(str_in[:-1])
    except ValueError:
        print("an issue occured, go fix")

# part 1
# a calibration value is the first and last digit in a sting
'''
sum = 0

for str_item in test_str_dump:
    pattern = r'\D'
    digit = re.sub(pattern, '', str_item)
    cal_val = digit[0] + digit[-1]
    sum += int(cal_val) # kek lazy pogramming

print(sum)
'''
# part 2
# some values are spelled out
sum = 0

for str_item in str_dump:
    numdict = {'one':'1', 'two': '2', 'three': '3', 'four': '4','five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    pattern = r'(one|two|three|four|five|six|seven|eight|nine|\d)'
    rightpattern = r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)'
    instances = re.findall(pattern,str_item)
    rinstances = re.findall(rightpattern, str_item[::-1])
    first = instances[0]
    last = rinstances[0]
    cal_val = ''
    if first in numdict.keys():
        cal_val += numdict[first]
    else:
        cal_val += first
    if last[::-1] in numdict.keys():
        cal_val += numdict[last[::-1]]
    else:
        cal_val += last
    print(cal_val)
    sum += int(cal_val) # kek lazy pogramming

print(sum)