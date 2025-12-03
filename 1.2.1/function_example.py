# Goal -- Draw squares with a Turtle

import turtle as t

y = t.Turtle()

def drawSquare(length):
    for sides in range(4):
        y.pendown()
        y.forward(length)
        y.right(90)
        y.penup()

sqlength = 50
sqdist = 65

for g in range(67):
    drawSquare(sqlength)
    y.goto(y.xcor()+sqdist, 0)
    sqlength = sqlength+25
    if sqdist == 65:
        sqdist = sqdist+65
    elif not sqdist == 65:
        sqdist = sqdist+sqdist
    else:
        sqdist = 65

# Handle Screen
wn = t.Screen()
wn.mainloop()