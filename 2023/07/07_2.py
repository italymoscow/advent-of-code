import os
import datetime
from operator import itemgetter


def main():

    # Read the input file
    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\07_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    # Parse input into a list of [[hand_cards], hand_win, hand_type]
    hands = parse_input(lines)

    # Define hand type and update it in the hand
    for hand in hands:
        hand[2] = define_hand_type(hand)

    # Sort by type (2) and hand (0)
    hands_sorted = sorted(hands, key=itemgetter(2, 0))
    
    # Calculate total_winnings
    total_winnings = 0
    for index, hand in enumerate(hands_sorted):
        # print(hand)
        bid = hand[1]
        rank = index + 1
        winning = bid * rank
        total_winnings += winning

    print("Total Winnings:", total_winnings) # 243255879 is too high


def parse_input(lines: list):
    hands = []
    for line in lines:
        line = line.split()
        hand_cards = list(line[0])
        hand_win = int(line[1])
        hand_type = 0
        for index, char in enumerate(hand_cards):
            if char == "A":
                hand_cards[index] = 14
            elif char == "K":
                hand_cards[index] = 13
            elif char == "Q":
                hand_cards[index] = 12
            elif char == "J":
                hand_cards[index] = 1
            elif char == "T":
                hand_cards[index] = 10
        hand_cards = list(map(int, hand_cards))
        hand = [hand_cards, hand_win, hand_type]
        hands.append(hand)

    return hands


def define_hand_type(hand: list):
    cards = hand[0]
    hand_size = len(cards)
    unique_cards = list(set(cards))
    hand_type = 0

    if len(unique_cards) == hand_size:
        if 1 in unique_cards:
            hand_type = 2  # One pair
        else:
            hand_type = 1  # High card
        return hand_type

    if len(unique_cards) == 1:
        hand_type = 7  # Five of a kind
        return hand_type

    pairs_count = 0

    if 1 not in unique_cards:
        for unique_card in unique_cards:
            card_count = cards.count(unique_card)
            if card_count == 4:
                hand_type = 6  # Four of a kind
                return hand_type
            elif card_count == 3:
                if len(unique_cards) == 2:
                    hand_type = 5  # Full house
                else:
                    hand_type = 4  # Three of a kind
                return hand_type
            elif card_count == 2:
                pairs_count += 1
            else:  # card_count == 1
                continue
        
        if pairs_count == 2:
            hand_type = 3  # Two pair
        else:
            hand_type = 2  # One pair
    
    else: # Contains a joker
    
        for unique_card in unique_cards:
            card_count = cards.count(unique_card)
            
            if card_count == 4:
                hand_type = 7
                return hand_type
            
            elif card_count == 3:
                if len(unique_cards) == 2:
                    hand_type = 7  # Five of a kind
                else:
                    hand_type = 6  # Four of a kind
                return hand_type
            
            elif card_count == 2:
                pairs_count += 1
            else:  # card_count == 1
                continue

        jokers_cnt = cards.count(1)
        if pairs_count == 2:
            if jokers_cnt == 2:
                hand_type = 6  # Four of a kind
            else:
                hand_type = 5  # Full house
        else: # pairs_count == 1
            hand_type = 4  # Three of a kind

    return hand_type


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
