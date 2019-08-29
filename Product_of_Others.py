""" Given an array of integers,
return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""


def product_others(a, arr_size):
    p = 1
    for i in range(0, arr_size):
        p = p * a[i]
    product = [p // a[i] for i in range(0, arr_size)]
    return product

inp = [1, 8, 9, 5, 7]
print("Output: ", product_others(inp, len(inp)))
