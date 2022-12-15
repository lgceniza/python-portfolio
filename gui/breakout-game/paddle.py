from turtle import Turtle


class Paddle(Turtle):
  def __init__(self, pos):
    super().__init__()
    self.shape('square')
    self.color('white')
    self.shapesize(0.5,6)
    self.penup()
    self.goto(pos)
  
  def goLeft(self):
    new_x = self.xcor() - 30
    self.goto(new_x, self.ycor())

  def goRight(self):
    new_x = self.xcor() + 30
    self.goto(new_x, self.ycor())
