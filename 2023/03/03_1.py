import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\03_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    numbers_coords = []
    symbols_coords = []

    sum_part_numbers = 0

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

        pos_in_line = 0
        while pos_in_line < LINE_LEN:
            
            number_coords = []
            number_str = ""
            if line[pos_in_line].isdigit():
                while line[pos_in_line].isdigit():
                    number_coords.append([line_index, pos_in_line])
                    number_str += line[pos_in_line]
                    pos_in_line += 1
            
                number = int(number_str)
                numbers_coords.append([number, number_coords])
                pos_in_line -= 1
            
            elif line[pos_in_line] != ".":
                symbols_coords.append([line_index, pos_in_line])
            
            pos_in_line += 1

    for number_coords in numbers_coords:
        number = number_coords[0]
        coords = number_coords[1]
        adjacent_coords = []

        # Find min and max y coord of the number
        coord_x = coords[0][0]
        coords_y = []
        for coord in coords:
            coords_y.append(coord[1])
        coord_y_min = min(coords_y)
        coord_y_max = max(coords_y)
        
        # add row above and below
        for y in range(coord_y_min - 1, coord_y_max + 2):
            adjacent_coords.append([coord_x - 1, y])
            adjacent_coords.append([coord_x + 1, y])
        # add coordinates on the sides
        adjacent_coords.append([coord_x, coord_y_min - 1])
        adjacent_coords.append([coord_x, coord_y_max + 1])

        # Check if any of the adjacent coordinates exists in symbol coordinates
        for adjacent_coord in adjacent_coords:
            if adjacent_coord in symbols_coords:
                sum_part_numbers += number
                break
        
    print(sum_part_numbers) # 494956 is too small


if __name__ == "__main__":
    main()
