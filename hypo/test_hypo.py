from hypothesis import given
from hypothesis.strategies import integers

@given(integers(), integers())
def test_addition(x, y):
    assert x + y == y + x
