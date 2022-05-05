from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Score
import time

"""Screen Setup"""
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

"""Create and Control two paddles"""
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_score = Score((-100, 200))
r_score = Score((100, 200))
scoreboard = Scoreboard()

screen.listen()
# Control right paddle
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

# Control left paddle
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.pace)
    ball.move()
    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the r_paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) <= 50 or ball.xcor() < -320 and ball.distance(l_paddle) <= 50:
        ball.bounce_x()

    # The R paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        l_paddle.score += 1

    # The L paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        r_paddle.score += 1

    # Keep track of the score
    l_score.print_score(l_paddle.score)
    r_score.print_score(r_paddle.score)


screen.exitonclick()