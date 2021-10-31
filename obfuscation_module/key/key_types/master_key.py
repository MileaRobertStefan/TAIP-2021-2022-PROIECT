import copy
import pickle as pk
import zlib


from typing import List,Tuple

from key.key_types.zone_key import ZoneKey
from key.key_types.layer import Layer
import codecs

class MasterKey:
    zones: List[ZoneKey] = []

    def __init__(self, zones: List[ZoneKey]) -> None:
        self.zones = copy.deepcopy(zones)

    def __repr__(self) -> str:
        return "" + str(self.zones)
        pass

    def to_string(self):
        pickled = pk.dumps(self)
        pickled = zlib.compress(pickled)
        pickled = codecs.encode(pickled, "base64").decode()
        return pickled



    pass
