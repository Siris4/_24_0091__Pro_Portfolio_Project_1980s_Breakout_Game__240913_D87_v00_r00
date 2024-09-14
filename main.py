# main.py
from turtle import Screen
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard
import time

# Constants
INITIAL_PADDLE_WIDTH = 16
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_ROWS = 5
BLOCKS_PER_ROW = 30
PADDLE_SHRINK_RATE = 0.95
BALL_SPEED_INCREASE_RATE = 1.05
COLORS = ['purple', 'blue', 'green', 'yellow', 'red']
SCORES = [100, 200, 400, 800, 1000]

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.title("Breakout by Siris")

# Paddle setup
paddle = Paddle((0, -250), INITIAL_PADDLE_WIDTH)

# Ball setup
ball = Ball()

# Block setup (5 rows x 30 blocks)
blocks = []
for row in range(BLOCK_ROWS):
    row_color = COLORS[row]
    row_score = SCORES[row]
    y_position = 200 - row * 20  # Adjust the vertical spacing of rows
    for col in range(BLOCKS_PER_ROW):
        x_position = -350 + col * 24  # Adjust horizontal spacing of blocks
        block = Block((x_position, y_position), row_color, row_score)
        blocks.append(block)

# Scoreboard setup
scoreboard = Scoreboard()

# Control paddle with keys
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

# Game loop
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290:
        ball.bounce_off_y_vertical_walls()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() > -240:
        ball.bounce_off_paddle()
        ball.move_speed *= BALL_SPEED_INCREASE_RATE

    # Detect collision with blocks
    for block in blocks:
        if ball.distance(block) < 20:
            block.break_block()
            blocks.remove(block)
            ball.bounce_off_y_vertical_walls()
            scoreboard.add_score(block.points)
            break

    # Detect when the ball goes out of bounds
    if ball.ycor() < -290:
        ball.reset_position()
        paddle.shrink()
        ball.move_speed *= BALL_SPEED_INCREASE_RATE

    # End game if all blocks are cleared
    if not blocks:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
