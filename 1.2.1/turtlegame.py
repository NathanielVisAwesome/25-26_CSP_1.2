# Import stuff

import turtle as trtl
import random as rand

# Creator Specialities

creator = "Nathaniel M. Vitale"
schoolclass = "Computer Science Principals AP"
teacher = "A. Kiedes"

# Initialize screen

wn = trtl.Screen()
print("Game by:",creator,"In",teacher+"'s",schoolclass,"class")


# Game configuration

spot_color = "red"
clicked_color = "dark red"
score = 0


# Initialize turtle as "Game"

game = trtl.Turtle()
game.shape("circle")

# Score Writer
score_writer = trtl.Turtle()

# Turtle features

game.penup()
game.color(spot_color)
game.shapesize(5)


# Game functions

# Score Maker
def update_score():
    global score
    score += 1
    print("Score:",score)

# Change turtle position
def change_pos():
    newX = rand.randint(-300,300)
    newY = rand.randint(-300,300)
    game.goto(newX, newY)
    update_score()

#Get a score boost, change turtle position to a random coordinate
def click(x, y):
    game.color(clicked_color)
    game.color(spot_color)
    change_pos()

def score_update():
    print("Scorewriter is not ready at this time")

# Game Events

game.onclick(click)


# Screen
wn.mainloop()