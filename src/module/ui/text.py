from pygame import font, Surface
from src.constants import *


class Text():
  def __init__(self, string: str,  font_size: int, position: tuple) -> None:
    self.string = string
    self.position = position
    self.font = font.Font(FONT_PATH, font_size)
    self.color = (255, 255, 255)
    self.update()
  
  
  def update(self) -> None:
    self.text = self.font.render(self.string, True, self.color)
    self.text_rect = self.text.get_rect()
    self.text_rect.center = (self.position[0] // 2, self.position[1] // 2)
  
  
  def draw(self, screen: Surface) -> None:
    self.update()    
    screen.blit(self.text, self.text_rect)
