from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))

game_is_on = True

screen.listen()
screen.onkeypress(fun=l_paddle.up, key="Up")
screen.onkeypress(fun=l_paddle.down, key="Down")
screen.onkeypress(fun=r_paddle.up, key="w")
screen.onkeypress(fun=r_paddle.down, key="s")


while game_is_on:
    screen.update()

screen.exitonclick()