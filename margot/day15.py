import sys

def hash(string:str):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value = (17*current_value)%256
    sum += current_value


def main():
    name = "input"

    sum = 0
    with open("inputs/day15/{}.txt".format(name)) as file:
        line = next(file).rstrip()
        for string in line.split(","):
            sum += hash(string)

    print("Sum (task 1):", sum)

if __name__ == "__main__":
    sys.exit(main())

