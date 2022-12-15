from turtle import Turtle

BRICK_ROWS = 6
NUMBER_OF_BRICKS = 9*BRICK_ROWS
X_INC = 86
HALF_X_INC = X_INC // 2
Y_DEC = 50

class Brick(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('square')
    self.color('white')
    self.shapesize(2,3.8)
    self.penup()
    self.visible = True

  def is_visible(self):
    return self.visible

  def turn_invisible(self):
    self.hideturtle()
    self.visible = False

class BrickManager(Turtle):
  def __init__(self):
    super().__init__()
    self.bricks = [Brick() for _ in range(NUMBER_OF_BRICKS)]
    self.place_bricks()
  
  def place_bricks(self):
    def is_odd(n):
      return True if i^1==i-1 else False
    x = -348
    y = 230
    pos = [x, y]
    for i in range(BRICK_ROWS):
      for j in range(NUMBER_OF_BRICKS//BRICK_ROWS):
        index = (i*(NUMBER_OF_BRICKS//BRICK_ROWS))+j
        if is_odd(i) and j+1 == NUMBER_OF_BRICKS//BRICK_ROWS:
          self.bricks[index].turn_invisible()
          continue
        self.bricks[index].goto(*pos)
        pos[0] += X_INC
      pos[0] = (x + HALF_X_INC) if not is_odd(i) else x
      pos[1] -= Y_DEC

  def is_all_invisible(self):
    return list(map(lambda brick: not brick.is_visible(), self.bricks)).count(True) == NUMBER_OF_BRICKS
