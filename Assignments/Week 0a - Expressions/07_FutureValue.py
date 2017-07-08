# http://www.codeskulptor.org/#user43_dvIZ3xH9Oe_0.py

# Compute the future value of a given present value, annual rate, and number of years.

# Given p dollars, the future value of this money when compounded yearly at a rate of 
# r percent interest for y years is p(1+0.01r)y.

# Write a Python statement that calculates and prints the value of 1000 dollars compounded
# at 7 percent interest for 10 years.

###################################################
# Future value formula: p(1+0.01r)y
# Student should enter statement on the next line.

p = 1000.0
r = 7.0
y = 10.0

print p * (1.0 + 0.01 * r) ** y

# Alternatively:
# print 1000.0 * (1.0 + 0.01 * 7.0) ** 10.0


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#1967.15135729