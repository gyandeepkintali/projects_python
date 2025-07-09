from turtle import Turtle, Screen
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.speed = STARTING_MOVE_DISTANCE
        self.reset_position()

    def move(self):
        self.backward(self.speed)

    def reset_position(self):
        self.goto(300, random.randint(-250, 250))

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.reset_position()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.bgcolor("black")

player = Player()
cars = []
score = 0

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
car_creation_counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_creation_counter += 1
    if car_creation_counter % 6 == 0:
        cars.append(Car())
    
    for car in cars:
        car.move()
        
        if car.distance(player) < 20:
            game_is_on = False
            
    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        score += 1
        for car in cars:
            car.speed += MOVE_INCREMENT

    cars = [car for car in cars if car.xcor() > -320]

game_over = Turtle()
game_over.hideturtle()
game_over.color("white")
game_over.write(f"GAME OVER! Score: {score}", align="center", font=("Arial", 24, "normal"))

screen.exitonclick()