from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color('white')
    self.penup()
    self.hideturtle()
    self.score = 0

    self.displayScore()

  def displayScore(self):
    self.goto(250, 270)
    self.write(f"Score: {self.score}", align='left', font=FONT)
  
  def add_point(self):
    self.score += 50
    self.clear()
    self.displayScore()

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER!", align='center', font=FONT)
