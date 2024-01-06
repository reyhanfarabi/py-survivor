import pygame
import time
from .entity import Entity
from src import constants, utils
from src.module.sprite import Sprite
from src.module.ui.text import Text


class Player(Entity):
  def __init__(self, sprite: Sprite, position: pygame.Vector2, speed: int) -> None:
    super().__init__(sprite, position, speed)
    
    # player hud attribute
    self.text_health = Text(f"HP  {str(self.health)}", 18, (80, 40))
  
    # temporary attribute to test reduce health
    self.delay = time.time() + 2

  
  def update(self, dt: float):
    self.movement(dt)
    
    # temporary test reduce health (will be deleted later)
    if utils.is_collided(self.position, self.sprite.rect_size, pygame.Vector2(100, 100), (32, 32)):
      if time.time() > self.delay:
        self.health -= 5
        self.delay = time.time() + 2
        print(self.health)
    
    self.text_health.string = f"HP  {str(self.health)}"
  
  
  def draw(self, screen: pygame.Surface) -> None:
    screen.blit(self.sprite.image, (self.position.x, self.position.y), self.sprite.image_at)
    
    # player hud
    self.text_health.draw(screen)
  
  
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
