import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()
    car_manager.create_car()

    # Detect collision with car
    for car in car_manager.traffic:
        if player.distance(car) < 19:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the player has reached the other side of the road
    if player.ycor() > 275:
        player.next_level()
        scoreboard.increase_level()
        car_manager.increase_car_speed()


screen.exitonclick()
