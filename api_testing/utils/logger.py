import logging
import logging.handlers
import os

path = os.path.join(os.path.dirname(__file__), '..', 'utils', 'logs', 'logger.log')


def setup_logging(name):
    logger = logging.getLogger(name)
    msg_format = '%(asctime)s %(name)s %(levelname)s %(message)s'
    logger.setLevel(logging.DEBUG)
    file_handler = logging.handlers.RotatingFileHandler(path, "a", 2048, 10)
    file_handler.setFormatter(logging.Formatter(msg_format))
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)


setup_logging("api_testing")


