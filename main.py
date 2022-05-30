from turtle import Turtle, Screen
from scoreboard import Scoreboard
import random
from paddle import Paddle
import time
from ball import Ball

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.screensize(800,600)
screen.title("Pong")
separator = Turtle()
separator.hideturtle()
separator.color("white")
separator.penup()
separator.speed(0)
separator.goto(0,-550)
separator.pensize(10)
separator.setheading(90)


while separator.ycor() < 550:
    separator.pendown()
    separator.forward(20)
    separator.penup()
    separator.forward(30)

scoreboard = Scoreboard()

scoreboard.updateScore()
ball = Ball()
paddleR = Paddle(400,0)
paddleL = Paddle(-400,0)
game_is_on = True
screen.listen()
screen.onkey(key="w", fun=paddleL.paddle_up)
screen.onkey(key="s", fun= paddleL.paddle_down)
screen.onkey(key="Up", fun=paddleR.paddle_up)
screen.onkey(key="Down", fun=paddleR.paddle_down)

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.moveBall()

    if ball.ycor() > 400 or ball.ycor() < -400:
        ball.bounce()

    if ball.distance(paddleR) < 43 and ball.xcor() > 320 or ball.distance(paddleL) < 43 and ball.xcor() < -320:
        ball.touchPaddle()
        continue

    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.player1_scored()

    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.player2_scored()





screen.exitonclick()