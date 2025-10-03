empty_set = set()

def test_difference(A, B):

    A_B = A - B
    B_A = B - A
    assert A.difference(B) == A_B
    assert not A_B
    assert A_B <= B
    assert A_B <= A
    assert B_A <= B
    assert not (A <= B_A)
    print("difference tests passed")


def test_subset(A, B):

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

    assert A & A == A
    assert A & A != B
    assert A & B == B & A
    assert A & B <= A
    assert A & B <= B
    assert A & B <= A | B
    assert A & B == A
    print("intersection tests passed")


def test_union(A, B):

    assert A | A == A
    assert A | B >= B
    assert A | B >= A
    assert A | B >= A & B
    assert A | B == B
    assert B | B == B
    print("union tests passed")


def test_symmetric_diff(A, B):

    assert A ^ B <= B
    assert A ^ B == B ^ A
    assert A ^ B == (A | B) - (A & B)
    assert (A ^ B) & (A & B) == empty_set
    print("symmetric diff tests passed")


def test_set_properties(A, B):
    test_difference(A, B)
    test_subset(A, B)
    test_intersection(A, B)
    test_union(A, B)
    test_symmetric_diff(A, B)

    print("all set tests passed!")


def run_test_suite():
    set_pairs = [
        (set(range(5)), set(range(10))),
        (set(range(10)), set(range(5))),
        (set(range(5)), set(range(5))),
        (set(), set(range(5))),
        (set(range(5)), set()),
    ]

    for i, (A, B) in enumerate(set_pairs):
        print(f"\n--- Running test case {i+1} ---")
        test_set_properties(A, B)


def main():
    run_test_suite()


if __name__ == "__main__":
    main()
