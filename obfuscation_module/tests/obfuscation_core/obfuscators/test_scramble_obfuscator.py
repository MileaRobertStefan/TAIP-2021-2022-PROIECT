import random
import unittest
import numpy as np
from freezegun import freeze_time
from mockito import when, ANY, spy, verify

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
from obfuscation_core.obfuscators.scramble_obfuscator import ScrambleObfuscator


class TestScrambleObfuscator(unittest.TestCase):
    def setUp(self) -> None:
        self.obfuscator = ScrambleObfuscator()

    @freeze_time("2012-01-01")
    def test_obfuscate(self):
        when(random).random().thenReturn(1)

        image = np.arange(9).reshape((1, 3, 3))
        expected_image = np.array([3, 4, 5, 0, 1, 2, 6, 7, 8]).reshape((1, 3, 3))
        expected_layer = Layer(50, "100000000000||15")
        key_builder = spy(KeyBuilder)

        when(key_builder).set_step(ANY).thenReturn(None)
        self.obfuscator.obfuscate(image, key_builder)

        self.assertEqual(image.shape, expected_image.shape)
        self.assertTrue(np.array_equal(image, expected_image))
        verify(key_builder).set_step(expected_layer)



