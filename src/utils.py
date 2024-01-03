from pygame import Vector2
import math


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
