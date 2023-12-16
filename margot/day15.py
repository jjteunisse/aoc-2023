import sys

def hash_algorithm(string:str)->int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value = (17*current_value)%256
    return current_value


def main():
    name = "input"

    sum_hashes = 0
    with open("inputs/day15/{}.txt".format(name)) as file:
        line = next(file).rstrip()
    
    #(Task 2) Initialize dictionaries for box contents.
    #No need to distinguish labels per box, since label determines box id.
    lenses = {i:[] for i in range(256)}
    focal_lengths = {}
    
    for string in line.split(","):
        sum_hashes += hash_algorithm(string)
        
        if "=" in string:
            label, focal_length = string.split("=")
            box_id = hash_algorithm(label)
            if not label in focal_lengths:
                lenses[box_id].append(label)
            focal_lengths[label] = focal_length
        
        if "-" in string:
            label = string.strip("-")
            box_id = hash_algorithm(label)
            focal_lengths.pop(label, None)
            if label in lenses[box_id]:
                lenses[box_id].remove(label)
                
    print("Sum (task 1):", sum_hashes)
            
    total_focussing_power = 0
    for box_id in lenses:
        for i, label in enumerate(lenses[box_id]):
            total_focussing_power += (box_id+1)*(i+1)*int(focal_lengths[label])
    
    print("Total focussing power (task 2):", total_focussing_power)

if __name__ == "__main__":
    sys.exit(main())

