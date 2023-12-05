from laurens.util.file_reader import read_from_file

TEST = True


def get_conversion_lists(values: list):
    conversion_lists = []
    conversion_list = []

    for i in range(2, len(values)):
        if values[i].strip() == "":
            conversion_lists.append(conversion_list.copy())
            conversion_list = []
            continue

        if values[i][0].isdigit():
            conversion_list.append(values[i].split(" "))

    conversion_lists.append(conversion_list.copy())

    return conversion_lists


def task_1(values: list):
    seeds = values[0].split(":")[1].strip().split(" ")
    conversion_lists = get_conversion_lists(values)
    location_entries = conversion_lists.pop()
    conversion_lists_reversed = reversed(conversion_lists)
    location = 0
    found_location = -1

    while found_location == -1:
        for index, entry in enumerate(location_entries):
            previous_index = -1
            if location in range(int(entry[0]), int(entry[0]) + int(entry[2])):
                previous_index = location - int(entry[0]) + int(entry[1])

            if index == len(location_entries) - 1:
                previous_index = location

            if previous_index != -1:
                for conversion_list in conversion_lists_reversed:
                    for e in conversion_list:
                        if previous_index in range(int(e[0]), int(e[0]) + int(e[2]) + 1):
                            previous_index = previous_index - int(e[0]) + int(e[1])
                            break

            if str(previous_index) in seeds:
                return location

        location += 1


def task_2(values: list):
    found_values = values[0].split(":")[1].strip().split(" ")
    seed_ranges = []

    while len(found_values) > 0:
        first_index = int(found_values.pop(0))
        found_range = int(found_values.pop(0))

        seed_ranges.append([first_index, first_index + found_range])

    conversion_lists = get_conversion_lists(values)
    location_entries = conversion_lists.pop()
    conversion_lists_reversed = list(reversed(conversion_lists))
    location = 0
    found_location = -1

    while found_location == -1:
        for index, entry in enumerate(location_entries):
            previous_index = -1
            if location in range(int(entry[0]), int(entry[0]) + int(entry[2])):
                previous_index = location - int(entry[0]) + int(entry[1])

            if index == len(location_entries) - 1:
                previous_index = location

            if previous_index != -1:
                for conversion_list in conversion_lists_reversed:
                    for e in conversion_list:
                        if previous_index in range(int(e[0]), int(e[0]) + int(e[2]) + 1):
                            previous_index = previous_index - int(e[0]) + int(e[1])
                            break

            for seed_range in seed_ranges:
                if seed_range[0] <= previous_index <= seed_range[1]:
                    return location

        location += 1


if __name__ == '__main__':
    values = []
    if TEST:
        values = read_from_file("./data/day_5_test.txt")
    else:
        values = read_from_file("./data/day_5.txt")

    print("Task 1: " + str((task_1(values))))
    print("Task 2: " + str((task_2(values))))
