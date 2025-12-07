import turtle as t
import random

class Food(t.Turtle):
    #Inheritance from Turtle class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x,y)