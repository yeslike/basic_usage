import time
import logging
import logging.handlers

def log_setup():
    log_handler = logging.handlers.WatchedFileHandler('my.log')
    formatter = logging.Formatter(
        '%(asctime)s program_name [%(process)d]: %(message)s',
        '%b %d %H:%M:%S')
    formatter.converter = time.gmtime  # if you want UTC time
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)


log_setup()
logging.info('Hello, World!')
import os
os.rename('my.log', 'my.log-old')
logging.info('Hi, New log!')

