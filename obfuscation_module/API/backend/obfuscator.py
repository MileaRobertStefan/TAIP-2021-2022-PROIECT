from typing import *

import json

from key.key_types.master_key import MasterKey
from key.key_types.zone_key import ZoneKey
from key.key_builder import KeyBuilder

from obfuscation_core.factory.obfuscastor_factory import ObfuscationFactory
from API.backend.Comm.export import *
from obfuscation_core.obfuscators.obfuscator import Obfuscator
import numpy as np

from cv2 import cv2 as cv

of = ObfuscationFactory()


class Obfuscastor:
    @staticmethod
    def get(self):
        pass

    @staticmethod
    def post(photo, the_json: dict):
        mk = MasterKey.loadJson(the_json)

        chain_of_commands = []
        for z in mk.zones:
            print(z)
            commands: List[Command] = []
            for l in z.layers:
                try:
                    c = get_command(int(l.alg_id))
                    c.set_params(l.key_data)
                    commands.append(c)
                except KeyError:

                    print("Error!", l )

            ob: Obfuscator = of.create_obfuscation(commands)
            chain_of_commands.append((ob, z.coordinates))

        img = cv.imdecode(np.fromstring(photo.read(), np.uint8), cv.IMREAD_COLOR)
        print(chain_of_commands)
        masterKey  = MasterKey([])


        for obf, coord in chain_of_commands:
            kb: KeyBuilder = KeyBuilder(coord)
            img2 = img[coord[0][0]:coord[1][0], coord[0][1]:coord[1][1]]
            obf.obfuscate(img2, kb)

            img[coord[0][0]:coord[1][0], coord[0][1]:coord[1][1]] = img2
            masterKey.zones.append(kb.build())

        cv.imshow("Poza mea!", img)

        cv.waitKey(0)

        return json.dumps({"masterKey": masterKey.to_string()})
        pass

    def __init__(self):
        pass
