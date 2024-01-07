import pygame

from .entity import Entity
from .stats import Stats
from src import constants
from src.module.sprite import Sprite
from src.module.ui.text import Text


class Player(Entity):
  def __init__(self, sprite: Sprite, position: pygame.Vector2, stats: Stats) -> None:
    super().__init__(sprite, position, stats)
    
    # player hud attribute
    self.text_health = Text(f"HP  {str(self.stats.get_health())}", 18, (80, 40))

  
  def update(self, dt: float):
    self.movement(dt)
  
  
  def draw(self, screen: pygame.Surface) -> None:
    screen.blit(self.sprite.image, (self.position.x, self.position.y), self.sprite.image_at)
    
    # player hud
    self.text_health.string = f"HP  {str(self.stats.get_health())}"
    self.text_health.draw(screen)
  
  
  def movement(self, dt: float) -> None:
    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.position.y > 0:
      self.position.y -= self.stats.get_speed() * dt
    
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.position.y < constants.SCREEN_HEIGHT - self.sprite.image_at.width:
      self.position.y += self.stats.get_speed() * dt
    
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.position.x > 0:
      self.position.x -= self.stats.get_speed() * dt
    
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and self.position.x < constants.SCREEN_WIDTH - self.sprite.image_at.width:
      self.position.x += self.stats.get_speed() * dt


  def take_damage(self, damage_amount: int) -> None:
    if self.stats.get_health() > 0:
      self.stats.reduce_health(damage_amount)
