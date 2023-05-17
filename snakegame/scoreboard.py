from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        self.write(f"Score= {self.score}", align="center", font=('Arial', 20, 'normal'))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score= {self.score}", align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER" , align="center", font=('Arial', 20, 'normal'))