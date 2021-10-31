import codecs
import pickle

import copy
import cv2
import numpy as np
from numpy import byte, ndarray, number, product, short

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

import codecs

from obfuscation_module.key.key_builder import KeyBuilder
from obfuscation_module.key.key_types.zone_key import ZoneKey
from obfuscation_module.obfuscation_core.obfuscators.encryption_obfuscator import EncryptionObfuscator
from obfuscation_module.obfuscation_core.deobfusators.encryption_deobfuscator import EncryptionDeObfuscator

from tests.key_test.test_key_builder import build_key_test

def get_cut_image(coordinates, image):
    ((x1, y1), (x2, y2)) = coordinates
    return image[y1:y2, x1:x2]

def encryption_test():
    cv2.startWindowThread()
    img: ndarray = cv2.imread('tests\\obfuscation_test\\cute_kitty.jpeg')

    img_og = copy.deepcopy(img)
    s = ((100,100),(300,300))
    img = get_cut_image(s,img)

    kb : KeyBuilder = KeyBuilder(s)
    cv2.imshow('Start', img_og)

    eo2 = EncryptionObfuscator()
    eo2.obfuscate(img,kb)

    zk : ZoneKey = kb.build()
 
    img_og[s[0][0]:s[1][0] , s[0][1]:s[1][1]] = img
    cv2.imshow('Mid', img_og)

    ed2 = EncryptionDeObfuscator()
    ed2.key_data = zk.layers[0].key_data
    ed2.deobfuscate(img)

    img_og[s[0][0]:s[1][0] , s[0][1]:s[1][1]] = img
    cv2.imshow('Final', img_og)
    cv2.waitKey(0)
