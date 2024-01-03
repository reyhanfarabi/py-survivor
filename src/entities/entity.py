from pygame import Surface, Vector2
from abc import ABC, abstractmethod
from src.components.sprite import Sprite


class Entity(ABC):
  def __init__(self, sprite: Sprite, position: Vector2, speed: int) -> None:
    super().__init__()
    self.sprite = sprite
    self.position = position
    self.speed = speed
  
  
  @abstractmethod
  def update(self, dt: float) -> None:
    pass
  
  
  @abstractmethod
  def draw(self, screen: Surface) -> None:
    pass
