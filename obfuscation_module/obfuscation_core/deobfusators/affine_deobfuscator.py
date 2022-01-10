import numpy as np
from numpy import ndarray

from obfuscation_core.deobfusators.deobfuscator import DeObfuscator


class AffineDeObfuscator(DeObfuscator):
    def __init__(self):
        super().__init__()
        self.m = 256
        self.a_inverse = 207
        self.b = None

    def deobfuscate(self, image: ndarray):
        print("Affine")
        np.random.seed(self.key_data)
        self.b = np.random.randint(0, 256)
        self.decryption(image)
        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(image)

    def get_correspondent(self, y):
        return (self.a_inverse * (y - self.b)) % self.m

    def decryption(self, image):
        affine_image = np.vectorize(self.get_correspondent)(image)
        for i in range(len(affine_image)):
            image[i] = affine_image[i]
