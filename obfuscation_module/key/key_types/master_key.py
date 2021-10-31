import copy
import pickle as pk
from typing import List,Tuple

from obfuscation_module.key.key_types.zone_key import ZoneKey
from obfuscation_module.key.key_types.layer import Layer
import codecs

class MasterKey:
    zones: List[ZoneKey] = []

    def __init__(self, zones: List[ZoneKey]) -> None:
        self.zones = copy.deepcopy(zones)

    def __repr__(self) -> str:
        return "" + str(self.zones)
        pass

    def to_string(self):
        pickled = codecs.encode(pk.dumps(self), "base64").decode()


        return pickled



    pass
