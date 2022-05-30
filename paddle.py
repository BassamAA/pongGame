from turtle import Turtle



class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shapesize(5,1)
        self.create_paddle(x,y)

    def create_paddle(self,x,y):
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(x, y)


    def paddle_up(self):
        self.goto(self.xcor(),self.ycor()+20)


    def paddle_down(self):
        self.goto(self.xcor(), self.ycor() - 20)










