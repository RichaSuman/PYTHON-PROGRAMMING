import pytest

def func(a,b):
    return a==b

@pytest.mark.parametrize("value_a,value_b,result", [
    (2,2,True),
    (15,3*5,True)
     ])
def test_func(value_a,value_b,result):
    assert func(value_a,value_b) == result