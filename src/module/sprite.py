from pygame import image, Rect


class Sprite():
  def __init__(self, image_path: str, rect: Rect) -> None:
    self.image = image.load(image_path).convert_alpha()
    self.image_at = rect
    self.rect_size = self.image_at.size  
