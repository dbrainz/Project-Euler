# Project Euler - Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
# Darren Brain
# darren.brain@gmail.com
# 2/28/2016

from pyprimes import nth_prime

print(nth_prime(10001))