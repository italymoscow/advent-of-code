import os
import time


def get_lines():
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\02_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    return lines


def get_levels(report: str):
    report = report.rstrip()
    levels_str = report.split(" ")
    levels = [int(item) for item in levels_str]

    return levels


def is_safe(levels: list):

    # Check condition 2
    is_condition_2 = True
    for i in range(len(levels) - 1):
        dif = abs(levels[i] - levels[i + 1])
        if dif == 0 or dif > 3:
            is_condition_2 = False
            break

    if not is_condition_2:
        return is_condition_2

    # Check condition 1
    levels_asc = sorted(levels, reverse=False)
    if levels == levels_asc:
        return True
    else:
        levels_desc = sorted(levels, reverse=True)
        if levels == levels_desc:
            return True


def main():

    lines = get_lines()

    time_start = time.time()

    safe_reports = 0
    for report in lines:
        levels = get_levels(report)

        for i in range(len(levels)):
            if is_safe(levels):
                safe_reports += 1
                break
            else:
                shortened_levels = levels[:i] + levels[i + 1 :]
                if is_safe(shortened_levels):
                    safe_reports += 1
                    break
                else:
                    continue

    time_total = time.time() - time_start
    print("Safe reports: ", safe_reports, "\nTime: ", time_total, " sec")


if __name__ == "__main__":
    main()
