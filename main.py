import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Game")
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")



game_is_on = True
while game_is_on:
    finish_line_y = 280
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect successful crossing
    if player.ycor() > finish_line_y:
        player.goto(0, -280)
        car_manager.increase_speed()
        scoreboard.increase_level()








screen.exitonclick()