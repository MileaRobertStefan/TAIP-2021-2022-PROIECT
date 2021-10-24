class Obfuscator:
    def __init__(self):
        self.next_obfuscator = None

    def set_next_obfuscator(self, next_obfuscator):
        self.next_obfuscator = next_obfuscator

    def obfuscate(self, coordinates, image, key_builder):

        # TODO obfuscate
        
        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(coordinates, image,key_builder)




