from obfuscation_core.obfuscators.blur_obfuscator import BlurObfuscator
from obfuscation_core.obfuscators.encryption_obfuscator import EncryptionObfuscator


class ObfuscationContext:
    def __init__(self):
        self.obfuscator = self.init_obfuscators()

    def obfuscate(self, coordinates, image, key_builder):
        self.obfuscator.obfuscate(coordinates, image, key_builder)

    @staticmethod
    def init_obfuscators():
        encryption1 = EncryptionObfuscator()
        blur = BlurObfuscator()
        encryption2 = EncryptionObfuscator()
        encryption1.set_next_obfuscator(blur)
        blur.set_next_obfuscator(encryption2)
        return encryption1
