import codecs
import random

import cv2
from numpy import ndarray

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
from obfuscation_core.obfuscators.obfuscator import Obfuscator


def my_encode(s):
    return codecs.encode(s, "base64").decode()


class BlurObfuscator(Obfuscator):
    id = 1

    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        print("Blurring")
        odd_rand_num = random.randrange(19, 29, 2)
        blurred_image = cv2.blur(image, (odd_rand_num, odd_rand_num))
        for i in range(len(image)):
            image[i] = blurred_image[i]

        key_data = str(odd_rand_num)
        layer = Layer(BlurObfuscator.id, key_data)
        key_builder.set_step(layer)

        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)

