"""
Solution to the Day 7, Part 1 and 2.

Returns:
    PART 1. Total size of folders less than 100 Kb: 1297159
    PART 2. Folder to delete: /tchbjclg/bljmjwm/qlzg/ghllcw, freed up space: 3866390
"""


import os
import pprint


def create_file_structure():
    """
    Based on the contents of input_lines, creates dict file_structure, where
        key: string - dir_path,
        value: int - total_dir_size in bytes (includes all files recursively)
    """
    cur_dir = ["/"]
    for input_string in input_strings:
        # Change dir
        if input_string.startswith("$ cd"):
            cur_dir = get_current_dir(input_string, cur_dir)
            cur_dir_str = "/".join(cur_dir).replace("//", "/")
            # Add current directory into file_structure if new
            if not cur_dir_str in file_structure:
                file_structure[cur_dir_str] = 0
            continue

        # Process file size (starts with a digit)
        if input_string[0].isdigit():
            file_size = int(input_string.split(" ")[0])
            file_structure[cur_dir_str] += file_size
            update_size_recursively(cur_dir, file_size)


def get_current_dir(input_str: str, cur_dir: list):
    """
    Returns current directory as a list based on the cd command in input_str
    """
    cd_to = input_str.replace("$ cd ", "").strip()
    if cd_to == "/":
        cur_dir = ["/"]
    elif cd_to == "..":
        cur_dir.pop()
    else:
        cur_dir.append(cd_to)
    return cur_dir


def get_parent_dir_str(cur_dir: list):
    """
    Returns parent dir as a string. Returns None if cur_dir is a root 
    """
    if len(cur_dir) > 1:
        parent_dir_str = "/".join(cur_dir[:-1]).replace("//", "/")
        return parent_dir_str
    else:
        return None


def update_size_recursively(cur_dir: list, file_size: int):
    """
    Updates children_dirs_size and total_dir_size in dict.values() recursively
    """
    parent_dir_str = get_parent_dir_str(cur_dir)
    while parent_dir_str:
        cur_dir_str = parent_dir_str
        file_structure[cur_dir_str] += file_size
        if cur_dir_str == "/":
            cur_dir_local = ["/"]
        else:
            cur_dir_local = cur_dir_str.split("/")
            cur_dir_local[0] = "/"
        parent_dir_str = get_parent_dir_str(cur_dir_local)


def part_1():
    """
    Solution to Part 1. Prints the result.
    """
    tot_size = sum(filter(lambda dir_size: dir_size <=
                   100000, file_structure.values()))
    
    print("PART 1. Total size of folders less than 100 Kb:", tot_size)


def part_2():
    """
    Solution to Part 2. Prints the result.
    """
    root_dir_size = file_structure["/"]  # 43636666
    total_disk_space = 70000000
    required_unused_space = 30000000
    unused_space = total_disk_space - root_dir_size  # 26363334
    space_to_free_up = required_unused_space - unused_space  # 3636666

    # Find min dir size to delete without
    # (enough for the solution)
    freed_up_space = min(filter(lambda dir_size: dir_size >=
                                space_to_free_up, file_structure.values()))

    folder_to_delete = list(filter(
        lambda item: item[1] == freed_up_space, file_structure.items()))[0][0]

    print("PART 2. Folder to delete: " +
          str(folder_to_delete) + ", freed up space:", freed_up_space)


cur_path = os.path.dirname(os.path.abspath(__file__))
input_file = open(cur_path + "\\07_input.txt", "r")
input_strings = input_file.readlines()
input_file.close()

file_structure = {}
file_structure.setdefault("/", 0)

create_file_structure()
print("File structure: ")
print("dir_path: dir_size")
pprint.pprint(file_structure)
print("\n")


if __name__ == "__main__":
    part_1()
    part_2()
