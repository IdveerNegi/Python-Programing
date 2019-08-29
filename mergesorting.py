# Merge Sorting

def merge(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0) #current position of A and B
    while i+j < m+n:
        if j==n or A[i]<=B[j]:
            C.append(A[i])
            i=i+1
        elif i==m or A[i]>=B[j]:
            C.append(B[j])
            j=j+1
           
    return(C)

def mergesort(A,left,right):
    if right - left <=1:
        return(A[left:right])
    if right - left > 1:
        mid = (left+right)//2
        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)
        return (merge(L,R))
