from typing import List
from obfuscation_core.obfuscators.obfuscator import Obfuscator
from user_interaction.command.command import Command

class ObfuscationFactory:

    def __init__(self) -> None:
        pass

    def create_obfuscation(commands : List[Command]) -> Obfuscator:
        obfuscators = []
    
        for command in commands:
            obfuscators.append( command.execute() )
        
        current_ob = obfuscators[0]
        for ob in obfuscators[1:]:
            current_ob.next_obfuscator = ob
            current_ob = ob
           
        return obfuscators[0]
    pass



