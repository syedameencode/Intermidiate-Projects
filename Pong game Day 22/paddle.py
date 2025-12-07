import turtle as t

class Paddle(t.Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        self.goto(pos)

    def go_up(self):
        new_y=self.ycor()+15
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y=self.ycor()-15
        self.goto(self.xcor(),new_y)
    
    