# http://www.codeskulptor.org/#user43_SFSbiBw2Nj_0.py

# QUIZ Question 6:
# Implement the mathematical function f(x)=−5x5+69x2−47 as a Python function.
# Then use Python to compute the function values f(0), f(1), f(2), and f(3).
# Enter the maximum of these four values calculated.

def math_function(x):
    return -5 * (x ** 5) + 69 * (x ** 2) - 47


fzero = math_function(0)
fone = math_function(1)
ftwo = math_function(2)
fthree = math_function(3)

print "f(0)= " + str(fzero) + ", f(1)= " +  str(fone) + ",",
print "f(2)= " + str(ftwo) + ", f(3)= " + str(fthree)

maximum = fzero

if (maximum < fone):
    maximum = fone
if (maximum < ftwo):
    maximum = ftwo
if (maximum < fthree):
    maximum = fthree

print "Maximum value is: " + str(maximum)