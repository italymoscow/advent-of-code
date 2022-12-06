'''
Solution to the Day 6, Part 1 and 2.

Task, Part 1 and 2:
    How many characters need to be processed before the first start-of-packet marker is detected?

Returns:
    PART1. Processed characters:  1779
    PART2. Processed characters:  2635
'''


import os


def part_1():
    '''
    Solution to Part 1. Prints the result.
    '''
    seq_len = 4
    index_first = 0
    while index_first < len(input_string) + seq_len - 1:
        index_last = index_first + seq_len
        sequence = input_string[index_first:index_last]
        if len(set(sequence)) == seq_len:
            print("PART1. Processed characters: ", index_last)
            break
        index_first += 1


def part_2():
    '''
    Solution to Part 2. Prints the result.
    '''
    seq_len = 14
    index_first = 0
    while index_first < len(input_string) + seq_len - 1:
        index_last = index_first + seq_len
        sequence = input_string[index_first:index_last]
        if len(set(sequence)) == seq_len:
            print("PART2. Processed characters: ", index_last)
            break
        index_first += 1


# Extract initial stack information and movement instructions from input file
cur_path = os.path.dirname(os.path.abspath(__file__))
input_file = open(cur_path + "\\06_input.txt", "r")
input_string = input_file.readline().strip()
input_file.close()


if __name__ == "__main__":
    part_1()
    part_2()
