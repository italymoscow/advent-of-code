"""
Solution to the Day 18, Part 1 and 2.

Returns:
    PART 1. Exposed surfaces:  3448
    PART 2. External surfaces:  1698 (That's not the right answer; your answer is too low)
"""

import logging
import os


def part_1():
    """
    Solution to Part 1.
    """

    # Count duplicates
    covered_sides_cnt = 0
    for i in range(0, len(surfaces)):
        dup_cnt = 1
        for j in range(i + 1, len(surfaces)):
            if surfaces[i] == surfaces[j]:
                dup_cnt += 1
        if dup_cnt != 1:
            covered_sides_cnt += dup_cnt

    print("PART 1. Exposed surfaces: ", len(surfaces) - covered_sides_cnt)


def part_2():
    """
    Solution to Part 2. Incorrect.
    """

    # Flatten the coordinates by removing a specific axis
    # Count unique surfaces

    # The solution does not take into account hidden cavities

    exterior_surfaces_cnt = 0

    abcd_surfaces = []
    for i in range(0, len(surfaces), 6):
        abcd_surface = []
        # remove coord z
        for surface in surfaces[i]:
            new_coord = (surface[0], surface[1])
            abcd_surface.append(new_coord)
        abcd_surfaces.append(abcd_surface)
    exterior_surfaces_cnt += get_unique_surfaces_cnt(abcd_surfaces)

    efgh_surfaces = []
    for i in range(1, len(surfaces), 6):
        efgh_surface = []
        # remove coord z
        for surface in surfaces[i]:
            new_coord = (surface[0], surface[1])
            efgh_surface.append(new_coord)
        efgh_surfaces.append(efgh_surface)
    exterior_surfaces_cnt += get_unique_surfaces_cnt(efgh_surfaces)

    abef_surfaces = []
    for i in range(2, len(surfaces), 6):
        abef_surface = []
        # remove coord y
        for surface in surfaces[i]:
            new_coord = (surface[0], surface[2])
            abef_surface.append(new_coord)
        abef_surfaces.append(abef_surface)
    exterior_surfaces_cnt += get_unique_surfaces_cnt(abef_surfaces)

    cdgh_surfaces = []
    for i in range(3, len(surfaces), 6):
        cdgh_surface = []
        # remove coord y
        for surface in surfaces[i]:
            new_coord = (surface[0], surface[2])
            cdgh_surface.append(new_coord)
        cdgh_surfaces.append(cdgh_surface)
    exterior_surfaces_cnt += get_unique_surfaces_cnt(cdgh_surfaces)

    aceg_surfaces = []
    for i in range(4, len(surfaces), 6):
        aceg_surface = []
        # remove coord x
        for surface in surfaces[i]:
            new_coord = (surface[1], surface[2])
            aceg_surface.append(new_coord)
        aceg_surfaces.append(aceg_surface)
    exterior_surfaces_cnt += get_unique_surfaces_cnt(aceg_surfaces)

    bdfh_surfaces = []
    for i in range(5, len(surfaces), 6):
        bdfh_surface = []
        # remove coord x
        for surface in surfaces[i]:
            new_coord = (surface[1], surface[2])
            bdfh_surface.append(new_coord)
        bdfh_surfaces.append(bdfh_surface)
    exterior_surfaces_cnt += get_unique_surfaces_cnt(bdfh_surfaces)

    print("PART 2. External surfaces: ", exterior_surfaces_cnt)


def get_unique_surfaces_cnt(coords: list[list[tuple[int, int]]]):
    unique_coords = []
    for c in coords:
        if c not in unique_coords:
            unique_coords.append(c)

    return len(unique_coords)


def define_cube_surfaces():
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

    s = 1  # size of the side of the cube
    surfaces = []

    # Get a list of all the surfaces based on the input file
    for line in input_lines:
        coord = line.rstrip().split(",")
        x = int(coord[0])
        z = int(coord[2])
        y = int(coord[1])
        new_cube_surfaces = define_cube_surfaces()
        surfaces += new_cube_surfaces

    part_1()
    part_2()
