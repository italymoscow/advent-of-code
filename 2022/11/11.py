"""
Solution to the Day 11, Part 1 and 2.

Returns:
    PART 1. The level of monkey business: 120056
    PART 2. The level of monkey business: 21816744824
"""

import logging
import os


def part_1():
    """
    Solution to Part 1. Prints the result.
    """
    monkeys = parse_input()
    monkeys_inspections = {}
    for monkey in monkeys:
        monkeys_inspections[monkey] = 0

    for round in range(1, 21):
        logging.debug("Round: " + str(round))
        for key in monkeys:
            items = monkeys[key][0]
            operation = monkeys[key][1][0]
            divisor = int(monkeys[key][2])
            test_result_true = monkeys[key][3][0]
            test_result_false = monkeys[key][3][1]

            # Calculate worry level before the monkey gets bored
            while items:
                item = items[0]
                operand = monkeys[key][1][1]
                if operand == "old":
                    operand = item
                match operation:
                    case "+":
                        worry_level = item + int(operand)
                    case "-":
                        worry_level = item - int(operand)
                    case "*":
                        worry_level = item * int(operand)
                    case "/":
                        worry_level = item / int(operand)
                    case _:
                        logging.critical("Unsupported operation " + operation)
                        exit()

                # Monkey gets bored:
                worry_level //= 3

                # Test
                if worry_level % divisor == 0:
                    monkeys[test_result_true][0].append(worry_level)
                else:
                    monkeys[test_result_false][0].append(worry_level)
                monkeys_inspections[key] += 1
                items.pop(0)

        logging.debug("Monkeys:\n" + str(monkeys))
        logging.debug("Monkey inspections: \n" + str(monkeys_inspections))

    # Get the product of the top 2 inspection counts
    sorted_inspections = sorted(monkeys_inspections.values())
    business_level = sorted_inspections[-2] * sorted_inspections[-1]

    print("PART 1. The level of monkey business:", business_level)


def part_2():
    """
    Solution to Part 2. Prints the result.
    The same solution as for Part 1, but instead of dividing the worry level by 3
    we need to use the common divisor for test of which next monkey gets the item.
    """
    # monkeys is a dict that will store the items and operations for each monkey:
    # {monkey:[[items], [operation, operand], divisor, [true_result, false_result]]
    monkeys = parse_input()

    # monkeys_inspections is a dict that will store the level of business for each monkey:
    # {monkey: business_level}
    monkeys_inspections = {}
    for monkey in monkeys:
        monkeys_inspections[monkey] = 0

    # Get common_divisor:
    common_divisor = 1
    for val in monkeys.values():
        common_divisor *= val[2]  # divisor of each monkey

    # Loop for 10000 rounds
    for round in range(1, 10001):
        logging.debug("Round: " + str(round))
        for monkey in monkeys:
            items = monkeys[monkey][0]
            operation = monkeys[monkey][1][0]
            divisor = int(monkeys[monkey][2])
            test_result_true = monkeys[monkey][3][0]
            test_result_false = monkeys[monkey][3][1]

            # Calculate new worry level of the item and pass the item
            while items:
                item = items[0] % common_divisor
                operand = monkeys[monkey][1][1]
                if operand == "old":
                    operand = item
                match operation:
                    case "+":
                        worry_level = item + int(operand)
                    case "-":
                        worry_level = item - int(operand)
                    case "*":
                        worry_level = item * int(operand)
                    case "/":
                        worry_level = item / int(operand)
                    case _:
                        logging.critical("Unsupported operation " + operation)
                        exit()

                # Test and pass the item to another monkey
                if worry_level % divisor == 0:
                    monkeys[test_result_true][0].append(worry_level)
                else:
                    monkeys[test_result_false][0].append(worry_level)
                items.pop(0)

                monkeys_inspections[monkey] += 1

        # logging.debug("Monkeys:\n" + str(monkeys))
        logging.debug(str(monkeys_inspections))

    # Get the product of the top 2 inspection counts
    sorted_inspections = sorted(monkeys_inspections.values())
    business_level = sorted_inspections[-2] * sorted_inspections[-1]

    print("PART 2. The level of monkey business:", business_level)


def parse_input():
    """
    Return a dict holding the input data:
    {monkey:[[items], operation, divisor, [true_result, false_result]],
    e.g. {0: [[79, 98], ["*", "19"], 23, [2, 3]]}
    That is:
        Monkey 0 has items with worry level 79 and 98, 
        operation = old * 19
        test = divisible by 23
        test_result = if true - throw to Monkey 2, else to Monkey 3
    """
    monkey = "0"  # Default
    monkeys = {}
    for input_string in input_strings:

        # "Monkey X:"
        if input_string.startswith("M"):
            monkey = input_string.rstrip(":\n").split()[1]  # current monkey
            monkeys[monkey] = [[0, 0], ["", 0], "", [0, 0]]

        # "  Starting items:"
        elif input_string.startswith("  S"):
            items = input_string.rstrip().replace("  Starting items: ", "").split(", ")
            # Convert all items to int (worry levels are int)
            items = list(map(int, items))
            monkeys[monkey][0] = items

        # "  Operation: new = old [sign] X:"
        elif input_string.startswith("  O"):
            operation = input_string.rstrip().replace(
                "  Operation: new = old ", "").split()
            monkeys[monkey][1] = operation

        # "  Test: divisible by X:"
        elif input_string.startswith("  T"):
            divisor = int(input_string.rstrip().replace(
                "Test: divisible by ", ""))
            monkeys[monkey][2] = divisor

        # "    If true: throw to monkey X"
        elif input_string.startswith("    If t"):
            to_monkey = input_string.rstrip().replace(
                "    If true: throw to monkey ", "")
            monkeys[monkey][3][0] = to_monkey

        # "    If false: throw to monkey X"
        elif input_string.startswith("    If f"):
            to_monkey = input_string.rstrip().replace(
                "    If false: throw to monkey ", "")
            monkeys[monkey][3][1] = to_monkey

    return monkeys


def read_input(file_name: str):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\" + file_name, "r")
    input_strings = input_file.readlines()
    input_file.close()
    return input_strings


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    logging.disable(logging.CRITICAL)
    input_strings = read_input("11_input.txt")
    part_1()
    part_2()
