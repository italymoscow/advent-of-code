"""
Solution to the Day 9, Part 1 and 2.

Returns:
    PART 1. Unique position of the tail of the rope: 6745
    PART 2. Unique position of the tail of the rope: 2793
"""

import logging
import os


def part_1():
    """
    Solution to Part 1. Prints the result.
    """
    head_position = [0, 0]
    tail_position = [0, 0]
    tail_positions = []
    tail_positions_unique_count = 0
    for input_string in input_strings:
        head_moves = get_moves(input_string)
        if head_moves[0] < 0:
            step = -1
        else:
            step = 1
        for head_move_x in range(0, head_moves[0], step):
            head_position[0] += step
            tail_position = move_tail(head_position, tail_position)
            if not tail_position in tail_positions:
                tail_positions.append(tail_position)
                tail_positions_unique_count += 1

        if head_moves[1] < 0:
            step = -1
        else:
            step = 1
        for head_move_y in range(0, head_moves[1], step):
            head_position[1] += step
            tail_position = move_tail(head_position, tail_position)
            if not tail_position in tail_positions:
                tail_positions.append(tail_position)
                tail_positions_unique_count += 1

    print("PART 1. Unique position of the tail of the rope:",
          tail_positions_unique_count)


def part_2():
    """
    Solution to Part 2. Prints the result. 
    Can also be used to solve part_1. Just change nodes_number to 2.
    part_1 seems to be faster to solve the task for nodes_number = 2,
    therefore leaving both. 
    """
    # Create dict(rope_nodes) of int(node):list(position), ex. {0: [0, 0]},
    # where keys are from 0 to 9 where 0 - header, 9 - tail
    nodes_number = 10
    rope_nodes = {}
    for i in range(nodes_number):
        rope_nodes[i] = [0, 0]

    head_position = rope_nodes[0]

    tail_positions = [[0, 0]]
    tail_position = rope_nodes[nodes_number - 1]

    for input_string in input_strings:
        head_moves = get_moves(input_string)
        logging.debug("------")
        logging.debug("\nHead moves" + str(head_moves))

        # Moving the head along the horizontal axis X
        if head_moves[0] < 0:
            step = -1
        else:
            step = 1
        for head_move_x in range(0, head_moves[0], step):
            head_position[0] += step
            logging.debug("")
            logging.debug("Node 0: " + str(head_position))
            rope_nodes = move_trailing_nodes(rope_nodes)
            if is_tail_position_new:
                if not tail_position in tail_positions:
                    tail_positions.append(tail_position.copy())

        # Moving the head along vertical axis Y
        if head_moves[1] < 0:
            step = -1
        else:
            step = 1
        for head_move_y in range(0, head_moves[1], step):
            head_position[1] += step
            logging.debug("")
            logging.debug("Node 0: " + str(head_position))
            rope_nodes = move_trailing_nodes(rope_nodes)
            if is_tail_position_new:
                if not tail_position in tail_positions:
                    tail_positions.append(tail_position.copy())

    print("PART 2. Unique position of the tail of the rope:",
          len(tail_positions))


def get_moves(input_string: str):
    input = input_string.rstrip().split(" ")
    direction = input[0]
    steps = int(input[1])
    match direction:
        case "U":
            moves = (0, steps)
        case "D":
            moves = (0, -steps)
        case "L":
            moves = (-steps, 0)
        case "R":
            moves = (steps, 0)
        case _:
            moves = (0, 0)
    return moves


def move_tail(head_position: list, tail_position: list):
    """
    Parameter head_position: current position of the head
    Parameter tail_position: current position of the tail
    Returns: new position of the tail as a list of coordinates [0, 0]
    """

    tail_position_new = tail_position.copy()
    head_position_x = head_position[0]
    head_position_y = head_position[1]
    tail_position_x = tail_position_new[0]
    tail_position_y = tail_position_new[1]

    abs_dif_x = abs(head_position_x - tail_position_x)
    abs_dif_y = abs(head_position_y - tail_position_y)
    if head_position_x > tail_position_x:
        step_x = 1
    else:
        step_x = -1

    if head_position_y > tail_position_y:
        step_y = 1
    else:
        step_y = -1

    if (abs_dif_x == 2 and abs_dif_y == 1) or (abs_dif_y == 2 and abs_dif_x == 1):
        tail_position_new[0] += step_x
        tail_position_new[1] += step_y
        # print("new tail pos: ", tail_position_new)
    elif abs_dif_x == 2:
        tail_position_new[0] += step_x
        # print("new tail pos: ", tail_position_new)
    elif abs_dif_y == 2:
        tail_position_new[1] += step_y
        # print("new tail pos: ", tail_position_new)

    return tail_position_new


def move_trailing_nodes(rope_nodes: dict):
    """
    Parameter head_position: current position of the head
    Returns: rope_nodes with updated positions of all trailing nodes
    """
    global is_tail_position_new
    is_tail_position_new = False

    for i in range(1, len(rope_nodes)):
        prev_node_position_x = rope_nodes[i - 1][0]
        prev_node_position_y = rope_nodes[i - 1][1]
        node = rope_nodes[i]
        node_position_x = node[0]
        node_position_y = node[1]

        abs_dif_x = abs(prev_node_position_x - node_position_x)
        abs_dif_y = abs(prev_node_position_y - node_position_y)
        if prev_node_position_x > node_position_x:
            step_x = 1
        else:
            step_x = -1

        if prev_node_position_y > node_position_y:
            step_y = 1
        else:
            step_y = -1

        if (abs_dif_x == 2 and abs_dif_y == 1) or (abs_dif_y == 2 and abs_dif_x == 1):
            node[0] += step_x
            node[1] += step_y
            logging.debug("Node " + str(i) + ": " + str(node))
            if i == len(rope_nodes) - 1:
                is_tail_position_new = True
        elif abs_dif_x == 2 and abs_dif_y == 2:
            node[0] += step_x
            node[1] += step_y
            logging.debug("Node " + str(i) + ": " + str(node))
            if i == len(rope_nodes) - 1:
                is_tail_position_new = True
        elif abs_dif_x == 2:
            node[0] += step_x
            logging.debug("Node " + str(i) + ": " + str(node))
            if i == len(rope_nodes) - 1:
                is_tail_position_new = True
        elif abs_dif_y == 2:
            node[1] += step_y
            logging.debug("Node " + str(i) + ": " + str(node))
            if i == len(rope_nodes) - 1:
                is_tail_position_new = True
        elif abs_dif_x < 2 and abs_dif_y < 2:
            logging.debug("Node " + str(i) + ": " + str(node))
            if i == len(rope_nodes) - 1:
                is_tail_position_new = True
        else:
            break # Do not process the remaining nodes. They won't be moved.

    return rope_nodes

def read_input(file_name):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\" + file_name, "r")
    input_strings = input_file.readlines()
    input_file.close()
    return input_strings


if __name__ == "__main__":
    is_tail_position_new = False
    
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    logging.disable(logging.CRITICAL)
    input_strings = read_input("09_input.txt")
    part_1()
    part_2()
