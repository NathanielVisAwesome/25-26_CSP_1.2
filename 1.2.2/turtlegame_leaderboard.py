# Import stuff

# 1.2.2 File

import turtle as trtl
import random as rand
import leaderboard as lb

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

#---Game configuration

# Leaderboard

leaderboardFileName = "leaderboard.txt"
player_name = input("What is your name?")



# Spot config

spot_color = "yellow"
clicked_color = "light blue"
score = 0

# Font config

font = "Comic Sans MS"
fontType = "normal"
fontSize = 30

# Scene config

bgcolor = "sky blue"

# Timer config

timer = 30
timerDone = False
counter_interval = 1000

# gameStart variables

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
wn.title("nVte's Aim  Trainer")

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

def manage_leaderboard():
  global score
  global game

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboardFileName)
  leader_scores_list = lb.get_scores(leaderboardFileName)

  # show the leaderboard with or without the current player
  if len(leader_scores_list) < 5 or score >= leader_scores_list[4]:
    lb.update_leaderboard(leaderboardFileName, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, game, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, game, score)

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
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=fontSettings)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def start_game(x, y):
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

game.onclick(start_game)

if game.onclick(start_game) and play == "startGame":
    game.onclick(click)
elif game.onclick(click) and play == "gameOver":
    print("Game Over!")
else:
    game.onclick(start_game)

scoreBox()

wn.ontimer(countdown, counter_interval)
wn.mainloop()