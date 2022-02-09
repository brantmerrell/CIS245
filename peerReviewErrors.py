'''
Game: DragonCaves

You are in a land full of dragons. Choose your dragon, your cave, and your fate.

Run from command line: python peerReviewErrors.py
'''
# documentation: pylint C0114 module docstring
# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Josh Merrell
# Creation Date: February 9, 2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors).
# You need to identify the issues and correct them.

import random
import time

def displayIntro():
    '''Introduces game to user.'''
    # documentation: pylint C0116 function docstrings
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.\n\r''')
    # print()
    # style: replace empty print() with '\n\r' in previous print string

def chooseCave():
    '''Allows user to choose cave.'''
    # documentation: pylint C0116 function docstrings
    cave = ''
    # while cave != '1' and cave != '2':
    while cave not in ('1', '2'):
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    # return caves
    return cave
    # syntax: name 'caves' is not defined; function creates 'cave'

def checkCave(chosenCave):
    '''Indicates to user which scenario follows from chosen cave.'''
    # documentation: pylint C0116 function docstrings
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...\n\r')
    print()
    # style: replace empty print() with '\n\r' in previous print string
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2) # should game be random or solvable?

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
# style: pylint R1714 consider-using-in
    displayIntro()
    # caveNumber = choosecave()
    caveNumber = chooseCave()
    # syntax: `def chooseCave():...` is camelCased
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
    while playAgain not in ('yes', 'y', 'no', 'n'):
        print('Do you want to play again? (please choose yes or no)')
        playAgain = input()
    # design: unexpected playAgain input
    # if playAgain == "no":
    if playAgain not in ('no', 'n'):
    # design: 'y' is accepted as 'yes' so 'n' should be accepted as 'no'
    # style: consistent single-quotes
        # print('Thanks for planing')
        print('Thanks for playing')
        # spelling: playing is a word, and it makes sense in context of a game
        # style: consistent single-quotes

'''
Note from student:

I have corrected anywhere from 5 to 19 errors depending how to count them:
    - 4 or 6 for syntax depending whether to count multiple per line
    - 1 for spelling
    - 0 or 2 for pylint suggestion R1714: `A==B & A==C` -> `A in (B, C)`.
    - 0 or 2 for stylistic suggestions: consistent single-quotes.
    - 0 or 1 for design - unexpected playAgain input (adds while-loop).
    - 0 or 2 for style - replacing empty print statements with '\n\r' in previous print statements
    - 0 or 1 for design - accepting 'n' as 'no' for user input
    - 0 or 4 for pylint suggestions C0114/C0116: module & function docstrings
I have left the following unsolved:
    - pylint error C0103 (invalid-name) - ____ not snake_case: 6 counts
    - pylint error C0103 (invalid-name) - ____ not UPPER_CASE: 4 counts
    - pylint error W0104 (pointless-string-statement) - this note.

Which corrections are in scope of the assignment? Am I missing any?
'''
