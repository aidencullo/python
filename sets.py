A = set(range(5))
B = set(range(10))


def test_difference(A, B):
    empty_set = set()
    # difference
    A_B = A - B
    B_A = B - A
    assert A.difference(B) == A_B
    assert A_B == empty_set
    assert not A_B
    assert A_B <= B
    assert A_B <= A
    assert B_A <= B
    assert not (A <= B_A)
    print("difference tests passed")


def test_subset(A, B):
    # subset
    assert A <= B
    assert A <= A
    assert A < B
    assert not (A < A)
    assert not (B <= A)
    assert not (B < A)
    assert A.issubset(B)
    assert A.issubset(A)
    assert not B.issubset(A)
    print("subset tests passed")


def test_intersection(A, B):
    # Intersection
    assert A & A == A
    assert A & A != B
    assert A & B == B & A
    assert A & B <= A
    assert A & B <= B
    assert A & B <= A | B
    assert A & B == A
    print("intersection tests passed")


def test_union(A, B):
    # union
    assert A | A == A
    assert A | B >= B
    assert A | B >= A
    assert A | B >= A & B
    assert A | B == B
    assert B | B == B
    print("union tests passed")


def test_symmetric_diff(A, B):
    # symmetric diff
    assert A ^ B <= B
    assert A ^ B == B ^ A
    assert A ^ B == (A | B) - (A & B)
    assert (A ^ B) & (A & B) == set()
    print("symmetric diff tests passed")


def test_set_properties(A, B):
    test_difference(A, B)
    test_subset(A, B)
    test_intersection(A, B)
    test_union(A, B)
    test_symmetric_diff(A, B)

    print("all set tests passed!")


test_set_properties(A, B)