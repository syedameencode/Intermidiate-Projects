FONT = ("Courier", 24, "normal")
import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write(f"Score: {self.score}", align="center", font=FONT)
    def increase_level(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
        

    
