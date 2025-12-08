number = 50
rnge = [0, 99]

while rnge[1] - rnge[0] > 1:
    user_guess = input(f"Is it greater or equal than {number} ?\n")
    if user_guess == "y":
        rnge[0] = number
        
    elif user_guess == "n":
        rnge[1] = number 
    
    number = (rnge[0] + rnge[1]) // 2

if rnge[0] < rnge[1]:
    if input(f"Is it {rnge[0]} ?\n") == "y":
        print(f"thenumber: {rnge[0]}")
    else:
        print(f"the number: {rnge[1]}")
else:
    print(f"the number: {rnge[0]}")