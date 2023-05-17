from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import random
import time

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")

s = Snake()
food=Food()
score=Score()

# screen.update()
screen.onkey(s.up, "w")
screen.onkey(s.down, "s")
screen.onkey(s.left, "a")
screen.onkey(s.right, "d")

screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")

game_on = True
while game_on:
    # update-> show only once every seg has moved
    screen.update()
    # package to see motion--slows motion,can show movt of head,add of seg if delayed very much
    time.sleep(0.01)
    s.move()
    if s.head.distance(food) < 15:
        # print("chop")
        food.refresh()
        s.extend()
        score.update()
    if s.head.xcor()>300 or s.head.xcor()<-300 or s.head.ycor()>290 or s.head.ycor()<-290:
        game_on=False
        score.game_over()

#     detect colls with head
    for ele in s.wturtle[1:]:
       if s.head.distance(ele) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
