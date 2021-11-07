from numpy import ndarray
import cv2
import numpy as np

from obfuscation_core.deobfusators.deobfuscator import DeObfuscator


class ColorDeObfuscator(DeObfuscator):
    def convert_string_to_tuple(self, tuple_str):
        tuple_str = tuple_str.replace("(", "").replace(")", "")
        return tuple(map(int, tuple_str.split(',')))

    def parse_key_data(self):
        values = self.key_data.split("|")

        original_values = values[::2]
        replacement_values = values[1::2]
        original_values.pop()

        original_values_dict = dict()
        for i in range(0, len(original_values)):
            original_values[i] = self.convert_string_to_tuple(original_values[i])
            replacement_values[i] = self.convert_string_to_tuple(replacement_values[i])
            original_values_dict[replacement_values[i]] = original_values[i]
        return replacement_values, original_values_dict

    def deobfuscate(self, image: ndarray) -> None:
        print("Removing color obfuscation...")

        replacement_values, original_values_dict = self.parse_key_data()

        for i in range(0, len(image)):
            for j in range(0, len(image[i])):
                if tuple(image[i][j]) in replacement_values:
                    image[i][j] = original_values_dict[tuple(image[i][j])]
                else:
                    if j % 5 == 0:
                        image[i][j] = 255 - np.roll(image[i][j], -(i % 3))
                    else:
                        image[i][j] = np.roll(image[i][j], -(i % 3))

        inverted_image = cv2.bitwise_not(image)
        for i in range(len(image)):
            image[i] = inverted_image[i]

        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(image)
