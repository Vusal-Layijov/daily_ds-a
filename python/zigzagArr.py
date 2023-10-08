def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)//2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while (st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for ind in range(len(nums)):
            leftSum = sum(nums[:ind])
            rightSum = sum(nums[ind+1:])
            if leftSum == rightSum:
                return ind
        return -1
