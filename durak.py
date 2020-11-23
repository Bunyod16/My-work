#this is a python immitation of a russian card game Durak

import time
from enum import Enum
from random import *
from enum import IntEnum

full_deck = []
partial_deck = []
playerdeck = []
aideck = []

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

def dealingplayers():
    while(len(partial_deck) > 0):
            playerdeck.append(draw_deck(partial_deck))
            aideck.append(draw_deck(partial_deck))


#draw a single card from the deck

def draw_deck(deck):
    
    rand_card = randint(0,len(deck)-1)
    return deck.pop(rand_card)
    


create_deck()
partial_deck = list(full_deck)
dealingplayers()

def game():
    
    for x in range(0,len(playerdeck)):
        
        #GRAPHICAL
        print('You have:')
        
        for x in range(0,len(playerdeck)):
            print(playerdeck[x].card)
        print(len(playerdeck))
        ###############

        #Picking a random number to pick a card
        randomint = randint(0,len(playerdeck)-1)
    
    
        playerscard = playerdeck[randomint].card
        aiscards = aideck[randint(0,len(aideck)-1)].card
    
        if playerscard > aiscards:
            print('WIN!')
        else: print('LOOSE!')
        print('randint =',randomint)
        playerdeck.pop(playerscard)
        aideck.pop(aiscards)

#while win not True:
#    game():
end = False
def test():
    

        for x in range(len(playerdeck)):
            print(x,playerdeck[x].card,playerdeck[x].suit)
            
        player = int(input('Which card do you want to pick?: '))
        try:

            print('You picked: ',playerdeck[player].card,playerdeck[player].suit)
            time.sleep(3)
            playerdeck.pop(player)
            if len(playerdeck) < 1:
                end = False
            else: end = True
        except:
            print('Your Index was out of range!!!')
            time.sleep(2)

        
while end == False:
    test()

#for x in playerdeck:
#   print(playerdeck