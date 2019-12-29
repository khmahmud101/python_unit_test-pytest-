import math_func
import pytest
@pytest.mark.number
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
@pytest.mark.number
def test_product():
    assert math_func.product(7,3) == 21
    assert math_func.product(7) == 14
    assert math_func.product(5) == 9
@pytest.mark.strings
def test_add_string():
    result = math_func.add('Hello ','world')
    assert result == 'Hello world'
    assert type(result) is str
    assert 'Hello' in result

@pytest.mark.strings
def test_product_string():
    assert math_func.product('Hello ',3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result