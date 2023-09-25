def maxSubarray(arr):
    # Write your code here
    maxx=arr[-1]
    for ind in range(-2,-len(arr)-1,-1):
        if maxx <0 and arr[ind]<0:
            maxx=max(arr[ind],maxx)
        else:
            maxx+=arr[ind]
            maxx=max(arr[ind],maxx)
        
        
    
    
    
    print(arr)
    subSeq=[]
    for num in arr:
        if num>0:
            subSeq.append(num)
    summ=sum(subSeq)
    if summ==0:
        summ=max(arr)
    return maxx,summ