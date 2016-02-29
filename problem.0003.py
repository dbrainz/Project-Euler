# Project Euler - Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from pyprimes import is_prime
from math import sqrt
test_number = 600851475143
answer = 1

test_sqrt = sqrt(test_number) // 1
if test_sqrt % 2 == 0:
    test_sqrt += 1

for test_value in range(1, int(test_sqrt) +2, 2):
    if test_number % test_value == 0:
        if is_prime(test_value):
            if test_value > answer:
                answer = test_value
        if is_prime(test_number // test_value):
            print(test_number // test_value)
            if (test_number // test_value) > answer:
                answer = test_number // test_value

print(answer)

