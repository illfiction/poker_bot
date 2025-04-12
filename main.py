# Start of PokerBotv1
import sys
import time

start = time.time()

from card import Card
from parse_cards import parse_cards
from  flop_probability import flop_probability

# pre-flop
input_str = "6h Kc"
# input_str = input("Enter your cards:")
pocket_cards = parse_cards(input_str)
# print(pocket_cards[0])
if len(pocket_cards) != 2:
    print("Number of pocket cards is not 2!")
    sys.exit(1)

# pre-flop_probability
#TODO : calculate pre-flop probability
#pre-flop probability will take too long to run

input_str = "8d 5s Ac"
# input_str = input("Enter flop cards:")
flop_cards = parse_cards(input_str)
if len(flop_cards) != 3:
    print("Number of flop cards is not 3!")
    sys.exit(1)

# print(flop_cards)

flop_prob = flop_probability(pocket_cards,flop_cards)

end = time.time()
print(f"Runtime: {end - start:.4f} seconds")