import logging, logging.handlers

def configure_logger():
    # create logger  
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.handlers.TimedRotatingFileHandler(str(__file__).replace('.py','.log'),when='D',interval=2)
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger



logger = configure_logger()
import time
while True:
    logger.info(__file__)
    logger.info(__name__)
    time.sleep(1)
