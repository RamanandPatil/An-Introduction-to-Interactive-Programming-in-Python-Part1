# http://www.codeskulptor.org/#user43_EudHsPsthS_0.py

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


# helper functions

def name_to_number(name):
    """
    Function which takes a string input from [rock, Spock, paper, lizard, scissors]
    and returns a corresponding number from [0, 1, 2, 3, 4]
    """
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print name + " is not a valid choice. Please provide a valid name from: ",
        print "rock, Spock, paper, lizard and scissors"

def number_to_name(number):
    """
    Function that converts a given number in the range 0 to 4 into its
    corresponding string name from [rock, Spock, paper, lizard, scissors].
    """
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print str(number) + " is not a valid choice. Please provide a valid number from:",
        print "0, 1, 2, 3 and 4."

import random

def rpsls(player_choice):
    """
    main Rock-paper-scissors-lizard-Spock function, which prints
    the coices made by player and computer and then
    calculates and prints the final winner of the game.
    If there is no winner as per the game rules, itprints "Player and computer tie!"
    """
    
    # print a blank line to separate consecutive games
    print

    # print out the message for the player's choice
    print "Player chooses " + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # return from here if player has made an invalid string choice
    if (player_number == None):
        print "Game terminated!, player made an invalid choice."
        return

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice

    # compute difference of comp_number and player_number modulo five
    result = (comp_number - player_number) % 5

    # use if/elif/else to determine winner, print winner message
    if (result == 1 or result == 2):
        print "Computer wins!"
    elif (result == 3 or result == 4):
        print "Player wins!"
    else:
        print "Player and computer tie!"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


