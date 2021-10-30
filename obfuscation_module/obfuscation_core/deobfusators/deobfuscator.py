class DeObfuscator:
    next_deobfuscator = None
    key_data = ""
    def __init__(self, key_data):
        pass

    def set_next_deobfuscator(self, next_deobfuscator):
        self.next_deobfuscator = next_deobfuscator

    def parse_key_data(key_data : str) -> None:
        pass

    def deobfuscate(self, coordinates, image):

        # TODO deobfuscate

        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(coordinates, image)
        pass


