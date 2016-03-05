# Project Euler - Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
#   are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
#   115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance
#   with British usage.
#
# Darren Brain
# darren.brain@gmail.com
# 3/3/2016

total_letters = 0
len_and = 3
len_hundred = 7
len_thousand = 8
len_1 = 3
len_2 = 3
len_3 = 5
len_4 = 4
len_5 = 4
len_6 = 3
len_7 = 5
len_8 = 5
len_9 = 4
len_10 = 3
len_20 = 6
len_30 = 6
len_40 = 5
len_50 = 5
len_60 = 5
len_70 = 7
len_80 = 6
len_90 = 6
len_1_to_9 = len_1 + len_2 + len_3 + len_4 + len_5 + len_6 + len_7 + len_8 + len_9
len_1_to_19 = len_1_to_9 + 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
len_20_to_99 = (len_20 + len_30 + len_40 + len_50 +  len_60 + len_70 + len_80 + len_90) * 10 + len_1_to_9 * 8
# 1 to 99
total_letters = len_1_to_19 + len_20_to_99
# add in the even hundreds - e.g. 100, 200, 300
total_letters += len_1_to_9 + 9 * len_hundred
# add in the other numbers 100-999 that are not even hundreds
total_letters += (len_1_to_9 * 99) + (9 * 99 * len_hundred) + (9 * 99 * len_and) + (9 * (len_1_to_19 + len_20_to_99))
# add in 1000
total_letters += len_1 + len_thousand

print(total_letters)