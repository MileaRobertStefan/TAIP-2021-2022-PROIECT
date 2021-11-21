import random
from datetime import datetime

import numpy as np
from numpy import ndarray

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
# from time_logging.time_logger import time_logged
from obfuscation_core.obfuscators.obfuscator import Obfuscator


class AffineObfuscator(Obfuscator):
    def __init__(self):
        super().__init__()
        self.a = 7727
        self.m = 256
        self.b = None

    # @time_logged
    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        random.seed(datetime.now())
        key_data = int(random.random() * 1000000000)
        np.random.seed(key_data)
        self.b = np.random.randint(0, 256)
        layer = Layer(75, key_data)
        key_builder.set_step(layer)
        image = self.affine_cipher(image)
        print("Affine")
        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)

    def get_correspondent(self, x):
        return (self.a * x + self.b) % self.m

    def affine_cipher(self, image):
        height = image.shape[0]
        width = image.shape[1]
        for i in range(0, height):
            for j in range(0, width):
                pixel = image[i][j]
                r = self.get_correspondent(pixel[0])
                g = self.get_correspondent(pixel[1])
                b = self.get_correspondent(pixel[2])
                image[i][j] = [r, g, b]
        return image
