import functools
import logging
import time

from datetime import date
obfuscation_module_logger_status = 0


def load():
    global obfuscation_module_logger_status
    if obfuscation_module_logger_status == 0:
        logging.basicConfig(filename="timelog.txt", level=logging.DEBUG)
        obfuscation_module_logger_status = 1


load()


def time_logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_date = date.today()
        start_time = time.time()
        logger = logging.getLogger('{0}-{1}'.format(func.__qualname__, func.__name__))

        func(*args, **kwargs)

        elapsed = time.time() - start_time
        logger.info('- start date: {0} , elapsed: {1}'.format(start_date, elapsed))
    return wrapper
