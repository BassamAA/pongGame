from turtle import Turtle

ALIGN = "center"
FONT = ("Roboto",90,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0

    def updateScore(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 320)
        self.write(f"{self.player1_score}    {self.player2_score}", font=FONT, align= "center")

    def player1_scored(self):
        self.player1_score += 1
        self.updateScore()

    def player2_scored(self):
        self.player2_score += 1
        self.updateScore()

