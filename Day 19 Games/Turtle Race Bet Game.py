#Import turtle and random module
import turtle as t
import random

#Create a screen
screen=t.Screen()
#Dimentions of the screen
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win").lower()

#Positioning and Color of the turtle
colors=["red","orange","yellow","green","blue","purple"]
y=[-70,-40,-10,20,50,80]
all_turtles=[]

#Creating a multiple turtles
for i in range(5):
    timmy=t.Turtle()
    timmy.color(colors[i])
    timmy.penup()
    timmy.shape("turtle")
    timmy.goto(x=-230,y=y[i])
    all_turtles.append(timmy)

#Random Movement of the turtle
is_race_on=False # Race is off
if user_bet:
    is_race_on=True
while is_race_on: #Race is on
    for i in all_turtles:
        #Stop the game
        if i.xcor()>230:
            is_race_on=False
            winning_color=i.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance=random.randint(0,10)
        i.fd(random_distance)#Race Goes on

screen.exitonclick()

