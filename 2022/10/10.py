"""
Solution to the Day 10, Part 1 and 2.

Returns:
    PART 1. The sum of all signal strengths: 15220
    PART 2. Screen:
    ###..####.####.####.#..#.###..####..##..
    ####.#.......#.#....#.#..#..#.#....#..#.
    #..#.###....#..###..##...###..###..#..#.
    ###..#.....#...#....#.#..#..#.#....####.
    ###..#....#....#....#.#..#..#.#....#..#.
    #..#.#....####.####.#..#.###..#....#..#.

"""

import logging
import os


def print_screen(screen_pixels: list):
    for i in range(6):
        print("".join(screen_pixels[i]))


def part_1():
    """
    Solution to Part 1. Prints the result.
    """
    cycle_count = 0
    register = 1
    signal_cycle = 20
    signal_strength_total = 0

    for input_string in input_strings:
        logging.debug("Register before the command " +
                      input_string.rstrip() + ": " + str(register))
        logging.debug("Cycle before the command " +
                      input_string.rstrip() + ": " + str(cycle_count))
        if input_string.startswith("a"):  # "addx V"
            reg_change = int(input_string.rstrip().split(" ")[1])
            cycle_count += 1
            if cycle_count == signal_cycle:
                signal_strength = cycle_count * register
                logging.debug("Cycle count: " + str(cycle_count) + " - Register: " +
                              str(register) + " - Signal strength: " + str(signal_strength))
                signal_strength_total += signal_strength
                signal_cycle += 40
            cycle_count += 1
            if cycle_count == signal_cycle:
                signal_strength = cycle_count * register
                logging.debug("Cycle count: " + str(cycle_count) + " - Register: " +
                              str(register) + " - Signal strength: " + str(signal_strength))
                signal_strength_total += signal_strength
                signal_cycle += 40
            register += reg_change
        else:  # noop
            cycle_count += 1
            if cycle_count == signal_cycle:
                signal_strength = cycle_count * register
                logging.debug("Cycle count: " + str(cycle_count) + " - Register: " +
                              str(register) + " - Signal strength: " + str(signal_strength))
                signal_strength_total += signal_strength
                signal_cycle += 40
    logging.debug("Last cycle_count: " + str(cycle_count))
    print("PART 1. The sum of all signal strengths:", signal_strength_total)


def part_2():
    """
    Solution to Part 2. Prints the result.
    """
    cycle = 0
    register = 1
    cycles_per_row = 40
    row = 0
    position = 0
    next_row_cycle = cycles_per_row
    # Initial sprite position: # [0, 1, 2]
    sprite_positions = [register - 1, register, register + 1]
    screen_pixels = []
    for j in range(6):
        screen_pixels.append(list("." * cycles_per_row))

    for input_string in input_strings:
        logging.debug("Command: " + input_string.rstrip())
        logging.debug("Register: " + str(register))
        logging.debug("Cycle: " + str(cycle))
        logging.debug("Sprite position: " + str(sprite_positions))

        if input_string.startswith("a"):  # "addx V" - two cycles
            reg_change = int(input_string.rstrip().split(" ")[1])

            # begin executing
            cycle += 1

            update_screen(screen_pixels, position, sprite_positions, row)

            # Move pixel position to the right
            position += 1

            # if reached the end of the screen,
            # move to the next row and set the sprite to the left
            if cycle == next_row_cycle:
                row += 1
                position = 0
                sprite_positions = [0, 1, 2]
                next_row_cycle += cycles_per_row

            cycle += 1

            update_screen(screen_pixels, position, sprite_positions, row)

            # Move pixel position to the right
            position += 1

            # Move to the next row and set the sprite to the left
            if cycle == next_row_cycle:
                row += 1
                position = 0
                sprite_positions = [0, 1, 2]
                next_row_cycle += cycles_per_row

            register += reg_change
            sprite_positions = [register - 1, register, register + 1]
        else:  # noop
            cycle += 1

            update_screen(screen_pixels, position, sprite_positions, row)

            position += 1

            # Move to the next row and set the sprite to the left
            if cycle == next_row_cycle:
                row += 1
                position = 0
                sprite_positions = [0, 1, 2]
                next_row_cycle += cycles_per_row

    logging.debug("Last cycle_count: " + str(cycle))

    print("PART 2. Screen:")
    print_screen(screen_pixels)


def update_screen(screen_pixels: list, position: int, sprite_positions: list, row: int):
    """
    Returns updated list screen_pixels with a new lit/unlit pixel 
    with coordinates (position, row). The pixel is lit if its coordinates
    are inside the sprite_positions list of coordinates.
    """
    if position in sprite_positions:
        screen_pixels[row][position] = "#"
    else:
        screen_pixels[row][position] = "."


def read_input(file_name: str):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\" + file_name, "r")
    input_strings = input_file.readlines()
    input_file.close()
    return input_strings


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    logging.disable(logging.CRITICAL)
    input_strings = read_input("10_input.txt")
    part_1()
    part_2()
