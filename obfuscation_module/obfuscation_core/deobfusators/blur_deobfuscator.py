from numpy import ndarray

from obfuscation_core.deobfusators.deobfuscator import DeObfuscator


class BlurDeObfuscator(DeObfuscator):
    def deobfuscate(self, image: ndarray) -> None:
        print("DeBlurring")
        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(image)
