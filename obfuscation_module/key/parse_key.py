from key.key_types.master_key import MasterKey


class Parse_Key_Builder:
    key: MasterKey

    def __init__(self, key: str):
        self.key = self.parse_key(key)

    def parse_key(self, key: str) -> MasterKey:
        # TODO parse key
        return key
