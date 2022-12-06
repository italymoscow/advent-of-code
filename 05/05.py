'''
Solution to the Day 5, Part 1 and 2.

Task, Part 1: 
    After the rearrangement procedure completes, what crate ends up
    on top of each stack?

Task, Part 2:
    Before the rearrangement process finishes, update your simulation so 
    that the Elves know where they should stand to be ready to unload 
    the final supplies.

Returns:
    PART 1: Top crates in the stacks:
    VGBBJCRMN

    PART 2: Top crates in the stacks:
    LBBVJBRMH
'''


import os
import copy  # to create a deep copy of the stacks_dict


def create_stacks_dict(stacks_info: list):
    '''
    Returns a dict holding the initial stack:
        {
            "first_stack_name": ["bottom_crate", ..., "top_crate"],
            ...
            "last_stack_name": ["bottom_crate", ..., "top_crate"]}
        }
    For example:
        {
            '1': ['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q'],
            ...,
            '9': ['Q', 'N', 'B', 'G', 'L', 'S', 'P', 'H']
        }
    '''
    stacks_dict = {}

    stack_names_str = " ".join(stacks_info[-1].strip().split())
    stack_names = stack_names_str.split(" ")
    stacks_info.pop()
    stacks_info.reverse()

    for stack in stacks_info:
        stack = stack.strip().replace("[", "").replace("]", "")
        stack = stack.replace("    ", " 0")
        stack_list = stack.split(" ")
        i = 0
        for stack_name in stack_names:
            if stack_name in stacks_dict:
                if stack_list[i] != "0":
                    crates_in_stack = stacks_dict[stack_name]
                    crates_in_stack.append(stack_list[i])
            else:
                if stack_list[i] != 0:
                    crates_in_stack = [stack_list[i]]
                    stacks_dict[stack_name] = crates_in_stack
            i += 1

    return stacks_dict


def part_1(stacks_dict: dict):
    '''
    Solution to Part 1. Prints the result.
    '''
    for movement in movements:
        movement_instr = movement.strip().replace("move ", "").replace(
            " from", "").replace(" to", "").split(" ")
        crates_to_move = int(movement_instr[0])
        move_from = movement_instr[1]
        move_to = movement_instr[2]
        for i in range(0, crates_to_move):
            crate_to_move = stacks_dict[move_from][-1]
            crates_in_from_stack = stacks_dict[move_from]
            crates_in_from_stack.pop()
            crates_in_to_stack = stacks_dict[move_to]
            crates_in_to_stack.append(crate_to_move)

    print("PART 1: Top crates in the stacks:")
    for stacks in stacks_dict.values():
        print(stacks[-1], end="")


def part_2(stacks_dict: dict):
    '''
    Solution to Part 2. Prints the result.
    '''
    for movement in movements:
        movement_instr = movement.strip().replace("move ", "").replace(
            " from", "").replace(" to", "").split(" ")
        crates_to_move_count = int(movement_instr[0])
        move_from = movement_instr[1]
        move_to = movement_instr[2]

        crates_in_from_stack = stacks_dict[move_from]
        crates_to_move = crates_in_from_stack[-crates_to_move_count:]
        del crates_in_from_stack[-crates_to_move_count:]
        crates_in_to_stack = stacks_dict[move_to]
        crates_in_to_stack.extend(crates_to_move)

    print("PART 2: Top crates in the stacks:")
    for stacks in stacks_dict.values():
        print(stacks[-1], end="")


# Extract initial stack information and movement instructions from input file
cur_path = os.path.dirname(os.path.abspath(__file__))
input_file = open(cur_path + "\\05_input.txt", "r")
all_input_lines = input_file.readlines()
separator_line_index = all_input_lines.index("\n")
stacks_info = all_input_lines[:separator_line_index]
movements = all_input_lines[separator_line_index + 1:]
input_file.close()

# Create dict holding the initial stack:
#   {"stack_name": ["bottom_crate", ..., "top_crate"]}
stacks_dict = create_stacks_dict(stacks_info)

# Make a deep copy of the original stack_dict to be used for Part 2
stacks_dict_2 = copy.deepcopy(stacks_dict)


if __name__ == "__main__":
    part_1(stacks_dict)
    print("\n")
    part_2(stacks_dict_2)
