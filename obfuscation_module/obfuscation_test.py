import copy
import argparse
import os

import sys

import cv2

from numpy import ndarray

from key.key_builder import KeyBuilder
from key.key_types.zone_key import ZoneKey
from obfuscation_core.factory.deobfuscation_factory import DeobfuscationFactory
from obfuscation_core.obfuscation_context import ObfuscationContext
from obfuscation_core.obfuscators.XOR_obfuscator import XORObfuscator
from obfuscation_core.obfuscators.affine_obfuscator import AffineObfuscator
from obfuscation_core.obfuscators.color_obfuscator import ColorObfuscator
from obfuscation_core.obfuscators.encryption_obfuscator import EncryptionObfuscator

from obfuscation_core.obfuscators.puzzle_obfuscator import PuzzleObfuscator
from obfuscation_core.obfuscators.scramble_obfuscator import ScrambleObfuscator

OBFUSCATORS = {
    'affine': AffineObfuscator(),
    'color': ColorObfuscator(),
    'encryption': EncryptionObfuscator(),
    'xor': XORObfuscator(),
    'puzzle':  PuzzleObfuscator(),
    'scramble': ScrambleObfuscator(),
    'all': ObfuscationContext()
}

sys.path.append('key')


def get_cut_image(coordinates, image):
    ((x1, y1), (x2, y2)) = coordinates
    return image[y1:y2, x1:x2]


def get_image_path():
    if os.path.exists('tests/integration_tests/obfuscation_test/cute_kitty.jpeg'):
        return 'tests/integration_tests/obfuscation_test/cute_kitty.jpeg'
    return 'cute_kitty.jpeg'


if __name__ == '__main__':
    possible_modes = []
    for key in OBFUSCATORS:
        possible_modes.append(key)
    parser = argparse.ArgumentParser(description="Obfuscation tests")
    parser.add_argument('--obfuscator', '-o', default="all", help="Obfuscator", choices=possible_modes)

    cv2.startWindowThread()
    img: ndarray = cv2.imread(get_image_path())

    img_og = copy.deepcopy(img)
    s = ((100, 100), (300, 300))
    img = get_cut_image(s, img)

    kb: KeyBuilder = KeyBuilder(s)
    cv2.imshow('Start', img_og)

    args = parser.parse_args(sys.argv[1:])
    OBFUSCATORS[args.obfuscator].obfuscate(img, kb)

    zk: ZoneKey = kb.build()

    img_og[s[0][0]:s[1][0], s[0][1]:s[1][1]] = img
    cv2.imshow('Mid', img_og)

    ed2 = DeobfuscationFactory().create_deobfuscation(zk)
    ed2.deobfuscate(img)

    img_og[s[0][0]:s[1][0], s[0][1]:s[1][1]] = img
    cv2.imshow('Final', img_og)
    cv2.waitKey(0)
