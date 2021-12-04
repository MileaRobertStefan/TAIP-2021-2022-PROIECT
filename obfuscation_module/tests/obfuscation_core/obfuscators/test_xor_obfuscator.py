import random
import unittest

import numpy as np
from freezegun import freeze_time
from mockito import when, ANY, spy, verify

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
from obfuscation_core.obfuscators.XOR_obfuscator import XORObfuscator


class TestXORObfuscator(unittest.TestCase):
    def setUp(self) -> None:
        self.obfuscator = XORObfuscator()

    @freeze_time("2012-01-01")
    def test_obfuscate(self):
        when(random).random().thenReturn(1)

        image = np.arange(3).reshape((1, 1, 3))
        expected_image = np.array([188, 116, 123]).reshape((1, 1, 3))
        expected_layer = Layer(25, 1000000000)
        key_builder = spy(KeyBuilder)

        when(key_builder).set_step(ANY).thenReturn(None)
        self.obfuscator.obfuscate(image, key_builder)

        self.assertEqual(image.shape, expected_image.shape)
        self.assertTrue(np.array_equal(image, expected_image))
        verify(key_builder).set_step(expected_layer)
