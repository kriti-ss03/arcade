from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball   
from scoreboard import Score
import time 
# to show ball move step by step

score=Score()

screen =Screen()
screen.screensize(600, 800) 
screen.bgcolor("black")
# close animation->tracer
screen.tracer(0)
screen.title("PINGpPONG")

r= Paddle()
r.place(350,0)
l=Paddle()
l.place(-350,0)
ball=Ball()


screen.listen()
# left n right paddle movt keys
screen.onkey(r.moveup,"Up")
screen.onkey(r.movedown,"Down")
screen.onkey(l.moveup,"w")
screen.onkey(l.movedown,"s")

isgameon= True
while isgameon==True:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # for top n bottom screen cond
    if ball.ycor()>=290 or ball.ycor()<=-290:
        ball.reflecty()
    
    # Collison of ball n paddle -paddle n ball dist<20 then contact but for center only
    # to resolve this 2 condn-
    if ball.distance(r)<50 and ball.xcor()>330:
        ball.reflectx()
         
    # LEFT PADDLE COLLSN-
    if ball.distance(l)<50 and ball.xcor()<-330:
        ball.reflectx()
      
    # missed by left
    if ball.xcor()>350:
        ball.reset_ball()
        score.r_point()
    
    # missed by right
    if ball.xcor()<-350:
        ball.reset_ball()
        score.l_point()

   
screen.exitonclick()
