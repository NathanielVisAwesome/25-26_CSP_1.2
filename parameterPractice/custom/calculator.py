# Calculator Method

Type = ""
num1 = 0
num2 = 0
result = 0
cont = ""

def calculator(type,one,two):
    global Type
    global num1
    global num2
    global result
    global cont

    Type = input("What calculation type would you like to use?")
    one = input("What is the first number you will use?")
    
    if not cont == "y":
        two = input("What is the second number you will use?")

    if type in ("plus","addition"):
        result = one + two
    elif type in ("minus","subtraction"):
        result = one - two
    elif type in ("times","multiplication"):
        result = one * two
    elif type in ("divide","division"):
        result = one / two
    elif type in ("mod","modulo"):
        result = one % two
    else:
        result = "TYPE NOT SPECIFIED"

    print(calculator(Type, num1, num2))
    cont = input("Would you like to continue? (y/n)")

if cont == "y":
    calculator(Type, result, num1)