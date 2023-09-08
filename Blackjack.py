# -*- coding: utf-8 -*-
import random
"""
Created on Tue Sep  5 19:04:39 2023

@author: Joseph Cheatham

Uses random number generation to simulate a blackjack-like game
"""
if __name__ == "__main__":
    print("Welcome to python Black Jack!")
    print("For rules see readme.txt")

    #variable declarations
    playerHand = 0
    dealerHand = 0  
    drawValue = 0
    bustValue = 21
    roundNum = 1
    playerDecision = "yes"
    winner = "None"    
    
    #This loop controls the drawing phase
    while(playerDecision == "yes"):
        print("You draw...")
        playerHand += random.randrange(1,11)
        print("Your hand:", playerHand)
        if playerHand > 21:
            print("Your hand is busted!")
            break
        print("Dealer draws...")
        dealerHand += random.randrange(1,11)
        playerDecision = input("Would you like to draw again? (yes / no)\n")
    
    #Card reveal
    print("Show your cards...")
    print("Your hand:", playerHand)
    print("Dealer's hand:", dealerHand)
    
    #Hands are compared to determine winner
    if playerHand <= 21 and dealerHand <= 21: #neither player or dealer bust
        if playerHand > dealerHand:
            winner = "You"
        elif dealerHand > playerHand:
            winner = "Dealer"
        else:
            winner = "none"
    elif playerHand > 21 and dealerHand <= 21: #player busts but dealer does not
        winner = "dealer"
    else: #both bust
        winner = "None"
            
    #displays winner
    print("Winner:", winner)
        