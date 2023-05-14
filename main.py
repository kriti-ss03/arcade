from turtle import Turtle,Screen
import random
import time

screen=Screen()
screen.screensize(600,600)
screen.bgcolor("black")

def u():
    for t in wturtle:
        t.setheading(270)
        t.fd(10)
        t.speed("fastest")

def d():
    for t in wturtle:
        t.setheading(90)
        t.fd(10)

wturtle=[]
start_pos=[(0,0),(-20,0),(-40,0)]


for pos in start_pos:
    t=Turtle(shape="square")
    t.color("white")
    t.penup()
    wturtle.append(t)
    t.goto(pos)



# MOVING FIRST FIRST
# game_on=True
# while game_on:
#     for w in wturtle:
#         w.fd(10)


game_on=True
while game_on:
    # update-> show only once every seg has moved
    screen.update()
    # package to see motion
    time.sleep(0.01)

    # LOOP FROM BACK(st,end,moveby) n then moving FIRST
    for seg in range(len(wturtle)-1,0,-1):
        new_x=wturtle[seg-1].xcor()
        new_y=wturtle[seg-1].ycor()
        wturtle[seg].goto(new_x,new_y)

    wturtle[0].fd(20)
    wturtle[0].left(90)

screen.onkey(u,"Up")
screen.onkey(d,"Down")
screen.listen()


screen.exitonclick()