# http://www.codeskulptor.org/#user43_QrGaastCBD_0.py

# Compute the distance between the points (x0, y0) and (x1, y1).

# Write a Python function point_distance that takes as the parameters x0, y0, x1 and y1,
# and returns the distance between the points (x0,y0) and (x1,y1). 

###################################################
# Distance formula
# Student should enter function on the next lines.

# Hint: You need to use the power operation ** .
def point_distance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
# Alternatively we can use import math and math.sqrt and math.pow functions.



###################################################
# Tests
# Student should not change this code.

def test(x0, y0, x1, y1):
    print "The distance from (" + str(x0) + ", " + str(y0) + ") to",
    print "(" + str(x1) + ", " + str(y1) + ") is",
    print str(point_distance(x0, y0, x1, y1)) + "."

test(2, 2, 5, 6)
test(1, 1, 2, 2)
test(0, 0, 3, 4)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The distance from (2, 2) to (5, 6) is 5.0.
#The distance from (1, 1) to (2, 2) is 1.41421356237.
#The distance from (0, 0) to (3, 4) is 5.0.
