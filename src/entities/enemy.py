from pygame import Surface, Vector2
from .entity import Entity
from .player import Player
from src import utils
from src.components.sprite import Sprite


class Enemy(Entity):
  def __init__(self, sprite: Sprite, position: Vector2, speed: int, player: Player) -> None:
    super().__init__(sprite, position, speed)
    self.player = player
    self.target_distance_padding = 0.2
  
  
  def update(self, dt: float) -> None:
    self.move_to_player(dt, self.player.position)
  
  
  def draw(self, screen: Surface) -> None:
    screen.blit(self.sprite.image, (self.position.x, self.position.y), self.sprite.image_at)


  def move_to_player(self, dt: float, player_pos: Vector2) -> None:
    direction = (player_pos - self.position).normalize()

    if utils.get_distance_between_vector(self.position, player_pos) > self.target_distance_padding:
      self.position += direction * self.speed * dt
