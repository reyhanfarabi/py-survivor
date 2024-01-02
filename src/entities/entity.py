from pygame import Rect, Surface, Vector2
from abc import ABC, abstractmethod
from src.components.sprite import Sprite


class Entity(ABC):
  def __init__(self, sprite_path: str, sprite_at: Rect, position: Vector2, speed: int) -> None:
    super().__init__()
    self.sprite = Sprite(sprite_path, sprite_at)
    self.position = position
    self.speed = speed
  
  
  @abstractmethod
  def update(self, dt: float) -> None:
    pass
  
  
  @abstractmethod
  def draw(self, screen: Surface) -> None:
    pass
