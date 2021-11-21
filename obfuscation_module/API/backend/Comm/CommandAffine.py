from API.backend.Comm.command import Command
from  obfuscation_core.obfuscators.affine_obfuscator import AffineObfuscator


class CommandAffine(Command):
    id = 1

    def __init__(self):
        self.key: str = ""

        pass

    def set_params(self, params : dict) :
        print(params)


    def execute(self) -> AffineObfuscator:
        print("Executing AffineObfuscator!")
        return AffineObfuscator()
