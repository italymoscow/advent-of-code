import os
import time
import re


def get_lines(file_name: str):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\" + file_name, "r")
    lines = input_file.readlines()
    input_file.close()
    lines = [line.strip() for line in lines]

    return [list(string) for string in lines]


def get_a_positions(lines: list):
    a_positions = []
    row_len = len(lines[0])
    col_len = len(lines)
    for x in range(1, row_len - 1):
        for y in range(1, col_len - 1):
            if lines[x][y] == "A":
                a_positions.append([x, y])

    return a_positions


def is_x_mas(a_pos: list, lines: list):
    x = a_pos[0]
    y = a_pos[1]
    tl = lines[x - 1][y - 1]
    tr = lines[x + 1][y - 1]
    bl = lines[x - 1][y + 1]
    br = lines[x + 1][y + 1]
    rd = tl + "A" + br
    ru = bl + "A" + tr
    if (rd == "MAS" or rd == "SAM") and (ru == "MAS" or ru == "SAM"):
        is_x_mas = True
    else:
        is_x_mas = False

    return is_x_mas


def main():

    time_start = time.time()

    lines = get_lines("04_input.txt")

    x_mas_count = 0

    a_positions = get_a_positions(lines)

    for a_pos in a_positions:
        if is_x_mas(a_pos, lines):
            x_mas_count += 1

    time_total = time.time() - time_start
    print("X-MAS count: ", x_mas_count, "\nTime: ", time_total, " sec")


if __name__ == "__main__":
    main()
