import os
import time
import re


def get_enabled_positions(do_positions: list, dont_positions: list):
    """
    Retrieves the positions that are enabled

    Args:
        do_positions (list or dict): The input data containing do-positions.
        dont_positions (list or dict): The input data containing dont-positions.

    Returns:
        list: A list of tuples - enabled positions based on the input data.
    """
    i = 0
    enabled_positions = []
    while i < dont_positions[-1]:
        for value in do_positions:
            if value >= i:
                do_start = value
                i = value
                break
        for value in dont_positions:
            if value >= i:
                do_stop = value
                i = value
                break
        enabled_positions.append((do_start, do_stop))

    return enabled_positions


def main():
    cur_path = os.path.dirname(os.path.abspath(__file__))
    with open(cur_path + "\\03_input.txt", "r") as file:
        text = file.read()

    time_start = time.time()
    pattern = r"mul\((\d+),(\d+)\)"
    muls = re.findall(pattern, text)
    muls = [(int(a), int(b)) for a, b in muls]

    matches = re.finditer(pattern, text)
    mul_positions = [(match.start()) for match in matches]

    muls_with_pos = list(zip(muls, mul_positions))

    pattern = r"do\(\)"
    matches = re.finditer(pattern, text)
    do_positions = [(match.start()) for match in matches]
    do_positions.insert(0, 0)

    pattern = r"don't\(\)"
    matches = re.finditer(pattern, text)
    dont_positions = [(match.start()) for match in matches]
    if dont_positions[-1] < do_positions[-1]:
        dont_positions.append(len(text))

    enabled_positions = get_enabled_positions(do_positions, dont_positions)

    result = 0
    for enabled_position in enabled_positions:
        for mul_with_pos in muls_with_pos:
            mul_pos = mul_with_pos[1]
            if mul_pos >= enabled_position[0] and mul_pos < enabled_position[1]:
                mul = mul_with_pos[0]
                result += mul[0] * mul[1]

    time_total = time.time() - time_start
    print("Result: ", result, "\nTime: ", time_total, " sec")


if __name__ == "__main__":
    main()
