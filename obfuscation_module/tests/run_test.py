key_test = False
obfuscation_test = True

if key_test:
    from obfuscation_module.tests.key_test.test_key_type import *
    from obfuscation_module.tests.key_test.test_key_builder import *
    from obfuscation_module.tests.key_test.test_parse_key import *

    key_types_test = False
    key_builder = True

    if key_types_test:
        layer_test()
        zone_key_test()        
        master_key_test()


    # build_key_test()
    parse_key_test()

if obfuscation_test == True:
    from obfuscation_module.tests.integration_tests.obfuscation_test.XOR_test import *
    from obfuscation_module.tests.integration_tests.obfuscation_test.encryption_test import*
    
    #obfuscation_xor_test()
    encryption_test()


      
