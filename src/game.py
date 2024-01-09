from pygame import Rect, Surface, Vector2

from src.entities.player import Player
from src.entities.stats import Stats
from src.module.enemy_spawner import EnemySpawner
from src.module.sprite import Sprite
from src.module.ui.text import Text
from src.constants import *


class Game():
  def __init__(self) -> None:
    self.__kill_count = 0
    self.__enemy_wave = 0
     
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
    
    self.spawn_enemy_wave()
    
    # ui attributes
    self.__text_kill_count = Text(f"Kill Count  {str(self.__kill_count)}", 18, (1470, 40))
    self.__text_enemy_wave = Text(f"Wave {str(self.__enemy_wave)}", 18, (750, 40))
  
  
  def update(self, dt: float) -> None:
    self.player.update(dt)
    
    self.player.attack_enemies(self.spawner.enemies_container)
    
    # check if all enemy is dead
    if not self.spawner.enemies_container:
      self.spawn_enemy_wave()
    
    # update enemies logic
    for enemy in self.spawner.enemies_container:
      enemy.update(dt)

      # check if enemy is dead
      if not enemy.is_alive:
        self.spawner.enemies_container.remove(enemy)
        self.__kill_count += 1

    self.__text_kill_count.string = f"Kill Count  {str(self.__kill_count)}"
    self.__text_enemy_wave.string = f"Wave {str(self.__enemy_wave)}"
    
  
  def draw(self, screen: Surface) -> None:
    self.player.draw(screen)

    # draw enemies
    for enemy in self.spawner.enemies_container:
      enemy.draw(screen)
  
    # draw ui
    self.__text_kill_count.draw(screen)
    self.__text_enemy_wave.draw(screen)


  def spawn_enemy_wave(self) -> None:
    self.__enemy_wave += 1
    self.spawner.spawn_with_amount(10)
