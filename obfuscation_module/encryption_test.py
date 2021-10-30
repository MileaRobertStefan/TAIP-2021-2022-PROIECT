# from obfuscation_core.obfuscation_context import ObfuscationContext
import cv2

from key.key_builder import KeyBuilder
from obfuscation_core.factory.deobfuscation_factory import DeobfuscationFactory
from obfuscation_core.obfuscation_context import ObfuscationContext


def get_cut_image( coordinates, image):
    ((x1, y1), (x2, y2)) = coordinates
    return image[y1:y2, x1:x2]

if __name__ == '__main__':
    print("saluttt")
    cv2.startWindowThread()
    img = cv2.imread('download.jpeg')




    oc = ObfuscationContext()
    oc.init_obfuscators()
    coords = ((0, 0), (100, 100))
    img = get_cut_image(coords, img)
    cv2.imshow('Start', img)

    keyBuilder = KeyBuilder(coords)
    oc.obfuscate(img, keyBuilder)

    zoneKey = keyBuilder.build()
    cv2.imshow('Encrypt', img)

    deobfuscator = DeobfuscationFactory().create_deobfuscation(zoneKey)
    deobfuscator.deobfuscate(img)

    cv2.imshow('Decrypt', img)

    cv2.waitKey(0)