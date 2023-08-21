def sockMerchant(n, ar):
    # Write your code here
    myset = set()
    result = []
    count = 0
    for num in ar:
        if num in myset:
            continue
        togo = ar.count(num)
        result.append(togo)
        myset.add(num)
    for num in result:
        if num // 2 > 0:
            count += num // 2
    return count
