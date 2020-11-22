#this is a python immitation of a russian card game Durak

from enum import Enum
from random import *
from enum import IntEnum

full_deck = []
partial_deck = []

#Creating Enum for each card
class Cards(IntEnum):
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

#Suits of every card
class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'

#Class to hold info for playing cards
class PlayingCards():
    def __init__(self,card_value,card_suit):
        self.card = card_value
        self.suit = card_suit


#Creating a full deck of cards
def create_deck():
    for x in Suit:  
        
        for i in Cards:
            
            full_deck.append(PlayingCards(Cards(i),Suit(x)))
    return full_deck

#draw a single card from the deck
def draw_deck(deck):
    rand_card = randint(0,len(deck)-1)
    return deck.pop(rand_card)

create_deck()
partial_deck = list(full_deck)

for c in full_deck.Suit():
    print(c)