# Project Euler - Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# Darren Brain
# darren.brain@gmail.com
# 3/2/2016

longest_number = 0
longest_chain = 0

for check_num in range(1,1000000):
    work_num = check_num
    work_counter = 0
    one_found = False
    while one_found != True:
        if work_num % 2 == 0:
             work_num = work_num / 2
        else:
            work_num = 3 * work_num + 1
        work_counter += 1
        if work_num == 1:
            one_found = True
    if work_counter > longest_chain:
        longest_chain = work_counter
        longest_number = check_num

print(longest_number)
