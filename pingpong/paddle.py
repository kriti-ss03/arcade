from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        # self.setheading(90)
        self.shapesize(5,1)
        
    
    def place(self,x,y):
        self.goto(x,y)

    def moveup(self):
        newy=self.ycor()+20
        self.goto(self.xcor(),newy)

    def movedown(self):
        newy=self.ycor()-20
        self.goto(self.xcor(),newy)
    
    

