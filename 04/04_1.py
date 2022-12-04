'''
Solution to the Day 4: Camp Cleanup, Part 1.

Task: 
    In how many assignment pairs does one range fully contain the other?

Returns:
    ...
    range(87, 89) - range(4, 89) --> True
    range(21, 34) - range(20, 33) --> False
    range(20, 33) - range(21, 34) --> False
    Pairs with full overlap: 571
'''


import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\04_input.txt", "r")
    assignment_pairs = input_file.readlines()
    input_file.close()

    full_overlap_count = 0

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

        if range_subset(assignment_1_rng, assignment_2_rng) \
                or range_subset(assignment_2_rng, assignment_1_rng):
            full_overlap_count += 1

    print("Pairs with full overlap: " + str(full_overlap_count))


def range_subset(range1, range2):
    result = range1.start in range2 and range1[-1] in range2
    print(str(range1) + " - " + str(range2) + " --> " +
          str(result))
    return result


if __name__ == "__main__":
    main()
