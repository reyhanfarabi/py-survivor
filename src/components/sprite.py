import pygame


class Sprite():
  def __init__(self, image_path: str, rect: pygame.Rect) -> None:
    self.image = pygame.image.load(image_path).convert_alpha()
    self.image_at = rect
  