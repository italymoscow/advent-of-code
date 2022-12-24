"""
Solution to the Day 18, Part 1 and 2.

Returns:
    PART 1. Exposed surfaces:  3448
"""

import logging
import os
from datetime import datetime


def part_1():
    """
    Solution to Part 1.
    """
    logging.info("Started: " + str(datetime.now()))

    s = 1  # size of the side of the cube
    surfaces = []

    # Get a list of all the surfaces based on the input file
    for line in input_lines:
        coord = line.rstrip().split(",")
        x = int(coord[0])
        z = int(coord[2])
        y = int(coord[1])
        new_cube_surfaces = define_cube_surfaces(x, y, z, s)

        surfaces += new_cube_surfaces

    # Count duplicates
    covered_sides_cnt = 0
    for i in range(0, len(surfaces)):
        dup_cnt = 1
        for j in range(i + 1, len(surfaces)):
            if surfaces[i] == surfaces[j]:
                dup_cnt += 1
        if dup_cnt != 1:
            covered_sides_cnt += dup_cnt

    logging.info("Finished: " + str(datetime.now()))

    print("PART 1. Exposed surfaces: ", len(surfaces) - covered_sides_cnt)


def define_cube_surfaces(x: int, y: int, z: int, s: int):
    """
    Return a list of coordinates of all surfaces of a cube of size s with
    starting coordinate (x, y, z).
    Returns list[list[tuple[int, int, int]]]
    """
    a = (x, y, z)
    b = (x + s, y, z)
    c = (x, y + s, z)
    d = (x + s, y + s, z)

    e = (x, y, z + s)
    f = (x + s, y, z + s)
    g = (x, y + s, z + s)
    h = (x + s, y + s, z + s)

    abcd = [a] + [b] + [c] + [d]
    efgh = [e] + [f] + [g] + [h]
    abef = [a] + [b] + [e] + [f]
    cdgh = [c] + [d] + [g] + [h]
    aceg = [a] + [c] + [e] + [g]
    bdfh = [b] + [d] + [f] + [h]
    cube = [abcd] + [efgh] + [abef] + [cdgh] + [aceg] + [bdfh]

    return cube


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
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    # logging.disable(logging.CRITICAL)
    input_lines = read_input("day_18_input.txt")
    part_1()
    # part_2()
