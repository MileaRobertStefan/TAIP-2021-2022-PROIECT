import random
import unittest
import numpy as np
from freezegun import freeze_time
from mockito import when, ANY, spy, verify

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
from obfuscation_core.obfuscators.affine_obfuscator import AffineObfuscator


class TestAffineObfuscator(unittest.TestCase):
    def setUp(self) -> None:
        self.obfuscator = AffineObfuscator()

    def test_affine_cipher(self):
        self.obfuscator.b = 5
        image = np.arange(3).reshape((1, 1, 3))
        expected_image = np.array([5, 52, 99]).reshape((1, 1, 3))

        self.obfuscator.affine_cipher(image)

        self.assertEqual(image.shape, expected_image.shape)
        self.assertTrue(np.array_equal(image, expected_image))

    def test_set_correspondent(self):
        x = 10
        self.obfuscator.b = 5

        correspondent = self.obfuscator.get_correspondent(x)

        self.assertEqual(correspondent, 219)

    @freeze_time("2012-01-01")
    def test_obfuscate(self):
        when(random).random().thenReturn(1)

        image = np.arange(3).reshape((1, 1, 3))
        expected_image = np.array([188, 235, 26]).reshape((1, 1, 3))
        expected_layer = Layer(75, 1000000000)
        key_builder = spy(KeyBuilder)

        when(key_builder).set_step(ANY).thenReturn(None)
        self.obfuscator.obfuscate(image, key_builder)

        self.assertEqual(self.obfuscator.b, 188)
        self.assertEqual(image.shape, expected_image.shape)
        self.assertTrue(np.array_equal(image, expected_image))
        verify(key_builder).set_step(expected_layer)



