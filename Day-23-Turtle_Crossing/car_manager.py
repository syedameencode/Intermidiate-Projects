COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import turtle as t
import random

class CarManager:
    def __init__(self):
        # store active cars and current move distance
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE


    def create_car(self):
        # Create a new car occasionally (so we don't spawn every frame)
        if random.randint(1, 6) != 1:
            return

        new_car = t.Turtle("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        random_color = random.choice(COLORS)
        new_car.color(random_color)
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.cars.append(new_car)
    
    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
            
    
