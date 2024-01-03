from pygame import Rect, Surface, Vector2
from .entities.player import Player
from .entities.enemy import Enemy
from src.components.sprite import Sprite


class Game():
  def __init__(self) -> None:
    self.player = Player(
      Sprite('assets/hooded_protagonist/spritesheets.png', Rect(0, 0, 32, 32)), 
      Vector2(100, 100),
      100
    )
    self.enemy = Enemy(
      Sprite('assets/enemies/slime/slime_idle.png', Rect(0, 0, 32, 32)), 
      Vector2(100, 200), 
      50, 
      self.player
    )
  
  
  def update(self, dt: float) -> None:
    self.player.update(dt)
    self.enemy.update(dt)
  
  
  def draw(self, screen: Surface) -> None:
    self.player.draw(screen)
    self.enemy.draw(screen)
