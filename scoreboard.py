from turtle import Turtle
FONT = ('Courier', 50, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.draw_line()

    def draw_line(self):
        self.goto(x=0, y=-280)
        self.setheading(90)
        self.pensize(5)
        for _ in range(28):
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)

    def print_score(self, score):
        self.clear()
        self.write(f"{score}", align='center', font=FONT)


