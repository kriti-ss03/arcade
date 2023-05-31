from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.goto(0,0)
        self.xmove=1
        self.ymove=1
        self.move_speed=0.1 
        # to incr speed of ball with each hit
    
    def move(self):
        new_x=self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove
        self.goto(new_x,new_y)


    def reflecty(self):
        self.ymove*=-1

# with paddle
    def reflectx(self):
        self.xmove*=-1
        self.move_speed*=0.9
    
    def reset_ball(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.reflectx()

