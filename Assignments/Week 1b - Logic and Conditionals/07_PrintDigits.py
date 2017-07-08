# http://www.codeskulptor.org/#user43_SRSd1BdwuV_0.py

# Compute and print tens and ones digit of an integer in [0,100).

# Write a Python function print_digits that takes an integer number in the range [0,100)
# and prints the message "The tens digit is %, and the ones digit is %."
# where the percents should be replaced with the appropriate values.
# The function should include an error check for the case
# when number is negative or greater than or equal to 100.
# In those cases, the function should instead print "Error: Input is not a two-digit number.". 

###################################################
# Digits function
# Student should enter function on the next lines.
def print_digits(number):
    """Prints the tens and ones digit of an integer in [0,100)."""
    
    if 0 <= number < 100:
        print "The tens digit is " + str(number // 10) + ",",
        print "and the ones digit is " + str(number % 10) + "."
    else:
        print "Error: Input is not a two-digit number."
        
#My Solution
#    if(number >= 0 and number < 100):
#        print "The tens digit is " + str(number//10)+ ", and",
#        print "the ones digit is " + str(number % 10)+ "."
#    else:
#        print "Error: Input is not a two-digit number."

    
###################################################
# Tests
# Student should not change this code.
    
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
#Error: Input is not a two-digit number.
