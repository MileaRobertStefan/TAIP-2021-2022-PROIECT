import json
from typing import List, Tuple
import copy 
from key.key_types.layer import Layer


class ZoneKey:
    coordonates: Tuple[Tuple[int]] = ()
    layers: List[Layer] = []

    def __init__(self, coordonates: Tuple[Tuple[int]], layers: List[Layer]) -> None:
        self.coordonates = copy.deepcopy(coordonates)
        self.layers = copy.deepcopy(layers)
        pass
    
    def __repr__(self) -> str:
        return f""" 
    coord : {self.coordonates}
    layers  {self.layers}
\n"""

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    pass

