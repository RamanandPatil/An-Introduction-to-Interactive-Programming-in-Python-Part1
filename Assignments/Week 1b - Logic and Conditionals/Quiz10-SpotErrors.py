# http://www.codeskulptor.org/#user43_Nsxa606Hst_0.py

# The following code has a number of syntactic errors in it.
# The intended math calculations are correct, so the only errors are syntactic.
# Fix the syntactic errors.
#
# Once the code has been fully corrected, it should print out two numbers.
# The first should be 1.09888451159. Submit the second number printed in CodeSkulptor.
# Provide at least four digits of precision after the decimal point.

# define project_to_distance(point_x point_y distance):
#     dist_to_origin = math.square_root(pointx ** 2 + pointy ** 2)
#      scale == distance / dist_to_origin
#     print point_x * scale, point_y * scale
#
# project-to-distance(2, 7, 4)

# My Solution:
import math
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)