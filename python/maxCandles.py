def birthdayCakeCandles(candles):
    # Write your code here
    maxN = max(candles)
    return candles.count(maxN)


def arrayManipulation(n, queries):
    # Create an array of zeros with an extra element for handling boundary conditions
    myArr = [0] * (n + 1)

    # Apply the difference array technique
    for q in queries:
        a, b, k = q
        myArr[a - 1] += k
        if b <= n:
            myArr[b] -= k

    # Calculate the prefix sum and find the maximum value
    max_value = 0
    current_value = 0
    for i in range(n):
        current_value += myArr[i]
        if current_value > max_value:
            max_value = current_value

    return max_value
