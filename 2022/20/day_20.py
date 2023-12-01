"""
Solution to the Day 20, Part 1 and 2.

Returns:
    PART 1. The sum of the three numbers that form the grove coordinates =  589
    (That's not the right answer; your answer is too low)
    The test file works.
"""

import logging
import os


def part_1():
    """
    Solution to Part 1.
    """

    nums = list(map(int, input_lines.copy()))
    i = 0
    for line in input_lines:
        num = int(line.rstrip())
        index_in_nums = nums.index(num)

        num_new_index = get_num_new_index(num, index_in_nums, nums)

        nums.insert(num_new_index, num)
        if num_new_index > index_in_nums:
            nums.pop(index_in_nums)
        else:
            nums.pop(index_in_nums + 1)

    num_1000 = get_number_after_zero(1000, nums)
    logging.debug("num_1000 = " + str(num_1000))

    num_2000 = get_number_after_zero(2000, nums)
    logging.debug("num_2000 = " + str(num_2000))

    num_3000 = get_number_after_zero(3000, nums)
    logging.debug("num_3000 = " + str(num_3000))

    the_sum = sum([num_1000, num_2000, num_3000])

    print("PART 1. The sum of the three numbers that form the grove coordinates = ", the_sum)


def part_2():
    """
    Solution to Part 2. Incorrect.
    """

    print("PART 2.")


def get_number_after_zero(n: int, nums: list):
    zero_index = nums.index(0)
    nums_len = len(nums)
    rest = n % nums_len
    if zero_index + rest > nums_len:
        num = nums[zero_index + rest - nums_len]
    else:
        num = nums[zero_index + rest]
    return num


def get_num_new_index(num: int, index: int, nums: list[int]):
    rest = abs(num) % len(nums)
    if num >= 0:
        num_new_index = index + rest + 1
    else:
        num_new_index = index - rest

    if num_new_index >= len(nums):
        num_new_index = num_new_index - len(nums)
    if abs(num_new_index) >= len(nums):
        num_new_index = len(nums) - (abs(num_new_index) - len(nums))
    elif num_new_index <= 0:
        num_new_index = len(nums) + num_new_index
    return num_new_index


def read_input(file_name: str):
    """
    Return a list containing all the lines of the input file.
    Parameters:
        file_name, str, name of the input file
    """
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\" + file_name, "r")
    file_contents = input_file.readlines()
    input_file.close()
    return file_contents


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    # logging.disable(logging.CRITICAL)
    input_lines = read_input("day_20_input_test.txt")
    part_1()
    # part_2()
