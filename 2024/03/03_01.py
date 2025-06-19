import os
import time
import re


def main():
    cur_path = os.path.dirname(os.path.abspath(__file__))
    with open(cur_path + "\\03_input.txt", "r") as file:
        text = file.read()

    time_start = time.time()
    pattern = r"mul\((\d+),(\d+)\)"
    muls = re.findall(pattern, text)
    
    result = sum(int(a) * int(b) for a, b in muls)

    time_total = time.time() - time_start
    print("Result: ", result, "\nTime: ", time_total, " sec")


if __name__ == "__main__":
    main()