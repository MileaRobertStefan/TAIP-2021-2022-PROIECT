import random

import cv2

from obfuscation_core.deobfusators.deobfuscator import DeObfuscator


class ScrambleDeObfuscator(DeObfuscator):
    scramble_percent = 10

    def deobfuscate(self, image):
        print("Descramble")
        random.seed(self.key_data)
        y_size = len(image)
        x_size = len(image[0])
        nr_pixels = (self.scramble_percent * image.size) // 100
        coords_list = []
        for i in range(nr_pixels):
            start_x = random.randrange(1000000) % x_size
            start_y = random.randrange(1000000) % y_size
            end_x = random.randrange(1000000) % x_size
            end_y = random.randrange(1000000) % y_size
            coords_list.append(((start_y, start_x), (end_y, end_x)))

        for coords in coords_list[::-1]:
            ((start_y, start_x), (end_y, end_x)) = coords
            aux = image[start_y][start_x].copy()
            image[start_y][start_x] = image[end_y][end_x]
            image[end_y][end_x] = aux

        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(image)
