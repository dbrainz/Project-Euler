# Project Euler - Problem 16
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2**1000?
#
# Darren Brain
# darren.brain@gmail.com
# 3/3/2016

total = 0
giant_num = 2**1000
giant_str = str(giant_num)
for pointer in range(0,len(giant_str)):
    total += int(giant_str[pointer])
print(total)