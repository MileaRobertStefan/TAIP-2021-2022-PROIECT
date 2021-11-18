from API.backend.Comm.command import Command

from obfuscation_core.obfuscators.blur_obfuscator import BlurObfuscator


class CommandBlur(Command):
    id = 6

    def __init__(self):
        self.puzzle_size: int = None

        pass

    def set_params(self, params: dict):
      #puzzle_size = params["puzzle_size"]
        print(params)

    def execute(self) -> BlurObfuscator:
        print("Executing BlurObfuscator!")
        return BlurObfuscator()
