import unittest

import numpy as np

from key.key_builder import KeyBuilder
from obfuscation_core.deobfusators.puzzle_deobfuscator import PuzzleDeObfuscator
from obfuscation_core.obfuscators.puzzle_obfuscator import PuzzleObfuscator


class TestPuzzleDeobfuscator(unittest.TestCase):
    def setUp(self) -> None:
        self.deobfuscator = PuzzleDeObfuscator()

    def test_deobfuscate(self):
        initial_image = np.arange(675).reshape((15, 15, 3))
        image = np.arange(675).reshape((15, 15, 3))

        key_builder = KeyBuilder(((1, 1), (3, 3)))
        PuzzleObfuscator(5).obfuscate(image, key_builder)
        self.deobfuscator.key_data = key_builder.steps[0].key_data
        self.deobfuscator.deobfuscate(image)

        self.assertEqual(image.shape, initial_image.shape)
        self.assertTrue(np.array_equal(image, initial_image))

