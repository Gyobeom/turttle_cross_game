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
scoreboard = Scoreboard()

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
            scoreboard.end_game()
            game_is_on = False


    if turtle_player.ycor() > 280:
        turtle_player.goto(0, -280)
        car_manager.move_increment()
        scoreboard.point()




screen.exitonclick()







