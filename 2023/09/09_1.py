from itertools import pairwise
import os
import datetime


def main():

    # Read the input file
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\09_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Find the sum of predictions
    sum_predictions = 0
    for line in lines:
        # Make line into a sequence of integers
        sequence = list(map(int, line.split()))
        
        next_val = predict_next_in_sequence(sequence)
        sum_predictions += next_val
    
    print("Sum of predictions:", sum_predictions)


def predict_next_in_sequence(sequence: list):
    last = 0
    while sequence:
        last += sequence[-1]
        sequence = [b - a for a, b in pairwise(sequence)]

    return last


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
