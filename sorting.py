# sort dict by increasing key and decreasing value

from collections import Counter
hello = "hello"
d = { i: x for i, x in enumerate(hello)}
counter = Counter(hello)
counter_list = list(counter)
sorted_tuples = sorted(counter.items(), key=lambda key_value: key_value[1])
sorted_tuples = sorted(d.items())
print(sorted_tuples)
