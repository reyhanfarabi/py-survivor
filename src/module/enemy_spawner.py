from src.entities.enemy import Enemy
from src.entities.player import Player
from src.entities.stats import Stats
from src import utils
from .sprite import Sprite


class EnemySpawner():
  def __init__(self, sprite: Sprite, stats: tuple, player: Player) -> None:
    self.enemies_container = []
    self.sprite = sprite
    self.stats = stats
    self.player = player
  
  
  def spawn(self) -> None:
    e = Enemy(
      self.sprite,
      utils.generate_random_location(),
      Stats(
        self.stats[0],
        self.stats[1],
        self.stats[2]
      ),
      self.player
    )
    
    self.enemies_container.append(e)

  
  def spawn_with_amount(self, amount: int) -> None:
    for _ in range(amount):
      self.spawn()
