def maximizingXor(l, r):
    # Write your code here
    res=[]
    for i in range(l,r+1):
        for j in range(i,r+1):
            res.append(i^j)
    return max(res)