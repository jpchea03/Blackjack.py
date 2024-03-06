#Title: sBlackjack.py
#Author: Joseph Cheatham
#Description: This program simulates a simple, blackjack style card game
#where the user and dealer draw cards. The goal is to get as large a hand
#as possible without exceeding 21, called going bust.
import random

def showPlayerHand(playerHand):
    print("Your hand: ", playerHand)

def showDealerHand(dealerHand):
    print("Dealer's Hand: ", dealerHand)

def draw():
    #Variables that track the hands and the decision to continue drawing
    playerHand = random.randrange(1, 11)
    dealerHand = random.randrange(1, 11)
    decision = 'y'
    
    #Runs until player decides to stop drawing or exceeds 21
    while (decision != 'n' and playerHand <= 21):
        decision = input("Would you like to draw")

if __name__ == '__main__':
    playerHand = 15
    dealerHand = 12
    showPlayerHand(playerHand)
    showDealerHand(dealerHand)