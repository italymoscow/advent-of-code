"""
Solution to the Day 13, Part 1 and 2.

Returns:
    PART 1. The sum of the indices of the pairs in the right order: 5252
    PART 2. The product of the indices of the additional divider packets: 20592
"""

import logging
import os


def part_1():
    """
    Solution to Part 1. Prints the result.
    """
    input_list = parse_input(input_strings)
    logging.debug("input_list: " + str(input_list))
    results = compare_pairs_in_list(input_list)
    sum_of_right_indices = 0
    for key, val in results.items():
        if val == "right":
            sum_of_right_indices += key
    print("PART 1. The sum of the indices of the pairs in the right order: "
          + str(sum_of_right_indices))


def part_2():
    """
    Solution to Part 2. Prints the result.
    """

    input_list = parse_input(input_strings)

    flat_list = [item for sublist in input_list for item in sublist]
    flat_list.append([[2]])
    flat_list.append([[6]])
    logging.info("Input list with divider packets, unsorted: " + str(flat_list))
    flat_list_sorted = sort_flat_list(flat_list)

    product = (flat_list_sorted.index([[2]]) + 1) * (flat_list_sorted.index([[6]]) + 1)

    print("PART 2. The product of the indices of the additional divider packets: "
          + str(product))


def sort_flat_list(flat_list: list):
    """
    Return flat list "in the right order"
    """
    n = len(flat_list)

    # Traverse through all list elements
    for i in range(n):
        # Traverse the list from 0 to n-i-1
        # (The last element will already be in place after first pass, so no need to re-check)
        for j in range(0, n - i - 1):

            # Swap if current element is greater than next
            if compare_lists(flat_list[j], flat_list[j + 1]) == "wrong":
                # if flat_list[j] > flat_list[j + 1]:
                flat_list[j], flat_list[j + 1] = flat_list[j + 1], flat_list[j]

    return flat_list


def compare_lists(list_1: list, list_2: list):
    """
    Returns "right" if lists are in the "right order" (see README.md),
    "wrong" if lists are in a "wrong order" and
    "equal" if lists are identical
    """
    i = 0
    while i < len(list_1):
        if i < len(list_2):
            # Both values are lists
            if type(list_1[i]) == list and type(list_2[i]) == list:
                result = compare_lists(list_1[i], list_2[i])
                if result != "equal":
                    return result

            # Mixed types (left is list)
            elif type(list_1[i]) == list:
                result = compare_lists(list_1[i], [list_2[i]])
                if result != "equal":
                    return result

            # Mixed types (right is list)
            elif type(list_2[i]) == list:
                result = compare_lists([list_1[i]], list_2[i])
                if result != "equal":
                    return result

            # Both values are integers, left is greater
            elif list_1[i] > list_2[i]:
                return "wrong"

            # Both values are integers, right is greater
            elif list_1[i] < list_2[i]:
                return "right"

            # Continue checking the next part of the input
            i += 1

        else:
            return "wrong"  # The right list runs out of items first

    # The left list runs out of items first
    if len(list_2) > len(list_1):
        return "right"

    return "equal"


def compare_pairs_in_list(input_list):
    """
    Return a dict with pair index and result of the comparison:
    "right", "wrong", "equal"
    """
    results = {}
    for pair in input_list:
        index = input_list.index(pair) + 1
        result = compare_lists(pair[0], pair[1])
        results[index] = result

    logging.info("Results: " + str(results))

    return results


def parse_string_into_list(input_string: str):
    matching_brackets = find_matching_brackets(input_string)
    logging.debug("Matching brackets: " + str(matching_brackets))
    split_input_string = []

    if len(matching_brackets) > 1:
        first_level_brackets = find_first_level_brackets(matching_brackets)
        last_position = 0
        for first_level_bracket in first_level_brackets:
            # Before the list
            if first_level_bracket != last_position + 1:
                for item in input_string[1:first_level_bracket].rstrip(",").split(","):
                    if item.isnumeric():
                        split_input_string.append(int(item))

            # The list
            bracket_open_pos = first_level_bracket
            bracket_close_pos = first_level_brackets[first_level_bracket]
            inner_list = parse_string_into_list(input_string[bracket_open_pos:bracket_close_pos + 1])
            split_input_string.append(inner_list)
            last_position = bracket_close_pos + 1

        # After all lists
        last_first_level_bracket_close_pos = list(first_level_brackets.values())[-1]
        if last_first_level_bracket_close_pos != len(input_string) - 2:
            for item in input_string[last_position:-1].lstrip(",").split(","):
                if item.isnumeric():
                    split_input_string.append(int(item))
                elif item == ",":
                    continue
                else:
                    split_input_string.append(list(()))

        logging.debug("split_input_string: " + str(split_input_string))

    elif len(matching_brackets) == 1:
        input_string = input_string.lstrip("[").rstrip("]")
        split_input_string = input_string.split(",")
        try:
            split_input_string = list(map(int, split_input_string))
        except ValueError:
            if split_input_string == [""]:
                split_input_string = list(())

    return split_input_string


def find_matching_brackets(input_string: str):
    """
    Return a dict where keys are indices of the opening brackets
    and values are the indices of the corresponding closing brackets.
    """

    indices_open = []  # indices of opening brackets
    matching_brackets = {}

    for index, value in enumerate(input_string):
        if value == "[":
            indices_open.append(index)
            continue
        if value == "]":
            try:
                matching_brackets[indices_open.pop()] = index
            except IndexError:
                logging.exception("Too many closing brackets")
                exit()

    if indices_open:  # check if stack is empty afterwards
        logging.exception("Too many opening brackets")

    return dict(sorted(matching_brackets.items()))


def find_first_level_brackets(matching_brackets: dict):
    """
    Return dict containing indices of the brackets of the first level (children).
    Key - index of the opening bracket, Value - index of the closing bracket
    Return an empty dict if no children exist.
    Examples:
        Input = {0: 26, 3: 21, 6: 20, 9: 19, 12: 18}
        Output = {3: 21}, where
        {0: 26} is the parent, {3: 21} is the only child, {6: 20, 9: 19, 12: 18} - grandchildren and their descendants
    """
    input_dict = matching_brackets.copy()
    first_level_brackets = {}
    if len(input_dict) == 1:
        first_level_brackets = {}
    elif len(input_dict) == 2:
        input_dict.pop(0)
        first_level_brackets = input_dict
    elif len(input_dict) > 2:
        input_dict.pop(0)

        # first element will always have first level list
        first_level_brackets[list(input_dict.keys())[0]] = list(input_dict.values())[0]

        # Loop through the rest of the elements
        for i in range(1, len(input_dict)):
            key = list(input_dict.keys())[i]
            value = list(input_dict.values())[i]
            prev_value = list(first_level_brackets.values())[-1]
            if key > prev_value:
                first_level_brackets[key] = value

    return first_level_brackets


def parse_input(input_strings):
    """
    Return a list containing all the pairs from the input:
    """
    pairs = []
    i = 0
    first_in_pair = ""
    while i < len(input_strings):
        # "[...]"
        if input_strings[i].startswith("["):
            if type(first_in_pair) == str:
                first_in_pair = parse_string_into_list(
                    input_strings[i].rstrip())
                logging.debug(str(first_in_pair))
            else:
                second_in_pair = parse_string_into_list(
                    input_strings[i].rstrip())
                logging.debug(str(second_in_pair))
                pairs.append([first_in_pair, second_in_pair])
        else:  # Empty line
            first_in_pair = ""
        i += 1
    return pairs


def read_input(file_name: str):
    """
    Return a list containing all the lines of the input file.
    Parameters:
        file_name, str, name of the input file
    """
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\" + file_name, "r")
    lines = input_file.readlines()
    input_file.close()
    return lines


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logging.disable(logging.CRITICAL)
    input_strings = read_input("day_13_input.txt")
    part_1()
    part_2()
