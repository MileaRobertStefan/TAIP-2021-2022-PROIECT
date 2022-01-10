import random
from datetime import datetime

import numpy as np
from numpy import ndarray

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
from obfuscation_core.obfuscators.obfuscator import Obfuscator
from time_logging.time_logger import monitor_obfuscation


class AffineObfuscator(Obfuscator):
    def __init__(self):
        super().__init__()
        self.a = 7727
        self.m = 256
        self.b = None

    @monitor_obfuscation
    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        random.seed(datetime.now())
        key_data = int(random.random() * 1000000000)
        np.random.seed(key_data)
        self.b = np.random.randint(0, 256)
        layer = Layer(75, key_data)
        key_builder.set_step(layer)
        self.affine_cipher(image)
        print("Affine")
        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)

    def get_correspondent(self, x):
        return (self.a * x + self.b) % self.m

    def affine_cipher(self, image):
        affine_image = np.vectorize(self.get_correspondent)(image)
        for i in range(len(affine_image)):
            image[i] = affine_image[i]
