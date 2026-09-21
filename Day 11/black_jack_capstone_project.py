

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """returns a random card from the deck..."""
    card = random.choice(cards)
    return cards

deal_card()