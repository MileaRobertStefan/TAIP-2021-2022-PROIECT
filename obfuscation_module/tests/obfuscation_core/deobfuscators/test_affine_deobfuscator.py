import unittest

import numpy as np

from obfuscation_core.deobfusators.affine_deobfuscator import AffineDeObfuscator


class TestAffineDeobfuscator(unittest.TestCase):
    def setUp(self) -> None:
        self.deobfuscator = AffineDeObfuscator()

    def test_affine_cipher(self):
        self.deobfuscator.b = 5
        expected_image = np.arange(3).reshape((1, 1, 3))
        image = np.array([5, 52, 99]).reshape((1, 1, 3))

        self.deobfuscator.decryption(image)

        self.assertEqual(image.shape, expected_image.shape)
        self.assertTrue(np.array_equal(image, expected_image))

    def test_set_correspondent(self):
        x = 219
        self.deobfuscator.b = 5

        correspondent = self.deobfuscator.get_correspondent(x)

        self.assertEqual(correspondent, 10)

    def test_deobfuscate(self):
        self.deobfuscator.key_data = 1000000000
        expected_image = np.arange(3).reshape((1, 1, 3))
        image = np.array([188, 235, 26]).reshape((1, 1, 3))

        self.deobfuscator.deobfuscate(image)

        self.assertEqual(self.deobfuscator.b, 188)
        self.assertEqual(image.shape, expected_image.shape)
        self.assertTrue(np.array_equal(image, expected_image))

