from obfuscation_module.key.key_builder import *


def build_key_test():

    kb: KeyBuilder = KeyBuilder(((0, 0), (100, 100)))

    layers: list[Layer] = [
        Layer(1, "test-1"), Layer(2, "test-2"), Layer(3, "test-3")
    ]

    for l in layers:
        kb.set_step(l)

    zk: ZoneKey = kb.build()

    print(zk)
        
