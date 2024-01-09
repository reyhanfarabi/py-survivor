from pygame import Vector2, Rect
import math
import random
from .constants import *


def get_distance_between_vector(origin_position: Vector2, position: Vector2) -> float:
  return math.sqrt((origin_position.x - position.x) ** 2 + (origin_position.y - position.y) ** 2)


def is_collided(origin_position: Vector2, origin_size: tuple, target_position: Vector2, target_size: tuple) -> bool:
  origin_center_pos = Vector2(origin_position.x + origin_size[0] / 2, origin_position.y + origin_size[1] / 2)
  
  return (
    origin_center_pos.x >= target_position.x and
    origin_center_pos.x <= target_position.x + target_size[0] and
    origin_center_pos.y >= target_position.y and
    origin_center_pos.y <= target_position.y + target_size[1]
  )


# this function will generate a random location within the game area as a Vector2
def generate_random_location() -> Vector2:
  x = random.randrange(0, SCREEN_WIDTH)
  y = random.randrange(0, SCREEN_HEIGHT)
  return Vector2(x, y)


def get_list_index_from_2d_list(x_index: int, x_length: int, y_index: int) -> int:
  return x_index * x_length + y_index


def is_vec_collide_with_rect(origin_vec: Vector2, target_rect: Rect) -> bool:
  return (
    origin_vec.x >= target_rect.x and
    origin_vec.x <= target_rect.x + target_rect.width and
    origin_vec.y >= target_rect.y and
    origin_vec.y <= target_rect.y + target_rect.height
  )