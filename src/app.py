import pygame


class App:
  def __init__(self, screen_width: int, screen_height: int, app_name: str, fps: int) -> None:
    self.SCREEN_WIDTH = screen_width
    self.SCREEN_HEIGHT = screen_height
    self.APP_NAME = app_name
    self.FPS = fps
    self.clock = pygame.time.Clock()
    self.delta_time = 0
    self.running = True
    self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    pygame.display.set_caption(self.APP_NAME)
  
  def run(self) -> None:
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
      
      # update the entire screen      
      pygame.display.flip()

      # update latest delta time
      self.delta_time = self.clock.tick(self.FPS) / 1000

    pygame.quit()