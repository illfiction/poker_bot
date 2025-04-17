# Start of PokerBotv1
import sys
import time
import os
start = time.time()

from card import Card
from parse_cards import parse_cards
from  flop_probability import flop_probability


# pre-flop
pocket_cards_str = "2d qs"
# pocket_cards_str = input("Enter your cards:")
pocket_cards = parse_cards(pocket_cards_str)
# print(pocket_cards[0])
if len(pocket_cards) != 2:
    print("Number of pocket cards is not 2!")
    sys.exit(1)

# pre-flop_probability
#TODO : calculate pre-flop probability
#pre-flop probability will take too long to run

flop_cards_str = "9h 7c 10s"
# flop_cards_str = input("Enter flop cards:")
flop_cards = parse_cards(flop_cards_str)
if len(flop_cards) != 3:
    print("Number of flop cards is not 3!")
    sys.exit(1)

# print(flop_cards)

flop_prob = flop_probability(pocket_cards,flop_cards,pocket_cards_str,flop_cards_str)

end = time.time()
print(f"Runtime: {end - start:.4f} seconds")