from treys import *
from parse_cards import parse_cards

# pocket_cards,flop_cards,turn_card,river_card,opp_pocket_card1,opp_pocket_card2
def treys_checker(pocket_cards,flop_cards,turn_card,river_card,opp_pocket_card1,opp_pocket_card2):
    board = [Card.new(repr(flop_card)) for flop_card in flop_cards]

    user_hand = [Card.new(repr(pocket_card)) for pocket_card in pocket_cards]
    opp_hand = [Card.new(repr(opp_pocket_card1)),Card.new(repr(opp_pocket_card2))]
    turn_card = Card.new(repr(turn_card))
    river_card = Card.new(repr(river_card))

    board = board + [turn_card,river_card]
    # print("Board:")
    # Card.print_pretty_cards(board)

    evaluator = Evaluator()
    p1_score = evaluator.evaluate(board, user_hand)
    p2_score = evaluator.evaluate(board, opp_hand)
    p1_class = evaluator.get_rank_class(p1_score)
    p2_class = evaluator.get_rank_class(p2_score)

    # print("Player 1 hand rank = %d (%s)\n" % (p1_score, evaluator.class_to_string(p1_class)))
    # print("Player 2 hand rank = %d (%s)\n" % (p2_score, evaluator.class_to_string(p2_class)))

    if p1_score < p2_score:
        # print("ACCORDING TO TREYS: USER WON")
        return 1
    elif p1_score == p2_score:
        # print("ACCORDING TO TREYS: TIE")
        return 0.5
    else:
        # print("ACCORDING TO TREYS: OPP WON")
        return 0

if __name__ == '__main__':
    flop_cards = parse_cards("Ah kd jc")
