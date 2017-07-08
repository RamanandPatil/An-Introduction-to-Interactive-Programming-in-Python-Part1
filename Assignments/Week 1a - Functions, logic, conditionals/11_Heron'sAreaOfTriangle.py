# http://www.codeskulptor.org/#user43_xBWpqOow5q_0.py

# Compute the area of a triangle (using Heron's formula),
# given its side lengths.

# Challenge: Write a Python function triangle_area that takes the parameters x0, y0, x1,y1, x2, and y2,
# and returns the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2).
# (Hint: use the function point_distance as a helper function and apply Heron's formula.) 

###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Also define point_distance as use it as a helper function.
def triangle_area(x0, y0, x1, y1, x2, y2):
    
    # calculate the sides namely a, b and c of the traingle, using distance formula.
    a = point_distance(x0, y0, x1, y1)
    b = point_distance(x1, y1, x2, y2)
    c = point_distance(x2, y2, x0, y0)
    
    # Compute the semi-perimeter length, i.e., half of the perimeter length.
    s = (a + b + c)/2
    # Compute and return the area according to Heron's formula.
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
def point_distance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5


###################################################
# Tests
# Student should not change this code.

def test(x0, y0, x1, y1, x2, y2):
    print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
    print "(" + str(x1) + "," + str(y1) + "), and",
    print "(" + str(x2) + "," + str(y2) + ") has an area of",
    print str(triangle_area(x0, y0, x1, y1, x2, y2)) + "."

test(0, 0, 3, 4, 1, 1)
test(-2, 4, 1, 6, 2, 1)
test(10, 0, 0, 0, 0, 10)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
