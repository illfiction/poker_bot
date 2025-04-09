from parse_cards import parse_cards
from tiebreaker import tiebreaker
from hand_checker import flush_checker,straight_checker,is_two_pair,is_single_pair,is_full_house,is_four_of_a_kind,is_three_of_a_kind
from time import sleep

if __name__ == '__main__':

    while(True):
        pocket_cards = parse_cards(input("Enter pocket cards: "))
        flop_cards = parse_cards(input("Enter flop cards: "))
        opp_cards = parse_cards(input("Enter opp cards: "))

        user_hand = set(pocket_cards + flop_cards)
        opp_hand = set(flop_cards + opp_cards)

        is_flush = flush_checker(user_hand)
        is_straight = (straight_checker(user_hand) != 0)
        is_royal_straight = (straight_checker(user_hand) == 2)
        '''
            used this way just so it is more efficient as flush straight are checked multiple times as there are many sub cases
            the following if elif ladder is implemented so that in a particular 7 card set only the highest hand win, more efficient
        '''

        if is_flush and is_royal_straight:
            user_hand_score = 10
            print('user got Royal Flush')
        elif is_straight and is_flush:
            print('user got Straight Flush')
            user_hand_score = 9
        elif is_four_of_a_kind(user_hand):
            print('user got Four of a Kind')
            user_hand_score = 8
        elif is_full_house(user_hand):
            print('user got Full House')
            user_hand_score = 7
        elif is_flush:
            print('user got Flush')
            user_hand_score = 6
        elif is_straight:
            print('user got Straight')
            user_hand_score = 5
        elif is_three_of_a_kind(user_hand):
            print('user got Three of a Kind')
            user_hand_score = 4
        elif is_two_pair(user_hand):
            print('user got Two Pair')
            user_hand_score = 3
        elif is_single_pair(user_hand):
            print('user got Single Pair')
            user_hand_score = 2
        else:
            print('user got No Pair')
            user_hand_score = 1

        is_flush = flush_checker(opp_hand)
        is_straight = (straight_checker(opp_hand) != 0)
        is_royal_straight = (straight_checker(opp_hand) == 2)

        if is_flush and is_royal_straight:
            print('Opp got Royal Flush')
            opp_hand_score = 10
        elif is_straight and is_flush:
            print('Opp got Straight Flush')
            opp_hand_score = 9
        elif is_four_of_a_kind(opp_hand):
            print('Opp got Four of a Kind')
            opp_hand_score = 8
        elif is_full_house(opp_hand):
            print('Opp got Full House')
            opp_hand_score = 7
        elif is_flush:
            print('Opp got Flush')
            opp_hand_score = 6
        elif is_straight:
            print('Opp got Straight')
            opp_hand_score = 5
        elif is_three_of_a_kind(opp_hand):
            print('Opp got Three of a Kind')
            opp_hand_score = 4
        elif is_two_pair(opp_hand):
            print('Opp got Two Pair')
            opp_hand_score = 3
        elif is_single_pair(opp_hand):
            print('Opp got Single Pair')
            opp_hand_score = 2
        else:
            print('Opp got No Pair')
            opp_hand_score = 1

        if user_hand_score > opp_hand_score:
            print("User Won")
        elif user_hand_score < opp_hand_score:
            print("User Lost")
        else:
            print("sort of Tie")
            if tiebreaker(user_hand, opp_hand, user_hand_score):
                     print("User Won")
            elif(tiebreaker(user_hand, opp_hand, user_hand_score)):)

        sleep(10)