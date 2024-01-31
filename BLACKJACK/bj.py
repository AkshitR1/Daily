import pysimplegui
import random

card_size = (73,98)
card_centre = (36,49)
card_image = pysimplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

card_back = (71,96)
card_back_centre = (35,48)
card_back_img = pysimplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

in_play = False
outcome = ""
score = 0
cover = 1

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class Card:

    def __init__(self , suit , rank):
        
        if(suit in SUITS) and (rank in RANKS):
                         
                         self.suit = suit
                         self.rank = rank

        else:
            
            self.suit = None
            self.rank = None
            print("Invalid Rank:", suit,rank)

    def __str__(self):
           return self.suit + self.rank
    
    def get_suit(self):
           
           return self.suit
    def get_rank(self):
           
           return self.rank

    def draw(self, canvas, pos):

        card_loc = (card_centre[0] + card_size[0] * RANKS.index(self.rank),
                    card_centre[1] + card_size[1] * SUITS.index(self.suit))
        canvas.draw_image(card_image, card_loc, card_size, [pos[0] + card_centre[0], pos[1] + card_centre[1]], card_size)

class Hand:
        
        def __init__(self):
              
              self.cards = []
       
       

        def __str__(self):
              
            s = "Cards in Hand: "

            for i in self.cards:
                     s = s + str(i) + " "

            return s
        

        def add_card(self,card):
               
               self.cards.append(card)

        def get_value(self):
               
               value = 0
               isAcePr = False
       

                
            