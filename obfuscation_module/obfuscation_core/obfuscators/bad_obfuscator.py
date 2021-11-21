import cv2
from numpy import ndarray
import numpy as np

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
from time_logging.time_logger import time_logged, monitor_obfuscation
from obfuscation_core.obfuscators.obfuscator import Obfuscator


class BadObfuscator(Obfuscator):
    id = 127

    @monitor_obfuscation
    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        print("Running bad obfuscator...")

        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grayscale_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2RGB)
        #for i in range(len(image)):
            # image[i] = grayscale_image[0]

        image = np.concatenate((image, grayscale_image[0]))

        # image.reshape((image.shape[1], image.shape[0], image.shape[2]))


        layer = Layer(BadObfuscator.id, "")
        key_builder.set_step(layer)

        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)

