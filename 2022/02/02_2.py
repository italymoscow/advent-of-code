'''
Solution to the Day 2: Rock Paper Scissors, Part 2.

Task:
    Following the Elf's instructions for the second column, 
    what would your total score be if everything goes exactly 
    according to your strategy guide?

Returns:
    "Total score: 12526"
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
        case "X":  # Need to loose
            score_round += 0
            match outcome_opponent:
                case "A":  # "Rock"
                    score_round += 3  # Scissors
                case "B":  # "Paper"
                    score_round += 1  # Rock
                case "C":  # "Scissors"
                    score_round += 2  # Paper
        case "Y":  # End in a draw
            score_round += 3
            match outcome_opponent:
                case "A":  # "Rock"
                    score_round += 1  # Rock
                case "B":  # "Paper"
                    score_round += 2  # Paper
                case "C":  # "Scissors"
                    score_round += 3  # Scissors
        case "Z":  # Need to win
            score_round += 6
            match outcome_opponent:
                case "A":  # "Rock"
                    score_round += 2  # Paper
                case "B":  # "Paper"
                    score_round += 3  # Scissors
                case "C":  # "Scissors"
                    score_round += 1  # Rock
    return score_round


if __name__ == "__main__":
    main()
