# http://www.codeskulptor.org/#user43_QCmXyknBZs_0.py

# There are several ways to calculate the area of a regular polygon.
# Given the number of sides, n, and the length of each side, s, the polygon's area is
# ns2/4tan(π/n)
# For example, a regular polygon with 5 sides, each of length 7 inches,
# has area 84.3033926289 square inches.
# Write a function that calculates the area of a regular polygon,
# given the number of sides and length of each side.
# Submit the area of a regular polygon with 7 sides each of length 3 inches.
# Enter a number (and not the units) with at least four digits of precision after the decimal point.

# Note that the use of inches as the unit of measurement in these examples is arbitrary.
# Python only keeps track of the numerical values, not the units.

import math
def ploygon_area(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi/n))

print str(ploygon_area(5, 7))