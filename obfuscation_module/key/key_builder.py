from typing import List, Tuple

from obfuscation_module.key.key_types.layer import Layer
from obfuscation_module.key.key_types.zone_key import ZoneKey
class KeyBuilder:
    def __init__(self, coord: Tuple[Tuple[int]]):
        self.key: ZoneKey = ZoneKey(
            coord,
            []
        )
        self.steps: List[Layer] = []

    def reset(self) -> None:
        self.key = ZoneKey()
        self.steps = []

    def set_step(self, layer: Layer) -> None:
        self.key.layers.append(layer)
        self.steps.append(layer)

    def build(self) -> ZoneKey:
        zk: ZoneKey = ZoneKey(self.key.coordonates, self.steps)
        self.key = zk
        return self.key

