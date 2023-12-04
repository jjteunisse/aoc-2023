from laurens.util.file_reader import read_from_file

TEST = False


def number_string_to_list(string: str):
    list = string.strip().split(" ")
    return [num for num in list if num]


def get_amount_matching(game_card: str):
    game_card = game_card.split(":")[1].strip()
    winning_numbers = number_string_to_list(game_card.split("|")[0])
    card_numbers = number_string_to_list(game_card.split("|")[1])

    amount_matching = 0
    for winning_number in winning_numbers:
        if winning_number in card_numbers:
            amount_matching += 1

    return amount_matching


def get_total_cards(game_cards: list):
    total_cards = 0
    score_dictionary = []

    for x in range(0, len(game_cards)):
        score_dictionary.append(None)

    index = len(game_cards) - 1

    while index >= 0:
        wins = get_amount_matching(game_cards[index])
        first_index = index + 1
        last_index = index + wins

        card_score = 1
        for i in range(first_index, last_index + 1):
            if i < len(game_cards):
                card_score += score_dictionary[i]

        score_dictionary[index] = card_score

        index -= 1

    for i in range(0, len(game_cards)):
        total_cards += score_dictionary[i]

    return total_cards


if __name__ == '__main__':
    game_cards = []
    if TEST:
        game_cards = read_from_file("./data/day_4_test_1.txt")
    else:
        game_cards = read_from_file("./data/day_4.txt")

    task_1_result = 0

    for game_card in game_cards:
        amount_matching = get_amount_matching(game_card)
        if amount_matching > 0:
            task_1_result += 2 ** (amount_matching - 1)

    print("Task 1: " + str(task_1_result))
    print("Task 2: " + str(get_total_cards(game_cards)))
