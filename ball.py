from turtle import Turtle
from time import sleep


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.pace = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Change the direction of the ball vertically"""
        self.y_move *= -1

    def bounce_x(self):
        """Change the direction of the ball horizontally"""
        self.x_move *= -1
        if self.pace > 0:
            self.pace *= 0.9

    def reset_position(self):
        self.home()
        self.pace = 0.1
        self.bounce_x()
        sleep(0.5)
