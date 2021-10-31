import cv2
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
        image = self.decryption(image)
        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(image)

    def get_correspondent(self, y):
        return (self.a_inverse * (y - self.b)) % self.m

    def decryption(self, image):
        height = image.shape[0]
        width = image.shape[1]

        for i in range(0, height):
            for j in range(0, width):
                a = image[i][j]  # rgb list
                r = self.get_correspondent(a[0])
                g = self.get_correspondent(a[1])
                b = self.get_correspondent(a[2])
                image[i][j] = [r, g, b]
        return image
