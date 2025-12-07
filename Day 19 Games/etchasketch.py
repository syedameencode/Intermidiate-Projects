#Import turtle Graphics
import turtle as t

#Create a screen
tim=t.Turtle()
screen=t.Screen()

#function for moving forward
def move_forward():
    tim.fd(10)

#function for moving backward
def move_backward():
    tim.bk(10)
#function for turning LEFT as counter clockwise
def turn_left():
    tim.left(10)

#function for turning RIGHT as clockwise
def turn_right():
    tim.right(10)
#Funvtion on clearing the screen
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

#Implementations
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")

#Exit on click
screen.exitonclick()

