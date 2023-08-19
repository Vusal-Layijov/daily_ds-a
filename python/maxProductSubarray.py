def maxProduct(nums):
    res = max(nums)
    curMin,curMax=1,1
    for n in nums:
        if n==0:
            curMin,curMax=1,1
            continue
        tmp=curMax*n
        curMax = max(curMax*n,n*curMin,n)
        curMin=min(curMin*n,tmp,n)
        res=max(res,curMax)
    return res
            