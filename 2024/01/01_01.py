import os


def main():
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\01_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Create a list to store left values
    left_values = []
    # Create a list to store right values
    right_values = []
    for line in lines:
        line = line.rstrip()
        values = line.split("   ")
        left_values.append(int(values[0]))
        right_values.append(int(values[1]))

    left_values.sort()
    right_values.sort()

    totalDistance = 0
    for i in range(len(left_values)):
        totalDistance += abs(left_values[i] - right_values[i])

    print(totalDistance)

if __name__ == "__main__":
    main()