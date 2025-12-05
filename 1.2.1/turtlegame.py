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

font = "Wingdings"
fontType = "normal"
fontSize = 20

# Initialize turtle as "Game"

game = trtl.Turtle()
game.shape("circle")

# Score Writer
score_writer = trtl.Turtle()
scorebox = 120

score_counter = trtl.Turtle()

# Turtle features

game.penup()
game.color(spot_color)
game.shapesize(5)

score_writer.hideturtle()
score_counter.hideturtle()

score_counter.penup()
score_counter.speed(0)

# Game functions

#Update Font Size if it gets too big.
fontScale = 5

if score <= 1000:
    fontSize = fontSize - fontScale
elif score >= 1000:
    fontSize = fontSize - fontScale
elif score >= 10000:
    fontSize = fontSize - fontScale
elif fontSize == 1:
    fontSize = 20
else:
    fontSize = 20

fontSettings = (font, fontSize, fontType)

# Score Box
def scoreBox():
    score_writer.penup()
    score_writer.teleport(-475, 400)
    score_writer.pendown()
    for scoreDraw in range(2):
        score_writer.forward(scorebox)
        score_writer.right(90)
        score_writer.forward(scorebox / 2)
        score_writer.right(90)

    score_writer.penup()
    score_counter.teleport(-450, 350)


# Score Updater
def update_score():
    global score
    score += 1
    print("Score:",score)
    #Make it so the counter can draw
    score_counter.pendown()
    # Clear the prior score from the screen
    score_counter.clear()
    # Print the current score
    score_counter.write(score, font = fontSettings)

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