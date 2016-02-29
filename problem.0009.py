# Project Euler - Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
# Darren Brain
# darren.brain@gmail.com
# 2/28/2016

from math import sqrt

answer_found = False
for a in range(1,400):
    if not answer_found:
        for b in range(a,400):
            c = sqrt(a**2 + b**2)
            if c % 1 == 0:
                if a + b + c == 1000.0:
                    answer_found = True
                    print(a * b * sqrt(a**2 + b**2))
                    break
