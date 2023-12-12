from itertools import pairwise
import os
import datetime

pipe_len = 0

# {direction_char: [[up], [down], [left], [right]]}
directions = {
    "|": [[-1, 0], [1, 0], [0, 0], [0, 0]],
    "-": [[0, 0], [0, 0], [0, -1], [0, 1]],
    "L": [[0, 0], [0, 1], [-1, 0], [0, 0]],
    "J": [[0, 0], [0, -1], [0, 0], [-1, 0]],
    "7": [[0, -1], [0, 0], [0, 0], [1, 0]],
    "F": [[0, 1], [0, 0], [1, 0], [0, 0]],
    ".": [[0, 0], [0, 0], [0, 0], [0, 0]]
}


def main():

    # Read the input file
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\10_input_test.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Parse input
    for index, line in enumerate(lines):
        lines[index] = list(char for char in line.rstrip())
        # print(lines[index])

    # Find starting position
    starting_pos = get_starting_pos(lines, "S")
    print("Starting position:", starting_pos)

    # Find first step in the loop
    first_step_pos = get_first_step_pos(lines, starting_pos)
    print("First step position:", first_step_pos)

    positions = [starting_pos, first_step_pos]

    if first_step_pos != starting_pos:
        pipe_len = + 1
    else:
        print("Pipeline length: ", pipe_len,
              "\nSteps to the farthest position from the start: ", pipe_len)
        return

    # Find loop
    while positions[1] != starting_pos:
        positions = get_next_pos(
            lines, cur_pos=positions[1], prev_pos=positions[0])
        pipe_len += 1

    # Find and print the furthermost point in the loop
    print("Pipeline length:", pipe_len,
          "\nSteps to the farthest position from the start:", pipe_len // 2)


def get_starting_pos(input_list: list, start_char: str):
    for sublist in input_list:
        for element in sublist:
            if element == start_char:
                return [input_list.index(sublist), sublist.index(element)]
    return None


def get_first_step_pos(input_list: list, starting_pos: list):
    # Check on the right:
    pos = [starting_pos[0], starting_pos[1] + 1]
    if is_pos_on_map(input_list, pos):
        # Check if pipe on the right is "-", "J", "7"
        direction = input_list[pos[0]][pos[1]]
        if input_list[pos[0]][pos[1]] in ("-", "J", "7"):
            return pos

    # Check on the left:
    pos = [starting_pos[0], starting_pos[1] - 1]
    if is_pos_on_map(input_list, pos):
        # Check if pipe on the left is "-", "L", "F"
        if input_list[pos[0]][pos[1]] in ("-", "L", "F"):
            return pos

    # Check above:
    pos = [starting_pos[0] - 1, starting_pos[1]]
    if is_pos_on_map(input_list, pos):
        # Check if pipe on the left is "|", "F", "7"
        if input_list[pos[0]][pos[1]] in ("|", "F", "7"):
            return pos

    # Check below:
    pos = [starting_pos[0] + 1, starting_pos[1]]
    if is_pos_on_map(input_list, pos):
        # Check if pipe on the left is "|", "J", "L"
        if input_list[pos[0]][pos[1]] in ("|", "J", "L"):
            return pos

    return None


def is_pos_on_map(input_list: list, pos: list):
    # Check x
    if pos[0] < 0 or pos[0] + 1 > len(input_list):
        return False

    # Check y
    if pos[1] < 0 or pos[1] + 1 > len(input_list[0]):
        return False

    return True


def get_next_pos(input_list: list, cur_pos: list, prev_pos: list):
    direction = input_list[cur_pos[0]][cur_pos[1]]

    # moving up:
    if prev_pos[0] > cur_pos[0]:
        direction_coord = directions[direction][0]

    # moving down
    elif prev_pos[0] < cur_pos[0]:
        direction_coord = directions[direction][1]

    # moving left
    elif prev_pos[1] > cur_pos[1]:
        direction_coord = directions[direction][2]

    # moving right
    else:
        direction_coord = directions[direction][3]

    next_pos = [cur_pos[0] + direction_coord[0],
                cur_pos[1] + direction_coord[1]]

    return [cur_pos, next_pos]


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
