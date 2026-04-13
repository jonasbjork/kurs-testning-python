import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(5, 3) == 8
    assert calc.add(-5, 3) == -2

def test_divide_by_zero(calc):
    assert calc.divide(10, 0) == "Error"

def test_sqrt_negative(calc):
    assert calc.sqrt(-16) == "Error"

def test_modulo_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.modulo(10, 0)
