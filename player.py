from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self .shape("turtle")
        self.color("black")
        self.penup()
        self.goto(x = 0, y = -280)
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(0, -280)





