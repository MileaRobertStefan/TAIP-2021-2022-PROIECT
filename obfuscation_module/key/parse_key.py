from key.key_types.master_key import MasterKey

import pickle
import zlib
import codecs

class Parse_Key_Builder:
    key: MasterKey

    def __init__(self, key: str):
        self.key = self.parse_key(key)

    def parse_key(self, key: str) -> MasterKey:
        unpickled = pickle.loads(codecs.decode(key.encode(), "base64"))
        return unpickled

def parse_key(key: str) ->  MasterKey:
    unpickled = codecs.decode(key.encode(), "base64")
    unpickled = zlib.decompress(unpickled)
    unpickled = pickle.loads(unpickled)
   
    return unpickled
