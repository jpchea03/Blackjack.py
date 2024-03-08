#Title: Blackjack.py
#Author: Joseph Cheatham
#Description: This program simulates a simple, blackjack style card game
#where the user and dealer draw cards. The goal is to get as large a hand
#as possible without exceeding 21, called going bust.
import random
def displayRules():
    print("The goal of Blackjack is to get the value\n"
          + "of your hand as high as possible without exceeding\n"
          + "21. You will play against the dealer, who also will\n"
          + "be drawing. If both the players and the dealers hand\n"
          + "exceeds 21, neither win. Otherwise, whoever has\n"
          + "the better hand wins.")

#Functions to reveal hands in console
def showPlayerHand(playerHand):
    print("Your hand: ", playerHand)

def showDealerHand(dealerHand):
    print("Dealer's Hand: ", dealerHand)

def playerDraw(playerHand):
    playerHand += random.randrange(1, 11)
    return playerHand

def dealerDraw(dealerHand):
    dealerHand += random.randrange(1, 11)

def blackjack():
    playerInput = ''
    print("Welcome to blackjack!")
    playerInput= input("Would you like to read the rules?")

if __name__ == '__main__':
    print("Welcome to Lucky 21 Casino!")