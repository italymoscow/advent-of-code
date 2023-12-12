from os import path
from datetime import datetime
from itertools import combinations


def main():

    # Read the input file
    cur_path = path.dirname(path.abspath(__file__))
    input_file = open(cur_path + "\\11_input.txt", "r")
    image = input_file.readlines()
    input_file.close()

    # Parse input
    for index, row in enumerate(image):
        image[index] = list(char for char in row.rstrip())
        # print(image[index])

    # Duplicate rows without galaxies
    duplicate_rows_without_galaxies(image)

    # Duplicate columns without galaxies
    transposed_list = list(map(list, zip(*image)))
    duplicate_rows_without_galaxies(transposed_list)
    image = list(map(list, zip(*transposed_list)))

    # Find coordinates of all galaxies
    galaxies = get_galaxies(image)

    # Find unique pairs of galaxies
    pairs = get_galaxy_pairs(galaxies)
    print("Number of galaxy pairs:", len(pairs))

    # Find the shortest routes in galaxy pairs
    sum_paths = 0
    for pair in pairs:
        shortest_path_len = get_shortest_route_len(pair)
        sum_paths += shortest_path_len

    print("Sum of shortest paths lengths:", sum_paths)


def get_shortest_route_len(galaxy_pair: list):
    galaxy1 = galaxy_pair[0]
    galaxy2 = galaxy_pair[1]
    x_path_len = abs(galaxy1[0] - galaxy2[0])
    y_path_len = abs(galaxy1[1] - galaxy2[1])
    shortest_route_len = x_path_len + y_path_len
    # print("Galaxy pair:", galaxy_pair, ":", shortest_route_len)

    return shortest_route_len


def duplicate_rows_without_galaxies(image: list):
    index = 0
    col_cnt = len(image[0])
    while index < len(image):
        if image[index].count(".") == col_cnt:
            image.insert(index, image[index])
            index += 1
        index += 1


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
