'''
Solution to the Day 2: Rock Paper Scissors, Part 1.

Task: 
    What would your total score be if everything goes exactly according to your strategy guide?

Returns:
    "Total score: 10994"
'''


import os


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\02_input.txt", "r")
    rounds = input_file.readlines()
    input_file.close()

    score_total = 0

    for round in rounds:
        round_outcomes = round.strip().split(" ")
        outcome_opponent = round_outcomes[0]
        outcome_me = round_outcomes[1]
        score_total += get_round_score(outcome_opponent, outcome_me)

    print("Total score: " + str(score_total))


def get_round_score(outcome_opponent, outcome_me):
    score_round = 0
    match outcome_me:
        case "X":  # Rock
            score_round += 1
            match outcome_opponent:
                case "A":  # "Rock"
                    score_round += 3  # Draw
                case "B":  # "Paper"
                    score_round += 0  # I lost
                case "C":  # "Scissors"
                    score_round += 6  # I won
        case "Y":  # Paper
            score_round += 2
            match outcome_opponent:
                case "A":  # "Rock"
                    score_round += 6  # I won
                case "B":  # "Paper"
                    score_round += 3  # Draw
                case "C":  # "Scissors"
                    score_round += 0  # I lost
        case "Z":  # Scissors
            score_round += 3
            match outcome_opponent:
                case "A":  # "Rock"
                    score_round += 0  # I lost
                case "B":  # "Paper"
                    score_round += 6  # I won
                case "C":  # "Scissors"
                    score_round += 3  # Draw
    return score_round


if __name__ == "__main__":
    main()
