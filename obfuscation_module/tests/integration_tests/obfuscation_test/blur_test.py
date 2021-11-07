import copy

import cv2
from numpy import ndarray

from key.key_builder import KeyBuilder
from key.key_types.zone_key import ZoneKey
from obfuscation_core.deobfusators.blur_deobfuscator import BlurDeObfuscator
from obfuscation_core.obfuscators.blur_obfuscator import BlurObfuscator
from obfuscation_test import get_image_path


def get_cut_image(coordinates, image):
    ((x1, y1), (x2, y2)) = coordinates
    return image[y1:y2, x1:x2]


def blur_test():
    cv2.startWindowThread()
    img: ndarray = cv2.imread(get_image_path())

    img_og = copy.deepcopy(img)
    s = ((100, 100), (300, 300))
    img = get_cut_image(s, img)

    kb: KeyBuilder = KeyBuilder(s)
    cv2.imshow('Start', img_og)

    eo2 = BlurObfuscator()
    eo2.obfuscate(img, kb)

    zk: ZoneKey = kb.build()

    img_og[s[0][0]:s[1][0], s[0][1]:s[1][1]] = img
    cv2.imshow('Mid', img_og)

    ed2 = BlurDeObfuscator()
    ed2.key_data = zk.layers[0].key_data
    ed2.deobfuscate(img)

    img_og[s[0][0]:s[1][0], s[0][1]:s[1][1]] = img
    cv2.imshow('Final', img_og)
    cv2.waitKey(0)


if __name__ == '__main__':
    blur_test()
