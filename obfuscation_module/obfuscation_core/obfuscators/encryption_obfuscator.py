import random
from datetime import datetime

import cv2
import numpy as np
from numpy import ndarray

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
from obfuscation_core.obfuscators.obfuscator import Obfuscator


class EncryptionObfuscator(Obfuscator):
    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        random.seed(datetime.now())
        key_data = int(random.random() * 1000000000)
        np.random.seed(key_data)
        key = np.random.randint(0, 256, size=image.shape, dtype=np.uint8)
        layer = Layer(25, key_data)
        key_builder.set_step(layer)

        image_encrypt = cv2.bitwise_xor(image, key)  # encryption
        for i in range(len(image)):
            image[i] = image_encrypt[i]

        print("Encrypting")
        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)
