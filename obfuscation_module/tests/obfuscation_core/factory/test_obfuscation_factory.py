import unittest

from API.backend.Comm.CommandAffine import CommandAffine
from API.backend.Comm.CommandEncryption import CommandEncryption
from API.backend.Comm.CommandXOR import CommandXOR
from obfuscation_core.factory.obfuscastor_factory import ObfuscationFactory
from obfuscation_core.obfuscators.XOR_obfuscator import XORObfuscator
from obfuscation_core.obfuscators.affine_obfuscator import AffineObfuscator
from obfuscation_core.obfuscators.encryption_obfuscator import EncryptionObfuscator


class TestObfuscationFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.obfuscatorFactory = ObfuscationFactory()

    def test_create_obfuscator_affine(self):
        command = CommandAffine()
        obfuscator = self.obfuscatorFactory.create_obfuscation([command])

        self.assertEqual(obfuscator.__class__, AffineObfuscator)

    def test_create_obfuscator_encryption(self):
        command = CommandEncryption()
        obfuscator = self.obfuscatorFactory.create_obfuscation([command])

        self.assertEqual(obfuscator.__class__, EncryptionObfuscator)

    def test_create_obfuscator_xor(self):
        command = CommandXOR()
        obfuscator = self.obfuscatorFactory.create_obfuscation([command])

        self.assertEqual(obfuscator.__class__, XORObfuscator)

    def test_create_obfuscator_combine(self):
        command1 = CommandAffine()
        command2 = CommandEncryption()
        command3 = CommandXOR()
        obfuscator = self.obfuscatorFactory.create_obfuscation([command1, command2, command3])

        self.assertEqual(obfuscator.__class__, AffineObfuscator)
        self.assertTrue(obfuscator.next_obfuscator is not None)
        self.assertEqual(obfuscator.next_obfuscator.__class__, EncryptionObfuscator)
        self.assertTrue(obfuscator.next_obfuscator.next_obfuscator is not None)
        self.assertEqual(obfuscator.next_obfuscator.next_obfuscator.__class__, XORObfuscator)
