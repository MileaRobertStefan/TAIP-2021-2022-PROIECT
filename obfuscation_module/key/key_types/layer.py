class Layer:
    alg_id: int
    key_data: str

    def __init__(self, alg_id, key_data) -> None:
        self.alg_id = alg_id
        self.key_data = key_data
        pass

    def __eq__(self, other):
        return self.alg_id == other.alg_id and self.key_data == other.key_data
