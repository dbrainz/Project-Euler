# Project Euler - Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

import sys

def is_palindrome(check_num):
    work_str = str(check_num)
    for check_pos in range(0, len(work_str) // 2 ):
        if work_str[check_pos] != work_str[len(work_str) - check_pos - 1]:
            return False
    return True

answer = 0

for first_num in range(999, 99, -1):
    for second_num in range(first_num, 99, -1):
        if is_palindrome(first_num * second_num):
            if (first_num * second_num) > answer:
                answer = first_num * second_num
                
print(answer)

