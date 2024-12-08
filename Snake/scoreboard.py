from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.start_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.start_score}", align= ALIGNMENT, font = FONT)
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.start_score += 1
        self.write(f"Score: {self.start_score}", align=ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font = FONT)
