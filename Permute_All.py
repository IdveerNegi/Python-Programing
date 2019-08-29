"""Given a number in the form of a list of digits, return all possible permutations.
For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]"""


def permutations(arr, Left, right, output):
    """Function that returns all the permutation for a given list."""
    if Left == right:
        output.append(arr[:])

    for i in range(Left, right + 1):
        arr[i], arr[Left] = arr[Left], arr[i]
        permutations(arr, Left + 1, right, output)
        arr[i], arr[Left] = arr[Left], arr[i]         # {Backtrack}

    return output


arr = [1, 2, 3]
print(permutations(arr, 0, len(arr) - 1, []))
