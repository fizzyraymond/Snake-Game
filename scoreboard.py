from turtle import Turtle
Alignment = "center"
Font = ("Arial", 24, "normal")
#create constants for the font and alignment of the scoreboard

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=Alignment, font=Font)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=Alignment, font=Font)

