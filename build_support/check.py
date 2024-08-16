import sys; import os; sys.path.append(os.path.abspath('py/src/'))


from pycpyc import string_size

some_string = "Hello"
expected = len(some_string)
actual = string_size(some_string)

assert expected == actual, f"Expected {expected}, got {actual} instead"

print("OK!")
