from API.backend.Comm.command import Command

from  obfuscation_core.obfuscators.color_obfuscator import ColorObfuscator

class CommandColor(Command):
    id = 4

    def __init__(self):
        self.key: str = ""

        pass

    def set_params(self, params : dict) :
        print(params)
        # self.key = params["key"]

    def execute(self) -> ColorObfuscator:
        print("Executing ColorObfuscator!")
        return ColorObfuscator()
