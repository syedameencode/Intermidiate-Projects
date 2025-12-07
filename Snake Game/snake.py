class Snake:
    MOVE_DISTANCE = 20
    STARTING = [(0, 0), (-20, 0), (-40, 0)]
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        # Create a Snake body. Each segment is 20x20 pixels.
        import turtle as t
        
        for pos in self.STARTING:
            self.add_body(pos)
    
    def add_body(self, pos):
        import turtle as t
        new_body= t.Turtle(shape="square")
        new_body.penup()
        
        new_body.color("black")
        new_body.goto(pos)
        self.snake_body.append(new_body)

    def extend(self):
        self.add_body(self.snake_body[-1].position())
        


    def move(self):
        # Move each segment to the position of the previous segment
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        # Move head forward by one segment distance
        self.head.forward(self.MOVE_DISTANCE)

    def up(self):
        # Prevent moving directly opposite to current heading
        if self.head.heading() != 270:
            #if snake pointing down then it should not go up
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)