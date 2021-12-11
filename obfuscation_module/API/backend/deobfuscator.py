import json
import pickle
import zlib
import codecs
import os

from key.key_types.zone_key import ZoneKey
from obfuscation_core.factory.deobfuscation_factory import DeobfuscationFactory

from cv2 import  cv2

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Deobfuscator:

    @staticmethod
    def parse_key(key: str) -> ZoneKey:
        unpickled = codecs.decode(key.encode(), "base64")
        unpickled = zlib.decompress(unpickled)
        unpickled = pickle.loads(unpickled)
        return unpickled

    @staticmethod
    def post(image_id : int , zones:str):
        try:
            print("deobfuscator start")

            img = cv2.imread(__location__ + "/images/" + image_id + ".png")


            zones:dict = json.loads(zones)

            df = DeobfuscationFactory()

            for key, val in zones.items():
                zone = Deobfuscator.parse_key(val)

                a ,b =  zone.coordinates
                temp_img = img[a[0]:b[0],a[1]:b[1]]
                starting_node = df.create_deobfuscation(zone)
                try:
                    starting_node.deobfuscate(temp_img)
                except Exception as e:
                    print("ERR:", e)



            cv2.imshow("deobfuscata",img)
            cv2.waitKey(0)

            print("deobfuscator stop")
            retval, buffer = cv2.imencode('.png', img)
            return  buffer
        except Exception as e:
            print(e)

    pass


