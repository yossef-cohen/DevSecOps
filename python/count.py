#!/usr/bin/python3
num = 1
while num <= 50:
    if num == 5:
        print("First num is 5")
    elif num % 5 == 0 and num != 5 and num != 50:
        print(f"next num is {num}")
    elif num == 50:
        print("Last num is 50")
    num += 1