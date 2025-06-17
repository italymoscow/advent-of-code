from itertools import pairwise
import os
import datetime

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
    input_file = open(cur_path + "\\10_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Parse input
    for index, line in enumerate(lines):
        lines[index] = list(char for char in line.rstrip())
        # print(lines[index])

    loop_coords = []
    loop_coords_dict = {}

    # Find starting position
    starting_coord = get_starting_pos(lines, "S")
    print("Starting position:", starting_coord)
    loop_coords.append(starting_coord)
    loop_coords_dict[starting_coord[0]] = [starting_coord]

    # Find first step in the loop
    first_step_coord = get_first_step_coord(lines, starting_coord)
    print("First step position:", first_step_coord)
    loop_coords.append(first_step_coord)
    if first_step_coord[0] not in loop_coords_dict:
        loop_coords_dict[first_step_coord[0]] = first_step_coord
    else:
        loop_coords_dict[first_step_coord[0]].append(first_step_coord)

    positions = [starting_coord, first_step_coord]

    # Find loop
    while positions[1] != starting_coord:
        positions = get_next_pos(
            lines, cur_pos=positions[1], prev_pos=positions[0])
        if positions[1] not in loop_coords:
            loop_coords.append(positions[1])

        if positions[1][0] not in loop_coords_dict:
            loop_coords_dict[positions[1][0]] = []

        if positions[1] not in loop_coords_dict[positions[1][0]]:
            loop_coords_dict[positions[1][0]].append(positions[1])

    # Sort
    loop_coords.sort()
    loop_coords_dict = dict(sorted(loop_coords_dict.items()))
    loop_coords_dict = {key: sorted(values)
                        for key, values in loop_coords_dict.items()}

    print("Loop coords:", loop_coords)

    # Find extremes
    x_min = min(list(map(int, loop_coords_dict.keys())))
    x_max = max(list(map(int, loop_coords_dict.keys())))
    y_min = min(
        [value[1] for sublist in loop_coords_dict.values() for value in sublist])
    y_max = max(
        [value[1] for sublist in loop_coords_dict.values() for value in sublist])
    print("Top left coordinate:", (x_min, y_min))
    print("Bottom right coordinate:", (x_max, y_max))

    # Print loop
    print("\nLoop:")
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if [x, y] not in loop_coords:
                print(".", end="")
            else:
                if lines[x][y] not in ["L", "F", "|"]
                print(lines[x][y], end="")
        print()
    print()

    # Group coordinates b/w F and 7, F and J, L and 7, L and J
    for key in loop_coords_dict:
        groups = []
        current_group = []
        values = loop_coords_dict[key]
        for i in range(len(values) - 1):
            current_group.append(values[i])
            pipe_sym_cur = lines[values[i][0]][values[i][1]]
            pipe_sym_next = lines[values[i + 1][0]][values[i + 1][1]]
            if pipe_sym_cur in (["F", "-", "L"]) and pipe_sym_next in (["-", "7", "J"]):
                pass
            else:
                groups.append(current_group)
                current_group = []
        current_group.append(values[-1])
        groups.append(current_group)
        loop_coords_dict[key] = groups

    print()
    print("loop_coords_dict with groups:")
    for key, value in loop_coords_dict.items():
        print(key, value)
    print()

    area_coords = []
    for x in range(x_min, x_max + 1):
        # print(x, end=" ")
        for y in range(y_min, y_max + 1):
            # Check if [x, y] is part of the loop (included into the area)
            is_in_loop = False
            for group in loop_coords_dict[x]:
                if [x, y] in group:
                    area_coords.append([x, y])
                    is_in_loop = True
                    break
            
            # Else check using Ray casting algorithm
            if not is_in_loop:
                ray_coords = get_shortest_ray([x, y], [x_min, y_min], [
                                            x_max, y_max])

                intersection_cnt = 0
                for group in loop_coords_dict[x]:
                    if group[-1][1] < ray_coords[0][1]:
                        continue 
                    for ray_coord in ray_coords:
                        if ray_coord in group:
                            # intersection_cnt += 1
                            if len(group) == 1:
                                intersection_cnt += 1
                            else:
                                intersection_cnt += 1
                            break

                if intersection_cnt % 2 != 0:
                    area_coords.append([x, y])

    print()
    print("Area coordinates:", area_coords)

    print("\nLength of the loop:", len(loop_coords))
    print("Tiles in the area:", len(area_coords))
    enclosed_tiles_cnt = len(area_coords) - len(loop_coords)

    print("\nEnclosed tiles count:", enclosed_tiles_cnt) # 593 is too high


def get_starting_pos(input_list: list, start_char: str):
    for sublist in input_list:
        for element in sublist:
            if element == start_char:
                return [input_list.index(sublist), sublist.index(element)]
    return None


def get_first_step_coord(input_list: list, starting_pos: list):
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


def get_shortest_ray(cur_coord: list, min_coord: list, max_coord: list):
    shortest_ray = []

    dist_left = abs(cur_coord[1] - min_coord[1])
    dist_right = abs(max_coord[1] - cur_coord[1])

    if dist_left <= dist_right:
        for y in range(min_coord[1], cur_coord[1] + 1):
            shortest_ray.append([cur_coord[0], y])
    else:
        for y in range(cur_coord[1], max_coord[1] + 1):
            shortest_ray.append([cur_coord[0], y])

    return shortest_ray


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Execution started:", time_start)

    main()

    time_end = datetime.datetime.now()
    print("Execution ended:", time_end)
    print("Duration:", time_end - time_start)
