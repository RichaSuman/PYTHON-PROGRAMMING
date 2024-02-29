import pytest 

def capital_case(x):
    if not isinstance(x,str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()

def test_capital_case1():
    assert capital_case('semaphore')=='Semaphore'

def test_capital_case2():
    assert capital_case('semaphore')=='sEmaphore'

def test_capital_case3():
    with pytest.raises(TypeError):
        capital_case(9)

def test_uppercase():
    assert "test".upper() == "TEST"

def test_reversed():
    assert list(reversed([1,2,3,4])) == [4,3,2,1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2,50)
        if not any (num % div == 0 for div in range(2,num))
    }
