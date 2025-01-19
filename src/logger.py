import logging
from datetime import datetime
from colorama import init, Fore, Style

def get_logger(name):
  """
  Initializes and returns a Python logger with colored output.

  Args:
    name: The name of the logger.

  Returns:
    A configured logger object.
  """
  logger = logging.getLogger(name)
  logger.setLevel(logging.DEBUG)

  # Initialize colorama for Windows
  init(autoreset=True)

  # Create a custom formatter
  class ColoredFormatter(logging.Formatter):
    def format(self, record):
      levelname = record.levelname
      if levelname == 'DEBUG':
        color = Fore.BLUE
      elif levelname == 'INFO':
        color = Fore.GREEN
      elif levelname == 'WARNING':
        color = Fore.YELLOW
      elif levelname == 'ERROR':
        color = Fore.RED
      elif levelname == 'CRITICAL':
        color = Fore.MAGENTA
      else:
        color = Fore.WHITE

      record.levelname = color + levelname + Style.RESET_ALL
      return f"[{Fore.WHITE}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}] {record.levelname}: {Style.BRIGHT}{record.msg}{Style.RESET_ALL}"

  formatter = ColoredFormatter("[%(asctime)s] %(levelname)s: %(message)s")

  # Create a console handler
  console_handler = logging.StreamHandler()
  console_handler.setLevel(logging.DEBUG)
  console_handler.setFormatter(formatter)

  # Add the console handler to the logger
  logger.addHandler(console_handler)

  return logger

# Example usage:
if __name__ == "__main__":
  my_logger = get_logger(__name__)
  my_logger.debug("This is a debug message.")
  my_logger.info("This is an info message.")
  my_logger.warning("This is a warning message.")
  my_logger.error("This is an error message.")
  my_logger.critical("This is a critical message.")