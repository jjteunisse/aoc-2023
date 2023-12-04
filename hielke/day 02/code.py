# advent of code 2023 day 2
# by: hielke
from pathlib import Path
import re

path = Path(__file__).parent / "input.txt"
str_dump = []
test_str_dump = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

for str_in in open(path, "rt"):
    try:
        str_dump.append(str_in[:-1])
    except ValueError:
        print("an issue occured, go fix")

# part 1
# find games that are possible with 12 red, 13 green and 14 blue
id_sum = 0
for game_str in str_dump:
    id_str, plays_str = game_str.split(': ')
    id = int(id_str[5:]) # game xxx
    plays = plays_str.split('; ')

    possible = True
    for play in plays:
        colours = {'red': 0, 'green': 0, 'blue': 0}
        colours_str = play.split(', ')
        for colour in colours_str:
            colours[colour.split(' ')[1]] = int(colour.split(' ')[0])
        if (colours['red'] > 12 or colours['green'] > 13 or colours['blue'] > 14):
            possible = False
    # print(id, plays)
    if(possible):
        id_sum += id
        # print(f'{id} is possible')

print(id_sum)

# part 2
# find the fewest amount of cubes required to play a round, then multiply those minimums

powers = 0
for game_str in str_dump:
    id_str, plays_str = game_str.split(': ')
    id = int(id_str[5:]) # game xxx
    plays = plays_str.split('; ')

    colours = {'red': 0, 'green': 0, 'blue': 0}
    for play in plays:
        colours_str = play.split(', ')
        for colour in colours_str:
            if(colours[colour.split(' ')[1]] < int(colour.split(' ')[0])):
                colours[colour.split(' ')[1]] = int(colour.split(' ')[0])
    # print(f"id {id}: red {colours['red']}, green {colours['green']}, blue {colours['blue']}")
    powers += colours['red'] * colours['green'] * colours['blue']

print(powers)