from numb3rs import validate

def test_invalid_adress():
    assert validate("512.1.1.0") == False
    assert validate("512.512.512.512") == False
    assert validate("0.0.275.1.1.0") == False
    assert validate("275-1.1.0") == False
    assert validate("199.911.288.882") == False
    assert validate("0.1.1?0") == False
    assert validate("cat") == False
    assert validate("1.1.1.1000") == False

def test_valid_adress():
    assert validate("1.1.1.0") == True
    #assert validate("255.255.255.0") == True
    assert validate("1.2.3.4") == True
    assert validate("87.45.72.12") == True
    assert validate("249.249.249.249") == True
