#!/usr/bin/python3
#7. Tuples addition

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])

# Example usage:
tuple1 = (1, 2)
tuple2 = (3, 4)
result = add_tuple(tuple1, tuple2)
print(result)  # Output: (4, 6)
