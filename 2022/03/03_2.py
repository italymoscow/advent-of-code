'''
Solution to the Day 3: Rucksack Reorganization, Part 2.

Task: 
    Find the item type that corresponds to the badges of each three-Elf group. 
    What is the sum of the priorities of those item types?

Returns:
    Shared item: h, Priority: 8
    ...
    Total priority: 2413
'''


import os
import string


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\03_input.txt", "r")
    rucksacks = input_file.readlines()
    input_file.close()
    rucksacks_len = len(rucksacks)

    priorities = string.ascii_letters
    priorities_total = 0

    for i in range(0, rucksacks_len, 3):
        rucksack_1 = rucksacks[i].strip()
        # Check if list is long enough to avoid nullpointerexception 
        if i + 1 < rucksacks_len:
            rucksack_2 = rucksacks[i + 1].strip()
        else:
            print("Warning. The group has only one elf and thus will not be calculated..")
            continue
        if i + 2 < rucksacks_len:
            rucksack_3 = rucksacks[i + 2].strip()
        else:
            print("Warning. The group has only two elves and thus will not be calculated.")
            continue

        for item in rucksack_1:
            if item in rucksack_2 and item in rucksack_3:
                priority = priorities.index(item) + 1
                print("Shared item: " + item + ", "
                      + "Priority: " + str(priority))
                priorities_total += priority
                break

    print("Total priority: " + str(priorities_total))


if __name__ == "__main__":
    main()
