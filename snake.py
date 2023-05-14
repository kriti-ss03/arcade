from turtle import Turtle
wturtle=[]
start_pos=[(0,0),(-20,0),(-40,0)]

class Snake():
    def __init__(self):
        for pos in start_pos:
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            wturtle.append(t)
            t.goto(pos)

    def move(self):
        for seg in range(len(wturtle) - 1, 0, -1):
            new_x = wturtle[seg - 1].xcor()
            new_y = wturtle[seg - 1].ycor()
            wturtle[seg].goto(new_x, new_y)

        wturtle[0].fd(20)
        wturtle[0].left(90)