from os import path
from datetime import datetime


def main():

    # Read the input file
    cur_path = path.dirname(path.abspath(__file__))
    input_file = open(cur_path + "\\15_input.txt", "r")
    line = input_file.readline()
    input_file.close()

    steps = line.split(",")

    # boxes Will contain box number (0-255) and a list of lenses: {box_num: [[label, focal_power]]}
    boxes = {}
    # labels will contain labels and their focal power: {"label": focal_power}
    labels = {}

    for step in steps:
        parsed_step = parse_step(step)
        label = parsed_step[0]
        operation = parsed_step[1]
        foc_len = parsed_step[2]

        # Get box_num from labels if exists
        # Otherwise calculate it and insert into labels
        if label not in labels:
            box_num = get_hash(label)
            labels[label] = box_num
        else:
            box_num = labels[label]

        if box_num in boxes:
            lenses = boxes[box_num]
            if operation == "=":
                lense_found = False
                for i, lense in enumerate(lenses):
                    if label == lense[0]:
                        lenses[i] = [label, foc_len]
                        lense_found = True
                        break
                if not lense_found:
                    boxes[box_num].append([label, foc_len])

            else:
                for i, lense in enumerate(lenses):
                    lense_found = False
                    if label == lense[0]:
                        lenses.pop(i)
                        lense_found = True
                        break
        else:
            if operation == "=":
                boxes[box_num] = [[label, foc_len]]

    # Calculate total focal power
    tot_foc_pwr = 0
    for box, lenses in boxes.items():
        for i, lense in enumerate(lenses):
            foc_pwr = (int(box) + 1) * (i + 1) * int(lense[1])
            tot_foc_pwr += foc_pwr

    print("Total focal power:", tot_foc_pwr)


def parse_step(step: str):
    """
    Returns a list containing the label, operation and focal length of the step
    """

    if "-" in step:
        label = step.split("-")[0]
        operation = "-"
        foc_len = 0
    else:  # contains "="
        label = step.split("=")[0]
        operation = "="
        foc_len = step.split("=")[1]

    return [label, operation, foc_len]


def get_hash(label: str):
    """
    Returns the hash value of the label
    """
    cur_val = 0
    chars = list(label)
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
