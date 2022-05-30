from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(1.5,1.5)
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed= 0.1

    def moveBall(self):
        self.penup()
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def bounce(self):
        self.y_move = -self.y_move

    def touchPaddle(self):
        self.x_move = - self.x_move
        self.move_speed*=0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce()
        self.move_speed = 0.1

