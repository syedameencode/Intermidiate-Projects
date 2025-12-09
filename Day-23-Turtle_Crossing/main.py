import time
from turtle import Screen
import player as p
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=p.Player()
Car_manager=CarManager()
Score_board=Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    Car_manager.create_car()
    Car_manager.move_cars()

    #Detect Collision with car
    for car in Car_manager.cars:
        if car.distance(player)<20:
            game_is_on=False
            Score_board.game_over()
            

    #Detect successful crossing
    if player.is_at_finish_line():
        player.back_to_start()
        Car_manager.level_up()
        Score_board.increase_level()


screen.exitonclick()
    
    

