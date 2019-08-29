"""Given an array and a permutation, apply the permutation to the array. For example,
given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"]."""

arr = list(map(str,input("\nEnter the list : ").split()))
p = list(map(int,input("\nEnter the list : ").split()))
out = []
for i in p:
    out.append(arr[i])
print(out)
