from os import path
from datetime import datetime


def main():

    # Read the input file
    cur_path = path.dirname(path.abspath(__file__))
    input_file = open(cur_path + "\\18_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Split lines by space
    for i, line in enumerate(lines):
        lines[i] = line.rstrip().split()

    trench_border_coords_dict = get_trench_border_coords_dict(lines)

    x_trench_min = min(list(map(int, trench_border_coords_dict.keys())))
    x_trench_max = max(list(map(int, trench_border_coords_dict.keys())))

    y_trench_max = max(
        [value[1] for sublist in trench_border_coords_dict.values() for value in sublist])

    y_trench_min = min(
        [value[1] for sublist in trench_border_coords_dict.values() for value in sublist])

    print("Top left coordinate:", (x_trench_min, y_trench_min))
    print("Bottom right coordinate:", (x_trench_max, y_trench_max))

    lagoon_coords = []

    for x in range(x_trench_min, x_trench_max + 1):
        print(x, end=" ")
        for y in range(y_trench_min, y_trench_max + 1):
            if [x, y] in trench_border_coords_dict[x]:
                lagoon_coords.append([x, y])
            else:
                ray_coords = get_shortest_ray([x, y], [x_trench_min, y_trench_min], [
                                              x_trench_max, y_trench_max])

                intersection_cnt = 0
                for ray_coord in ray_coords:
                    if ray_coord in trench_border_coords_dict[x]:
                        intersection_cnt += 1

                if intersection_cnt % 2 != 0:
                    lagoon_coords.append([x, y])

    print("\nCount of trench coords:",
          sum(len(value) for value in trench_border_coords_dict.values()))

    print("Count of lagoon coords:", len(lagoon_coords))

    # Top left coordinate: (-254, -38)
    # Bottom right coordinate: (13, 328)
    # 45426 (0:11:58.00) and 46002 (0:00:02.630552 - after introd. dict) are too low


def get_trench_border_coords_dict(lines: list):
    # trench_coords = []
    trench_coords_dict = {}
    coord_cur = [0, 0]
    for line in lines:
        x_cur = coord_cur[0]
        y_cur = coord_cur[1]

        direction = line[0]
        length = int(line[1])
        if direction == "R":
            for y_next in range(y_cur + 1, y_cur + 1 + length):
                if x_cur not in trench_coords_dict:
                    trench_coords_dict[x_cur] = []

                if not [x_cur, y_next] in trench_coords_dict[x_cur]:
                    trench_coords_dict[x_cur].append([x_cur, y_next])

            coord_cur = [x_cur, y_cur + length]

        elif direction == "L":
            for y_next in range(y_cur - 1, y_cur - 1 - length, -1):
                if x_cur not in trench_coords_dict:
                    trench_coords_dict[x_cur] = []

                if not [x_cur, y_next] in trench_coords_dict[x_cur]:
                    trench_coords_dict[x_cur].append([x_cur, y_next])

                # if not [x_cur, y_next] in trench_coords:
                #     trench_coords.append([x_cur, y_next])
                #     if x_cur not in trench_coords_dict:
                #         trench_coords_dict[x_cur] = []
                #     trench_coords_dict[x_cur].append([x_cur, y_next])
            coord_cur = [x_cur, y_cur - length]

        elif direction == "U":
            for x_next in range(x_cur - 1, x_cur - 1 - length, -1):
                if x_next not in trench_coords_dict:
                    trench_coords_dict[x_next] = []

                if not [x_next, y_cur] in trench_coords_dict[x_next]:
                    trench_coords_dict[x_next].append([x_next, y_cur])

                # if not [x_next, y_cur] in trench_coords:
                #     trench_coords.append([x_next, y_cur])
                #     if x_next not in trench_coords_dict:
                #         trench_coords_dict[x_next] = []
                #     trench_coords_dict[x_next].append([x_next, y_cur])
            coord_cur = [x_cur - length, y_cur]

        elif direction == "D":
            for x_next in range(x_cur + 1, x_cur + 1 + length):
                if x_next not in trench_coords_dict:
                    trench_coords_dict[x_next] = []

                if not [x_next, y_cur] in trench_coords_dict[x_next]:
                    trench_coords_dict[x_next].append([x_next, y_cur])

                # if not [x_next, y_cur] in trench_coords:
                #     trench_coords.append([x_next, y_cur])
                #     if x_next not in trench_coords_dict:
                #         trench_coords_dict[x_next] = []
                #     trench_coords_dict[x_next].append([x_next, y_cur])
            coord_cur = [x_cur + length, y_cur]
        else:
            pass

    return trench_coords_dict


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
    time_start = datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
