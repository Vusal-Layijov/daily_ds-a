def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]  # Initialize n empty arrays
    lastAnswer = 0
    answers = []

    for query in queries:
        query_type, x, y = int(query[0]), int(query[1]), int(query[2])
        print(query_type, x, y)
        idx = (x ^ lastAnswer) % n  # Calculate index based on XOR operation
        if query_type == 1:
            arr[idx].append(y)
        elif query_type == 2:
            # Use modulo to get correct index
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers


def gridChallenge(grid):
    # Write your code here

    some = []
    for st in grid:
        new = list(st)
        nn = list(sorted(new))
        some.append(nn)
    print('sssss', some)
    for i in range(len(some)-1):
        for j in range(len(some[0])):
            if some[i+1][j] < some[i][j]:
                return 'NO'
    return 'YES'
