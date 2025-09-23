# filter_dicts.py

from typing import List, Dict

def filter_dicts(data: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """
    Filter a list of dictionaries, keeping only those where:
    - 'name' starts with 'a'
    - 'score' is greater than 10
    """
    from functools import partial
    def starts_with_a_and_greater_than_ten(pair):
        name, score = data["name"], data["score"]
        key, value = name, score
        print(key, value)
        if not key.startswith('a'):
            return False
        if value <= 10:
            return False        
        return True
    filtered = list(filter(starts_with_a_and_greater_than_ten, data)
    )
    return filtered

# ====== Tests ======

test_data = [
    {"name": "alice", "score": 12},
    {"name": "amy", "score": 5},
    {"name": "bob", "score": 15},
    {"name": "andrew", "score": 20},
    {"name": "anna", "score": 10},
]

# Expected output
expected = [
    {"name": "alice", "score": 12},
    {"name": "andrew", "score": 20},
]

# Assertions
assert filter_dicts(test_data) == expected
assert filter_dicts([]) == []  # empty input
assert filter_dicts([{"name": "alex", "score": 11}]) == [{"name": "alex", "score": 11}]
assert filter_dicts([{"name": "alex", "score": 9}]) == []  # score too low
assert filter_dicts([{"name": "bob", "score": 20}]) == []  # name doesn't start with 'a'

print("All tests passed!")
