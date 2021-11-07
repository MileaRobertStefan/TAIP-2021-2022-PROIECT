from numpy import ndarray
import cv2
import numpy as np

from obfuscation_core.deobfusators.deobfuscator import DeObfuscator


class PuzzleDeObfuscator(DeObfuscator):

    def deobfuscate(self, image: ndarray) -> None:
        print("Removing puzzle obfuscation...")
        values = self.key_data.split("|")
        puzzle_size = values[0]
        values.pop()
        i0_originals = [int(x) for x in values[1::8]]
        i1_originals = [int(x) for x in values[2::8]]
        j0_originals = [int(x) for x in values[3::8]]
        j1_originals = [int(x) for x in values[4::8]]

        i0_shuffles = [int(x) for x in values[5::8]]
        i1_shuffles = [int(x) for x in values[6::8]]
        j0_shuffles = [int(x) for x in values[7::8]]
        j1_shuffles = [int(x) for x in values[8::8]]

        original_image = image.copy()

        for i in range(0, len(i0_originals)):
            original_image[i0_shuffles[i]:i1_shuffles[i], j0_shuffles[i]:j1_shuffles[i]] = image[i0_originals[i]:i1_originals[i],
                                                                               j0_originals[i]:j1_originals[i]]
        for i in range(len(image)):
            image[i] = original_image[i]

        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(image)
