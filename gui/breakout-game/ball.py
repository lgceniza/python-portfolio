from turtle import Turtle
import random


SPEEDS = [0.7,1,1.2]

class Ball(Turtle):
  def __init__(self, pos):
    super().__init__()
    self.shape('circle')
    self.color('white')
    self.penup()
    self.starting_pos = pos
    self.goto(self.starting_pos)

    self.x_move = 15
    self.y_move = 15

  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() - self.y_move

    self.goto(new_x, new_y)

  def bounce(self):
    self.x_move *= random.choice(SPEEDS)
    self.y_move *= -1

  def wall_bounce(self):
    self.x_move *= -1
    self.y_move *= random.choice(SPEEDS)

  def reset_position(self):
    self.goto(self.starting_pos)
    self.wall_bounce()
