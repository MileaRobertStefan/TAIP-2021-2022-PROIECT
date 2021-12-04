import codecs
import copy
import pickle

import numpy as np
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from numpy import ndarray

from key.key_builder import KeyBuilder
from key.key_types.layer import Layer
from obfuscation_core.obfuscators.obfuscator import Obfuscator

sep = "||"
t = np.uint8


def my_encode(s):
    return codecs.encode(s, "base64").decode()


class EncryptionObfuscator(Obfuscator):
    key_size = 16
    id = 150

    def obfuscate(self, image: ndarray, key_builder: KeyBuilder):
        random_generator = Random.new()
        key = random_generator.read(EncryptionObfuscator.key_size)
        iv = random_generator.read(EncryptionObfuscator.key_size)

        shape = copy.deepcopy(image.shape)
        plain_text = image.tobytes()

        cipher_e = AES.new(key, AES.MODE_CBC, iv)
        e = cipher_e.encrypt(pad(plain_text, EncryptionObfuscator.key_size))

        temp: ndarray = np.frombuffer(e, dtype=t)[:len(plain_text)]
        aux: ndarray = np.frombuffer(e, dtype=t)[len(plain_text):]

        temp = temp.reshape(shape)

        for i in range(shape[0]):
            for j in range(shape[1]):
                image[i][j] = temp[i][j]

        key_data = "" + my_encode(key) + sep + my_encode(iv) + sep + my_encode(aux.tobytes()) + sep + my_encode(
            pickle.dumps(shape))
        # print(key_data)
        layer = Layer(EncryptionObfuscator.id, key_data)
        key_builder.set_step(layer)

        if self.next_obfuscator is not None:
            self.next_obfuscator.obfuscate(image, key_builder)
