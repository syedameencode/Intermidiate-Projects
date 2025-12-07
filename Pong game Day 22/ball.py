import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove
        self.goto(new_x,new_y)

    def bounce_x(self):
        # Reverse X direction and slightly increase speed (make sleep smaller)
        self.xmove *= -1
        # decrease move_speed slightly so the main loop sleeps less -> game speeds up
        self.move_speed *= 0.9
    def bounce_y(self):
        self.ymove*=-1

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed=0.1