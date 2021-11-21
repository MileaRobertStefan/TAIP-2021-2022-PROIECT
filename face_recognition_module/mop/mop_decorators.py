import functools
import logging
import os.path

monitoring_logger = 0
event_stack = []


def load():
    global monitoring_logger
    if monitoring_logger == 0:
        logging.basicConfig(filename="monitoring.txt", level=logging.DEBUG)
        monitoring_logger = 1


load()


def requires_file_created_before(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        path = args[0]
        try:
            assert os.path.exists(path)
        except:
            logger = logging.getLogger('{0}-{1}'.format(func.__qualname__, func.__name__))
            logger.error("File not saved")
            raise Exception("File not saved")

        return func(*args, **kwargs)

    return wrapper


def requires_file_deleted_after(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        path = args[0]
        try:
            assert os.path.exists(path) is not True
        except:
            logger = logging.getLogger('{0}-{1}'.format(func.__qualname__, func.__name__))
            logger.warning("File not deleted")
        return result

    return wrapper


def requires_called_before(event_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                assert event_stack[len(event_stack) - 1]["name"] == event_name
            except:
                logger = logging.getLogger('{0}-{1}'.format(func.__qualname__, func.__name__))
                logger.warning("Event " + event_name + " was not called before")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def requires_calls(event_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                assert event_stack[len(event_stack) - 1]["name"] == event_name
            except:
                logger = logging.getLogger('{0}-{1}'.format(func.__qualname__, func.__name__))
                logger.warning("Event " + event_name + " was not called during method execution")

            return result

        return wrapper

    return decorator


def event(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        event_stack.append({"name": func.__name__, "args": args, "kwargs": kwargs})
        print(event_stack)
        return func(*args, **kwargs)

    return wrapper
