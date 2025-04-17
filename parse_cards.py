
from card import Card

def parse_cards(input_str):
    rank_map = {'a': 14, '1': 14, 'j': 11, 'q': 12, 'k': 13}

    valid_ranks = {2,3,4,5,6,7,8,9,10,11,12,13,14}
    valid_suits = {'s','d','c','h'}

    input_cards = input_str.split()
    parsed_cards = []

    for input_card in input_cards:
        rank = input_card[:-1]
        suit = input_card[-1]

        rank = rank.lower()
        if rank in rank_map:
            rank = rank_map[rank]
        else:
            rank = int(rank)  # Convert rank if it's in rank_map


        if rank not in valid_ranks or suit not in valid_suits:
            raise ValueError(f"Invalid card: {input_card}")

        output_card = Card(rank, suit)
        parsed_cards.append(output_card)

    return parsed_cards
