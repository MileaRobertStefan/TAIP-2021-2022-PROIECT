import cv2
import numpy as np
from numpy import ndarray

from obfuscation_module.obfuscation_core.deobfusators.deobfuscator import DeObfuscator


class XORDeObfuscator(DeObfuscator):
    def deobfuscate(self, image: ndarray):
        print("Decryption")
        np.random.seed(self.key_data)
        key = np.random.randint(0, 256, size=image.shape, dtype=np.uint8)

        image_decrypt = cv2.bitwise_xor(image, key)  # decrypt
        for i in range(len(image)):
            image[i] = image_decrypt[i]
        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(image)
