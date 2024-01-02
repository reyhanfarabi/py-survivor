from src.app import App


def main() -> None:
  app = App(800, 600, 'Py Survivor', 60)
  
  try:
    app.run()
  except:
    raise ValueError('Unable to start application')


if __name__ == '__main__':
  main()