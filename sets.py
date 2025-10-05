empty_set = set()


def test_difference(A, B):

    A_B = A - B
    B_A = B - A
    assert A.difference(B) == A_B
    assert A_B <= A
    assert B_A <= B
    if A:
        assert not (A <= B_A)
    print("difference tests passed")


def test_subset(A, B):

    C = A - {1, 2}
    assert A <= A
    assert C <= A
    assert B <= B
    assert not (A < A)
    assert empty_set.issubset(B)
    assert empty_set.issubset(A)
    print("subset tests passed")


def test_intersection(A, B):

    sets = (A, B)
    assert A & A == A
    assert A & B == B & A
    assert A & B <= A
    assert A & B <= B
    assert A & B <= A | B
    if A <= B:
        assert A & B == A
    assert set.intersection(*sets) <= A
    assert set.intersection(*sets) <= B
    print("intersection tests passed")


def test_union(A, B):

    sets = (A, B)

    assert A | A == A
    assert A | B >= B
    assert A | B >= A
    assert A | B >= A & B
    if A <= B:
        assert A | B == B
    assert B | B == B
    assert set.union(*sets) == A | B
    assert A <= set.union(*sets)
    print("union tests passed")


def test_symmetric_diff(A, B):

    if A <= B:
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
        ({1, 2, 3}, {3, 4, 5}),
        (set("hello"), set("world")),
        ({1, 2}, {1, 2, 3, 4}),
        ({1, 2, 3, 4}, {1, 2}),
        (set(), set()),
    ]

    for i, (A, B) in enumerate(set_pairs):
        print(f"\n--- Running test case {i+1} with A={A} and B={B} ---")
        test_set_properties(A, B)


def main():
    run_test_suite()


if __name__ == "__main__":
    main()
main()
