# Project Euler - Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
# Darren Brain
# darren.brain@gmail.com
# 3/4/2016

from math import factorial

digit_sum = 0
big_num_str = str(factorial(100))

for str_ptr in range(0,len(big_num_str)):
    digit_sum += int(big_num_str[str_ptr])

print(digit_sum)