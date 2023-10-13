from turtle import *
import random

colors = ['#AA0000', '#fd5c63', '#D2122E', '#9e1b32', '#E32636', '#E52B50', '#BA0021', '#FF033E', '#FBCEB1', '#EF0107',
          '#660000', '#CC0000']


class Block(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2.3)
        self.color('#AA0000')
        self.goto(x, y)


class BlockManager:
    def __init__(self):
        self.blocks = []
        self.x = -520
        self.y = 80
        self.x_constant = 49
        self.y_constant = 22
        self.gap = 0

    def block_generator(self):
        for y in range(6):
            for i in range(20):
                self.x += self.x_constant

                block = Block(self.x, self.y)
                block.color(random.choice(colors))
                self.blocks.append(block)
            self.x = -520
            self.y += self.y_constant
        self.gap = self.blocks[20].ycor() - self.blocks[0].ycor()
