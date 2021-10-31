from obfuscation_module.key.key_types.zone_key import ZoneKey
from obfuscation_module.obfuscation_core.deobfusators.blur_deobfuscator import BlurDeObfuscator
from obfuscation_module.obfuscation_core.deobfusators.deobfuscator import DeObfuscator
from obfuscation_module.obfuscation_core.deobfusators.XOR_deobfuscator import XORDeObfuscator
from obfuscation_module.obfuscation_core.deobfusators.scramble_deofuscator import ScrambleDeObfuscator


class DeobfuscationFactory:

    def __init__(self) -> None:
        pass

    def create_deobfuscation(self, zone_key: ZoneKey) -> DeObfuscator:
        deobfuscator = None
        starting_deobuscator = None
        switcher = {
            1: BlurDeObfuscator,
            25: XORDeObfuscator,
            50: ScrambleDeObfuscator
        }
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
