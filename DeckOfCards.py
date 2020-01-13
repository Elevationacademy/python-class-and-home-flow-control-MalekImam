import random

arr_card_types = ['red', 'blue', 'green', 'yellow']
arr_card_numbers = [x for x in range(1, 11)]


class Card:
    def __init__(self, card_type=None, card_number=None):
        self.card_type = card_type
        self.card_number = card_number


class Deck:
    def __init__(self, cards):
        self.deck_cards = cards
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > len(self.deck_cards):
            raise StopIteration
        return self.deal()

    def __bool__(self):
        return True if self.deck_cards else False

    def print_deck(self):
        for d_card in self.deck_cards:
            print(f"({d_card.card_type} {d_card.card_number})", end=" ")
        print("\n")

    def shuffle(self):
        random.shuffle(self.deck_cards)

    def deal(self):
        return self.deck_cards.pop(len(self.deck_cards) - 1)


def build_array_cards(cards_type, cards_number):
    return [Card(c_number, c_type) for c_number in cards_number for c_type in cards_type]

    # array_cards = []
    # for c_number in cards_number:
    #     for c_type in cards_type:
    #         new_card = Card(c_number, c_type)
    #         array_cards.append(new_card)
    # return array_cards


arr_cards = build_array_cards(arr_card_types, arr_card_numbers)
deck_cards = Deck(arr_cards)
deck_cards.print_deck()
deck_cards.shuffle()
deck_cards.print_deck()
deal_card = deck_cards.deal()
print(f"Card details: {deal_card.card_type}, {deal_card.card_number} ")
deal_card = deck_cards.deal()
deck_cards.print_deck()

if deck_cards:
    card = deck_cards.deal()
else:
    print("the deck is empty")
