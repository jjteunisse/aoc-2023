from laurens.util.file_reader import read_from_file

TEST = True

if __name__ == '__main__':
    values = []
    if TEST:
        values = read_from_file("./data/day_5_test.txt")
    else:
        values = read_from_file("./data/day_5.txt")

    print("Task 1: ")
    print("Task 2: ")