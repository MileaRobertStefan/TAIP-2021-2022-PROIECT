from obfuscation_core.deobfusators.deobfuscator import DeObfuscator


class EncryptionDeObfuscator(DeObfuscator):
    def deobfuscate(self, image):
        print("Decryption")
        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(image)

