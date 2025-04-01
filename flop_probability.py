import numpy as np
from deck import deck
from card import Card

def flop_probability(pocket_cards,flop_cards):\

    opened_cards_list = pocket_cards + flop_cards #all cards that are visible to user

    # to check if cards are same
    # for card1 in opened_cards_list:
    #     opened_cards_list.remove(card1)
    #     for card2 in opened_cards_list:
    #         if card1 == card2:
    #             print("ERROR: 2 cards are equal")
    #             return -1
    #     opened_cards_list.append(card1)
    # TODO:make a better card checker to check if 2 cards are same


    opened_cards = set(opened_cards_list) #
    '''    
    changing list to set so they can be easily checked
    Used set because it removes duplicate elements
    faster look up times due to not needing to loop 
    sets are also unordered
    '''

    remaining_cards = [card for card in deck if card not in opened_cards]
    print(remaining_cards)

    for card1 in remaining_cards:
        remaining_cards.remove(card1)
        for card2 in remaining_cards:
            all_open_cards = opened_cards.union(set([card1, card2]))

            # 2 diff cards from remaining cards to find probabilty

def flush(card_set):
    suit_counts = {suit: 0 for suit in "shdc"}  # Initialize suit count dictionary

    for card in card_set:
        suit_counts[card.suit] += 1  # Increment suit count

    max_suit_count = max(suit_counts.values())  # Find the highest suit count

    return max_suit_count >= 5