import turtle as t
class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("red")
        self.penup()
        self.goto(0,-280)
        self.hideturtle()
        self.new_scoreboard()
    
    def new_scoreboard(self):
        self.write(f"Score:{self.score}",align="center",font=("Times New Roman",24,"bold"))
       
    def score_increase(self):
        self.score+=1
        self.clear()
        self.new_scoreboard()