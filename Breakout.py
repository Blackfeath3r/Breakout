import turtle
from blocks import BlockManager
from ball import Ball
import time
from board import Board, Score

screen = turtle.Screen()
screen.tracer(0)
screen.setup(width=1000, height=600)

screen.listen()
board = Board()
block_manager = BlockManager()
block_manager.block_generator()
ball = Ball()
score = Score()
screen.update()
screen.onkeypress(board.move_right, 'Right')
screen.onkeypress(board.move_left, 'Left')

game = True

while game:
    time.sleep(0.001)
    screen.update()
    ball.move()
    if ball.ycor() > 290:
        ball.bounce_y()
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()
    if ball.ycor() < -250:
        pass
    elif ball.distance(board) < 80 and ball.ycor() < -230:
        ball.bounce_y()
    for block in block_manager.blocks:
        if ball.ycor() > block.ycor() - 4 and ball.distance(block) < 31:
            ball.bounce_x()
            block.color('white')
            block_manager.blocks.remove(block)
            score.score += 10
            score.clear()
            score.display()
            score.live()
        elif ball.ycor() > block.ycor() - 21 and ball.distance(block) < 31:
            ball.bounce_y()
            block.color('white')
            block_manager.blocks.remove(block)
            score.score += 10
            score.clear()
            score.display()
            score.live()
    if ball.ycor() < -300:
        score.lives -= 1
        score.clear()
        score.display()
        score.live()
        ball.reset()

    if score.lives == 0:
        game = False



if not game:
    screen.clear()
    score.goto(-100, 0)
    score.write(f'Game Over', font=('courier', 25, 'normal'))

screen.exitonclick()
