# Project Euler - Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# Darren Brain
# darren.brain@gmail.com
# 2/28/2016

from pyprimes import primes

total = 0
prime_list = primes(2,2000000)
for prime_num in prime_list:
    total += prime_num

print(total)