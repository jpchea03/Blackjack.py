#Title: Blackjack.py
#Author: Joseph Cheatham
#Description: This program simulates a simple, blackjack style card game
#where the user and dealer draw cards. The goal is to get as large a hand
#as possible without exceeding 21, called going bust.
import random

#Function to display game rules
def displayRules():
    print("\n**************************************************\n"
          +"The goal of Blackjack is to get the value\n"
          + "of your hand as high as possible without exceeding\n"
          + "21. You will play against the dealer, who also will\n"
          + "be drawing. If both the players and the dealers hand\n"
          + "exceeds 21, neither win. Otherwise, whoever has\n"
          + "the better hand wins. Good luck!\n"
          +"\n**************************************************\n")

#Functions to reveal hands in console
def showPlayerHand(playerHand):
    print("Your hand: ", playerHand)

def showDealerHand(dealerHand):
    print("Dealer's Hand: ", dealerHand)


#Functions to draw cards
def playerDraw(playerHand):
    cardValue = random.randrange(1, 11)
    playerHand += cardValue
    print("Player draws " + str(cardValue) + ".")
    return playerHand

def dealerDraw(dealerHand):
    cardValue = random.randrange(1, 11)
    dealerHand += cardValue
    return dealerHand


#Function to compare hands and choose a winner
def compareHands(dealerHand, playerHand):
    winner = 'None'
    # Show player / dealer hands
    print("\n**************************************************\n")
    showPlayerHand(playerHand)
    showDealerHand(dealerHand)
    #Choose a winner
    if playerHand <= 21:
        if dealerHand > 21 or playerHand > dealerHand:
            winner = 'Player'
        elif dealerHand <= 21 and playerHand < dealerHand:
            winner = 'Dealer'
    else:
        if dealerHand <= 21:
            winner = 'Dealer'
    #Display winner
    print("Winner: " + winner)
    print("\n**************************************************\n")


#Function for Blackjack game. Calls previous functions  
def blackjack():
    #Variables for input, hands
    playerInput = ''
    playerHand = 0
    dealerHand = 0
    print("This is blackjack!")
    #Display rules or not (player choice)
    playerInput= input("Would you like to read the rules? (y/n) ")
    if playerInput == 'y':
        displayRules()
    else:
        print("\n**************************************************\n")
    #Initial draw. Happens every game
    print("prepare to draw!")
    print("\n**************************************************\n")
    playerHand = playerDraw(playerHand)
    dealerHand = dealerDraw(dealerHand)
    #Rest of the draws. User chooses whether or not to draw if hand is not busted.
    while True:
        print("\n**************************************************\n")
        print("Players hand: " + str(playerHand))
        #Allows user to draw if hand is not busted
        if playerHand <= 21:
            playerInput = input("Would you like to draw? (y/n) ")
            if playerInput == 'y':
                playerHand = playerDraw(playerHand)
            else:
                break
        else:
            print("Your hand is busted!")
            break
    #Callse compareHands() to determine and display a winner
    compareHands(dealerHand, playerHand)

#Main function
if __name__ == '__main__':
    print("Welcome to Lucky 38 Casino!")
    blackjack()
    print("Thank you for playing!")