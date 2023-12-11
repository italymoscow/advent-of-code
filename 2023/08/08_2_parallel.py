import multiprocessing
import os
import datetime

steps_cnt = 0
nodes_instructions = {}
directions = []

def main():

    # Read the input file
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\08_input_test.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    
    directions = get_directions(lines[0])
    
    global nodes_instructions
    nodes_instructions = get_node_instructions(lines[2:])

    # Define starting nodes
    global starting_nodes
    starting_nodes = []
    for key in nodes_instructions.keys():
        if key[-1] == "A":
            starting_nodes.append(key)
    print("Starting nodes: ", len(starting_nodes))

    global steps_cnt

    z_nodes_cnt = 0
    while z_nodes_cnt != len(starting_nodes):
        global direction
        for direction in directions:
            results = []
            steps_cnt += 1

            with multiprocessing.Pool(len(starting_nodes)) as pool:
                results = pool.map(make_step, enumerate(starting_nodes))
            
            z_nodes_cnt = sum(results)
            
            if z_nodes_cnt == len(starting_nodes):
                break
            
            print("Step:", steps_cnt, "z_nodes_cnt =", z_nodes_cnt)

    print("Steps required: ", steps_cnt)


def make_step(args):
    index, x = args
    cur_node = nodes_instructions[x][direction]
    starting_nodes[index] = cur_node
    if cur_node[-1] == "Z":
        z_nodes_cnt = 1
    else:
        z_nodes_cnt = 0
    return z_nodes_cnt



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
