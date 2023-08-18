def twoArrays(k, A, B):
    # Write your code here
    n = len(A)
    A.sort()
    B.sort(reverse=True)
    for i in range(n):
        if A[i] + B[i] < k:
            return 'NO'
    return 'YES'
