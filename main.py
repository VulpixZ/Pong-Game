#PONG-GAME-by-iamjz

import turtle as t
import time
import pyautogui as pag     # pip install pyautogui
import keyboard as kb       # pip install keyboard

#mode / difficulty selection
def game():

    mode = pag.prompt(text="1-Player (1)\n"
                           "2-Players (2)",title="Choose mode : ")
    while not (0 < int(mode) < 3):
        mode = pag.prompt(text="1-Player (1)\n"
                               "2-Players (2)", title="Choose mode : ")
    difficulty = pag.prompt(text="Easy (1)\n"
                                 "Normal (2)\n"
                                 "Hard (3)", title="Choose difficulty : ")
    while not (0 < int(difficulty) < 4):
        difficulty = pag.prompt(text="Easy (1)\n"
                                     "Normal (2)\n"
                                     "Hard (3)", title="Choose difficulty : ")

    #variables
    scoreBlue = 0
    scoreRed = 0

    #window
    wn = t.Screen()
    wn.clear()
    wn.title("Pong Game by iamjz")
    wn.bgcolor("Black")
    wn.setup(width = 800, height = 600)
    wn.tracer(0)
    #football field pattern
    def field():
        t.penup()
        t.goto(-400, 300)
        t.pendown()
        t.color("white")
        t.pensize(3)
        t.goto(400, 300)
        t.goto(400, -300)
        t.goto(-400, -300)
        t.goto(-400, 300)
        t.penup()
        t.goto(0,300)
        t.pendown()
        t.goto(0,-300)
        t.penup()
        t.goto(0,-100)
        t.pendown()
        t.circle(100)
        t.hideturtle()

#draw football field pattern
    field()

    #paddle Blue
    padB = t.Turtle()
    padB.speed(0)
    padB.shape("square")
    padB.color("blue")
    padB.shapesize(stretch_wid= 5, stretch_len=0.5)
    padB.penup()
    padB.goto(-350 , 0)

    #paddle Red
    padR = t.Turtle()
    padR.speed(0)
    padR.shape("square")
    padR.color("red")
    padR.shapesize(stretch_wid= 5, stretch_len=0.5)
    padR.penup()
    padR.goto(350 , 0)

    #ball
    ball = t.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    ball.dx = 0.1
    ball.dy = 0.1

    #score
    pen = t.Turtle()
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("BLUE : 0     RED : 0",align = "center", font=("Itim" , 24 , "bold"))

    #functions / player limit
    def padB_up():
        if padB.ycor() < 245:
            y = padB.ycor()
            y += 50
            padB.sety(y)
    def padB_down():
        if padB.ycor() > -245:
            y = padB.ycor()
            y -= 50
            padB.sety(y)
    def padR_up():
        if padR.ycor() < 245:
            y = padR.ycor()
            y += 50
            padR.sety(y)
    def padR_down():
        if padR.ycor() > -245:
            y = padR.ycor()
            y -= 50
            padR.sety(y)

    #KB binding
    wn.listen()
    wn.onkeypress(padB_up , "w")
    wn.onkeypress(padB_down, "s")
    wn.onkeypress(padR_up, "Up")
    wn.onkeypress(padR_down, "Down")

    # Define the initial speed factor
    speed_factor = 30

    while 1:
        wn.update()
    # Add a delay
        time.sleep(0.01)

    #ball move
        ball.setx(ball.xcor() + ball.dx * speed_factor)
        ball.sety(ball.ycor() + ball.dy * speed_factor)

    #collision
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        if ball.xcor() > 390:
            scoreBlue += 1
            pen.clear()
            pen.write("BLUE : {}     RED : {}".format(scoreBlue,scoreRed), align = "center", font=("Itim", 24, "bold"))
            ball.goto(0,0)
            ball.dx *= -1
        if ball.xcor() < -390:
            scoreRed += 1
            pen.clear()
            pen.write("BLUE : {}     RED : {}".format(scoreBlue, scoreRed), align = "center", font=("Itim", 24, "bold"))
            ball.goto(0,0)
            ball.dx *= -1

    #player collision
        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > padB.ycor() - 50 and ball.ycor() < padB.ycor() + 50:
            ball.setx(-340)
            ball.dx *= -1
        if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > padR.ycor() - 50 and ball.ycor() < padR.ycor() + 50:
            ball.setx(340)
            ball.dx *= -1

    #win
        if scoreBlue == 5:
            wn.clear()
            wn.bgcolor("black")
            pen.clear()
            pen = t.Turtle()
            pen.color("blue")
            pen.penup()
            pen.hideturtle()
            pen.goto(0, 0)
            pen.write("BLUE WIN", align="center", font=("Itim", 24, "bold"))
            pen.penup()
            pen.goto(0, -200)
            pen.color("white")
            pen.pendown()
            pen.write("Press 'space' to restart", align="center", font=("Itim", 24, "bold"))
            time.sleep(1)
            while 1:
                if kb.is_pressed("space"):
                    game()
                    break
        if scoreRed == 5:
            wn.clear()
            wn.bgcolor("black")
            pen.clear()
            pen = t.Turtle()
            pen.color("red")
            pen.penup()
            pen.hideturtle()
            pen.goto(0, 0)
            pen.write("RED WIN", align="center", font=("Itim", 24, "bold"))
            pen.penup()
            pen.goto(0, -200)
            pen.color("white")
            pen.pendown()
            pen.write("Press 'space' to restart", align="center", font=("Itim", 24, "bold"))
            time.sleep(1)
            while 1:
                if kb.is_pressed("space"):
                    game()
                    break
    # AI Player (1-Player)
        if mode == "1":
            # Red-player
            if padR.ycor() > ball.ycor() and abs(padR.ycor() - ball.ycor()) > 10:
                padR_down()
            if padR.ycor() < ball.ycor() and abs(padR.ycor() - ball.ycor()) > 10:
                padR_up()
    # Difficulty
        if difficulty == "1":
            speed_factor = 30
            ball.color("lime")
        elif difficulty == "2":
            speed_factor = 35
            ball.color("yellow")
        else:
            speed_factor = 40
            ball.color("white")

game()