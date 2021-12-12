import unittest

from API.backend.Comm.CommandAffine import CommandAffine
from API.backend.Comm.CommandEncryption import CommandEncryption
from API.backend.Comm.CommandXOR import CommandXOR
from key.key_types.layer import Layer
from key.key_types.zone_key import ZoneKey
from obfuscation_core.deobfusators.XOR_deobfuscator import XORDeObfuscator
from obfuscation_core.deobfusators.affine_deobfuscator import AffineDeObfuscator
from obfuscation_core.deobfusators.encryption_deobfuscator import EncryptionDeObfuscator
from obfuscation_core.factory.deobfuscation_factory import DeobfuscationFactory
from obfuscation_core.factory.obfuscastor_factory import ObfuscationFactory
from obfuscation_core.obfuscators.XOR_obfuscator import XORObfuscator
from obfuscation_core.obfuscators.affine_obfuscator import AffineObfuscator
from obfuscation_core.obfuscators.encryption_obfuscator import EncryptionObfuscator


class TestObfuscationFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.obfuscatorFactory = DeobfuscationFactory()

    def test_create_deobfuscator_affine(self):
        layer = Layer(75, "dummy")
        zone_key = ZoneKey((), [layer])
        deobfuscator = self.obfuscatorFactory.create_deobfuscation(zone_key)

        self.assertEqual(deobfuscator.__class__, AffineDeObfuscator)

    def test_create_deobfuscator_encryption(self):
        layer = Layer(150, "dummy")
        zone_key = ZoneKey((), [layer])
        deobfuscator = self.obfuscatorFactory.create_deobfuscation(zone_key)

        self.assertEqual(deobfuscator.__class__, EncryptionDeObfuscator)

    def test_create_deobfuscator_xor(self):
        layer = Layer(25, "dummy")
        zone_key = ZoneKey((), [layer])
        deobfuscator = self.obfuscatorFactory.create_deobfuscation(zone_key)

        self.assertEqual(deobfuscator.__class__, XORDeObfuscator)

    def test_create_deobfuscator_combine(self):
        layer1 = Layer(25, "dummy")
        layer2 = Layer(75, "dummy")
        layer3 = Layer(150, "dummy")
        zone_key = ZoneKey((), [layer1, layer2, layer3])
        deobfuscator = self.obfuscatorFactory.create_deobfuscation(zone_key)

        self.assertEqual(deobfuscator.__class__, XORDeObfuscator)
        self.assertTrue(deobfuscator.next_deobfuscator is not None)
        self.assertEqual(deobfuscator.next_deobfuscator.__class__, AffineDeObfuscator)
        self.assertTrue(deobfuscator.next_deobfuscator.next_deobfuscator is not None)
        self.assertEqual(deobfuscator.next_deobfuscator.next_deobfuscator.__class__, EncryptionDeObfuscator)
