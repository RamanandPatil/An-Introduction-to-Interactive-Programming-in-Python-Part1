# http://www.codeskulptor.org/#user43_fWCeYCJci5_0.py

# Compute and print powerball numbers.

# Challenge: Powerball is lottery game in which 6 numbers are drawn at random.
# Players can purchase a lottery ticket with a specific number combination and,
# if the number on the ticket matches the numbers generated in a random drawing,
# the player wins a massive jackpot.
# Write a Python function powerball that takes no arguments and prints the message
# "Today's numbers are %, %, %, %, and %. The Powerball number is %.".
# The first five numbers should be random integers in the range [1,60),
# i.e., at least 1, but less than 60.
# In reality, these five numbers must all be distinct, but for this problem,
# we will allow duplicates.
# The Powerball number is a random integer in the range [1,36),
# i.e., at least 1 but less than 36.
# Use the random module and the function random.randrange to generate the appropriate random numbers.
# Note that this function should print the desired message, rather than returning it as a string.

###################################################
# Powerball function
# Student should enter function on the next lines.
import random
def powerball():
    print "Today's numbers are",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ", and",
    print str(random.randrange(1, 60)) + ". The powerball number is",
    print str(random.randrange(1, 36)) + "."
    

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
