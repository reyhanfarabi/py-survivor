from pygame import Rect, Surface, Vector2
from .entities.player import Player


class Game():
  def __init__(self) -> None:
    self.player = Player('assets\hooded_protagonist\spritesheets.png', Rect(0, 0, 32, 32), Vector2(100, 100), 100)
  
  
  def update(self, dt: int) -> None:
    self.player.update(dt)
  
  
  def draw(self, screen: Surface) -> None:
    self.player.draw(screen)
