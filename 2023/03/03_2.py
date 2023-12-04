import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\03_input_test.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    numbers_coords = []
    asterisk_coords = []

    sum_gear_ratios = 0

    # Add "." to the beginning and the end of each line
    for i in range(len(lines)):
        lines[i] = "." + lines[i].rstrip() + "."
    
    LINE_LEN = len(lines[0])

    # Add header line of "."
    lines.insert(0, "." * LINE_LEN)
    # Add footer line of "."
    lines.append("." * LINE_LEN)

    LINES_LEN = len(lines)
    
    for line_index, line in enumerate(lines):
        
        if line_index == 0 or line_index == LINES_LEN - 1:
            continue

        for char_index, char in enumerate(line):
            if char == "*":
                asterisk_coords.append([line_index, char_index])
    
    # find numbers in current row, the row above and below
    for asterisk_coord in asterisk_coords:
        numbers_cnt = 0

        # Find adjacent coordinates around asterisk
        adjacent_coords = []
        coord_x = asterisk_coord[0]
        coord_y = asterisk_coord[1]
        # add row above and below
        for y in range(coord_y - 1, coord_y + 2):
            adjacent_coords.append([coord_x - 1, y])
            adjacent_coords.append([coord_x + 1, y])
        # add coordinates on the sides
        adjacent_coords.append([coord_x, coord_y - 1])
        adjacent_coords.append([coord_x, coord_y + 1])

        for adjacent_coord in adjacent_coords:
            


        # Check if any of the adjacent coordinates exists in symbol coordinates
        for adjacent_coord in adjacent_coords:
            if adjacent_coord in symbols_coords:
                sum_part_numbers += number
                break
        
    print(sum_part_numbers) # 494956 is too small


if __name__ == "__main__":
    main()
