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

font = ("Comic Sans MS", 20, "normal")


# Initialize turtle as "Game"

game = trtl.Turtle()
game.shape("circle")

# Score Writer
score_writer = trtl.Turtle()
scorebox = 120

# Turtle features

game.penup()
game.color(spot_color)
game.shapesize(5)


# Game functions

# Score Box
def scoreBox():
    score_writer.hideturtle()
    score_writer.penup()
    score_writer.goto(-475, 400)
    score_writer.pendown()
    for scoreDraw in range(2):
        score_writer.forward(scorebox)
        score_writer.right(90)
        score_writer.forward(scorebox / 2)
        score_writer.right(90)

    score_writer.penup()
    score_writer.goto(-450, 350)


# Score Updater
def update_score():
    global score
    score += 1
    print("Score:",score)
    score_writer.write(score, font = font)

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

# Game Events

game.onclick(click)

scoreBox()

# Screen
wn.mainloop()