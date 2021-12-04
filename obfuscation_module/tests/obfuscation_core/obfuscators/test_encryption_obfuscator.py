import random
import unittest

import numpy as np
from freezegun import freeze_time
from mockito import when, spy

from key.key_builder import KeyBuilder
from obfuscation_core.obfuscators.encryption_obfuscator import EncryptionObfuscator


class TestEncryptionObfuscator(unittest.TestCase):
    def setUp(self) -> None:
        self.obfuscator = EncryptionObfuscator()

    @freeze_time("2012-01-01")
    def test_obfuscate(self):
        when(random).random().thenReturn(1)

        image = np.arange(5, 8).reshape((1, 1, 3))
        # expected_image = np.array([188, 235, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0]).reshape((1, 4, 3))
        # expected_layer = Layer(75, 1000000000)
        key_builder = spy(KeyBuilder)

        # when(key_builder).set_step(ANY).thenReturn(None)
        # self.obfuscator.obfuscate(image, key_builder)

        # self.assertEqual(image.shape, expected_image.shape)
        # self.assertTrue(np.array_equal(image, expected_image))
        # verify(key_builder).set_step(expected_layer)
