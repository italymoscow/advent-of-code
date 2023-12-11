import os
import datetime


def main():

    # Read the input file
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\08_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()


    directions = get_directions(lines[0])
    nodes_instructions = get_node_instructions(lines[2:])

    # Define starting nodes
    starting_nodes = []
    for key in nodes_instructions.keys():
        if key[-1] == "A":
            starting_nodes.append(key)

    steps_cnt = 0
    z_nodes_cnt = 0
    while z_nodes_cnt != len(starting_nodes):
        for direction in directions:
            steps_cnt += 1
            z_nodes_cnt = 0
            for index, starting_node in enumerate(starting_nodes):
                cur_node = nodes_instructions[starting_node][direction]
                starting_nodes[index] = cur_node
                if cur_node[-1] == "Z":
                    z_nodes_cnt += 1
            
            if z_nodes_cnt == len(starting_nodes):
                break
        print(steps_cnt)

    print("Steps required: ", steps_cnt)


def get_directions(line: str):
    directions = line.rstrip()
    directions = directions.replace("L", "0").replace("R", "1")
    directions = list(map(int, list(directions)))
    
    return directions


def get_node_instructions(lines: list):
    nodes_instructions = {}
    for line in lines:
        line = line.rstrip()
        node_instructions = line.split(" = ")
        node = node_instructions[0]
        instruction = node_instructions[1][1:-1].split(", ")
        nodes_instructions[node] = instruction
    
    return nodes_instructions


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
