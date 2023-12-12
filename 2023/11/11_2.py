from os import path
from datetime import datetime
from itertools import combinations

expansion = 1000000


def main():

    # Read the input file
    cur_path = path.dirname(path.abspath(__file__))
    input_file = open(cur_path + "\\11_input.txt", "r")
    image = input_file.readlines()
    input_file.close()

    # Parse input
    for index, row in enumerate(image):
        image[index] = list(char for char in row.rstrip())

    # Get empty rows numbers
    empty_rows = get_rows_without_galaxies(image)

    # Get empty columns numbers
    transposed_list = list(map(list, zip(*image)))
    empty_columns = get_rows_without_galaxies(transposed_list)

    # Find coordinates of all galaxies
    galaxies = get_galaxies(image)

    # Find unique pairs of galaxies
    pairs = get_galaxy_pairs(galaxies)
    print("Number of galaxy pairs:", len(pairs))

    # Find the shortest routes in galaxy pairs
    sum_paths = 0
    for pair in pairs:
        shortest_path_len = get_shortest_route_len(
            pair, empty_rows, empty_columns)
        sum_paths += shortest_path_len

    print("Sum of shortest paths lengths:", sum_paths)


def get_shortest_route_len(galaxy_pair: list, empty_rows, empty_columns):
    galaxy1 = galaxy_pair[0]
    galaxy2 = galaxy_pair[1]

    voids_cnt = get_voids_cnt_bw_galaxies(
        galaxy_pair, empty_rows, empty_columns)
    x_path_len = abs(galaxy1[0] - galaxy2[0]) + (expansion - 1) * voids_cnt[0]
    y_path_len = abs(galaxy1[1] - galaxy2[1]) + (expansion - 1) * voids_cnt[1]
    shortest_route_len = x_path_len + y_path_len
    # print("Galaxy pair:", galaxy_pair, ":", shortest_route_len, "(", x_path_len, "+", y_path_len, ")")

    return shortest_route_len


def get_voids_cnt_bw_galaxies(galaxy_pair: list, empty_rows: list, empty_columns: list):
    galaxy1 = galaxy_pair[0]
    galaxy2 = galaxy_pair[1]

    # Count X-voids
    x_voids_cnt = get_voids_cnt(
        first=galaxy1[0], last=galaxy2[0], empty_list=empty_rows)

    # Count Y-voids
    y_voids_cnt = get_voids_cnt(
        first=galaxy1[1], last=galaxy2[1], empty_list=empty_columns)

    return [x_voids_cnt, y_voids_cnt]


def get_voids_cnt(first: int, last: int, empty_list: list):
    voids_cnt = 0
    if first < last:
        step = 1
    else:
        step = -1
    for void in empty_list:
        if void in range(first, last, step):
            voids_cnt += 1

    return voids_cnt


def get_rows_without_galaxies(image: list):
    empty_rows = []
    index = 0
    col_cnt = len(image[0])
    for index, row in enumerate(image):
        if row.count(".") == col_cnt:
            empty_rows.append(index)

    return empty_rows


def get_galaxies(image: list):
    galaxies = []
    for x, row in enumerate(image):
        for y, char in enumerate(row):
            if char == "#":
                galaxies.append([x, y])

    return galaxies


def get_galaxy_pairs(galaxies: list):
    pairs = []
    for pair in combinations(galaxies, 2):
        pairs.append(pair)

    return pairs


if __name__ == "__main__":
    time_start = datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
