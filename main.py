from src.app import App
from src import constants


def main() -> None:
  app = App(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.APP_NAME, constants.FPS)
  
  try:
    app.run()
  except:
    raise ValueError('Unable to start application')


if __name__ == '__main__':
  main()
