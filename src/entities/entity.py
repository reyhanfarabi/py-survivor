from pygame import Surface, Vector2
from abc import ABC, abstractmethod
from src.module.sprite import Sprite


class Entity(ABC):
  def __init__(self, sprite: Sprite, position: Vector2, speed: int, attack: int) -> None:
    super().__init__()
    self.sprite = sprite
    self.position = position
    
    # stats
    self.speed = speed
    self.health = 100
    self.attack = attack
  
  
  @abstractmethod
  def update(self, dt: float) -> None:
    pass
  
  
  @abstractmethod
  def draw(self, screen: Surface) -> None:
    pass
