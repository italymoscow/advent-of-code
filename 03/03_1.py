'''
Solution to the Day 3: Rucksack Reorganization, Part 1.

Task: 
    Find the item type that appears in both compartments of each rucksack. 
    What is the sum of the priorities of those item types?

Returns:
    Rucksack: hCvHfWPPnvJhPWpqNNhqLqzLqLLd, Shared item: h, Priority: 8
    Total priority: 8394
'''


import os
import string


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\03_input.txt", "r")
    rucksacks = input_file.readlines()
    input_file.close()

    priorities = string.ascii_letters
    priorities_total = 0

    for rucksack in rucksacks:
        rucksack = rucksack.strip()
        rucksack_len = len(rucksack)
        items_comp_1 = rucksack[:int(rucksack_len/2)]
        items_comp_2 = rucksack[int(rucksack_len/2):]
        for item in items_comp_1:
            if item in items_comp_2:
                priority = priorities.index(item) + 1
                print("Rucksack: " + rucksack + ", "
                      + "Shared item: " + item + ", "
                      + "Priority: " + str(priority))
                priorities_total += priority
                break

    print("Total priority: " + str(priorities_total))


if __name__ == "__main__":
    main()
