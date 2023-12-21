from os import path
from datetime import datetime


def main():

    # Read the input file
    cur_path = path.dirname(path.abspath(__file__))
    input_file = open(cur_path + "\\14_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Parse each line into a list of chars
    for index, line in enumerate(lines):
        lines[index] = list(char for char in line.rstrip())

    # Transpose the list for convenience
    transposed_rows = list(map(list, zip(*lines)))

    # Move stones on each row
    for i, row in enumerate(transposed_rows):
        transposed_rows[i] = move_stones(row)

    # Transpose the resulting list back
    lines = list(map(list, zip(*transposed_rows)))

    # Calculate the loads
    total_load = 0
    for i, line in enumerate(lines):
        load = line.count("O") * (len(lines) - i)
        total_load += load

    print("Total load:", total_load)


def move_stones(row: list):
    char_index = 1
    while char_index < len(row):
        result = move_stone(row, char_index)
        row = result[0]
        char_index = result[1]

    return row


def move_stone(row: list, char_index: int):
    char_cur = row[char_index]
    char_prev = row[char_index - 1]
    if char_cur == "O":
        if char_prev == "#" or char_prev == "O":
            row[char_index] = char_cur
            char_index += 1
        else:
            row[char_index - 1] = char_cur
            row[char_index] = "."
            if char_index > 1:
                char_index -= 1
    else:
        char_index += 1
        
    return [row, char_index]


if __name__ == "__main__":
    time_start = datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
