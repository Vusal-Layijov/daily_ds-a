def flippingMatrix(matrix):
    n = len(matrix) // 2

    for i in range(n):
        for j in range(n):
            max_val = max(
                matrix[i][j],
                matrix[i][2*n - j - 1],
                matrix[2*n - i - 1][j],
                matrix[2*n - i - 1][2*n - j - 1]
            )
            matrix[i][j] = max_val

    max_sum = sum(matrix[i][j] for i in range(n) for j in range(n))
    return max_sum
