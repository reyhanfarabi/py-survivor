class Stats():
  def __init__(self, attack: int, health: int, speed: int) -> None:
    self.__attack = attack
    self.__health = health
    self.__speed = speed
  
  
  def get_attack(self) -> int:
    return self.__attack

  
  def get_health(self) -> int:
    return self.__health

  
  def reduce_health(self, amount: int) -> None:
    self.__health -= amount

  
  def get_speed(self) -> int:
    return self.__speed
