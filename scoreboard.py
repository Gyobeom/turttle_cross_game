from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230,260)
        self.write("Level: ", align="center", font=FONT)
        self.goto(-170, 260)
        self.write(self.score,align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER ", align="center", font=FONT)

