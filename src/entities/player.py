import pygame
import time

from .entity import Entity
from .stats import Stats
from .weapon import Weapon
from src import constants
from src.module.sprite import Sprite
from src.module.ui.text import Text


class Player(Entity):
  def __init__(self, sprite: Sprite, position: pygame.Vector2, stats: Stats) -> None:
    super().__init__(sprite, position, stats)
    self.__ATACK_DELAY = 1
    self.__attack_delay_counter = time.time() + self.__ATACK_DELAY
    self.__weapon = Weapon(self.get_player_center_pos())
    
    # player hud attribute
    self.text_health = Text(f"HP  {str(self.stats.get_health())}", 18, (80, 40))

  
  def update(self, dt: float):
    self.movement(dt)    
    self.__weapon.update(self.get_player_center_pos())
  
  
  def draw(self, screen: pygame.Surface) -> None:
    screen.blit(self.sprite.image, (self.position.x, self.position.y), self.sprite.image_at)
    
    # player hud
    self.text_health.string = f"HP  {str(self.stats.get_health())}"
    self.text_health.draw(screen)
    
    # player weapon
    self.__weapon.draw(screen)

  
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


  def get_player_center_pos(self) -> pygame.Vector2:
    return pygame.Vector2(
      self.position.x + self.sprite.rect_size[0] / 2, self.position.y + self.sprite.rect_size[1] / 2
    )
  
  
  def attack_enemies(self, enemies: list):
    for enemy in enemies:
        self.attack(enemy)
  
  
  def attack(self, enemy) -> bool:
    if self.__weapon.can_attack(enemy) and time.time() > self.__attack_delay_counter:
      enemy.take_damage(self.stats.get_attack())
      self.__attack_delay_counter = time.time() + self.__ATACK_DELAY


  def reveal_enemies(self, enemies: list) -> None:
    for enemy in enemies:
      if self.__weapon.can_attack(enemy):
        enemy.reveal();