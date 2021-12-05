import unittest

import numpy as np

from obfuscation_core.deobfusators.XOR_deobfuscator import XORDeObfuscator


class TestXorDeobfuscator(unittest.TestCase):
    def setUp(self) -> None:
        self.deobfuscator = XORDeObfuscator()

    def test_deobfuscate(self):
        self.deobfuscator.key_data = 1000000000
        expected_image = np.array([0, 200, 199]).reshape((1, 1, 3))
        image = np.array([188, 116, 123]).reshape((1, 1, 3))

        self.deobfuscator.deobfuscate(image)

        self.assertEqual(image.shape, expected_image.shape)
        self.assertTrue(np.array_equal(image, expected_image))

