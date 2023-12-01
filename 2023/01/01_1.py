'''
Solution to the Day 1: Trebuchet?!, Part 1.

Returns:
The sum of all of the calibration values
'''


import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\01_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    sum_of_calibrations = 0
    for line in lines:
        line = line.rstrip()
        # check if character is a digit
        for char in line:
            if char.isdigit():
                first_digit_char = char
                break
        
        # check if character is a digit in reverse order
        for char in reversed(line):
            if char.isdigit():
                last_digit_char = char
                break
        
        # Join the first and last digits to form the calibration value into a string
        calibration_value = int(first_digit_char + last_digit_char)

        sum_of_calibrations += calibration_value
    
    print(sum_of_calibrations)


if __name__ == "__main__":
    main()
