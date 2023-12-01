'''
Solution to the Day 1: Calorie Counting, Part 2.

Task: Find the top three Elves carrying the most Calories. 
    How many Calories are those Elves carrying in total?

Returns:
"The three elves carrying most of the calories: 
21: 68802
155: 68708
119: 67860
These elves are carrying 205370 calories in total."
'''


import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\01_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Create elf-calories dict
    elf_cal_dict = {}
    elf_count = 1
    cal_per_elf = 0
    for line in lines:
        if line.strip():
            cal_per_elf += int(line)
            elf_cal_dict[elf_count] = cal_per_elf
        else:
            cal_per_elf = 0
            elf_count += 1

    # Get list of top three calories per elf
    elves = list(elf_cal_dict.keys())
    calories = list(elf_cal_dict.values())
    calories_sorted = calories.copy()
    calories_sorted.sort()
    top3_cal_per_elf = calories_sorted[-3:]
    top3_cal_per_elf.sort(reverse=True)

    top3_cal_total = sum(top3_cal_per_elf)

    print("The three elves carrying most of the calories: ")
    for cal_per_elf in top3_cal_per_elf:
        position = calories.index(cal_per_elf)
        print(str(elves[position]) + ": " + str(cal_per_elf))
    print("These elves are carrying " +
          str(top3_cal_total) + " calories in total.")


if __name__ == "__main__":
    main()
