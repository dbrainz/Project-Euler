# Project Euler - Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Darren Brain
# darren.brain@gmail.com
# 2/28/2016

for check_num in range(20, 1000000000, 20):
    for check_factor in range(2, 21):
        if check_num % check_factor != 0:
            break
    if check_factor == 20:
        print(check_num)
        break

