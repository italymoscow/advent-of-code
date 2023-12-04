import os
import datetime


def main():

    # Read input file contents into the list lines
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\04_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Set cards_nums, where key = card_id, value =
    #   [[winning_nums, own_nums], [winning_nums_copy1, own_nums_copy1]]
    cards_nums = {}

    # Set cards_matches where key = card_id, value = match_num_cnt
    cards_matches = {}

    # Create lists cards_nums and cards_matches from lines
    for line_index, line in enumerate(lines):
        line = lines[line_index].rstrip()

        # Delete start of the line until ": "
        line = line[line.index(": ") + 2:]
        line = line.replace("  ", " ")
        winning_nums = line.split(" | ")[0].split()
        own_nums = line.split(" | ")[1].split()

        cards_nums[line_index + 1] = [[winning_nums, own_nums]]
        cards_matches[line_index + 1] = -1  # match_num_cnt not yet calculated

    # Loop through the original card and all its copies
    for key, value in cards_nums.items():
        for card_item in value:
            match_num_cnt = cards_matches[key]

            if match_num_cnt == -1:  # not yet calculated
                # Find number of matches for the card item
                winning_nums = card_item[0]
                own_nums = card_item[1]
                match_num_cnt = 0
                for own_num in own_nums:
                    if own_num in winning_nums:
                        match_num_cnt += 1
                cards_matches[key] = match_num_cnt

            # Copy cards
            for i in range(key + 1, key + 1 + match_num_cnt):
                cards_nums[i].append(cards_nums[i][0])

    # Count all values in cards_nums
    tot_cards_cnt = sum(len(value) for value in cards_nums.values())

    print("Sum of points:", tot_cards_cnt)


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
