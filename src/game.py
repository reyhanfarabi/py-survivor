from pygame import Rect, Surface, Vector2

from src.entities.player import Player
from src.entities.stats import Stats
from src.module.enemy_spawner import EnemySpawner
from src.module.sprite import Sprite


class Game():
  def __init__(self) -> None:
    self.player = Player(
      Sprite('assets/hooded_protagonist/spritesheets.png', Rect(0, 0, 32, 32)), 
      Vector2(100, 100),
      Stats(10, 100, 100)
    )
    self.spawner = EnemySpawner(
      Sprite('assets/enemies/slime/slime_idle.png', Rect(0, 0, 32, 32)),
      (1, 10, 20),
      self.player
    )
    
    self.spawner.spawn_with_amount(10)
  
  
  def update(self, dt: float) -> None:
    self.player.update(dt)
    
    self.player.attack_enemies(self.spawner.enemies_container)
    
    # update enemies logic
    for enemy in self.spawner.enemies_container:
      enemy.update(dt)

      # check if enemy is dead
      if not enemy.is_alive:
        self.spawner.enemies_container.remove(enemy)
    
  
  def draw(self, screen: Surface) -> None:
    self.player.draw(screen)

    # draw enemies
    for enemy in self.spawner.enemies_container:
      enemy.draw(screen)
