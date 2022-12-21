"""
Solution to the Day 17, Part 1 and 2.

Returns:
    PART 1. The tower of rocks is 3130 units tall.
"""

import logging
import os
import copy
from rock import Rock


def part_1():
    """
    Solution to Part 1. Prints the result.
    """

    width = 7  # width of the chamber inside the walls

    rocks = initialize_rocks()

    rocks_order = [rock.get_name() for rock in rocks]

    input_str = read_input("day_17_input.txt")

    jets = list(input_str)

    bottom = {0: [[i, 0] for i in range(width + 2)]}  # 0 and 8 are the walls

    # Loop through rocks
    for i in range(2022):
        rock_name = rocks_order[0]
        rocks_order.append(rock_name)
        rocks_order.pop(0)

        rock_cur = rocks[rock_name]

        set_starting_pos(rock_cur, bottom)

        while True:
            jet = jets[0]
            jets.append(jet)
            jets.pop(0)

            move_rock_horizontally(rock_cur, jet, bottom)
            is_bottom_reached = move_rock_down(rock_cur, bottom)

            if is_bottom_reached:
                update_bottom(rock_cur, bottom)
                break

    print("PART 1. The tower of rocks is", len(bottom) - 1, "units tall.")


def part_2():
    """
    Solution to Part 2. Prints the result.
    I guess we need to find some repetitive pattern here. But how?
    """
    print()


def rock_intersects_with_bottom(rock: Rock, bottom: dict):
    """
    Return True if bottom coordinates intersect with the ones of the rock's, else False
    """

    rock_pos_cur = rock.get_pos_cur()

    # Start from the upper bottom line
    for bottom_row in reversed(bottom):
        for rock_coord in rock_pos_cur:
            if rock_coord in bottom[bottom_row]:
                return True

    return False


def update_bottom(rock: Rock, bottom: dict):
    rock_pos_cur = rock.get_pos_cur()
    for rock_coord in rock_pos_cur:
        y = rock_coord[1]
        if bottom.get(y):
            bottom[y] += [rock_coord]
        else:
            bottom[y] = [rock_coord]


def set_starting_pos(rock_cur: Rock, bottom: dict):
    rock_init_pos = copy.deepcopy(rock_cur.get_pos_init())
    for rock_coord in rock_init_pos:
        # rock_coord[0] += 3
        rock_coord[1] += 4 + list(bottom)[-1]

    rock_cur.set_pos_cur(copy.deepcopy(rock_init_pos))
    rock_cur.set_pos_prev(copy.deepcopy(rock_init_pos))


def get_rock_min_max_x(stone_cur_pos: list):
    all_x = []
    for rock_coord in stone_cur_pos:
        all_x.append(rock_coord[0])

    return min(all_x), max(all_x)


def get_rock_min_max_y(rock_cur_pos: list):
    all_y = list()
    for rock_coord in rock_cur_pos:
        all_y.append(rock_coord[1])

    return min(all_y), max(all_y)


def move_rock_horizontally(rock: Rock, jet: str, bottom: dict):
    rock_pos_cur = rock.get_pos_cur()
    rock.set_pos_prev(copy.deepcopy(rock_pos_cur))
    rock_min_max_x = get_rock_min_max_x(rock_pos_cur)
    rock_min_max_y = get_rock_min_max_y(rock_pos_cur)
    rock_min_y = rock_min_max_y[0]  # lowest coord of the rock
    moved = False

    # Moving to the right
    if jet == ">":
        rock_max_x = rock_min_max_x[1]
        if rock_max_x < 7:  # does not touch the right wall of the chamber
            for rock_coord in rock_pos_cur:
                rock_coord[0] += 1
            moved = True

    # Moving to the left
    else:
        rock_min_x = rock_min_max_x[0]
        if rock_min_x > 1:  # does not touch the left wall of the chamber
            for rock_coord in rock_pos_cur:
                rock_coord[0] -= 1
            moved = True

    # If moved, check if the bottom is an obstacle. Cancel the move if so.
    if moved:
        if rock_min_y <= list(bottom)[-1]:
            if rock_intersects_with_bottom(rock, bottom):
                # "Return" the rock to the previous position
                rock.set_pos_cur(copy.deepcopy(rock.get_pos_prev()))


def move_rock_down(rock: Rock, bottom: dict):
    is_bottom_reached = False
    rock_pos_cur = rock.get_pos_cur()
    rock.set_pos_prev(copy.deepcopy(rock_pos_cur))

    # Move down
    for rock_coord in rock_pos_cur:
        rock_coord[1] -= 1

    rock_min_max_y = get_rock_min_max_y(rock_pos_cur)
    rock_min_y = rock_min_max_y[0]  # lowest coord of the rock

    # Check if previous rocks are not obstacles
    if rock_min_y <= list(bottom)[-1]:
        if rock_intersects_with_bottom(rock, bottom):
            # "Return" the rock to the previous position
            rock.set_pos_cur(copy.deepcopy(rock.get_pos_prev()))
            is_bottom_reached = True
            logging.debug("Rock " + str(rock.get_name())
                          + " final pos is: " + str(rock.get_pos_cur()))

    return is_bottom_reached


def read_input(file_name: str):
    """
    Return a list containing all the lines of the input file.
    Parameters:
        file_name, str, name of the input file
    """
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\" + file_name, "r")
    file_contents = input_file.read()
    input_file.close()
    return file_contents


def initialize_rocks():
    """
    Initializes the five rocks as object having initial position starting from [3, 0].
    Returns a list with the five rock objects
    """
    rocks = []
    s0 = Rock(0)
    s0.set_pos_init([[3, 0], [4, 0], [5, 0], [6, 0]])
    rocks.append(s0)

    s1 = Rock(1)
    s1.set_pos_init([[4, 0],
                     [3, 1], [4, 1], [5, 1],
                     [4, 2]])
    rocks.append(s1)

    s2 = Rock(2)
    s2.set_pos_init([[3, 0], [4, 0], [5, 0],
                     [5, 1],
                     [5, 2]])
    rocks.append(s2)

    s3 = Rock(3)
    s3.set_pos_init([[3, 0],
                     [3, 1],
                     [3, 2],
                     [3, 3]])
    rocks.append(s3)

    s4 = Rock(4)
    s4.set_pos_init([[3, 0], [4, 0],
                     [3, 1], [4, 1]])
    rocks.append(s4)

    return rocks


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    logging.disable(logging.CRITICAL)

    part_1()
    part_2()
