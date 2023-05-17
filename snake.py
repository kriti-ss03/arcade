from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake():
    # init=what happens when initialize
    def __init__(self):
        # using wturtle inside function so as to vary it; insted of global
        self.wturtle = []
        self.create_snake()
        self.head = self.wturtle[0]
        self.tail=self.wturtle[-1]

    def create_snake(self):
        for pos in START_POS:
            self.add_seg(pos)

    def add_seg(self,pos):
    # add new seg
        t = Turtle(shape="square")
        t.speed("fastest")
        t.penup()
        t.goto(pos)
        t.color("white")
        self.wturtle.append(t)

    def extend(self):
        # getting position() of last seg using turtle method
        self.add_seg(self.wturtle[-1].position())
        self.tail=self.wturtle[-1]



    # MOVING FROM BACK
    def move(self):
        for seg in range(len(self.wturtle) - 1, 0, -1):
            new_x = self.wturtle[seg - 1].xcor()
            new_y = self.wturtle[seg - 1].ycor()
            self.wturtle[seg].goto(new_x, new_y)
        self.head.fd(MOVE_DIS)
        # self.wturtle[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
