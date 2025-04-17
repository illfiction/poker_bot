from treys import *

evaluator = Evaluator()

def treys_checker(pocket_cards, flop_cards, turn_card, river_card, opp_pocket_card1, opp_pocket_card2):
    board = [Card.new(repr(card)) for card in flop_cards]
    board += [Card.new(repr(turn_card)), Card.new(repr(river_card))]

    user_hand = [Card.new(repr(card)) for card in pocket_cards]
    opp_hand = [Card.new(repr(opp_pocket_card1)), Card.new(repr(opp_pocket_card2))]

    p1_score = evaluator.evaluate(board, user_hand)
    p2_score = evaluator.evaluate(board, opp_hand)


    if p1_score < p2_score:
        return 1
    elif p1_score == p2_score:
        return 0.5
    else:
        return 0
