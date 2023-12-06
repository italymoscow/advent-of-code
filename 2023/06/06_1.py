import os
import datetime


def main():

    # Read the input file
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\06_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Parse input
    times_line = lines[0].replace("Time:", "")
    times_line = ' '.join(times_line.split())
    times = list(map(int, times_line.split()))

    dist_line = lines[1].replace("Distance:", "")
    dist_line = ' '.join(dist_line.split())
    distances = list(map(int, dist_line.split()))

    races = []
    for i in range(len(times)):
        races.append([times[i], distances[i]])

    # Find the error margin
    error_margin = 1
    for race in races:
        race_wins_cnt = 0
        race_time = race[0]
        race_record = race[1]
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