import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\02_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    sum_of_poss_ids = 0
    game_id = 1

    for line in lines:
        line = line.rstrip()

        # Delete start of the line until ": "
        line = line[line.index(": ") + 2:]

        is_game_valid = True

        game_sets = line.split("; ")

        for game_set in game_sets:  # E.g. 3 blue, 4 red
            set_outcomes = game_set.split(", ")

            for set_outcome in set_outcomes:  # E.g. 3 blue
                set_outcome = set_outcome.rstrip()
                cubes = int(set_outcome.split()[0])
                color = set_outcome.split()[1]

                if color == "red":
                    if cubes > MAX_RED:
                        is_game_valid = False
                        break
                elif color == "green":
                    if cubes > MAX_GREEN:
                        is_game_valid = False
                        break
                elif color == "blue":
                    if cubes > MAX_BLUE:
                        is_game_valid = False
                        break

            if not is_game_valid:
                break

        if is_game_valid:
            sum_of_poss_ids += game_id

        game_id += 1

    print(sum_of_poss_ids)


if __name__ == "__main__":
    main()
