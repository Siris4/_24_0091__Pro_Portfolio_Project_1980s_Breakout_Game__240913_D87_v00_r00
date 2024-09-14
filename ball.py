# ball.py
from turtle import Turtle

# Constants
BALL_INITIAL_SPEED = 0.1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed = BALL_INITIAL_SPEED
        self.x_move = 10
        self.y_move = 10
        self.move_speed = BALL_INITIAL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_off_y_vertical_walls(self):
        self.y_move *= -1

    def bounce_off_x_walls(self):
        self.x_move *= -1

    def bounce_off_paddle(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, -250)
        self.move_speed = BALL_INITIAL_SPEED
        self.bounce_off_paddle()
