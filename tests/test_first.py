from hello_world import add, sub, mult, divide

def testAdd():
    assert add(2 , 2) == 4

def testmult():
    assert mult(5 , 10 ) == 50


def testsub():
    assert sub(10 , 6) == 4

def test_divide():
    assert divide(18, 6) == 3