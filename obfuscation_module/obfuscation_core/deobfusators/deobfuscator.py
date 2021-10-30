class DeObfuscator:
    next_deobfuscator = None
    key_data = None
    def __init__(self):
        pass

    def set_next_deobfuscator(self, next_deobfuscator):
        self.next_deobfuscator = next_deobfuscator

    def parse_key_data(self) -> None:
        pass

    def deobfuscate(self, image):
        pass


