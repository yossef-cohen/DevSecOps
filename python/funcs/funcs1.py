
def add_nums(a, b):
    print(a + b)

def sub_nums(a, b):
    print(a - b)

def mul_nums(a, b):
    print(a * b)

def div_nums(a, b):
    if b == 0:
        print("Error: Division by zero")
    else:
        print(a / b)

def pow_nums(a, b):
    if a == 0 and b < 0:
        print("Error: 0 cannot be raised to a negative power")
    else:
        print(a ** b)

def root_nums(a, b):
    if a < 0 and b % 2 == 0:
        print("Error: Cannot compute even root of negative number")
    else:
        print(a ** (1 / b))


add_nums(3, 4)
sub_nums(10, 5)
mul_nums(2, 3)
div_nums(3, 0)
pow_nums(2, -2)
root_nums(-7, 3)