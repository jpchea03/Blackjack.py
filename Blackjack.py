#Title: sBlackjack.py
#Author: Joseph Cheatham
#Description: This program simulates a simple, blackjack style card game
#where the user and dealer draw cards. The goal is to get as large a hand
#as possible without exceeding 21, called going bust.
import random

#Functions to reveal hands in console
def showPlayerHand(playerHand):
    print("Your hand: ", playerHand)

def showDealerHand(dealerHand):
    print("Dealer's Hand: ", dealerHand)

def draw():
    #Variables that track the hands and the decision to continue drawing
    playerHand = 0
    dealerHand = 0
    decision = 'y'
    
    #Runs until player decides to stop drawing or exceeds 21
    while (decision != 'n' and playerHand <= 21):
        playerHand += random.randrange(1, 11)
        dealerHand += random.randrange(1, 11)
        showPlayerHand(playerHand)
        decision = input("Would you like to draw?(y/n) ")
    return dealerHand, playerHand

def compare(playerHand, dealerHand):
    winner = "No winner"
    if playerHand <= 21 and dealerHand <= 21:
        if playerHand > dealerHand:
            winner = "Player"
            return winner
        else:
            winner = "Dealer"
            return winner


if __name__ == '__main__':
    print("Welcome to Lucky 21 Casino!")
