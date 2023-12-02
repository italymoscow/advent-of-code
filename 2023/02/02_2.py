import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\02_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    sum_of_sets_power = 0

    for line in lines:
        line = line.rstrip()

        # Delete start of the line until ": "
        line = line[line.index(": ") + 2:]

        game_results = []

        game_sets = line.split("; ")
        for game_set in game_sets:  # E.g. 3 blue, 4 red
            set_outcomes = game_set.split(", ")

            # [0] red, [1] green, [2] blue
            cubes_in_set_outcome = [0, 0, 0]
            for set_outcome in set_outcomes:  # E.g. 3 blue
                set_outcome = set_outcome.rstrip()

                cubes = int(set_outcome.split()[0])
                color = set_outcome.split()[1]

                if color == "red":
                    cubes_in_set_outcome[0] = cubes
                elif color == "green":
                    cubes_in_set_outcome[1] = cubes
                elif color == "blue":
                    cubes_in_set_outcome[2] = cubes

            game_results.append(cubes_in_set_outcome)

        cubes_fewest_numbers = [0, 0, 0]  # red, green, blue

        for index in range(3):
            max_index_values = []
            for item in game_results:
                index_value = item[index]
                max_index_values.append(index_value)

            max_value = max(max_index_values)
            cubes_fewest_numbers[index] = max_value

        power = 1

        for cubes in cubes_fewest_numbers:
            power *= cubes

        sum_of_sets_power += power

    print(sum_of_sets_power)


if __name__ == "__main__":
    main()
