# Import stuff

import turtle as trtl
import random as rand

# Creator Specialities

creator = "Nathaniel M. Vitale"
schoolclass = "Computer Science Principals AP"
teacher = "A. Kiedes"


# Initialize screen

wn = trtl.Screen()
wn.register_shape("tolkie-cool.gif")

# Game configuration

spot_color = "red"
clicked_color = "dark red"


# Initialize turtle as "Game"

game = trtl.Turtle()
game.shape("tolkie-cool.gif")


# Turtle features

game.penup()
game.color(spot_color)
game.shapesize(5)


# Game functions

#Get a score boost, change turtle position to a random coordinate
def click(x, y):
    print("Turtle has been Clicked! Game by:",creator, schoolclass,teacher)
    game.color(clicked_color)
    game.color(spot_color)
    rand


# Game Events

game.onclick(click)


# Screen
wn.mainloop()