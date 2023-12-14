from os import path
from datetime import datetime


def main():

    # Read the input file
    cur_path = path.dirname(path.abspath(__file__))
    input_file = open(cur_path + "\\13_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Parse input into a list of patterns: [[pattern1], [pattern2], ...]
    patterns = []
    index_outer = 0
    while index_outer < len(lines):
        pattern = []
        index_inner = 0
        for line in lines[index_outer:]:
            if line != "\n":
                pattern.append(list(char for char in line.rstrip()))
                index_inner += 1
            else:
                index_inner += 1
                break
        patterns.append(pattern)
        index_outer += index_inner

    sum_of_cols_left_of_mirror = 0
    sum_of_rows_above_mirror = 0
    for index, pattern in enumerate(patterns):

        # Check rows
        mirror_pos_rows = get_mirror_pos(pattern)
        sum_of_rows_above_mirror += mirror_pos_rows

        # Check columns (transpose to rows to make it easier)
        transposed_pattern = list(map(list, zip(*pattern)))
        for sublist in transposed_pattern:
            sublist.reverse()
        mirror_pos_cols = get_mirror_pos(transposed_pattern)
        sum_of_cols_left_of_mirror += mirror_pos_cols

        print("Pattern", index, "of", len(patterns) - 1,
              "(", mirror_pos_rows, ",", mirror_pos_cols, ")")
        if mirror_pos_rows == mirror_pos_cols:
            print("------------------")
    
    # Calculate the summarized data
    result = sum_of_cols_left_of_mirror + 100 * sum_of_rows_above_mirror

    print("Result:", result)  # 29870 is too high, 28803 is too low


def get_mirror_pos(pattern: list):
    
    # Get mirror position based on the top row
    mirror_pos = get_mirror_pos_helper(pattern, direction=-1, base_pos=0, row_index=len(pattern) - 1)

    # Get mirror position based on the bottom row if based on top returned zero
    if mirror_pos == 0:
        mirror_pos = get_mirror_pos_helper(pattern, direction=1, base_pos=len(pattern) - 1, row_index=0)

    return mirror_pos


def get_mirror_pos_helper(pattern: list, direction: int, base_pos: int, row_index):
    mirror_pos = 0
    while row_index * direction < base_pos * direction:
        if pattern[row_index] == pattern[base_pos]:
            # Check rows in between
            if direction == -1:
                start_row = base_pos
                finish_row = row_index
            else:
                start_row = row_index
                finish_row = base_pos
            if has_mirrored_row(pattern, start_row, finish_row):
                mirror_pos = (row_index + base_pos + 1) // 2
                break
            else:
                row_index += 1 * direction
        else:
            row_index += 1 * direction
    
    return mirror_pos


def has_mirrored_row(pattern: list, start_row, finish_row):
    if finish_row - start_row > 1:
        if pattern[start_row] == pattern[finish_row]:
            return has_mirrored_row(pattern, start_row + 1, finish_row - 1)
        else:
            return False
    elif finish_row - start_row == 1:
        if pattern[start_row] == pattern[finish_row]:
            return True
        else:
            return False
    else:
        return True


if __name__ == "__main__":
    time_start = datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
