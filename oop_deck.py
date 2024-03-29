# OOP practice. Source: https://www.youtube.com/watch?v=t8YkjDH86Y4
import random

class Card(object):
    """docstring for Card."""

    def __init__(self, suit, val):
#        super(Card, self).__init__()
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val, self.suit))

class Deck(object):
    """docstring for ."""

    def __init__(self):
#        super(, self).__init__()
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Heards"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player(object):
    """docstring for ."""

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

#card = Card("Clubs", 6)
#card.show()

deck = Deck()
deck.shuffle()
#deck.show()
bob = Player("Bob")
bob.draw(deck).draw(deck)
bob.showHand()
#card = deck.draw()
#card.show()
