class A:
    pass

class B:
    __slots__ = ("x",)

a = A()
b = B()

a.x = 1
a.y = 2          # OK: dynamic attributes

b.x = 1
b.y = 2          # AttributeError


class A:

    @property
    def a(self):
        return 1

a = A()
a.a
