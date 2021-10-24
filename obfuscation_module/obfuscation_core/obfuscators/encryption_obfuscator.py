from obfuscation_core.obfuscators.obfuscator import Obfuscator


class EncryptionObfuscator(Obfuscator):
    def obfuscate(self, coordinates, image, key_builder):
        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(coordinates, image, key_builder)
