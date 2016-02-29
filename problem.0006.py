# Project Euler - Problem 6
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum
#  is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
# Darren Brain
# darren.brain@gmail.com
# 2/28/2016

square_sum = 0
sum_of_squares = 0

for x in range(1,101):
    square_sum += x**2
    sum_of_squares += x

sum_of_squares = sum_of_squares**2

print(sum_of_squares - square_sum)