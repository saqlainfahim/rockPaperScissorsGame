# -*- coding: utf-8 -*-
"""rockPaperScissorsGame

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BHJ0IZukFWEB1dAHE09qL4lQ9Qw4_5ax
"""

import random

print("***  Welcome to the game of Rock, Paper, Scissors  ***")
print("             Press 'f' to leave the game.             ")
print()

pickOption = ["rock", "paper", "scissors"]
matchCount = 0
winCountUser = 0
winCountComputer = 0

while True:
    userInput = input("Enter rock / paper / scissors / f: ").lower()

    if userInput == "f":
        break

    if userInput not in pickOption:
        print("invalid Input!")
        continue

    randomNumber = random.randint(0, 2)
    computerInput = pickOption[randomNumber]

    if userInput == computerInput:
       print("Match Draw")
       matchCount += 1

    elif userInput == "rock" and computerInput == "scissors":
        print("Computer choose", computerInput + ". You win!")
        matchCount += 1
        winCountUser += 1

    elif userInput == "paper" and computerInput == "rock":
        print("Computer choose", computerInput + ". You win!")
        matchCount += 1
        winCountUser += 1

    elif userInput == "scissors" and computerInput == "paper":
        print("Computer choose", computerInput + ". You win!")
        matchCount += 1
        winCountUser += 1
    
    else:
        print("Computer choose", computerInput + ". You loose!")
        matchCount += 1
        winCountComputer += 1

    print()

print()
print("Total Match played =", matchCount)
print("You won", winCountUser, "times.")
print("You lost", winCountComputer, "times.")
print("Match drew", (matchCount - (winCountUser + winCountComputer)), "times.")
print()
print("                    - - - GG - - -                    ")