"""
Unit testing for the calculator library
"""
import calculator

class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2,2), "Adding two numbers should return their sum."

    def test_substraction(self):
        assert 10 == calculator.subtract(15,5), "-5 from a number is that number minus 5."