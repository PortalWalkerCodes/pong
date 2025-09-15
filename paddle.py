from turtle import Turtle

X_POS = 350
Y_POS = 0

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        if self.ycor() > 230:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(y=new_y, x=self.xcor())

    def down(self):
        if self.ycor() < -230:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(y=new_y, x=self.xcor())