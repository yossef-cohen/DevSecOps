#!/usr/bin/env python3

# Part 1:

# Start with a list with un-ordered numbers.
# Example:

# [15 , 2 , 8, -4, 76, 3, 2, 1, 80, -3]

# first, write a code that finds the SMALLEST number, then:
# - print this number
# - remove it from the list.

# Part2: 

# You you repeatedly remove and print the smallest number, your program may end up
# printing all numbers in ascending order.
# Can you loop around all of your code from part 1, until the list is empty?

import random


lst = [15 , 2 , 8, -4, 76, 3, 2, 1, 80, -3]
min_index = 1
for i in range(len(lst)):
    for j, num in enumerate(lst):
        if lst[j] < lst[min_index] and len(lst) != 1:
            min_index = j
    print(f"min_index: {min_index}, min_value: {lst[min_index]}")
    del(lst[min_index])
    min_index = random.randint(0, len(lst))
print(lst)
            
            