from API.backend.Comm.command import Command

from obfuscation_core.obfuscators.scramble_obfuscator import ScrambleObfuscator


class CommandScramble(Command):
    id = 2

    def __init__(self):
        self.scramble_percent: int = 100

        pass

    def set_params(self, params: dict):
        # self.scramble_percent = params["scramble_percent"]
        print(params)

    def execute(self) -> ScrambleObfuscator:
        print("Executing ScrambleObfuscator!")
        return ScrambleObfuscator(self.scramble_percent)
