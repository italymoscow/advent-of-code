'''
Solution to the Day 1: Calorie Counting, Part 1.

Task: Find the Elf carrying the most Calories. 
    How many total Calories is that Elf carrying?

Returns:
"Elf 21 carries the most calories; 68802 to be exact."
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

    # Find max and print the result
    max_cal_per_elf = max(elf_cal_dict.values())
    for key, value in elf_cal_dict.items():
        if value == max_cal_per_elf:
            print("Elf " + str(key) + " carries the most calories; "
                  + str(max_cal_per_elf) + " to be exact.")
            break  # The first elf with max calories wins


if __name__ == "__main__":
    main()
