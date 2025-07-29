from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(0, 260)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 282)
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 17, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

