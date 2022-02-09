# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.\n\r''')

def chooseCave():
    cave = ''
    # while cave != '1' and cave != '2':
    while cave not in ('1', '2'):
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    # return caves
    return cave
    # syntax: name 'caves' is not defined; function creates 'cave'

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...\n\r')
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        # print 'Gobbles you down in one bite!'
        print('Gobbles you down in one bite!')
        # syntax: missing parentheses

playAgain = 'yes'
# while playAgain = 'yes' or playAgain = 'y':
while playAgain in ('yes', 'y'):
# syntax: equality operations use two parentheses
# pylint R1714 consider-using-in
    displayIntro()
    # caveNumber = choosecave()
    caveNumber = chooseCave()
    # syntax: `def chooseCave():...` is camelCased
    checkCave(caveNumber)
    
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    if playAgain == "no":
        # print("Thanks for planing")
        print("Thanks for playing")
        # spelling: playing is a word, and it makes sense in context of a game

