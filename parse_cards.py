
from card import Card

def parse_cards(input_str):
    rank_map = {'a': '1','k': '13','q': '12','j': '11'}

    valid_ranks = {'1','2','3','4','5','6','7','8','9','10','11','12','13'}
    valid_suits = {'s','d','c','h'}

    input_cards = input_str.split()
    parsed_cards = []

    for input_card in input_cards:
        rank = input_card[:-1]
        suit = input_card[-1]

        rank = rank_map.get(rank.lower(), rank)  # Convert rank if it's in rank_map
        if rank.lower() not in valid_ranks or suit not in valid_suits:
            raise ValueError(f"Invalid card: {input_card}")

        output_card = Card(rank, suit)
        parsed_cards.append(output_card)

    return parsed_cards

