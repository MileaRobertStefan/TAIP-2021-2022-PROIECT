from key.key_types.zone_key import ZoneKey
from obfuscation_core.deobfusators.XOR_deobfuscator import XORDeObfuscator
from obfuscation_core.deobfusators.affine_deobfuscator import AffineDeObfuscator
from obfuscation_core.deobfusators.color_deobfuscator import ColorDeObfuscator
from obfuscation_core.deobfusators.deobfuscator import DeObfuscator
from obfuscation_core.deobfusators.encryption_deobfuscator import EncryptionDeObfuscator
from obfuscation_core.deobfusators.puzzle_deobfuscator import PuzzleDeObfuscator
from obfuscation_core.deobfusators.scramble_deofuscator import ScrambleDeObfuscator

switcher = {
    25: XORDeObfuscator,
    50: ScrambleDeObfuscator,
    75: AffineDeObfuscator,
    100: ColorDeObfuscator,
    125: PuzzleDeObfuscator,
    150: EncryptionDeObfuscator
}

class DeobfuscationFactory:


    def __init__(self) -> None:
        pass

    def create_deobfuscation(self, zone_key: ZoneKey) -> DeObfuscator:
        deobfuscator = None
        starting_deobuscator = None

        for layer in zone_key.layers[::-1]:
            if deobfuscator is None:
                deobfuscator = switcher[layer.alg_id]()
                deobfuscator.key_data = layer.key_data
                starting_deobuscator = deobfuscator
            else:
                next_deobfuscator = switcher[layer.alg_id]()
                deobfuscator.next_deobfuscator = next_deobfuscator
                deobfuscator = next_deobfuscator
                deobfuscator.key_data = layer.key_data

        return starting_deobuscator
