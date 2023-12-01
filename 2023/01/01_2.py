'''
Solution to the Day 1: Trebuchet?!, Part 2.

Returns:
The sum of all of the calibration values
'''


import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\01_input_test.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Dictionary of numbers in words
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    # Get min length of the keys in the numbers dictionary
    max_key_len = len(min(numbers.keys(), key=len))

    sum_of_calibrations = 0

    for line in lines:
        line = line.rstrip()

        # Check if the line both starts and ends with a digit
        if line[0].isdigit() and line[-1].isdigit():
            calibration = int(line[0] + line[-1])
            sum_of_calibrations += calibration
            continue

        # Check if line starts with any of the keys in the numbers dictionary
        line_orig = line
        line_orig_len = len(line_orig)
        pos = 0
        while pos <= line_orig_len - max_key_len:
            substring = line_orig[pos:line_orig_len]
            for key in numbers.keys():
                if substring.startswith(key):
                    # replace the key with the value in the numbers dictionary only once
                    line = line.replace(key, str(numbers[key]), 1)
                    pos += len(key) - 1
                    break
            pos += 1

        # # Write line to file
        # output_file = open(cur_path + "\\01_output.txt", "a")
        # output_file.write(line + "\n")

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

        sum_of_calibrations += calibration

    print(sum_of_calibrations)


if __name__ == "__main__":
    main()
