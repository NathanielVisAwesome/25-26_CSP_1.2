# Import stuff

import turtle as trtl
import random as rand

# Creator Specialities

gameName = "nVte's Aim Trainer"
creator = "Nathaniel M. Vitale"
schoolClass = "Computer Science Principals AP"
teacher = "A. Kiedes"

# Initialize screen

wn = trtl.Screen()

#Credits

print(gameName,"Game by:",creator,"In",teacher+"'s",schoolClass,"class")

cred = trtl.Turtle()
cred.ht()
cred.pd()
cred.teleport(-450,-375)
cred.write((gameName,"Game by:",creator,"In",teacher+"'s",schoolClass,"class"))

# Game configuration

# LISTS

spot_color = "yellow"
clicked_color = "light blue"
score = 0

font = "Comic Sans MS"
fontType = "normal"
fontSize = 30

bgcolor = "sky blue"

timer = 30
timerDone = False
counter_interval = 1000

clickCircle = False

# Initialize turtle as "Game"

game = trtl.Turtle()
game.shape("circle")

# Score Writer
score_writer = trtl.Turtle()
scorebox = 120

score_counter = trtl.Turtle()

# Counter

counter =  trtl.Turtle()

counter.teleport(150, 350)


# Turtle features

game.penup()
game.color(spot_color)
game.shapesize(5)

score_writer.hideturtle()
score_counter.hideturtle()

score_counter.penup()
score_counter.speed(0)

# Game functions

# Scene Setup
wn.bgcolor(bgcolor)

#Update Font Size if it gets too big.
fontScale = 5
fontSettings = (font, fontSize, fontType)

if score <= 1000:
    fontSize = fontSize - fontScale
elif score >= 1000:
    fontSize = fontSize - fontScale
elif score >= 10000:
    fontSize = fontSize - fontScale
elif score == 0:
    score = 0
elif fontSize == 1:
    fontSize = 20
else:
    fontSize = 20

# Score Box
def scoreBox():
    global clickCircle

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
    score_counter.write(score, font=fontSettings)
    clickCircle = True

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
    game.teleport(newX, newY)
    update_score()

#Get a score boost, change turtle position to a random coordinate
def click(x, y):
    global timerDone
    global spot_color

    if not timerDone:
        change_pos()
    else:
        game.hideturtle()

    game.color(clicked_color)
    game.stamp()
    game.color(spot_color)

# Start the countdown and update each frame
def countdown():
  global timer, timerDone
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=fontSettings)
    timerDone = True
  else:
    counter.write("Timer: " + str(timer), font=fontSettings)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def startGame(x,y):
    global play

    if play == "startGame" and clickCircle:
        game.onclick(click)
        play = "playing"
    elif timerDone and clickCircle:
        play = "gameOver"
        print("Time's Up!")
    else:
        play = "startGame"

play = "startGame"

# Game Events

game.onclick(startGame)

if game.onclick(startGame) and play == "startGame":
    game.onclick(click)
else:
    game.onclick(startGame)

scoreBox()

wn.ontimer(countdown, counter_interval)
wn.mainloop()