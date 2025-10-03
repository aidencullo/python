A = set(range(5))
B = set(range(10))
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

# subset

# intersection

# union

# symmetric diff

# xor?

# empty

