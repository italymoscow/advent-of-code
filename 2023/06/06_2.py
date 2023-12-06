import os
import datetime


def main():

    # Read the input file
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\06_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Parse input
    time_line = lines[0].replace("Time:", "")
    time_line = time_line.replace(" ", "")
    race_time = int(time_line)

    dist_line = lines[1].replace("Distance:", "")
    dist_line = dist_line.replace(" ", "")
    race_record = int(dist_line)

    # Find the error margin
    error_margin = 1
    race_wins_cnt = 0
    for press_time in range(1, race_time):
        speed = press_time
        movement_time = race_time - press_time
        distance = speed * movement_time
        if distance > race_record:
            race_wins_cnt += 1

    error_margin *= race_wins_cnt

    print("Error margin:", error_margin)


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)