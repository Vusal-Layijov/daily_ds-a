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


def height(root):
    if root is None:
        return -1
    left=height(root.left)
    right=height(root.right)
    return 1+ max(left,right)