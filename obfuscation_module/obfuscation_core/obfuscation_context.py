from numpy import ndarray

from key.key_builder import KeyBuilder
from obfuscation_core.obfuscators.affine_obfuscator import AffineObfuscator
from obfuscation_core.obfuscators.blur_obfuscator import BlurObfuscator
from obfuscation_core.obfuscators.encryption_obfuscator import EncryptionObfuscator
from obfuscation_core.obfuscators.scramble_obfuscator import ScrambleObfuscator


class ObfuscationContext:
    def __init__(self):
        self.obfuscator = self.init_obfuscators()

    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        self.obfuscator.obfuscate(image, key_builder)

    @staticmethod
    def init_obfuscators():
        blur = BlurObfuscator()
        scramble = ScrambleObfuscator()
        encryption1 = EncryptionObfuscator()
        encryption2 = EncryptionObfuscator()
        affine = AffineObfuscator()

        blur.set_next_obfuscator(scramble)
        scramble.set_next_obfuscator(encryption1)
        encryption1.set_next_obfuscator(encryption2)
        encryption2.set_next_obfuscator(affine)
        return blur
