def quicksort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[0]
    left=[]
    right=[]
    for ind in range(1,len(arr)):
        if arr[ind]<=pivot:
            left.append(arr[ind])
        else:
            right.append(arr[ind])
    leftsort=quicksort(arr)
    rightsort=quicksort(arr)
    return leftsort+[pivot]+rightsort