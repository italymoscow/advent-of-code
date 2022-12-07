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
    Creates dict file_structure, where
        key: string dir_path,
        value: list [children_files_size, children_dirs_size, dir_size]
    """
    cur_dir = ["/"]
    for input_string in input_strings:
        # Change dir
        if input_string.startswith("$ cd"):
            cur_dir = get_current_dir(input_string, cur_dir)
            cur_dir_str = "/".join(cur_dir).replace("//", "/")
            # Add current directory into file_structure if new
            if not cur_dir_str in file_structure:
                file_structure[cur_dir_str] = [0, 0, 0]
            continue

        # Process file size and name
        if input_string[0].isdigit():
            file_size = int(input_string.split(" ")[0])
            cur_dir_info = file_structure[cur_dir_str]
            cur_dir_info[0] += file_size  # children_files_size
            cur_dir_info[2] += file_size  # total_dir_size
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
        cur_dir_info = file_structure[cur_dir_str]
        cur_dir_info[1] += file_size  # children_dirs_size
        cur_dir_info[2] += file_size  # total_dir_size
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
    tot_size = 0
    # print("\n")
    # print("Directories with a total size of at most 100000:")
    for dir_path, dir_info in file_structure.items():
        dir_size = dir_info[2]
        if dir_size <= 100000:
            # print(dir_path, dir_size)
            tot_size += dir_size

    print("\n")
    print("PART 1. Total size of folders less than 100 Kb:", tot_size)


def part_2():
    """
    Solution to Part 2. Prints the result.
    """
    root_dir_size = file_structure["/"][2]  # 43636666
    total_disk_space = 70000000
    required_unused_space = 30000000
    unused_space = total_disk_space - root_dir_size  # 26363334
    space_to_free_up = required_unused_space - unused_space  # 3636666

    potential_dirs_to_delete = {}
    for dir_path, dir_info in file_structure.items():
        dir_size = dir_info[2]
        if dir_size >= space_to_free_up:
            potential_dirs_to_delete[dir_path] = dir_size
    potential_dirs_to_delete_sorted = dict(
        sorted(potential_dirs_to_delete.items(), key=lambda item: item[1]))
    # print("Potential directories to delete:")
    # pprint.pprint(potential_dirs_to_delete_sorted)
    folder_to_delete = list(potential_dirs_to_delete_sorted)[0]
    freed_up_space = potential_dirs_to_delete_sorted[folder_to_delete]

    print("PART 2. Folder to delete: " +
          folder_to_delete + ", freed up space:", freed_up_space)


# Extract initial stack information and movement instructions from input file
cur_path = os.path.dirname(os.path.abspath(__file__))
input_file = open(cur_path + "\\07_input.txt", "r")
input_strings = input_file.readlines()
input_file.close()

file_structure = {}
file_structure.setdefault("/", [0, 0, 0])

create_file_structure()
print("File structure: ")
print("dir_path: [children_files_size, children_dirs_size, dir_size]")
pprint.pprint(file_structure)


if __name__ == "__main__":
    part_1()
    part_2()
