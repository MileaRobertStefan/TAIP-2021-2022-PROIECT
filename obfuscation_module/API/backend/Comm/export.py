from API.backend.Comm.CommandAffine import *
from API.backend.Comm.CommandColor import *
from API.backend.Comm.CommandEncryption import *
from API.backend.Comm.CommandPuzzle import *
from API.backend.Comm.CommandScramble import *
from API.backend.Comm.CommandXOR import *

ALL_COMMANDS_DICT = {
    CommandAffine.id: CommandAffine,
    CommandEncryption.id: CommandEncryption,
    CommandScramble.id: CommandScramble,
    CommandColor.id: CommandColor,
    CommandPuzzle.id: CommandPuzzle,
    CommandXOR.id: CommandXOR
}


# will crash if the comm_id is not in ALL_COMMANDS_DICT
def get_command(comm_id: int) -> Command:
    return ALL_COMMANDS_DICT[comm_id]()
