import random

class Card:

    def __init__(self, suit, number):
       # the constructor for a class.
        self._suit = suit
        self._number = number

    def __repr__(self):
    #    RePresenation of number and suit    """
        return self._number + " of " + self._suit

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
    #    Searching the suit in the Array and then prints a suit(s) that user ask.    """
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
     # getter """
        return self._number

    @number.setter
    def number(self, number):
      #setter """
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:

    def __init__(self):
    #    the constructor for a class.    """
        self._cards = []
        self.populate()

    def populate(self):
       # This method shows a betting """
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        # make a deal and put it to array """
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"

deck = Deck()
print(deck)
