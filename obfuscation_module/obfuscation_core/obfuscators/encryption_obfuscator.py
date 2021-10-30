import random

from key.key_types.layer import Layer
from obfuscation_core.obfuscators.obfuscator import Obfuscator


class EncryptionObfuscator(Obfuscator):
    def obfuscate(self, image, key_builder):
        layer = Layer(25, "key_data for encrypt")
        random.seed("key_data")
        key_builder.set_step(layer)

        print("Encrypting")
        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)

