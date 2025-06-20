import os
import time
import re


def get_lines():
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\04_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()
    lines = [line.strip() for line in lines]

    return lines


def count_matches_in_line(pattern: str, text: str):

    return len(re.findall(pattern, text))


def count_matches_in_lines(pattern: str, lines: list):
    xmas_count = 0
    for line in lines:
        xmas_count += count_matches_in_line(pattern, line)

    return xmas_count


def get_diagonal_lines(lines: list):
    lines_chars = [list(string) for string in lines]
    diagonal_lines = []

    # Top-left to bottom-right diagonals
    for i in range(len(lines_chars)):
        diagonal = []
        for j in range(i + 1):
            diagonal.append(lines_chars[i - j][j])
        diagonal_lines.append(diagonal)

    for i in range(1, len(lines_chars[0])):  # Start from the second column
        diagonal = []
        for j in range(len(lines_chars) - i):
            diagonal.append(lines_chars[len(lines_chars) - 1 - j][i + j])
        diagonal_lines.append(diagonal)

    # Top-right to bottom-left diagonals
    for i in range(len(lines_chars)):
        diagonal = []
        for j in range(i + 1):
            diagonal.append(lines_chars[i - j][-(j + 1)])
        diagonal_lines.append(diagonal)

    for i in range(1, len(lines_chars[0])):  # Start from the second column
        diagonal = []
        for j in range(len(lines_chars) - i):
            diagonal.append(lines_chars[len(lines_chars) - 1 - j][-(i + j + 1)])
        diagonal_lines.append(diagonal)

    return diagonal_lines


def main():

    lines = get_lines()

    time_start = time.time()

    xmas_count = 0

    # Horizontally
    xmas_count += count_matches_in_lines("XMAS", lines)
    xmas_count += count_matches_in_lines("SAMX", lines)

    # Vertically
    transposed_lines = list(zip(*lines))
    transposed_lines = ["".join(list(row)) for row in transposed_lines]
    xmas_count += count_matches_in_lines("XMAS", transposed_lines)
    xmas_count += count_matches_in_lines("SAMX", transposed_lines)

    # Diagonally
    diagonal_lines = get_diagonal_lines(lines)
    diagonal_lines = ["".join(list(row)) for row in diagonal_lines]
    xmas_count += count_matches_in_lines("XMAS", diagonal_lines)
    xmas_count += count_matches_in_lines("SAMX", diagonal_lines)

    time_total = time.time() - time_start
    print("XMAS count: ", xmas_count, "\nTime: ", time_total, " sec")

    # 1724 is too low


if __name__ == "__main__":
    main()
