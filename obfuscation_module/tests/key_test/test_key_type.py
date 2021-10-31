from key.key_types.export import *  
from typing import *

def layer_test():
    print("Start Test of Layer")
    test_data = (10,"some random data")
    layer = Layer(*test_data)
    print(f"data input : {test_data}" )
    print(f"data saved : {layer}")
    print("End Test of Layer")


def zone_key_test():    
    print("Start Test ZoneKey")
    test_data: Tuple[Layer] = [
        Layer(*td) for td in [(1, "aaa"), (2, "bbb"), (3, "ccc"), (4, "ddd"), (5, "eee")]
    ]
    print(f"input data :{test_data}")
    coord = ((0,0) , (300,300))
    zk: ZoneKey = ZoneKey(coord, test_data)
    print(f"stored data : {zk}")
    print("End Test ZoneKey")


def master_key_test():
    print("Start Test Master Key")
    test_data: Tuple[Layer] = [
        Layer(*td) for td in [(1, "aaa"), (2, "bbb"), (3, "ccc"), (4, "ddd"), (5, "eee")]
    ]
    coords = [
        ( (0 + i) , (300 + i) ) for i in range(3) 
    ]
    input_data = [ ZoneKey(coord, test_data) for coord in coords]
    mk: MasterKey = MasterKey(input_data)
    print(mk)
    print("End Test Master Key")