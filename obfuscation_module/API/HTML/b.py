import  json

from key.key_types.master_key import MasterKey

a = json.loads("{\"zones\": [{\"coordonates\": [[0, 0], [100, 100]], \"layers\": [{\"alg_id\": 1, \"key_data\": \"test-1\"}, {\"alg_id\": 2, \"key_data\": \"test-2\"}, {\"alg_id\": 3, \"key_data\": \"test-3\"}]}, {\"coordonates\": [[0, 0], [100, 100]], \"layers\": [{\"alg_id\": 1, \"key_data\": \"test-1\"}, {\"alg_id\": 2, \"key_data\": \"test-2\"}, {\"alg_id\": 3, \"key_data\": \"test-3\"}]}, {\"coordonates\": [[0, 0], [100, 100]], \"layers\": [{\"alg_id\": 1, \"key_data\": \"test-1\"}, {\"alg_id\": 2, \"key_data\": \"test-2\"}, {\"alg_id\": 3, \"key_data\": \"test-3\"}]}]}")


print(type(a), a)
