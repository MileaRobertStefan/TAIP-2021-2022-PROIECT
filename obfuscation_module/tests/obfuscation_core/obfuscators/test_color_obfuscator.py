import random
import unittest

import numpy as np
from freezegun import freeze_time
from mockito import when, ANY, spy, verify

from key.key_builder import KeyBuilder
from obfuscation_core.obfuscators.color_obfuscator import ColorObfuscator


class TestColorObfuscator(unittest.TestCase):
    def setUp(self) -> None:
        self.obfuscator = ColorObfuscator()

    def test_my_custom_random(self):
        values_to_exclude = [1, 2, 3, 4, 5]
        random_result = self.obfuscator.my_custom_random(values_to_exclude)

        self.assertTrue(random_result not in values_to_exclude)

    @freeze_time("2012-01-01")
    def test_obfuscate(self):
        when(random).random().thenReturn(1)

        initial_image = np.arange(300).reshape((10, 10, 3))
        image = np.arange(300).reshape((10, 10, 3))
        key_builder = spy(KeyBuilder)

        when(key_builder).set_step(ANY).thenReturn(None)
        self.obfuscator.obfuscate(image, key_builder)

        self.assertFalse(np.array_equal(image, initial_image))
        verify(key_builder).set_step(ANY)
