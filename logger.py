import logging


# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a formatter for the log messages
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

# Create a file handler for the log messages
file_handler = logging.FileHandler('log.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Create a console handler for the log messages
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)