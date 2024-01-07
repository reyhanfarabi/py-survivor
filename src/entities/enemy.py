from pygame import Surface, Vector2
import time
import random

from src import utils
from src.entities.entity import Entity
from src.entities.stats import Stats
from src.entities.player import Player
from src.module.sprite import Sprite


class Enemy(Entity):
  def __init__(self, sprite: Sprite, position: Vector2, stats: Stats, player: Player) -> None:
    super().__init__(sprite, position, stats)
    self.player = player
    self.target_distance_padding = 0.2
    self.attack_delay = time.time() + 2
    self.speed_rand_factor = 3
    self.new_speed = random.randrange(self.stats.get_speed() - self.speed_rand_factor, self.stats.get_speed() + self.speed_rand_factor)
  
  
  def update(self, dt: float) -> None:
    self.move_to_player(dt, self.player.position)
    self.attack_player()
  
  
  def draw(self, screen: Surface) -> None:
    screen.blit(self.sprite.image, (self.position.x, self.position.y), self.sprite.image_at)


  def move_to_player(self, dt: float, player_pos: Vector2) -> None:
    direction = (player_pos - self.position).normalize()

    if utils.get_distance_between_vector(self.position, player_pos) > self.target_distance_padding:
      self.position += direction * self.new_speed * dt
  
  
  def attack_player(self) -> None:
    if utils.is_collided(self.position, self.sprite.rect_size, self.player.position, self.player.sprite.rect_size):
      if time.time() > self.attack_delay:
        self.player.take_damage(self.stats.get_attack())
        self.attack_delay = time.time() + 2
