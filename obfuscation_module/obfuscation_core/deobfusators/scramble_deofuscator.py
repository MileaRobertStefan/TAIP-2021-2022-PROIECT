import random

from numpy import ndarray

from obfuscation_module.obfuscation_core.deobfusators.deobfuscator import DeObfuscator


class ScrambleDeObfuscator(DeObfuscator):
    seed = None
    scramble_percent = None

    def parse_key_data(self) -> None:
        self.seed, self.scramble_percent = self.key_data.split("||")
        self.seed = int(self.seed)
        self.scramble_percent = int(self.scramble_percent)

    def deobfuscate(self, image: ndarray):
        if self.seed is None or self.scramble_percent is None:
            self.parse_key_data()
        print("Descramble")
        random.seed(self.seed)
        y_size = len(image)
        x_size = len(image[0])
        nr_pixels = (self.scramble_percent * image.size) // 100
        coords_list = []
        for i in range(nr_pixels):
            start_x = random.randrange(1000000) % x_size
            start_y = random.randrange(1000000) % y_size
            end_x = random.randrange(1000000) % x_size
            end_y = random.randrange(1000000) % y_size
            coords_list.append(((start_y, start_x), (end_y, end_x)))

        for coords in coords_list[::-1]:
            ((start_y, start_x), (end_y, end_x)) = coords
            aux = image[start_y][start_x].copy()
            image[start_y][start_x] = image[end_y][end_x]
            image[end_y][end_x] = aux

        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(image)
