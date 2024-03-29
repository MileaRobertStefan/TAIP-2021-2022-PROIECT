import codecs
import random

from numpy import ndarray

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
from obfuscation_core.obfuscators.obfuscator import Obfuscator
from time_logging.time_logger import monitor_obfuscation


def my_encode(s):
    return codecs.encode(s, "base64").decode()


class PuzzleObfuscator(Obfuscator):
    id = 125

    def __init__(self, puzzle_size: int = None):
        super().__init__()

        if puzzle_size is not None:
            self.puzzle_size = puzzle_size
        else:
            self.puzzle_size = random.randint(3, 7)

    def my_custom_random(self, values_to_exclude):
        random_tuple = tuple(random.randint(0, 255) for _ in range(3))
        return self.my_custom_random(values_to_exclude) if random_tuple in values_to_exclude else random_tuple

    @monitor_obfuscation
    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        print("Creating puzzle...")

        puzzle_piece_height = max(len(image) // self.puzzle_size, 5)
        puzzle_piece_width = max(len(image[0]) // self.puzzle_size, 5)
        print(puzzle_piece_height, puzzle_piece_width)
        puzzle_pieces_coords = []
        for i in range(0, self.puzzle_size):
            if (i + 1) * puzzle_piece_height < len(image):
                for j in range(0, self.puzzle_size):
                    if (j + 1) * puzzle_piece_width < len(image[0]):
                        puzzle_pieces_coords.append(tuple((i * puzzle_piece_height, j * puzzle_piece_width)))

        puzzle_pieces_shuffled = puzzle_pieces_coords.copy()
        random.shuffle(puzzle_pieces_coords)

        key_data = str(self.puzzle_size) + "|"
        shuffled_image = image.copy()
        for i in range(0, len(puzzle_pieces_shuffled)):
            i0_original, j0_original = puzzle_pieces_coords[i][0], puzzle_pieces_coords[i][1]
            i1_original, j1_original = i0_original + puzzle_piece_height, j0_original + puzzle_piece_width

            i0_shuffle, j0_shuffle = puzzle_pieces_shuffled[i][0], puzzle_pieces_shuffled[i][1]
            i1_shuffle, j1_shuffle = i0_shuffle + puzzle_piece_height, j0_shuffle + puzzle_piece_width

            key_data += str(i0_original) + "|" + str(i1_original) + "|" + str(j0_original) + "|" + str(
                j1_original) + "|"
            key_data += str(i0_shuffle) + "|" + str(i1_shuffle) + "|" + str(j0_shuffle) + "|" + str(j1_shuffle) + "|"

            shuffled_image[i0_original:i1_original, j0_original:j1_original] = image[i0_shuffle:i1_shuffle,
                                                                               j0_shuffle:j1_shuffle]

        for i in range(len(image)):
            image[i] = shuffled_image[i]

        layer = Layer(PuzzleObfuscator.id, key_data)
        key_builder.set_step(layer)

        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)
