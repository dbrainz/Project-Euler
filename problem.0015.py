# Project Euler - Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are
# exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#
# Darren Brain
# darren.brain@gmail.com
# 3/3/2016

from math import factorial

def number_of_paths(x, y = 0):
    if y == 0 and x > 0:
        y = x
    elif x == 0:
        return 0
    paths = (factorial(x + y)) / (factorial(x) * factorial(y))
    return paths

euler_answer = number_of_paths(20)
print(euler_answer)

