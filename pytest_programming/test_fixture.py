import pytest

@pytest.fixture
def my_state():
    state = {"value": 0}     # set up state
    return state

def test_my_function(my_state):
    my_state["value"] += 1
    assert my_state["value"] == 1

def test_my_other_function(my_state):
    my_state["value"] += 1
    assert my_state["value"] == 1


class Calculator:
        def __init__(self,Initial_value=0):
             self.value = Initial_value

        def add(self,num):
             self.value += num
        
        def sub(self,num):
             self.value -= num

@pytest.fixture
def calculator_factory():
     calculator = Calculator(Initial_value=10)
     yield calculator
     # Cleanup or teardown code can be added here if needed
     

def test_calculator_add(calculator_factory):
     calculator_factory.add(5)
     assert calculator_factory.value == 15

def test_calculator_sub(calculator_factory):
     calculator_factory.sub(3)
     assert calculator_factory.value == 7
