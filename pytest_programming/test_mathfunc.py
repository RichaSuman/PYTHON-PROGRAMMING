import pytest

class Algerba:
    def square(x):
        return x**2
    
    def cube(x):
        return x**3
    
class Geometry:
    def is_triangle(a,b,c):
        return a+b+c == 180
    
    def is_quadrilateral(w,x,y,z):
        return w+x+y+z == 360 
'''
## Using class for grouping the tests

class Test_Algebra:
    def test_square(self):
        assert Algerba.square(4) == 16
        assert Algerba.square(10) == 100

    def test_cube(self):
        assert Algerba.cube(4) == 64
        assert Algerba.cube(9) == 729
    
class Test_Geometry:
    def test_is_triangle(self):
        assert Geometry.is_triangle(50,60,70) == True
        assert Geometry.is_triangle(90,90,90) == False

    def test_is_quadilateral(self):
        assert Geometry.is_quadrilateral(350,5,5,0) == True
        assert Geometry.is_quadrilateral(11,22,33,44) == False
'''
## Using pytest marker to group the tests
@pytest.mark.algerba
def test_square():
        assert Algerba.square(4) == 16
        assert Algerba.square(10) == 100

@pytest.mark.algerba
def test_cube():
        assert Algerba.cube(4) == 64
        assert Algerba.cube(9) == 729

@pytest.mark.geometry
def test_is_triangle():
        assert Geometry.is_triangle(50,60,70) == True
        assert Geometry.is_triangle(90,90,90) == False

@pytest.mark.geometry
def test_is_quadilateral():
        assert Geometry.is_quadrilateral(350,5,5,0) == True
        assert Geometry.is_quadrilateral(11,22,33,44) == False

## we can also group them by writing them in seperate files
        
        
# to run all the 4 tests : pytest test_mathfunc.py -v
# to run a perticluar class : pytest test_mathfunc.py::Test_Algebra -v
# to run with a perticular marker :  pytest -vm algerba test_mathfunc.py