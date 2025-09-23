from collections import Counter

def top_n_words(words, n):
    """
    Returns a list of the top `n` most frequent words from the input list `words`.
    """
    counter = Counter(words)
    most_common = counter.most_common(n)
    words = list(map(lambda x: x[0], most_common))
    return words


# --- TESTS ---
words_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Test 1: top 1 word
assert top_n_words(words_list, 1) == ['apple'], "Test 1 failed"

# Test 2: top 2 words
assert set(top_n_words(words_list, 2)) == set(['apple', 'banana']), "Test 2 failed"

# Test 3: n larger than unique words
assert set(top_n_words(words_list, 10)) == set(['apple', 'banana', 'orange']), "Test 3 failed"

# Test 4: empty input
assert top_n_words([], 2) == [], "Test 4 failed"

# Test 5: ties
words_with_tie = ['a', 'b', 'c', 'a', 'b', 'c']
result = top_n_words(words_with_tie, 2)
assert set(result) <= set(['a', 'b', 'c']) and len(result) == 2, "Test 5 failed"

print('All tests passed')
