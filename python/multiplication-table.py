#!/usr/bin/env python3

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}".center(1, " "), end="")
    print()