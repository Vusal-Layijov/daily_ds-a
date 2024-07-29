def pageCount(n, p):
    # Write your code here
    result = []
    if p == 1:
        return 0
    elif p == n:
        return 0

    count = 1
    if p < n/2:
        return p//2
    else:
        if n % 2 == 0:
            num = abs(p-n)
            if num > 0 and n-p in [1]:
                return 1+num//2
            else:
                return num//2
        else:
            num = abs(p-n)
            return num//2
def maxMin(k, arr):
    # Write your code here
    res=[]
    while k>0: 
        s=min(arr)
        arr.remove(s)
        res.append(s)
        k-=1
    return res[-1]-res[0]