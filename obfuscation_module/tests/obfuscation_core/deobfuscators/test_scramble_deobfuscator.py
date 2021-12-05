import unittest

import numpy as np

from obfuscation_core.deobfusators.scramble_deofuscator import ScrambleDeObfuscator


class TestScrambleDeobfuscator(unittest.TestCase):
    def setUp(self) -> None:
        self.deobfuscator = ScrambleDeObfuscator()

    def test_deobfuscate(self):
        self.deobfuscator.key_data = "100000000000||15"
        expected_image = np.arange(9).reshape((1, 3, 3))
        image = np.array([3, 4, 5, 0, 1, 2, 6, 7, 8]).reshape((1, 3, 3))

        self.deobfuscator.deobfuscate(image)

        self.assertEqual(image.shape, expected_image.shape)
        self.assertTrue(np.array_equal(image, expected_image))
