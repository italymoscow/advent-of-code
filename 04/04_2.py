'''
Solution to the Day 4: Camp Cleanup, Part 2.

Task: 
    In how many assignment pairs do the ranges overlap?

Returns:
    ...
    Does range(87, 89) overlaps with range(4, 89)? True
    Does range(21, 34) overlaps with range(20, 33)? True
    Total overlapping pairs: 917
'''


import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\04_input.txt", "r")
    assignment_pairs = input_file.readlines()
    input_file.close()

    overlapping_pairs_count = 0

    for assignment_pair in assignment_pairs:
        assignment_pair = assignment_pair.strip()
        assignment_pair_list = assignment_pair.split(",")

        assignment_1_list = assignment_pair_list[0].split("-")
        assignment_1_rng_start = int(assignment_1_list[0])
        assignment_1_rng_end = int(assignment_1_list[1]) + 1
        assignment_1_rng = range(assignment_1_rng_start, assignment_1_rng_end)

        assignment_2_list = assignment_pair_list[1].split("-")
        assignment_2_rng_start = int(assignment_2_list[0])
        assignment_2_rng_end = int(assignment_2_list[1]) + 1
        assignment_2_rng = range(assignment_2_rng_start, assignment_2_rng_end)

        if range_subset(assignment_1_rng, assignment_2_rng):
            overlapping_pairs_count += 1

    print("Total overlapping pairs: " + str(overlapping_pairs_count))


def range_subset(range1, range2):
    result_rng = range(max(range1[0], range2[0]),
                       min(range1[-1], range2[-1]) + 1)
    if result_rng:
        result = True
    else:
        result = False
    print("Does " + str(range1) + " overlaps with " +
          str(range2) + "? " + str(result))
    return result


if __name__ == "__main__":
    main()
