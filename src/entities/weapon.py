from pygame import Vector2, Surface, mouse
from pygame.draw import line


class Weapon():
  def __init__(self, position: Vector2) -> None:
    self.__position = position
    self.__length = 50
  
  
  def draw(self, screen: Surface) -> None:
    LINE_COUNT = 5
    SEPARATION_ANGLE = 20
    loop_start = -2
    target_vec = (self.__length * self.__get_look_at_direction())
    
    for i in range(LINE_COUNT):
      line(
        screen,
        (255, 255, 255),
        self.__position,
        self.__position + target_vec.rotate((loop_start + i) * SEPARATION_ANGLE)
      )
  
  
  def update(self, new_position: Vector2) -> None:
    self.__position = new_position


  def __get_look_at_direction(self) -> Vector2:
    return (mouse.get_pos() - self.__position).normalize()
