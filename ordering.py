import functools

@functools.total_ordering
class Point:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x < other.x

p1 = Point(1)
p2 = Point(2)

print(p1 <= p2)  # True (auto)
print(p1 > p2)   # False (auto)
print(p1 == p2)   # False (auto)
