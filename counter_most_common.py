from collections import Counter

data = ['a', 'b', 'a', 'b', 'c', 'c']
counter = Counter(data)

# [('a', 2), ('b', 2)]
assert counter.most_common(2) == [('a', 2), ('b', 2)]
from collections import Counter

data = ['a', 'b', 'a', 'b', 'c', 'c']
data.reverse()
counter = Counter(data)

# [('c', 2), ('b', 2)]
assert counter.most_common(2) == [('c', 2), ('b', 2)]

