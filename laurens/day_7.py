from laurens.util.file_reader import read_from_file
from enum import Enum

TEST = True


class Hand:
    def __init_(self, cards: list, bet: int):
        self.cards: list = cards
        self.bet: int = bet

class Score(Enum):
    ONE_OF_A_KIND = 1
    TWO_OF_A_KIND = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


def get_hand_score(hand: str):
    return Score.ONE_OF_A_KIND


def get_total_score(hands: list):
    total_score = 0

    for hand in hands:
        total_score += get_hand_score(hand)

    return total_score


if __name__ == '__main__':
    hands = []
    if TEST:
        hands = read_from_file("./data/day_7_test.txt")
    else:
        hands = read_from_file("./data/day_7.txt")

    print("Task 1: " + str(get_total_score(['hand', 'hand'])))
    print("Task 2: ")