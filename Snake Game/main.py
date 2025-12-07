import turtle as t
import time
import snake as s
import food as f
import Scoreboard as sb

# Set up the screen
screen=t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("White")
screen.title("Snake Game")
screen.tracer(0)

snake=s.Snake()
#Init food
food=f.Food()
#Init Scoreboard
scoreboard=sb.Scoreboard()
#Inserting keystrokes
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


#Snake Movement Lookin good:
"""use tracer and update method of screen to control the animation of the snake movement"""

#Move the snake
gameon=True
while gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    #Distance function of turtle class
    if snake.head.distance(food)<15:
        food.new_food()
        snake.extend()
        scoreboard.score_increase()
    #Detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        gameon=False
        scoreboard.goto(0,0)
        scoreboard.write("GAME OVER",align="center",font=("Times New Roman",30,"bold"))
    #Detect collision with tail  
    # if head collison with any body in tail  
    for snake_body in snake.snake_body[1:]:
        if snake.head.distance(snake_body)<10:
            gameon=False
            scoreboard.goto(0,0)
            scoreboard.write("GAME OVER",align="center",font=("Times New Roman",30,"bold"))
screen.exitonclick()