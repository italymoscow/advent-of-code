'''
Solution to the Day 1: Trebuchet?!, Part 2.

Returns:
The sum of all of the calibration values
'''


import datetime
import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\01_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Dictionary of numbers in words
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    # Get min length of the keys in the numbers dictionary
    min_key_len = len(min(numbers.keys(), key=len))

    output_file = open(cur_path + "\\01_02_output.txt", "a")

    sum_of_calibrations = 0

    for line in lines:
        line = line.rstrip()

        # Check if the line both starts and ends with a digit
        if line[0].isdigit() and line[-1].isdigit():
            calibration = int(line[0] + line[-1])
            sum_of_calibrations += calibration
            
            # Write line to file
            output_file.write(str(calibration) + ": " + line + " (unchanged) \n")
            
            continue

        # Check if line starts with any of the keys in the numbers dictionary
        line_orig = line
        line_orig_len = len(line_orig)
        pos = 0
        while pos <= line_orig_len and line_orig_len - pos >= min_key_len :
            substring = line_orig[pos:]
            for key in numbers.keys():
                if substring.startswith(key):
                    # replace only the first occurrence of the key with the value in the numbers dictionary
                    line = line.replace(key, str(numbers[key]), 1)
                    pos += len(key) - 1
                    break
            pos += 1

        # Find the first digit in the line
        for char in line:
            if char.isdigit():
                first_digit_char = char
                break

        # Find the last digit in the line
        for char in reversed(line):
            if char.isdigit():
                last_digit_char = char
                break

        # Join the first and last digits to form the calibration value, and convert to int
        calibration = int(first_digit_char + last_digit_char)

        # Write line to file
        output_file.write(str(calibration) + ": " + line + " (" + line_orig + ")\n")

        sum_of_calibrations += calibration

    print(sum_of_calibrations) # 54878

    output_file.close()


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Start:", time_start)
    main()
    time_end = datetime.datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
