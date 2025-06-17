import os
import time


def main():
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\01_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    left_values = []
    right_values = []
    for line in lines:
        line = line.rstrip()
        values = line.split("   ")
        left_values.append(int(values[0]))
        right_values.append(int(values[1]))

    left_values.sort()
    right_values.sort()

    time_start = time.time()
    
    similarityScoreTotal = 0
    similarityScore = 0
    last_pos = 0
    
    for i in range(len(left_values)):
        left_value = left_values[i]
        counter = 0
        for j in range(last_pos, len(right_values)):
            right_value = right_values[j]
            if left_value < right_value:
                break
            if left_value == right_value:
                counter += 1
            last_pos = j
        similarityScore = left_value * counter
        similarityScoreTotal += similarityScore

    time_total = time.time() - time_start
    print("similarityScoreTotal: ", similarityScoreTotal, "\nTime taken:", time_total, "seconds")

if __name__ == "__main__":
    main()