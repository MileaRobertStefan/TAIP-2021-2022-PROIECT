from API.backend.Comm.command import Command

from  obfuscation_core.obfuscators.encryption_obfuscator import EncryptionObfuscator

class CommandEncryption(Command):
    id = 1

    def __init__(self):
        self.key: str = ""

        pass

    def set_params(self, params : dict) :
        print(params)

        self.key = params["key"]



    def execute(self) -> EncryptionObfuscator:
        print("Executing CommandEncryption!")
        return EncryptionObfuscator()
