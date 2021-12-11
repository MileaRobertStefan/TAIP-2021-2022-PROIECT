import json
import os
from random import random
from typing import *

import cv2
import numpy as np

from API.backend.Comm.export import *
from key.key_builder import KeyBuilder
from key.key_types.master_key import MasterKey
from obfuscation_core.factory.obfuscastor_factory import ObfuscationFactory
from obfuscation_core.obfuscators.obfuscator import Obfuscator

of = ObfuscationFactory()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

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

                    print("Error!", l)

            ob: Obfuscator = of.create_obfuscation(commands)
            chain_of_commands.append((ob, z.coordinates))

        img = cv2.imdecode(np.fromstring(photo.read(), np.uint8), cv2.IMREAD_COLOR)
        print(chain_of_commands)
        masterKey = MasterKey([])

        for obf, coord in chain_of_commands:
            kb: KeyBuilder = KeyBuilder(coord)
            img2 = img[coord[0][0]:coord[1][0], coord[0][1]:coord[1][1]]
            obf.obfuscate(img2, kb)

            img[coord[0][0]:coord[1][0], coord[0][1]:coord[1][1]] = img2
            masterKey.zones.append(kb.build())

        random_name = str(int(random() * 100000000))
        cv2.imwrite(__location__ + "/images/" + random_name + ".png", img)

        return json.dumps({
            "image_id": random_name,
            "zone_keys": masterKey.encodedZoneKeys()
        })

    def __init__(self):
        pass
