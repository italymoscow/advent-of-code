from os import path
from datetime import datetime
from itertools import combinations


def main():

    # Read the input file
    cur_path = path.dirname(path.abspath(__file__))
    input_file = open(cur_path + "\\12_input_test.txt", "r")
    records = input_file.readlines()
    input_file.close()

    # Parse input
    for index, record in enumerate(records):
        conditions = list(char for char in record.split()[0])
        sizes = list(map(int,
                         list(char for char in
                              record.rstrip().split()[1].split(","))))
        records[index] = [conditions, sizes]

    arrangements_cnt = 0
    for record in records:
        print(record)


if __name__ == "__main__":
    time_start = datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
