def is_truthy(value):
  """
  Checks if a given value is truthy in Python.

  Args:
    value: The value to check.

  Returns:
    True if the value is truthy, False otherwise.
  """
  return bool(value)

# Examples of truthy values
print(f"1 is truthy: {is_truthy(1)}")
print(f"'hello' is truthy: {is_truthy('hello')}")
print(f"[1, 2, 3] is truthy: {is_truthy([1, 2, 3])}")
print(f"{{'a': 1}} is truthy: {is_truthy({'a': 1})}")
print(f"True is truthy: {is_truthy(True)}")

# Examples of falsy values
print(f"0 is truthy: {is_truthy(0)}")
print(f"'' is truthy: {is_truthy('')}")
print(f"[] is truthy: {is_truthy([])}")
print(f"{{}} is truthy: {is_truthy({})}")
print(f"None is truthy: {is_truthy(None)}")
print(f"False is truthy: {is_truthy(False)}")

int_attrs = dir(int)
filtered_int_attrs = list(filter(bool, int_attrs))

print(filtered_int_attrs)


