import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
count = 0

turtle_player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle_player.move,"Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(turtle_player) < 20:
            game_is_on = False


screen.exitonclick()







