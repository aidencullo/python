class A:
    pass

class B:
    __slots__ = ("x",)

a = A()
b = B()

a.x = 1
a.y = 2          # OK: dynamic attributes


import pytest

def test_division_by_zero():
    with pytest.raises(AttributeError):
        b.y = 2          # AttributeError

test_division_by_zero()

b.x = 1


class A:

    @property
    def a(self):
        return 1

a = A()
a.a


class MyClass:
    def __str__(self):
        return "Custom string representation"

obj = MyClass()
print(str(obj))  # Calls obj.__str__()
# Output: Custom string representation

import pytest

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
