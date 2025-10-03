A = set(range(5))
B = set(range(10))
empty_set = set()


def test_set_properties(A, B):
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

    # Intersection
    assert A & A == A
    assert A & A != B
    assert A & B == B & A
    assert A & B <= A
    assert A & B <= B
    assert A & B <= A | B
    assert A & B == A
    print("intersection tests passed")

    # union
    assert A | A == A
    assert A | B >= B
    assert A | B >= A
    assert A | B >= A & B
    assert A | B == B
    assert B | B == B
    print("union tests passed")

    # symmetric diff
    assert A ^ B <= B
    assert A ^ B == B ^ A
    assert A ^ B == (A | B) - (A & B)
    assert (A ^ B) & (A & B) == set()
    print("symmetric diff tests passed")

    print("all set tests passed!")

test_set_properties(A, B)
