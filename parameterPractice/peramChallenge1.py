# Make 3 methods following the details given here.
# Method 1: name it "tic" and it takes 2 parameters "num1" and "num2" and returns
# the value of the two parameters when subtracted (ie: num1-num2)
def tic(num1,num2):
    result = num1-num2
    return result

# Method 2: name it "tac" and it takes 1 parameter "exp"
# use a loop to multiply the number 5 by itself "exp" times
def tac(exp):
    for x in range(exp):
        mult = 5**exp
        return mult

# Method 3: name it "toe" that takes no parameters. This method should
# print the results of a method call to "tic(3,5)" and "toe(4)"
def toe():
    print(tic(3,5),tac(4))

toe()