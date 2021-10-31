import random

from numpy import ndarray

from obfuscation_module.key.key_builder import KeyBuilder
from obfuscation_module.key.key_types.layer import Layer
from obfuscation_module.obfuscation_core.obfuscators.obfuscator import Obfuscator


class BlurObfuscator(Obfuscator):
    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        layer = Layer(1, "key_data for blur")
        random.seed("key_data")
        key_builder.set_step(layer)
        print("Blurring")
        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)
