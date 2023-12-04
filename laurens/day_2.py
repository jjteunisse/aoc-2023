from laurens.util.file_reader import read_from_file

TEST = True
BLUE = 14
GREEN = 13
RED = 12


class Game:
    def __init__(self, id, turns):
        self.id: int = id
        self.turns: list = turns


class Turn:
    def __init__(self, blue, green, red):
        self.blue: int = blue
        self.green: int = green
        self.red: int = red


def parse_game_line(game_line):
    game_id, turns_data = game_line.split(': ', 1)
    game_id = int(game_id.split(' ')[1])

    turns = turns_data.split('; ')

    turns_list = []
    for turn in turns:
        turn = turn.strip()
        blue_count = green_count = red_count = 0

        components = turn.split(', ')
        for component in components:
            count, color = component.split(' ')
            count = int(count)

            if color == 'blue':
                blue_count = count
            elif color == 'green':
                green_count = count
            elif color == 'red':
                red_count = count

        turn = Turn(blue_count, green_count, red_count)
        turns_list.append(turn)

    return Game(game_id, turns_list)


def game_possible(game: Game):
    for turn in game.turns:
        if turn.blue > BLUE:
            return False
        elif turn.green > GREEN:
            return False
        elif turn.red > RED:
            return False

    return True


def calculate_game_power(game: Game):
    highest_green = 0
    highest_blue = 0
    highest_red = 0

    for turn in game.turns:
        if turn.green > highest_green:
            highest_green = turn.green
        if turn.blue > highest_blue:
            highest_blue = turn.blue
        if turn.red > highest_red:
            highest_red = turn.red

    return highest_green * highest_blue * highest_red


if __name__ == '__main__':
    games = []
    if TEST:
        games = read_from_file("./data/day2_test.txt")
    else:
        games = read_from_file("./data/day2.txt")

    index_count = 0
    power_count = 0

    for game in games:
        if game_possible(game):
            index_count += game.id
        power_count += calculate_game_power(game)

    print('Part 1: ' + str(index_count))
    print('Part 2: ' + str(power_count))
