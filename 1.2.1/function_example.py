# Goal -- Draw squares with a Turtle

import turtle as t

y = t.Turtle()

def drawSquare():
    for q in range(4):
        y.pendown()
        y.forward(30)
        y.right(90)
        y.penup()

for g in range(2):
    drawSquare()
    y.goto(y.xcor()+60, 0)

# Handle Screen
wn = t.Screen()
wn.mainloop()