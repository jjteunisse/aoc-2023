# advent of code 2023 day 2
# by: hielke
from pathlib import Path
import re

path = Path(__file__).parent / "input.txt"
str_dump = []
test_str_dump = ['467..114..',
                '...*......',
                '..35..633.',
                '......#...',
                '617*......',
                '.....+.58.',
                '..592.....',
                '......755.',
                '...$.*....',
                '.664.598..']

for str_in in open(path, "rt"):
    try:
        str_dump.append(str_in[:-1])
    except ValueError:
        print("an issue occured, go fix")

height = len(str_dump)
width = len(str_dump[0])

# part 1
# find numbers near special characters and add all together
# find number, check if it's a part number
'''
sum = 0
for i in range(len(str_dump)):
    for matched in re.finditer(r'\d+', str_dump[i]):
        print(matched)
        str_to_check = ''
        start, end = matched.span()
        if start > 0: start -= 1
        if end < width: end += 1
        for dy in range(-1, 2):
            if(i+dy >= 0 and i + dy < len(str_dump)):
                str_to_check += str_dump[i+dy][start:end]
        print(str_to_check)
        if(re.search(r'[^.\d]', str_to_check)):
            num = int(matched.group(0))
            print(num)
            sum += num
print(f'sum: {sum}')
'''
# part 2
# find any *, check if it has 2 values ajacent and multiply them with each other

sum = 0
temp_num = 0
temp_starloc_x, temp_starloc_y = 0, 0
for i in range(len(str_dump)):
    for matched in re.finditer(r'\d+', str_dump[i]):
        # print(matched)
        str_to_check = ''
        
        start, end = matched.span()
        if start > 0: start -= 1
        if end < width: end += 1
        for dy in range(-1, 2):
            if(i+dy >= 0 and i + dy < len(str_dump)):
                str_to_check += str_dump[i+dy][start:end]
        starmatch = re.search(r'[*]', str_to_check)
        if(starmatch):
            # print(starmatch, str_to_check)
            x = 0
            y = 0
            if i == 0 or i == len(str_dump):
                y = 2
            else:
                y = 3
            x = start + starmatch.start() % (len(str_to_check)//y)
            if(i > 0): 
                y = i - 1 + starmatch.start() // (len(str_to_check)//y)
            else:
                y = i + starmatch.start() // (len(str_to_check)//y)
            
            num = int(matched.group(0))
            if temp_starloc_x == 0 and temp_starloc_y == 0:
                temp_starloc_x, temp_starloc_y = x, y
                temp_num = num
                # print(temp_num, (temp_starloc_x, temp_starloc_y))
            else:
                if temp_starloc_x == x and temp_starloc_y == y:
                    gearfactor = num * temp_num
                    print(gearfactor)
                    sum += gearfactor
                    temp_starloc_x, temp_starloc_y = 0, 0
                    tep_num = 0
                else:
                    temp_starloc_x, temp_starloc_y = x, y
                    temp_num = num
                    
            # print(f'starloc: {(x, y)}, temp: {(temp_starloc_x, temp_starloc_y)}')
print(sum)