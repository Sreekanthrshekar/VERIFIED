''' This document demonstrates the power of implementing two
dunder methods: __len__ and __getitem__ '''

from collections import namedtuple
from random import choice

Card = namedtuple('Card','rank suit')

class FrenchDeck:
    ''' has methods for len and getitem '''

    ranks = [str(n) for n in range(2,11)] + list('JKQA')
    suits = 'spades clubs diamonds hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.suits
                       for suit in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# number of cards in French Deck
deck = FrenchDeck()
print(len(deck))
print('''
      ''')

# reading both first and last cards in the Deck

print(deck[0]) # first card
print(deck[-1]) # last card
print('''
      ''')

# choosing random card from deck
print(choice(deck))
print(choice(deck))
print(choice(deck))
print(choice(deck))
print('''
      ''')

# first five cards
print(deck[:5])
print('''
      ''')
#all aces
print(deck[12::13])
print('''
      ''')

# iterating through deck
for card in deck:
    print(card)
print('''
      ''')

# iterating deck in reverse
for card in reversed(deck):
    print(card)

# methods and attributes of deck
print(dir(deck))
