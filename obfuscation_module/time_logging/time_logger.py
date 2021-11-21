import functools
import logging
import time

from datetime import date

obfuscation_module_logger_status = 0
obfuscation_function_time_limit = 1


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


def monitor_obfuscation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        input_image = args[1].copy()
        start_date = date.today()
        start_time = time.time()
        logger = logging.getLogger('{0}-{1}'.format(func.__qualname__, func.__name__))

        func(*args, **kwargs)

        elapsed = time.time() - start_time
        logger.info('- start date: {0} , elapsed: {1}'.format(start_date, elapsed))
        if elapsed > obfuscation_function_time_limit:
            logger.warning('Warning! This function\'s execution exceeded the time limit of {0} second(s)!'
                           .format(obfuscation_function_time_limit))

        output_image = args[1]
        print(input_image.shape == output_image.shape)

    return wrapper
