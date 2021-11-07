import time

import logging
from aop import Aspect


class InvocationLoggerAspect(Aspect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger('python-aop')
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler('time.log')
        fh.setLevel(logging.DEBUG)

        self.logger.addHandler(fh)
        self.time = None

    def before(self, *args, **kwargs):
        self.time = time.time()

    def after(self, *args, **kwargs):
        self.logger.info(
            'Invocation: name=%s, time=%s' % (
                self.function,
                str(time.time() - self.time)
            )
        )