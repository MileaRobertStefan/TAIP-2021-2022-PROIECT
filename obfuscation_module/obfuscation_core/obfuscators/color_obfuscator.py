import codecs

import cv2
from numpy import ndarray
import numpy as np
import random

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
from time_logging.time_logger import time_logged, monitor_obfuscation
from obfuscation_core.obfuscators.obfuscator import Obfuscator


def my_encode(s):
    return codecs.encode(s, "base64").decode()


class ColorObfuscator(Obfuscator):
    id = 100

    def my_custom_random(self, values_to_exclude):
        random_tuple = tuple(random.randint(0, 255) for _ in range(3))
        return self.my_custom_random(values_to_exclude) if random_tuple in values_to_exclude else random_tuple

    @monitor_obfuscation
    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        print("Coloring...")
        inverted_image = cv2.bitwise_not(image)
        for i in range(len(image)):
            image[i] = inverted_image[i]

        pixels_to_replace = set()
        for i in range(0, len(image), round(len(image) / 10)):
            for j in range(0, len(image[i]), round(len(image[i]) / 10)):
                pixels_to_replace.add(tuple(image[i][j]))
                if len(pixels_to_replace) > 300:
                    break
            else:
                continue
            break

        key_data = str("")

        replacements_dict = dict()
        for i, value in enumerate(pixels_to_replace):
            replacements_dict[value] = self.my_custom_random(list(replacements_dict.keys()) + list(pixels_to_replace))
            key_data += str(value).replace(" ", "") + "|" + str(replacements_dict[value]).replace(" ", "") + "|"

        for i in range(len(image)):
            for j in range(0, len(image[i])):
                if tuple(image[i][j]) in pixels_to_replace:
                    image[i][j] = replacements_dict[tuple(image[i][j])]
                else:
                    if j % 5 == 0:
                        image[i][j] = 255 - np.roll(image[i][j], i % 3)
                    else:
                        image[i][j] = np.roll(image[i][j], i % 3)

        layer = Layer(ColorObfuscator.id, key_data)
        key_builder.set_step(layer)

        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)

