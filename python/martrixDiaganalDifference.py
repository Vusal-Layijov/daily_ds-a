def diagonalDifference(arr):
    # Write your code here
    n, m = len(arr), len(arr[0])
    first = 0
    second = 0
    for ind in range(n):
        first += arr[ind][ind]
    for ind in range(n):
        second += arr[ind][m-ind-1]

    return abs(first-second)
