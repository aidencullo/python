import unittest
from combine import combine


class TestCombine(unittest.TestCase):
    """Test suite for combine function"""

    def test_combine_empty_arrays(self):
        """Test combining two empty arrays"""
        result = combine([], [])
        self.assertEqual(result, [])

    def test_combine_single_element(self):
        """Test combining arrays with single element"""
        array1 = [{"id": 1, "name": "Alice"}]
        array2 = [{"age": 30}]
        expected = [{"id": 1, "name": "Alice", "age": 30}]
        self.assertEqual(combine(array1, array2), expected)

    def test_combine_multiple_elements(self):
        """Test combining arrays with multiple elements"""
        array1 = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"}
        ]
        array2 = [
            {"age": 30},
            {"age": 25},
            {"age": 35}
        ]
        expected = [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25},
            {"id": 3, "name": "Charlie", "age": 35}
        ]
        self.assertEqual(combine(array1, array2), expected)

    def test_combine_overlapping_keys(self):
        """Test combining dicts with overlapping keys (array2 overwrites)"""
        array1 = [{"id": 1, "value": "first"}]
        array2 = [{"value": "second"}]
        expected = [{"id": 1, "value": "second"}]
        self.assertEqual(combine(array1, array2), expected)

    def test_combine_multiple_keys_per_dict(self):
        """Test combining dicts with multiple keys"""
        array1 = [
            {"id": 1, "name": "Alice", "department": "Engineering"},
            {"id": 2, "name": "Bob", "department": "Sales"}
        ]
        array2 = [
            {"age": 30, "salary": 100000},
            {"age": 25, "salary": 80000}
        ]
        expected = [
            {"id": 1, "name": "Alice", "department": "Engineering", "age": 30, "salary": 100000},
            {"id": 2, "name": "Bob", "department": "Sales", "age": 25, "salary": 80000}
        ]
        self.assertEqual(combine(array1, array2), expected)


if __name__ == "__main__":
    unittest.main()
