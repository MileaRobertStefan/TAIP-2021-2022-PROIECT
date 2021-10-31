# from obfuscation_core.obfuscation_context import ObfuscationContext
import cv2
from numpy import ndarray

from obfuscation_module.key.key_builder import KeyBuilder
from obfuscation_module.obfuscation_core.factory.deobfuscation_factory import DeobfuscationFactory
from obfuscation_module.obfuscation_core.obfuscation_context import ObfuscationContext


def get_cut_image(coordinates, image):
    ((x1, y1), (x2, y2)) = coordinates
    return image[y1:y2, x1:x2]


def obfuscation_encryption_test():
    cv2.startWindowThread()
    img: ndarray = cv2.imread('tests\\obfuscation_test\download.jpeg')
    print(img)
    oc = ObfuscationContext()
    oc.init_obfuscators()
    coords = ((0, 0), (100, 100))
    img = get_cut_image(coords, img)
    cv2.imshow('Start', img)

    keyBuilder = KeyBuilder(coords)
    oc.obfuscate(img, keyBuilder)

    zoneKey = keyBuilder.build()
    cv2.imshow('Image after obfuscation', img)

    deobfuscator = DeobfuscationFactory().create_deobfuscation(zoneKey)
    deobfuscator.deobfuscate(img)

    cv2.imshow('Image after deobfuscation', img)

    cv2.waitKey(0)
