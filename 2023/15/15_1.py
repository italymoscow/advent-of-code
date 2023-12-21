from os import path
from datetime import datetime


def main():

    # Read the input file
    cur_path = path.dirname(path.abspath(__file__))
    input_file = open(cur_path + "\\15_input.txt", "r")
    line = input_file.readline()
    input_file.close()

    steps = line.split(",")

    sum_of_hashes = 0
    for step in steps:
        step_hash = get_step_hash(step)
        sum_of_hashes += step_hash
    
    print("Sum of hashes:", sum_of_hashes)


def get_step_hash(step: str):
    cur_val = 0
    chars = list(step)
    for char in chars:
        cur_val += ord(char)
        cur_val *= 17
        cur_val %= 256
    
    return cur_val



if __name__ == "__main__":
    time_start = datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
