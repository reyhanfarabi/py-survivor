from pygame import Vector2, Surface, Rect, mouse
from pygame.draw import circle
from src import utils


class Weapon():
  def __init__(self, position: Vector2) -> None:
    self.__LINE_COUNT = 9
    self.__DOTS_PER_LINE = 9
    self.__SEPARATION_ANGLE = 10
    self.__ANGLE_START_OFFSET = -(self.__LINE_COUNT // 2)
    self.__RANGE = 100
    self.__position = position
    self.__dots_vecs = [Vector2() for _ in range(self.__LINE_COUNT * self.__DOTS_PER_LINE)]
  
  
  def draw(self, screen: Surface) -> None:
    target_vec = (self.__RANGE * self.__get_look_at_direction())
    
    for line_index in range(self.__LINE_COUNT): 
      for dots_index in range(self.__DOTS_PER_LINE):
        index = utils.get_list_index_from_2d_list(dots_index, self.__DOTS_PER_LINE, line_index)
        target_dot_vec = (target_vec * (dots_index / self.__DOTS_PER_LINE))
        
        self.__dots_vecs[index] = Vector2(
          self.__position + target_dot_vec.rotate((self.__ANGLE_START_OFFSET + line_index) * self.__SEPARATION_ANGLE)
        )
        
        circle(
          screen,
          (255, 255, 255),
          self.__dots_vecs[index],
          1
        )
  
  
  def update(self, new_position: Vector2) -> None:
    self.__position = new_position


  def can_attack(self, target) -> None:
    target_rect = Rect(target.position.x, target.position.y, target.sprite.rect_size[0], target.sprite.rect_size[1])
    is_collided = [utils.is_vec_collide_with_rect(dots, target_rect) for dots in self.__dots_vecs]
    
    return any(is_collided)


  def __get_look_at_direction(self) -> Vector2:
    return (mouse.get_pos() - self.__position).normalize()
