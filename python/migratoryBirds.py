def migratoryBirds(arr):
    # Write your code here
    obj = {}
    for num in arr:
        if num in obj:
            obj[num] += 1
        else:
            obj[num] = 1
    val = 0
    go = 0
    for k, v in obj.items():
        if v > val:
            go = k
            val = v
    return go
