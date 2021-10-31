from numpy import ndarray

from obfuscation_module.key.key_builder import KeyBuilder


class Obfuscator:
    def __init__(self):
        self.next_obfuscator = None

    def set_next_obfuscator(self, next_obfuscator):
        self.next_obfuscator = next_obfuscator

    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        # TODO obfuscate

        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)
