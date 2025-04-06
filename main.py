# Start of PokerBotv1

from card import Card
from parse_cards import parse_cards
from  flop_probability import flop_probability

# pre-flop
# input_str = input("Enter your cards:")
input_str = "1s 2c"
pocket_cards = parse_cards(input_str)
# print(pocket_cards[0])

# pre-flop_probability
#TODO : calculate pre-flop probability
#pre-flop probability will take too long to run

input_str = "10s 3c 4h"
# input_str = input("Enter flop cards:")
flop_cards = parse_cards(input_str)
# print(flop_cards)

flop_prob = flop_probability(pocket_cards,flop_cards)