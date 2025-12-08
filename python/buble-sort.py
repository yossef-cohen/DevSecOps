#!/usr/bin/env python3

lst = [15 , 2 , 8, -4, 76, 3, 2, 1, 80, -3]
for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)