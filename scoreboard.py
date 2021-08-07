from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

with open("high_score.txt") as file:
    contents = int(file.read())


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = contents
        self.penup()
        self.goto(0, 275)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        if contents > self.high_score:
            self.high_score = contents
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,
                   font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        if self.high_score > contents:
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
