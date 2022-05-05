from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=6)
        self.setposition(position)

    def up(self):
        if self.ycor() < 230:
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > -230:
            self.sety(self.ycor() - 20)


