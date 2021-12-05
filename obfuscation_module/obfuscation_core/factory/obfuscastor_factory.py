from typing import List

from API.backend.Comm.command import Command
from obfuscation_core.obfuscators.XOR_obfuscator import *
from obfuscation_core.obfuscators.affine_obfuscator import *
from obfuscation_core.obfuscators.encryption_obfuscator import *
from obfuscation_core.obfuscators.scramble_obfuscator import *


# from obfuscation_core.obfuscators. import *
# from obfuscation_core.obfuscators. import *


class ObfuscationFactory:
    switcher = {
        25: XORObfuscator,
        50: ScrambleObfuscator,
        75: AffineObfuscator,
        100: EncryptionObfuscator
    }

    def __init__(self) -> None:
        pass

    def create_obfuscation(self, commands: List[Command]) -> Obfuscator:
        obfuscators = []

        for command in commands:
            obfuscators.append(command.execute())

        current_ob = obfuscators[0]
        for ob in obfuscators[1:]:
            current_ob.next_obfuscator = ob
            current_ob = ob

        return obfuscators[0]

    pass
