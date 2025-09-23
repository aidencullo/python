from functools import partial

def starts_with(s, prefix):
    return s.startswith(prefix)

def filter_strs(strs):
    starts_with_a = partial(starts_with, prefix='a')
    lst = list(filter(starts_with_a, strs))
    return lst
