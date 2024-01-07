from pygame import Surface, Vector2
from abc import ABC, abstractmethod

from .stats import Stats
from src.module.sprite import Sprite


class Entity(ABC):
  def __init__(self, sprite: Sprite, position: Vector2, stats: Stats) -> None:
    super().__init__()
    self.sprite = sprite
    self.position = position
    self.stats = stats
  
  
  @abstractmethod
  def update(self, dt: float) -> None:
    pass
  
  
  @abstractmethod
  def draw(self, screen: Surface) -> None:
    pass
