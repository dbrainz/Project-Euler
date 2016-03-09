# Project Euler - Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are
# called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#
# Darren Brain
# darren.brain@gmail.com
# 3/6/2016

from math import sqrt

def sum_of_factors(check_factor):
    '''Returns the sum of the factors of check_factor'''

    factor_sum = 1
    step = 2
    start_num = 1
    if check_factor % 2 == 0:
        step = 1
        start_num = 2
    for work_factor in range(start_num, int(sqrt(check_factor)) + 1, step):
        if check_factor % work_factor == 0:
            factor_sum += work_factor + (check_factor / work_factor)
    return int(factor_sum)




amicable_sum = 0
amicable_list= []
for check_num in range(2,10000):
    if check_num not in amicable_list:
        num_factor = sum_of_factors(check_num)
        if num_factor != check_num:
            second_sum = sum_of_factors(num_factor)
        if check_num == second_sum:
            print(check_num, num_factor)
            if num_factor < 10000:
                amicable_sum += check_num + num_factor
                amicable_list.append(check_num)
                amicable_list.append(num_factor)
            else:
                amicable_sum += check_num
                amicable_list.append(check_num)
print(amicable_sum)
print(amicable_list)


