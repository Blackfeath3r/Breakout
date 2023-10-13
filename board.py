import turtle

MOVE_DISTANCE = 20


class Board(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=6, stretch_wid=0.6)
        self.goto(0, -250)

    def move_right(self):
        if self.xcor() > 420:
            pass
        else:
            self.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.xcor() < -430:
            pass
        else:
            self.backward(MOVE_DISTANCE)


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.score = 0
        self.display()
        self.lives = 3
        self.live()

    def display(self):
        self.goto(-450, 250)
        self.write(f'Score: {self.score}', font=('courier', 25, 'normal'))

    def live(self):
        self.goto(350, 250)
        self.write(f'Lives: {self.lives}', font=('courier', 20, 'normal'))
