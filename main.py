from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

game_is_on = True

screen.listen()
screen.onkeypress(fun=l_paddle.up, key="Up")
screen.onkeypress(fun=l_paddle.down, key="Down")
screen.onkeypress(fun=r_paddle.up, key="w")
screen.onkeypress(fun=r_paddle.down, key="s")

def game():
    if game_is_on:
        ball.move()
        screen.update()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
            ball.bounce_x()

        screen.ontimer(fun=game, t=70)


game()
screen.exitonclick()