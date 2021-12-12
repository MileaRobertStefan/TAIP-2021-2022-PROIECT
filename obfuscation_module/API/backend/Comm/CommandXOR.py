from API.backend.Comm.command import Command

from obfuscation_core.obfuscators.XOR_obfuscator import XORObfuscator


class CommandXOR(Command):
    id = 5

    def __init__(self):
        self.puzzle_size: int = None

        pass

    def set_params(self, params: dict):
        print(params)

    def execute(self) -> XORObfuscator:
        print("Executing XORObfuscator!")
        return XORObfuscator()
