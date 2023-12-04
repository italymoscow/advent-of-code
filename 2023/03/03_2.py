import os
import datetime


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\03_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

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
        
        # Skip header and footer lines
        if line_index == 0 or line_index == LINES_LEN - 1:
            continue
        
        # Parse all lines and find coordinates of all asterisks
        for char_index, char in enumerate(line):
            if char == "*":
                asterisk_coords.append([line_index, char_index])

    # Find adjacent cells for each asterisk:
    for asterisk_coord in asterisk_coords:
        numbers = [] # store found numbers in this list

        # Find adjacent coordinates around asterisk
        adjacent_coords = []
        asterisk_x = asterisk_coord[0]
        asterisk_y = asterisk_coord[1]
        
        # add adjacent coordinates above
        for y in range(asterisk_y - 1, asterisk_y + 2):
            adjacent_coords.append([asterisk_x - 1, y])
        
        # add adjacent coordinates on the sides
        adjacent_coords.append([asterisk_x, asterisk_y - 1])
        adjacent_coords.append([asterisk_x, asterisk_y + 1])
        
        # add adjacent coordinates below
        for y in range(asterisk_y - 1, asterisk_y + 2):
            adjacent_coords.append([asterisk_x + 1, y])

        coord_index = 0
        while coord_index < len(adjacent_coords) and len(numbers) < 3:
            adjacent_coord = adjacent_coords[coord_index]
            x = adjacent_coord[0]
            y = adjacent_coord[1]
            char = lines[x][y]
            if char.isdigit():
                number_str = char
                # check on the left
                while y > 0 and lines[x][y - 1].isdigit():
                    y -= 1
                    number_str = lines[x][y] + number_str
                # check on the right
                y = adjacent_coord[1]
                while y < LINE_LEN and lines[x][y + 1].isdigit():
                    y += 1
                    if y <= asterisk_y + 1:
                        coord_index += 1
                    number_str = number_str + lines[x][y]
                number = int(number_str)
                numbers.append(number)
            coord_index += 1
        
        # Calculate the gear ratio
        if len(numbers) == 2:
            gear_ratio = numbers[0] * numbers[1]
            sum_gear_ratios += gear_ratio
        
    print("Sum of gear ratios:", sum_gear_ratios)


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Start:", time_start)
    main()
    time_end = datetime.datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
