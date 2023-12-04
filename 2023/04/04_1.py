import os
import datetime


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\04_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    points_sum = 0

    for line in lines:
        line = line.rstrip()
        
        # Delete start of the line until ": "
        line = line[line.index(": ") + 2:]
        line = line.replace("  ", " ")
        winning_nums = line.split(" | ")[0].split()
        own_nums = line.split(" | ")[1].split()

        points = 0

        for own_num in own_nums:
            if own_num in winning_nums:
                if points == 0:
                    points = 1
                else:
                    points = points * 2
        
        points_sum += points
        
    print("Sum of points:", points_sum)


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Start:", time_start)
    
    main()
    
    time_end = datetime.datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
