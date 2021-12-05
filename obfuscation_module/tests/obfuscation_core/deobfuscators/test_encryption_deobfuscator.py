import unittest

import numpy as np

from key.key_builder import KeyBuilder
from obfuscation_core.deobfusators.encryption_deobfuscator import EncryptionDeObfuscator
from obfuscation_core.obfuscators.encryption_obfuscator import EncryptionObfuscator


class TestColorDeobfuscator(unittest.TestCase):
    def setUp(self) -> None:
        self.deobfuscator = EncryptionDeObfuscator()

    def test_deobfuscate(self):
        initial_image = np.arange(300, dtype=np.uint8).reshape((10, 10, 3))
        image = np.arange(300, dtype=np.uint8).reshape((10, 10, 3))

        key_builder = KeyBuilder(((1, 1), (3, 3)))
        EncryptionObfuscator().obfuscate(image, key_builder)
        self.deobfuscator.key_data = key_builder.steps[0].key_data
        self.deobfuscator.deobfuscate(image)

        self.assertEqual(image.shape, initial_image.shape)
        self.assertTrue(np.array_equal(image, initial_image))
