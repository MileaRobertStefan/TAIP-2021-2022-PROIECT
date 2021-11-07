from typing import *

import json

from key.key_types.master_key import MasterKey
from key.key_types.zone_key import ZoneKey

from obfuscation_core.factory.obfuscastor_factory import ObfuscationFactory
from API.backend.Comm.export import *
from obfuscation_core.obfuscators.obfuscator import Obfuscator
import  numpy as np

import  cv2

of = ObfuscationFactory()

class Obfuscastor:
    @staticmethod
    def get(self):
        pass

    @staticmethod
    def post(photo, the_json: dict):
        mk = MasterKey.loadJson(the_json)


        chain_of_commands: List[Obfuscator] = []
        for z in mk.zones:
            commands: List[Command] = []
            for l in z.layers:
                try:
                    c = get_command(l.alg_id)
                    c.set_params(l.key_data)
                    commands.append(c)
                except KeyError:
                    print("Error!")
            ob: Obfuscator = of.create_obfuscation(commands)
            chain_of_commands.append(ob)

        #print(chain_of_commands)

        img = cv2.imdecode(np.fromstring( photo.read(), np.uint8), cv2.IMREAD_COLOR)

        # cv2.imshow('Mid', img)
        # cv2.waitKey(0)
        return json.dumps(the_json)
        pass

    def __init__(self):
        pass
