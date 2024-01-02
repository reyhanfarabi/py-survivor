import pygame
from .entity import Entity
from src import constants


class Player(Entity):
  def __init__(self, sprite_path: str, sprite_at: pygame.Rect, position: pygame.Vector2, speed: int) -> None:
    super().__init__(sprite_path, sprite_at, position, speed)
  
  
  def update(self, dt: float):
    self.movement(dt)
  
  
  def draw(self, screen: pygame.Surface) -> None:
    screen.blit(self.sprite.image, (self.position.x, self.position.y), self.sprite.image_at)
  
  
  def movement(self, dt: float) -> None:
    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.position.y > 0:
      self.position.y -= self.speed * dt
    
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.position.y < constants.SCREEN_HEIGHT - self.sprite.image_at.width:
      self.position.y += self.speed * dt
    
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.position.x > 0:
      self.position.x -= self.speed * dt
    
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and self.position.x < constants.SCREEN_WIDTH - self.sprite.image_at.width:
      self.position.x += self.speed * dt
