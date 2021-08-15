# Rabbit Game by Kelompok 9 
# Women Tech in Python Programming by Digital Talent Scholarship
# References By @TokyoEdTech

import turtle
import os
import random
import time
import pygame
from pygame import mixer
pygame.init()


# Set up the screen
wn = turtle.Screen()
wn.title("Rabbit Game By Kelompok 9")
wn.bgcolor("black")
wn.bgpic("bg_kebun.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("kelinci_left.gif")
wn.register_shape("kelinci_right.gif")
wn.register_shape("carrot2.gif")
wn.register_shape("brokoli2.gif")

# Score
score = 0

# Health
lives = 3


# Player
player = turtle.Turtle()
player.speed(0)
player.shape("kelinci_right.gif")
player.color("white")
player.penup()
player.goto(0, -220)
player.direction = "stop"

# Good things
good_things = []

for _ in range(10):
    good_thing = turtle.Turtle()
    good_thing.speed = 1
    good_thing.shape("carrot2.gif")
    good_thing.color("green")
    good_thing.penup()
    good_thing.goto(-100, 250)
    #good_thing.speed = random.randint(1, 2)

    good_things.append(good_thing)

# Bad things
bad_things = []

for _ in range(3):
    bad_thing = turtle.Turtle()
    bad_thing.speed(2)
    bad_thing.shape("brokoli2.gif")
    bad_thing.color("red")
    bad_thing.penup()
    bad_thing.goto(100, 250)
    bad_thing.speed = random.randint(1, 2)

    bad_things.append(bad_thing)

# Pen
pen = turtle.Turtle()
pen.speed(6)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Lives: 5", align="center", font=("Courier", 24, "bold"))
pen.color('black')

eatSound = pygame.mixer.Sound("rabbit_eat2.mp3")
failedSound = pygame.mixer.Sound("brokoli.wav")
# Functions
def go_left():
    player.direction = "left"
    player.shape("kelinci_left.gif")
    
def go_right():
    player.direction = "right"
    player.shape("kelinci_right.gif")

    
# Keyboard bindings
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()
    
    # Move the player
    if player.direction == "left":
        player.setx(player.xcor() - 1)
    
    if player.direction == "right":
        player.setx(player.xcor() + 1)
        
    # Check for border collisions
    if player.xcor() < -390:
        player.setx(-390)
        
    elif player.xcor() > 390:
        player.setx(390)
        
    for good_thing in good_things:
        # Move the good things
        good_thing.sety(good_thing.ycor() - good_thing.speed)

        # Check if good things are off the screen
        if good_thing.ycor() < -300:
            good_thing.goto(random.randint(-300, 300), random.randint(400, 800))
            

        # Check for collisions
        if player.distance(good_thing) < 40:
            eatSound.play()
            # Score increases
            score += 10
        
            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "bold"))
            pen.color('black')
        
            # Move the good thing back to the top
            good_thing.goto(random.randint(-300, 300), random.randint(400, 800))



    for bad_thing in bad_things:    
        # Move the bad things
        bad_thing.sety(bad_thing.ycor() - bad_thing.speed)
    
        if bad_thing.ycor() < -300:
            bad_thing.goto(random.randint(-300, 300), random.randint(400, 800))
    
        
        if player.distance(bad_thing) < 40:
            failedSound.play()
            # Score increases
            score -= 10
            lives -= 1
        
            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "bold"))
            pen.color('black')
            
            time.sleep(1)
            # Move the bad things back to the top
            for bad_thing in bad_things:
                bad_thing.goto(random.randint(-300, 300), random.randint(400, 800))
        


    # Check for game over
    if lives == 0 and score > 500:
        pen.clear()
        pen.write("You are Winner! Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        pen.color('black')
        wn.update()
        time.sleep(5)
        score = 0
        lives = 5
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "bold"))
        pen.color('black')
        wn.update()

    elif lives == 0 and score <= 500:
        pen.clear()
        pen.write("Game Over! Score : {}".format(score), align="center", font=("Courier", 24, "bold"))
        pen.color('black')
        wn.update()
        time.sleep(5)
        score = 0
        lives = 5
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "bold"))
        pen.color('black')
        wn.update()

        
   