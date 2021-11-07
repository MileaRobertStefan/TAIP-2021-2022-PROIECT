from key.parse_key import *
from key.key_types.master_key import *



def parse_key_test():

    coords = ((0, 0), (100, 100))
    layers: list[Layer] = [
        Layer(1, "test-1"), Layer(2, "test-2"), Layer(3, "test-3")
    ]

    zone_keys = [
        ZoneKey(coords, layers)   for _ in range(3)
    ]

    mk: MasterKey = MasterKey(zone_keys)

    mk_str: str = mk.to_string()

    print(mk_str)

    parsed_mk: MasterKey = parse_key(mk_str)

    print(parsed_mk)


if __name__ == '__main__':
    parse_key_test()
