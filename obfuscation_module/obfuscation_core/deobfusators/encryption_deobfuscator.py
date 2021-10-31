import codecs
import pickle
import cv2
import numpy as np
from numpy import ndarray

from obfuscation_core.deobfusators.deobfuscator import DeObfuscator


from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad


def my_decode(s: str):
    return codecs.decode(s.encode(), "base64")


class EncryptionDeObfuscator(DeObfuscator):
    def parse_key_data(self):
        words = self.key_data.split("||")

        key, iv, rest, shape = words

        key = my_decode(key)
        iv = my_decode(iv)
        rest = np.frombuffer(my_decode(rest), dtype=np.uint8)
        shape = pickle.loads(my_decode(shape))


        return key, iv, rest, shape

    def deobfuscate(self, image: ndarray):
        key, iv, rest, shape = self.parse_key_data()

        temp_img = image.ravel()

        cipher_text = np.concatenate( (temp_img, rest) )
        cipher_text = cipher_text.tobytes()

        cipher_d = AES.new(key, AES.MODE_CBC, iv)

        d = unpad(cipher_d.decrypt(cipher_text), 16)

        rez: ndarray = np.frombuffer(d, np.uint8)
        rez = rez.reshape(shape)

        for i in range(shape[0]):
           for j in range(shape[1]):
               image[i][j] = rez[i][j]


        if self.next_deobfuscator is not None:
            self.next_deobfuscator.deobfuscate(image)
