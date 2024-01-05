from src.entities.enemy import Enemy
from src.entities.player import Player
from src import utils
from .sprite import Sprite


class EnemySpawner():
  def __init__(self, sprite: Sprite, speed: int, player: Player) -> None:
    self.enemies_container = []
    self.sprite = sprite
    self.speed = speed
    self.player = player
  
  
  def spawn(self) -> None:
    e = Enemy(self.sprite, utils.generate_random_location(), self.speed, self.player)
    self.enemies_container.append(e)

  
  def spawn_with_amount(self, amount: int) -> None:
    for _ in range(amount):
      self.spawn()
