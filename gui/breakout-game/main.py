import time
import random
from turtle import *
from paddle import Paddle
from ball import Ball
from brick import BrickManager
from scoreboard import Scoreboard

STARTING_POSITION_PADDLE = (0, -250)
STARTING_POSITION_BALL = (0, -200)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('BREAKOUT')

screen.tracer(0)
paddle = Paddle(STARTING_POSITION_PADDLE)
ball = Ball(STARTING_POSITION_BALL)
brickManager = BrickManager()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(paddle.goRight, 'Right')
screen.onkey(paddle.goLeft, 'Left')
screen.onkey(bye, 'Escape')

game_loop = True
while game_loop:
  time.sleep(0.1)
  screen.update()
  ball.move()

  x = ball.xcor()
  y = ball.ycor()

  if x > 370 or x < -370:
    ball.wall_bounce()
  
  if (y < -225 and ball.distance(paddle) < 50) or y > 260:
    ball.bounce()
  
  if y < -280:
    ball.reset_position()
  
  for brick in brickManager.bricks:
    if ball.distance(brick) < 48 and brick.is_visible():
      brick.turn_invisible()
      ball.wall_bounce()
      scoreboard.add_point()

      if brickManager.is_all_invisible():
        game_loop = False
        scoreboard.game_over()

      if random.randint(0,1):
        ball.bounce()

screen.exitonclick()
