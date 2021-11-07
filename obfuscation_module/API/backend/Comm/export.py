from  API.backend.Comm.command import *
from  API.backend.Comm.CommandEncryption import *

ALL_COMMANDS_DICT = {
    CommandEncryption.id : CommandEncryption
}


# will crash if the comm_id is not in ALL_COMMANDS_DICT
def get_command(comm_id : int) -> Command:
    return ALL_COMMANDS_DICT[comm_id]()
